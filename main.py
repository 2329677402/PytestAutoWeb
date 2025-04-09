#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20
@Author  : Poco Ray
@File    : main.py
@Software: PyCharm
@Desc    : 主程序入口
"""
import os
import shutil
import pytest

if __name__ == '__main__':
    # 运行pytest并生成报告
    pytest.main()
    # 在测试开始运行，执行了--clean-alluredir的命令行参数后，再将environment.properties文件复制到allure-results目录下
    shutil.copy("environment.properties", "./allure-results/environment.properties")
    os.system("allure generate ./allure-results -o ./report --clean")