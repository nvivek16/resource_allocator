class CpuAndPriceBasedAllocator():
    def __init__(self, cpus, price, hours, resources):
        self.cpus = cpus
        self.hours = hours
        self.price = price / float(10)
        self.resources_dict = resources
        self.output = []
        self.tmp_storage = []

    def get_costs(self):
        for region, resources in self.resources_dict.iteritems():
            self.rec_fun(resources, 0, len(resources))
        self.output.sort(key = lambda x: x['total_cost'])
        self.preformat_output()
        return self.output

    def preformat_output(self):
        for entry in self.output:
            entry['total_cost'] = "$" + str(entry['total_cost'] * self.hours)
            entry['servers'] = entry['servers'].items()

    def rec_fun(self, resources, start, end):
        path_added = False
        while(start < end):
            self.tmp_storage.append(resources[start])
            self.price -= resources[start].price_per_hour
            self.cpus -= resources[start].cpus
            if(self.cpus <= 0 and self.price == 0):
                self.output.append(self.compute_total_cost_cpus_server_count())
            elif(self.price < 0):
                self.tmp_storage.pop()
                self.cpus += resources[start].cpus
                self.price += resources[start].price_per_hour
                if(len(self.tmp_storage) > 0 and not path_added and self.cpus <= 0):
                    self.output.append(self.compute_total_cost_cpus_server_count())
                return True     
            else:
                path_added = self.rec_fun(resources, start, end)
            self.price += resources[start].price_per_hour
            self.cpus += resources[start].cpus
            self.tmp_storage.pop()
            start += 1

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