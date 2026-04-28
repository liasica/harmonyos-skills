---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-appversioninfo
title: AppVersionInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > app > AppVersionInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:58:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:94d0b1a22f5051f03f663338cdf0ba20cb472251197af1f5abc6483c3f8b0c91
---

应用版本信息，可以通过[getAppVersionInfo](js-apis-inner-app-context.md#contextgetappversioninfo7)获取当前应用的版本信息。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import featureAbility from '@ohos.ability.featureAbility';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appName | string | 是 | 否 | 应用名称。 |
| versionCode | number | 是 | 否 | 应用版本编码。 |
| versionName | string | 是 | 否 | 应用版本名称。 |
