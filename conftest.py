#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 14:57
@Author  : Poco Ray
@File    : conftest.py
@Software: PyCharm
@Desc    : 公共的测试配置文件
"""
import time
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    option = webdriver.ChromeOptions()
    option.page_load_strategy = 'eager'  # 设置页面加载策略，可选项：normal, eager, none
    option.unhandled_prompt_behavior = 'dismiss'  # 设置未处理的弹窗行为，可选项：dismiss and notify, ignore, dismiss, accept, accept and notify
    option.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])  # 排除日志和自动化开关
    option.add_argument('headless') # 无头模式
    driver = webdriver.Chrome(options=option)
    try:
        driver.maximize_window()
        driver.implicitly_wait(3)
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope='function', autouse=True)
def sleep():
    time.sleep(2)
