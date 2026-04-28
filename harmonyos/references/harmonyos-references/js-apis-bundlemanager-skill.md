---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-skill
title: Skill
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > bundleManager > Skill
category: harmonyos-references
scraped_at: 2026-04-28T07:58:47+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2915d6738b694222e1baf4f1edab1ed56881877c705baa74a3c465d2a708c5f7
---

skill标签对象，可以通过[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取skill([BundleInfo](js-apis-bundlemanager-bundleinfo.md)->[HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md)->[AbilityInfo](js-apis-bundlemanager-abilityinfo.md)或[ExtensionAbilityInfo](js-apis-bundlemanager-extensionabilityinfo.md)中)信息，其中参数bundleFlags至少包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ABILITY和GET\_BUNDLE\_INFO\_WITH\_SKILL。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bundleManager } from '@kit.AbilityKit';
```

## Skill

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actions | Array<string> | 是 | 否 | Skill接收的[Action集合](js-apis-ability-wantconstant.md#action)。 |
| entities | Array<string> | 是 | 否 | Skill接收的[Entity集合](js-apis-ability-wantconstant.md#entity)。 |
| uris | Array<SkillUri> | 是 | 否 | Want匹配的Uri集合。 |
| domainVerify | boolean | 是 | 否 | Skill接收的DomainVerify值，仅在AbilityInfo中存在，表示是否开启域名校验，取值为true表示开启域名校验，取值为false表示未开启域名校验。 |

## SkillUri

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scheme | string | 是 | 否 | 标识 URI 协议名，常见的有http、https、file、ftp等。 |
| host | string | 是 | 否 | 标识 URI 主机地址部分，仅当 scheme 存在时才生效。 |
| port | number | 是 | 否 | 标识 URI 端口，仅当 scheme 和 host 同时存在时才生效。 |
| path | string | 是 | 否 | 标识 URI 路径部分，仅当 scheme 和 host 同时存在时才生效。 |
| pathStartWith | string | 是 | 否 | 标识 URI 路径部分，用于前缀匹配，仅当 scheme 和 host 同时存在时才生效。 |
| pathRegex | string | 是 | 否 | 标识 URI 路径部分，用于正则匹配，仅当 scheme 和 host 同时存在时才生效。 |
| type | string | 是 | 否 | 标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范和[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型规范。 |
| utd | string | 是 | 否 | 标识与 Want 相匹配的 URI 的标准化数据类型，适用于分享等场景。 |
| maxFileSupported | number | 是 | 否 | 对于指定类型的文件，标识一次能接收或打开的最大数量。取值范围：不小于0的整数。 |
| linkFeature | string | 是 | 否 | 标识 URI 提供的[功能类型](../harmonyos-guides/app-uri-config.md#linkfeature标签说明)，用于实现应用间跳转，仅在AbilityInfo中存在。 |
