# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_connect_11ax_channel_149.py
# Time       ：2023/7/26 10:23
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
11ax mode 信道120

Connect an AP which channel is 5G AX-149

Platform connect the AP successful
'''

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'Abc@123456'
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='AX only', channel='149', bandwidth='40 MHz',
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
def test_channel_149():
    assert pytest.executer.connect_ssid(ssid, passwd=passwd), "Can't connect"
