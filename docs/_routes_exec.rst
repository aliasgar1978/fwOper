fw_Oper.route User documentation!
============================================

Cisco Firewall Routes - How To ?
-----------------------------------------

Use the route module of fw_oper package to get the necessary matching entries for the Routes
on Cisco Firewall.  

.. note::
	
	For now route changes are not implemented.


High-level Overview 
----------------------------

	#. Define inputs
	#. Import package, modules
	#. select firewall, routes, route Objects
	#. perform necessary search operations


Detailed How To
--------------------

	#. Define inputs::

		file = 'running-config log captuerd file for fw.log'	# fw log
		
		prefix = '10.10.10.0/24'


	#. Import necessary package/modules::

		import fwOper as fw

	#. Create Firewall Object::

		with open(file, 'r') as f:
			flst = f.readlines()

		insts = fw.get_object(fw.Instances, conf_list=flst)
		print(insts)			# set of instances

	#. Refereance to Instance to routes

		.. code:: python

			routes = insts['instance_name'].routes
			routes = insts.instance_name.routes
			print(routes)			# all routes

		*instance_name* can be accepted in either **bracket** or **dotted** format. 
		Use of bracket format is must if space/special characters involved in *instance_name*.

	#. Operations on routes::

		print(routes)				# all routes
		print(prefix in routes)		# bool: is prefix match any route.
		print(routes.prefix(prefix))	# matching route for given prefix
		print(routes.prefix(prefix).ifdesc)	# route description for matching route
		print(routes.prefix(prefix).route_line)	# string prop ( object work without it )




