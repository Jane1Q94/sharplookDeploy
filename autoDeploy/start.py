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
        print os.popen(command).read().strip()

    except:
        return None

def startAuto():
    """

    :return:
    """

    os.chdir("/root/autoDeploy/deploy")
    bash_command('./deploy start all')


startAuto()