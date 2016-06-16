import copy
import lookup
import resource

def get_costs(instances, hours, cpus):
	# create resources and group based on region
	resources_dict = create_resources(instances)
	
	output = {}
	for region, resources in resources_dict.iteritems():
		output[region] = []
		func_rec(output[region], [], resources, cpus, 0, len(resources))
	return output

def create_resources(instances):
	output = {}
	for region, server_config in instances.iteritems():
		output[region] =  [resource.Resource(key, region, lookup.get_cpu_configuration_based_on_instance_type(key), value) for key, value in server_config.iteritems()]
		# to handle minimum cpus
		output[region].sort(key=lambda x: x.cpus)
	return output

def func_rec(output, tmp, resources, cpus, start, end):
	if(cpus <= 0):
		output.append(copy.deepcopy(tmp))
		return	
	while(start < end):
		tmp.append(resources[start])
		func_rec(output, tmp, resources, cpus - resources[start].cpus, start, end)
		if(len(tmp) > 0):
			tmp.pop()
		start += 1