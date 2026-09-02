---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-68
title: 如何通过Hypium脚本实现多端连续滑动
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何通过Hypium脚本实现多端连续滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:23007c9c49cb1bd6451752ba3b56f355ea5f328392d8b9805c5778a26412a400
---

## 问题现象

如何利用Hypium实现UI自动化脚本，实现多端连续滑动，类似解锁图形密码操作？

## 背景知识

[应用UI测试（基于Python）](../harmonyos-guides/hypium-python-guidelines.md)：DevEco Testing Hypium(以下简称Hypium)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本，主要包含以下特性：

* Hypium提供了控件、图像、比例坐标等多种控件定位能力，支持多窗口操作以及触摸屏、鼠标、键盘等多种模拟输入功能，支持多设备并行操作，能够覆盖各类场景和多种形态设备上的自动化用例编写需求。
* Hypium包含配套用例编写辅助插件，支持控件查看、投屏操作等多种用例开发辅助功能，提升用例开发体验和效率。
* Hypium能够为执行的用例生成详细的用例执行报告，并且自动记录设备日志以及执行步骤截图，为开发者和测试人员提供高效和专业的测试用例执行和结果分析体验。

## 解决方案

通过手势对象的move\_to方法进行移动实现连续滑动效果。

```python
from devicetest.core.test_case import TestCase
from hypium import Gesture, Point, UiDriver
class TC_001(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, controllers)
        self.driver = UiDriver(self.device1)
    def setup(self):
        # 创建手势对象
        gesture = Gesture()
        # 起始位置, 长按2秒
        gesture.start(Point(360, 500).to_tuple(), 2)
        # 停留2秒
        gesture.pause(2)
        # 移动到(100, 500)的位置
        gesture.move_to(Point(100, 500).to_tuple())
        # 停留2秒结束
        gesture.pause(2)
        # 移动到(300, 500)的位置
        gesture.move_to(Point(300, 500).to_tuple())
        # 停留2秒结束
        gesture.pause(2)
        # 执行gesture对象描述的操作
        self.driver.inject_gesture(gesture)
```
