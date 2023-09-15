# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_5g_4k_seek.py
# Time       ：2023/9/14 10:46
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""

import logging
import pytest
import time
from tools.Asusax88uControl import Asusax88uControl
from Router import Router

ssid = 'ATC_ASUS_AX88U_5G'
passwd = 'test1234'
router_ausu = Router(band='5 GHz', ssid=ssid, wireless_mode='自动', channel='自动', bandwidth='20 MHz',
                     authentication_method='WPA2-Personal', wpa_passwd=passwd)


@pytest.fixture(autouse=True, scope='session')
def setup():
    logging.info('start setup')
    ax88uControl = Asusax88uControl()
    ax88uControl.change_setting(router_ausu)
    ax88uControl.router_control.driver.quit()
    time.sleep(3)
    pytest.executer.connect_ssid(ssid, passwd)
    yield
    pytest.executer.home()
    pytest.executer.forget_ssid(ssid)


def test_4k_playback():
    pytest.executer.playback_youtube(seek=True, seek_time=5)
