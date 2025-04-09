#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 17:08
@Author  : Poco Ray
@File    : shoppingPage.py
@Software: PyCharm
@Desc    : 购物页面对象
"""

from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class ShoppingPage(BasePage):
    ele_title = (By.CLASS_NAME, 'title')
    ele_cart_count = (By.CLASS_NAME, 'shopping_cart_badge')
    ele_cart = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def have_title(self, txt):
        return self.get_text(self.ele_title) == txt

    def add_cart(self, product_id):
        ele_add_cart = (By.ID, product_id)
        add_cart_btn = self.find_element(ele_add_cart)
        self.click(add_cart_btn)

    def get_product_count(self):
        try:
            return int(self.get_text(self.ele_cart_count))
        except Exception:
            return 0

    def add_cart_by_name(self, product):
        pass

    def to_cart(self):
        self.click(self.ele_cart)
