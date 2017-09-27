#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.list_buckets()
        data = list()
        for bucket in response["Buckets"]:
            ldd = {
                "{#NAME}": bucket['Name'],
            }
            data.append(ldd)
        return data
