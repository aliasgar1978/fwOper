
Sample Execution Steps!
============================================

Here below is the sample code from my desk, alter it as per your need to get the desired result. 


.. code:: pyhon

	# ------------------------------------------------------------------------------
	# Imports
	# ------------------------------------------------------------------------------
	import os
	import pandas as pd
	from collections import OrderedDict
	from pprint import pprint
	import fwOper



	#  sample DATABASE request.xlsx FORMAT
	# ------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
	# |request_type|firewall_name|firewall_instance|acl_name|action|source|destination|protocol|ports|remark|insert_at|source_grp|destination_grp|ports_grp|protocol_grp|
	# ------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


	# ------------------------------------------------------------------------------
	#  global vars
	# ------------------------------------------------------------------------------

	REQUEST_TYPES = ('del', 'add')
	GROUPBY_SEQUENCE = ['request_type', 'firewall_name', 'firewall_instance', 'acl_name']

	# ------------------------------------------------------------------------------
	#                               FUNCTIONS
	# ------------------------------------------------------------------------------

	def get_file_name(folder, hostname):
		"""file name for the given hostname in folder
		assumed that firewall logs are stored with hostname as filename

		Args:
			folder (str): Folder path
			hostname (str): hostname

		Returns:
			str: filename containing hostname in given folder.
		"""
		for file in os.listdir(folder):
			if file.lower().find(hostname.lower()) > -1: 
				return file


	def filter_request(request):
		"""filters request dictionary for the mentioned fields only

		Args:
			request (dict): input request attributes 

		Returns:
			dict: filtered request attributes
		"""
		fields = {'source', 'destination', 'protocol', 'ports', 'action', 'remark', 'insert_at'}
		return {field: request[field] for field in fields if request[field]}


	def execute_req(req_type, Firewalls, req_grp):
		"""Excute the ACL Change request

		Args:
			req_type (str): request type (either 'add', 'del')
			Firewalls (dict): Firewall objects dictionary
			req_grp (dict): grouped input requests

		Returns:
			s: delta change for the execution of request
		"""
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# ~~~~ go sequencial on REQUEST_TYPES ('del', 'add') ~~~~
		if req_grp['request_grp']['request_type'] != req_type: return ''
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# ~~~~ set group request variable ~~~~
		grp_request = req_grp['req_grp']
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# ~~~~ set fw parameters/variables ~~~~
		fw = Firewalls[req_grp['request_grp']['firewall_name']]
		fw_inst = fw.instances[req_grp['request_grp']['firewall_instance']]
		acl = fw_inst.acls[req_grp['request_grp']['acl_name']]
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		# ~~~~ execute request based on request type ~~~~
		if req_type == 'del':  return execute_del_req(acl, grp_request)
		if req_type == 'add':  return execute_add_req(acl, grp_request)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def execute_del_req(acl, grp_request):
		"""execution of grouped delete requests

		Args:
			acl (ACL): access-list object
			grp_request (list): grouped input request attributes to be deleted on given ACL

		Returns:
			str: delta change(s) for given delete request
		"""
		### here some where group check will get insert ### [TBD]
		acl.sequence = False										# Enable if require sequence number in delta output
		s = ''
		for gr in grp_request:
			s += acl.delete(gr)
		return s

		
	def execute_add_req(acl, grp_request):
		"""execution of grouped add/insert requests
		'insert_at'-attribute needed per request for inserting, otherwise request will be considered as add(append).

		Args:
			acl (ACL): access-list object
			grp_request (list): grouped input request attributes to be added/inserted on given ACL

		Returns:
			str: delta change(s) for given add/insert request
		"""
		acl.sequence = True
		s = ''
		for gr in grp_request:
			if gr.get('insert_at'):
				n = int(gr['insert_at'])
				del(gr['insert_at'])
				s += acl.insert(n, gr)
			else:
				s += acl.append(gr)
		return s



	def check_exact_group()
		source_grp=fwOper.NetworkObject()
		item = 'destination'
		values = set()
		for gr in grp_request:
			values.add(gr['destination'])
		dum_grp = fwOper.dummy_group(source_grp, item, values)



	# ------------------------------------------------------------------------------
	#                                  CLASSES
	# ------------------------------------------------------------------------------

	# ------------------------------------------------------------------------------
	# REQUEST Parameters
	# ------------------------------------------------------------------------------
	class Request():
		"""Firewall change request (Excel) method, properties, exections 
		"""

		def __init__(self, request_input_file, sheet_name='Sheet1'):
			"""provide excel input file

			Args:
				request_input_file (str): input request file
			"""
			self.request_input_file = request_input_file
			self.get_dataframe(sheet_name)

		def get_dataframe(self, sheet_name):
			"""creates data frame (requests), and firewalls name-list in the requests
			"""
			self.requests = pd.read_excel(self.request_input_file, sheet_name=sheet_name).fillna("")
			self.firewalls = self.requests.firewall_name.unique()
			self.requests = self.requests.groupby( GROUPBY_SEQUENCE )

		def group_members(self, group):
			"""convert the grouping members in dictionary format ( from tuples (group, df) ),
			also updaets missing firewall_instance with default 'system'.

			Args:
				group (dict of tulpes): group members

			Returns:
				dict: grouping members
			"""
			members = {}
			for i, gm in enumerate(GROUPBY_SEQUENCE):
				if gm == 'firewall_instance' and group[0][i] == '':
					members[gm] = 'system'
				else:
					members[gm] = group[0][i]
			return members

		def create_request_group(self, df):
			"""create the requests list based on group

			Args:
				df (pandas.DataFrame): filtered (member) DataFrame to create a list of group request

			Returns:
				list: input requests
			"""
			req_grp = []
			d = df.T.to_dict()
			for i, req in d.items():
				req_grp.append(filter_request(req))
			return req_grp

		def gen_request_id_groups(self):
			"""group input request and get the grouped request format= {id:req_grp_dict}

			Returns:
				dict: grouped request
			"""
			request_id_grp = {}
			for i, group in enumerate(self.requests):
				request_grp = self.group_members(group)			# get request type
				request_df = group[1]
				req_grp = self.create_request_group(request_df)	# get group of requests.
				request_id_grp[i] = {'request_grp':request_grp, 'req_grp':req_grp}
			return request_id_grp

	# ------------------------------------------------------------------------------
	# Firewall Object
	# ------------------------------------------------------------------------------
	class Firewall(object):
		"""A Firewall object

		Args:
			object (object): default
		"""

		def __init__(self, folder, firewall):
			"""provide folder and firewall name for which Firewall object to be created

			attributes:
				instances: instances of the firewall

			Args:
				folder (str): folder path where config backup stored
				firewall (str): firewall name with which backup is stored
			"""
			file = get_file_name(folder, firewall)
			self.read(folder, file)

		def read(self, folder, file):
			"""reads firewall configuration file from provided folder.

			Raises:
				Exception: MissingInput

			Args:
				folder (str): where configuration files stored
				file (str): filename of config file
			"""
			try:
				with open(folder+file, 'r') as f:
					fw_lst = f.readlines()
					self.instances = fwOper.get_object(fwOper.Instances, conf_list=fw_lst)
			except:
				Exception(f"MissingInput{folder+file}")


	# ------------------------------------------------------------------------------
	# EXECUTION
	# ------------------------------------------------------------------------------
	if __name__ == '__main__':
		pass
	# ------------------------------------------------------------------------------

		############## WAY OF EXECUTION ##############

		# STEP1: Provide Inputs ----------------------------------------------
		file = 'request.xlsx'
		firewall_backup_folder = '/path_to_firewall_backup_folder/'

		# STEP2: Initialize Request and Firewall inputs ----------------------
		Req = Request(file)
		rigs = Req.gen_request_id_groups()
		Firewalls = {fw: Firewall(firewall_backup_folder, fw) for fw in Req.firewalls}

		# STEP3: Iterate thru requests ---------------------------------------
		for req_type in REQUEST_TYPES:	# default (first='del', second='add') 
			for i, req_id_grp in rigs.items():
				pass
				s = execute_req(req_type, Firewalls, req_id_grp)
				if s: print(s)			# This is delta output



		fw = 'testfw'					# provide FW Name to see update
		print(Firewalls[fw].instances.system.acls.al_PERMIT_I)	# This is updated ACL

	# ------------------------------------------------------------------------------


**Thank You!**
