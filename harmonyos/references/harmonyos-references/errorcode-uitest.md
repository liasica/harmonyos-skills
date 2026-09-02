---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest
title: UiTest错误码
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > 错误码 > UiTest错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95424cdc4f57c7d8e51a581a76c077ef8ef9152bcd0d6a01e1abee7a80f34a3a
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 17000001 初始化失败

**错误信息**

Initialization failed.

**错误描述**

框架初始化失败。

**可能原因**

无法连接到无障碍服务。

**处理步骤**

执行param set persist.ace.testmode.enabled 1，并重启设备。

## 17000002 接口不支持并发调用

**错误信息**

The API does not support concurrent calls.

**错误描述**

接口不支持并发调用。

**可能原因**

异步API没有使用await等待异步执行完成，导致出现接口并发调用。

**处理步骤**

请确保同一时间只执行一个API调用，异步函数使用await同步等待执行完成。

## 17000003 断言失败

**错误信息**

Assertion failed.

**错误描述**

用户断言失败。

**可能原因**

用户断言存在的控件实际不存在。

**处理步骤**

检查用户断言存在的控件实际是否存在。

## 17000004 目标控件/窗口不可见或已销毁

**错误信息**

The window or component is invisible or destroyed.

**错误描述**

目标控件/窗口不可见或已销毁，无法进行操作。

**可能原因**

获取到目标控件或窗口后，页面发生变化导致目标丢失。

**处理步骤**

检查获取到目标控件或窗口后，页面是否发生变化导致目标丢失。

## 17000005 操作不支持

**错误信息**

This operation is not supported.

**错误描述**

UI对象不支持该操作。

**可能原因**

当前界面控件/窗口属性/设备不支持该操作。

**处理步骤**

检查当前界面控件/窗口属性/设备是否支持该操作。

## 17000007 参数不合法

**错误信息**

Parameter verification failed.

**错误描述**

参数校验失败。

**可能原因**

参数类型错误/参数取值超出规定范围。

**处理步骤**

检查接口入参是否符合要求。
