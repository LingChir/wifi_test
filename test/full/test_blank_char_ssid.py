#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_blank_char_ssid.py
# Time       ：2023/7/24 10:22
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
测试步骤
SSID含有空格

1.设置SAP SSID为"SAP_12  34"

SSID输入成功
'''

ssid = "SAP_12  34"


router_2g = Router(band='2.4 GHz', ssid=ssid, wireless_mode='N only', channel='自动', bandwidth='20 MHz',
                   authentication_method='Open System')


@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_2g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.forget_network_cmd(target_ip='192.168.50.1',ssid=ssid)
    pytest.executer.kill_tvsetting()


def test_connect_blank_chars_ssid():
    assert pytest.executer.connect_ssid(ssid), "Can't connect"

