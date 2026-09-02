---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext
title: DriverExtensionContext
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > application > DriverExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa75cfa0ed31b3462378a960dcedb765c9a9b5eea958d2b62f25575fcb97eef9
---

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。

DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { DriverExtensionAbility, DriverExtensionContext } from '@kit.DriverDevelopmentKit';
```

## 使用说明

在使用DriverExtensionContext的功能前，需要通过DriverExtensionAbility子类实例获取。

```ts
  let context: DriverExtensionContext | undefined;
  class EntryAbility extends DriverExtensionAbility {
    onInit() {
      context = this.context; // 获取DriverExtensionContext
    }
  }
```

## DriverExtensionContext.updateDriverState

updateDriverState(): void

驱动状态上报。预留接口，暂不提供具体功能。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```ts
// 当前代码实现依赖上一节代码实现
if (context !== undefined) {
  context.updateDriverState();
}
```
