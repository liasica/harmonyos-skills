---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-74
title: Hypium中，如何判断当前屏幕为横屏或竖屏
breadcrumb: FAQ > DevEco Studio > 应用调试 > Hypium中，如何判断当前屏幕为横屏或竖屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b73f5c658078e314e3b2cf236d53e420e1038c9187583f51dc735abce7fee29b
---

## 问题现象

Hypium中，执行视频类应用的全屏或者游戏类应用横屏时，应当如何判断当前为横屏还是竖屏？

## 背景知识

[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用Python语言为应用编写UI自动化测试脚本，主要包含以下特性：

1. Hypium提供了控件/图像/比例坐标等多种控件定位能力，支持多窗口操作以及触摸屏/鼠标/键盘等多种模拟输入功能，支持多设备并行操作，能够覆盖各类场景和多种形态设备上的自动化用例编写需求。
2. Hypium包含配套用例编写辅助插件,支持控件查看/投屏操作等多种用例开发辅助功能，提升用例开发体验和效率。
3. Hypium能够为执行的用例生成详细的用例执行报告，并且自动记录设备日志以及执行步骤截图，为开发者和测试人员提供高效和专业的测试用例执行和结果分析体验。

参考[窗口旋转说明](../best-practices/bpta-landscape-and-portrait-development.md#section388473115175)，窗口旋转形态有以下四种，分别为顺时针方向旋转0度（竖屏），旋转90度（反向横屏），旋转270度（横屏），旋转180度（反向竖屏）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/hIEECqOvSdCaZ-wysLO1ag/zh-cn_image_0000002628569338.png "点击放大")

## 解决方案

```python
# -*- coding: utf-8 -*-
from devicetest.core.test_case import TestCase, Step
from hypium import UiDriver
class TC_001(TestCase):
    def __init__(self, configs):
        self.TAG = self.__class__.__name__
        super().__init__(self.TAG, configs)
        self.driver = UiDriver(self.device1)
        self.driver_width, self.driver_height = self.driver.get_display_size()
    def setup(self):
        Step("预制条件")
    def process(self):
        Step("方法一：使用driver.get_display_size()方法获取当前屏幕的宽和高，当宽>高时，即为横屏，反之为竖屏。")
        # 获取当前屏幕尺寸
        display = self.driver.get_display_size()
        # 屏幕宽度（像素）
        width = display[0]
        # 屏幕高度（像素）
        height = display[1]
        # 当屏幕宽度>屏幕高度，表示当前为横屏观看,否则为竖屏
        if width > height:
            current_orientation = "landscape"
        else:
            current_orientation = "portrait"
        print(f"当前屏幕方向: {current_orientation}")
        Step("方法二：使用driver.get_display_rotation()方法获取当前手机方向")
        # 获取当前屏幕方向，正常横屏值为：DisplayRotation.ROTATION_270、DisplayRotation.ROTATION_90，竖屏为：DisplayRotation.ROTATION_0
        current_orientation = self.driver.get_display_rotation()
        print(f"当前屏幕方向: {current_orientation}")
    def teardown(self):
        Step("收尾工作xxxx")
```
