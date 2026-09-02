---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-remote-notification-extension-context
title: RemoteNotificationExtensionContext（通知扩展Context）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > RemoteNotificationExtensionContext（通知扩展Context）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e2722d6575dfce5753ba48bb4ff127c62c3bf658694c6798b492bd086f9aef0c
---

RemoteNotificationExtensionContext是[RemoteNotificationExtensionAbility](push-remote-notification-extension-ability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，未新增内容。RemoteNotificationExtensionContext模块提供访问RemoteNotificationExtensionAbility资源的能力。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { RemoteNotificationExtensionContext } from '@kit.PushKit';
```

## RemoteNotificationExtensionContext

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)~6.0.2(22)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.1.0(11)
