
from pprint import pprint
import fwOper as fw

file1 = 'c:/users/al202t/desktop/data/mk-S-5515irf-1 sh run.log'
file2 = 'c:/users/al202t/desktop/data/d4z-vfw-iiw-bgym-admin.log'

file = file1
file = file2

with open(file, 'r') as f:
	flst = f.readlines()

insts = fw.get_object(fw.Instances, conf_list=flst)
insts1 = fw.get_object(fw.Instances, conf_list=flst)

pfx1 = '178.98.101.0/24'
pfx2 = '9.98.101.0/24'
pfx3 = '129.39.115.0/24'

# ==================================================================================

if file == file1:
# if file == file2:

	# ==============================================================================
	# print(insts)
	# print(insts.system.routes[3].network)
	# ==============================================================================

	# ################# -------- ROUTES USAGE --------- #############################
	routes = insts.system.routes

	# print(routes)							# all routes
	# print(pfx1 in routes)					# bool: is prefix match any route.
	# print(routes.prefix(pfx2))			# matching route for given prefix (pfx2)
	# print(routes.prefix(pfx2).ifdesc)		# route description for matching route
	# print(routes.prefix(pfx2).route_line)	# string prop ( object work without it )

	print(dir(routes))
	print( routes )


# ==================================================================================
