#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_add_network_wpa3.py
# Time       ：2023/7/24 10:16
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""



import logging
import os
import time

import pytest

from tools.Asusax88uControl import Asusax88uControl
from Router import Router
'''
测试配置
添加WIFI网络

WPA3-Personal加密

添加安全性选择 加密方式-WPA3-Personal的网络

能添加成功
'''

ssid = 'ATC_ASUS_AX88U_2G'
passwd = '12345678'
router_2g = Router(band='2.4 GHz', ssid=ssid, wireless_mode='Legacy', channel='1', bandwidth='20 MHz',
                   authentication_method='WPA3-Personal', wpa_passwd=passwd)



@pytest.fixture(scope='function', autouse=True)
def setup():
    # set router
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.kill_tvsetting()
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')


def test_add_network_wpa3():
    pytest.executer.add_network(ssid, 'WPA3-Personal',passwd=passwd)
    assert pytest.executer.wait_for_wifi_address(), "Connect fail"
