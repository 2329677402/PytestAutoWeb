#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 17:40
@Author  : Poco Ray
@File    : test_shopping.py
@Software: PyCharm
@Desc    : Description
"""
import pytest
from data.testData import TestData
from pages.shoppingPage import ShoppingPage

count = 0
class TestShopping:
    @pytest.mark.parametrize('product', TestData.Products)
    @pytest.mark.run(order=2)
    def test_add_cart(self, driver, product):
        shopping_page = ShoppingPage(driver)
        shopping_page.add_cart(product['id'])
        global count
        count += 1
        assert shopping_page.get_product_count() == count

