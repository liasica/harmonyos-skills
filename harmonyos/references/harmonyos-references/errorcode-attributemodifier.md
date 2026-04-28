---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-attributemodifier
title: 动态属性设置错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df459c0a3baa6f08544f51a865b1f30db2c358990bff27f4ed91db8789615b9d
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 100201 attributeModifier不支持部分接口的使用

**错误信息**

Something not supported in attributeModifier scenario.

**错误描述**

部分接口不支持通过[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)设置，具体请参考[属性或事件对attributeModifier的支持情况](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#属性或事件对attributemodifier的支持情况)。

**可能原因**

部分接口不支持通过attributeModifier设置。

**处理步骤**

根据错误码对应的具体信息，停止使用该部分接口，请参考[用attributemodifier设置组件动态属性出现jscrash](../harmonyos-guides/arkts-attribute-modifier-faq.md#使用attributemodifier设置组件动态属性出现jscrash)。
