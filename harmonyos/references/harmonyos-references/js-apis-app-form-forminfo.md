---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-forminfo
title: "@ohos.app.form.formInfo (formInfo)"
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.formInfo (formInfo)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b174629bd9564f5b4818743c2faebc8791c5b1ce635c9a072a1f2b3d8dd71072
---

formInfo模块提供了卡片信息和状态等相关类型和枚举，用于获取卡片配置信息、状态信息、参数枚举等，适用于需要查询卡片属性、管理卡片状态、处理卡片参数的场景，帮助开发者快速访问和操作卡片相关信息。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { formInfo } from '@kit.FormKit';
```

## FormInfo

卡片配置信息。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 卡片所属包的Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| moduleName | string | 否 | 否 | 卡片所属模块的模块名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| abilityName | string | 否 | 否 | 卡片所属的Ability名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 卡片名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayName11+ | string | 否 | 否 | 卡片展示名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayNameId11+ | number | 否 | 否 | 卡片预览时标识卡片名称的ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 数值为大于0小于2^32的整数。 |
| description | string | 否 | 否 | 卡片描述。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| descriptionId10+ | number | 否 | 否 | 卡片描述ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 数值为大于0小于2^32的整数。 |
| type | [FormType](js-apis-app-form-forminfo.md#formtype) | 否 | 否 | 卡片类型。当前支持JS卡片、ArkTS卡片。  **说明：** 当卡片类型为JS时，isDynamic强制为true，transparencyEnabled不生效，jsComponentName为必填项。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| jsComponentName | string | 否 | 否 | JS卡片的组件名，仅当卡片类型为JS时有效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| colorMode(deprecated) | [ColorMode](js-apis-app-form-forminfo.md#colormodedeprecated) | 否 | 否 | 卡片颜色模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  从API version 9开始支持，从API version 20开始废弃。无替代接口。 |
| isDefault | boolean | 否 | 否 | 卡片是否是默认卡片。  - true：默认卡片。  - false：非默认卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| updateEnabled | boolean | 否 | 否 | 卡片是否使能更新。  - true：表示支持周期性刷新。  - false：表示不支持周期性刷新。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| formVisibleNotify | boolean | 否 | 否 | 卡片是否使能可见通知。  - true：通知卡片提供方可见状态变化。  - false：不通知卡片提供方可见状态变化。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| scheduledUpdateTime | string | 否 | 否 | 卡片更新时间。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| formConfigAbility | string | 否 | 否 | 卡片配置Ability。指定长按卡片弹出的选择框内，编辑选项所对应的Ability。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| updateDuration | number | 否 | 否 | 卡片更新周期。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 数值为[0, 336]的整数。超出范围时抛出异常。 |
| defaultDimension | number | 否 | 否 | 卡片规格。具体可选规格参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 数值为[1, 9]的整数，数值5从API version 9开始支持，从API version 20开始废弃。超出范围时抛出异常。 |
| supportDimensions | Array<number> | 否 | 否 | 卡片支持的规格。具体可选规格参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：** 最大长度为9，数值取值范围[1, 9]的整数的数组，数值5从API version 9开始支持，从API version 20开始废弃。超出范围时抛出异常。 |
| customizeData | Record<string, string> | 否 | 否 | 卡片用户数据。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isDynamic10+ | boolean | 否 | 否 | 卡片是否为动态卡片。  仅ArkTS卡片区分动静态卡片，JS卡片均为动态卡片。  - true：为动态卡片。  - false：为静态卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| transparencyEnabled11+ | boolean | 否 | 否 | 卡片是否支持设置背景透明度。  ArkTS卡片由用户配置决定是否支持，JS卡片均不支持。  - true：表示是透明卡片。  - false：表示不是透明卡片。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| supportedShapes12+ | Array<number> | 否 | 否 | 卡片支持的形状。具体可选形状参考[FormShape12+](js-apis-app-form-forminfo.md#formshape12)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **说明：** 1代表方形，2代表圆形。 |

## FormType

支持的卡片类型枚举。JS卡片使用Web技术实现，适合简单的展示类卡片；ArkTS卡片使用ArkTS语言开发，支持更丰富的交互和动画效果。开发时应根据卡片复杂度和交互需求选择合适类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JS | 1 | 卡片类型为JS。使用Web技术开发，功能相对基础，适合简单场景。 |
| eTS | 2 | 卡片类型为ArkTS。使用ArkTS语言开发，支持丰富的交互和动画，适合复杂场景。 |

## ColorMode(deprecated)

卡片主题样式统一跟随系统的颜色模式，卡片支持的颜色模式枚举。

**说明** 

从API version 9开始支持，从API version 20开始废弃。无替代接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_AUTO | -1 | 表示自动模式。 |
| MODE\_DARK | 0 | 表示暗色。 |
| MODE\_LIGHT | 1 | 表示亮色。 |

## FormStateInfo

卡片状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formState | [FormState](js-apis-app-form-forminfo.md#formstate) | 否 | 否 | 卡片状态，用于标识卡片当前状态（如未知、默认、就绪）。 |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | Want对象，用于承载卡片状态切换时的意图信息。 |

## FormState

卡片状态枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 表示未知状态。 |
| DEFAULT | 0 | 表示默认状态。 |
| READY | 1 | 表示就绪状态。 |

## FormParam

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
| ABILITY\_NAME\_KEY | 'ohos.extra.param.key.ability\_name' | Ability名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BUNDLE\_NAME\_KEY | 'ohos.extra.param.key.bundle\_name' | Bundle名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LAUNCH\_REASON\_KEY10+ | 'ohos.extra.param.key.form\_launch\_reason' | 卡片创建原因。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PARAM\_FORM\_CUSTOMIZE\_KEY10+ | 'ohos.extra.param.key.form\_customize' | 自定义数据。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FORM\_RENDERING\_MODE\_KEY11+ | 'ohos.extra.param.key.form\_rendering\_mode' | 卡片渲染模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| HOST\_BG\_INVERSE\_COLOR\_KEY12+ | 'ohos.extra.param.key.host\_bg\_inverse\_color' | 卡片使用方的背景反色颜色值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FORM\_LOCATION\_KEY12+ | 'ohos.extra.param.key.form\_location' | 卡片位置。 具体可选位置参考[FormLocation](js-apis-app-form-forminfo.md#formlocation20)。 |
| FORM\_PERMISSION\_NAME\_KEY12+ | 'ohos.extra.param.key.permission\_name' | 用户授权权限名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FORM\_PERMISSION\_GRANTED\_KEY12+ | 'ohos.extra.param.key.permission\_granted' | 用户是否授权。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ORIGINAL\_FORM\_KEY20+ | 'ohos.extra.param.key.original\_form\_id' | 用groupId关联的一组卡片，在调整大小时，会先创建新尺寸的卡片，再删除旧尺寸的卡片。新尺寸卡片创建时want参数会通过该key传递旧尺寸卡片的卡片id。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| EDIT\_FORM\_KEY22+ | 'ohos.extra.param.key.edit\_form\_id' | 在半模态页面的卡片编辑中，通过onAddForm回调函数传递该key表示被编辑的卡片id，用来确保预览卡片与被编辑卡片信息同步。如果卡片onAddForm回调函数中携带了该key，则说明当前卡片为半模态页面中的预览卡片，需要基于被编辑卡片来筛选预览卡片内容。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| UPDATE\_FORM\_REASON\_KEY24+ | 'ohos.extra.param.key.update\_form\_reason' | 卡片更新的原因，请参考[FormUpdateReason](js-apis-app-form-forminfo.md#formupdatereason24)。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## FormDimension

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

定义卡片形状枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RECT | 1 | 矩形 form。 |
| CIRCLE | 2 | 圆形 form。 |

## FormInfoFilter

卡片信息过滤器，仅将符合过滤器内要求的卡片信息返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 是 | 卡片所属模块的名称，用于过滤卡片信息。仅保留含moduleName与提供值相符的卡片信息，未填写时则不通过moduleName进行过滤。 |

## VisibilityType

卡片当前可见类型枚举。表示卡片在宿主界面上的可见状态，当卡片从桌面移入/移出屏幕或切换应用时状态会发生变化，开发者可据此优化卡片刷新策略。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN10+ | 0 | 表示卡片为未知。 |
| FORM\_VISIBLE | 1 | 表示卡片为可见。卡片在前台显示，会正常接收更新和可见性通知。 |
| FORM\_INVISIBLE | 2 | 表示卡片为不可见。卡片不在前台显示，系统可能暂停更新以节省资源。 |

## LaunchReason10+

卡片创建原因枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FORM\_DEFAULT | 1 | 表示卡片创建原因为默认创建。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FORM\_SHARE | 2 | 表示卡片创建原因为共享创建。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FORM\_SIZE\_CHANGE20+ | 3 | 表示卡片创建原因为尺寸变化。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## FormUpdateReason24+

卡片更新原因枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 卡片更新的原因未知。 |
| FORM\_NODE\_REUSE | 0 | 卡片更新的原因是节点复用。 |

## OverflowInfo20+

互动卡片动效信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| area | [Rect](js-apis-app-form-forminfo.md#rect20) | 否 | 否 | 描述互动卡片动效区域范围，以卡片左上角为原点。 |
| duration | number | 否 | 否 | 互动卡片动效持续时长，单位ms。取值为大于0的整数，取值要求不大于3500。 |
| useDefaultAnimation | boolean | 否 | 是 | 互动卡片状态切换时是否启动系统提供的默认动效，默认为true。  - true：表示系统提供默认切换动效。  - false：表示系统不提供切换动效，画面直接切换，适合切换时非激活态和激活态UI完全一致的场景。 |

## Rect20+

通用矩形区域信息。可用于描述卡片坐标区域、互动卡片动效区域等信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 描述矩形的左上角顶点的 x 坐标，单位：vp，用于定位卡片区域的位置。范围参考[请求参数约束](../harmonyos-guides/arkts-ui-liveform-sceneanimation-development.md#请求参数约束)。 |
| top | number | 否 | 否 | 描述矩形的左上角顶点的 y 坐标，单位：vp，用于定位卡片区域的位置。范围参考[请求参数约束](../harmonyos-guides/arkts-ui-liveform-sceneanimation-development.md#请求参数约束)。 |
| width | number | 否 | 否 | 描述矩形的宽度，单位：vp，用于定义卡片区域的尺寸。范围参考[请求参数约束](../harmonyos-guides/arkts-ui-liveform-sceneanimation-development.md#请求参数约束)。 |
| height | number | 否 | 否 | 描述矩形的高度，单位：vp，用于定义卡片区域的尺寸。范围参考[请求参数约束](../harmonyos-guides/arkts-ui-liveform-sceneanimation-development.md#请求参数约束)。 |

## FormLocation20+

卡片当前位置枚举。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DESKTOP | 0 | 表示卡片位于桌面。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| FORM\_CENTER | 1 | 表示卡片位于桌面的卡片中心。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| FORM\_MANAGER | 2 | 表示卡片位于桌面的卡片管理器。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| NEGATIVE\_SCREEN | 3 | 表示卡片位于负一屏。 |
| SCREEN\_LOCK | 6 | 表示卡片位于锁屏页面。 |
| AI\_SUGGESTION | 7 | 表示卡片位于小艺建议的推荐区。 |
| STANDBY | 8 | 表示卡片位于待机屏保显示页面。 |

## RunningFormInfo20+

已经添加到桌面的卡片信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 是 | 否 | 卡片唯一标识，用于识别和管理已添加到桌面的卡片实例。 |
| bundleName | string | 是 | 否 | 卡片提供方所属包的Bundle名称，用于定位卡片提供方应用。 |
| moduleName | string | 是 | 否 | 卡片所属模块的名称，用于定位卡片提供方的具体模块。 |
| abilityName | string | 是 | 否 | 卡片所属的Ability名称，用于定位卡片提供方的具体Ability组件。 |
| formName | string | 是 | 否 | 卡片名称，用于标识和区分同一模块中的不同卡片。 |
| dimension | number | 是 | 否 | 卡片尺寸，用于标识卡片的大小规格。取值及其对应含义请参考[FormDimension](js-apis-app-form-forminfo.md#formdimension)。  **说明：** 取值范围[1, 9]的整数，数值5从API version 9开始支持，从API version 20开始废弃。 |
| formLocation | [FormLocation](js-apis-app-form-forminfo.md#formlocation20) | 是 | 否 | 卡片位置信息，用于标识卡片当前所在的位置（如桌面、卡片中心等）。 |
