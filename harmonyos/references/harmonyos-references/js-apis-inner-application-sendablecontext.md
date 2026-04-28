---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext
title: SendableContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > SendableContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0368520cb376f3c4d2e9c65eaac5ec31b14aec9248b6afa567fbdf0da427a3df
---

SendableContext符合[Sendable协议](../harmonyos-guides/arkts-sendable.md#sendable协议)，继承自[lang.ISendable](js-apis-arkts-lang.md#langisendable)。

说明

* 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableContextManager } from '@kit.AbilityKit';
```

## SendableContext

PhonePC/2in1TabletTVWearable

SendableContext符合[Sendable协议](../harmonyos-guides/arkts-sendable.md#sendable协议)，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。
