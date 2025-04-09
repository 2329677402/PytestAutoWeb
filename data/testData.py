#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 17:01
@Author  : Poco Ray
@File    : testData.py
@Software: PyCharm
@Desc    : 测试数据类
"""


class TestData:
    LoginInfo = [
        {'username': 'standard_user', 'password': 'secret_sauce', 'expect': 'Products'},
        {'username': 'locked_out_user', 'password': 'secret_sauce', 'expect': 'locked out.'},
    ]

    Products = [
        {'name': 'Backpack', 'id': 'add-to-cart-sauce-labs-backpack', 'price': 29.99},
        {'name': 'Bike Light', 'id': 'add-to-cart-sauce-labs-bike-light', 'price': 9.99}
    ]

    CheckInfo = {
        'firstName': '城下秋草',
        'lastName': '黄',
        'postCode': '123456',
    }
