---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-errorcode-00404
title: hdc命令失败错误码
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 调试错误码 > hdc命令失败错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:57+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:58a2a9efff7c88882a8f3712037bbbdd096170e7922623fbbbacd81c00a11051
---

## 00404035 安装hap包超时

**错误信息**

Install hap timeout.

**错误描述**

安装hap包超时。

**可能原因**

设备连接异常或者hdc服务异常。

**处理步骤**

重新拔插下设备，或者执行hdc kill -r命令再重新运行。

## 00404036 删除临时目录超时

**错误信息**

Remove Directory Timeout: XXX.

**错误描述**

删除临时目录超时。

**可能原因**

设备连接异常或者hdc服务异常。

**处理步骤**

重新拔插下设备，或者执行hdc kill -r命令再重新运行。

## 00404037 创建临时目录超时

**错误信息**

Create Directory Timeout.

**错误描述**

创建临时目录超时。

**可能原因**

设备连接异常或者hdc服务异常。

**处理步骤**

重新拔插下设备，或者执行hdc kill -r命令再重新运行。

## 00404038 构建打包信息为空

**错误信息**

Build package info list is empty.

**错误描述**

构建打包信息为空。

**可能原因**

构建没有正确打包生成应用信息。

**处理步骤**

点击菜单栏**Build > Clean Project**清理缓存后重试。

## 00404039 创建临时目录失败

**错误信息**

Failed to create temporary directory during hap push operation.

**错误描述**

创建临时目录失败。

**可能原因**

设备连接异常或者hdc服务异常。

**处理步骤**

重新拔插下设备，或者执行hdc kill -r命令再重新运行。

## 00404040 推包超时

**错误信息**

Push Hap Timeout.

**错误描述**

推包超时。

**可能原因**

数据连接线非原装数据线导致传输速率不高，或者hdc服务异常。

**处理步骤**

换原装数据线，或者执行hdc kill -r命令再重新运行。

## 00404041 不支持方舟native模块加载异常信息增强

**错误信息**

Start ability failed:The current device version does not support enhance error info. Update device version or deselect the Enhanced Error Info.

**错误描述**

启动ability失败，不支持方舟native模块加载异常信息增强，请升级设备系统或者取消勾选方舟native模块加载异常信息增强功能。

**可能原因**

当前设备系统版本不支持方舟native模块加载异常信息增强。

**处理步骤**

请升级设备系统，或者在运行/调试配置面板取消勾选方舟native模块加载异常信息增强功能。

## 00404042 不支持方舟多线程检测

**错误信息**

The current device version does not support multi thread check. Update device version or deselect the Multi Thread Check.

**错误描述**

不支持方舟多线程检测，请升级设备系统或者取消勾选方舟多线程检测功能。

**可能原因**

当前设备系统版本不支持方舟多线程检测。

**处理步骤**

请升级设备系统，或者在运行/调试配置面板取消勾选方舟多线程检测功能。

## 00404053 不支持等待调试功能

**错误信息**

The current device version does not support the waiting for debugging capability. Update or upgrade the device version.

**错误描述**

当前设备系统版本不支持等待调试功能，请升级设备系统版本。

**可能原因**

当前设备系统版本不支持等待调试功能。

**处理步骤**

请升级当前设备系统版本。

## 00404054 等待调试命令执行超时

**错误信息**

Waiting for the debug command times out.

**错误描述**

等待调试命令执行超时。

**可能原因**

设备连接异常或者hdc服务异常。

**处理步骤**

重新拔插下设备，或者执行hdc kill -r命令再重试。

## 00404055 应用没安装或者不是debug签名

**错误信息**

This app is not installed or not signed with a debug signature.

**错误描述**

应用没安装或者不是debug签名。

**可能原因**

1. 通过命令设置应用进入等待调试模式失败，应用没安装或者不是debug签名；
2. 设备连接异常，执行命令失败。

**处理步骤**

1. 检查应用是否已安装，应用签名是否使用debug签名；
2. 检查设备连接是否正常，可以尝试拔插设备重新连接，再重新启动等待调试。
