---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-policy
title: 策略管理错误码
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 错误码 > 策略管理错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ac3078005b898320a7224991a96edb1228a7c8b46039b76dbbb69aab9f72421
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 2100001 无效的参数

**错误信息**

Invalid parameter value.

**错误描述**

参数输入有误。

**可能原因**

输入的结束时间小于开始时间。

**处理步骤**

检查输入的时间参数是否合理。

## 2100002 连接服务失败

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

服务发生异常。

**处理步骤**

检查系统服务运行状态是否正常。

## 2100003 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

1. 内存异常。
2. 空指针。

**处理步骤**

1. 检查内存空间是否充足，清理内存后重试。
2. 系统异常，请稍后重试或重启设备。
