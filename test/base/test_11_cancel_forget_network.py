#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_11_cancel_forget_network.py
# Time       ：2023/7/13 15:48
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
1.进入设置-无线网络
2.选中已经连接的无线网络，选择忘记网络，取消
3.从设备 shell里面 ping 路由器网关地址：ping 192.168.50.1
'''

ssid = 'ATC_ASUS_AX88U_2G'
passwd = '12345678'
router_2g = Router(band='2.4 GHz', ssid=ssid, wireless_mode='N only', channel='1', bandwidth='40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.forget_network_cmd(target_ip="192.168.50.1")
    pytest.executer.kill_tvsetting()


def test_cancel_forgetted():
    pytest.executer.connect_ssid(ssid,passwd)
    pytest.executer.kill_tvsetting()
    pytest.executer.find_ssid('ATC_ASUS_AX88U_2G')
    pytest.executer.wait_and_tap('Forget network', 'text')
    pytest.executer.wait_and_tap('Cancel', 'text')
    assert pytest.executer.ping(hostname="192.168.50.1"), "Can't ping"
