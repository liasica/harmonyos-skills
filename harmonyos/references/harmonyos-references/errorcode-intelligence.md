---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-intelligence
title: 智慧数据平台错误码
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > 错误码 > 智慧数据平台错误码
category: harmonyos-references
scraped_at: 2026-04-28T07:59:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4678196646e0f2ece72e25d12c79a03497c17a04e07ef7d9cd205d5246ed72d
---

说明：

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 31300000 服务内部异常

PhonePC/2in1Tablet

**错误信息**

Inner error.

**错误描述**

当调用智慧数据平台模块相关接口时，若服务内部异常，会报此错误码。

**可能原因**

服务内部状态异常，例如应用在没有加载对应嵌入模型后调用获取对应嵌入向量的结果，此时属于模型未加载，获取向量化接口就是异常调用。

**处理步骤**

1. 开发者排查是否按接口文档正确使用接口。
2. 定时重试操作，如间隔1s或者按照指数增长间隔重试，如果依然无法解决，可以提示用户重启应用、升级应用或升级设备版本。
