---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-intelligentscene
title: 情景模式错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 情景模式错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:10:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6152bb4c76fc8c0f61e2ef4a7523d259802b4ff1d7ad07a24cfdbf086aa05607
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 35200001 内部错误

PhoneTablet

**错误信息**

Internal error.

**错误描述**

多线程处理异常、内部指针校验错误等内部处理错误时，方法将返回该错误码。

**可能原因**

多线程处理、内部处理异常等内核通用错误。

**处理步骤**

确认系统资源是否足够。
