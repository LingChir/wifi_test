#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_71_hot_spot_special_passwd.py
# Time       ：2023/7/17 16:48
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""

import logging
import time

import pytest

from ADB import accompanying_dut

'''
测试步骤
1.设置SAP 密码为"SAP_123test_"
'''
ssid = 'android_test_sap'
passwd = 'SAP_123test_'


@pytest.fixture(autouse=True)
def setup_teardown():
    pytest.executer.open_hotspot()
    logging.info('setup done')
    yield
    pytest.executer.close_hotspot()


@pytest.mark.hot_spot
def test_hotspot_special_passwd():
    pytest.executer.set_hotspot(ssid=ssid, passwd=passwd)
    accompanying_dut.accompanying_dut_wait_ssid(ssid)
