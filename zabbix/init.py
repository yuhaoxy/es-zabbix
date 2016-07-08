#!/usr/bin/env python

import socket
from pyzabbix.api import ZabbixAPI
import config

def add_monitor(hostname, url=config.XG_URL, auth=config.XG_AUTH):
    try:
        zabbix_api = ZabbixAPI(url=url, use_auth=True, auth=auth)
        hosts_id = zabbix_api.do_request('host.get', params={'output':'hostid', 'filter':{'host':[hostname]}})

        if url==config.XG_URL:
            zabbix_api.do_request('host.massadd', params={'hosts': hosts_id['result'],
                            'templates': config.XG_TEMPLATE_IDS})
        else:
            zabbix_api.do_request('host.massadd', params={'hosts': hosts_id['result'],
                            'templates': config.QC_TEMPLATE_IDS})
    except Exception,e:
        pass

def main():
    hostname = socket.gethostname()
    if hostname.startswith('vpc'):
        pass
    elif hostname.startswith('qc'):
        add_monitor(hostname, url=config.QC_URL, auth=config.QC_AUTH)
    else:
        add_monitor(hostname, url=config.XG_URL, auth=config.XG_AUTH)

if __name__ == '__main__':
    main()
