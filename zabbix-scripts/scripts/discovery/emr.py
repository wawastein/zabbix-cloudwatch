#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.list_clusters(
                        ClusterStates=["RUNNING", "WAITING",
                                       "STARTING", "BOOTSTRAPPING"])
        data = list()
        for cluster in response["Clusters"]:
            ldd = {
                    "{#CLUSTER_ID}":      cluster["Id"],
                    "{#CLUSTER_NAME}":    cluster["Name"],
            }
            data.append(ldd)
        return data
