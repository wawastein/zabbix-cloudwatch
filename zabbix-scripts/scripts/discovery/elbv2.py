#!/usr/bin/python
from basic_discovery import BasicDiscoverer

import re

class Discoverer(BasicDiscoverer):
    def discovery(self, *args):

        response = self.client.describe_target_groups()

        data = []

        # Load balancer data cache
        LoadBalancersDescrByArn = {}

        for TargetGroup in response["TargetGroups"]:

            # A target group may be related to one or more load balancers - create one entry per lb-target group
            # combination
            for LoadBalancerArn in TargetGroup["LoadBalancerArns"]:

                if LoadBalancerArn not in LoadBalancersDescrByArn:
                    LoadBalancersDescrByArn[LoadBalancerArn] = self.client.describe_load_balancers(
                        LoadBalancerArns=[LoadBalancerArn]
                    )['LoadBalancers'][0]

                target_health = self.client.describe_target_health(
                    TargetGroupArn=TargetGroup["TargetGroupArn"]
                )

                # Get the short ARNs that are effectivelly used when querying for metrics
                Arn = re.search(":(targetgroup/.*)", TargetGroup["TargetGroupArn"]).group(1)
                LoadBalancerShortArn = re.search(":loadbalancer/(.*)", LoadBalancerArn).group(1)

                # Final discovery entry
                ldd = {
                    "{#TARGET_GROUP_NAME}": TargetGroup["TargetGroupName"],
                    "{#TARGET_GROUP_ARN}": Arn,
                    "{#TARGET_GROUP_PORT}": TargetGroup["Port"],
                    "{#TARGET_GROUP_VPC_ID}": TargetGroup["VpcId"],
                    "{#TARGET_GROUP_LOAD_BALANCER_NAME}": LoadBalancersDescrByArn[LoadBalancerArn]['LoadBalancerName'],
                    "{#TARGET_GROUP_LOAD_BALANCER_DNS_NAME}": LoadBalancersDescrByArn[LoadBalancerArn]['DNSName'],
                    "{#TARGET_GROUP_LOAD_BALANCER_ARN}": LoadBalancerShortArn,
                    "{#TARGET_COUNT}": len(target_health['TargetHealthDescriptions']),
                }

                # Next load balancer in target group
                data.append(ldd)

        return data
