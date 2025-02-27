#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
# File       : test_sap_cn_blank_passwd.py
# Time       ：2023/7/25 10:39
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""



import logging

import pytest


'''
测试步骤
SSID中文字符

密码含有中文和空格

1.设置SAP 密码为"SAP_测试  123"

可以保存成功，并能正确显示
'''

ssid = 'SAP_测试 123'

@pytest.fixture(autouse=True)
def setup_teardown():
    # pytest.executer.change_keyboard_language()
    pytest.executer.open_hotspot()
    logging.info('setup done')
    yield
    pytest.executer.reset_keyboard_language()
    pytest.executer.close_hotspot()

@pytest.mark.hot_spot
def test_hotspot_cn_char_ssid():
    pytest.executer.wait_and_tap('Hotspot name', 'text')
    pytest.executer.u().d2(resourceId="android:id/edit").clear_text()
    pytest.executer.checkoutput(f'am broadcast -a ADB_INPUT_TEXT --es msg  "{ssid}"')
    pytest.executer.wait_and_tap('GO','text')
    pytest.executer.keyevent(66)
    pytest.executer.wait_element('Hotspot name', 'text')
    assert ssid == pytest.executer.u().d2(resourceId="android:id/summary").get_text(), "ssid can't be set currently"
    pytest.executer.accompanying_dut_wait_ssid(ssid)
