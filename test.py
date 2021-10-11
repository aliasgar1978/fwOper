from pprint import pprint
import fwOper as fw

file1 = 'c:/users/al202t/desktop/data/mk-S-5515irf-1 sh run.log'
file2 = 'c:/users/al202t/desktop/data/d4z-vfw-iiw-bgym-admin.log'

file = file1
# file = file2

with open(file, 'r') as f:
	flst = f.readlines()

insts = fw.get_object(fw.Instances, conf_list=flst)
insts1 = fw.get_object(fw.Instances, conf_list=flst)

new = {
	'acl_type': 'extended', 
	'action': 'permit', 
	'protocol': 'tcp', 
	'source': '10.10.10.0 255.255.255.0',
	'destination': 'host 2.2.2.2',
	'ports': 'eq 2222',
	'log_warning': True,
	'remark': 'adfadfs',
	}

old = {
	'action': 'permit', 
	'protocol': 'tcp', 
	'source': '158.98.23.194 255.255.255.255',
	'destination': 'host 210.89.6.101',
	'ports': 'eq 22',
}

amem = "1.1.1.1 255.255.255.255"
bmem = "10.0.0.0 255.0.0.0"
setofmems = {"1.1.1.0 255.255.255.0", "2.2.2.2 255.255.255.255"}

if file == file1:
	# print(insts.system)
	# print(insts.system.routes[3].network)

	# ################# -------- OBJ GRP USAGE --------- #############################
	grps = insts.system.obj_grps
	grp = grps.CUSTOM
	# grps1 = insts1.system.obj_grps
	# grp1 = grps1.CUSTOM

	# print(grps)			# see of all object group name
	# print(grp)			# matter of object group
	# print(grp.keys())		# object group MEMBER_TYPES ex: network-object, port-object...
	# print(grp.values())	# object group MEMBERs ex: address, ports, objgrp refereance...
	# print(grp.description)	# object group description
	# print(grp['network-object'])	# set of members of given member type.

	# add a member / set of memers to given member type.
	# grp += amem			# WAY1
	# grp += setofmems		# WAY1
	# grp.add(amem)			# WAY2
	# grp.add(setofmems)		# WAY2
	# print(grp.add_str())	# set of members for adds in group.

	# Delete a member / set of memers to given member type.
	# grp -= bmem			# Way1
	# grp -= setofmems		# Way1
	# grp.delete(amem)			# Way2
	# grp.delete(setofmems)		# Way2
	# print(grp.del_str())	# set of members for deletes in group.
	# print(grp)

	# grp1 = grp + setofmems			# creating a new group / copy+add
	# grp1 = grp - bmem					# creating a new group / copy-remove
	# print(grp1)

	# comparision
	# print(grp > grp1)				# difference in two groups
	# print(grp < grp1)				# difference in two groups

	# group has something ?
	# print(bmem in grp)				# boolean check for an item in grp


	# ################# -------- ACL USAGE --------- #############################
	acl = insts.system.acls.al_PERMIT_IN
	# # --- set sequence numbering in output/ display full/set of acl
	# acl.sequence = True
	# print(acl[8:13])

	# # --- insert a new entery at position / display range of acl
	# acl.insert(10, new)
	# print(acl[8:13])

	# # --- append a new entery at last / display range of acl
	# acl.append(new)
	# acl += new
	# acl1 = acl + old			# return a new acl (acl1)
	# print(acl[-2:])

	# # --- delete an entery from position(s) / display updated range of acl / removals
	# del(acl[9:11])
	# acl -= old			## remove by attribute match
	# acl -= 10				## remove by sequence number
	# acl1 = acl - old		# return a new acl (acl1) ## remove by attribute match
	# acl1 = acl - 10		# return a new acl (acl1) ## remove by sequence number
	# print(acl[8:13])
	# print(acl.removals)	# deleted entries

	# # --- create new copy and append an entery at last
	# acl1 = acl - 10
	# acl1+=new
	# acl1-=old
	# acl1 -= 10
	# print(acl1)

	# comparision
	# print(acl1 > acl)				# difference in two groups
	# print(acl1 < acl)				# difference in two groups

# if file == file2:
# 	print(insts.admin)
	# print(insts['Blue-Green'].routes)
	# print(insts['Blue-Green'].obj_grps.Local_DNS_Prod_wifi['network-object'])
	# print(insts['Blue-Green'].acls.al_from_blue[2])

# rts = insts.admin.routes
# pfx = '178.98.101.0/24'
# pfx = '9.98.101.0/24'
# # pfx = '129.39.115.0/24'
# print(rts)
# print(rts.prefix(pfx))
# print(pfx in rts)
# print(rts.prefix(pfx).ifdesc)
# print(rts.prefix(pfx).route_line)



