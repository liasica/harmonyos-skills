---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext
title: DriverExtensionContext
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > application > DriverExtensionContext
category: harmonyos-references
scraped_at: 2026-04-28T08:10:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e745d645689a546732aba44b5e3901bc2c5a5bb08023034034240c0e114128fc
---

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。

DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PC/2in1

```
1. import { common } from '@kit.AbilityKit';
```

## 使用说明

PC/2in1

在使用DriverExtensionContext的功能前，需要通过DriverExtensionAbility子类实例获取。

```
1. import { DriverExtensionAbility, DriverExtensionContext } from '@kit.DriverDevelopmentKit';

3. let context : DriverExtensionContext | undefined;
4. class EntryAbility extends DriverExtensionAbility {
5. onInit() {
6. context = this.context; // 获取DriverExtensionContext
7. }
8. }
```

## DriverExtensionContext.updateDriverState

PC/2in1

updateDriverState(): void

驱动状态上报。预留接口，暂不提供具体功能。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```
1. // 当前代码实现依赖上一节代码实现
2. if (context != null) {
3. context.updateDriverState();
4. }
```
