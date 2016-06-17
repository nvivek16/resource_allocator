from cpu_based_allocator import CpuBasedAllocator
from price_based_allocator import PriceBasedAllocator
from cpu_and_price_based_allocator import CpuAndPriceBasedAllocator
def get_allocator_based_on_input_params(cpus, price, hours, resources):
    if(cpus >= 0 and price >= 0):
        return CpuAndPriceBasedAllocator(cpus, price, hours, resources)
    elif(price >= 0):
        return PriceBasedAllocator(price, hours, resources)
    else:
        return CpuBasedAllocator(cpus, hours, resources)
