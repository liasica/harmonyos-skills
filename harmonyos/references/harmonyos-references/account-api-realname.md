---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-realname
title: realName (华为账号实名认证服务)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > realName (华为账号实名认证服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30c15980318d3d78310ce1b6f0810e1885910126a872d7e72bd9f9f6cbbaa598
---

本模块提供Account Kit实名认证能力，包括人脸核身功能。当需要验证用户实名信息的场景，为保证用户填写的实名信息的正确性，应用需要对用户的实名信息进行校验。

**起始版本：** 5.0.0(12)

说明

该接口目前暂停开放。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { realName } from '@kit.AccountKit';
```

## FacialRecognitionVerificationRequest

PhonePC/2in1TabletTVWearable

该类为人脸核身请求对象，定义了人脸核身请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| verificationToken | string | 否 | 否 | 身份验证令牌，调用华为账号OpenRealName服务[实名信息校验](account-api-verify-realname.md)接口获取。长度限制1-2048。 |
| state | string | 否 | 是 | 请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。  默认值：undefined。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

**示例：**

```
1. import { realName } from '@kit.AccountKit';
2. import { util } from '@kit.ArkTS';

4. const request: realName.FacialRecognitionVerificationRequest = {
5. verificationToken: "<可调用华为账号服务实名信息校验接口获取>", // 调用华为账号OpenRealName服务实名信息校验接口获取
6. state: util.generateRandomUUID() // 建议使用generateRandomUUID生成state
7. }
```

## FacialRecognitionVerificationResult

PhonePC/2in1TabletTVWearable

该类为人脸核身请求结果对象，定义了人脸核身请求返回结果数据字段。如果成功返回该对象，说明人脸核身验证成功。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| facialRecognitionVerificationToken | string | 是 | 否 | 验证成功后返回的人脸核身验证令牌。长度限制1-2048。 |
| state | string | 是 | 是 | 响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

## RealNameErrorCode

PhonePC/2in1TabletTVWearable

该枚举为Account Kit实名认证服务的错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NETWORK\_ERROR | [1002500001](account-api-error-code.md#section1002500001-网络不可用) | 网络不可用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1002500002](account-api-error-code.md#section1002500002-账号未登录) | 用户未登录华为账号。 |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1002500003](account-api-error-code.md#section1002500003-应用指纹证书校验失败) | 应用指纹证书校验失败。 |
| PERMISSION\_CHECK\_ERROR | [1002500004](account-api-error-code.md#section1002500004-应用未申请对应permissions权限) | 应用程序未申请对应permissions权限。 |
| USER\_CANCELED | [1002500005](account-api-error-code.md#section1002500005-用户取消验证) | 用户取消验证。 |
| INTERNAL\_ERROR | [1002500006](account-api-error-code.md#section1002500006-内部错误) | 内部错误。 |
| REAL\_NAME\_UNSUPPORTED | [1002500008](account-api-error-code.md#section1002500008-该华为账号不支持实名验证) | 该华为账号不支持实名验证。 |
| REAL\_NAME\_VERIFICATION\_ERROR | [1002500009](account-api-error-code.md#section1002500009-实名渠道验证失败) | 实名渠道验证错误。 |
| FACE\_NOT\_MATCH | [1002500011](account-api-error-code.md#section1002500011-您的面部与作为身份证明的面部图像不匹配) | 您的面部与作为身份证明的面部图像不匹配。 |
| REAL\_NAME\_NOT\_EXIST | [1002500012](account-api-error-code.md#section1002500012-未查询到实名信息) | 未查询到该华为账号的实名信息。 |
| NAME\_AND\_ID\_NUMBER\_NOT\_MATCH | [1002500013](account-api-error-code.md#section1002500013-姓名和身份证号码不匹配) | 姓名和身份证号码不匹配。 |
| TOO\_MANY\_ATTEMPTS | [1002500014](account-api-error-code.md#section1002500014-实名验证尝试次数过多) | 实名验证尝试次数过多。24小时后重试。 |
| VERIFICATION\_TOKEN\_INCORRECT | [1002500015](account-api-error-code.md#section1002500015-参数verificationtoken不合法) | 参数verificationToken不合法。 |
| DEVICE\_NOT\_SUPPORTED | [1002500016](account-api-error-code.md#section1002500016-此设备不支持此api) | 此设备不支持此API。 |

## startFacialRecognitionVerification

PhonePC/2in1TabletTVWearable

startFacialRecognitionVerification(context: common.Context, request: FacialRecognitionVerificationRequest): Promise<FacialRecognitionVerificationResult>

执行华为账号人脸核身请求，拉起验证人脸页面。使用Promise异步回调。

说明

该接口暂不支持儿童账号使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.RealNameVerify

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| request | [FacialRecognitionVerificationRequest](account-api-realname.md#facialrecognitionverificationrequest) | 是 | 人脸核身请求对象，传入令牌等信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FacialRecognitionVerificationResult](account-api-realname.md#facialrecognitionverificationresult)> | Promise对象，返回[FacialRecognitionVerificationResult](account-api-realname.md#facialrecognitionverificationresult)对象。返回该对象，说明人脸核身验证成功。可使用该对象的state和入参对象的state比较，校验是否是当前请求，可防止跨站攻击。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. Function startFacialRecognitionVerification can not work correctly due to limited device capabilities. |
| [1002500001](account-api-error-code.md#section1002500001-网络不可用) | The network is unavailable. |
| [1002500002](account-api-error-code.md#section1002500002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1002500003](account-api-error-code.md#section1002500003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1002500004](account-api-error-code.md#section1002500004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1002500005](account-api-error-code.md#section1002500005-用户取消验证) | The user canceled the verification of the HUAWEI ID. |
| [1002500006](account-api-error-code.md#section1002500006-内部错误) | Internal error. |
| [1002500008](account-api-error-code.md#section1002500008-该华为账号不支持实名验证) | Real-name verification is not supported for the HUAWEI ID. |
| [1002500011](account-api-error-code.md#section1002500011-您的面部与作为身份证明的面部图像不匹配) | Your face does not match your facial image as proof of identity. |
| [1002500012](account-api-error-code.md#section1002500012-未查询到实名信息) | No real-name information is found for the HUAWEI ID. |
| [1002500013](account-api-error-code.md#section1002500013-姓名和身份证号码不匹配) | Your name and ID number do not match. |
| [1002500014](account-api-error-code.md#section1002500014-实名验证尝试次数过多) | Too many real-name verification attempts. |
| [1002500015](account-api-error-code.md#section1002500015-参数verificationtoken不合法) | The verificationToken parameter is incorrectly set. |
| [1002500016](account-api-error-code.md#section1002500016-此设备不支持此api) | This device does not support this API. |

**示例：**

```
1. import { realName } from '@kit.AccountKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { util } from '@kit.ArkTS';

6. const request: realName.FacialRecognitionVerificationRequest = {
7. verificationToken: "<可调用华为账号服务实名信息校验接口获取>", // 调用华为账号OpenRealName服务实名信息校验接口获取
8. state: util.generateRandomUUID() // 建议使用generateRandomUUID生成state
9. }
10. hilog.info(0x0000, 'testTag', `verifyFacialRecognitionWithPromise params ${request}`);
11. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
12. realName.startFacialRecognitionVerification(this.getUIContext().getHostContext(), request).then(data => {
13. const verifyResult = data as realName.FacialRecognitionVerificationResult;
14. // 开发者处理verifyResult
15. hilog.info(0x0000, 'testTag', 'Succeeded in verifying facial recognition.');
16. }).catch((error: BusinessError<Object>) => {
17. dealAllError(error);
18. })

20. // 错误处理
21. function dealAllError(error: BusinessError<Object>): void {
22. hilog.error(0x0000, 'testTag', `Failed to authorize. Code: ${error.code}, message: ${error.message}`);
23. }
```
