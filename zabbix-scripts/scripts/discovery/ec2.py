#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_instances(Filters=[
            {"Name": "instance-state-name", "Values": ["running"]}])
        instances = list()
        for reservation in response["Reservations"]:
            instances.extend(reservation["Instances"])
        data = list()
        for instance in instances:
            name = ""
            ldd = {
                    "{#INSTANCE_ID}":   instance["InstanceId"],
                    "{#PRIVATE_IP}":    instance["PrivateIpAddress"]
            }
            if "Tags" not in instance.keys():
                name = instance["InstanceId"]
            else:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name":
                        if tag["Value"]:
                            name = tag["Value"]
                        else:
                            ldd["{#INSTANCE_ID}"]
                        break
            if not name:
                name = instance["InstanceId"]
            ldd["{#NAME}"] = name
            data.append(ldd)
        return data
