# -*- codeing = utf-8 -*-
# @Time : 2020/12/8 12:01 下午

import os
import socket


# 获取IP
# ip = socket.gethostbyname(hostname)
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    hostname = socket.gethostname()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip, hostname


ip, hostname = get_host_ip()
print(hostname, ip)
