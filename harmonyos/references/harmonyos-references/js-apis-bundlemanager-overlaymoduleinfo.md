---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-overlaymoduleinfo
title: OverlayModuleInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > OverlayModuleInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:71d6bc4987eebbbf07161bd6f1264674d82a43435a5fa9e4e58e058cd2195d96
---

OverlayModuleInfo信息，可以通过[overlay.getOverlayModuleInfo](js-apis-overlay.md#overlaygetoverlaymoduleinfo)接口获取当前应用中具有overlay特征模块的OverlayModuleInfo信息。

说明

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { overlay } from '@kit.AbilityKit';
```

## OverlayModuleInfo

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | overlay特征module所属的应用的bundle名称。 |
| moduleName | string | 是 | 否 | overlay特征module的名称。 |
| targetModuleName | string | 是 | 否 | overlay特征指定的目标module的名称，表示当前overlay包的资源需要替换生效的模块名称。 |
| priority | number | 是 | 否 | overlay特征module的优先级。取值为整数，取值范围1 ~ 100，数值越大优先级越高。 |
| state | number | 是 | 否 | overlay特征module的[禁用使能状态](js-apis-overlay.md#overlaysetoverlayenabled)。0代表禁用状态，1代表使能状态。 |
