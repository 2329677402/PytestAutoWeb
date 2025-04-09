#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
@Date    : 2025/3/20 14:59
@Author  : Poco Ray
@File    : basePage.py
@Software: PyCharm
@Desc    : 基础页面对象类——页面的公共操作方法
"""
from typing import Union, Tuple
from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url: str) -> None:
        """
        Open the specified URL.

        :param url: URL web address.
        :return: None
        """
        self.driver.get(url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        """
        Find a single element.

        :param locator: The locator of the element.
        :return:
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """
        Find multiple elements.

        :param locator: The locator of the elements.
        :return:
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def _get_element(self, element) -> WebElement:
        """
        Get the element.

        :param element:
        :return:
        """
        if isinstance(element, WebElement):
            return element
        elif not isinstance(element, WebElement) and len(element) == 2:
            return self.find_element(element)
        else:
            raise ValueError("Invalid element type or locator format.")

    def _take_error_screenshot(self, info: str) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(f"{info}_{timestamp}.png")

    def click(self, element: Union[WebElement, tuple[str, str]]) -> None:
        """
        Click the element.

        :param element: The element to be clicked.
        :return: None
        """
        try:
            ele = self.wait.until(EC.element_to_be_clickable(self._get_element(element)))
            ele.click()
        except Exception as e:
            self._take_error_screenshot("click_error")
            print(f"Error clicking element: {e}")
            raise

    def type(self, element: WebElement or tuple[str, str], content: str) -> None:
        """
        Input content into the element.

        :param element: The element to be input.
        :param content: The content to be input.
        :return:
        """
        if isinstance(element, WebElement):
            ele = element
        else:
            ele = self.find_element(element)
        ele.send_keys(content)

    def get_text(self, element: WebElement or tuple[str, str]) -> str:
        """
        Get the text of the element.

        :param element: The element to get text.
        :return:
        """
        if isinstance(element, WebElement):
            ele = element
        else:
            ele = self.find_element(element)
        return ele.text
