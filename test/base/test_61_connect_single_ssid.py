#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_61_connect_single_ssid.py
# Time       ：2023/7/14 17:56
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
1.设置路由器2.4G和5G为相同的SSID"ATC_ASUS_AX88U"，相同的密码为test1234,带宽，无线模式，信道都为Auto。
2.DUT连接路由器 ATC_ASUS_AX88U，cmd下输入iw wlan0 link
'''

ssid = 'ATC_ASUS_AX88U'
passwd = 'test1234'
router_2g = Router(band='2.4 GHz', ssid=ssid, wireless_mode='自动', channel='自动', bandwidth='20 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='自动', channel='自动', bandwidth='20 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    # ax88uControl.router_control.driver.quit()
    time.sleep(1)
    ax88uControl.change_setting(router_5g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.forget_network_cmd()
    pytest.executer.kill_tvsetting()


@pytest.mark.wifi_connect
def test_connect_ssid_wireless_auto():
    pytest.executer.connect_ssid(ssid, passwd), "Can't connect"
    assert pytest.executer.ping(hostname="192.168.50.1"), "Can't ping"
    assert 'freq: 5' in pytest.executer.checkoutput(pytest.executer.IW_LINNK_COMMAND), "Doesn't conect 5g "
