---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-component-manager
title: loginComponentManager (华为账号登录组件管理)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS组件 > loginComponentManager (华为账号登录组件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6190152999efcaa528d1ed49a6e22a6b2c47fea40c8fb5db06507f5e466c81f
---

本模块提供华为账号登录组件的逻辑管理，辅助应用通过集成华为账号登录组件完成登录功能。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { loginComponentManager } from '@kit.AccountKit';
```

## LoginType

PhonePC/2in1TabletTV

该枚举定义了华为账号登录类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ID | 0 | 表示用OpenID、UnionID来关联华为账号。  用户在登录成功后会返回对应数据。  该登录类型响应数据包含openID、unionID、authorizationCode、idToken字段。 |
| PHONE\_NUMBER | 1 | 表示用PhoneNumber来关联华为账号。  用户在登录成功后，如之前未对快速验证手机号进行授权，则会拉起手机号授权页面；如已授权，则返回对应数据。  该登录类型不需要实时验证华为账号的手机号码，响应数据包含openID、unionID、authorizationCode、idToken字段。  应用使用Authorization Code调用[获取用户级凭证接口](account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token，再使用Access Token调用[获取华为账号用户信息接口](account-api-get-user-info-get-phone.md#接口原型)获取用户信息，从用户信息中获取用户手机号。 |
| REAL\_TIME\_PHONE\_NUMBER | 2 | 表示用PhoneNumber来关联华为账号。  用户每次在登录成功后，都会拉起实时验证手机号授权页面。  该登录类型会实时验证华为账号的手机号码，响应数据包含openID、unionID、authorizationCode、idToken字段。  应用使用Authorization Code调用[获取用户级凭证接口](account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token，再使用Access Token调用[获取华为账号用户信息接口](account-api-get-user-info-get-phone.md#接口原型)获取用户信息，从用户信息中获取用户手机号。  **说明：** REAL\_TIME\_PHONE\_NUMBER暂不支持使用。 |
| QUICK\_LOGIN | 3 | 表示用PhoneNumber来关联华为账号。  该类型不支持Icon类型和图文类型的LoginWithHuaweiIDButton组件。  该登录类型需要通过[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口获取华为账号绑定的匿名手机号，如果未获取到华为账号绑定的匿名手机号，请使用其他登录类型。  该登录类型响应数据包含openID、unionID、authorizationCode、idToken字段。  应用使用Authorization Code调用[/oauth2/v6/quickLogin/getPhoneNumber接口](account-api-get-user-info-quicklogin-by-code.md#接口原型)获取用户信息，从用户信息中获取用户手机号。  **起始版本：** 5.0.0(12)  **设备行为差异：** 该接口在Phone、PC/2in1、Tablet、TV中可正常调用（TV设备从5.1.1(19)版本开始支持），在其他设备类型中返回1001500003错误码。 |

## AppInfo

PhonePC/2in1TabletTV

该接口定义了用于显示登录面板的应用信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIcon | [PixelMap](arkts-apis-image-pixelmap.md) | [ResourceStr](ts-types.md#resourcestr) | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 否 | 应用的图标。 |
| appName | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 应用的名称，长度限制1-19个字符，字符超长和大字体下展示不全会截断，使用省略号填充。 |
| appDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 应用的详细描述，长度限制1-44个字符。  **说明：**  - 在4.1.0(11)版本，为必填参数。  - 从5.0.0(12)版本开始，为非必填参数。仅当登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时不需要设置该值。 |

## TextType

PhonePC/2in1TabletTV

该枚举定义了显示在登录面板上的隐私文本类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAIN\_TEXT | 0 | 纯文本类型不支持点击。 |
| RICH\_TEXT | 1 | 富文本类型展示为蓝色，支持点击。用于展示《华为账号用户认证协议》和应用相关隐私协议。 |

## PrivacyText

PhonePC/2in1TabletTV

该接口定义了使用登录面板或登录按钮时需要展示的隐私文本。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TextType](account-api-component-manager.md#texttype) | 否 | 否 | 隐私文本的类型，包含纯文本和富文本。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 在登录面板上显示的隐私文本内容，一般用于展示应用隐私协议和《华为账号用户认证协议》跳转链接。 |
| tag | string | 否 | 是 | 当type类型为[TextType.RICH\_TEXT](account-api-component-manager.md#texttype)必须设置tag。当用户点击文本时将跳转应用给tag设置的链接，应用可以根据用户的点击行为展示不同的隐私内容。 |

## LoginIcon

PhonePC/2in1TabletTV

该接口定义了可选登录区域展示的登录Icon属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [PixelMap](arkts-apis-image-pixelmap.md) | [ResourceStr](ts-types.md#resourcestr) | [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 否 | 否 | 可选登录区域展示其他登录方式的Icon。根据[视觉规范](../design-guides/id-0000001880001344.md#section61791745172816)，Icon建议为半径18vp的圆形图片。 |
| tag | string | 否 | 是 | 当用户点击Icon时可以将tag对应值回调给应用，应用可以根据用户的点击行为展示其他登录方式页面。 |

## OptionalLoginButtonAttr

PhonePC/2in1TabletTV

该接口定义了可选登录按钮的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 可选登录按钮的文字描述。 |

## OptionalLoginAreaAttr

PhonePC/2in1TabletTV

该接口定义了可选登录区域的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconArray | [LoginIcon](account-api-component-manager.md#loginicon)[] | 否 | 否 | 可选登录区域会展示应用传入的其他登录方式的Icon，最多支持展示5个Icon。 |

## LoginPanelParams

PhonePC/2in1TabletTV

该接口定义了显示在登录面板上的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appInfo | [AppInfo](account-api-component-manager.md#appinfo) | 否 | 否 | 组件展示应用信息。 |
| privacyText | [PrivacyText](account-api-component-manager.md#privacytext)[] | 否 | 是 | 组件展示隐私文本内容。 |
| optionalLoginButtonAttr | [OptionalLoginButtonAttr](account-api-component-manager.md#optionalloginbuttonattr) | 否 | 是 | 组件展示可选登录按钮。 |
| loginType | [LoginType](account-api-component-manager.md#logintype) | 否 | 是 | 华为账号登录类型。默认值：[LoginType.ID](account-api-component-manager.md#logintype)。  一键登录请使用[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)。 |
| anonymousPhoneNumber | string | 否 | 是 | 华为账号绑定的匿名手机号。当登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时需要设置该参数。可参考[华为账号一键登录客户端开发](../harmonyos-guides/account-phone-unionid-login.md#客户端开发)获取。  **起始版本：** 5.0.0(12) |
| verifyPhoneNumber | boolean | 否 | 是 | 华为账号用户在过去90天内未进行过短信验证，是否拉起Account Kit提供的短信验证码页面。  true：拉起Account Kit提供的短信验证码页面。  false：不拉起Account Kit提供的短信验证码页面。需要应用验证手机号时效性。  默认值：true。  **起始版本：** 5.0.0(12) |
| optionalLoginAreaAttr | [OptionalLoginAreaAttr](account-api-component-manager.md#optionalloginareaattr) | 否 | 是 | 组件可选登录区域属性。  如果optionalLoginButtonAttr和optionalLoginAreaAttr同时存在，优先展示optionalLoginAreaAttr。  **起始版本：** 5.0.0(12) |
| riskLevel | boolean | 否 | 是 | 是否需要获取华为账号用户风险等级。  仅登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时需要设置该参数。  true：需要[获取用户风险等级](../harmonyos-guides/account-get-risklevel-byquicklogin.md)。  false：不获取用户风险等级。  默认值：false。  **起始版本：** 5.1.0(18) |
| securityVerification | boolean | 否 | 是 | 用户开启华为账号一键登录增强身份验证后，应用会在登录过程中通过华为账号使用生物识别或短信进行身份验证。如果需要获取用户一键登录增强身份验证的开关状态，需设置该字段为false。  仅登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时需要设置该参数。  true：响应结果HuaweiIDCredential将不会返回 [enableSecurityVerification](account-api-component-manager.md#huaweiidcredential)。  false：响应结果HuaweiIDCredential将返回 [enableSecurityVerification](account-api-component-manager.md#huaweiidcredential)。  默认值：true。  **起始版本：** 6.0.0(20) |

## ClickEvent

PhonePC/2in1TabletTV

该枚举定义了用户点击华为账号登录按钮事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUAWEI\_ID\_LOGIN\_BUTTON | 0 | 点击华为账号登录按钮。 |

## AgreementStatus

PhonePC/2in1TabletTV

该枚举定义了用户是否同意通过[TextType.RICH\_TEXT](account-api-component-manager.md#texttype)设置的协议的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_ACCEPTED | 0 | 用户未同意协议。 |
| ACCEPTED | 1 | 用户已同意协议。 |

## HuaweiIDCredential

PhonePC/2in1TabletTV

定义使用华为账号登录成功响应结果。用于获取用户相关信息和关联华为账号。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| unionID | string | 是 | 否 | UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| openID | string | 是 | 否 | OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| authorizationCode | string | 是 | 否 | Authorization Code。临时凭据，用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。 |
| idToken | string | 是 | 是 | ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。 |
| enableSecurityVerification | boolean | 是 | 是 | enableSecurityVerification。华为账号用户是否开启一键登录增强身份验证。如果开发者需要获取该字段，请将参数[securityVerification](account-api-component-manager.md#loginwithhuaweiidbuttonparams)设置为false。  仅登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时会返回该字段。  true：表示用户已启用增强身份验证。  false：表示用户未启用增强身份验证。  **起始版本：** 6.0.0(20) |

## 事件

PhonePC/2in1TabletTV

不支持通用事件，仅支持以下事件：

## LoginPanelController

PhonePC/2in1TabletTV

[LoginPanel](account-api-loginpanel.md)组件控制器，用来注册组件内部的点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

### onClickLoginWithHuaweiIDButton

PhonePC/2in1TabletTV

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginPanelController

注册华为账号一键登录结果事件。使用callback异步回调。可在回调方法中处理登录响应结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[HuaweiIDCredential](account-api-component-manager.md#huaweiidcredential)> | 是 | 回调函数。当注册华为账号登录返回结果成功，err为undefined，data为获取到的[HuaweiIDCredential](account-api-component-manager.md#huaweiidcredential)对象；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)和[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001500002](account-api-error-code.md#section1001500002-重复请求) | This error code is reported when a request is already being processed. |
| [1001500003](account-api-error-code.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported. |
| [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](account-api-error-code.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | Invalid input parameter value. |
| [1001502005](account-api-error-code.md#section1001502005-网络错误) | Network error. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | The user canceled the authorization. |
| [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1005300001](account-api-error-code.md#section1005300001-用户未同意协议) | The user did not accept the agreement. |

### onClickOptionalLoginButton

PhonePC/2in1TabletTV

onClickOptionalLoginButton(callback: AsyncCallback<void>): LoginPanelController

注册可选登录按钮的点击事件。使用callback异步回调。用于应用跳转其他登录方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当用户点击可选登录按钮操作成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickOptionalLoginIcon

PhonePC/2in1TabletTV

onClickOptionalLoginIcon(callback: AsyncCallback<string>): LoginPanelController

注册可选登录Icon的点击事件。使用callback异步回调。用于应用跳转其他登录方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当用户点击[LoginIcon](account-api-component-manager.md#loginicon)操作成功，err为undefined，data为获取到的[LoginIcon](account-api-component-manager.md#loginicon)的tag；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickPrivacyText

PhonePC/2in1TabletTV

onClickPrivacyText(callback: AsyncCallback<string>): LoginPanelController

注册隐私内容为富文本的点击事件。使用callback异步回调。应用可以让用户点击跳转到应用的隐私协议。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当注册隐私内容为富文本的点击操作成功时，err为undefined，data为获取到的[PrivacyText](account-api-component-manager.md#privacytext)的tag；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onChangeAgreementStatus

PhonePC/2in1TabletTV

onChangeAgreementStatus(callback: AsyncCallback<AgreementStatus>): LoginPanelController

注册用户协议状态变化的事件。使用callback异步回调。当用户同意或者取消同意协议成功时，通过[setAgreementStatus](account-api-component-manager.md#setagreementstatus-1)设置用户同意或取消同意的协议状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[AgreementStatus](account-api-component-manager.md#agreementstatus)> | 是 | 回调函数。当用户同意或者取消同意协议成功，err为undefined，data为获取到的[AgreementStatus](account-api-component-manager.md#agreementstatus)；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### setAgreementStatus

PhonePC/2in1TabletTV

setAgreementStatus(agreementStatus: AgreementStatus): LoginPanelController

设置用户协议的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agreementStatus | [AgreementStatus](account-api-component-manager.md#agreementstatus) | 是 | 开发者如果使用自定义协议页面，需要先设置agreementStatus为NOT\_ACCEPTED，当用户同意协议后设置为ACCEPTED。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### setShowAgreementForOptionalLogin

PhonePC/2in1TabletTV

setShowAgreementForOptionalLogin(): LoginPanelController

设置用户点击其他方式登录选项时展示隐私协议弹框。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickEvent

PhonePC/2in1TabletTV

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginPanelController

注册华为账号登录按钮的点击事件。使用callback异步回调。应用可以在用户点击华为账号登录按钮后收到回调，可用于记录运营事件等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ClickEvent](account-api-component-manager.md#clickevent)> | 是 | 回调函数。当用户点击华为账号登录按钮时，err为undefined，data为获取到的[ClickEvent](account-api-component-manager.md#clickevent)；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickCloseButton

PhonePC/2in1TabletTV

onClickCloseButton(callback: AsyncCallback<void>): LoginPanelController

注册关闭按钮的点击事件或用户侧滑返回事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当注册关闭按钮的点击操作或侧滑返回成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginPanelController](account-api-component-manager.md#loginpanelcontroller) | [LoginPanel](account-api-loginpanel.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

**示例：**

```
1. import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct PreviewLoginPanelPage {
8. // 是否展示LoginPanel组件
9. @State show: boolean = true;
10. // 定义LoginPanel展示的隐私文本
11. privacyText: loginComponentManager.PrivacyText[] = [{
12. text: '已阅读并同意',
13. type: loginComponentManager.TextType.PLAIN_TEXT
14. }, {
15. text: '《用户服务协议》',
16. tag: '用户服务协议',
17. type: loginComponentManager.TextType.RICH_TEXT
18. }, {
19. text: '《隐私协议》',
20. tag: '隐私协议',
21. type: loginComponentManager.TextType.RICH_TEXT
22. }, {
23. text: '和',
24. type: loginComponentManager.TextType.PLAIN_TEXT
25. }, {
26. text: '《华为账号用户认证协议》',
27. tag: '华为账号用户认证协议',
28. type: loginComponentManager.TextType.RICH_TEXT
29. }];
30. // 定义LoginPanel展示的其他方式登录Icon
31. iconArray: loginComponentManager.LoginIcon[] = [{
32. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
33. icon: $r('app.media.app_icon'),
34. tag: '其他方式登录'
35. }];
36. // 构造LoginPanel组件的控制器
37. controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
38. // 当登录类型不是QUICK_LOGIN且未设置协议时，如果需要展示自定义协议弹框，需要设置协议状态为NOT_ACCEPTED
39. .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
40. // 用户点击其他方式登录展示隐私协议弹框
41. .setShowAgreementForOptionalLogin()
42. .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
43. hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
44. if (error) {
45. this.dealAllError(error);
46. return;
47. }
48. if (response) {
49. // 获取到Authorization Code后，传给应用服务端
50. const authorizationCode = response.authorizationCode;
51. hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
52. this.show = false;
53. return;
54. }
55. })
56. .onClickOptionalLoginButton(() => {
57. hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
58. this.show = false;
59. })
60. .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
61. if (error) {
62. this.dealAllError(error);
63. return;
64. }
65. hilog.info(0x0000, 'testTag', `onClickOptionalLoginIcon tag: ${tag}`);
66. this.show = false;
67. })
68. .onClickPrivacyText((error: BusinessError, tag: string) => {
69. if (error) {
70. this.dealAllError(error);
71. return;
72. }
73. // 应用需要实现协议页面的跳转逻辑
74. hilog.info(0x0000, 'testTag', `onClickPrivacyText tag: ${tag}`);
75. })
76. .onClickCloseButton(() => {
77. hilog.info(0x0000, 'testTag', 'onClickCloseButton.');
78. this.show = false;
79. })
80. .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
81. if (error) {
82. this.dealAllError(error);
83. return;
84. }
85. hilog.info(0x0000, 'testTag', `onChangeAgreementStatus agreementStatus: ${agreementStatus}`);
86. })
87. .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
88. if (error) {
89. this.dealAllError(error);
90. return;
91. }
92. hilog.info(0x0000, 'testTag', `onClickEvent clickEvent: ${clickEvent}`);
93. });

95. // 错误处理
96. dealAllError(error: BusinessError): void {
97. hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
98. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
99. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
100. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
101. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
102. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
103. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
104. // 登录失败，请尝试使用其他方式登录
105. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
106. // 用户取消授权
107. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
108. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
109. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
110. // 重复请求，应用无需处理
111. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
112. // 用户未同意协议
113. } else {
114. // 应用登录失败，请尝试使用其他方式登录
115. }
116. }

118. build() {
119. if (this.show) {
120. Stack() {
121. LoginPanel({
122. show: this.show,
123. params: {
124. appInfo: {
125. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
126. appIcon: $r('app.media.app_icon'),
127. appName: '应用名称',
128. },
129. privacyText: this.privacyText,
130. // 参考华为账号开发指南获取匿名手机号
131. anonymousPhoneNumber: '139******99',
132. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
133. // optionalLoginAreaAttr和optionalLoginButtonAttr同时存在时优先展示optionalLoginAreaAttr
134. optionalLoginAreaAttr: { iconArray: this.iconArray },
135. optionalLoginButtonAttr: { text: '其他方式登录' }
136. },
137. controller: this.controller
138. })
139. }
140. .height('100%')
141. .width('100%')
142. }
143. }
144. }

146. export enum ErrorCode {
147. // 账号未登录
148. ERROR_CODE_LOGIN_OUT = 1001502001,
149. // 网络错误
150. ERROR_CODE_NETWORK_ERROR = 1001502005,
151. // 内部错误
152. ERROR_CODE_INTERNAL_ERROR = 1001502009,
153. // 用户取消授权
154. ERROR_CODE_USER_CANCEL = 1001502012,
155. // 系统服务异常
156. ERROR_CODE_SYSTEM_SERVICE = 12300001,
157. // 用户未同意用户协议
158. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
159. // 重复请求
160. ERROR_CODE_REQUEST_REFUSE = 1001500002
161. }
```

## LoginWithHuaweiIDButtonParams

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮的属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [Style](account-api-component-manager.md#style) | 否 | 否 | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件的样式。 |
| borderRadius | number | 否 | 是 | 按钮边框圆角半径。  取值范围：[0,+∞)，值小于0时，按0处理。  默认值：height属性取值的一半。  单位：vp。 |
| iconRadius | number | 否 | 是 | Icon类型按钮的半径。  取值范围：[0,+∞)，值小于0时，按0处理。  默认值：24。  单位：vp。 |
| supportDarkMode | boolean | 否 | 是 | 表示按钮的样式是否随系统深浅色模式变化。  true：按钮的样式会随着系统深浅色模式变化。  false：按钮的样式不会随着系统深浅色模式变化。  默认值：true。 |
| loginType | [LoginType](account-api-component-manager.md#logintype) | 否 | 是 | 华为账号登录类型。默认值：[LoginType.ID](account-api-component-manager.md#logintype)。  一键登录请使用[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)。 |
| textAndIconStyle | boolean | 否 | 是 | 是否展示图文混合样式的华为账号登录按钮。  true：按钮支持Icon和文字混合样式。  false：按钮仅支持文本样式。  默认值：false。  当loginType不等于[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)且style等于[BUTTON\_RED](account-api-component-manager.md#style)、[BUTTON\_WHITE](account-api-component-manager.md#style)、[BUTTON\_WHITE\_OUTLINE](account-api-component-manager.md#style)、[BUTTON\_BLACK](account-api-component-manager.md#style)、[BUTTON\_GRAY](account-api-component-manager.md#style)时该参数生效。  **起始版本：** 5.0.0(12) |
| customButtonParams | [CustomButtonParams](account-api-component-manager.md#custombuttonparams) | 否 | 是 | [BUTTON\_CUSTOM](account-api-component-manager.md#style)按钮样式参数。  **起始版本：** 5.0.0(12) |
| verifyPhoneNumber | boolean | 否 | 是 | 华为账号用户在过去90天内未进行短信验证，是否拉起Account Kit提供的短信验证码页面。  true：拉起Account Kit提供的短信验证码页面。  false：不拉起Account Kit提供的短信验证码页面。需要应用验证手机号时效性。  默认值：true。  **起始版本：** 5.0.0(12) |
| extraStyle | [ExtraStyle](account-api-component-manager.md#extrastyle) | 否 | 是 | 如果应用想使用华为账号提供的固定样式之外的效果，可使用此接口自定义按钮样式。  **起始版本：** 5.0.0(12) |
| loginButtonTextType | [LoginButtonTextType](account-api-component-manager.md#loginbuttontexttype) | 否 | 是 | 当loginType为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时，可传入此参数，控制按钮文本内容显示。  默认值：[LoginButtonTextType.QUICK\_LOGIN](account-api-component-manager.md#loginbuttontexttype)  - 当该参数为[LoginButtonTextType.QUICK\_LOGIN](account-api-component-manager.md#loginbuttontexttype)时，按钮文本内容显示“华为账号一键登录”。  - 当该参数为[LoginButtonTextType.QUICK\_REGISTRATION](account-api-component-manager.md#loginbuttontexttype)时，按钮文本内容显示“华为账号一键注册”。  **起始版本：** 5.0.0(12) |
| riskLevel | boolean | 否 | 是 | 是否需要获取华为账号用户风险等级。  仅登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时需要设置该参数。  true：需要[获取用户风险等级](../harmonyos-guides/account-get-risklevel-byquicklogin.md)。  false：不获取用户风险等级。  默认值：false。  **起始版本：** 5.1.0(18) |
| securityVerification | boolean | 否 | 是 | 用户开启华为账号一键登录增强身份验证后，应用会在登录过程中通过华为账号使用生物识别或短信进行身份验证。如果需要获取用户一键登录增强身份验证的开关状态，需设置该字段为false。  仅登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时需要设置该参数。  true：响应结果HuaweiIDCredential将不会返回 [enableSecurityVerification](account-api-component-manager.md#huaweiidcredential)。  false：响应结果HuaweiIDCredential将返回 [enableSecurityVerification](account-api-component-manager.md#huaweiidcredential)。  默认值：true。  **起始版本：** 6.0.0(20) |

## Style

PhonePC/2in1TabletTV

该枚举表示华为账号登录按钮的类型。

如果以下华为账号登录按钮的样式仍不能满足开发需求，请参见[华为账号开放登录设计指南](../design-guides/id-0000001880001344.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BUTTON\_RED | 0 | 红色背景白色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| BUTTON\_WHITE | 1 | 白色背景黑色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| BUTTON\_WHITE\_OUTLINE | 2 | 白色背景黑色文字带边框按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| BUTTON\_BLACK | 3 | 黑色背景白色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| ICON\_RED | 4 | 红色背景白色Icon按钮。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| ICON\_WHITE | 5 | 白色背景红色Icon按钮。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| ICON\_WHITE\_OUTLINE | 6 | 白色背景红色Icon带边框按钮。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| ICON\_BLACK | 7 | 黑色背景白色Icon按钮。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。 |
| ICON\_GRAY | 8 | 灰色背景红色Icon按钮。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。  **起始版本：** 5.0.0(12) |
| BUTTON\_GRAY | 9 | 灰色背景黑色文字按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。  **起始版本：** 5.0.0(12) |
| BUTTON\_CUSTOM | 10 | 支持自定义背景颜色、文字颜色及圆角等效果的按钮，字体大小会随着按钮的宽高自适应，最小为9号，最大为16号。开发者可以通过[CustomButtonParams](account-api-component-manager.md#custombuttonparams)设置按钮自定义的参数，且需要自行适配深浅色模式。  根据开发场景从以下链接中选择其中一个规范查看。  请参见[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)视觉规范。  请参见[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)视觉规范。  **起始版本：** 5.0.0(12)  **说明：** 此类型仅支持纯文本按钮。 |

## LoginButtonTextType

PhonePC/2in1TabletTV

该枚举表示华为账号一键登录按钮显示的文本内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QUICK\_LOGIN | 0 | 华为账号一键登录按钮文本内容显示为“华为账号一键登录”。用于应用账号登录场景。 |
| QUICK\_REGISTRATION | 1 | 华为账号一键登录按钮文本内容显示为“华为账号一键注册”。用于应用账号注册场景。 |

## CustomButtonParams

PhonePC/2in1TabletTV

该接口定义了[BUTTON\_CUSTOM](account-api-component-manager.md#style)按钮的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | [FontColor](account-api-component-manager.md#fontcolor) | 否 | 是 | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)按钮文字颜色。  默认值：[FontColor](account-api-component-manager.md#fontcolor).WHITE |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)按钮背景颜色。  默认值：Red |

## FontColor

PhonePC/2in1TabletTV

该枚举定义了[BUTTON\_CUSTOM](account-api-component-manager.md#style)按钮可以使用的文字颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WHITE | 0 | 华为账号登录按钮文字颜色为白色。 |
| BLACK | 1 | 华为账号登录按钮文字颜色为黑色。 |

## ExtraStyle

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮拓展参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttonStyle | [ButtonStyle](account-api-component-manager.md#buttonstyle) | 否 | 是 | 华为账号登录按钮提供给开发者自定义按钮样式，可动态设置一些属性。 |
| customButtonStateStyles | [StateStyles](account-api-component-manager.md#statestyles) | 否 | 是 | 华为账号登录按钮提供给开发者自定义按钮多态样式。仅对[BUTTON\_CUSTOM](account-api-component-manager.md#style)类型按钮生效。 |
| textAndIconButtonParams | [TextAndIconButtonParams](account-api-component-manager.md#textandiconbuttonparams) | 否 | 是 | 图文混合样式按钮下设置该参数可以控制图文间距。 |
| iconButtonParams | [IconButtonParams](account-api-component-manager.md#iconbuttonparams) | 否 | 是 | 纯图标按钮下设置该参数可控制图标按钮内图标的显示半径。 |

## RadialGradient

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮径向渐变的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center | [[Length](ts-types.md#length), [Length](ts-types.md#length)] | 否 | 否 | 径向渐变的中心点，即相对于当前组件左上角的坐标。 |
| radius | number | string | 否 | 否 | 径向渐变的半径。  取值范围：[0,+∞)。  值小于0时，按0处理。 |
| colors | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。  不设置则无效果。 |
| repeating | boolean | 否 | 是 | 为渐变的颜色重复着色。  true：重复着色。  false：不重复着色。  默认值：false。 |

## SweepGradient

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮角度渐变的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center | [[Length](ts-types.md#length), [Length](ts-types.md#length)] | 否 | 否 | 角度渐变的中心点，即相对于当前组件左上角的坐标。 |
| start | number | string | 否 | 是 | 角度渐变的起点。  当start的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。  当start的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。 |
| end | number | string | 否 | 是 | 角度渐变的终点。  当end的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。  当end的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。 |
| rotation | number | string | 否 | 是 | 角度渐变的旋转角度。  当rotation的数据类型为number时，默认值是0，设置为小于0的值时，按值为0处理，设置为大于360的值时，按值为360处理。  当rotation的数据类型为string时，合法的取值为纯数字或纯数字后带"deg"(度)、"rad"(弧度)、"grad"(梯度)、"turn"(圈)单位，例如："90"、 "90deg"、"1.57rad"。 |
| colors | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定某百分比位置处的渐变色颜色，设置非法颜色直接跳过。  不设置则无效果。 |
| repeating | boolean | 否 | 是 | 为渐变的颜色重复着色。  true：重复着色。  false：不重复着色。  默认值：false。 |

## ButtonStyle

PhonePC/2in1TabletTV

该类定义了华为账号登录按钮的通用属性。通过new loginComponentManager.ButtonStyle()构造实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

### buttonSize

PhonePC/2in1TabletTV

buttonSize(value: ButtonSize): ButtonStyle

调用该方法设置华为账号登录按钮的宽高尺寸。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonSize](account-api-component-manager.md#buttonsize-1) | 是 | 当按钮类型为纯图标按钮时，按钮的宽度和高度相等，取value.width和value.height的非undefined的最小值，如果value.width和value.height都为undefined取[LoginWithHuaweiIDButtonParams](account-api-component-manager.md#loginwithhuaweiidbuttonparams)的iconRadius的2倍值，如果iconRadius也是undefined则取默认值48vp；  当按钮类型为非纯图标按钮时，按钮的宽度和高度分别取value.width和value.height，当value.width或者value.height为undefined，按钮宽度或高度取父布局宽高。  **说明：** 当设置该属性的宽高，父组件的宽高值应该大于等于该属性的宽高值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### fontSize

PhonePC/2in1TabletTV

fontSize(value: Length): ButtonStyle

调用该方法设置华为账号登录按钮的字号。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 当按钮为图文按钮或文本按钮时，设置按钮文字的字号。根据[华为账号开放登录视觉规范](../design-guides/id-0000001880001344.md#section61791745172816)，设置范围建议在按钮高度的30%~50%之间。  如果没传此值，字号大小在9~16vp之间随按钮宽度自适应。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### fontColor

PhonePC/2in1TabletTV

fontColor(value: ResourceColor | FontColor): ButtonStyle

调用该方法设置华为账号登录按钮的文字颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [FontColor](account-api-component-manager.md#fontcolor) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮文字颜色。当已经设置[CustomButtonParams](account-api-component-manager.md#custombuttonparams)的fontColor属性时，优先取此参数值。  不设置则为黑色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### fontWeight

PhonePC/2in1TabletTV

fontWeight(value: string | number | FontWeight): ButtonStyle

调用该方法设置华为账号登录按钮的文字字重。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | [FontWeight](ts-appendix-enums.md#fontweight) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮文字字重。number类型取值[100, 900]，取值间隔为100，取值越大字体越粗，当超出边界值时取值为400。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认字重为FontWeight.Medium，对应的number值为500。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### fontFamily

PhonePC/2in1TabletTV

fontFamily(value: ResourceStr): ButtonStyle

调用该方法设置华为账号登录按钮的文字字体。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮文字字体。  默认字体'HarmonyOS Sans'。  应用当前支持'HarmonyOS Sans'字体和[注册自定义字体](js-apis-font.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### backgroundColor

PhonePC/2in1TabletTV

backgroundColor(value: ResourceColor): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景颜色。  当已经设置[CustomButtonParams](account-api-component-manager.md#custombuttonparams)的backgroundColor属性时，优先取此参数值。  不设置则为 Red 红色背景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### backgroundEffect

PhonePC/2in1TabletTV

backgroundEffect(value: BackgroundEffectOptions): ButtonStyle

调用该方法设置华为账号登录按钮的背景属性。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景属性，包括饱和度，亮度，颜色。  不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### backgroundBrightness

PhonePC/2in1TabletTV

backgroundBrightness(value: BackgroundBrightnessOptions): ButtonStyle

调用该方法设置华为账号登录按钮的背景提亮效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BackgroundBrightnessOptions](ts-universal-attributes-background.md#backgroundbrightnessoptions12对象说明) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景提亮效果，包括：亮度变化速率，提亮程度。  不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### linearGradient

PhonePC/2in1TabletTV

linearGradient(value: LinearGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色线性渐变效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LinearGradient](ts-universal-attributes-border-image.md#lineargradient) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景颜色线性渐变效果，不设置则无效果。  **说明：**  使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### sweepGradient

PhonePC/2in1TabletTV

sweepGradient(value: SweepGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色角度渐变效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SweepGradient](account-api-component-manager.md#sweepgradient) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景颜色角度渐变效果。  不设置则无效果。  **说明：**  使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### radialGradient

PhonePC/2in1TabletTV

radialGradient(value: RadialGradient): ButtonStyle

调用该方法设置华为账号登录按钮的背景颜色径向渐变效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RadialGradient](account-api-component-manager.md#radialgradient) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮背景颜色径向渐变效果。  不设置则无效果。  **说明：**  使用此属性时，按钮不能有背景色，否则按钮边缘会出现锯齿毛边，需把按钮背景色设置为透明色，如backgroundColor(Color.Transparent)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### shadow

PhonePC/2in1TabletTV

shadow(value: ShadowOptions | ShadowStyle): ButtonStyle

调用该方法设置华为账号登录按钮的阴影效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮阴影效果，不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### opacity

PhonePC/2in1TabletTV

opacity(value: number | Resource): ButtonStyle

调用该方法设置华为账号登录按钮的不透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 元素的不透明度，取值范围为0~1，1表示不透明，0表示完全透明, 达到隐藏组件效果，但是在布局中占位。  默认值：1  当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的不透明度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### border

PhonePC/2in1TabletTV

border(value: BorderOptions): ButtonStyle

调用该方法设置华为账号登录按钮的边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderOptions](ts-types.md#borderoptions) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的边框样式，不设置则无效果。  **说明：** 设置内边框需要预留充足的空间展示按钮，请确保按钮父组件宽高大于按钮本身。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### borderImage

PhonePC/2in1TabletTV

borderImage(value: BorderImageOption): ButtonStyle

调用该方法设置华为账号登录按钮的图片边框样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderImageOption](ts-universal-attributes-border-image.md#borderimageoption对象说明) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的图片边框样式，不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### outline

PhonePC/2in1TabletTV

outline(value: OutlineOptions): ButtonStyle

调用该方法设置华为账号登录按钮的外描边样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [OutlineOptions](ts-types.md#outlineoptions11对象说明) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的外描边样式，不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### hoverEffect

PhonePC/2in1TabletTV

hoverEffect(value: HoverEffect): ButtonStyle

调用该方法设置华为账号登录按钮的悬浮态效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HoverEffect](ts-appendix-enums.md#hovereffect8) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的悬浮态效果，不设置则为默认效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### clickEffect

PhonePC/2in1TabletTV

clickEffect(value: ClickEffect): ButtonStyle

调用该方法设置华为账号登录按钮的点击回弹效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ClickEffect](ts-universal-attributes-click-effect.md#clickeffect对象说明) | 是 | 当按钮类型为[BUTTON\_CUSTOM](account-api-component-manager.md#style)时，此参数可设置按钮的点击回弹效果，不设置则无效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

### loadingStyle

PhonePC/2in1TabletTV

loadingStyle(value: LoadingStyle): ButtonStyle

调用该方法设置华为账号登录按钮在登录过程中是否显示加载态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LoadingStyle](account-api-component-manager.md#loadingstyle-1) | 是 | 此参数可设置按钮在登录过程中是否显示加载态，  默认不显示加载态。  **说明：** 纯图标按钮不支持设置加载态，此参数不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ButtonStyle](account-api-component-manager.md#buttonstyle) | 定义了华为账号登录按钮的通用属性。 |

## ButtonSize

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮的尺寸参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | [Length](ts-types.md#length) | 否 | 是 | 设置华为账号登录按钮宽度。 |
| height | [Length](ts-types.md#length) | 否 | 是 | 设置华为账号登录按钮高度。 |

## LoadingStyle

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮在登录过程中是否展示加载态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| show | boolean | 否 | 是 | 设置华为账号登录按钮在登录过程中是否展示加载态。  true：展示登录按钮加载态  false：不展示登录按钮加载态  默认值：false |

## TextAndIconButtonParams

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮为图文按钮时的图文间距。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textAndIconMargin | number | 否 | 是 | 设置华为账号登录按钮为图文按钮时的图文间距。默认值：8vp，取值范围：4~16vp。当小于4vp时取值为4vp，当大于16vp时取值为16vp。 |

## IconButtonParams

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮为纯图标按钮时的华为图标的半径。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| logoRadius | number | 否 | 是 | 设置华为账号登录按钮为纯图标按钮时的华为图标的半径。  默认值：14vp，最小值：8vp。取值范围：按钮高度的20%~32%。当小于20%时取值为20%，当大于32%时取值为32%。 |

## StateStyles

PhonePC/2in1TabletTV

该接口定义了华为账号登录按钮的多态样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| normal | [ButtonStyle](account-api-component-manager.md#buttonstyle) | 否 | 是 | 登录按钮正常态的通用样式。 |
| pressed | [ButtonStyle](account-api-component-manager.md#buttonstyle) | 否 | 是 | 登录按钮按压态的通用样式。 |
| disabled | [ButtonStyle](account-api-component-manager.md#buttonstyle) | 否 | 是 | 登录按钮不可点击态的通用样式。 |
| focused | [ButtonStyle](account-api-component-manager.md#buttonstyle) | 否 | 是 | 登录按钮聚焦态的通用样式。 |

## LoginWithHuaweiIDButtonController

PhonePC/2in1TabletTV

[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)组件控制器，用来回调组件内部的点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

### setAgreementStatus

PhonePC/2in1TabletTV

setAgreementStatus(agreementStatus: AgreementStatus): LoginWithHuaweiIDButtonController

设置用户协议的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| agreementStatus | [AgreementStatus](account-api-component-manager.md#agreementstatus) | 是 | 当登录类型为[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时必须设置协议状态为ACCEPTED才可以完成华为账号登录。  当登录类型不是[LoginType.QUICK\_LOGIN](account-api-component-manager.md#logintype)时，如果需要用户同意协议才能完成华为账号登录，请先设置协议状态为NOT\_ACCEPTED，当用户同意协议后设置协议状态为ACCEPTED，才可以完成华为账号登录。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickEvent

PhonePC/2in1TabletTV

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginWithHuaweiIDButtonController

华为账号登录按钮的点击事件。使用callback异步回调。应用可以在用户点击华为账号登录按钮后收到回调，可用于记录运营事件等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ClickEvent](account-api-component-manager.md#clickevent)> | 是 | 回调函数。当用户点击华为账号登录时，err为undefined，data为获取到的[ClickEvent](account-api-component-manager.md#clickevent)；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### onClickLoginWithHuaweiIDButton

PhonePC/2in1TabletTV

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginWithHuaweiIDButtonController

华为账号一键登录结果事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[HuaweiIDCredential](account-api-component-manager.md#huaweiidcredential)> | 是 | 回调函数。当华为账号登录成功返回结果，err为undefined，data为获取到的[HuaweiIDCredential](account-api-component-manager.md#huaweiidcredential)对象；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)和[账号管理错误码](errorcode-account.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001500002](account-api-error-code.md#section1001500002-重复请求) | This error code is reported when a request is already being processed. |
| [1001500003](account-api-error-code.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported. |
| [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](account-api-error-code.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | Invalid input parameter value. |
| [1001502005](account-api-error-code.md#section1001502005-网络错误) | Network error. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | The user canceled the authorization. |
| [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1005300001](account-api-error-code.md#section1005300001-用户未同意协议) | The user did not accept the agreement. |

### setEnabled

PhonePC/2in1TabletTV

setEnabled(enabled: boolean): LoginWithHuaweiIDButtonController

设置华为账号登录按钮是否可点击。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 按钮是否可点击。  当enabled为true时，华为账号登录按钮高亮可点击，当enabled为false时，华为账号登录按钮置灰不可点击，默认值：true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

### continueLogin

PhonePC/2in1TabletTV

continueLogin(callback: AsyncCallback<void>): LoginWithHuaweiIDButtonController

未同意协议时点击登录按钮弹出协议确认弹框，点击同意并登录按钮时调用该接口。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当用户点击协议弹框的同意并登录按钮操作成功，err为undefined，否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDButtonController](account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | [LoginWithHuaweiIDButton](account-api-huawei-id-button.md)组件控制器可以用来注册组件内部的点击事件或者调用组件提供的方法。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1005300002](account-api-error-code.md#section1005300002-用户未点击华为账号一键登录按钮) | The user did not click the HUAWEI ID login button. |

**示例：**

```
1. import { util } from '@kit.ArkTS';
2. import { authentication, loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct QuickLoginButtonComponent {
9. logTag: string = 'QuickLoginButtonComponent';
10. domainId: number = 0x0000;
11. // 匿名手机号
12. @State quickLoginAnonymousPhone: string = '';
13. // 是否勾选协议
14. @State isSelected: boolean = false;
15. // 华为账号用户认证协议链接，此处仅为示例，实际开发过程中，出于可维护性、安全性等方面考虑，域名不建议硬编码在本地
16. private static USER_AUTHENTICATION_PROTOCOL: string =
17. 'https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
18. private static USER_SERVICE_TAG = '用户服务协议';
19. private static PRIVACY_TAG = '隐私协议';
20. private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';
21. // 定义LoginWithHuaweiIDButton展示的隐私文本，展示应用的用户服务协议、隐私协议和华为账号用户认证协议
22. privacyText: loginComponentManager.PrivacyText[] = [{
23. text: '已阅读并同意',
24. type: loginComponentManager.TextType.PLAIN_TEXT
25. }, {
26. text: '《用户服务协议》',
27. tag: QuickLoginButtonComponent.USER_SERVICE_TAG,
28. type: loginComponentManager.TextType.RICH_TEXT
29. }, {
30. text: '《隐私协议》',
31. tag: QuickLoginButtonComponent.PRIVACY_TAG,
32. type: loginComponentManager.TextType.RICH_TEXT
33. }, {
34. text: '和',
35. type: loginComponentManager.TextType.PLAIN_TEXT
36. }, {
37. text: '《华为账号用户认证协议》',
38. tag: QuickLoginButtonComponent.USER_AUTHENTICATION_TAG,
39. type: loginComponentManager.TextType.RICH_TEXT
40. }, {
41. text: '。',
42. type: loginComponentManager.TextType.PLAIN_TEXT
43. }];
44. // 构造LoginWithHuaweiIDButton组件的控制器
45. controller: loginComponentManager.LoginWithHuaweiIDButtonController =
46. new loginComponentManager.LoginWithHuaweiIDButtonController()
47. /**
48. * 当应用使用自定义的登录页时，如果用户未同意协议，需要设置协议状态为NOT_ACCEPTED，当用户同意协议后再设置
49. * 协议状态为ACCEPTED，才可以使用华为账号一键登录功能
50. */
51. .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
52. .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
53. response: loginComponentManager.HuaweiIDCredential) => {
54. this.handleLoginWithHuaweiIDButton(error, response);
55. })
56. .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
57. if (error) {
58. hilog.error(this.domainId, this.logTag,
59. `Failed to click. errCode is ${error.code}, errMessage is ${error.message}`);
60. return;
61. }
62. hilog.info(this.domainId, this.logTag, `onClickEvent clickEvent: ${clickEvent}`);
63. });
64. agreementDialog: CustomDialogController = new CustomDialogController({
65. builder: AgreementDialog({
66. privacyText: this.privacyText,
67. cancel: () => {
68. this.agreementDialog.close();
69. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
70. },
71. confirm: () => {
72. this.agreementDialog.close();
73. this.isSelected = true;
74. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
75. // 调用此方法，同意协议与登录一并完成，无需再次点击登录按钮
76. this.controller.continueLogin((error: BusinessError) => {
77. if (error) {
78. hilog.error(this.domainId, this.logTag,
79. `Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}`);
80. } else {
81. hilog.info(this.domainId, this.logTag,
82. 'Succeeded in clicking agreementDialog continueLogin.');
83. }
84. });
85. },
86. clickHyperlinkText: () => {
87. this.agreementDialog.close();
88. this.jumpToPrivacyWebView();
89. }
90. }),
91. autoCancel: false,
92. alignment: DialogAlignment.Center,
93. });

95. // 传递页面渲染所需的数据，如匿名手机号等
96. aboutToAppear(): void {
97. this.getQuickLoginAnonymousPhone();
98. }

100. // Toast提示
101. showToast(resource: string) {
102. try {
103. this.getUIContext().getPromptAction().showToast({
104. message: resource,
105. duration: 2000
106. });
107. } catch (error) {
108. const message = (error as BusinessError).message
109. const code = (error as BusinessError).code
110. hilog.error(this.domainId, this.logTag, `showToast args  errCode is ${code}, errMessage is ${message}`);
111. }
112. }

114. // 跳转华为账号用户认证协议页,该页面需在工程main_pages.json文件配置
115. jumpToPrivacyWebView() {
116. this.getUIContext().getRouter().pushUrl({
117. // 需在module.json5中增加“ohos.permission.INTERNET”权限
118. url: 'pages/WebPage',
119. params: {
120. isFromDialog: true,
121. url: QuickLoginButtonComponent.USER_AUTHENTICATION_PROTOCOL,
122. }
123. }, (err) => {
124. if (err) {
125. hilog.error(this.domainId, this.logTag,
126. `Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}`);
127. }
128. });
129. }

131. handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
132. response: loginComponentManager.HuaweiIDCredential) {
133. if (error) {
134. hilog.error(this.domainId, this.logTag,
135. `Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}`);
136. if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
137. this.getUIContext().showAlertDialog(
138. {
139. message: "网络未连接，请检查网络设置。",
140. offset: { dx: 0, dy: -12 },
141. alignment: DialogAlignment.Bottom,
142. autoCancel: false,
143. confirm: {
144. value: "知道了",
145. action: () => {
146. }
147. }
148. }
149. );
150. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
151. // 未同意协议，弹出协议弹框，推荐使用该回调方式
152. this.agreementDialog.open();
153. } else if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
154. // 华为账号未登录提示
155. this.showToast("华为账号未登录，请重试");
156. } else if (error.code === ErrorCode.ERROR_CODE_NOT_SUPPORTED) {
157. // 不支持该scopes或permissions提示
158. this.showToast("该scopes或permissions不支持");
159. } else if (error.code === ErrorCode.ERROR_CODE_PARAMETER_ERROR) {
160. // 参数错误提示
161. this.showToast("参数错误");
162. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
163. // 用户取消，无需特别处理
164. } else {
165. // 其他提示系统或服务异常
166. this.showToast('服务或网络异常，请稍后重试');
167. }
168. return;
169. }
170. try {
171. if (this.isSelected) {
172. if (response) {
173. hilog.info(this.domainId, this.logTag, 'Succeeded in clicking LoginWithHuaweiIDButton.');
174. // 开发者根据实际业务情况使用以下信息
175. const authCode = response.authorizationCode;
176. const openID = response.openID;
177. }
178. } else {
179. this.agreementDialog.open();
180. }
181. } catch (err) {
182. hilog.error(this.domainId, this.logTag,
183. `Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}`);
184. this.getUIContext().showAlertDialog(
185. {
186. message: '服务或网络异常，请稍后重试',
187. offset: { dx: 0, dy: -12 },
188. alignment: DialogAlignment.Bottom,
189. autoCancel: false,
190. confirm: {
191. value: '知道了',
192. action: () => {
193. }
194. }
195. }
196. );
197. }
198. }

200. // 错误处理
201. dealAllError(error: BusinessError): void {
202. hilog.error(0x0000, 'testTag', `Failed to login, errorCode=${error.code}, errorMsg=${error.message}`);
203. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
204. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
205. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
206. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
207. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
208. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
209. // 登录失败，请尝试使用其他方式登录
210. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
211. // 用户取消授权
212. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
213. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
214. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
215. // 重复请求，应用无需处理
216. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
217. // 用户未同意协议
218. } else {
219. // 应用登录失败，请尝试使用其他方式登录
220. }
221. }

223. getQuickLoginAnonymousPhone() {
224. // 创建授权请求，并设置参数
225. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
226. /**
227. * 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限
228. * (权限名称为：quickLoginMobilePhone),后续才能获取匿名手机号数据
229. */
230. authRequest.scopes = ['quickLoginAnonymousPhone'];
231. // 用于防跨站点请求伪造
232. authRequest.state = util.generateRandomUUID();
233. // 一键登录场景该参数必须设置为false
234. authRequest.forceAuthorization = false;
235. const controller = new authentication.AuthenticationController();
236. try {
237. controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
238. // 获取到匿名手机号
239. const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
240. if (anonymousPhone) {
241. hilog.info(this.domainId, this.logTag, 'Succeeded in authentication.');
242. this.quickLoginAnonymousPhone = anonymousPhone;
243. return;
244. }
245. hilog.info(this.domainId, this.logTag, 'Succeeded in authentication. AnonymousPhone is empty.');
246. // 未获取到匿名手机号需要跳转到应用自定义的登录页面
247. }).catch((error: BusinessError) => {
248. this.dealAllError(error);
249. })
250. } catch (error) {
251. this.dealAllError(error);
252. }
253. }

255. build() {
256. Scroll() {
257. Column() {
258. Column() {
259. Column() {
260. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
261. Image($r('app.media.app_icon'))
262. .width(48)
263. .height(48)
264. .draggable(false)
265. .copyOption(CopyOptions.None)
266. .onComplete(() => {
267. hilog.info(this.domainId, this.logTag, 'appIcon loading success.');
268. })
269. .onError(() => {
270. hilog.error(this.domainId, this.logTag, 'appIcon loading fail.');
271. })

273. Text($r('app.string.app_name'))
274. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
275. .fontWeight(FontWeight.Medium)
276. .fontWeight(FontWeight.Bold)
277. .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
278. .minFontSize($r('sys.float.ohos_id_text_size_body1'))
279. .maxLines(1)
280. .fontColor($r('sys.color.ohos_id_color_text_primary'))
281. .constraintSize({ maxWidth: '100%' })
282. .margin({
283. top: 12,
284. })

286. Text('应用描述')
287. .fontSize($r('sys.float.ohos_id_text_size_body2'))
288. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
289. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
290. .fontWeight(FontWeight.Regular)
291. .constraintSize({ maxWidth: '100%' })
292. .margin({
293. top: 8,
294. })
295. }.margin({
296. top: 100
297. })

299. Column() {
300. Text(this.quickLoginAnonymousPhone)
301. .fontSize(36)
302. .fontColor($r('sys.color.ohos_id_color_text_primary'))
303. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
304. .fontWeight(FontWeight.Bold)
305. .lineHeight(48)
306. .textAlign(TextAlign.Center)
307. .maxLines(1)
308. .constraintSize({ maxWidth: '100%', minHeight: 48 })

310. Text('华为账号绑定号码')
311. .fontSize($r('sys.float.ohos_id_text_size_body2'))
312. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
313. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
314. .fontWeight(FontWeight.Regular)
315. .lineHeight(19)
316. .textAlign(TextAlign.Center)
317. .maxLines(1)
318. .constraintSize({ maxWidth: '100%' })
319. .margin({
320. top: 8
321. })
322. }.margin({
323. top: 64
324. })

326. Column() {
327. LoginWithHuaweiIDButton({
328. params: {
329. // LoginWithHuaweiIDButton支持的样式
330. style: loginComponentManager.Style.BUTTON_RED,
331. // 账号登录按钮在登录过程中展示加载态
332. extraStyle: {
333. buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
334. show: true
335. })
336. },
337. // LoginWithHuaweiIDButton的边框圆角半径
338. borderRadius: 24,
339. // LoginWithHuaweiIDButton支持的登录类型
340. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
341. // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
342. supportDarkMode: true
343. },
344. controller: this.controller
345. })
346. }
347. .height(40)
348. .margin({
349. top: 56
350. })

352. Column() {
353. Button({
354. type: ButtonType.Capsule,
355. stateEffect: true
356. }) {
357. Text('其他方式登录')
358. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
359. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
360. .fontWeight(FontWeight.Medium)
361. .fontSize($r('sys.float.ohos_id_text_size_button1'))
362. .focusable(true)
363. .focusOnTouch(true)
364. .textOverflow({ overflow: TextOverflow.Ellipsis })
365. .maxLines(1)
366. .padding({ left: 8, right: 8 })
367. }
368. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
369. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
370. .fontWeight(FontWeight.Medium)
371. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
372. .focusable(true)
373. .focusOnTouch(true)
374. .constraintSize({ minHeight: 40 })
375. .width('100%')
376. .onClick(() => {
377. hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
378. })
379. }.margin({ top: 16 })
380. }.width('100%')

382. Row() {
383. Row() {
384. Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
385. .width(24)
386. .height(24)
387. .focusable(true)
388. .focusOnTouch(true)
389. .margin({ top: 0 })
390. .select(this.isSelected)
391. .onChange((value: boolean) => {
392. if (value) {
393. this.isSelected = true;
394. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
395. } else {
396. this.isSelected = false;
397. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
398. }
399. hilog.info(this.domainId, this.logTag, `agreementChecked: ${value}`);
400. })
401. }

403. Row() {
404. Text() {
405. ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
406. if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
407. Span(item?.text)
408. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
409. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
410. .fontWeight(FontWeight.Regular)
411. .fontSize($r('sys.float.ohos_id_text_size_body3'))
412. } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
413. Span(item?.text)
414. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
415. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
416. .fontWeight(FontWeight.Medium)
417. .fontSize($r('sys.float.ohos_id_text_size_body3'))
418. .onClick(() => {
419. // 应用需要根据item.tag实现协议页面的跳转逻辑
420. hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
421. // 华为账号用户认证协议
422. if (item.tag === QuickLoginButtonComponent.USER_AUTHENTICATION_TAG) {
423. this.jumpToPrivacyWebView();
424. }
425. })
426. }
427. }, (item: loginComponentManager.PrivacyText) => item.text.toString())
428. }
429. .width('100%')
430. }
431. .margin({ left: 12 })
432. .layoutWeight(1)
433. .constraintSize({ minHeight: 24 })
434. }
435. .alignItems(VerticalAlign.Top)
436. .margin({
437. bottom: 44
438. })
439. }
440. .justifyContent(FlexAlign.SpaceBetween)
441. .constraintSize({ minHeight: '100%' })
442. .margin({
443. left: 16,
444. right: 16
445. })
446. }
447. .width('100%')
448. .height('100%')
449. }
450. }

452. @CustomDialog
453. export struct AgreementDialog {
454. logTag: string = 'AgreementDialog';
455. domainId: number = 0x0000;
456. dialogController?: CustomDialogController;
457. cancel: () => void = () => {
458. };
459. confirm: () => void = () => {
460. };
461. clickHyperlinkText: () => void = () => {
462. };
463. privacyText: loginComponentManager.PrivacyText[] = [];
464. private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';

466. build() {
467. Column() {
468. Row() {
469. Text('用户协议与隐私条款')
470. .id('loginPanel_agreement_dialog_privacy_title')
471. .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
472. .minFontSize($r('sys.float.ohos_id_text_size_body1'))
473. .fontColor($r('sys.color.ohos_id_color_text_primary'))
474. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
475. .fontWeight(FontWeight.Bold)
476. .textAlign(TextAlign.Center)
477. .textOverflow({ overflow: TextOverflow.Ellipsis })
478. .maxLines(2)
479. }
480. .alignItems(VerticalAlign.Center)
481. .constraintSize({ minHeight: 56, maxWidth: 400 })
482. .margin({
483. left: $r('sys.float.ohos_id_max_padding_start'),
484. right: $r('sys.float.ohos_id_max_padding_start')
485. })

487. Row() {
488. Text() {
489. ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
490. if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
491. Span(item?.text)
492. .fontSize($r('sys.float.ohos_id_text_size_body1'))
493. .fontColor($r('sys.color.ohos_id_color_text_primary'))
494. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
495. .fontWeight(FontWeight.Regular)
496. } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
497. Span(item?.text)
498. .fontSize($r('sys.float.ohos_id_text_size_body1'))
499. .fontColor('#CE0E2D')
500. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
501. .fontWeight(FontWeight.Medium)
502. .onClick(() => {
503. // 应用需要根据item.tag实现协议页面的跳转逻辑
504. hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
505. // 华为账号用户认证协议
506. if (item.tag === AgreementDialog.USER_AUTHENTICATION_TAG) {
507. hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
508. this.clickHyperlinkText();
509. }
510. })
511. }
512. }, (item: loginComponentManager.PrivacyText) => item.text.toString())
513. }
514. .width('100%')
515. .textOverflow({ overflow: TextOverflow.Ellipsis })
516. .maxLines(10)
517. .textAlign(TextAlign.Start)
518. .focusable(true)
519. .focusOnTouch(true)
520. .padding({ left: 24, right: 24 })
521. }.width('100%')

523. Flex({
524. direction: FlexDirection.Row
525. }) {
526. Button('取消',
527. { type: ButtonType.Capsule, stateEffect: true })
528. .id('loginPanel_agreement_cancel_btn')
529. .fontColor($r('sys.color.ohos_id_color_text_primary'))
530. .fontSize($r('sys.float.ohos_id_text_size_button1'))
531. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
532. .backgroundColor(Color.Transparent)
533. .fontWeight(FontWeight.Medium)
534. .focusable(true)
535. .focusOnTouch(true)
536. .constraintSize({ minHeight: 40, maxWidth: 400 })
537. .width('50%')
538. .onClick(() => {
539. hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
540. this.cancel();
541. })

543. Button('同意并登录',
544. { type: ButtonType.Capsule, stateEffect: true })
545. .id('loginPanel_agreement_dialog_huawei_id_login_btn')
546. .fontColor(Color.White)
547. .backgroundColor('#CE0E2D')
548. .fontSize($r('sys.float.ohos_id_text_size_button1'))
549. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
550. .fontWeight(FontWeight.Medium)
551. .focusable(true)
552. .focusOnTouch(true)
553. .constraintSize({ minHeight: 40, maxWidth: 400 })
554. .width('50%')
555. .onClick(() => {
556. hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
557. this.confirm();
558. })
559. }
560. .margin({
561. top: 8,
562. left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
563. right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
564. bottom: 16
565. })
566. }.backgroundColor($r('sys.color.ohos_id_color_dialog_default_bg'))
567. .padding({
568. left: 16,
569. right: 16
570. })
571. }
572. }

574. export enum ErrorCode {
575. // 账号未登录
576. ERROR_CODE_LOGIN_OUT = 1001502001,
577. // 该账号不支持一键登录，如海外账号
578. ERROR_CODE_NOT_SUPPORTED = 1001500003,
579. // 网络错误
580. ERROR_CODE_NETWORK_ERROR = 1001502005,
581. // 内部错误
582. ERROR_CODE_INTERNAL_ERROR = 1001502009,
583. // 用户取消授权
584. ERROR_CODE_USER_CANCEL = 1001502012,
585. // 系统服务异常
586. ERROR_CODE_SYSTEM_SERVICE = 12300001,
587. // 用户未同意用户协议
588. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
589. // 参数错误
590. ERROR_CODE_PARAMETER_ERROR = 401,
591. // 重复请求
592. ERROR_CODE_REQUEST_REFUSE = 1001500002
593. }
```

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 华为账号用户认证协议展示页
5. @Entry
6. @Component
7. struct WebPage {
8. @State webUrl?: string = '';
9. @State progress: number = 0;
10. logTag: string = 'WebPage';
11. domainId: number = 0x0000;
12. controller: webview.WebviewController = new webview.WebviewController();

14. build() {
15. Column() {
16. Column() {
17. Button({ type: ButtonType.Normal }) {
18. Image($r('sys.media.ohos_ic_compnent_titlebar_back'))
19. .backgroundColor(Color.Transparent)
20. .borderRadius(20)
21. .width(24)
22. .height(24)
23. .draggable(false)
24. .autoResize(false)
25. .focusable(true)
26. .fillColor($r('sys.color.ohos_id_color_titlebar_icon'))
27. .matchTextDirection(true)
28. }
29. .alignSelf(ItemAlign.Start)
30. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
31. .borderRadius(20)
32. .width(40)
33. .height(40)
34. .onClick(() => {
35. this.getUIContext().getRouter().back();
36. })
37. }
38. .height(56)
39. .width('100%')
40. .justifyContent(FlexAlign.Center)

42. Progress({ value: this.progress, type: ProgressType.Linear })
43. .width('100%')
44. .visibility(this.progress <= 99 ? Visibility.Visible : Visibility.None)

46. Web({ src: this.webUrl ?? '', controller: this.controller })
47. .backgroundColor(Color.Transparent)
48. .onProgressChange((event) => {
49. hilog.info(this.domainId, this.logTag,
50. 'onProgressChange: ', (event ? event.newProgress : -1));
51. this.progress = event ? event.newProgress : 0;
52. })
53. .darkMode(WebDarkMode.Auto)
54. .forceDarkAccess(true)
55. .onLoadIntercept((event) => {
56. hilog.info(this.domainId, this.logTag, 'onLoadIntercept');
57. return false;
58. })
59. .onErrorReceive((event) => {
60. if (event) {
61. hilog.error(this.domainId, this.logTag, `onErrorReceive,errorInfo: ${event?.error?.getErrorInfo()}`);
62. }
63. })
64. }
65. .alignItems(HorizontalAlign.Start)
66. .padding({ left: 12, right: 12 })
67. .width('100%')
68. .height('100%')
69. }

71. aboutToAppear(): void {
72. hilog.info(0x0000, 'testTag', 'aboutToAppear');
73. const params = this.getUIContext().getRouter().getParams() as Record<string, string>;
74. this.webUrl = params.url ?? '';
75. hilog.info(0x0000, 'testTag', `webUrl: ${this.webUrl}`);
76. }

78. aboutToDisappear(): void {
79. hilog.info(0x0000, 'testTag', 'aboutToDisappear');
80. if (this.webUrl) {
81. try {
82. this.controller.stop();
83. } catch (error) {
84. hilog.error(0x0000, 'testTag', `stop web error, errorCode=${error.code}, errorMsg=${error.message}`);
85. }
86. }
87. }
88. }
```
