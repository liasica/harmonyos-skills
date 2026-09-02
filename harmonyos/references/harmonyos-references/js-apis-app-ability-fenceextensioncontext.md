---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensioncontext
title: "@ohos.app.ability.FenceExtensionContext (FenceExtensionContext)"
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > @ohos.app.ability.FenceExtensionContext (FenceExtensionContext)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:61b38bd48473f1517e4001b3a36b0325f62ba26036fb463d0e3831ba90c9dcd3
---

FenceExtensionContext是FenceExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，提供FenceExtensionAbility的相关配置信息以及启动Ability接口。

**说明** 

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { FenceExtensionContext } from '@kit.LocationKit';
```

## 使用说明

在使用FenceExtensionContext的功能前，需要通过FenceExtensionAbility获取。

```ts
import { FenceExtensionAbility, FenceExtensionContext } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onCreate() {
    let fenceExtensionContext: FenceExtensionContext = this.context;
  }
}
```
