class Resource:
    def __init__(self, server_type, region, cpus, price_per_hour):
        self.region = region
        self.cpus = cpus
        self.price_per_hour = price_per_hour
        self.server_type = server_type