---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname
title: ElementName
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > ElementName
category: harmonyos-references
scraped_at: 2026-04-28T07:58:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb1de07921380d511b731ba40e00fef92db0556b2e040059d3c8598d8b4a1b08
---

应用组件结构体，包含bundleName、moduleName和abilityName等。通常用于组件启动信息[AbilityRunningInfo.ability](js-apis-inner-application-abilityrunninginfo.md)和组件启动回调函数[connectOptions.onConnect](js-apis-inner-ability-connectoptions.md#onconnect)中。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## ElementName

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 设备ID。 |
| bundleName | string | 否 | 否 | 应用Bundle名称。 |
| abilityName | string | 否 | 否 | Ability名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability短名称，以“.”为开头的字符串。 |
| moduleName | string | 否 | 是 | Ability所属的HAP的模块名称。 |
