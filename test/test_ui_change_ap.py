#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


"""
# File       : test_ui_change_ap.py
# Time       ：2023/7/10 18:37
# Author     ：chao.li
# version    ：python 3.9
# Description：
"""

import logging
import re
import time

import pytest

'''
测试步骤
切换ap
'''

ssid1 = 'sunshine'
ssid2 = 'galaxy'


@pytest.fixture(autouse=True,scope='session')
def setup():
    logging.info('start setup')
    # pytest.executer.connect_ssid(ssid1, 'Home1357')
    # pytest.executer.kill_tvsetting()
    # pytest.executer.connect_ssid(ssid2, 'Qatest123')
    pytest.executer.kill_tvsetting()
    yield
    pytest.executer.kill_tvsetting()
    pytest.executer.home()


@pytest.mark.repeat(5000)
def test_change_ap():
    pytest.executer.connect_save_ssid(ssid1, target='10.18')
    pytest.executer.kill_tvsetting()
    # pytest.executer.playback_youtube()
    pytest.executer.connect_save_ssid(ssid2, target='10.18')
    pytest.executer.kill_tvsetting()
    # pytest.executer.playback_youtube()
