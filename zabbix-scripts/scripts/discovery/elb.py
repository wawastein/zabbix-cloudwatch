#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_load_balancers()
        data = list()
        for balancer in response["LoadBalancerDescriptions"]:
            ldd = {
                    "{#BALANCER_NAME}":      balancer["LoadBalancerName"],
                    "{#INSTANCES_COUNT}":    len(balancer["Instances"])
            }
            data.append(ldd)
        return data
