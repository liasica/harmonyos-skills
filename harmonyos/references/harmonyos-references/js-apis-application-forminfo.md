---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-forminfo
title: @ohos.application.formInfo (formInfo)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > 已停止维护的接口 > @ohos.application.formInfo (formInfo)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b05b1ee9ccb589bfe98d647779f5f7f44666250604da8e2e9b97d4b4f2dc379d
---

formInfo模块提供了卡片信息和状态等相关类型和枚举。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始废弃，建议使用[formInfo](js-apis-app-form-forminfo.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formInfo } from '@kit.FormKit';
```

## FormInfo

PhonePC/2in1TabletTVWearable

卡片信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 表示卡片所属包的Bundle名称。 |
| moduleName | string | 否 | 否 | 表示卡片所属模块的模块名。 |
| abilityName | string | 否 | 否 | 表示卡片所属的Ability名称。 |
| name | string | 否 | 否 | 表示卡片名称。 |
| description | string | 否 | 否 | 表示卡片描述。 |
| type | [FormType](js-apis-application-forminfo.md#formtype) | 否 | 否 | 表示卡片类型，当前支持JS卡片。 |
| jsComponentName | string | 否 | 否 | 表示JS卡片的组件名。 |
| colorMode | [ColorMode](js-apis-application-forminfo.md#colormode) | 否 | 否 | 表示卡片颜色模式。 |
| isDefault | boolean | 否 | 否 | 表示是否是默认卡片。  - true：默认卡片。  - false：非默认卡片。 |
| updateEnabled | boolean | 否 | 否 | 表示卡片是否使能更新。  - true：表示支持周期性刷新。  - false：表示不支持周期性刷新。 |
| formVisibleNotify | boolean | 否 | 否 | 表示卡片是否使能可见通知。  - true：通知卡片提供方可见状态变化。  - false：不通知卡片提供方可见状态变化。 |
| relatedBundleName | string | 否 | 否 | 表示卡片所属的相关联Bundle名称。 |
| scheduledUpdateTime | string | 否 | 否 | 表示卡片更新时间。 |
| formConfigAbility | string | 否 | 否 | 表示卡片配置ability。 |
| updateDuration | number | 否 | 否 | 表示卡片更新周期。 |
| defaultDimension | number | 否 | 否 | 表示卡片规格。 |
| supportDimensions | Array<number> | 否 | 否 | 表示卡片支持的规格。 |
| customizeData | {[key: string]: [value: string]} | 否 | 否 | 表示卡片用户数据。 |

## FormType

PhonePC/2in1TabletTVWearable

支持的卡片类型枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JS | 1 | 卡片类型为JS。 |

## ColorMode

PhonePC/2in1TabletTVWearable

卡片支持的颜色模式枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_AUTO | -1 | 表示自动模式。 |
| MODE\_DARK | 0 | 表示暗色。 |
| MODE\_LIGHT | 1 | 表示亮色。 |

## FormStateInfo

PhonePC/2in1TabletTVWearable

卡片状态信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formState | [FormState](js-apis-application-forminfo.md#formstate) | 否 | 否 | 表示卡片状态。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | Want文本内容。 |

## FormState

PhonePC/2in1TabletTVWearable

卡片状态枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 表示未知状态。 |
| DEFAULT | 0 | 表示默认状态。 |
| READY | 1 | 表示就绪状态。 |

## FormParam

PhonePC/2in1TabletTVWearable

卡片参数枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DIMENSION\_KEY | 'ohos.extra.param.key.form\_dimension' | 卡片规格样式。 |
| NAME\_KEY | 'ohos.extra.param.key.form\_name' | 卡片名称。 |
| MODULE\_NAME\_KEY | 'ohos.extra.param.key.module\_name' | 卡片所属模块名称。 |
| WIDTH\_KEY | 'ohos.extra.param.key.form\_width' | 卡片宽度。 |
| HEIGHT\_KEY | 'ohos.extra.param.key.form\_height' | 卡片高度。 |
| TEMPORARY\_KEY | 'ohos.extra.param.key.form\_temporary' | 临时卡片。 |
