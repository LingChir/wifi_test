#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_63_hot_spot_control.py
# Time       ：2023/7/17 13:55
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
1.进入设置，检查热点状态
2.重复开关热点20次.
'''

times = pytest.config_yaml.get_note('times_063')


@pytest.fixture(autouse=True)
def setup_teardown():
    pytest.executer.open_hotspot()
    yield
    pytest.executer.kill_moresetting()

@pytest.mark.hot_spot
# @pytest.mark.repeat(times)
def test_hotspot_control():
    pytest.executer.get_dump_info()
    ssid = re.findall(r'text="(.*?)" resource-id="android:id/summary"', pytest.executer.get_dump_info())[0]
    logging.info(f'ssid {ssid}')
    accompanying_dut.accompanying_dut_wait_ssid(ssid)
    pytest.executer.wait_and_tap('Portable HotSpot Enabled', 'text')
    accompanying_dut.accompanying_dut_wait_ssid_disapper(ssid)
    pytest.executer.wait_and_tap('Portable HotSpot Enabled', 'text')
