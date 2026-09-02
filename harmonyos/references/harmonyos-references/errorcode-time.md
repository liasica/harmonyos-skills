---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-time
title: 时间时区服务错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 时间时区服务错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e582f33074cf6335945c66774d86101b79ff085408fdf248febba077eac9288f
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## -1 时间时区服务异常

**错误信息**

Parameter check failed, permission denied, or system error.

**错误描述**

时间时区服务异常。

**可能原因**

系统运行异常。内存申请、多线程处理等内核通用错误。

**处理步骤**

系统运行异常。请确认内存是否充足。

## 13000001 网络或操作系统异常

**错误信息**

Network connection error or OS error.

**错误描述**

网络或操作系统异常。

**可能原因**

网络或操作系统异常。网络无法连接或无法创建套接字等系统异常。

**处理步骤**

网络或操作系统异常。确认网络连接是否成功，系统资源是否足够。
