#!/usr/bin/env python

from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_cache_clusters()

        data = []

        for instance in response["CacheClusters"]:
            if instance["CacheNodeType"] == "cache.t2.micro":
                memory_bytes = int(555 * pow(1024, 2))
            if instance["CacheNodeType"] == "cache.t2.small":
                memory_bytes = int(1.55 * pow(1024, 3))
            if instance["CacheNodeType"] == "cache.t2.medium":
                memory_bytes = int(3.22 * pow(1024, 3))
            if instance["CacheNodeType"] == "cache.m3.medium":
                memory_bytes = int(2.78 * pow(1024, 3))
            try:
                cache_replicationgroupid = "%s" % instance["ReplicationGroupId"]
            except:
                cache_replicationgroupid = "%s" % None
            ldd = {
                "{#CACHE_REPLICATIONGROUPID}": cache_replicationgroupid,
                "{#CACHE_CACHECLUSTERID}": instance["CacheClusterId"],
                "{#CACHE_CACHECLUSTERSTATUS}": instance["CacheClusterStatus"],
                "{#CACHE_ENGINE}": instance["Engine"],
                "{#CACHE_CACHESUBNETGROUPNAME}": instance["CacheSubnetGroupName"],
                "{#MEMORY}": memory_bytes
            }
            data.append(ldd)
        return data
