#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_sap_special_chars_ssid.py
# Time       ：2023/7/25 13:44
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""

import logging

import pytest

'''
测试步骤
密码含有特殊字符

1.设置SAP 密码为"SAP_123test_"

可以保存成功，并能正确显示
'''

ssid = 'SAP_123test_'


@pytest.fixture(autouse=True)
def setup_teardown():
    pytest.executer.open_hotspot()
    logging.info('setup done')
    yield
    pytest.executer.close_hotspot()

@pytest.mark.hot_spot
def test_hotspot_blank_ssid():
    pytest.executer.set_hotspot(ssid=ssid)
    pytest.executer.wait_element('Hotspot name', 'text')
    assert ssid == pytest.executer.u().d2(resourceId="android:id/summary").get_text(), "ssid can't be set currently"
    pytest.executer.accompanying_dut_wait_ssid(ssid)
