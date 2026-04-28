---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-faultlogger
title: Faultlogger 错误码
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误码 > Faultlogger 错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:11:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b50dacce9d9f128eb1af85d79cea2a629e8bea1804c69c3d8beee3d25408e60b
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 10600001 服务未启动或故障

PhonePC/2in1TabletTVWearable

**错误信息**

The service is not started or is faulty.

**错误描述**

服务未启动或者遇到未知错误。

**可能原因**

hiview服务未启动。

**处理步骤**

不应该发生的场景，考虑重试。
