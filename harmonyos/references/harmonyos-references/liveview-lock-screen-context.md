---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-context
title: LiveViewLockScreenExtensionContext
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewLockScreenExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T14:53:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0d669ee1bd07862f844fb15ac9779444698f7edfb3f18b287e3c48053a32253a
---

LiveViewLockScreenExtensionContext是[LiveViewLockScreenExtensionAbility](liveview-lock-screen-ability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，该类在API定义中未显式定义具体的属性和方法，其功能主要通过继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)的通用上下文能力实现。为开发者提供在锁屏场景下访问锁屏沉浸态实况窗的上下文能力。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { LiveViewLockScreenExtensionContext } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## LiveViewLockScreenExtensionContext

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)
