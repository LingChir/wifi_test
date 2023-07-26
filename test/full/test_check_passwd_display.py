# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_check_passwd_display.py
# Time       ：2023/7/26 15:07
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
连接一个AP

1.WIFI列表中点击要连接的AP
2.输入密码时选择”隐藏密码“

连接AP时候，密码键盘输入界面，输入密码时，如果“显示密码”设置成disable,则输入的密码全部以“明码的”形式显示。
'''

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'Abc@123456'
router_5g = Router(band='5 GHz', ssid=ssid, wireless_mode='N/AC/AX mixed', channel='36', bandwidth='40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)

check_info = 'resource-id="com.android.tv.settings:id/password_checkbox" class="android.widget.CheckBox" package="com.android.tv.settings" content-desc="" checkable="true" checked="false"'


@pytest.fixture(scope='function', autouse=True)
def setup():
    # set router
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_5g)
    ax88uControl.router_control.driver.quit()
    yield
    pytest.executer.kill_tvsetting()


def test_check_passwd_display():
    pytest.executer.find_ssid(ssid)
    pytest.executer.text(passwd)
    pytest.executer.uiautomator_dump()
    assert ssid in pytest.executer.get_dump_info(),"Passwd can not be display"
