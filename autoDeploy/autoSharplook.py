#!/usr/bin python
# *** coding: utf*8 ***
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

def esconfig():
    """

    :return:
    """

    with open("/home/eoi/itoa/app/elasticsearch/elasticsearch-5.4.3/config/elasticsearch.yml", 'r') as f:
        content = f.readlines()
        content = content[::-1][:6][::-1]
        with open("/root/autoDeploy/elasticsearch.yml", 'a') as f2:
            f.write("\n")
            f2.writelines(content)

def auto():
    """

    auto deploy
    :return:
    """

    os.chdir('/root/autoDeploy/deploy')

    bash_command("./deploy install all")

    esconfig()

    bash_command("cp /root/autoDeploy/elasticsearch.yml /home/eoi/itoa/app/elasticsearch/elasticsearch-5.4.3/config/elasticsearch.yml")


    print "\n\n安装完成，执行start命令启动，如果有错误，请执行stop命令停止所有进程，并利用相关命令查看日志"


auto()
