import lookup
import resource
import allocator_factory
'''
	1) Create resource object for each instance. The resource object stores no of cpus it has, its price per hour and its region
	2) Allocator factory chooses the correst request handler based on the given input params
	3) Backtracking algorithm is used for allocating resources
'''
def get_costs(instances, hours, **options):
    # create resources and group based on region
    resources_dict = create_resources(instances)
    allocator = allocator_factory.get_allocator_based_on_input_params(hours, resources_dict, options)
    if(allocator):
    	return allocator.get_costs()

def create_resources(instances):
    output = {}
    for region, server_config in instances.iteritems():
        output[region] =  [resource.Resource(key, region, lookup.get_cpu_configuration_based_on_instance_type(key), value) for key, value in server_config.iteritems()]
        # to handle minimum cpus
        output[region].sort(key=lambda x: x.cpus)
    return output