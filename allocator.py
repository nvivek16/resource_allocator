import lookup
import resource
import allocator_factory
def get_costs(instances, hours, cpus, price):
    # create resources and group based on region
    resources_dict = create_resources(instances)
    return allocator_factory.get_allocator_based_on_input_params(cpus, price, hours, resources_dict).get_costs()

def create_resources(instances):
    output = {}
    for region, server_config in instances.iteritems():
        output[region] =  [resource.Resource(key, region, lookup.get_cpu_configuration_based_on_instance_type(key), value) for key, value in server_config.iteritems()]
        # to handle minimum cpus
        output[region].sort(key=lambda x: x.cpus)
    return output