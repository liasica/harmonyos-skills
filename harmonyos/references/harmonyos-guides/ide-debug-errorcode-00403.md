---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-errorcode-00403
title: 调试失败错误码
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 调试错误码 > 调试失败错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:56+08:00
doc_updated_at: 2026-02-12
content_hash: sha256:c037f0a17db7fc163e39ef4d2d8daaa2bea118e8b13a66698acb0e1bc9054962
---

## 00403001 离线日志解析失败

**错误信息**

Failed to parse the HiLog file: XXX.

**错误描述**

离线日志解析失败。

**可能原因**

离线日志解析失败。

**处理步骤**

重新选择离线日志。

## 00403003 应用堆栈解析出现错误

**错误信息**

应用堆栈解析相关报错，具体报错视情况而定。

**错误描述**

应用堆栈解析出现错误。

**可能原因**

根据报错提示信息来查找原因，具体参考处理步骤。

**处理步骤**

参考[Release应用堆栈解析相关错误提示及解决措施](../harmonyos-faqs/faqs-app-debugging-17.md)。

## 00403028 应用程序意外退出

**错误信息**

App have been shutdown unexpectedly.

**错误描述**

应用程序意外退出。

**可能原因**

应用程序意外退出，因此调试服务也退出。

**处理步骤**

重新启动调试。

## 00403029 sourceMaps.map文件内容为空

**错误信息**

The JSON content is empty when the sourceMaps.map file is read.

**错误描述**

读取sourceMaps.map文件时，JSON内容为空。

**可能原因**

sourceMaps.map文件内容为空。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试。

## 00403030 连接WebSocket失败

**错误信息**

Failed to connect to the WebSocket. Restart the debugging. If the problem persists, restart DevEco Studio and start debugging again.

**错误描述**

无法连接到WebSocket。请重新启动调试。如果问题仍然存在，请重启DevEco Studio并重新启动调试。

**可能原因**

1. 连接WebSocket失败。
2. 如果是2in1设备，可能是应用开启了应用加速服务。

**处理步骤**

1. 请重新启动调试。如果问题仍然存在，请重启DevEco Studio并重新启动调试。
2. 如果是2in1设备，请在设备的**设置 > 应用加速服务**中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。

## 00403031 进程pid无效

**错误信息**

The process has invalid pid.

**错误描述**

进程pid无效。

**可能原因**

获取进程pid失败。

**处理步骤**

请重新启动调试。

## 00403032 连接调试服务器失败

**错误信息**

Failed to connect to the debug server. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**错误描述**

无法连接到调试服务器。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

**可能原因**

连接panda server失败。

**处理步骤**

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

## 00403033 获取ROM镜像版本失败

**错误信息**

Failed to obtain the ROM image version.

**错误描述**

获取ROM镜像版本失败。

**可能原因**

设备连接异常。

**处理步骤**

重新连接设备，或者执行hdc kill -r重启hdc后再重试。

## 00403043 预览器启动失败

**错误信息**

Failed to start the Previewer. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**错误描述**

预览器启动失败。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

**可能原因**

预览调试启动失败。

**处理步骤**

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

## 00403044 仿真器启动失败

**错误信息**

Failed to start the simulator. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

**错误描述**

仿真器启动失败。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

**可能原因**

仿真器启动失败。

**处理步骤**

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

## 00403045 编译失败

**错误信息**

Compilation failed.

**错误描述**

编译失败。

**可能原因**

编译失败。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试。

## 00403046 找不到Jerry适配器文件

**错误信息**

Jerry adapter file not found.

**错误描述**

找不到Jerry适配器文件。

**可能原因**

安装目录下找不到Jerry适配器文件。

**处理步骤**

在官网上重新[下载DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00403047 node路径无效

**错误信息**

Node path is invalid.

**错误描述**

Node路径无效。

**可能原因**

无法获取node路径。

**处理步骤**

检查DevEco Studio安装目录的tools目录下是否存在node工具，如果不存在，在官网上重新[下载DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00403048 无法启动webpack

**错误信息**

Unable to start webpack.

**错误描述**

无法启动webpack。

**可能原因**

webpack服务启动失败。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试，如果未解决，重启DevEco Studio。

## 00403049 预览插件未完全安装

**错误信息**

The Previewer plugin not fully installed. Please verify.

**错误描述**

预览插件未完全安装。请确认。

**可能原因**

预览插件未完全安装。

**处理步骤**

在官网上重新[下载DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)。

## 00403050 Jerry适配器无法连接到服务器

**错误信息**

Jerry Adapter fails to connect to the engine.

**错误描述**

Jerry适配器无法连接到服务器。

**可能原因**

Jerry调试连接失败。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试，如果未解决，重启DevEco Studio。

## 00403051 Jerry调试引擎异常停止

**错误信息**

Adapter server or engine stopped abnormally.

**错误描述**

Jerry调试引擎异常停止。

**可能原因**

Jerry调试引擎异常停止。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试，如果未解决，重启DevEco Studio。
