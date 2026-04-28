---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-colorspace-manager
title: 色彩管理错误码
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 错误码 > 色彩管理错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:15:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b2bec7acb39825037c0a5e816c45affc6c90e04b4fc30dbbea474a3813007da2
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 18600001 参数值异常

PhonePC/2in1TabletTVWearable

**错误信息**

The parameter value is abnormal.

**错误描述**

当参数值不符合接口调用要求时，系统会报此错误码。

**可能原因**

参数值超出接口调用范围会报错，如枚举值超出定义范围。

**处理步骤**

在定义接口参数前，确保参数值符合接口参数要求。
