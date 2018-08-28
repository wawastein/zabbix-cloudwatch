#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):

        response = self.client.list_buckets()
        data = list()

        # list_buckets() will return the buckets in all regions. Get only those in the requested region
        # See https://stackoverflow.com/questions/49814173/boto3-get-only-s3-buckets-of-specific-region
        region_buckets = \
            [bucket["Name"] for bucket in self.client.list_buckets()["Buckets"] \
            if self.client.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint'] == self.region]

        for bucket_name in region_buckets:
            ldd = {
                "{#BUCKET_NAME}": bucket_name,
            }
            data.append(ldd)
        return data
