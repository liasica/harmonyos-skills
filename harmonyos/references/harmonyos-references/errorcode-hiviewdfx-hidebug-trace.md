---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-trace
title: HiDebug Trace错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > HiDebug Trace错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3b1c6bd45994db814077659ae88425cacf32092da1d9c03ba33a0684d694ce8
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 11400102 重复采集

**错误信息**

Capture trace already enabled.

**错误描述**

进程已开启trace采集。

**可能原因**

进程正在进行trace采集。

**处理步骤**

应等待trace采集结束或调用hidebug.stopAppTraceCapture接口关闭正在运行的trace采集，以解决重复采集问题。

## 11400103 权限校验失败

**错误信息**

No write permission on the file.

**错误描述**

当前目录没有权限写trace文件。

**可能原因**

目录不存在或被误操作删除。

**处理步骤**

应重新运行采集接口，再次生成正确的目录文件，以解决权限校验失败问题。

## 11400104 内部异常

**错误信息**

Abnormal trace status.

**说明** 

错误信息请以接口实际返回内容为准。

**错误描述**

当前trace采集内部状态异常。

**可能原因**

系统内核崩溃或应用进程无响应。

**处理步骤**

应重启应用或设备，以解决trace采集内部状态异常问题。

## 11400105 未开启trace采集

**错误信息**

No capture trace running.

**错误描述**

当前没有trace正在采集。

**可能原因**

未开启trace采集。

**处理步骤**

确保在调用停止trace采集接口前，已经成功开启trace采集。

## 11400106 接口调用配额已超出

**错误信息**

Quota exceeded.

**错误描述**

接口调用配额已超出。

**可能原因**

1. 进程调用次数超出配额（1次/天）。
2. 整机调用次数超出配额（5次/周）。

**处理步骤**

应等待进程或整机的调用配额刷新，以解决接口调用配额已超出问题。

## 11400120 trace文件存储达到限制

**错误信息**

Trace storage limit reached.

**错误描述**

采集trace返回的.sys文件在目录下的存储超出限制。

**可能原因**

采集trace返回的.sys文件在目录下的数量大于等于3份。

**处理步骤**

应清理trace目录下的文件，以解决trace文件存储达到限制问题。

## 11400302 trace采集超出资源配额

**错误信息**

Resource unavailable.

**错误描述**

应用调用trace采集超出系统资源配额。

**说明** 

开发者模式下[debug版本应用](../harmonyos-guides/performance-analysis-kit-terminology.md#debug版本应用)不被管控。

**可能原因**

应用调用trace采集超出系统资源的每日配额。

**处理步骤**

应等待次日系统资源配额刷新，以解决trace采集超出资源配额问题。
