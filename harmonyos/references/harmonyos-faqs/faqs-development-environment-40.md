---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-40
title: DevEco Studio中快捷键使用常见问题
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio中快捷键使用常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77bfaa7e3dc8c4c5dba156507b88ebc570756f94086482d38711e3abdd3fa44b
---

## 问题现象

* 按键冲突：
  + 场景一：DevEco Studio快捷键Ctrl+shift+f，弹出正在搜索“这台Mac”。
* 按键使用：
  + 场景二：撤回、重做的快捷键Ctrl+Z和Ctrl+Y，但Ctrl+Y是删除行。
  + 场景三：如何为Open in Finder增加快捷键。

## 背景知识

[DevEco Studio](../harmonyos-guides/ide-tools-overview.md)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。

## 解决方案

* 按键冲突：
  + 场景一：
    - 方案一：修改DevEco Studio快捷键（推荐）：
      1. 打开快捷键设置：通过菜单栏进入：DevEco Studio>Preferences>Keymap（macOS路径：Settings>Keymap）。
      2. 修改全局搜索快捷键：

         2.1在搜索框输入Find in Files。

         2.2右键单击现有快捷键Ctrl+Shift+F→选择Remove。

         2.3添加新快捷键（如Ctrl+Shift+G）：→单击Add Keyboard Shortcut→输入新组合键→点击OK。
    - 方案二：关闭macOS系统快捷键冲突：
      1. 打开**系统设置**>**键盘**>**键盘快捷键**。
      2. 在左侧选择**聚焦**。
      3. 取消勾选显示聚焦搜索对应的快捷键（或修改为其他组合键）。
* 按键使用：
  + 场景二：
    - 首次使用Ctrl+Y快捷键会出现弹窗将该快捷键映射到重做或删除行，当时应该选择了删除行。想修改可以点击"File->Settings->Keymap"，在搜索中输入redo，选择edit目录下的快捷键，右键新增快捷键Ctrl+Y即可。
    - 若依旧未成功，重新依照上述步骤，在搜索中输入delete line，选择edit目录下的快捷键，右键移除快捷键Ctrl+Y即可。
  + 场景三：
    1. 打开DevEco Studio，点击菜单栏DevEco Studio-Preferences。
    2. 选择Keymap进入快捷键配置界面，在搜索框输入关键词"Finder"或"Reveal in"。
    3. 分配快捷键右键点击目标操作，选择Add Keyboard Shortcut然后保存即可。

## 常见FAQ

Q：如何更改对应功能的快捷键？

A：鼠标右键点击对应功能条目，通过弹出的菜单中Add XXX添加快捷方式、Remove XXX删除快捷方式。

Q：代码跳转的功能名称是什么？

A：Click Link inherited from Go to Declaration or Usages。
