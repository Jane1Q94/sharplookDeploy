#!/usr/bin python
# -*- coding: utf-8 -*-
# @name   : preConfig.py
# @author : Jane
# @date   : 2018/8/27

import os

def bash_command(command):
    """

    excute bash command in python
    :param command: command
    :return: the bash command result
    """

    try:
        print os.popen(command).read().strip()

    except:
        return None


def commandAlias():
    """

    define some alias.
    :return:
    """
    als = ['alias "data"="cd /home/eoi/itoa/app/"',
           'alias "home"="cd /root/autoDeploy/deploy/"',
           'alias "eslog"="cat /home/eoi/itoa/app/elasticsearch/logs/eoi-elasticsearch.log"',
           'alias "zklog"="cat /home/eoi/itoa/app/zookeeper/zookeeper-3.4.10/zookeeper.out"',
           'alias "kafkalog"="cat /home/eoi/itoa/app/kafka/kafka_2.11-0.10.2.1/logs/server.log"',
           'alias "itoalog"="cat /home/eoi/itoa/app/itoaservice/itoaservice/logs/itoaService.log"',
           'alias "nginxlog"="cat /var/log/nginx/access.log"',
           'alias "celllog"="cat /home/eoi/itoa/app/cell/cell/logs/cell.log"',
           'alias "routerlog"="cat /home/eoi/itoa/app/router/router/logs/router.log"',
           'alias "curatorlog"="cat /home/eoi/itoa/app/curator/curator/logs/"',
           'alias "streamlog"="cat /home/eoi/itoa/app/kstream/stream/logs/stream.log"',
           'alias "persistentlog"="cat /home/eoi/itoa/app/persistent/persistent/logs/persistent.log"',
           'alias "uqlog"="cat /home/eoi/itoa/app/uq/uql/logs/UniversalQueryService.log"',
           'alias "hublog"="cat /home/eoi/itoa/app/hub/hub/logs/hub.log"',
           'alias "connectorlog"="cat /home/eoi/itoa/app/connector/connector/logs/connects.log"',
           'alias "config"="vim /root/autoDeploy/deploy/config/conf.toml"',
           'alias "start"="python /root/autoDeploy/start.py"',
           'alias "stop"="python /root/autoDeploy/stop.py"',
           'alias "pre"="python /root/autoDeploy/preConfig.py"',
           'alias "install"="python /root/autoDeploy/autoSharplook.py"',
           'alias "backup"="python /root/autoDeploy/backup.py"'
           ]

    with open("/root/.bash_profile", 'a') as f:
        content = "\n".join(als)
        f.writelines(content)



    bash_command("source /root/.bash_profile")
    
    
commandAlias()
