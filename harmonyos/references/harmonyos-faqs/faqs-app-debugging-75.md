---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-75
title: Hypium中多种进行系统返回键操作方法
breadcrumb: FAQ > DevEco Studio > 应用调试 > Hypium中多种进行系统返回键操作方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dafc8f550ef9aef8571247df4fd295c5fa3f36286aecec1b657261ab0cd56a46
---

## 问题现象

使用[Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)编写UI自动化用例时，如果某个页面没有返回键按钮，如何模拟系统返回键进行返回操作？

## 解决方案

```screen
# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step
from hypium import UiDriver, KeyCode
from hypium.model import UiParam
class TC_001(TestCase):
    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()
    def setup(self):
        Step('1.回到桌面')
        self.driver.swipe_to_home()
    def process(self):
        Step('2.多种系统返回操作方法')
        # 方法一,通过swipe_to_back()方法返回
        self.driver.start_app("com.huawei.hmos.browser")
        self.driver.wait(3)
        self.driver.swipe_to_back()
        # 方法二,通过go_back()方法返回
        self.driver.start_app("com.huawei.hmos.browser")
        self.driver.wait(3)
        self.driver.go_back()
        # 方法三,通过press_key(KeyCode.BACK)方法返回
        self.driver.start_app("com.huawei.hmos.browser")
        self.driver.wait(3)
        self.driver.press_key(KeyCode.BACK)
        # 方法四,通过模拟屏幕边缘向左或向右滑动手势返回，设置起点的相对坐标尽量靠近屏幕边缘，防止操作页面内的控件左滑或右滑
        self.driver.start_app("com.huawei.hmos.browser")
        self.driver.wait(3)
        self.driver.swipe(UiParam.RIGHT, distance=30, start_point=(0.01, 0.5))
        self.driver.start_app("com.huawei.hmos.browser")
        self.driver.wait(3)
        self.driver.swipe(UiParam.LEFT, distance=30, start_point=(0.99, 0.5))
    def teardown(self):
        Step('3.关闭华为浏览器')
        self.driver.stop_app("com.huawei.hmos.browser")
```
