---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager
title: functionalButtonComponentManager(场景化融合Button组件管理)
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > functionalButtonComponentManager(场景化融合Button组件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:18:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3557c7aaef350936f4ae09fd60ed07a6928ecc7240944b906d5cddf880aff7e
---

本模块提供Button组件的逻辑管理，辅助HarmonyOS应用和元服务通过Button组件完成相应功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
```

## OpenType

PhonePC/2in1TabletTV

该枚举定义了FunctionalButton组件的功能类型，通过设置该参数来指定FunctionalButton的功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GET\_PHONE\_NUMBER | 0 | 快速验证手机号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| GET\_REALTIME\_PHONENUMBER | 1 | 实时验证手机号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**    从版本5.0.0(12)开始，GET\_REALTIME\_PHONENUMBER暂不对外开放使用。 |
| LAUNCH\_APP | 2 | 打开APP。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| OPEN\_SETTING | 3 | 打开授权设置页。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**    从版本5.0.2(14)开始，OPEN\_SETTING不再演进，建议使用PERMISSION\_SETTING。 |
| CHOOSE\_AVATAR | 4 | 选择头像。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| CHOOSE\_ADDRESS | 5 | 选择地址。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| CHOOSE\_INVOICE\_TITLE | 6 | 选择发票抬头。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| REAL\_NAME\_AUTHENTICATION | 7 | 实名信息校验。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**    REAL\_NAME\_AUTHENTICATION暂不对外开放使用。 |
| FACE\_AUTHENTICATION | 8 | 人脸核身。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**    FACE\_AUTHENTICATION暂不对外开放使用。 |
| CHOOSE\_LOCATION | 9 | 地图选点。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| SUBSCRIBE\_LIVE\_VIEW | 10 | 实况窗订阅。  **起始版本：** 5.0.0(12)  **说明：**    SUBSCRIBE\_LIVE\_VIEW暂不对外开放使用。 |
| PERMISSION\_SETTING | 11 | 权限设置。  **起始版本：** 5.0.2(14)  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| REQUEST\_SUBSCRIBE\_MESSAGE | 12 | 服务动态授权码按钮的类型。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| SHARE | 13 | 分享按钮的类型。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| FEEDBACK | 14 | 反馈按钮的类型。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| GET\_PHONE\_NUMBER\_AND\_RISK\_LEVEL | 15 | 获取手机号和风险等级。  **起始版本：** 6.0.2(22)  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。 |

## SizeType

PhonePC/2in1TabletTV

该枚举定义了FunctionalButton的尺寸类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认大小。 |
| MINI | 1 | 小尺寸。 |

## HoverClassType

PhonePC/2in1TabletTV

该枚举定义了FunctionalButton点击态的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无效果。 |
| HOVER\_CLASS | 1 | 默认样式。 |

## ColorType

PhonePC/2in1TabletTV

该枚举定义了FunctionalButton的颜色类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 蓝色。 |
| PRIMARY | 1 | 绿色。 |
| WARN | 2 | 红色。 |

## CredentialType(deprecated)

PhonePC/2in1TabletTV

说明

从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口；6.0.2(23)版本前功能不可用，6.0.2(23)版本及以上正常使用。

该枚举定义了FunctionalButton的认证类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDCard | 0 | 身份证件类型。 |

## RealNameAuthenticationInfo(deprecated)

PhonePC/2in1TabletTV

说明

从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口。

该接口定义了FunctionalButton组件的实名信息校验对象（预留能力，暂未支持）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| openID | string | 否 | 否 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |
| realName | string | 否 | 否 | 证件姓名。 |
| credentialID | Uint8Array | 否 | 否 | 证件号码。 |
| credentialType | [CredentialType](scenario-fusion-functionalbuttoncomponentmanager.md#credentialtypedeprecated) | 否 | 是 | 证件类型。 |

## StyleOption

PhonePC/2in1TabletTV

该接口定义了FunctionalButton组件的样式信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | [SizeType](scenario-fusion-functionalbuttoncomponentmanager.md#sizetype) | 否 | 是 | 按钮尺寸类型。默认值：functionalButtonComponentManager.SizeType.DEFAULT，字体大小为：16fp。 |
| bgColor | [ColorType](scenario-fusion-functionalbuttoncomponentmanager.md#colortype) | 否 | 是 | 按钮颜色类型。默认值：functionalButtonComponentManager.ColorType.DEFAULT，默认蓝底白字按钮样式。 |
| plain | boolean | 否 | 是 | 按钮是否镂空。“true”表示镂空。默认值：false，不镂空。 |
| disabled | boolean | 否 | 是 | 按钮是否禁用。“true”表示按钮禁用。默认值：false，不禁用Button。 |
| loading | boolean | 否 | 是 | 名称前是否带loading图标。“true”表示名称前带loading图标。  默认值：false，关闭loading动画。 |
| hoverClass | [HoverClassType](scenario-fusion-functionalbuttoncomponentmanager.md#hoverclasstype) | 否 | 是 | 按钮按下去的样式。默认值：functionalButtonComponentManager.HoverClassType.HOVER\_CLASS，开启点击效果。 |
| hoverStartTime | number | 否 | 是 | 按住后多久出现点击态，单位毫秒。  默认值：0  取值范围： [0, +∞)  **说明：**    设置为小于0的值时，按值为0处理。 |
| hoverStayTime | number | 否 | 是 | 手指松开后点击态保留时间，单位毫秒。  默认值：0  取值范围： [0, +∞)  **说明：**    设置为小于0的值时，按值为0处理。 |
| styleConfig | [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | 否 | 是 | 按钮样式配置。  **说明：**    当styleConfig和[StyleOption](scenario-fusion-functionalbuttoncomponentmanager.md#styleoption)中定义的样式冲突时，最终以styleConfig的为准。 |

## FunctionalButtonParams

PhonePC/2in1TabletTV

该接口定义了FunctionalButton组件的参数，定义Button功能以及样式等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| openType | [OpenType](scenario-fusion-functionalbuttoncomponentmanager.md#opentype) | 否 | 否 | 按钮功能场景类型。默认值：functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 按钮展示文字。默认值：空字符串。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| styleOption | [StyleOption](scenario-fusion-functionalbuttoncomponentmanager.md#styleoption) | 否 | 是 | 按钮样式。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**    - 在Button外设置的样式属性不生效，仅生效styleOption中设置的样式。    - 使用buttonModifier、textModifier、loadingProgressModifier设置按钮样式时，对应属性会被覆盖。 |
| appParam | [AppParam](scenario-fusion-functionalbuttoncomponentmanager.md#appparam) | 否 | 是 | 需打开APP的信息。例如：{bundleName: "xxx", abilityName: "xxx"}。  bundleName：包名。  abilityName：Ability名称。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**    openType为“functionalButtonComponentManager.OpenType.LAUNCH\_APP”时必填。 |
| realNameAuthenticationInfo(deprecated) | [RealNameAuthenticationInfo](scenario-fusion-functionalbuttoncomponentmanager.md#realnameauthenticationinfodeprecated) | 否 | 是 | 实名信息校验按钮信息。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**    从5.0.0(12)开始支持，从6.0.2(22)开始废弃，无替代接口。 |
| subscribeLiveViewParam | [SubscribeLiveViewParam](scenario-fusion-functionalbuttoncomponentmanager.md#subscribeliveviewparam) | 否 | 是 | 实况窗订阅按钮信息。  **起始版本：** 5.0.0(12) |
| permissionListParam | Array<[Permissions](../harmonyos-guides/app-permissions.md)> | 否 | 是 | 权限设置Button参数。  **起始版本：** 5.0.2(14)  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。  **说明：**    需设置权限的权限名称列表，权限名称可参考[应用权限列表](../harmonyos-guides/app-permissions.md)。 |
| subSceneId | string | 否 | 是 | 子场景ID，在服务动态授权码场景时，该参数必填。参考[服务动态场景模板](../atomic-guides/push-as-timeline.md#section442012142311)，由开发者传入。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| shareParam | [ShareParam](scenario-fusion-functionalbuttoncomponentmanager.md#shareparam) | 否 | 是 | 需要分享的Button参数。  **起始版本：** 6.0.0(20)  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| buttonModifier | [ButtonModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置Button的属性，如设置按钮的样式，颜色等。  **起始版本：** 5.1.0(18)  **元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |
| textModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置文本的属性，如设置文本颜色，字体大小，字重等。  **起始版本：** 5.1.0(18)  **元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |
| loadingProgressModifier | [LoadingProgressModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置加载动效的属性，如设置加载动效的样式，颜色，定制内容区等。  **起始版本：** 5.1.0(18)  **元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。  **说明：**    使用loadingProgressModifier时，需配合styleOption设置loading为true才能生效。 |

## GetPhoneNumberResult

PhonePC/2in1TabletTV

该接口定义了使用快速验证功能成功验证的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 账号用户的临时登录凭证（Authorization Code）。  **说明：**    可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“[服务端开发](../harmonyos-guides/account-get-phonenumber.md#服务端开发)”章节。 |

## GetRealtimePhoneNumberResult

PhonePC/2in1TabletTV

该接口定义了使用实时验证功能成功验证的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 账号用户的临时登录凭证（Authorization Code）。  **说明：**    可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“[服务端开发](../harmonyos-guides/account-get-phonenumber.md#服务端开发)”章节。 |

## OpenSettingResult

PhonePC/2in1TabletTV

该接口定义了使用打开授权设置页功能，成功跳转授权设置页后返回应用或结束设置应用，应用权限设置情况的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | Map<string, boolean> | 否 | 是 | 权限字典表。  key为权限名称，value为权限是否开启，true表示开启权限，false表示关闭权限。 |

## ChooseAvatarResult

PhonePC/2in1TabletTV

该接口定义了使用选择头像功能成功选择的响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| avatarUri | string | 否 | 是 | 所选头像图片的地址。  **说明：**    返回的地址为裁剪之后的图片对应的地址。 |

## AppParam

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为打开APP功能时，通过该参数指定打开的应用对应的包名和Ability名称。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 包名。 |
| abilityName | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Ability名称。默认值：EntryAbility。 |

## ChooseAddressResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为选择收货地址功能时，通过该参数指定选择收货地址对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userName | string | 否 | 否 | 用户名称。 |
| mobileNumber | string | 否 | 是 | 手机号码。 |
| telNumber | string | 否 | 是 | 固定电话号码。 |
| zipCode | string | 否 | 是 | 邮政编码。 |
| countryCode | string | 否 | 是 | 国家/地区代码。 |
| provinceName | string | 否 | 是 | 省份名称。 |
| cityName | string | 否 | 是 | 城市名称。 |
| districtName | string | 否 | 是 | 地区名称。 |
| streetName | string | 否 | 是 | 街道名称。 |
| detailedAddress | string | 否 | 否 | 详细地址。 |

## ChooseInvoiceTitleResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为选择发票抬头功能时，通过该参数指定选择发票抬头对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 发票类型，0-个人 1-企业。 |
| title | string | 否 | 否 | 发票抬头。 |
| taxNumber | string | 否 | 否 | 税号。 |
| companyAddress | string | 否 | 是 | 公司地址。 |
| telephone | string | 否 | 是 | 电话号码。 |
| bankName | string | 否 | 是 | 银行名称。 |
| bankAccount | string | 否 | 是 | 银行账户。 |

## RealNameAuthenticationResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为实名信息校验功能时，通过该参数指定实名信息校验对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authCode | string | 否 | 是 | 临时凭据，有效时间5分钟，并且只能使用一次。 |
| openID | string | 否 | 是 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |

## FaceAuthenticationResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为人脸核身功能时，通过该参数指定人脸认证对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| authCode | string | 否 | 是 | 临时凭据，有效时间5分钟，并且只能使用一次。 |
| openID | string | 否 | 是 | OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。 |

## FaceVerificationResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为人脸核身功能时，通过该参数指定人脸核身对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| facialRecognitionVerificationToken | string | 否 | 是 | 验证成功后返回的token。 |
| state | string | 否 | 是 | 响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杆、下划线等，长度限制255，校验规则^[0-9a-zA-Z:/.-\_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。 |

## ChooseLocationResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton为地图选点功能时，通过该参数指定地图选点对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.0.1(13)之前的版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于5.0.1(13)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 位置名称。 |
| longitude | number | 否 | 否 | 经度。 |
| latitude | number | 否 | 否 | 纬度。 |
| address | string | 否 | 否 | 地址。 |

## SubscribeLiveViewParam

PhonePC/2in1TabletTV

该接口定义了FunctionalButton组件为实况窗订阅功能时，通过该参数指定实况窗订阅对应的订阅事件和计时器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | string | 否 | 否 | 订阅事件。  固定值：SUBSCRIBE\_TIMER。 |
| alertTime | number | 否 | 否 | 计时器提醒时间，毫秒级时间戳。  **说明：**    1. 参数不能为空。    2. 0<=startTime-alertTime。    3. startTime和alertTime晚于当前时间。    4. startTime-alertTime <= 3600000(可在push侧配置)。 |
| startTime | number | 否 | 否 | 计时器开始时间，毫秒级时间戳。  **说明：**    1. 参数不能为空。    2. 0<=startTime-alertTime。    3. startTime和alertTime晚于当前时间。    4. startTime-alertTime <= 3600000(可在push侧配置)。 |

## SubscribeLiveViewResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton组件为实况窗订阅功能时，通过该参数指定实况窗订阅对应的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subscribeId | string | 否 | 否 | 订阅事件ID。 |

## PermissionSettingResult

PhonePC/2in1TabletTV

该接口定义了FunctionalButton组件为权限设置功能时，通过该参数指定权限设置的返回体，用于UIAbility/UIExtensionAbility二次拉起权限设置弹框。

在调用此接口前，应用需要先调用[requestPermissionsFromUser](js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)，如果用户在首次弹窗授权时已授权，调用当前接口将无法拉起弹窗。

说明

仅支持UIAbility/UIExtensionAbility。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissionResult | Array<abilityAccessCtrl.[GrantStatus](js-apis-abilityaccessctrl.md#grantstatus)> | 否 | 否 | 权限设置结果。 |

## RequestSubscribeMessageResult

PhonePC/2in1TabletTV

该接口定义请求订阅消息的返回体。

说明

仅提供给元服务使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 否 | 服务动态授权码 。用于校验服务是否合法，服务动态等 |

## ShareParam

PhonePC/2in1TabletTV

该接口定义分享的参数。

说明

仅提供给已发布的元服务使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| description | string | 否 | 是 | 元服务描述，支持开发者传入，默认是元服务描述。 |
| previewUri | string | 否 | 是 | 元服务预览图，由开发者传入图片，否则返回默认元服务icon图标；本地文件路径、代码包文件路径或者网络图片路径。 |

## GetPhoneNumberAndRiskLevelResult

PhonePC/2in1TabletTV

该接口定义获取手机号和风险等级的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 6.0.2(22)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | string | 否 | 是 | 手机号和风险等级授权码。成功获取授权码时返回。 |
| errCode | number | 否 | 是 | 错误码。获取授权码失败时返回。 |
| errMsg | string | 否 | 是 | 错误信息。获取授权码失败时返回。 |

## 事件

PhonePC/2in1TabletTV

不支持通用事件，仅支持以下事件：

## FunctionalButtonController

PhonePC/2in1TabletTV

FunctionalButton组件控制器，用来回调组件内部的点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

### onGetPhoneNumber

PhonePC/2in1TabletTV

onGetPhoneNumber(callback: AsyncCallback<GetPhoneNumberResult>): FunctionalButtonController

注册FunctionalButton组件为快速验证手机号的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[GetPhoneNumberResult](scenario-fusion-functionalbuttoncomponentmanager.md#getphonenumberresult)> | 是 | 回调函数。当获取电话号码成功，err为undefined，data为获取到的账号用户的临时登录凭证（Authorization Code）；否则为错误对象。  **说明：**    可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“[服务端开发](../harmonyos-guides/account-get-phonenumber.md#服务端开发)”章节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
14. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
15. label: '快速验证手机号',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. },
22. // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
23. controller: new functionalButtonComponentManager.FunctionalButtonController()
24. .onGetPhoneNumber((err, data) => {
25. if (err) {
26. // 错误日志处理。
27. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
28. return;
29. }
30. // 成功日志处理。
31. hilog.info(0x0000, "testTag", "succeeded in authenticating");
32. // 获取授权码。
33. let authorizationCode = data.code;
34. })
35. })
36. }.width('100%')
37. }.height('100%')
38. }
39. }
```

### onGetRealtimePhoneNumber

PhonePC/2in1TabletTV

onGetRealtimePhoneNumber(callback: AsyncCallback<GetRealtimePhoneNumberResult>): FunctionalButtonController

注册FunctionalButton组件为实时验证手机号的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[GetRealtimePhoneNumberResult](scenario-fusion-functionalbuttoncomponentmanager.md#getrealtimephonenumberresult)> | 是 | 回调函数。当获取实时电话号码成功，err为undefined，data为获取到的账号用户的临时登录凭证（Authorization Code）；否则为错误对象。  **说明：**    可通过临时登录凭证获取真实手机号，临时登录凭证时效5分钟，具体操作可参考“[服务端开发](../harmonyos-guides/account-get-phonenumber.md#服务端开发)”章节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import {FunctionalButton, functionalButtonComponentManager} from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.GET_REALTIME_PHONENUMBER表示该按钮用于实时验证手机号码。
14. openType: functionalButtonComponentManager.OpenType.GET_REALTIME_PHONENUMBER,
15. label: '实时验证手机号',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. },
22. // 当OpenType为GET_REALTIME_PHONENUMBER时，回调必须为onGetRealtimePhoneNumber。
23. controller: new functionalButtonComponentManager.FunctionalButtonController()
24. .onGetRealtimePhoneNumber((err, data) => {
25. if (err) {
26. // 错误日志处理。
27. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
28. return;
29. }
30. // 成功日志处理。
31. hilog.info(0x0000, "testTag", "succeeded in authenticating");
32. // 获取授权码。
33. let authorizationCode = data.code;
34. })
35. })
36. }
37. .width('100%')
38. }
39. .height('100%')
40. }
41. }
```

### onLaunchApp

PhonePC/2in1TabletTV

onLaunchApp(callback: AsyncCallback<void>): FunctionalButtonController

注册FunctionalButton组件为打开APP的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[startAbility](js-apis-inner-application-uiabilitycontext.md#startability)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当打开APP完成，err为undefined，否则返回错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.LAUNCH_APP表示该按钮用于启动应用。
14. openType: functionalButtonComponentManager.OpenType.LAUNCH_APP,
15. label: '打开APP',
16. // 当OpenType为functionButtonComponentManager.OpenType.LAUNCH_APP时，appParam为必填项。
17. appParam: {
18. bundleName: "xxx",
19. abilityName: "xxx"
20. },
21. // 调整按钮样式。
22. styleOption: {
23. styleConfig: new functionalButtonComponentManager.ButtonConfig()
24. .fontSize(20)
25. },
26. },
27. // 当OpenType设置为LAUNCH_APP时，回调函数必须是onLaunchApp。
28. controller: new functionalButtonComponentManager.FunctionalButtonController().onLaunchApp((err) => {
29. if (err) {
30. // 错误日志处理。
31. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
32. return;
33. }
34. // 处理成功。成功时不会返回任何值。
35. hilog.info(0x0000, "testTag", "succeeded in launching app");
36. })
37. })
38. }.width('100%')
39. }.height('100%')
40. }
41. }
```

说明

“bundleName”为包名，“abilityName”为Ability名称。

### onOpenSetting

PhonePC/2in1TabletTV

onOpenSetting(callback: AsyncCallback<OpenSettingResult>): FunctionalButtonController

注册FunctionalButton组件为打开授权设置页的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[OpenSettingResult](scenario-fusion-functionalbuttoncomponentmanager.md#opensettingresult)> | 是 | 回调函数。当打开授权设置页成功，err为undefined，data为打开设置成功时返回的响应；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.OPEN_SETTING表示该按钮用于打开授权设置页面。
14. openType: functionalButtonComponentManager.OpenType.OPEN_SETTING,
15. label: '打开授权设置页',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. },
22. // 当OpenType为OPEN_SETTING时，回调必须为onOpenSetting。
23. controller: new functionalButtonComponentManager.FunctionalButtonController().onOpenSetting((err, data) => {
24. if (err) {
25. // 错误日志处理。
26. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
27. return;
28. }
29. // 成功处理，当应用程序进程停止时触发。
30. hilog.info(0x0000, "testTag", "succeeded in opening setting");
31. data.permissions!.forEach((value, key) => {
32. hilog.info(0x0000, "testTag", "key: %{public}s value: %{public}s", String(key), value);
33. })
34. })
35. })
36. }.width('100%')
37. }.height('100%')
38. }
39. }
```

### onChooseAvatar

PhonePC/2in1TabletTV

onChooseAvatar(callback: AsyncCallback<ChooseAvatarResult>): FunctionalButtonController

注册FunctionalButton组件为选择头像的点击事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ChooseAvatarResult](scenario-fusion-functionalbuttoncomponentmanager.md#chooseavatarresult)> | 是 | 回调函数。当选择头像调用成功，err为undefined，data为选择头像成功时返回的所选头像图片的地址；否则为错误对象。  **说明：**    返回的地址为裁剪之后的图片对应的地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. // 将account.png文件添加到/resources/base/media/目录中。否则，将显示错误信息，提示找不到该文件。
8. @State url: ResourceStr = $r('app.media.account');

10. build() {
11. Column() {
12. // 构建FunctionalButton组件实例。
13. FunctionalButton({
14. params: {
15. // OpenType.CHOOSE_AVATAR表示该按钮用于选择头像。
16. openType: functionalButtonComponentManager.OpenType.CHOOSE_AVATAR,
17. label: '',
18. // 调整按钮样式。
19. styleOption: {
20. styleConfig: new functionalButtonComponentManager.ButtonConfig()
21. .type(ButtonType.Normal)
22. .backgroundImage(this.url)
23. .backgroundImageSize(ImageSize.Cover)
24. .width(80)
25. .height(80)
26. .backgroundColor('#E5E5E5')
27. },
28. },
29. // 当OpenType设置为CHOOSE_AVATAR时，回调函数必须是onChooseAvatar。
30. controller: new functionalButtonComponentManager.FunctionalButtonController().onChooseAvatar((err, data) => {
31. if (err) {
32. // 错误日志处理。
33. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
34. return;
35. }
36. // 成功日志处理。
37. hilog.info(0x0000, "testTag", "succeeded in choosing avatar");
38. this.url = data.avatarUri!;
39. })
40. })
41. }
42. .padding({ top: 200 })
43. .height('100%')
44. .width('100%')
45. }
46. }
```

### onChooseAddress

PhonePC/2in1TabletTV

onChooseAddress(callback: AsyncCallback<ChooseAddressResult>): FunctionalButtonController

注册FunctionalButton组件为选择收货地址的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[chooseAddress](account-choose-address.md#chooseaddress)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ChooseAddressResult](scenario-fusion-functionalbuttoncomponentmanager.md#chooseaddressresult)> | 是 | 回调函数。当选择收货地址点击成功，err为undefined，data为选择收货地址的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.CHOOSE_ADDRESS表示该按钮用于选择收货地址。
14. openType: functionalButtonComponentManager.OpenType.CHOOSE_ADDRESS,
15. label: '选择收货地址',
16. // 调整按钮样式。
17. styleOption: {
18. bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
19. size: functionalButtonComponentManager.SizeType.DEFAULT,
20. plain: false,
21. disabled:false,
22. loading: false,
23. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
24. hoverStartTime: 0,
25. hoverStayTime: 0,
26. styleConfig: new functionalButtonComponentManager.ButtonConfig()
27. .fontSize(20)
28. },
29. },
30. // 当OpenType设置为CHOOSE_ADDRESS时，回调必须为onChooseAddress。
31. controller: new functionalButtonComponentManager.FunctionalButtonController()
32. .onChooseAddress((err, data) => {
33. if (err) {
34. // 错误日志处理。
35. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
36. return;
37. }
38. // 成功日志处理。
39. hilog.info(0x0000, "testTag", "succeeded in choosing address");
40. // 获取地址信息。
41. let userName: string = data.userName;
42. let mobileNumber: string = data.mobileNumber as string;
43. let countryCode: string = data.countryCode as string;
44. let provinceName: string = data.provinceName as string;
45. let cityName: string = data.cityName as string;
46. let districtName: string = data.districtName as string;
47. let streetName: string = data.streetName as string;
48. let detailedAddress: string = data.detailedAddress;
49. })
50. })
51. }.width('100%')
52. }.height('100%')
53. }
54. }
```

### onChooseInvoiceTitle

PhonePC/2in1TabletTV

onChooseInvoiceTitle(callback: AsyncCallback<ChooseInvoiceTitleResult>): FunctionalButtonController

注册FunctionalButton组件为选择发票抬头的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[selectInvoiceTitle](account-api-invoiceassistant.md#selectinvoicetitle)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ChooseInvoiceTitleResult](scenario-fusion-functionalbuttoncomponentmanager.md#chooseinvoicetitleresult)> | 是 | 回调函数。当选择发票抬头点击成功，err为undefined，data为选择发票抬头的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.CHOOSE_INVOICE_TITLE表示该按钮用于选择发票标题。
14. openType: functionalButtonComponentManager.OpenType.CHOOSE_INVOICE_TITLE,
15. label: '选择发票抬头',
16. // 调整按钮样式。
17. styleOption: {
18. bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
19. size: functionalButtonComponentManager.SizeType.DEFAULT,
20. plain: false,
21. disabled:false,
22. loading: false,
23. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
24. hoverStartTime: 0,
25. hoverStayTime: 0,
26. styleConfig: new functionalButtonComponentManager.ButtonConfig()
27. .fontSize(20)
28. },
29. },
30. // 当OpenType为CHOOSE_INVOICE_TITLE时，回调必须为onChooseInvoiceTitle。
31. controller: new functionalButtonComponentManager.FunctionalButtonController()
32. .onChooseInvoiceTitle((err, data) => {
33. if (err) {
34. // 错误日志处理。
35. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
36. return;
37. }
38. // 成功日志处理。
39. hilog.info(0x0000, "testTag", "succeeded in obtaining invoice title");
40. // 获取发票信息。
41. let type: string = data.type;
42. let title: string = data.title;
43. let taxNumber: string = data.taxNumber;
44. let companyAddress: string | undefined = data.companyAddress;
45. let telephone: string | undefined = data.telephone;
46. let bankName: string | undefined = data.bankName;
47. let bankAccount: string | undefined = data.bankAccount;
48. })
49. })
50. }.width('100%')
51. }.height('100%')
52. }
53. }
```

### onRealNameAuthentication

PhonePC/2in1TabletTV

onRealNameAuthentication(callback: AsyncCallback<RealNameAuthenticationResult>): FunctionalButtonController

注册FunctionalButton组件为实名信息校验的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)，[AuthenticationController](account-api-authentication.md#authenticationcontroller)，[executeRequest](account-api-authentication.md#executerequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[RealNameAuthenticationResult](scenario-fusion-functionalbuttoncomponentmanager.md#realnameauthenticationresult)> | 是 | 回调函数。当实名信息校验成功，err为undefined，data为获取到的实名信息校验鉴权对应的返回体：authCode、openID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { http } from '@kit.NetworkKit';
4. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

6. interface Result {
7. state?: number;
8. realNameLevel?: number;
9. verifyResult?: number;
10. verifyToken?: string;
11. }

13. @Entry
14. @Component
15. struct SecondPage {

17. obtainRealNameDataInfo(authCode: string, sceneID:number, openID: string, realName: string, idNo: string,
18. callback: AsyncCallback<Result>) {
19. // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
20. let httpRequest = http.createHttp();
21. // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
22. httpRequest.on('headersReceive', (header) => {
23. hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
24. });
25. httpRequest.request(
26. // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
27. "EXAMPLE_URL",
28. {
29. method: http.RequestMethod.POST,
30. // 您可以根据服务需求添加头部字段。
31. header: {
32. 'Content-Type': 'application/json'
33. },
34. // 使用此字段在POST请求中传递信息。
35. extraData: {
36. "authCode": authCode,
37. "sceneID": sceneID,
38. "openID": openID,
39. "realname": realName,
40. "idNo": idNo,
41. },
42. expectDataType: http.HttpDataType.STRING,
43. usingCache: true,
44. priority: 1,
45. connectTimeout: 60000,
46. readTimeout: 60000,
47. usingProtocol: http.HttpProtocol.HTTP1_1,
48. }, (err, data) => {
49. if (!err) {
50. let res: Result = JSON.parse(data.result as string);
51. callback(undefined, res);
52. } else {
53. let error: BusinessError = {code: err.code, message: err.message, name: ''};
54. callback(error, undefined);
55. // 取消订阅HTTP响应头事件。
56. httpRequest.off('headersReceive');
57. // 在httpRequest完成后调用destroy()方法以释放资源。
58. httpRequest.destroy();
59. }
60. })
61. }

63. build() {
64. Row() {
65. Column() {
66. FunctionalButton({
67. params: {
68. // OpenType.REAL_NAME_AUTHENTICATION表示该按钮用于实名信息校验。
69. openType: functionalButtonComponentManager.OpenType.REAL_NAME_AUTHENTICATION,
70. label: '实名信息校验',
71. // 调整按钮样式。
72. styleOption: {
73. styleConfig: new functionalButtonComponentManager.ButtonConfig()
74. .fontSize(20)
75. },
76. },
77. // 当OpenType设置为REAL_NAME_AUTHENTICATION时，回调必须为onRealNameAuthentication。
78. controller: new functionalButtonComponentManager.FunctionalButtonController()
79. .onRealNameAuthentication((err, data) => {
80. if (err) {
81. // 错误日志处理。
82. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
83. return;
84. }
85. // 成功日志处理。
86. hilog.info(0x0000, "testTag", "succeeded in authenticating");
87. // 获取授权码。
88. let authCode: string = data.authCode as string;
89. let openID: string = data.openID as string;
90. // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
91. this.obtainRealNameDataInfo(authCode, 0, openID, 'name', 'idNo', (err, data) => {
92. if (err) {
93. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
94. return;
95. }
96. let state = data.state;
97. let realNameLevel = data.realNameLevel;
98. let verifyResult = data.verifyResult;
99. let verifyToken = data.verifyToken;
100. hilog.info(0x0000, "testTag", "succeeded in verifying");
101. })
102. })
103. })
104. }
105. .width('100%')
106. }
107. .height('100%')
108. }
109. }
```

### onFaceAuthentication

PhonePC/2in1TabletTV

onFaceAuthentication(callback: AsyncCallback<FaceAuthenticationResult>): FunctionalButtonController

注册FunctionalButton组件为人脸核身的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)，[AuthenticationController](account-api-authentication.md#authenticationcontroller)，[executeRequest](account-api-authentication.md#executerequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[FaceAuthenticationResult](scenario-fusion-functionalbuttoncomponentmanager.md#faceauthenticationresult)> | 是 | 回调函数。当人脸认证成功，err为undefined，data为获取到的人脸认证对应的返回体：authCode、openID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { http } from '@kit.NetworkKit';
4. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

6. interface Result {
7. state?: number;
8. realNameLevel?: number;
9. verifyResult?: number;
10. verifyToken?: string;
11. }

13. @Entry
14. @Component
15. struct SecondPage {
16. obtainFaceVerifyDataInfo(authCode: string, sceneID: number, openID: string, realName: string, idNo: string,
17. callback: AsyncCallback<Result>) {
18. // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
19. let httpRequest = http.createHttp();
20. // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
21. httpRequest.on('headersReceive', (header) => {
22. hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
23. });
24. httpRequest.request(
25. // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
26. "EXAMPLE_URL",
27. {
28. method: http.RequestMethod.POST,
29. // 您可以根据服务需求添加头部字段。
30. header: {
31. 'Content-Type': 'application/json'
32. },
33. // 使用此字段在POST请求中传递信息。
34. extraData: {
35. "authCode": authCode,
36. "sceneID": sceneID,
37. "openID": openID,
38. "realname": realName,
39. "idNo": idNo,
40. },
41. expectDataType: http.HttpDataType.STRING,
42. usingCache: true,
43. priority: 1,
44. connectTimeout: 60000,
45. readTimeout: 60000,
46. usingProtocol: http.HttpProtocol.HTTP1_1,
47. }, (err, data) => {
48. if (!err) {
49. let res: Result = JSON.parse(data.result as string);
50. callback(undefined, res);
51. } else {
52. let error: BusinessError = { code: err.code, message: err.message, name: '' };
53. callback(error, undefined);
54. // 取消订阅HTTP响应头事件。
55. httpRequest.off('headersReceive');
56. // 在httpRequest完成后调用destroy()方法以释放资源。
57. httpRequest.destroy();
58. }
59. })
60. }

62. build() {
63. Row() {
64. Column() {
65. FunctionalButton({
66. params: {
67. // OpenType.FACE_AUTHENTICATION表示该按钮用于人脸身份验证。
68. openType: functionalButtonComponentManager.OpenType.FACE_AUTHENTICATION,
69. label: '人脸核身',
70. // 调整按钮样式。
71. styleOption: {
72. styleConfig: new functionalButtonComponentManager.ButtonConfig()
73. .fontSize(20)
74. },
75. },
76. // 当OpenType为FACE_AUTHENTICATION时，回调必须为onFaceAuthentication。
77. controller: new functionalButtonComponentManager.FunctionalButtonController()
78. .onFaceAuthentication((err, data) => {
79. if (err) {
80. // 错误日志处理。
81. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
82. return;
83. }
84. // 成功日志处理。
85. hilog.info(0x0000, "testTag", "succeeded in authenticating");
86. // 获取授权码。
87. let authCode: string = data.authCode as string;
88. let openID: string = data.openID as string;
89. hilog.info(0x0000, "testTag", "succeeded in authCode");
90. // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
91. this.obtainFaceVerifyDataInfo(authCode, 2, openID, "", "", (err, data) => {
92. if (err) {
93. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
94. return;
95. }
96. let verifyToken: string = data.verifyToken as string;
97. new functionalButtonComponentManager.FunctionalButtonController().onFaceVerification(verifyToken,
98. (error, data) => {
99. if (error) {
100. // 错误日志处理。
101. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", error.code, error.message);
102. return;
103. }
104. let facialRecognitionVerificationToken = data.facialRecognitionVerificationToken;
105. let state = data.state;
106. hilog.info(0x0000, 'testTag', 'auth result success');
107. });
108. })
109. })
110. })
111. }
112. .width('100%')
113. }
114. .height('100%')
115. }
116. }
```

### onFaceVerification

PhonePC/2in1TabletTV

onFaceVerification(verifyToken: string, callback: AsyncCallback<FaceVerificationResult>): void

注册FunctionalButton组件为人脸验证的点击事件，使用callback异步回调。

该接口功能依赖Account Kit，参见[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)，[AuthenticationController](account-api-authentication.md#authenticationcontroller)，[executeRequest](account-api-authentication.md#executerequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在2in1中返回1001500003错误码，在TV中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| verifyToken | string | 是 | 验证成功的idToken，三方应用拉起华为账号客户端人脸验证页面时传入此Token，供华为账号客户端校验验证结果，参见[FacialRecognitionVerificationRequest](account-api-realname.md#facialrecognitionverificationrequest)。 |
| callback | AsyncCallback<[FaceVerificationResult](scenario-fusion-functionalbuttoncomponentmanager.md#faceverificationresult)> | 是 | 回调函数。当人脸验证点击成功，err为undefined，data为人脸验证的返回结果；否则为错误对象。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { http } from '@kit.NetworkKit';
4. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

6. interface Result {
7. state?: number;
8. realNameLevel?: number;
9. verifyResult?: number;
10. verifyToken?: string;
11. }

13. @Entry
14. @Component
15. struct SecondPage {
16. obtainFaceVerifyDataInfo(authCode: string, sceneID: number, openID: string, realName: string, idNo: string,
17. callback: AsyncCallback<Result>) {
18. // 每个httpRequest对应一个HTTP请求任务，且不可重复使用。
19. let httpRequest = http.createHttp();
20. // 监听HTTP响应头事件，该事件比HTTP请求的响应返回得更早。是否监听HTTP响应头事件由您决定。
21. httpRequest.on('headersReceive', (header) => {
22. hilog.info(0x0000, "testTag", "header: %{public}s", header as string);
23. });
24. httpRequest.request(
25. // 请自行在extraData中自定义EXAMPLE_URL。是否向URL添加参数由您决定。
26. "EXAMPLE_URL",
27. {
28. method: http.RequestMethod.POST,
29. // 您可以根据服务需求添加头部字段。
30. header: {
31. 'Content-Type': 'application/json'
32. },
33. // 使用此字段在POST请求中传递信息。
34. extraData: {
35. "authCode": authCode,
36. "sceneID": sceneID,
37. "openID": openID,
38. "realname": realName,
39. "idNo": idNo,
40. },
41. expectDataType: http.HttpDataType.STRING,
42. usingCache: true,
43. priority: 1,
44. connectTimeout: 60000,
45. readTimeout: 60000,
46. usingProtocol: http.HttpProtocol.HTTP1_1,
47. }, (err, data) => {
48. if (!err) {
49. let res: Result = JSON.parse(data.result as string);
50. callback(undefined, res);
51. } else {
52. let error: BusinessError = { code: err.code, message: err.message, name: '' };
53. callback(error, undefined);
54. // 取消订阅HTTP响应头事件。
55. httpRequest.off('headersReceive');
56. // 在httpRequest完成后调用destroy()方法以释放资源。
57. httpRequest.destroy();
58. }
59. })
60. }

62. build() {
63. Row() {
64. Column() {
65. FunctionalButton({
66. params: {
67. // OpenType.FACE_AUTHENTICATION表示该按钮用于人脸身份验证。
68. openType: functionalButtonComponentManager.OpenType.FACE_AUTHENTICATION,
69. label: '人脸核身',
70. // 调整按钮样式。
71. styleOption: {
72. styleConfig: new functionalButtonComponentManager.ButtonConfig()
73. .fontSize(20)
74. },
75. },
76. // 当OpenType为FACE_AUTHENTICATION时，回调必须为onFaceAuthentication。
77. controller: new functionalButtonComponentManager.FunctionalButtonController()
78. .onFaceAuthentication((err, data) => {
79. if (err) {
80. // 错误日志处理。
81. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
82. return;
83. }
84. // 成功日志处理。
85. hilog.info(0x0000, "testTag", "succeeded in authenticating");
86. // 获取授权码。
87. let authCode: string = data.authCode as string;
88. let openID: string = data.openID as string;
89. hilog.info(0x0000, "testTag", "succeeded in authCode");
90. // sceneid 表示场景ID。选项包括：0（实名验证）、1（人脸验证，验证姓名、证件类型、证件号码和人脸）和2（人脸验证，仅验证人脸）。
91. this.obtainFaceVerifyDataInfo(authCode, 2, openID, "", "", (err, data) => {
92. if (err) {
93. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
94. return;
95. }
96. let verifyToken: string = data.verifyToken as string;
97. new functionalButtonComponentManager.FunctionalButtonController().onFaceVerification(verifyToken,
98. (error, data) => {
99. if (error) {
100. // 错误日志处理。
101. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", error.code, error.message);
102. return;
103. }
104. let facialRecognitionVerificationToken = data.facialRecognitionVerificationToken;
105. let state = data.state;
106. hilog.info(0x0000, 'testTag', 'auth result success');
107. });
108. })
109. })
110. })
111. }
112. .width('100%')
113. }
114. .height('100%')
115. }
116. }
```

### onChooseLocation

PhonePC/2in1TabletTV

onChooseLocation(callback: AsyncCallback<ChooseLocationResult>): FunctionalButtonController

注册FunctionalButton组件为打开地图选点的点击事件，使用callback异步回调。

该接口功能依赖Map Kit，参见[chooseLocation](map-scenemap.md#chooselocation)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.0.1(13)之前的版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于5.0.1(13)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ChooseLocationResult](scenario-fusion-functionalbuttoncomponentmanager.md#chooselocationresult)> | 是 | 回调函数。当打开地图选点成功，err为undefined，data为地图选点的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.CHOOSE_LOCATION表示该按钮用于在地图上选择位置。
14. openType: functionalButtonComponentManager.OpenType.CHOOSE_LOCATION,
15. label: '地图选点',
16. // 调整按钮样式。
17. styleOption: {
18. bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
19. size: functionalButtonComponentManager.SizeType.DEFAULT,
20. plain: false,
21. disabled:false,
22. loading: false,
23. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
24. hoverStartTime: 0,
25. hoverStayTime: 0,
26. styleConfig: new functionalButtonComponentManager.ButtonConfig()
27. .fontSize(20)
28. },
29. },
30. // 当OpenType设置为CHOOSE_LOCATION时，回调必须为onChooseLocation。
31. controller: new functionalButtonComponentManager.FunctionalButtonController()
32. .onChooseLocation((err, data) => {
33. if (err) {
34. // 错误日志处理。
35. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
36. return;
37. }
38. // 成功日志处理。
39. hilog.info(0x0000, "testTag", "succeeded in choosing location");
40. let name: string = data.name;
41. let address: string = data.address;
42. let longitude: number = data.longitude;
43. let latitude: number = data.latitude;
44. })
45. })
46. }.width('100%')
47. }.height('100%')
48. }
49. }
```

### onSubscribeLiveView

PhonePC/2in1TabletTV

onSubscribeLiveView(callback: AsyncCallback<SubscribeLiveViewResult>): FunctionalButtonController

注册FunctionalButton组件为实况窗订阅的点击事件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SubscribeLiveViewResult](scenario-fusion-functionalbuttoncomponentmanager.md#subscribeliveviewresult)> | 是 | 回调函数。当实况窗订阅点击成功，err为undefined，data为实况订阅的返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.SUBSCRIBE_LIVE_VIEW表示该按钮用于实时视图订阅。
14. openType: functionalButtonComponentManager.OpenType.SUBSCRIBE_LIVE_VIEW,
15. label: '预约抢购',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. subscribeLiveViewParam: {
22. event: "SUBSCRIBE_TIMER",
23. alertTime: 172178838111,
24. startTime: 172170198111
25. },
26. },
27. // 当OpenType为SUBSCRIBE_LIVE_VIEW时，回调必须为onSubscribeLiveView。
28. controller: new functionalButtonComponentManager.FunctionalButtonController().onSubscribeLiveView((err,
29. data) => {
30. if (err) {
31. // 错误日志处理。
32. hilog.error(0x0000, "testTag", `error code is: ${err?.code} message is ${err?.message}`);
33. return;
34. }
35. let subscribeId = data.subscribeId;
36. // 成功日志处理。
37. hilog.info(0x0000, "testTag", "succeeded in subscribing LiveView");
38. })
39. })
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }
45. }
```

### onPermissionSetting

PhonePC/2in1TabletTV

onPermissionSetting(callback: AsyncCallback<PermissionSettingResult>): FunctionalButtonController

注册FunctionalButton组件为权限设置的点击事件，使用callback异步回调。

该接口功能依赖Ability Kit，参见[requestPermissionOnSetting](js-apis-abilityaccessctrl.md#requestpermissiononsetting12)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于5.1.0(18)之前的版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PermissionSettingResult](scenario-fusion-functionalbuttoncomponentmanager.md#permissionsettingresult)> | 是 | 回调函数。当权限设置点击成功，err为undefined，data为获取到的权限设置返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. Row() {
11. Column({ space: 3 }) {
12. // 调用requestPermissionsFromUser接口Button。
13. Button('请求用户授权')
14. .fontSize(20)
15. .onClick(() => {
16. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
17. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
18. try {
19. // 在module.json5文件中添加ohos.permission.READ_CALENDAR、ohos.permission.WRITE_CALENDAR权限。
20. atManager.requestPermissionsFromUser(context,
21. ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
22. (err: BusinessError, data: PermissionRequestResult) => {
23. if (err) {
24. hilog.error(0x0000, "testTag", "failed in requesting Permissions from user : %{public}d %{public}s",
25. err.code, err.message);
26. } else {
27. hilog.info(0x0000, "testTag", 'data permissions: %{public}s', data.permissions?.join(','));
28. hilog.info(0x0000, "testTag", 'data authResults: %{public}s', data.authResults?.join(','));
29. hilog.info(0x0000, "testTag", 'data dialogShownResults: %{public}s',data.dialogShownResults?.join(','));
30. }
31. })
32. } catch (err) {
33. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
34. }
35. })

37. // 构建FunctionalButton组件实例。
38. FunctionalButton({
39. params: {
40. // OpenType.PERMISSION_SETTING表示该按钮用于设置权限。
41. openType: functionalButtonComponentManager.OpenType.PERMISSION_SETTING,
42. label: '权限设置',
43. permissionListParam: ['ohos.permission.READ_CALENDAR', 'ohos.permission.WRITE_CALENDAR'],
44. // 调整按钮样式。
45. styleOption: {
46. styleConfig: new functionalButtonComponentManager.ButtonConfig()
47. .fontSize(20)
48. },
49. },
50. // 当OpenType设置为PERMISSION_SETTING时，回调必须为onPermissionSetting。
51. controller: new functionalButtonComponentManager.FunctionalButtonController().onPermissionSetting((err,
52. data) => {
53. if (err) {
54. // 错误日志处理。
55. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
56. return;
57. }
58. // 成功日志处理。
59. hilog.info(0x0000, "testTag", "succeeded in setting permission ");
60. let result = data.permissionResult;
61. result.forEach(res => {
62. hilog.info(0x0000, "testTag", "data: %{public}s", String(res));
63. })
64. })
65. })
66. }
67. .width('100%')
68. }
69. .height('100%')
70. }
71. }
```

### onRequestSubscribeMessage

PhonePC/2in1TabletTV

onRequestSubscribeMessage(callback: AsyncCallback<RequestSubscribeMessageResult>): FunctionalButtonController

注册FunctionalButton组件为服务动态授权码按钮的点击事件，使用callback异步回调。

说明

该接口在元服务中可正常使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于6.1.0(23)之前的版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[RequestSubscribeMessageResult](scenario-fusion-functionalbuttoncomponentmanager.md#requestsubscribemessageresult)> | 是 | 回调函数。当服务动态授权码按钮点击成功，err为undefined，data为获取到的code返回结果；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10004](scenario-fusion-error-code.md#section10004-系统内部异常) | Internal error. |
| [10008](scenario-fusion-error-code.md#section10008-调用方非元服务) | Not atomic service. |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Row() {
8. Column() {
9. // 构建FunctionalButton组件实例。
10. FunctionalButton({
11. params: {
12. // OpenType.REQUEST_SUBSCRIBE_MESSAGE表示该按钮用于获取服务动态授权码。
13. openType: functionalButtonComponentManager.OpenType.REQUEST_SUBSCRIBE_MESSAGE,
14. label: '服务动态授权码',
15. // 在获取服务动态授权码时，名为subSceneId的参数是必填项。
16. subSceneId: '',
17. // 调整按钮样式。
18. styleOption: {
19. styleConfig: new functionalButtonComponentManager.ButtonConfig()
20. .fontSize(20)
21. },
22. },
23. // 当OpenType为REQUEST_SUBSCRIBE_MESSAGE时，回调必须为onRequestSubscribeMessage。
24. controller: new functionalButtonComponentManager.FunctionalButtonController()
25. .onRequestSubscribeMessage((err, data) => {
26. if (err) {
27. // 错误日志处理。
28. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
29. return;
30. }
31. // 成功日志处理。
32. hilog.info(0x0000, "testTag", "succeeded in requesting subscribe message");
33. // 处理服务代码。
34. let code = data.code;
35. })
36. })
37. }.width('100%')
38. }.height('100%')
39. }
40. }
```

### onShare

PhonePC/2in1TabletTV

onShare(callback: AsyncCallback<void>): FunctionalButtonController

注册FunctionalButton组件为分享按钮的点击事件，使用callback异步回调。

说明

仅提供给已发布的元服务使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于6.1.0(23)之前的版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当分享按钮点击成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10004](scenario-fusion-error-code.md#section10004-系统内部异常) | Internal error. |
| [10006](scenario-fusion-error-code.md#section10006-获取分享数据失败) | Failed to get data. |
| [10008](scenario-fusion-error-code.md#section10008-调用方非元服务) | Not atomic service. |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.SHARE 表示该按钮用于调出分享页面。
14. openType: functionalButtonComponentManager.OpenType.SHARE,
15. label: '元服务分享',
16. shareParam: {
17. previewUri: '',
18. description: ''
19. },
20. // 调整按钮样式。
21. styleOption: {
22. styleConfig: new functionalButtonComponentManager.ButtonConfig()
23. .fontSize(20)
24. },
25. },
26. // 当OpenType设置为SHARE时，回调函数必须是onShare。
27. controller: new functionalButtonComponentManager.FunctionalButtonController()
28. .onShare((err) => {
29. if (err) {
30. // 错误日志处理。
31. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
32. return;
33. }
34. // 成功日志处理。
35. hilog.info(0x0000, "testTag", "succeeded in pulling up the sharing page");
36. })
37. })
38. }.width('100%')
39. }.height('100%')
40. }
41. }
```

### onFeedback

PhonePC/2in1TabletTV

onFeedback(callback: AsyncCallback<void>): FunctionalButtonController

注册FunctionalButton组件为反馈按钮的点击事件，使用callback异步回调。

说明

仅提供给元服务使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 对于6.1.0(23)之前的版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当反馈按钮点击成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [10008](scenario-fusion-error-code.md#section10008-调用方非元服务) | Not atomic service. |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.FEEDBACK表示该按钮用于拉起反馈页面。
14. openType: functionalButtonComponentManager.OpenType.FEEDBACK,
15. label: '反馈与投诉',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. },
22. // 当OpenType设置为FEEDBACK时，回调函数必须是onFeedback。
23. controller: new functionalButtonComponentManager.FunctionalButtonController()
24. .onFeedback((err) => {
25. if (err) {
26. // 错误日志处理。
27. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
28. return;
29. }
30. // 成功日志处理。
31. hilog.info(0x0000, "testTag", "succeeded in pulling up the feedback page");
32. })
33. })
34. }.width('100%')
35. }.height('100%')
36. }
37. }
```

### onGetPhoneNumberAndRiskLevel

PhonePC/2in1TabletTV

onGetPhoneNumberAndRiskLevel(callback: Callback<GetPhoneNumberAndRiskLevelResult>): FunctionalButtonController

注册FunctionalButton组件为获取手机号和风险等级的点击事件，使用callback同步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[GetPhoneNumberAndRiskLevelResult](scenario-fusion-functionalbuttoncomponentmanager.md#getphonenumberandrisklevelresult)> | 是 | 回调函数。返回获取手机号和风险等级的授权码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | [FunctionalButton](scenario-fusion-functionalbutton.md#functionalbutton)组件控制器。 |

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL表示该按钮用于获取手机号和风险等级。
14. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER_AND_RISK_LEVEL,
15. label: '获取手机号和风险等级',
16. // 调整按钮样式。
17. styleOption: {
18. styleConfig: new functionalButtonComponentManager.ButtonConfig()
19. .fontSize(20)
20. },
21. },
22. // 当OpenType为GET_PHONE_NUMBER_AND_RISK_LEVEL时，回调必须为onGetPhoneNumberAndRiskLevel。
23. controller: new functionalButtonComponentManager.FunctionalButtonController()
24. .onGetPhoneNumberAndRiskLevel((data) => {
25. if (data?.errCode) {
26. // 错误日志处理。
27. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", data?.errCode, data?.errMsg);
28. return;
29. }
30. // 成功日志处理。
31. hilog.info(0x0000, "testTag", "succeeded in authentication");
32. // 授权码处理。
33. let authorizationCode = data?.code;
34. })
35. })
36. }
37. .width('100%')
38. }
39. .height('100%')
40. }
41. }
```

## ButtonConfig

PhonePC/2in1TabletTV

该类提供了实现FunctionalButton自定义属性的方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

### type

PhonePC/2in1TabletTV

type(value: ButtonType): ButtonConfig

设置FunctionalButton的显示样式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonType](ts-basic-components-button.md#buttontype枚举说明) | 是 | 描述按钮显示样式。  默认值：ButtonType.Capsule |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### stateEffect

PhonePC/2in1TabletTV

stateEffect(value: boolean): ButtonConfig

设置FunctionalButton是否开启按压态显示效果属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭；设置为true时，按压效果开启。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### fontColor

PhonePC/2in1TabletTV

fontColor(value: ResourceColor): ButtonConfig

设置FunctionalButton的字体颜色属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置字体颜色。  默认值：#ffffff |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### fontSize

PhonePC/2in1TabletTV

fontSize(value: Length): ButtonConfig

设置FunctionalButton的字体大小属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置字体大小，[Length](ts-types.md#length)为number类型时，使用fp单位。  字体默认大小16fp。不支持设置百分比字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### fontWeight

PhonePC/2in1TabletTV

fontWeight(value: string | number | FontWeight): ButtonConfig

设置FunctionalButton的字体粗细属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | [FontWeight](ts-appendix-enums.md#fontweight) | 是 | 设置文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"，"bolder"，"lighter"，"regular"，"medium"，"normal"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### fontStyle

PhonePC/2in1TabletTV

fontStyle(value: FontStyle): ButtonConfig

设置FunctionalButton的字体样式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 设置字体样式。  默认值：FontStyle.Normal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### fontFamily

PhonePC/2in1TabletTV

fontFamily(value: string | Resource): ButtonConfig

设置FunctionalButton的字体属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 设置字体列表。默认字体'HarmonyOS Sans'，当前支持'[HarmonyOS Sans](../design-guides/font-0000001828772001.md#section51091561209)'字体和[注册自定义字体](js-apis-font.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### width

PhonePC/2in1TabletTV

width(value: Length): ButtonConfig

设置FunctionalButton的宽度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### height

PhonePC/2in1TabletTV

height(value: Length): ButtonConfig

设置FunctionalButton的高度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置组件自身的高度，缺省时使用元素自身内容需要的高度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### size

PhonePC/2in1TabletTV

size(value: SizeOptions): ButtonConfig

设置FunctionalButton的高宽尺寸属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | 是 | 设置高宽尺寸。举例：  {  width: 20,  height: 50  }  单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### constraintSize

PhonePC/2in1TabletTV

constraintSize(value: ConstraintSizeOptions): ButtonConfig

设置FunctionalButton的约束尺寸属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 设置约束尺寸，组件布局时，进行尺寸范围限制。constraintSize的优先级高于width和height。取值结果参考[constraintSize取值对width/height影响](ts-universal-attributes-size.md#constraintsize)。  默认值：  {  minWidth: 0,  maxWidth: Infinity,  minHeight: 0,  maxHeight: Infinity  }  单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### padding

PhonePC/2in1TabletTV

padding(value: Length | Padding): ButtonConfig

设置FunctionalButton的内边距属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [Padding](ts-types.md#padding) | 是 | 设置内边距属性。  参数为Length类型时，四个方向内边距同时生效。  默认值：{left: 16, right: 16}  单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### margin

PhonePC/2in1TabletTV

margin(value: Length | Padding): ButtonConfig

设置FunctionalButton的外边距属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [Padding](ts-types.md#padding) | 是 | 设置外边距属性。  参数为Length类型时，四个方向外边距同时生效。  默认值：0  单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### backgroundColor

PhonePC/2in1TabletTV

backgroundColor(value: ResourceColor): ButtonConfig

设置FunctionalButton的背景色属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置组件的背景色。  默认值：#ff007dff |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### backgroundImage

PhonePC/2in1TabletTV

backgroundImage(src: ResourceStr, repeat?: ImageRepeat): ButtonConfig

设置FunctionalButton的背景图像属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | 是 | 图片地址，支持网络图片资源和本地图片资源地址，不支持svg类型的图片。 |
| repeat | [ImageRepeat](ts-appendix-enums.md#imagerepeat) | 否 | 设置背景图的重复样式，默认不重复。当设置的背景图片为透明底色图片，且同时设置了backgroundColor时，二者叠加显示，背景颜色在最底部。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### backgroundImageSize

PhonePC/2in1TabletTV

backgroundImageSize(value: SizeOptions | ImageSize): ButtonConfig

设置FunctionalButton的背景图像的高度和宽度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | [ImageSize](ts-appendix-enums.md#imagesize) | 是 | 设置背景图像的高度和宽度。当输入为{width: Length, height: Length}对象时，如果只设置一个属性，则第二个属性保持图片原始宽高比进行调整。默认保持原图的比例不变。  width和height取值范围： [0, +∞)  默认值：ImageSize.Auto  **说明：**    设置为小于0的值时，按值为0显示。当设置了height未设置width时，width根据图片原始宽高比进行调整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### backgroundImagePosition

PhonePC/2in1TabletTV

backgroundImagePosition(value: Position | Alignment): ButtonConfig

设置FunctionalButton的背景图像的显示位置属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | [Alignment](ts-appendix-enums.md#alignment) | 是 | 设置背景图像在组件中显示位置，即相对于组件左上角的坐标，单位vp。  默认值：  {  x: 0,  y: 0  }  x和y值设置百分比时，偏移量是相对组件自身宽高计算的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### opacity

PhonePC/2in1TabletTV

opacity(value: number | Resource): ButtonConfig

设置FunctionalButton的透明度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 元素的不透明度，取值范围为0到1，默认值：1，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位。  **说明：**    子组件可以继承父组件的此属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### border

PhonePC/2in1TabletTV

border(value: BorderOptions): ButtonConfig

统一设置FunctionalButton的边框宽度、边框颜色、边框圆角半径、边框样式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderOptions](ts-types.md#borderoptions) | 是 | 统一边框样式设置接口。  - width：设置边框宽度。  - color：设置边框颜色。  - radius：设置边框圆角半径。  - style：设置边框样式。  **说明：**    边框宽度默认值为0，即不显示边框。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### borderStyle

PhonePC/2in1TabletTV

borderStyle(value: BorderStyle | EdgeStyles): ButtonConfig

设置FunctionalButton的边框样式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 是 | 设置元素的边框样式。  默认值：BorderStyle.Solid |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### borderWidth

PhonePC/2in1TabletTV

borderWidth(value: Length | EdgeWidths): ButtonConfig

设置FunctionalButton的边框宽度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [EdgeWidths](ts-types.md#edgewidths9) | 是 | 设置元素的边框宽度，不支持百分比。  默认值：1，单位：vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### borderColor

PhonePC/2in1TabletTV

borderColor(value: ResourceColor | EdgeColors): ButtonConfig

设置FunctionalButton的边框颜色属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | 是 | 设置元素的边框颜色。  默认值：#000000 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### borderRadius

PhonePC/2in1TabletTV

borderRadius(value: Length | BorderRadiuses): ButtonConfig

设置FunctionalButton的边框圆角半径属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | 是 | 设置元素的边框圆角半径，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### borderImage

PhonePC/2in1TabletTV

borderImage(value: BorderImageOption): ButtonConfig

设置FunctionalButton的图片边框属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderImageOption](ts-universal-attributes-border-image.md#borderimageoption对象说明) | 是 | 图片边框或者渐变色边框设置接口。  该接口支持在ArkTS卡片中使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### scale

PhonePC/2in1TabletTV

scale(value: ScaleOptions): ButtonConfig

设置FunctionalButton的缩放属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 是 | 可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1.0，同时可以通过centerX和centerY设置缩放的中心点。  默认值：  {  x: 1.0,  y: 1.0,  z: 1.0,  centerX:'0.5',  centerY:'0.5'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### align

PhonePC/2in1TabletTV

align(value: Alignment): ButtonConfig

设置FunctionalButton的对齐方式属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Alignment](ts-appendix-enums.md#alignment) | 是 | 设置元素内容的对齐方式，只有当设置的width和height大小超过元素本身内容大小时生效。  默认值：Alignment.Center |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### markAnchor

PhonePC/2in1TabletTV

markAnchor(value: Position): ButtonConfig

设置FunctionalButton在位置定位时的锚点。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | 是 | 设置元素在位置定位时的锚点，以元素顶部起点作为基准点进行偏移，单位vp。  默认值：  {  x: 0,  y: 1  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### offset

PhonePC/2in1TabletTV

offset(value: Position): ButtonConfig

设置FunctionalButton在位置坐标偏移量。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | 是 | 设置元素在位置定位时的锚点，以元素顶部起点作为基准点进行偏移，单位vp。  默认值：  {  x: 0,  y: 1  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### enabled

PhonePC/2in1TabletTV

enabled(value: boolean): ButtonConfig

设置FunctionalButton的是否禁用属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 值为true表示组件可交互，响应点击等操作。  值为false表示组件不可交互，不响应点击等操作。  默认值：true |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### loadingColor

PhonePC/2in1TabletTV

loadingColor(value: ResourceColor): ButtonConfig

设置FunctionalButton中的LoadingProgress图标的颜色属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置图标颜色。默认值：#FFFFFF  **说明：**    设置为异常值时，按值为'#ff666666'显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### loadingWidth

PhonePC/2in1TabletTV

loadingWidth(value: Length): ButtonConfig

设置FunctionalButton中的LoadingProgress图标的宽度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置图标自身的宽度。默认值：20，单位：vp。  取值范围：(-∞, +∞)  填写为负数时，宽度不超过按钮大小；填写正数时，宽度不受限于按钮大小，请合理填写数值。  **说明：**    [LoadingProgress](ts-basic-components-loadingprogress.md)图标始终保持正方形，在显示时边长会取loadingWidth和[loadingHeight](scenario-fusion-functionalbuttoncomponentmanager.md#loadingheight)中的最小值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### loadingHeight

PhonePC/2in1TabletTV

loadingHeight(value: Length): ButtonConfig

设置FunctionalButton中的LoadingProgress图标的高度属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置图标自身的高度。默认值：20，单位：vp。  取值范围：(-∞, +∞)  填写为负数时，高度不超过按钮大小。填写正数时，高度不受限于按钮大小，请合理填写数值。  **说明：**    [LoadingProgress](ts-basic-components-loadingprogress.md)图标始终保持正方形，在显示时边长会取[loadingWidth](scenario-fusion-functionalbuttoncomponentmanager.md#loadingwidth)和loadingHeight中的最小值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### loadingPadding

PhonePC/2in1TabletTV

loadingPadding(value: Length | Padding): ButtonConfig

设置FunctionalButton中的LoadingProgress图标的内边距属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [Padding](ts-types.md#padding) | 是 | 设置图标内边距属性。单位：vp。  默认值：0  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

### loadingMargin

PhonePC/2in1TabletTV

loadingMargin(value: Length | Padding): ButtonConfig

设置FunctionalButton中的LoadingProgress图标的外边距属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [Padding](ts-types.md#padding) | 是 | 设置图标外边距属性。单位：vp。  默认值：{left: -2, right: 2}  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonConfig](scenario-fusion-functionalbuttoncomponentmanager.md#buttonconfig) | ButtonConfig对象。 |

## 示例

PhonePC/2in1TabletTV

### 示例一（场景化Button使用自定义Modifier设置按钮样式）

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { ButtonModifier, LoadingProgressModifier, TextModifier } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Column() {
11. // 构建FunctionalButton组件实例。
12. FunctionalButton({
13. params: {
14. // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
15. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
16. label: '快速验证手机号',
17. // 调整按钮样式。
18. styleOption: {
19. loading: true,
20. },
21. textModifier: new TextModifier().fontColor(Color.Pink),
22. buttonModifier: new ButtonModifier().backgroundColor(Color.Green),
23. loadingProgressModifier: new LoadingProgressModifier().width(20).height(20),
24. },
25. // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
26. controller: new functionalButtonComponentManager.FunctionalButtonController()
27. .onGetPhoneNumber((err, data) => {
28. if (err) {
29. // 错误日志处理。
30. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
31. return;
32. }
33. // 成功日志处理。
34. hilog.info(0x0000, "testTag", "succeeded in authenticating");
35. // 处理授权码。
36. let authorizationCode = data.code;
37. })
38. })
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/hd8t7esFTLSnpd_9-rmpKg/zh-cn_image_0000002583480911.png?HW-CC-KV=V1&HW-CC-Date=20260428T001837Z&HW-CC-Expire=86400&HW-CC-Sign=2DF84D8A6ED6BDA3267A263370179A2F8696A70B79112D69A1A9DD7B231AA7DA)
