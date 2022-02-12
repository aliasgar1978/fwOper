fw_Oper.acg User documentation!
============================================

Cisco Firewall Object Groups - How To ?
-----------------------------------------

Use the acg module of fw_oper package to get the necessary changes for the Object Groups
on Cisco Firewall.

acg stands for Access Control Group (object-group)


.. Tip::
	Build your own script in order to get the change delta script generated using this package.

	**High-level steps:**

		#. Make a firewall change request excel, csv sheet. read it thru Pandas or other package.
		#. Read thru each add/del request.
		#. Convert request to dictionary format as required by this package.
		#. Find eligible Object Group that requires changes.
		#. Execute appropriate change request on eligible Object Group.
		#. At last get the delta changes.



High-level Overview 
----------------------------

	#. Define inputs
	#. Import package, modules
	#. select firewall, acgs, acg Objects
	#. Operate and View group/changes


Detailed How To
--------------------

	#. Define inputs::

		file = 'running-config log captuerd file for fw.log'	# fw log

		a_member = "1.1.1.1 255.255.255.255"
		setof_members = {"1.1.1.0 255.255.255.0", "2.2.2.2 255.255.255.255"}


	#. Import necessary package/modules::

		import fwOper as fw

	#. Create Firewall Object::

		with open(file, 'r') as f:
			flst = f.readlines()

		insts = fw.get_object(fw.Instances, conf_list=flst)
		print(insts)			# set of instances

	#. Refereance to Instance to object-group (set of object-groups)

		.. code:: python

			grps = insts['instance_name'].obj_grps
			grps = insts.instance_name.obj_grps
			print(grps)			# set of obj_grps

		*instance_name* can be accepted in either **bracket** or **dotted** format. 
		Use of bracket format is must if space/special characters involved in *instance_name*.

	#. Select an object-group from set of object-groups

		.. code:: python

			grp = grps['group_name']
			grp = grps.group_name

		*group_name* can be accepted in either **bracket** or **dotted** format. 
		Use of bracket format is must if space/special characters involved in *group_name*.

	#. Operations on object-group

		#. object-group views, properties::

			print(grp)		# full object-group
			print(grp.keys())	# object group MEMBER_TYPES ex: network-object, port-object...
			print(grp.values())	# object group MEMBERs ex: address, ports, objgrp refereance...
			print(len(grp1))	# count of members.
			print(grp.description)	# object group description
			print(grp['network-object'])	# set of members of given member type.


		#. add::

			print(grp.add(a_member))	# add a member to group, inline
			grp += a_member			# same as above
			print(grp.add(setof_members))	# add set of members, inline
			grp += setof_members		# same as above
			grp1 = grp + setof_members	# creates new group; i.e. copy+add


		#. delete::

			print(grp.delete(a_member))	# remove a member from group, inline
			grp -= a_member			# same as above
			print(grp.delete(setof_members))# remove set of members, inline
			grp -= setof_members		# same as above
			grp1 = grp - setof_members	# creates new group; i.e. copy+delete


		#. verifications::

			print(a_member in grp)			# bool: member found in group
			print(grp == grp1)			# bool: checks equality of two groups
			print(grp.over(acls))			# check for acl entries containing group.
			print(grp1.has(grp))			# check for grp1 members containing grp.

		#. comparisions::

			print(grp > grp1)			# difference in two group members
			print(grp < grp1)			# difference in two group members

		#. get delta::

			print(grp.add_str())	# members added to a group, string
			print(grp.del_str())	# members added from a group, negating string
			print(grps.changes('adds'))	# add strings for all groups
			print(grps.changes('removals')) # negating strings from all groups

.. Warning::
	Be extra careful on implementatin steps, if group is applied to multiple access-lists.

