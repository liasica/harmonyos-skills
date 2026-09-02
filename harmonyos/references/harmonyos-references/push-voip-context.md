---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-voip-context
title: VoIPExtensionContext（应用内通话消息扩展Context）（废弃）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > VoIPExtensionContext（应用内通话消息扩展Context）（废弃）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4c9f6c098f7995fc5ead8ce9ec4927f77125342d63bcce060012fea9fe6ea484
---

VoIPExtensionContext是VoIPExtensionAbility的上下文环境，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

**废弃版本：** 26.0.0

## 导入模块

```typescript
import { VoIPExtensionContext } from '@kit.PushKit';
```

## VoIPExtensionContext(deprecated)

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该属性在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**废弃版本：** 26.0.0

本类继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)，未新增内容。
