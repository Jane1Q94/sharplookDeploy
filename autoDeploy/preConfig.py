#!/usr/bin python
# -*- coding: utf-8 -*-
# @name   : preConfig.py
# @author : Jane
# @date   : 2018/8/25


import os
import time



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
    print "------------uname -a----------------\n"
    bash_command("uname -a")
    print "------------------------------------\n\n"
    time.sleep(4)

    print "------------setenforce0----------------\n"
    bash_command("setenforce 0")
    print "---------------------------------------\n\n"
    time.sleep(4)

    print "---------------systemctl stop firewalld----------\n"
    bash_command("systemctl stop firewalld")
    print "----------------------------------------------\n\n"
    time.sleep(4)

    print "---------------timedatectl----------------------\n"
    bash_command("timedatectl")
    print "-------------------------------------------------\n\n"
    time.sleep(4)

    print "------------------settimezone--------------------\n"
    bash_command("timedatectl set-timezone 'Asia/Shanghai'")
    print "--------------------------------------------------\n\n"
    time.sleep(4)

    print "----------------------sysctl -p---------------------\n"
    bash_command("sysctl -p")
    print "-----------------------------------------------------\n\n"
    time.sleep(4)

    print "-------------------------uninstall openjdk----------------------\n"
    bash_command("rpm -e --nodeps $(rpm -qa | grep openjdk)")
    print "-----------------------------------------------------------------\n\n"
    time.sleep(4)

    print "---------------------------create java dir------------------------\n"
    bash_command("mkdir /opt/java")
    print "------------------------------------------------------------------\n\n"
    time.sleep(4)

    print "--------------------------解压java包------------------------------\n"
    bash_command("tar xvf packages/00-jdk-* -C /opt/java")
    print "------------------------------------------------------------------\n\n"
    time.sleep(4)

    bash_command("source /etc/profile")

    print "---------------------------check java----------------------------\n"
    bash_command("java -version")
    print "-------------------------------------------------------------------\n\n"
    time.sleep(4)

    print '--------------------------uninstall mariadb---------------------\n'
    bash_command("rpm -e --nodeps $(rpm -qa | grep mariadb)")
    print "------------------------------------------------------------------\n\n"
    time.sleep(4)






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
    openFIle("/etc/selinux/config", "SELINUX=disabled")

    with open("hosts") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/hosts", content)

    with open("limits") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/security/limits.conf", content)

    openFIle("/etc/sysctl.conf", "vm.max_map_count=262144")

    with open("java") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/profile", content)





preAlterConfigFile()
preCommand()
