#!/usr/bin python
# -*- coding: utf-8 -*-
# @name   : preConfig.py
# @author : Jane
# @date   : 2018/8/25


import os

def bash_command(command):
    """

    excute bash command in python
    :param command: command
    :return: the bash command result
    """

    try:
        return os.popen(command).read().strip()

    except:
        return None


def preCommand():
    """

    preparation config before installing the software
    :return: None
    """

    bash_command("uname -a")
    bash_command("setenforce 0")
    bash_command("systemctl stop firewalld")
    bash_command("timedatectl")
    bash_command("timedatectl set-timezone 'Asia/Shanghai'")
    bash_command("sysctl -p")


def openFIle(path, content):
    """

    change the config file
    :param path:
    :param content:
    :return:
    """

    with open(path, 'a') as f:
        f.write(content)


def preAlterConfigFile():
    # openFIle("/etc/selinux/config", "SELINUX=disabled")
    openFIle("test3", "SELINUX=disabled")

    with open("hosts") as f:
        content = "\n".join(f.readlines())
        # openFIle("/etc/hosts", content)
        openFIle("test1", content)

    with open("limits") as f:
        content = "\n".join(f.readlines())
        # openFIle("/etc/security/limits.conf", content)
        openFIle("test2", content)

    # openFIle("/etc/sysctl.conf", "vm.max_map_count=262144")
    openFIle("test3", "vm.max_map_count=262144")






