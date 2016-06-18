from allocators import CpuBasedAllocator
from allocators import PriceBasedAllocator
from allocators import CpuAndPriceBasedAllocator

def get_allocator_based_on_input_params(cpus, price, hours, resources):
    if(cpus >= 0 and price >= 0):
        return CpuAndPriceBasedAllocator(cpus, price, hours, resources)
    elif(price >= 0):
        return PriceBasedAllocator(price, hours, resources)
    else:
        return CpuBasedAllocator(cpus, hours, resources)
