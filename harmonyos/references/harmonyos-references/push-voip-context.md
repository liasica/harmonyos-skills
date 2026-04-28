---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-context
title: VoIPExtensionContext（应用内通话消息扩展Context）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > VoIPExtensionContext（应用内通话消息扩展Context）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f610d8db9138a982021805986f81045a0e2a8a952a73b33e6f72d502a33570e
---

VoIPExtensionContext是VoIPExtensionAbility的上下文环境，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { VoIPExtensionContext } from '@kit.PushKit';
```

## VoIPExtensionContext

PhonePC/2in1TabletTVWearable

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该属性在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

本类继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)，未新增内容。
