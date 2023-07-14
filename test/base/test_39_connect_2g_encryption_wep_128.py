#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_39_connect_2g_encryption_wep_128.py
# Time       ：2023/7/14 15:40
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""


import logging
import re
import time

import pytest

from tools.Asusax88uControl import Asusax88uControl
from Router import Router
'''
测试步骤
1.设置路由器2.4G 无线网络名称为“ATC_ASUS_AX88U_2G”，隐藏SSID设置为否，无线模式设置为leacy，频道带宽设置为20 MHz,信道设置为自动,授权方式为shared key,WEP加密选择WPE-128bit，WEP无线密码设置为1234567890123
2.连接2.4G SSID
3.从设备 shell里面 ping 路由器网关地址：ping 192.168.50.1
'''
ssid = 'ATC_ASUS_AX88U_2G'
passwd = '1234567890123'
router_2g = Router(band='2.4 GHz', ssid=ssid, wireless_mode='Legacy', channel='自动', bandwidth='20 MHz',
                   authentication_method='Shared Key', wep_encrypt='WEP-128bits', wep_passwd='1234567890123')


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')
    pytest.executer.kill_tvsetting()

@pytest.mark.wifi_connect
def test_connect_ssid_enrtyption_wep_128():
    pytest.executer.connect_ssid(ssid, passwd), "Can't connect"
    assert pytest.executer.ping(hostname="192.168.50.1"), "Can't ping"
