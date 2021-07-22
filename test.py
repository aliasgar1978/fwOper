
import firewall as fw

file1 = 'c:/users/al202t/desktop/mk-S-5515irf-1 sh run.log'
file2 = 'c:/users/al202t/desktop/d4z-vfw-iiw-bgym-admin.log'

file = file1

with open(file, 'r') as f:
	flst = f.readlines()

insts = fw.get_object(fw.INSTANCES, conf_list=flst)

if file == file1:
	print(insts.system.keys())
	print(insts.system.obj_grps['maintenance-MAXIMO']['port-object'] )
	print(insts.system.acls.al_PERMIT_IN.keys())
	print(insts.system.routes)

if file == file2:
	print(insts['Blue-Green'].keys())
	print(insts['Blue-Green'].routes)
	print(insts['Blue-Green'].obj_grps.Local_DNS_Prod_wifi['network-object'])
	print(insts['Blue-Green'].acls.al_from_blue[2])

# pfx = '178.98.101.0/24'
# pfx = '9.98.101.0/24'
# pfx = '129.39.115.0/24'
# print(rts)
# print(dir(rts.prefix(pfx)))
# print(pfx in rts)
# print(rts.prefix(pfx).remark)
# print(rts.prefix(pfx).route_line)




