class PriceBasedAllocator():

    '''
        1) Resources are grouped based on regions, since each region has different price per hour for its instances
        2) Alogrithm adds each resource mutliple times so that total price doesnot exceed the given cap.
        3) Since the total price of each subset should not be more than given cap. Resources will be added even if it is less than the given cap
        4) This algorithm make sures that two selected set doesnot have the same prefix by using path_added flag
        5) Selected resource combinations are sorted based on no of cpus in desc order
        6) Each resource is then formatted as mentioned in the main documentation
    '''

    def __init__(self, price, hours, resources):
        self.hours = hours
        # Price is divided by total no of given hours. As we are going to use price per hour in the algo
        self.price = price / float(self.hours)
        self.resources_dict = resources
        self.output = []
        self.tmp_storage = []

    def get_costs(self):
        for region, resources in self.resources_dict.iteritems():
            self.rec_fun(resources, 0, len(resources))
        self.output.sort(key = lambda x: x['total_cpus'], reverse = True )
        self.preformat_output()
        return self.output

    def preformat_output(self):
        for entry in self.output:
            # We again multiply with total no of hours
            entry['total_cost'] = "$" + str(entry['total_cost'] * self.hours)
            entry['servers'] = entry['servers'].items()

    def rec_fun(self, resources, start, end):
        path_added = False
        while(start < end):
            self.tmp_storage.append(resources[start])
            self.price -= resources[start].price_per_hour
            if(self.price == 0):
                self.output.append(self.compute_total_cost_cpus_server_count())
                path_added = True
            elif(self.price < 0):        
                self.tmp_storage.pop()
                self.price += resources[start].price_per_hour
                if(len(self.tmp_storage) > 0 and not path_added):
                    self.output.append(self.compute_total_cost_cpus_server_count())
                return True
            else:
                path_added = self.rec_fun(resources, start, end)
            self.price += resources[start].price_per_hour
            self.tmp_storage.pop()
            start += 1
        return path_added

    def calculate_sum_and_count(self, collector, resource):
        collector['total_cost'] += resource.price_per_hour
        collector['total_cpus'] += resource.cpus
        if(not collector['servers'].get(resource.server_type)):
            collector['servers'][resource.server_type] = 0
        collector['servers'][resource.server_type] += 1
        return collector

    def compute_total_cost_cpus_server_count(self):
        collector = {"total_cost": 0, "total_cpus": 0, "servers": {}, "region": self.tmp_storage[0].region}
        return reduce(self.calculate_sum_and_count, self.tmp_storage, collector)