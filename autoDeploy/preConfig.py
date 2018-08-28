#!/usr/bin python
# *** coding: utf*8 ***
# @name   : preConfig.py
# @author : Jane
# @date   : 2018/8/25


import os
import time
import re



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
    print "########################START!##########################"
    print "******************查看操纵系统版本************************\n"
    bash_command("uname -a")
    print "\n\n"
    
    answer = raw_input("确认系统是否满足安装条件?[yes/no]")

    if answer == "yes":
        print "****************创建eoi用户**************\n"
        bash_command("useradd eoi")
        bash_command("passwd eoi")
        time.sleep(4)
        print "\n\n"


    

        print "************关闭SELINUX****************\n"
        bash_command("setenforce 0")
        bash_command("getenforce")
        time.sleep(4)
        print "\n\n"


        print "*************关闭防火墙*****************\n"
        bash_command("service firewalld stop")
        bash_command("service firewalld status")
        time.sleep(4)
        print "\n\n"

        print "*************设置时区********************\n"
        bash_command("timedatectl set-timezone 'Asia/Shanghai'")
        bash_command("timedatectl")
        time.sleep(4)
        print "\n\n"


        # print "*****************************************\n"
        # bash_command("ntpdate 192.168.21.198")
        # time.sleep(4)
        # print "\n\n"

        print "***************执行sysctl -p******************\n"
        bash_command("sysctl -p")
        time.sleep(4)
        print "\n\n"

        print "****************执行ulimit -n******************\n"
        bash_command("ulimit -n 65536")
        time.sleep(4)
        print 'done'
        print "\n\n"

        print "****************卸载openjdk********************\n"
        bash_command("rpm -e --nodeps $(rpm -qa | grep openjdk)")
        print "done"
        time.sleep(4)
        print "\n\n"

        print "***************创建java目录********************\n"
        bash_command("mkdir /opt/java")
        print "done"
        time.sleep(4)
        print "\n\n"

        print "****************解压java包*********************\n"
        bash_command("tar xvf packages/00-jdk* -C /opt/java")
        time.sleep(4)
        print "\n\n"

        bash_command("source /etc/profile")


        print '**************卸载mariadb******************\n'
        bash_command("rpm -e --nodeps $(rpm -qa | grep mariadb)")
        print "done"
        time.sleep(4)
        print "\n\n"

        print '*************安装Mysql包*********************\n'
        bash_command("tar xvf packages/04-mysql*")
        bash_command("rpm -ivh mysql-community-common-5.7*")
        bash_command("rpm -ivh mysql-community-libs-5.7*")
        bash_command("rpm -ivh mysql-community-client-5.7*")
        bash_command("rpm -ivh mysql-community-server-5.7*")
        bash_command("service mysqld start")
        passwd =  readMysqlPasswd()

        bash_command("tar zxvf packages/deploy*")
        print "准备工作完成，请用初始密码登录MySQL，执行三个sql脚本，完成后续。。。"
        print "\n\n"
        print "####################   %s    ##########################\n\n" % passwd
        print "mysql -u root -p  ***\n"
        print "source db.sql\n"
        print "use DB01"
        print "source structure.sql\n"
        print "source data.sql\n\n"
        print "#####################################################################"

    else:
        os._exists()

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
    """

    alter config file
    :return:
    """
    print "##################修改配置文件######################"
    print "\n\n"
    print "修改SELINUX的配置文件"
    openFIle("/etc/selinux/config", "SELINUX=disabled")
    time.sleep(2)
    print "\n\n"

    # print "修改ntp配置文件"
    # with open("ntpserver") as f:
    #     content = "\n".join(f.readlines())
    #     openFIle("/etc/ntp.conf", content)
    # time.sleep(2)
    # print "\n\n"

    print "修改hosts文件"
    with open("hosts") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/hosts", content)
    time.sleep(2)
    print "\n\n"

    print "修改limits配置文件"
    with open("limits") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/security/limits.conf", content)
    time.sleep(2)
    print "\n\n"

    print "修改sysctl配置文件"
    openFIle("/etc/sysctl.conf", "vm.max_map_count=262144")
    time.sleep(2)
    print "\n\n"

    print "设置JAVA环境变量"
    with open("java") as f:
        content = "\n".join(f.readlines())
        openFIle("/etc/profile", content)
    time.sleep(2)
    print "\n"

    print "write config file done"




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
    bash_command("cp /root/.bash_profile.bak  /root/.bash_profile")

def readMysqlPasswd():
    """

    get the origin passwd of mysql
    :return:
    """

    with open("/var/log/mysqld.log", 'r') as f:
        content = " ".join(f.readlines())
        return re.findall(r'root@localhost: (\S+)', content)[0]

preAlterConfigFile()
preCommand()
