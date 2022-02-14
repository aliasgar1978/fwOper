fw_Oper.acl User documentation!
============================================


Cisco Firewall Access-Lists - How To ?
----------------------------------------

Use the acl module of fw_oper package to get the necessary changes for the ACL 
on Cisco Firewall.


.. Tip::
	Build your own script in order to get the change delta script generated using this package.

	**High-level steps:**

		#. Make a firewall change request excel, csv sheet. read it thru Pandas or other package.
		#. Read thru each add/del request.
		#. Convert request to dictionary format as required by this package.
		#. Execute appropriate request on eligible ACL.
		#. At last get the delta changes.

	**See Also:** Sample Execution Steps!



High-level Overview 
----------------------------

	#. Define inputs
	#. Import package, modules
	#. select firewall, acls, acl Objects
	#. Operate and View acl


Detailed How To
--------------------

	#. Define inputs::

		file = 'running-config log captuerd file for fw.log'	# fw log

		new_entry_to_add = {		# acl detail to add
			'acl_type': 'extended', 
			'action': 'permit', 
			'protocol': 'tcp', 
			'source': '10.10.10.0 255.255.255.0',
			'destination': 'host 2.2.2.2',
			'ports': 'eq 2222',
			'log_warning': True,
			'remark': 'Remark if any',
		}

		old_entry_to_del = {	# acl detail to del
			'action': 'permit', 
			'protocol': 'tcp', 
			'source': '158.98.23.194 255.255.255.255',
			'destination': 'host 210.89.6.101',
			'ports': 'eq ssh',		
		}



	#. Import necessary package/modules::

		import fwOper as fw

	#. Create Firewall Object::

		with open(file, 'r') as f:
			flst = f.readlines()

		insts = fw.get_object(fw.Instances, conf_list=flst)
		print(insts)			# set of instances


	#. Refereance to Instance Access-lists (set of ALCs)

		.. code:: python

			acls = insts['instance_name'].acls
			acls = insts.instance_name.acls
			print(acls)			# set of acls

		*instance_name* can be accepted in either **bracket** or **dotted** format. 
		Use of bracket format is must if space/special characters involved in *instance_name*.

	#. Select an ACL from set of ACLS

		.. code:: python

			acl = acls['acl_name']
			acl = acls.acl_name

		*acl_name* can be accepted in either **bracket** or **dotted** format. 
		Use of bracket format is must if space/special characters involved in *acl_name*.

	#. Set ACL Numbering enable/disable on given acl::

		acl.sequence = True 	# set sequence numbering enabled (default=disable)

	#. Operations on ACL

		#. acl views, properties::

			print(acl)			# full acl
			print(acl[8:13])		# get range of acl lines
			print(acl.min, acl.max)		# least & maximm acl sequence number.

		#. add::

			acl1 = acl + new_entry_to_add 	# append new entry, create a new ACL
			acl += new_entry_to_add		# append new entry, same acl
			print(acl.append(new))		# same as above.

		#. delete::

			acl1 = acl - old_entry_to_del 	# create a new ACL by deleting an old entry.
			acl -= old_entry_to_del		# delete an old entry from existing ACL.
			print(acl.delete(old_entry_to_del))  # same as above
			acl1 = acl - 10			#  delete acl sequence number `10`
			print(acl.delete(10))		# same as above
			del(acl[210:212])		# delete range of lines from acl.
			print(acl.delete(200, 210, 2))	# delete range of lines from acl, with jump step.
			print(acl.removals)		# verify, get - deleted entries


		#. insert::

			print(acl.insert(10, new))	# insert new entry at position (10)

		#. verifications::

			print(old_entry_to_del in acl)	# bool: entry found in acl
			print(acl.contains(old_entry_to_del))# set: of line numbers containing attributes (sparse matche).
			print(acl.exact(old) )		# set: of line numbers matching attributes (exact matches)

		#. comparisions::

			acl1 = acls.another_acl_name	# select another ACL
			print(acl > acl1)		# acl1 entries missing in acl, diff in two acls
			print(acl < acl1)		# acl entries missing in acl1, diff in two acls
			print( acl == acl1 )		# bool: compare two acls / (exact match)
			print(acl.difference(acl1))	# differences: from acl to acl1
			print(acl1.same_elements(acl))	# bool: compare two acl elements == (sparse match)

		#. get delta::

			print(acls.changes("adds"))	# get additions for all ACLs after apply changes
			print(acls.changes("removals"))	# get removals for all ACLs after apply changes


.. Warning::
	Be extra careful on implementatin steps if sequence numbering used.

Extra Nuggets
--------------------

* In delta modification dictionary, ``source`` and ``destinations`` accepts all three variants of **addressing format**.  And no-mask will consider it as host entry.
	#. 10.10.10.1 255.255.255.255
	#. host 10.10.10.1
	#. 10.10.10.1/32

* Multiple ``source`` and/or ``destinations`` can be supplied in sets, as below.
	* 'source': {'1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4'}
	* 'destination': {'2.1.1.1', '2.1.1.2', '2.1.1.3', '2.1.1.4'},
