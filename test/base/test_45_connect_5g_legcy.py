#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_45_connect_5g_legcy.py
# Time       ：2023/7/14 16:01
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
1.设置路由器5G 无线网络名称为“ATC_ASUS_AX88U_5G”，隐藏SSID设置为否，无线模式设置为Legcy，频道带宽设置为20 M,信道设置为149，授权方式为shared key，WEP加密选择 WEP-64bits,无线密码索引选择1，WEP无线密码1设置为Abc1234567
2.连接5G SSID
3.从设备 shell里面 ping 路由器网关地址：ping 192.168.50.1
'''

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'Abc1234567'
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='Legacy', channel='149', bandwidth='20 MHz',
                   authentication_method='Shared Key', wep_passwd=passwd, wep_encrypt='WEP-64bits', passwd_index='1')


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_5g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')
    pytest.executer.kill_tvsetting()


@pytest.mark.wifi_connect
def test_connect_legcy_ssid():
    assert pytest.executer.connect_ssid(ssid, passwd),"Can't connect"
