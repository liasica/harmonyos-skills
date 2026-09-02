---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-perftest
title: PerfTest错误码
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > 错误码 > PerfTest错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0d401f58bfce512b7963341992a6fad49609994d258675e0d7cbb4c62898538
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 32400001 初始化失败

**错误信息**

Initialization failed.

**错误描述**

框架初始化失败。

**可能原因**

无法获取测试应用包名。

**处理步骤**

检查测试应用是否正常安装并可用，确保能够成功获取测试应用包名。

## 32400002 内部错误

**错误信息**

Internal error.

**错误描述**

框架内部运行出现错误。

**可能原因**

1. IPC传输失败。
2. PerfTest对象不存在。

**处理步骤**

1. 尝试通过重试解决IPC传输失败问题。
2. 判断PerfTest对象是否已被销毁，若已销毁需要重新使用[PerfTest.create](js-apis-perftest.md#create)创建PerfTest对象。

## 32400003 参数校验失败

**错误信息**

Parameter verification failed.

**错误描述**

参数校验失败。

**可能原因**

参数类型错误、参数取值超出规定范围。

**处理步骤**

检查接口入参的类型和取值范围是否符合接口定义要求。

## 32400004 执行回调函数失败

**错误信息**

Failed to execute the callback.

**错误描述**

执行回调函数失败。

**可能原因**

1. 回调函数内部抛出异常。
2. 回调函数执行超时。

**处理步骤**

检查回调函数内部逻辑，包括异常处理和超时控制机制，确保回调函数执行不会抛出异常或超时。

## 32400005 采集性能数据失败

**错误信息**

Failed to collect metric data.

**错误描述**

采集性能数据失败。

**可能原因**

采集性能数据时，被测应用进程不存在。

**处理步骤**

使用ps等shell命令查看，确保采集性能数据时被测应用进程存在。

## 32400006 无法获取性能数据

**错误信息**

Failed to obtain the measurement result.

**错误描述**

无法获取指定性能指标对应的测试数据。

**可能原因**

测试数据未采集完成。

**处理步骤**

首先保证[PerfTest.run](js-apis-perftest.md#run)接口已执行完成且未抛出异常，确保测试数据已采集完成，再获取指定数据。

## 32400007 接口不支持并行调用

**错误信息**

The API does not support concurrent calls.

**错误描述**

接口不支持并行调用。

**可能原因**

异步API没有使用await等待异步执行完成，导致出现接口并行调用。

**处理步骤**

使用await同步等待异步函数执行完成。
