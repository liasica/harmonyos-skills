---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-extendservice
title: "@hms.core.account.extendService (华为账号增强服务)"
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > @hms.core.account.extendService (华为账号增强服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca047d3b96c94e46f9c56b6cf9cdf879dd6eb343f04b61a0ef3d36878df3931c
---

## 模块概述

@hms.core.account.extendService模块提供华为账号增强能力，在基础的登录、授权功能之上，为应用提供更丰富的账号管理与安全校验能力。包含两大核心功能：身份验证、打开账号中心。

* 身份验证：拉起身份验证页面，对当前系统登录的华为账号用户的身份进行校验，以保护用户的个人信息和隐私安全。
* 打开账号中心：直接拉起华为账号中心页面，供用户查看并管理当前登录的华为账号信息。

开发者可通过@hms.core.account.extendService模块提供的方法[verifyAccount](account-api-extendservice.md#verifyaccount-1)、[startAccountCenter](account-api-extendservice.md#startaccountcenter-1)实现上述能力。

**起始版本：** 4.0.0(10)

**说明** 

该服务目前仅对系统应用开放。

## 导入模块

```typescript
import { extendService } from '@kit.AccountKit';
```

## IdType

华为账号身份标识类型枚举。当前支持设置：IdType.UNION\_ID或IdType.OPEN\_ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| USER\_ID | 1 | 华为账号用户的UID。  **说明：** 该参数仅对系统应用开放。 |
| OPEN\_ID | 2 | 华为账号用户的OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| UNION\_ID | 3 | 华为账号用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

## RiskLevel

风险等级枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| LOW | 1 | 低风险。 |
| HIGH | 2 | 高风险。 |

## VerifyRequest

身份验证请求。[verifyAccount](account-api-extendservice.md#verifyaccount-1)方法入参，接口需包含用户的基础身份标识，与系统华为账号用户进行身份比对。开发者可通过设置身份验证的场景值、风险等级等属性，控制身份验证的次数和方式，华为账号服务会根据这些属性拉起对应的身份验证页面。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-extendservice.md#idtype) | 否 | 否 | 华为账号身份标识类型。当前非系统应用仅支持设置：IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 华为账号身份标识UnionID/OpenID值。身份标识类型通过idType属性定义。长度限制1-256。  UnionID、OpenID值可以通过[华为账号登录](account-api-authentication.md#登录华为账号)、[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)、[华为账号Panel登录组件](account-api-loginpanel.md#loginpanel)或[华为账号Button登录组件](account-api-huawei-id-button.md#loginwithhuaweiidbutton)获取。 |
| sceneId | string | 否 | 否 | 身份验证的场景值，该值与riskLevel属性一起代表了应用在华为账号服务器上的一组配置，包括验证次数、首次验证方式、二次验证方式等。长度限制1-10。 |
| riskLevel | [RiskLevel](account-api-extendservice.md#risklevel) | 否 | 否 | 风险等级，该值与sceneId一起代表了应用在华为账号服务器上的一组配置，一般风险等级高的场景，需要进行二次验证。 |
| nonce | string | 否 | 否 | 请求体中的nonce属性，长度限制1-64。该属性会包含在返回的verifyToken中，通过校验一致性，可用于防止重放攻击。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { util } from '@kit.ArkTS';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
};
```

## VerifyResult

身份验证请求响应。[verifyAccount](account-api-extendservice.md#verifyaccount-1)方法返回值，当用户验证身份成功时返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| verifyToken | string | 是 | 否 | 身份验证返回的Token，JWT格式的数据。 |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录或授权接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
};

// 执行身份验证请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error: BusinessError, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // 开发者处理verifyToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

## ExtendErrorCode

华为账号增强服务接口错误码枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INVALID\_PARAMETER | [401](errorcode-universal.md#section401-参数检查失败) | 参数检查失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NETWORK\_ERROR | [1001600001](errorcode-account-kit.md#section1001600001-网络不可用) | 网络不可用。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001600002](errorcode-account-kit.md#section1001600002-账号未登录) | 用户未登录华为账号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001600003](errorcode-account-kit.md#section1001600003-应用指纹证书校验失败) | 应用指纹证书校验失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PERMISSION\_CHECK\_ERROR | [1001600004](errorcode-account-kit.md#section1001600004-应用未申请对应permissions权限) | 应用未申请对应permissions权限。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| USER\_CANCELED | [1001600005](errorcode-account-kit.md#section1001600005-用户取消当前操作) | 用户取消当前操作。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| VERIFICATION\_FACTOR\_UNAVAILABLE | [1001600006](errorcode-account-kit.md#section1001600006-当前设备不支持此验证要素) | 当前设备不支持此验证要素。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| INTERNAL\_ERROR | [1001600007](errorcode-account-kit.md#section1001600007-内部错误) | 内部错误。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| DEVICE\_NOT\_SUPPORTED | [1001600011](errorcode-account-kit.md#section1001600011-该设备不支持此api) | 该设备不支持此API。  **起始版本：** 6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

## verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest, callback: AsyncCallback<VerifyResult>): void

身份验证方法，使用Callback异步回调返回验证成功凭证。调用该方法会拉起身份验证页面，需要用户进行密码、短信等方式验证身份。身份页面可长时间停留，当用户验证成功后，会返回验证凭证给应用，其他场景如用户点击关闭则会抛出错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |
| request | [VerifyRequest](account-api-extendservice.md#verifyrequest) | 是 | 身份验证请求对象，包含请求参数。 |
| callback | AsyncCallback<[VerifyResult](account-api-extendservice.md#verifyresult)> | 是 | 回调函数。  当身份验证请求成功，err为undefined，data为获取到的[VerifyResult](account-api-extendservice.md#verifyresult)对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1001600001](errorcode-account-kit.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](errorcode-account-kit.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](errorcode-account-kit.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](errorcode-account-kit.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600005](errorcode-account-kit.md#section1001600005-用户取消当前操作) | The user canceled the current operation. |
| [1001600006](errorcode-account-kit.md#section1001600006-当前设备不支持此验证要素) | The requested verification factors are unavailable on the device. |
| [1001600007](errorcode-account-kit.md#section1001600007-内部错误) | Internal error. |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
};

// 执行身份验证请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const verifyResult = data as extendService.VerifyResult;
    hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
    const verifyToken = verifyResult.verifyToken;
    // 开发者处理verifyToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

## verifyAccount

verifyAccount(context: common.Context, request: VerifyRequest): Promise<VerifyResult>

身份验证方法，使用Promise异步回调返回验证成功凭证。调用该方法会拉起身份验证页面，需要用户进行密码、短信等方式验证身份。身份页面可长时间停留，当用户验证成功后，会返回验证凭证给应用，其他场景如用户点击关闭则会抛出错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |
| request | [VerifyRequest](account-api-extendservice.md#verifyrequest) | 是 | 身份验证请求对象，包含请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[VerifyResult](account-api-extendservice.md#verifyresult)> | Promise对象，返回[VerifyResult](account-api-extendservice.md#verifyresult)对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1001600001](errorcode-account-kit.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](errorcode-account-kit.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](errorcode-account-kit.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](errorcode-account-kit.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600005](errorcode-account-kit.md#section1001600005-用户取消当前操作) | The user canceled the current operation. |
| [1001600006](errorcode-account-kit.md#section1001600006-当前设备不支持此验证要素) | The requested verification factors are unavailable on the device. |
| [1001600007](errorcode-account-kit.md#section1001600007-内部错误) | Internal error. |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const request: extendService.VerifyRequest = {
  idType: extendService.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
  riskLevel: extendService.RiskLevel.LOW,
  nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
};

// 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
// 执行身份验证请求，并处理结果
extendService.verifyAccount(this.getUIContext().getHostContext(), request).then(data => {
  const verifyResult = data as extendService.VerifyResult;
  hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
  const verifyToken = verifyResult.verifyToken;
  // 开发者处理verifyToken
}).catch((error: BusinessError) => {
  dealAllError(error);
});

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```

## startAccountCenter

startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void

打开华为账号中心方法，使用Callback异步回调。开发者可调用该方法拉起账号中心页面，供用户查看并管理头像、昵称、手机号等个人信息。账号中心页面会长时间停留，当用户关闭该页面后，会触发Callback回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet、TV中可正常调用，在其他设备类型中返回1001600011错误码。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。  当执行打开账号中心请求成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.  适用版本：4.1.0(11)+ |
| [1001600001](errorcode-account-kit.md#section1001600001-网络不可用) | The network is unavailable.  适用版本：4.1.0(11)+ |
| [1001600002](errorcode-account-kit.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](errorcode-account-kit.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](errorcode-account-kit.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600007](errorcode-account-kit.md#section1001600007-内部错误) | Internal error. |
| [1001600011](errorcode-account-kit.md#section1001600011-该设备不支持此api) | This device does not support this API.  适用版本：6.1.0(23)+ |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 执行打开账号中心请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  extendService.startAccountCenter(this.getUIContext().getHostContext(), (error: BusinessError) => {
    if (error) {
      dealAllError(error);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
}
```

## startAccountCenter

startAccountCenter(context: common.Context): Promise<void>

打开华为账号中心方法，使用Promise异步回调。开发者可调用该方法拉起账号中心页面，供用户查看并管理头像、昵称、手机号等个人信息。账号中心页面会长时间停留，当用户关闭该页面后，会返回无结果的Promise对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet、TV中可正常调用，在其他设备类型中返回1001600011错误码。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.  适用版本：4.1.0(11)+ |
| [1001600001](errorcode-account-kit.md#section1001600001-网络不可用) | The network is unavailable.  适用版本：4.1.0(11)+ |
| [1001600002](errorcode-account-kit.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](errorcode-account-kit.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](errorcode-account-kit.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600007](errorcode-account-kit.md#section1001600007-内部错误) | Internal error. |
| [1001600011](errorcode-account-kit.md#section1001600011-该设备不支持此api) | This device does not support this API.  适用版本：6.1.0(23)+ |

**示例：**

```typescript
import { extendService } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
// 执行打开账号中心请求，并处理结果
extendService.startAccountCenter(this.getUIContext().getHostContext()).then(() => {
  hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
}).catch((error: BusinessError<Object>) => {
  dealAllError(error);
});

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
}
```
