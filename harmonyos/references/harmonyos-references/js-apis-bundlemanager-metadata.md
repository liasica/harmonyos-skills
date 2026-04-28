---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata
title: Metadata
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > Metadata
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad5bdd97e74afc7ca3940a9713f7c27ab9b468080736b740c52b63783004975a
---

元数据对象，可以通过[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取，其中参数bundleFlags至少包含GET\_BUNDLE\_INFO\_WITH\_METADATA。此对象在[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md)、[HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)、[AbilityInfo](js-apis-bundlemanager-abilityinfo.md)、[ExtensionAbilityInfo](js-apis-bundlemanager-extensionabilityinfo.md)中均包含。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

描述的module、uiAbility、extensionAbility配置信息，标签值为数组类型，该标签下的配置只对当前module、uiAbility或者extensionAbility生效。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## Metadata

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 元数据名称。 |
| value | string | 否 | 否 | 元数据值。 |
| resource | string | 否 | 否 | 元数据资源描述符，参考示例$profile:config\_file，表示profile目录下配置了config\_file.json文件。 |
| valueId18+ | number | 是 | 是 | 元数据值id。当valueId不为0时，表示当前元数据值为自定义配置，需要使用valueId去资源管理获取对应的值。 当valueId为0时，表示当前元数据值为固定字符串。 |
