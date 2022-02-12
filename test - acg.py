
from pprint import pprint
import fwOper as fw

file1 = 'c:/users/al202t/desktop/data/mk-S-5515irf-1.log'
file2 = 'c:/users/al202t/desktop/data/d4z-vfw-iiw-bgym-admin.log'

file = file1
# file = file2

with open(file, 'r') as f:
	flst = f.readlines()

insts = fw.get_object(fw.Instances, conf_list=flst)
insts1 = fw.get_object(fw.Instances, conf_list=flst)


amem = "1.1.1.1 255.255.255.255"
bmem = "10.0.0.0 255.0.0.0"
setofmems = {"1.1.1.0 255.255.255.0", "2.2.2.2 255.255.255.255"}

# ==================================================================================

# ==============================================================================
# print(insts)
# print(insts.system.routes[3].network)
# ==============================================================================

# ################# -------- OBJ GRP USAGE --------- #############################
# acls = insts.system.acls
# grps = insts.system.obj_grps
# grp = grps.CUSTOM
# grps = insts.system.obj_grps
# grp1 = grps['Blue-9']

# print(grps)			# set of object groups name
# print(grp)			# full object group
# print(grp.keys())		# object group MEMBER_TYPES ex: network-object, port-object...
# print(grp.values())	# object group MEMBERs ex: address, ports, objgrp refereance...
# print(len(grp1))		# count of members.
# print(grp.description)	# object group description
# print(grp['network-object'])	# set of members of given member type.
# print(grp.add(amem))				# add a member
# print(grp.add(setofmems))		# add set of members
# print(grp.delete(bmem))			# remove a member
# print(grp.delete(setofmems))		# remove set of members
# print(grp > grp1)				# difference in two group members
# print(grp < grp1)				# difference in two group members
# print(bmem in grp)				# bool: member found in group
# print(grp == grp1)				# bool: checks equality of two groups
# print(grp.over(acls))			# check for acl entries containing group.
# print(grp1.has(grp))			# check for grp1 members containing grp.


# ---- Other alternate ways ---- 
# grp += amem			# == add()
# grp += setofmems		# == add()
# grp -= bmem			# == delete()
# grp -= setofmems		# == delete()
# grp1 = grp - bmem			# creating a new group / copy-delete()
# grp1 = grp + setofmems	# creating a new group / copy+add()

# ---- Return changes strings for a group ---- 
# print(grp.add_str())	# members addition string
# print(grp.del_str())	# deleted members string (negates).

# ---- Return change strings for all groups ---- 
# print(grps.changes('adds'))
# print(grps.changes('removals'))




"""
item_k = 'source'
item_v = {'1.1.1.1', '1.1.1.2', '1.1.1.3',}
grps = insts['Green-Xpt'].obj_grps
grp = grps.SRC


temp_item_v_grp = fw.OBJ('temporary', 1)
if item_k in ('protocol',):rdk = 'protocol-object'
if item_k in ('ports',):rdk = 'port-object'
if item_k in ('source', 'destination'): rdk = 'network-object'
ogd = {}
ogd['candiates_list'] = ''
ogd['type'] = grp.obj_grp_type
ogd['svc_filter'] = grp.obj_grp_svc_filter
temp_item_v_grp.set_instance_primary_details(ogd)
temp_item_v_grp._repr_dic[rdk] = item_v
# print(temp_item_v_grp)
# print(grp)
# print(temp_item_v_grp > grp)
# print(grp > temp_item_v_grp)
print(grp != temp_item_v_grp)"""


