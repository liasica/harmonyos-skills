---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-extension-context
title: PushExtensionContext（推送扩展Context）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > PushExtensionContext（推送扩展Context）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:161342dadaf38ecb8b380cecc482e8ddf4e602baac7d8376f89cb171041d6827
---

PushExtensionContext是[PushExtensionAbility](push-extension-ability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { PushExtensionContext } from '@kit.PushKit';
```

## PushExtensionContext

PhonePC/2in1TabletTVWearable

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

本类继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，未新增内容。
