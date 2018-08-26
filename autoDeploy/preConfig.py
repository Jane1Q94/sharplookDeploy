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
        print os.popen(command).read().strip()

    except:
        return None

def preCommand():
    """

    preparation config before installing the software
    :return: None
    """

    print "----------------eoi user--------------\n"
    bash_command("useradd eoi")
    bash_command("passwd eoi")
    print "----------------------------------------\n\n"
    time.sleep(4)


    print "------------uname -a----------------\n"
    bash_command("uname -a")
    print "------------------------------------\n\n"
    time.sleep(4)

    print "------------setenforce0----------------\n"
    bash_command("setenforce 0")

    print "---------------systemctl stop firewalld----------\n"
    bash_command("systemctl stop firewalld")

    print "---------------timedatectl----------------------\n"
    bash_command("timedatectl")
    print "-------------------------------------------------\n\n"
    time.sleep(4)

    print "------------------settimezone--------------------\n"
    bash_command("timedatectl set-timezone 'Asia/Shanghai'")

    print "--------------------ntpdate----------------------\n"
    bash_command("ntpdate 192.168.21.198")
    print "----------------------------------------------------\n\n"
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

    print '--------------------------source /etc/profile--------------------\n'
    bash_command("source /etc/profile")
    time.sleep(4)

    print "---------------------------check java----------------------------\n"
    bash_command("java -version")
    print "-------------------------------------------------------------------\n\n"
    time.sleep(4)

    print '--------------------------uninstall mariadb---------------------\n'
    bash_command("rpm -e --nodeps $(rpm -qa | grep mariadb)")
    print "------------------------------------------------------------------\n\n"
    time.sleep(4)

    print '---------------------------安装mysql包--------------------------\n'
    bash_command("tar xvf packages/04-mysql*")
    bash_command("rpm -ivh mysql-community-common-5.7*")
    bash_command("rpm -ivh mysql-community-libs-5.7*")
    bash_command("rpm -ivh mysql-community-client-5.7*")
    bash_command("rpm -ivh mysql-community-server-5.7*")
    bash_command("service mysqld start")
    bash_command("grep 'temporary password' /var/log/mysqld.log")
    bash_command("mysql -uroot -p")
    print '----------------------------------------------------------------\n\n'






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

    with open("ntpserver") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/ntp.conf", content)

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



def backupConfig():
    """

    backup config file
    :return:
    """
    bash_command("cp /etc/selinux/config /etc/selinux/config.bak")
    bash_command("cp /etc/ntp.conf /etc/ntp.conf.bak")
    bash_command("cp /etc/hosts /etc/hosts.bak")
    bash_command("cp /etc/security/limits.conf /etc/security/limits.conf.bak")
    bash_command("cp /etc/sysctl.conf /etc/sysctl.conf.bak")
    bash_command("cp /etc/profile /etc/profile.bak")



def recover():
    """

    recover config file from backup fiel
    :return:
    """
    bash_command("cp /etc/selinux/config.bak /etc/selinux/config")
    bash_command("cp /etc/ntp.conf.bak /etc/ntp.conf")
    bash_command("cp /etc/hosts.bak /etc/hosts")
    bash_command("cp /etc/security/limits.conf.bak /etc/security/limits.conf")
    bash_command("cp /etc/sysctl.conf.bak /etc/sysctl.conf")
    bash_command("cp /etc/profile.bak /etc/profile")




preAlterConfigFile()
preCommand()
