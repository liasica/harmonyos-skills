---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-card-context
title: LiveViewCardExtensionContext
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewCardExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T14:53:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3ba0a003c5628fd75a32c04b9544a0903889c63a2b604eaea6f9d4d266ccd3c2
---

LiveViewCardExtensionContext是[LiveViewCardExtensionAbility](liveview-card-ability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，该类在API定义中未显式定义具体的属性和方法，其功能主要通过继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)的通用上下文能力实现。主要用于查询所属 [LiveViewCardExtensionAbility](liveview-card-ability.md)的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { LiveViewCardExtensionContext } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## LiveViewCardExtensionContext

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 26.0.0
