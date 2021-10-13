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


# ==================================================================================

if file == file1:
# if file == file2:

	# ==============================================================================
	# print(insts)			# set of instances
	# print(insts.system.routes[3].network)
	# ==============================================================================

	# ################# -------- ACL USAGE --------- #############################
	acls = insts.system.acls
	acl = acls.al_PERMIT_IN

	acl.sequence = True 	# sequence numbering enable/disable (default=disable
	# print(acls)			# set of acls
	# print(acl)			# full acl
	# print(acl.min, acl.max)	# least, max acl sequences.
	# print(acl[8:13])		# get range of acl lines
	# print(acl.insert(10, new))	# insert new entry at position (10)
	# print(acl.append(new))		# append new entry
	# print(acl.delete(200, 210,2))	# delete an entry at position (10) #### (TBD)
	# print(acl.delete(old))  		# delete an entry for matching attributes (old) #### (TBD)
	# print(acl1 > acl)		# acl1 entries missing in acl, diff in two acls
	# print(acl1 < acl)		# acl entries missing in acl1, diff in two acls
	# print( acl == acl1 )	# bool: compare two acls
	# print(old in acl)		# bool: entry found in acl

	# ---- Other optional ways ---- 
	# ---- be careful on implementatin steps if seq number used for below ----
	# acl += new 			#  == append()
	# acl1 = acl + new		#  == return updated object with append()
	# del(acl[210:212])		#  == delete() with range of lines
	# acl -= old			#  == delete(attr)
	# acl -= 10				#  == delete(n)
	# acl1 = acl - old		#  == return updated object with delete(attr)
	# acl1 = acl - 10		#  == return updated object with delete(n)
	# print(acl.removals)	#  deleted entries


	# print(acl)			# full acl

	# ################# -------- ACLs USAGE --------- #############################
	# print(acls.changes("adds"))			# get additions for all ACLs
	# print(acls.changes("removals"))		# get removals for all ACLs



