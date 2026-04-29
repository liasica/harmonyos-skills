---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-forminfo
title: @ohos.app.form.formInfo (formInfo)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.formInfo (formInfo)
category: harmonyos-references
scraped_at: 2026-04-29T13:56:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ef9576d5063cb2b958ce82e44cac0830c959a2f714d078a3a9bbfbb90db9138f
---

formInfo模块提供了卡片信息和状态等相关类型和枚举。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formInfo } from '@kit.FormKit';
```

## FormInfo

PhonePC/2in1TabletTVWearable

卡片配置信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 卡片所属包的Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 否 | 否 | 卡片所属模块的模块名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| abilityName | string | 否 | 否 | 卡片所属的Ability名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 卡片名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayName11+ | string | 否 | 否 | 卡片展示名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayNameId11+ | number | 否 | 否 | 卡片预览时标识卡片名称的ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| description | string | 否 | 否 | 卡片描述。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId10+ | number | 否 | 否 | 卡片描述id。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| type | [FormType](js-apis-app-form-forminfo.md#formtype) | 否 | 否 | 卡片类型。当前支持JS卡片、ArkTS卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| jsComponentName | string | 否 | 否 | js卡片的组件名。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| colorMode(deprecated) | [ColorMode](js-apis-app-form-forminfo.md#colormodedeprecated) | 否 | 否 | 卡片颜色模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  从API version 9开始支持，从API version 20开始废弃。应用卡片需要支持深浅色两种显示模式，无替代接口。 |
| isDefault | boolean | 否 | 否 | 卡片是否是默认卡片。  - true：默认卡片。  - false：非默认卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| updateEnabled | boolean | 否 | 否 | 卡片是否使能更新。  - true：表示支持周期性刷新。  - false：表示不支持周期性刷新。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| formVisibleNotify | boolean | 否 | 否 | 卡片是否使能可见通知。  - true：通知卡片提供方可见状态变化。  - false：不通知卡片提供方可见状态变化。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| scheduledUpdateTime | string | 否 | 否 | 卡片更新时间。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| formConfigAbility | string | 否 | 否 | 卡片配置ability。指定长按卡片弹出的选择框内，编辑选项所对应的ability。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| updateDuration | number | 否 | 否 | 卡片更新周期。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| defaultDimension | number | 否 | 否 | 卡片规格  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| supportDimensions | Array<number> | 否 | 否 | 卡片支持的规格。具体可选规格参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| customizeData | Record<string, string> | 否 | 否 | 卡片用户数据。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isDynamic10+ | boolean | 否 | 否 | 卡片是否为动态卡片。  仅ArkTS卡片区分动静态卡片，JS卡片均为动态卡片。  - true：为动态卡片。  - false：为静态卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| transparencyEnabled11+ | boolean | 否 | 否 | 卡片是否支持设置背景透明度。  ArkTS卡片由用户配置决定是否支持，JS卡片均不支持。  - true：表示是透明卡片。  - false：表示不是透明卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| supportedShapes12+ | Array<number> | 否 | 否 | 卡片支持的形状。具体可选形状参考[FormShape12+](js-apis-app-form-forminfo.md#formshape12)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## FormType

PhonePC/2in1TabletTVWearable

支持的卡片类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JS | 1 | 卡片类型为JS。 |
| eTS | 2 | 卡片类型为ArkTS。 |

## ColorMode(deprecated)

PhonePC/2in1TabletTVWearable

卡片主题样式统一跟随系统的颜色模式，卡片支持的颜色模式枚举。

说明

从API version 9开始支持，从API version 20开始废弃。应用卡片需要支持深浅色两种显示模式，无替代接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_AUTO | -1 | 表示自动模式。 |
| MODE\_DARK | 0 | 表示暗色。 |
| MODE\_LIGHT | 1 | 表示亮色。 |

## FormStateInfo

PhonePC/2in1TabletTVWearable

卡片状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formState | [FormState](js-apis-app-form-forminfo.md#formstate) | 否 | 否 | 卡片状态。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | Want文本内容。 |

## FormState

PhonePC/2in1TabletTVWearable

卡片状态枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

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
| IDENTITY\_KEY | 'ohos.extra.param.key.form\_identity' | 卡片标识。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DIMENSION\_KEY | 'ohos.extra.param.key.form\_dimension' | 卡片规格，规格尺寸参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NAME\_KEY | 'ohos.extra.param.key.form\_name' | 卡片名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MODULE\_NAME\_KEY | 'ohos.extra.param.key.module\_name' | 卡片所属模块名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| WIDTH\_KEY | 'ohos.extra.param.key.form\_width' | 卡片宽度。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| HEIGHT\_KEY | 'ohos.extra.param.key.form\_height' | 卡片高度。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TEMPORARY\_KEY | 'ohos.extra.param.key.form\_temporary' | 临时卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ABILITY\_NAME\_KEY | 'ohos.extra.param.key.ability\_name' | ability名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BUNDLE\_NAME\_KEY | 'ohos.extra.param.key.bundle\_name' | Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LAUNCH\_REASON\_KEY10+ | 'ohos.extra.param.key.form\_launch\_reason' | 卡片创建原因。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PARAM\_FORM\_CUSTOMIZE\_KEY10+ | 'ohos.extra.param.key.form\_customize' | 自定义数据。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FORM\_RENDERING\_MODE\_KEY11+ | 'ohos.extra.param.key.form\_rendering\_mode' | 卡片渲染模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| HOST\_BG\_INVERSE\_COLOR\_KEY12+ | 'ohos.extra.param.key.host\_bg\_inverse\_color' | 卡片使用方的背景反色颜色值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FORM\_LOCATION\_KEY12+ | 'ohos.extra.param.key.form\_location' | 卡片位置。  OTHER -1 （其他位置）  DESKTOP 0 （桌面）  FORM\_CENTER 1 （桌面的卡片中心）  FORM\_MANAGER 2 （桌面的卡片管理器）  NEGATIVE\_SCREEN 3 （负一屏）  FORM\_CENTER\_NEGATIVE\_SCREEN 4 （负一屏的服务中心）  FORM\_MANAGER\_NEGATIVE\_SCREEN 5 （负一屏的卡片管理器）  SCREEN\_LOCK 6 （锁屏）  AI\_SUGGESTION 7 （AI智慧助手推荐区）  STANDBY 8 （待机屏保显示界面） |
| FORM\_PERMISSION\_NAME\_KEY12+ | 'ohos.extra.param.key.permission\_name' | 用户授权权限名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FORM\_PERMISSION\_GRANTED\_KEY12+ | 'ohos.extra.param.key.permission\_granted' | 用户是否授权。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ORIGINAL\_FORM\_KEY20+ | 'ohos.extra.param.key.original\_form\_id' | 用groupId关联的一组卡片，在调整大小时，会先创建新尺寸的卡片，再删除旧尺寸的卡片。新尺寸卡片创建时want参数会通过该key传递旧尺寸卡片的卡片id。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| EDIT\_FORM\_KEY22+ | 'ohos.extra.param.key.edit\_form\_id' | 在半模态页面的卡片编辑中，通过onAddForm回调函数传递该key表示被编辑的卡片id，用来确保预览卡片与被编辑卡片信息同步。如果卡片onAddForm回调函数中携带了该key，则说明当前卡片为半模态页面中的预览卡片，需要基于被编辑卡片来筛选预览卡片内容。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## FormDimension

PhonePC/2in1TabletTVWearable

定义卡片尺寸枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Dimension\_1\_2 | 1 | 1 x 2 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension\_2\_2 | 2 | 2 x 2 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension\_2\_4 | 3 | 2 x 4 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension\_4\_4 | 4 | 4 x 4 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Dimension\_2\_1(deprecated) | 5 | 2 x 1 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 该字段从API version 9开始支持，从API version 20开始废弃。 |
| DIMENSION\_1\_111+ | 6 | 1 x 1 form。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 该尺寸仅在锁屏卡片上生效。 |
| DIMENSION\_6\_412+ | 7 | 6 x 4 form。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DIMENSION\_2\_318+ | 8 | 2 x 3 form。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。  **设备行为差异：** 该字段仅在Wearable上生效，在其他设备类型中无效果。 |
| DIMENSION\_3\_318+ | 9 | 3 x 3 form。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。  **设备行为差异：** 该字段仅在Wearable上生效，在其他设备类型中无效果。 |

## FormShape12+

PhonePC/2in1TabletTVWearable

定义卡片形状枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECT | 1 | 方形 form。 |
| CIRCLE | 2 | 圆形 form。 |

## FormInfoFilter

PhonePC/2in1TabletTVWearable

卡片信息过滤器，仅将符合过滤器内要求的卡片信息返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 是 | 选填，仅保留含moduleName与提供值相符的卡片信息，  未填写时则不通过moduleName进行过滤。 |

## VisibilityType

PhonePC/2in1TabletTVWearable

卡片当前可见类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN10+ | 0 | 表示卡片为未知。 |
| FORM\_VISIBLE | 1 | 表示卡片为可见。 |
| FORM\_INVISIBLE | 2 | 表示卡片为不可见。 |

## LaunchReason10+

PhonePC/2in1TabletTVWearable

卡片创建原因枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORM\_DEFAULT | 1 | 表示卡片创建原因为默认创建。 |
| FORM\_SHARE | 2 | 表示卡片创建原因为共享创建。 |
| FORM\_SIZE\_CHANGE20+ | 3 | 表示卡片创建原因为尺寸变化。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## OverflowInfo20+

PhonePC/2in1TabletTVWearable

互动卡片动效信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| area | [Rect](js-apis-app-form-forminfo.md#rect20) | 否 | 否 | 描述互动卡片动效区域范围，以卡片左上角为原点，单位为vp。 |
| duration | number | 否 | 否 | 互动卡片动效持续时长，单位ms。取值为大于0的整数，取值要求不大于3500。 |
| useDefaultAnimation | boolean | 否 | 是 | 互动卡片状态切换时是否启动系统提供的默认动效，默认为true。  - true：表示系统提供默认切换动效。  - false：表示系统不提供切换动效，画面直接切换，适合切换时非激活态和激活态UI完全一致的场景。 |

## Rect20+

PhonePC/2in1TabletTVWearable

通用矩形区域信息。可用于描述卡片位置、互动卡片动效区域等信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 描述矩形的左上角顶点的 x 坐标，单位：vp。 |
| top | number | 否 | 否 | 描述矩形的左上角顶点的 y 坐标，单位：vp。 |
| width | number | 否 | 否 | 描述矩形的宽度，单位：vp。 |
| height | number | 否 | 否 | 描述矩形的高度，单位：vp。 |

## FormLocation20+

PhonePC/2in1TabletTVWearable

卡片当前位置枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DESKTOP | 0 | 表示卡片位于桌面。 |
| FORM\_CENTER | 1 | 表示卡片位于桌面的卡片中心。 |
| FORM\_MANAGER | 2 | 表示卡片位于桌面的卡片管理器。 |
| NEGATIVE\_SCREEN | 3 | 表示卡片位于负一屏。 |
| SCREEN\_LOCK | 6 | 表示卡片位于锁屏页面。 |
| AI\_SUGGESTION | 7 | 表示卡片位于小艺建议的推荐区。 |
| STANDBY | 8 | 表示卡片位于待机屏保显示页面。 |

## RunningFormInfo20+

PhonePC/2in1TabletTVWearable

已经添加到桌面的卡片信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 是 | 否 | 卡片标识。 |
| bundleName | string | 是 | 否 | 卡片提供方所属包的Bundle名称。 |
| moduleName | string | 是 | 否 | 卡片所属模块的名称。 |
| abilityName | string | 是 | 否 | 卡片所属的Ability名称。 |
| formName | string | 是 | 否 | 卡片名称。 |
| dimension | number | 是 | 否 | 卡片尺寸，取值及其对应含义请参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)。 |
| formLocation | [FormLocation](js-apis-app-form-forminfo.md#formlocation20) | 是 | 否 | 卡片位置信息。 |
