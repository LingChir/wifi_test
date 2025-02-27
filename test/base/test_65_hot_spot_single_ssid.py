#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_65_hot_spot_single_ssid.py
# Time       ：2023/7/17 14:53
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""



import logging
import re
import time

import pytest

from ADB import accompanying_dut

'''
测试步骤
1.设置SAP SSID为单个字符"a"
'''
ssid = 'a'


@pytest.fixture(autouse=True)
def setup_teardown():
    pytest.executer.open_hotspot()
    logging.info('setup done')
    yield
    pytest.executer.close_hotspot()

@pytest.mark.hot_spot
def test_hotspot_single_ssid():
    pytest.executer.set_hotspot(ssid)
    accompanying_dut.accompanying_dut_wait_ssid(ssid)
