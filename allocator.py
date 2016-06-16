import copy
import lookup
import resource


def get_costs(instances, hours, cpus):
    # create resources and group based on region
    resources_dict = create_resources(instances)
    output = []
    for region, resources in resources_dict.iteritems():
        func_rec(output, [], resources, cpus, 0, len(resources))
    # output.sort(key=lambda x: x['total_cost'])
    return convert_to_dollars(output, hours)

def convert_to_dollars(output, hours):
    for entry in output:
        entry['total_cost'] = "$" + str(entry['total_cost'] * hours)
        entry['servers'] = entry['servers'].items()
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
        append_in_asc_order_of_cost(output, compute_total_cost_server_count(tmp))
        return
    while(start < end):
        tmp.append(resources[start])
        func_rec(output, tmp, resources, cpus - resources[start].cpus, start, end)
        if(len(tmp) > 0):
            tmp.pop()
        start += 1

def calculate_sum_and_count(collector, resource):
    collector['total_cost'] += resource.price_per_hour
    if(not collector['servers'].get(resource.server_type)):
        collector['servers'][resource.server_type] = 0
    collector['servers'][resource.server_type] += 1
    return collector

def compute_total_cost_server_count(resources_array):
    collector = {"total_cost": 0, "servers": {}, "region": resources_array[0].region}
    return reduce(calculate_sum_and_count, resources_array, collector)

def append_in_asc_order_of_cost(output, transformed_entry):
    output.append(transformed_entry)
    length = len(output) - 1
    while(length  > 0):
        if(output[length]['total_cost'] < output[length - 1]['total_cost']):
            output[length], output[length - 1] = output[length - 1], output[length]
            break
        length -= 1
