#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 16:43
@Author  : Poco Ray
@File    : test_login.py
@Software: PyCharm
@Desc    : 登录页面测试
"""
from time import sleep

import allure
import pytest

from data.testData import TestData
from pages.loginPage import LoginPage


class TestLogin:
    # @pytest.mark.skipif(reason='skip')
    @pytest.mark.run(order=1)
    def test_login_success(self, driver):
        login_data = TestData.LoginInfo[0]
        login_page = LoginPage(driver, login_data['username'], login_data['password'])
        login_page.login()
        shopping_page = login_page.go_shopping()
        assert shopping_page.have_title(login_data['expect'])

    def test_login_fail(self, driver):
        login_data = TestData.LoginInfo[1]
        login_page = LoginPage(driver, login_data['username'], login_data['password'])
        login_page.login()
        fail_msg = login_page.get_fail_info()
        assert fail_msg.find(login_data['expect']) > 0
