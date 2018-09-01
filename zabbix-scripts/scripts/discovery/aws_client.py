#!/usr/bin/python
import boto3


class AWSClient(object):
    "Basic object for AWS services discovery"
    def __init__(self, config, account, service, region):
        "Initializes Boto3 client for specified service"
        aws_key = config.get(account, "key")
        aws_secret = config.get(account, "secret")
        self.client = boto3.client(
            service,
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret,
            region_name=region)
        self.region = region
