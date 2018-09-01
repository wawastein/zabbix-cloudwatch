# zabbix-cloudwatch
Cloudwatch integration for Zabbix 3.x

**Current release: 1.1.0. Zabbix template was tested with Zabbix 3.4, please revert to 1.0.0 if you find any backward incompatibility and open an issue.**

Python 2.7.x

1. Create specialized user account in AWS and grant it permissions for required services and API calls (for example `describe_instances()` for EC2)
2. Clone github repo: https://github.com/wawastein/zabbix-cloudwatch
3. Copy contents of `zabbix-scripts` into `/usr/lib/zabbix` directory, change owner of  the dir and its contents to user under which you run Zabbix
4. [Install](http://boto3.readthedocs.io/en/latest/guide/quickstart.html) system-wide `boto3` package
5. Import `cloudwatch_template.xml` into Zabbix
6. Put credentials of account created in (1) into `/usr/lib/zabbix/scripts/conf/aws.conf`
7. Create host with 0.0.0.0 as interface and link it to the template. Change macros `ACCOUNT` and `REGION` to correspond to your case: 

![example](https://awawastuff.files.wordpress.com/2017/04/vi-sky-mon1-configuration-of-hosts.png)

8. Enable/Disable all discovery rules/items/triggers you think necessary, add new or modify existing ones.

Default template has rules and items for following services:
* EC2 (requires `describe_instances()` API call permissions)
* RDS (`describe_db_instances()` API call)
* ELB (`describe_load_balancers()` API call)
* EMR (`list_clusters()` API call)
* ELBv2 (`describe_target_groups()` API call)
* S3 (`list_buckets()` API call)

Detailed overview at: https://wordpress.com/read/feeds/49943587/posts/1417437611

Hit me up on twitter [@wawastein](https://twitter.com/wawastein) if you got any questions, submit pull requests, fork all you want, and Papa bless.
