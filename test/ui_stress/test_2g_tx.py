# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_2g_tx.py
# Time       ：2023/9/13 16:01
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""



import logging
import time

import pytest
from tools.Asusax88uControl import Asusax88uControl
from Router import Router
from Iperf import Iperf
'''
测试步骤
2G-TX

1.连接2g网络
3.配合终端A
4.tps 测试 TX

TPS正常，无掉零
'''

ssid = 'ATC_ASUS_AX88U_2G'
passwd = 'Abc@123456'

router = Router(band='2.4 GHz', ssid=ssid, wireless_mode='AX only', channel='1', bandwidth='20/40 MHz',
                    authentication_method='WPA2-Personal', wpa_passwd=passwd)

ax88uControl = Asusax88uControl()
iperf = Iperf()

@pytest.fixture(autouse=True)
def setup_teardown():
    ax88uControl.change_setting(router)
    ax88uControl.router_control.driver.quit()
    time.sleep(3)
    pytest.executer.connect_ssid(ssid, passwd)
    logging.info('setup done')
    yield
    pytest.executer.home()
    pytest.executer.forget_ssid(ssid)
    pytest.executer.IPERF_TEST_TIME = 30


@pytest.mark.hot_spot
def test_2g_iperf_tx():
    pytest.executer.IPERF_TEST_TIME = 3600*24
    assert iperf.run_iperf(type='tx'),'iperf with error'