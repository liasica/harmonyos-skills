---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-15
title: DevEco Testing Hypium录制回放功能如何操作
breadcrumb: FAQ > DevEco Studio > 应用测试 > DevEco Testing Hypium录制回放功能如何操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e67281a5aa58b35db5d8261b1e286adf1d977b4658c32f6d502529b43614b6f6
---

## 问题现象

Hypium UI自动化有录制回放工具，在HarmonyOS的UI自动化中使用Hypium的录制回放功能应该如何操作？

## 背景知识

[DevEco Testing Hypium](../harmonyos-guides/hypium-python-guidelines.md#section16890204264419)是HarmonyOS NEXT配套UI自动化测试框架，支持开发者使用Python语言为应用编写UI自动化测试脚本、性能测试脚本，覆盖全场景多形态设备上的自动化用例编写需求。

## 解决方案

UIViewer面板功能脚本录制按钮，点击后页面左上角将出现红色提示文字，提示进入录制状态，处于此状态时，点击画面中控件后，将在编辑器光标处生成Hypium用例测试语句。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/qqjI32BUSkiZhUMbXoqEWg/zh-cn_image_0000002658808809.png "点击放大")

* 点击控件录制；

  处于录制状态后，点击需要录制点击的控件，同时会在代码区域生成点击该控件的代码步骤。如点击桌面设置图标进入设置页面，生成代码如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/p8rEheoLQJaHEU4RFKurWA/zh-cn_image_0000002628409544.png "点击放大")

  ```python
  # 根据条件点击控件
  self.driver.touch(BY.key(
      'AppIcon_Image_com.huawei.hmos.settingscom.huawei.hmos.settings.MainAbilityphone_settings0_undefined'))
  self.driver.wait(0.5)
  ```
* 录制文本输入操作；

  处于录制状态后，输入文本功能按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/cL4LpKznR_WCI1G_wtIQGQ/zh-cn_image_0000002628569442.png)点击后，在[TextArea](../harmonyos-references/ts-basic-components-textarea.md)控件或[TextInput](../harmonyos-references/ts-basic-components-textinput.md)类型控件上方点击，会弹出文本输入框，用户输入完文本后，就会在当前代码编辑区的光标处插入一条由Hypium实现的输入代码。如搜索框输入搜索内容生成代码如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/1xWpCbGtSBW40yNqSOM31Q/zh-cn_image_0000002658928759.png "点击放大")

  ```python
  # 输入文本'Hello'
  self.driver.input_text(BY.key('__SearchField__searchComponent'), 'Hello')
  self.driver.wait(0.5)
  ```

## 常见FAQ

Q：双设备如何投屏(录制)界面？

A：双设备界面的功能与单设备的投屏(控件)界面功能相同，只是展示设备的数量变为2个。对某个设备进行控件查看时，会自动退出双设备投屏界面，回到单设备的控件查看界面。
