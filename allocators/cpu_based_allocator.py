class CpuBasedAllocator():
    def __init__(self, cpus, hours, resources):
        self.cpus = cpus
        self.hours = hours
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
        while(start < end):
            self.tmp_storage.append(resources[start])
            self.cpus -= resources[start].cpus
            if(self.cpus <= 0):
                self.output.append(self.compute_total_cost_server_count())
            else:
                self.rec_fun(resources, start, end)
            self.cpus += resources[start].cpus
            self.tmp_storage.pop()
            start += 1

    def calculate_sum_and_count(self, collector, resource):
        collector['total_cost'] += resource.price_per_hour
        if(not collector['servers'].get(resource.server_type)):
            collector['servers'][resource.server_type] = 0
        collector['servers'][resource.server_type] += 1
        return collector

    def compute_total_cost_server_count(self):
        collector = {"total_cost": 0, "servers": {}, "region": self.tmp_storage[0].region}
        return reduce(self.calculate_sum_and_count, self.tmp_storage, collector)