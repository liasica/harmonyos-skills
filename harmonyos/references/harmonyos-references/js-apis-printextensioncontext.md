---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-printextensioncontext
title: PrintExtensionContext
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > PrintExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T15:02:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a82a808d5dbd13c399b344d8c3395f160afb39d75555d03dd5a07bb684ec33db
---

PrintExtensionContext是PrintExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

PrintExtensionContext可直接作为PrintExtensionAbility的上下文环境，用于在打印扩展开发场景中获取和管理打印相关资源，以完成打印任务相关操作。关于PrintExtensionContext的设计逻辑与可访问资源，请参见[PrintExtensionAbility](js-apis-app-ability-printextensionability.md)与[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**说明** 

* 本模块接口仅可在Stage模型下使用。
* **起始版本：** 26.0.0

## 导入模块

```ts
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
```

## 使用说明

通过PrintExtensionAbility子类实例获取PrintExtensionContext。

```ts
import { PrintExtensionAbility } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

export default class PrintExtension extends PrintExtensionAbility {

  onCreate(want: Want) {
    let context = this.context; // 获取PrintExtensionContext，后续可通过context访问打印相关资源
  }
}
```
