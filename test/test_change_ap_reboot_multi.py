# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_change_ap_reboot_multi.py
# Time       ：2023/8/14 15:56
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""



import logging
import time

import pytest

from Router import Router
from tools.Asusax88uControl import Asusax88uControl

'''
测试步骤
1.连接ssid
2.改变带宽
3.播放youtube
重复1-3
'''

ssid = 'ATC_ASUS_AX88U_2G'
passwd = '12345678'
router_20 = Router(band='2.4 GHz', ssid=ssid, wireless_mode='自动', channel='1', bandwidth='20 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)
router_40 = Router(band='2.4 GHz', ssid=ssid, wireless_mode='N only', channel='6', bandwidth='40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)
router_mix = Router(band='2.4 GHz', ssid=ssid, wireless_mode='Legacy', channel='11', bandwidth='20/40 MHz',
                   authentication_method='WPA2-Personal', wpa_passwd=passwd)

devices_list = ['12345678901234','12345678904321']
ax88uControl = Asusax88uControl()


@pytest.fixture(autouse=True, scope='session')
def setup():
    # ax88uControl.change_setting(router_ch11)
    # pytest.executer.connect_ssid(ssid, passwd)
    # pytest.executer.wait_for_wifi_address()
    yield
    ax88uControl.router_control.driver.quit()
    pytest.executer.forget_network_ssid(ssid)
    pytest.executer.kill_tvsetting()

def test_change_bandwidth():
    count = 0
    for i in [router_20, router_40, router_mix] * 3000:
        count += 1
        try:
            logging.info(f"测试第 {count} 轮 。。。")
            ax88uControl.change_setting(i)
            for j in devices_list:
                pytest.executer.serialnumber = j
                pytest.executer.checkoutput(pytest.executer.CMD_WIFI_CONNECT.format(ssid, 'wpa2', passwd))
                pytest.executer.wait_for_wifi_address()
                pytest.executer.reboot()
                pytest.executer.wait_devices()
                pytest.executer.wait_for_wifi_service()
                pytest.executer.wait_for_wifi_address()
                pytest.executer.forget_network_cmd()
        except Exception as e:
            ...
        # playback_youtube()
        # time.sleep(60)
