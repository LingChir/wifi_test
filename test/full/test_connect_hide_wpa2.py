# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_connect_hide_wpa2.py
# Time       ：2023/8/1 16:34
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
1.配置一个WPA2密码加密 关闭SSID广播的AP
2.DUT新建一个连接 SSID与加密与测试AP一致
3.WiFi扫描（网络中需要没有其他连接成功过的AP）

channel 157

可以自动连接测试AP成功
'''

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'Abc@123456'
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='自动', channel='157', bandwidth='20/40/80 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd, hide_ssid='是')



@pytest.fixture(scope='function', autouse=True)
def setup():
    # set router
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_5g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.kill_tvsetting()
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')

@pytest.mark.wifi_connect
def test_connect_wpa2():
    pytest.executer.add_network(ssid, 'WPA/WPA2-Personal', passwd=passwd)
    assert pytest.executer.wait_for_wifi_address(), "Connect fail"
