#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_forget_then_reconnect.py
# Time       ：2023/7/25 9:00
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
忘记网络重新连接

1.Enter wifi list ，forget the current network
2.connect the AP again.

Need to input password
'''

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'Abc@123456'
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='AX only', channel='36', bandwidth='40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)


@pytest.fixture(scope='function', autouse=True)
def setup():
    # set router
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_5g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.kill_tvsetting()
    pytest.executer.forget_network_cmd()


@pytest.mark.wifi_connect
def test_channel_36():
    pytest.executer.connect_ssid(ssid, passwd=passwd)
    assert pytest.executer.wait_for_wifi_address(), "Connect fail"
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')
    pytest.executer.connect_ssid(ssid, passwd=passwd)
