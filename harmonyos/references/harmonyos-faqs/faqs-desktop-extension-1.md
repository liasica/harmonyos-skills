---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-desktop-extension-1
title: HarmonyOS PC应用接入状态栏如何实现鼠标悬停弹出气泡提示？
breadcrumb: FAQ > 系统开发 > 基础功能 > 桌面拓展服务（Desktop Extension Kit） > HarmonyOS PC应用接入状态栏如何实现鼠标悬停弹出气泡提示？
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:c80ff18c37b7d32a849655fcb82c2b2e61203a12b8ad67ef39b6996957565228
---

## 问题现象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/uYptuvjAQn2PZrGGM6N_Ow/zh-cn_image_0000002689159868.png "点击放大")

HarmonyOS PC应用接入状态栏后应该如何配置才能实现在鼠标悬停时弹出气泡提示？

## 背景知识

* [Desktop Extension Kit（桌面拓展服务）](../harmonyos-references/status-bar-extension-api.md)：提供系统级统一的操作入口，支持应用快捷功能接入桌面，注意该模块提供的接口能力只支持中国境内（不包含中国香港、中国澳门、中国台湾），仅在PC/2in1设备上生效。
* [statusBarManager.QuickOperation](../harmonyos-references/statusbar-extension-manager.md#quickoperation)：用于构建左键业务弹窗信息。

## 解决方案

1. 参考应用接入状态栏[开发步骤](../harmonyos-guides/statusbar-extension-guide.md#开发步骤)，先调用[statusBarManager.QuickOperation](../harmonyos-references/statusbar-extension-manager.md#quickoperation)构建左键业务弹窗信息，以下为关键代码：

   ```ts
   // 构建点击状态栏图标时弹出的快捷操作窗口
   let operation: statusBarManager.QuickOperation = {
     abilityName: 'MyStatusBarViewAbility',
     title: 'Test Demo',
     height: 300,
     moduleName: 'entry'
   };
   ```

   完整接入示例可参考官方教程：[接入状态栏开发](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_StatusBarExtensionKit)。
2. 将上述[statusBarManager.QuickOperation](../harmonyos-references/statusbar-extension-manager.md#quickoperation)的moduleName参数设置为所在模块对应module.json5中module-name字段。要实现鼠标悬停于状态栏时弹出气泡提示，则当前moduleName不可缺省，若未配置moduleName参数，该参数默认为''，则鼠标悬停时不会显示气泡提示，如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/-xE0pMFKRWuSVw-8SIlLKA/zh-cn_image_0000002718999953.png)
3. 设置状态栏悬停气泡展示内容：需在接入状态栏提供的模块名对应/moduleName/src/main目录下的module.json5文件中，找到对应的abilities-label字段，修改该关键字对应的value值。注意：状态栏label和应用窗口对应的名称是相同字段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/3BS9T-r7Q0yW38Y2CjRUZg/zh-cn_image_0000002719000127.png "点击放大")

## 常见FAQ

Q：PC端应用的系统托盘图标，是否支持根据鼠标左键或右键点击，分别弹出不同的快捷菜单？

A：系统托盘图标能够识别左键操作：[statusBarManager.QuickOperation](../harmonyos-references/statusbar-extension-manager.md#quickoperation)，但暂不支持快捷菜单的控制。支持右键操作：[statusBarManager.StatusBarGroupMenu](../harmonyos-references/statusbar-extension-manager.md#statusbargroupmenu)，弹出快捷菜单。

Q：状态栏托盘图标是否支持闪烁或动态改变图标样式？

A：当前没有接口直接提供图标闪烁的能力。可以通过白图标和正常图标交替出现的方式模拟闪烁效果，调用[statusBarManager.updateStatusBarIcon](../harmonyos-references/statusbar-extension-manager.md#statusbarmanagerupdatestatusbaricon)接口实现图标更新。
