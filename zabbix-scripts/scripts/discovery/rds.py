#!/usr/bin/python
from basic_discovery import BasicDiscoverer

class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
    
        # Clusters (e.g. Aurora)
        if "cluster" in args:
            data = list()
            response = self.client.describe_db_clusters()
            for cluster in response["DBClusters"]:
                ldd = {
                    "{#CLUSTER_ID}": cluster["DBClusterIdentifier"],
                    "{#CLUSTER_ENDPOINT}": cluster["Endpoint"],
                    "{#CLUSTER_READER_ENDPOINT}": cluster["ReaderEndpoint"]
                }
                data.append(ldd)
            return data

        # Standalone RDS instances
        response = self.client.describe_db_instances()
        for instance in response["DBInstances"]:
            data = list()
            storage_bytes = int(instance["AllocatedStorage"]) * pow(1024, 3)
            ldd = {
                    "{#STORAGE}": storage_bytes,
                    "{#RDS_ID}": instance["DBInstanceIdentifier"]
            }
            data.append(ldd)

        return data