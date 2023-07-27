# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_change_ap.py
# Time       ：2023/7/26 10:58
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
1.AP 5G和2.4G设置相同的SSID和密码类型以及密码
2.DUT连接AP（强信号）
3.修改AP信道,检查回连

默认连接5G
'''

ssid_name = 'ATC_ASUS_AX88U'
passwd = 'test1234'
router_2g = Router(band='2.4 GHz', ssid=ssid_name, wireless_mode='自动', channel='自动', bandwidth='20 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)
router_5g = Router(band='5 GHz', ssid=ssid_name, wireless_mode='自动', channel='自动', bandwidth='20 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)
router_5g_temp = Router(band='5 GHz', ssid=ssid_name, wireless_mode='自动', channel='36', bandwidth='20 MHz',
                        authentication_method='WPA2-Personal', wpa_passwd=passwd)

ax88uControl = Asusax88uControl()


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl.change_setting(router_2g)
    # ax88uControl.router_control.driver.quit()
    time.sleep(1)
    ax88uControl.change_setting(router_5g)
    yield
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1')
    pytest.executer.kill_tvsetting()


@pytest.mark.wifi_connect
def test_change_ap():
    assert pytest.executer.connect_ssid(ssid_name, passwd), "Can't connect"
    ax88uControl.change_setting(router_5g_temp)
    ax88uControl.router_control.driver.quit()
    time.sleep(5)
    assert 'freq: 5' in pytest.executer.checkoutput(pytest.executer.IW_LINNK_COMMAND), "Doesn't conect 5g "
