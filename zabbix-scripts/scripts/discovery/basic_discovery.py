#!/usr/bin/python
from aws_client import AWSClient
import json


class BasicDiscoverer(AWSClient):
    def get_instances(self, *args):
        "Runs discovery method and packs result into JSON"
        data = self.discovery(*args)
        return json.dumps({"data": data})

    def discovery(self, *args):
        "Method that should be overriden inside inherited classes"
        pass
