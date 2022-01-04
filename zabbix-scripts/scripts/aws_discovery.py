#!/usr/bin/python3
import configparser
import argparse
import importlib


if __name__ == "__main__":
    # Using CLI argument parser to save brain cells
    # if we need to add some arg down the road
    parser = argparse.ArgumentParser(
                description="AWS Service instances Zabbix discovery script")
    parser.add_argument("--service", dest="service",
                        help="Service to discover instances in",
                        required=True, type=str)
    parser.add_argument("--region", dest="region",
                        help="AWS region for discovery",
                        required=True, type=str)
    parser.add_argument("--account", dest="account",
                        help="AWS account for discovery",
                        required=True, type=str)
    parser.add_argument("--config", dest="config",
                        help="Optional path to config file",
                        required=False, type=str)
    parser.add_argument("--args", dest="args", default="",
                        help="Optional args for discovery modules",
                        required=False, type=str, nargs="+")
    args = parser.parse_args()

    # This config is optional and will use default value if you don't specify
    # Config contains credentials for specified accounts (see sample config)
    default_path = "/usr/lib/zabbix/scripts/conf/aws.conf"
    conf_file = args.config if args.config else default_path
    config = configparser.ConfigParser()
    config.read_file(open(conf_file))

    # Tricky part is to dynamically import ONLY one module
    # for the serice that was requested by CLI argument
    discovery_module = importlib.import_module(".{}".format(args.service),
                                               "discovery")

    # Create instance of discoverer from this module and run actual discovery
    d = discovery_module.Discoverer(config, args.account,
                                    args.service, args.region)
    print (d.get_instances(*args.args))
