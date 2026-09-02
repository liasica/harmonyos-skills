---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-intimate
title: "@hms.core.account.intimate (华为账号亲密圈)"
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > @hms.core.account.intimate (华为账号亲密圈)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:12b0f852c30252905554eec10f92c98b6aa7d93e82afbf1ec7b45ec2a76e8149
---

## 模块概述

@hms.core.account.intimate模块提供拉起亲密圈成员选择器的能力。用户可在成员选择器中添加、关联亲友。开发者可获取用户选择亲友的华为账号用户标识UnionID和OpenID值、匿名化账号、昵称、头像信息。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { intimate } from '@kit.AccountKit';
```

## IdType

华为账号用户标识类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Intimate

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OPEN\_ID | 1 | 华为账号用户的OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| UNION\_ID | 2 | 华为账号用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

## IntimatesSelectionRequest

拉起亲密圈成员选择器请求，开发者可将该对象作为入参。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Intimate

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxSelectionCount | number | 否 | 是 | 可选择亲友的最大数量。该值必须为[1,5]范围内的整数。默认值：1。若值为1，则表示仅可选择一个亲友。 |
| onlySelectIntimateWithHuaweiID | boolean | 否 | 是 | 是否获取仅有华为账号的亲友。默认值：true。  当为true时亲友列表中有华为账号的亲友会显示华为账号标签，没有华为账号的亲友也会在列表中展示，但选择时会引导绑定华为账号。返回数据包含OpenID、UnionID、华为账号的匿名账号、亲友昵称和头像。添加亲友时只能通过华为账号添加。  当为false时亲友都不会显示华为账号标签，返回数据仅包含亲友昵称和头像。添加亲友时可选择通讯录添加、华为账号添加和手动添加三种方式。 |
| idType | [IdType](account-intimate.md#idtype) | 否 | 否 | 华为账号用户标识类型。仅支持设置：IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 华为账号用户标识UnionID或OpenID值。传入值的类型由idType定义，不能为空。  UnionID、OpenID值可以通过[华为账号登录](account-api-authentication.md#登录华为账号)、[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)、[华为账号Panel登录组件](account-api-loginpanel.md#loginpanel)或[华为账号Button登录组件](account-api-huawei-id-button.md#loginwithhuaweiidbutton)获取。 |

## IntimatesSelectionResponse

拉起亲密圈成员选择器请求响应。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Intimate

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| openID | string | 否 | 是 | 亲友的华为账号在应用/元服务的唯一标识。同一个用户在不同应用下，其OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：当请求参数[IntimatesSelectionRequest](account-intimate.md#intimatesselectionrequest)的属性onlySelectIntimateWithHuaweiID设置为false时不返回此属性，设置为true时返回此属性。 |
| unionID | string | 否 | 是 | 亲友的华为账号用户在同一个开发者账号下的唯一标识。同一个用户在同一个开发者账号下的所有应用，其UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：当请求参数[IntimatesSelectionRequest](account-intimate.md#intimatesselectionrequest)的属性onlySelectIntimateWithHuaweiID设置为false时不返回此属性，设置为true时返回此属性。 |
| anonymousAccount | string | 否 | 是 | 匿名化账号。根据用户添加亲友时输入的华为账号，返回匿名化处理后的账号。  **返回场景**：当请求参数[IntimatesSelectionRequest](account-intimate.md#intimatesselectionrequest)的属性onlySelectIntimateWithHuaweiID设置为false时不返回此属性，设置为true时返回此属性。 |
| avatarUri | string | 否 | 否 | 亲友头像链接，当亲友更新头像后，原链接会立即失效。为确保头像正常显示，建议先将头像下载保存后再使用，避免因用户头像链接失效而影响业务流程。  格式例如：https://xxx/xxx。 |
| nickname | string | 否 | 否 | 亲友昵称。长度限制[1,256]个字符。 |

## IntimateErrorCode

拉起亲密圈成员选择器接口错误码枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Intimate

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCOUNT\_NOT\_LOGGED\_IN | 1026900001 | 用户未登录华为账号。 |
| INTERNAL\_ERROR | 1026900003 | 内部错误。 |
| SERVER\_ERROR | 1026900004 | 服务器错误。 |
| NETWORK\_ERROR | 1026900005 | 网络错误。 |
| PARAMETER\_ERROR | 1026900006 | 参数错误。 |
| UNSUPPORTED\_REGION | 1026900007 | 不支持的国家或地区。 |
| USER\_CANCELED | 1026900008 | 用户取消操作。 |
| PERMISSION\_CHECK\_ERROR | 1026900009 | 应用没有权限。 |

## selectIntimates

selectIntimates(context: common.Context, request: IntimatesSelectionRequest): Promise<IntimatesSelectionResponse[]>

拉起亲密圈成员选择器方法，实现用户添加和选择亲友的能力。使用Promise异步回调返回用户选择的亲友信息。如果从未使用亲密圈会引导用户添加亲友。当用户选择亲友点击完成会返回选择的亲友信息。其他场景如用户点击关闭则会抛出错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Intimate

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)、[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。 |
| request | [IntimatesSelectionRequest](account-intimate.md#intimatesselectionrequest) | 是 | 拉起亲密圈成员选择器请求对象。包含可选择亲友的最大数量、是否获取仅有华为账号的亲友、华为账号用户标识类型、 华为账号用户标识UnionID或OpenID值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[IntimatesSelectionResponse[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-intimate#intimatesselectionresponse)> | Promise对象，返回[IntimatesSelectionResponse](account-intimate.md#intimatesselectionresponse)对象数组。包含选择亲友的华为账号用户标识UnionID和OpenID值、匿名化账号、头像、昵称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported because device not support intimate feature. |
| [1026900001](errorcode-account-kit.md#section1026900001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1026900003](errorcode-account-kit.md#section1026900003-内部错误) | Internal error, possibly an IPC failure. |
| [1026900004](errorcode-account-kit.md#section1026900004-服务器错误) | Server error. |
| [1026900005](errorcode-account-kit.md#section1026900005-网络错误) | Network error. |
| [1026900006](errorcode-account-kit.md#section1026900006-参数错误) | Parameter check failed. |
| [1026900007](errorcode-account-kit.md#section1026900007-不支持的国家或地区) | Unsupported country/region. |
| [1026900008](errorcode-account-kit.md#section1026900008-用户取消操作) | The user canceled the current operation. |
| [1026900009](errorcode-account-kit.md#section1026900009-应用没有权限) | The app does not have the required permissions. |

**示例：**

```typescript
import { intimate } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
let request: intimate.IntimatesSelectionRequest = {
  'maxSelectionCount': 1,
  'onlySelectIntimateWithHuaweiID': true,
  'idType': intimate.IdType.OPEN_ID,
  'idValue': '<可通过华为账号登录接口获取>' // 该值可以通过华为账号登录接口获取
};
try {
  // 执行拉起亲密圈成员选择器请求
  intimate.selectIntimates(this.getUIContext().getHostContext(), request)
    .then((data: intimate.IntimatesSelectionResponse[]) => {
      // 开发者处理获取的亲友信息
      hilog.info(0x000, 'test selectIntimates', 'select intimate info success, %{public}s',
        JSON.stringify(data));
    })
    .catch((err: BusinessError) => {
      hilog.error(0x000, 'test selectIntimates',
        `select intimate info failed. Code: ${err.code}, message: ${err.message}`);
    });
} catch (error) {
  hilog.error(0x000, 'test selectIntimates',
    `select intimate info failed. Code: ${error.code}, message: ${error.message}`);
}
```
