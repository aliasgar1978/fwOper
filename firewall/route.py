
# ----------------------------------------------------------------------------------------
from nettoolkit import *

from .common import Singulars
# ----------------------------------------------------------------------------------------
def routes_list(config_list):
	"""list of lines with static routes from given config-list
	"""
	return [line.rstrip() for line in config_list if line.startswith("route ")]
def interface_group_list(config_list):
	"""extracts access-group from provided configuration list
	"""
	return [line.rstrip() for line in config_list if line.startswith("access-group ")]

# ----------------------------------------------------------------------------------------
# Static Route Entries
# ----------------------------------------------------------------------------------------
class ROUTES():
	"""collection of ROUTE objects
	:: Instance variables ::
	cfg_routes_list: list of routes
	cfg_interface_group_list: list of interface access-groups
	routes_list: list of ROUTE objects
	"""
	def __init__(self, config_list):
		self.cfg_routes_list = routes_list(config_list)
		self.cfg_interface_group_list = interface_group_list(config_list)
		self.routes_list = []
		self.get_route_objects()
	def __iter__(self):
		for item in self.routes_list: yield item
	def __getitem__(self, item):
		try:
			return self.routes_list[item]
		except:
			return None
	def __getattr__(self, attr): return self[attr]
	def __len__(self): return len(self.routes_list)
	def __contains__(self, network): return self.prefix(network)

	# ~~~~~~~~~~~~~~~~~~ CALLABLE ~~~~~~~~~~~~~~~~~~

	def prefix(self, network):
		"""check matching network in ROUTES object, return matching route
		"""
		route_match = None
		for sn in reversed(self):
			if network in sn:
				route_match = sn
				break
		if route_match: return route_match

	def get_route_objects(self):
		"""set ROUTE objects in self instance
		"""
		for route_line in self.cfg_routes_list:
			route =  ROUTE(route_line)
			route.parse()
			# route.parse_group(self.cfg_interface_group_list)	# customer specific to be remove
			self.routes_list.append(route)


# ----------------------------------------------------------------------------------------
# Static Route Details
# ----------------------------------------------------------------------------------------
class ROUTE(Singulars):
	"""Individual static-route object

	:: Instance variables ::
	route_line: static route line
	_repr_dic: static route attribute dictionary
	network: network/subnet for given route
	next_hop: next-hop value for given route
	distance: administrative distance value for given route
	interface_desc: description of route
	remark:  mathing access-list

	"""
	def __init__(self, route_line):
		super().__init__()
		self.route_line = route_line

	def __contains__(self, network): return isSubset(network, self.network)


	# ~~~~~~~~~~~~~~~~~~ CALLABLE ~~~~~~~~~~~~~~~~~~

	def parse(self):
		"""parse static route line and set route_dict
		"""
		spl_route_line = self.route_line.split()
		self.interface_desc = spl_route_line[1]
		self.next_hop = spl_route_line[4]
		try: self.distance = int(spl_route_line[5])
		except: self.distance = 1
		mask = to_dec_mask(spl_route_line[3])
		self.network = addressing(spl_route_line[2]+"/"+str(mask))

	def parse_group(self, cfg_interface_group_list):
		"""parse interface group list to get interface name-remark
		custom ---> to be moved to custom project
		"""
		self.remark = ""
		for grp_line in cfg_interface_group_list:
			spl_grp_line = grp_line.strip().split()
			if spl_grp_line[-1] == self.interface_desc:
				self.remark = spl_grp_line[1]
				break
		if not self.remark and cfg_interface_group_list:
			print(f"ACLNameundetected: {cfg_interface_group_list}")

# ------------------------------------------------------------------------------ #
if __name__=="__main__":
	pass
# ------------------------------------------------------------------------------ #
