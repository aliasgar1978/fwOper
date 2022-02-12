
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
	'ports': 'eq ssh',
}



old1 = {
	'action': 'permit', 
	'protocol': 'tcp', 
	'source': '1.1.1.1',
	# 'source': {'1.1.1.1', '1.1.1.2', '1.1.1.3',},
	'source': {'1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4'},
	# 'destination': '2.1.1.0 255.255.255.0',
	'destination': '2.1.1.1',
	# 'destination': {'2.1.1.1', '2.1.1.2', '2.1.1.3',},
	'destination': {'2.1.1.1', '2.1.1.2', '2.1.1.3', '2.1.1.4'},
	'ports': 'eq snmp',
}


old2 = {
	'action': 'permit', 
	'protocol': 'tcp', 
	'source': '129.39.125.175',
	'destination': '210.89.6.105',
	'ports': 'eq ssh',
}

# ==============================================================================
# print(insts)			# set of instances
# print(insts.system.routes[3].network)
# ==============================================================================
from copy import copy, deepcopy

acls = insts.system.acls
# acl = insts.system.acls.al_TEST
acl = insts.system.acls.al_PERMIT_I

acl1 = acl + new
# acl1 += copy(old)

acl.sequence = True 	# sequence numbering enable/disable (default=disable
acl1.sequence = True 	# sequence numbering enable/disable (default=disable
print(acl)
print(acl1)
# print(">", acl1.difference(acl))

# ==============================================================================
# ################# -------- ACL USAGE --------- #############################
# ==============================================================================
# acl.sequence = True 			# sequence numbering enable/disable (default=disable
# print(acls)					# set of acls
# print(acl)					# full acl
# print(acl.min, acl.max)		# least, max acl sequences.
# print(acl[8:13])				# get range of acl lines
# print(acl.insert(10, new))	# insert new entry at position (10)
# print(acl.append(new))		# append new entry
# print(acl.delete(200, 210,2))	# delete an entry at position (10)
# print(acl.delete(old))  		# delete an entry for matching attributes (old)
# print(acl > acl1)				# acl1 entries missing in acl, diff in two acls
# print(acl < acl1)				# acl entries missing in acl1, diff in two acls
# print( acl == acl1 )			# bool: compare two acls / (exact match)
# print(acl.difference(acl1))	# differences from acl to acl1
# print(acl1.same_elements(acl))# bool: compare two acl elements == (sparse match)
# print(old in acl)				# bool: entry found in acl ( same as: acl.contains(old) )
# print(acl.contains(old))		# set: of line numbers containing attributes (sparse matches, ex: matching object group containing attribs)
# print(acl.exact(old) )		# set: of line numbers matching attributes (exact matches, ex: matching exact object group)

# ==============================================================================
# ---- Other optional ways ---- 
# ---- be careful on implementatin steps if seq number used for below ----
# ==============================================================================
# acl += new 			#  == append()
# acl1 = acl + new		#  == return updated object with append()
# del(acl[210:212])		#  == delete() with range of lines
# acl -= old			#  == delete(attr)
# acl -= 10				#  == delete(n)
# acl1 = acl - old		#  == return updated object with delete(attr)
# acl1 = acl - 10		#  == return updated object with delete(n)
# print(acl.removals)	#  deleted entries
# ==============================================================================



# ==============================================================================
# ################# -------- ACLs USAGE --------- #############################
# ==============================================================================
# print(acls.changes("adds"))			# get additions for all ACLs
# print(acls.changes("removals"))		# get removals for all ACLs
# ==============================================================================




