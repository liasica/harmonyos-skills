---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-debug
title: 使用预览器调试应用
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > 使用预览器调试应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e0f99bbdd024dc8bfc4402833aadf107a708252985d1f5600734021e19c2ea15
---

使用真机或模拟器进行调试时，修改后的代码需要经过较长时间的编译和安装过程，才能刷新至调试环境。使用预览器进行调试，可快速地修改代码和运行应用，在DevEco Studio中直接查看修改后的界面显示效果。

开发者可以使用预览器运行调试Ability生命周期代码和界面代码，预览器调试支持基础调试能力，包括断点、调试执行、变量查看等。

## 使用约束

* 一个工程内不支持启动多个预览调试任务。
* 一个预览器只能支持普通预览或预览调试模式，不可同时支持两种模式。
* 使用预览器进行调试不支持以下场景：
  + 不支持Attach调试。
  + 不支持跨Ability调试。
  + 不支持C++调试。
  + 不支持Hot Reload。
  + 不支持多进程和worker/taskpool调试。

## 普通预览与预览调试能力对比

**表1** 普通预览与预览调试能力对比

|  |  |  |  |
| --- | --- | --- | --- |
| **功能** | **普通预览** | **预览调试** | |
| **页面预览** | **运行模式** | **调试模式** |
| ets页面预览 | 支持 | 支持 | 支持 |
| 动态预览 | 支持 | 支持 | 支持 |
| 指定页面文件预览 | 支持 | 不支持 | 不支持 |
| Inspector双向预览 | 支持 | 从DevEco Studio 6.0.0 Beta2版本开始支持 | 从DevEco Studio 6.0.0 Beta2版本开始，支持查看，不支持修改 |
| 实时预览 | 支持 | 支持 | 断点中断时不支持 |
| 极速预览 | 支持 | 从DevEco Studio 6.0.0 Beta2版本开始支持 | 不支持 |
| 组件预览 | 支持 | 不支持 | 不支持 |
| 多语言切换 | 支持 | 从DevEco Studio 6.0.0 Beta2版本开始支持 | 从DevEco Studio 6.0.0 Beta2版本开始支持，但断点中断时不支持 |
| 动态修改分辨率 | 支持 | 从DevEco Studio 6.0.0 Beta2版本开始，支持横竖屏切换 | 从DevEco Studio 6.0.0 Beta2版本开始，支持横竖屏切换，但断点中断时不支持 |
| 引用HSP | 从DevEco Studio 6.0.0 Beta3版本开始支持 | | |
