# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_forget_network.py
# Time       ：2023/8/1 15:43
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""

import logging
import os
import time

import pytest

from tools.Asusax88uControl import Asusax88uControl
from tools.yamlTool import yamlTool
from Router import Router
'''
测试步骤
Forget network

1.WIFI列表中存在一个Save的网络
2.点击Save的网络
3.选择Forget network

DUT不会再保存这个网络
'''

router_2g = Router(band='2.4 GHz', ssid='ATC_ASUS_AX88U_2G', wireless_mode='N only', channel='1', bandwidth='40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd='12345678')


@pytest.fixture(scope='function', autouse=True)
def setup():
    # set router
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    ax88uControl.router_control.driver.quit()
    # connect wifi
    cmd = pytest.executer.CMD_WIFI_CONNECT.format('ATC_ASUS_AX88U_2G', 'wpa2', '12345678')
    pytest.executer.checkoutput(cmd)
    pytest.executer.wait_for_wifi_address(cmd)
    yield


def test_forget_wifi():
    pytest.executer.find_ssid('ATC_ASUS_AX88U_2G')
    pytest.executer.wait_and_tap('Forget network', 'text')
    for _ in range(3):
        if pytest.executer.find_element('Internet connection', 'text'):
            break
        time.sleep(1)
        pytest.executer.keyevent(23)
        pytest.executer.keyevent(23)
    pytest.executer.uiautomator_dump()
    while 'Not connected' not in pytest.executer.get_dump_info():
        time.sleep(1)
        pytest.executer.uiautomator_dump()
    assert not pytest.executer.ping(hostname="192.168.50.1")
