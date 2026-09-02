---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensioncontext
title: "@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext（屏幕时间守护扩展Context）"
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > @hms.utilityApplication.screenTimeGuard.TimeGuardExtensionContext（屏幕时间守护扩展Context）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3ea7f47ecd8549ee7fedf33561e65463c430c4c319d52754e06c1ea4ee0328f4
---

## 模块概述

屏幕时间守护ExtensionContext模块提供了获取[TimeGuardExtensionAbility](screentimeguard-timeguardextensionability.md)上下文的能力。TimeGuardExtensionContext继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，是TimeGuardExtensionAbility的上下文环境，开发者可用于查询所属TimeGuardExtensionAbility的信息、Module的配置信息以及HAP包的信息，并根据自身业务需求使用对应的信息。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { TimeGuardExtensionContext } from '@kit.ScreenTimeGuardKit';
```

## TimeGuardExtensionContext

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

本类继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。相较于ExtensionContext，TimeGuardExtensionContex未新增功能，只是命名区分。
