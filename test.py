import allocator
instances = {"us-east" : {"large": 0.12, "xlarge": 0.23, "2xlarge": 0.45, "4xlarge": 0.774, "8xlarge": 1.4,"10xlarge": 2.82}, "us-west": {"large": 0.14, "2xlarge": 0.413, "4xlarge": 0.89, "8xlarge": 1.3, "10xlarge": 2.97}}
hours = 10
output = allocator.get_costs(instances, hours, cpus = 100)
print len(output)

output = allocator.get_costs(instances, hours, price = 100)
print len(output)

output = allocator.get_costs(instances, hours, price = 100, cpus = 100)
print len(output)