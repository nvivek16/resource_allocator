SERVER_CPU_CONFIGURATION = {
    "large": 1,
    "xlarge": 2,
    "2xlarge": 4,
    "4xlarge": 8,
    "8xlarge": 16,
    "10xlarge": 32
}

def get_cpu_configuration_based_on_instance_type(instance_name):
    return SERVER_CPU_CONFIGURATION.get(instance_name)