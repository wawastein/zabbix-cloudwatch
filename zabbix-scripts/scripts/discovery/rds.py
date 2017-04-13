#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_db_instances()
        data = list()
        for instance in response["DBInstances"]:
            storage_bytes = int(instance["AllocatedStorage"]) * pow(1024, 3)
            ldd = {
                    "{#STORAGE}": storage_bytes,
                    "{#RDS_ID}": instance["DBInstanceIdentifier"]
            }
            data.append(ldd)
        return data
