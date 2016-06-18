from allocators import CpuBasedAllocator
from allocators import PriceBasedAllocator
from allocators import CpuAndPriceBasedAllocator

def get_allocator_based_on_input_params(hours, resources, options):
    if(options.get("cpus") and options.get("price")):
        return CpuAndPriceBasedAllocator(options.get("cpus"), options.get("price"), hours, resources)
    elif(options.get("price")):
        return PriceBasedAllocator(options.get("price"), hours, resources)
    elif(options.get("cpus")):
        return CpuBasedAllocator(options.get("cpus"), hours, resources)
    else:
    	return None
