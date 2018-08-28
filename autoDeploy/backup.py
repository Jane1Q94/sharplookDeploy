#!/usr/bin python
# *** coding: utf*8 ***
# @name   : preConfig.py
# @author : Jane
# @date   : 2018/8/28


import os


def bash_command(command):
    """

    excute bash command in python
    :param command: command
    :return: the bash command result
    """

    try:
        print
        os.popen(command).read().strip()

    except:
        return None


def backupConfig():
    """

    backup config file
    :return:
    """
    print "#################备份配置文件######################\n\n"
    bash_command("cp /etc/selinux/config /etc/selinux/config.bak")
    #bash_command("cp /etc/ntp.conf /etc/ntp.conf.bak")
    bash_command("cp /etc/hosts /etc/hosts.bak")
    bash_command("cp /etc/security/limits.conf /etc/security/limits.conf.bak")
    bash_command("cp /etc/sysctl.conf /etc/sysctl.conf.bak")
    bash_command("cp /etc/profile /etc/profile.bak")
    bash_command("cp /root/.bash_profile /root/.bash_profile.bak")
    print "备份完成"


backupConfig()
