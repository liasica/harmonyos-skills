---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-colorspace-manager
title: 色彩管理错误码
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 错误码 > 色彩管理错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3de91a1a4436a304c6ee9ba2f4ebacd6ebd276a7ccd047e248c75f0dba39686b
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 18600001 参数值异常

**错误信息**

The parameter value is abnormal.

**错误描述**

当参数值不符合接口调用要求时，系统返回此错误码。

**可能原因**

参数值超出接口调用范围时会返回错误码，如枚举值超出定义范围。

**处理步骤**

在定义接口参数前，确保参数值符合接口参数要求。
