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

    bash_command("source /etc/profile")

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
    bash_command("source db.sql")
    print '----------------------------------------------------------------\n\n'
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

def deleteFile(path, numLine):
    """

    delete lines of a config file
    :param path:
    :param numLine:
    :return:
    """
    with open(path, 'w+') as f:
        content = f.readlines()
        content = content[:-numLine]
        f.writelines(content)


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


def clearAlter():
    """

    clear the change of the config file for better test.
    :return:
    """

    deleteFile("/etc/selinux/config", 1)

    deleteFile("/etc/ntp.conf", 2)

    deleteFile("/etc/hosts", 3)

    deleteFile("/etc/security/limits.conf", 8)

    deleteFile("/etc/sysctl.conf", 1)

    deleteFile("/etc/profile", 4)



preAlterConfigFile()
preCommand()
