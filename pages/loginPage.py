#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 16:20
@Author  : Poco Ray
@File    : loginPage.py
@Software: PyCharm
@Desc    : 登录页面对象类
"""
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.shoppingPage import ShoppingPage


class LoginPage(BasePage):
    ele_user = (By.ID, 'user-name')
    ele_password = (By.ID, 'password')
    ele_login_btn = (By.ID, 'login-button')
    ele_error_msg = (By.CSS_SELECTOR, '.error-message-container > h3')

    def __init__(self, driver, username, password):
        login_url = 'https://www.saucedemo.com/'
        super().__init__(driver)
        self.driver = driver
        self.open(login_url)
        self.user = username
        self.password = password

    def login(self):
        self.type(self.ele_user, self.user)
        self.type(self.ele_password, self.password)
        self.click(self.ele_login_btn)

    def get_fail_info(self):
        return self.get_text(self.ele_error_msg)

    def go_shopping(self):
        return ShoppingPage(self.driver)
