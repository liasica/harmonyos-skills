---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-authentication
title: "@hms.core.authentication (华为账号应用统一认证服务)"
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > @hms.core.authentication (华为账号应用统一认证服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:71d68f81a3166d50010de5ee737be3b7099c8777d9b269632eec31da94f4015b
---

## 模块概述

@hms.core.authentication模块提供华为账号应用统一认证能力，其中[登录华为账号](account-api-authentication.md#登录华为账号)与[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)为核心功能。

* 登录华为账号：获取华为账号用户（使用华为账号登录华为终端设备的用户，以下简称“华为账号用户”）的用户标识（UnionID/OpenID，可参考[基本概念](account-api-authentication.md#基本概念)），用于与应用原有用户体系进行关联，实现基于华为账号的免注册快速登录。
* 获取华为账号用户信息：申请华为账号用户授权，获取其头像昵称、风险等级等扩展用户信息，用于完善用户个人资料。

在此基础之上，该模块也提供了[获取华为账号登录状态](account-api-authentication.md#获取华为账号登录状态)、[获取手机号一致性状态](account-api-authentication.md#获取手机号一致性状态)两种辅助能力，用于优化登录状态管理、完善应用安全风控处理逻辑。

* 获取华为账号登录状态：快速判断当前系统登录的华为账号是否与应用已获取的用户标识（UnionID/OpenID）相匹配，查询系统是否已登录华为账号。
* 获取手机号一致性状态：通过[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)获取绑定手机号后，开发者可通过此能力判断开发者获取的手机号、系统华为账号绑定手机号与当前设备SIM卡之间的关系，辅助确认用户身份，用于安全风控处理。

开发者可通过[HuaweiIDProvider](account-api-authentication.md#huaweiidprovider)与[AuthenticationController](account-api-authentication.md#authenticationcontroller)协同实现华为账号统一认证的核心功能。

HuaweiIDProvider：华为账号服务认证工厂类，主要负责创建华为账号登录、授权、取消授权请求对象。开发者可根据具体业务场景灵活配置对象属性。

AuthenticationController：华为账号服务控制器类，负责接收并执行华为账号登录、授权、取消授权请求。开发者需将HuaweiIDProvider创建的请求对象作为入参，调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法请求华为账号服务。

### 基本概念

* **OpenID**：应用维度用户标识符，是华为账号用户在应用/元服务的唯一标识。不同应用/元服务（不管是否在同一个开发者账号下）获取到用户的OpenID不同。OpenID严格区分大小写。
* **UnionID**：开发者维度用户标识符，华为账号用户在同一开发者账号下的唯一标识。开发者有多个应用/元服务时，同一个开发者账号下的应用/元服务获取到用户的UnionID相同。UnionID严格区分大小写。
* **Authorization Code**：授权码，用户使用华为账号登录成功之后，可通过返回的结果解析出授权码。通过授权码可获取访问凭证Access Token、ID Token等，可参考[开放接口调用凭证](account-api-obtain-token-overview.md)。
* **ID Token**：用户身份凭证，是OIDC ([OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)) 协议相对于OAuth 2.0 协议扩展的一个用户身份凭证，包含用户信息。用户使用华为账号登录成功之后，可通过返回的凭据解析出Authorization Code、ID Token等数据。
* **Access Token**：访问凭证，是访问被权限管控资源的应用级凭证。可使用Access Token调用获取用户信息接口获取用户信息。

### 登录华为账号

@hms.core.authentication模块提供安全、便捷的华为账号登录能力。

开发者可通过登录能力获取授权码Authorization Code。应用服务端使用Authorization Code调用[获取用户级凭证](account-api-obtain-user-token.md#接口原型)接口向华为账号服务器请求获取Access Token，使用Access Token调用[解析凭证](account-api-get-token-info.md#接口原型)接口获取用户的UnionID/OpenID。应用服务端通过UnionID/OpenID判断该用户是否已关联其原有用户体系。如已关联，则完成用户登录；如未关联，则创建新用户，绑定UnionID/OpenID，完成用户登录。

开发者需使用HuaweiIDProvider构造华为账号登录请求对象，并通过AuthenticationController执行登录请求，流程伪代码如下：

```typescript
provider = new authentication.HuaweiIDProvider();
loginWithHuaweiIDRequest = provider.createLoginWithHuaweiIDRequest();
controller = new authentication.AuthenticationController(context);
loginWithHuaweiIDResponse = controller.executeRequest(loginWithHuaweiIDRequest);
loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
code = loginWithHuaweiIDCredential?.authorizationCode; // 由credential可解析出授权码Authorization Code
// 将Authorization Code上传应用服务端，应用服务端请求华为账号服务器获取UnionID/OpenID
```

### 获取华为账号用户信息

@hms.core.authentication模块提供了华为账号授权与取消授权能力，用于获取华为账号头像昵称、风险等级、华为账号绑定的匿名手机号等用户信息，以及管理用户与应用的授权关系。

开发者可通过授权能力申请获取用户信息访问权限，在用户授权后即可获得授权码Authorization Code。应用服务端使用Authorization Code通过[获取用户级凭证](account-api-obtain-user-token.md#接口原型)、[获取用户信息](account-api-get-user-info-overview.md)向华为账号服务器请求获取Access Token、用户信息。应用获取用户信息后，可用于完善并展示个人资料。

在获取到用户授权后，开发者可通过取消授权能力，主动解除用户授予应用的用户信息访问权限。

开发者需使用HuaweiIDProvider构造授权、取消授权请求对象，并通过AuthenticationController执行请求。流程伪代码如下：

```typescript
// 授权：
provider = new authentication.HuaweiIDProvider();
authorizationWithHuaweiIDRequest = provider.createAuthorizationWithHuaweiIDRequest();
controller = new authentication.AuthenticationController(context);
authorizationWithHuaweiIDResponse = controller.executeRequest(authorizationWithHuaweiIDRequest);
authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
code = authorizationWithHuaweiIDCredential?.authorizationCode; // 由credential可解析出授权码Authorization Code
// 将Authorization Code上传应用服务端，应用服务端请求华为账号服务器获取用户信息

// 取消授权：
cancelAuthorizationRequest = provider.createCancelAuthorizationRequest();
cancelAuthorizationResponse = controller.executeRequest(cancelAuthorizationRequest); // 取消授权成功时返回，失败时返回错误码
```

### 获取华为账号登录状态

@hms.core.authentication模块提供获取华为账号登录状态能力，用于判断当前系统是否已登录华为账号。 开发者获取用户标识（UnionID/OpenID）后，可通过该能力查询华为账号登录状态，不依赖网络连接。

开发者可创建获取华为账号登录状态请求对象，将已获取的用户标识（UnionID/OpenID）传入，查询登录状态。存在如下三种状态，具体可参考[State](account-api-authentication.md#state)：

* 华为账号未登录。
* 华为账号已登录且传入账号的UnionID/OpenID与当前账号一致。
* 华为账号已登录且传入账号的UnionID/OpenID与当前账号不一致。

### 获取手机号一致性状态

@hms.core.authentication模块提供手机号一致性状态校验能力，可校验应用通过[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)获取的手机号是否与华为账号绑定的手机号、本机SIM卡一致。当应用登录后需要进行高风险操作时，可通过该能力查询手机号一致性状态，从而进行相应的安全风控处理。

开发者可创建请求对象，将已获取的手机号、用户标识（UnionID/OpenID）传入。Account Kit会判断开发者传入的手机号、华为账号绑定手机号、当前设备SIM卡之间的关系，存在如下三种一致性状态，具体可参考[ConsistencyRequest](account-api-authentication.md#consistencyrequest)：

* 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号一致。
* 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号均不一致或当前设备无SIM卡。
* 华为账号已登录，传入的手机号与当前账号绑定的手机号不一致。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { authentication } from '@kit.AccountKit';
```

## HuaweiIDProvider

HuaweiIDProvider为华为账号服务认证工厂类，主要负责创建华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）、授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）、取消授权（[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)）请求对象。开发者可根据业务场景修改对象属性，之后通过[AuthenticationController](account-api-authentication.md#authenticationcontroller)执行请求。

此外，HuaweiIDProvider工厂类还提供了[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)和[getMobileNumberConsistency](account-api-authentication.md#getmobilenumberconsistency)方法，分别用以获取华为账号的登录状态和手机号一致性状态。开发者可根据业务信息，构造[StateRequest](account-api-authentication.md#staterequest)和[ConsistencyRequest](account-api-authentication.md#consistencyrequest)作为入参，调用上述方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** HuaweiIDProvider继承自[AuthenticationProvider](account-api-authentication.md#authenticationprovider)。

### createLoginWithHuaweiIDRequest

createLoginWithHuaweiIDRequest(): LoginWithHuaweiIDRequest

创建并返回华为账号登录请求对象[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)。

通过该方法创建并返回请求对象后，可将其作为入参调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行华为账号登录请求，获取用户标识（UnionID/OpenID）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest) | 华为账号登录请求对象。 |

**示例：**

参见[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)。

### createAuthorizationWithHuaweiIDRequest

createAuthorizationWithHuaweiIDRequest(): AuthorizationWithHuaweiIDRequest

创建并返回华为账号授权请求对象[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)。

通过该方法创建并返回请求对象后，可将其作为入参调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行华为账号授权请求，获取用户授权凭据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest) | 华为账号授权请求对象。 |

**示例：**

参见[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)。

### createCancelAuthorizationRequest

createCancelAuthorizationRequest(): CancelAuthorizationRequest

创建并返回华为账号取消授权请求对象[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)。

通过该方法创建并返回请求对象后，可将其作为入参调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行取消授权请求，主动解除用户授予应用的用户信息访问权限。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest) | 华为账号取消授权请求对象。 |

**示例：**

参见[CancelAuthorizationResponse](account-api-authentication.md#cancelauthorizationresponse)。

### getHuaweiIDState

getHuaweiIDState(request: StateRequest): Promise<StateResult>

获取华为账号登录状态，此方法不依赖网络连接，使用Promise异步回调。

开发者可创建请求对象[StateRequest](account-api-authentication.md#staterequest)，将已获取的用户标识（UnionID/OpenID）传入（UnionID、OpenID值可以通过[登录华为账号](account-api-authentication.md#登录华为账号)、[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)、[华为账号Panel登录组件](account-api-loginpanel.md#loginpanel)或[华为账号Button登录组件](account-api-huawei-id-button.md#loginwithhuaweiidbutton)获取）。Account Kit会判断系统是否已登录华为账号、已登录的华为账号是否与开发者传入的用户标识（UnionID/OpenID）相匹配。

存在如下三种状态，具体可参考[State](account-api-authentication.md#state)：

* 华为账号未登录。
* 华为账号已登录且传入账号的UnionID/OpenID与当前账号一致。
* 华为账号已登录且传入账号的UnionID/OpenID与当前账号不一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [StateRequest](account-api-authentication.md#staterequest) | 是 | 获取华为账号登录状态请求对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[StateResult](account-api-authentication.md#stateresult)> | Promise对象，返回[StateResult](account-api-authentication.md#stateresult)对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1001502003](errorcode-account-kit.md#section1001502003-输入参数值无效) | Invalid input parameter value. |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const stateRequest: authentication.StateRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>' // 该值可以通过华为账号登录接口获取
};
try {
  // 执行获取华为账号登录状态请求，并处理结果
  new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
    const state = data.state;
    // 处理state
  }).catch((error: BusinessError) => {
    dealAllError(error);
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
}
```

### getMobileNumberConsistency

getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>

获取手机号一致性状态，使用Promise异步回调。该方法可用于校验应用通过[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)获取的手机号是否与华为账号绑定的手机号、本机SIM卡一致。

开发者可创建请求对象[ConsistencyRequest](account-api-authentication.md#consistencyrequest)，将已获取的手机号、用户标识（UnionID/OpenID）传入。Account Kit会判断开发者传入的手机号、华为账号绑定手机号、当前设备SIM卡之间的关系。

存在如下三种一致性状态，具体可参考[ConsistencyState](account-api-authentication.md#consistencystate)：

* 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号一致。
* 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号均不一致或当前设备无SIM卡。
* 华为账号已登录，传入的手机号与当前账号绑定的手机号不一致。

开发者在使用获取手机号一致性状态方法前，需要完成quickLoginMobilePhone（华为账号一键登录）的账号权限申请，详情参见[开发前提](../harmonyos-guides/account-phone-unionid-login.md#开发前提)。账号权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**设备行为差异：** 对于6.1.1(24)及之前版本，该接口在Phone、PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。对于26.0.0及之后版本，该接口在Phone、PC/2in1、Tablet、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ConsistencyRequest](account-api-authentication.md#consistencyrequest) | 是 | 获取手机号一致性状态请求对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ConsistencyResult](account-api-authentication.md#consistencyresult)> | Promise对象，返回[ConsistencyResult](account-api-authentication.md#consistencyresult)对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. Function getMobileNumberConsistency can not work correctly due to limited device capabilities.  适用版本：5.1.0(18)+ |
| [1001500001](errorcode-account-kit.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001500004](errorcode-account-kit.md#section1001500004-已登录的华为账号不支持该功能) | The account does not support this function. |
| [1001500005](errorcode-account-kit.md#section1001500005-该功能被限制调用) | This function is restricted from being called. |
| [1001502001](errorcode-account-kit.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](errorcode-account-kit.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502005](errorcode-account-kit.md#section1001502005-网络错误) | Network error. |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error. |
| [1001502014](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建请求参数
const consistencyRequest: authentication.ConsistencyRequest = {
  idType: authentication.IdType.UNION_ID,
  idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
  mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
};
try {
  // 执行获取手机号一致性状态请求，并处理结果
  new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
    .then((data: authentication.ConsistencyResult) => {
      hilog.info(0x0000, 'testTag', `Succeeded in getting getMobileNumberConsistency result = ${data.state}`);
      const state = data.state;
      // 处理state
    })
    .catch((err: BusinessError) => {
      dealAllError(err);
    });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag',
    `Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}`);
}
```

## LoginWithHuaweiIDRequest

华为账号登录请求类。

开发者可将请求类对象作为入参，通过调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行华为账号登录请求，成功时返回[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)登录响应对象，用于获取用户标识（UnionID/OpenID）。

可通过修改该类的属性以控制是否拉起华为账号登录页面、完善业务的安全校验逻辑，具体方式可参考其属性介绍。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** LoginWithHuaweiIDRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| forceLogin | boolean | 否 | 是 | 表示当**系统未登录华为账号**时，是否需要拉起华为账号登录页。  - true：将拉起华为账号登录页。  - false：将返回[1001502001 用户未登录华为账号](errorcode-account-kit.md#section1001502001-用户未登录华为账号)。  如果**系统已登录华为账号**，则不管该值为true或false，均不会拉起华为账号登录页。  默认值：true。 |
| state | string | 否 | 是 | 请求中的state，通过与响应中的state比较，可校验是否是当前请求，用于防止跨站攻击。  支持字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  如该属性未传、传空，[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)中则不会包含属性state。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |
| nonce | string | 否 | 是 | 请求中的nonce，通过与响应中的ID Token包含的nonce比较，可校验是否是当前请求，用于防止重放攻击。  支持字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  如该属性未传、传空，ID Token中nonce默认值：“default”。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |
| idTokenSignAlgorithm | [IdTokenSignAlgorithm](account-api-authentication.md#idtokensignalgorithm) | 否 | 是 | ID Token签名算法类型。开发者可根据实际安全要求、性能、系统环境兼容性进行选择。  默认值：PS256。 |

**示例：**

参见[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)。

## IdTokenSignAlgorithm

ID Token签名算法类型枚举。根据IdTokenSignAlgorithm的不同类型，对ID Token进行不同方式的加密。请应用根据实际安全要求、性能、系统环境兼容性进行选择。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PS256 | 1 | RSASSA-PSS使用SHA-256和基于SHA-256的MGF1。为保证安全性建议使用PS256。 |
| RS256 | 2 | RSASSA-PKCS1-v1\_5使用SHA-256。 |

**示例：**

参见[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)。

## LoginWithHuaweiIDResponse

华为账号登录响应类，包含了属性data和state。属性data为华为账号登录凭据对象，用于获取授权码、用户标识（UnionID/OpenID）等数据；属性state则用于防止跨站攻击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** LoginWithHuaweiIDResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| data | [LoginWithHuaweiIDCredential](account-api-authentication.md#loginwithhuaweiidcredential) | 是 | 是 | 华为账号登录凭据对象。包含用户授权码Authorization Code、用户标识（UnionID/OpenID）等数据。 |
| state | string | 是 | 是 | 响应中的state，通过与请求中的state比较，可校验是否是当前请求，用于防止跨站攻击。  字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255。校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。 |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建登录请求，并设置参数
const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
// 默认值为true，若账号未登录则强制拉起账号登录页
loginRequest.forceLogin = true;
loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击

// 执行登录请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
    const state = loginWithHuaweiIDResponse.state;
    // state为空时，归一化处理为空字符串
    const normalizedRequestState = loginRequest.state || '';
    const normalizedState = state || '';
    if (normalizedRequestState !== normalizedState) {
      // state不一致，可能为跨站攻击，需重新登录
      hilog.error(0x0000, 'testTag', `Failed to login. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in login.');
    const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
    const authorizationCode = loginWithHuaweiIDCredential?.authorizationCode;
    const idToken = loginWithHuaweiIDCredential?.idToken;
    // 开发者处理authorizationCode, idToken
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
  // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络错误，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
    // 登录失败，请尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试或者尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 应用登录失败，请尝试使用其他方式登录
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 内部错误
  ERROR_CODE_INTERNAL_ERROR = 1001502009,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

## LoginWithHuaweiIDCredential

华为账号登录凭据。登录成功后返回的凭据结构体，可用于获取授权码Authorization Code、用户标识（UnionID/OpenID）等数据。

推荐使用Authorization Code，通过应用服务端与华为账号服务端交互获取UnionID/OpenID，可有效防范数据拦截、泄露等安全风险，交互流程可参考[登录华为账号](account-api-authentication.md#登录华为账号)。此外，该类型同时也包含了属性OpenID、UnionID，开发者若选择直接使用，需自行保障数据安全。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authorizationCode | string | 是 | 是 | Authorization Code授权码。用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。 |
| idToken | string | 是 | 是 | ID Token。用户身份凭证，JWT格式的字符串，包含用户信息。JSON Web Token（JWT）是一个开放标准（RFC 7519），定义了一种安全传输信息的方法，具体请参见[jwt.io](https://jwt.io/)。用于获取部分用户相关信息及验证签名，可参考[ID Token的使用场景与使用方法](../harmonyos-guides/account-faq-12.md)。长度限制1-2048。 |
| openID | string | 是 | 否 | OpenID。华为账号用户在应用/元服务的唯一标识。同一个用户在不同应用下，其OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| unionID | string | 是 | 否 | UnionID。华为账号用户在同一个开发者账号下的唯一标识。同一个用户，在同一个开发者账号的不同应用下，其UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

**示例：**

参见[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)。

## AuthorizationWithHuaweiIDRequest

华为账号授权请求类。

开发者可将请求类对象作为入参，通过调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行华为账号授权请求，成功时返回[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)授权响应对象，用于获取用户授权凭据。

当执行华为账号授权请求且属性forceAuthorization设置为true时，若系统未登录华为账号，会先拉起华为账号登录页面以完成用户登录；若用户已登录华为账号且未授权，则会拉起华为账号授权页面。

可通过修改该类的属性以设置应用需要访问的用户信息范围，也可用于控制是否拉起登录、授权页面，以及完善业务的安全校验逻辑，具体方式可参考其属性介绍。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** AuthorizationWithHuaweiIDRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| scopes | string[] | 否 | 是 | scope列表，scope表示应用需要访问的用户信息范围。开发者可传入不同的scope组合，用于获取用户数据。  scope类型说明及使用限制如下：  - profile：华为账号用户的头像昵称。（元服务从5.1.1(19)开始，支持该scope，并需配合supportAtomicService属性使用）。  - openid：华为账号用户标识OpenID、UnionID。  具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  - phone：华为账号快速验证手机号。  使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-get-phonenumber.md#开发前提)。元服务不能直接调用该接口获取手机号，可参考场景化控件[快速验证手机号Button](../harmonyos-guides/scenario-fusion-button-getphonenumber.md)获取。儿童账号的手机号无法通过该scope获取。  - quickLoginAnonymousPhone：华为账号绑定的匿名手机号。用于[华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)，需在页面展示匿名手机号，供用户确认信息。  使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-phone-unionid-login.md#开发前提)。该scope只能与openid同时使用，Wearable设备以及海外账号无法获取到手机号，会报[1001500003 不支持该scopes或permissions](errorcode-account-kit.md#section1001500003-不支持该scopes或permissions)。  **说明：** 中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）匿名手机号的返回格式不包含国际电话区号，其他国家和地区默认包含国际电话区号。  - riskLevel：华为账号用户风险等级。  使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-get-risklevel-on-demand-acquisition.md#开发前提)。该scope仅支持与openid、phone、profile组合使用。海外账号不支持获取用户风险等级。  **说明：** 元服务场景下，此scope不支持与phone组合使用，如果需要同时获取手机号和风险等级可参见Scenario Fusion Kit的场景化控件[获取手机号和风险等级Button](../harmonyos-guides/scenario-fusion-button-get-risklevel.md)。  - realNameAgeRange：华为账号用户的实名年龄段，使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-get-realname-age.md#开发前提)。  scopes与permissions属性不能同时为空，否则会返回[1001502003 输入参数值无效](errorcode-account-kit.md#section1001502003-输入参数值无效)错误码。如果传入不合法的scope（例如空值等）则直接返回OpenID、UnionID。  默认值：['openid']。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| permissions | string[] | 否 | 是 | permission列表，用于获取用户授权码和用户身份凭证。  permission取值范围：  - serviceauthcode：代表用户授权码。若permissions属性中包含该类型，则会在响应结构体[authorizationCode](account-api-authentication.md#authorizationwithhuaweiidcredential)中返回用户授权码Authorization Code。  - idtoken：代表用户身份凭证。若permissions属性中包含该类型，则会在响应结构体[idToken](account-api-authentication.md#authorizationwithhuaweiidcredential)中返回用户身份凭证ID Token。  使用限制：  - 与scopes属性不能同时为空，否则会返回[1001502003 输入参数值无效](errorcode-account-kit.md#section1001502003-输入参数值无效)错误码。如果传入不合法的permission（例如空值等）则直接返回OpenID、UnionID。  默认值为空，不返回授权码和用户身份凭证。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| forceAuthorization | boolean | 否 | 是 | 表示华为账号未登录、未授权时，是否需要拉起页面完成登录、授权。  - true：将会拉起页面完成登录、授权。  - false：若未登录，将返回[1001502001 用户未登录华为账号](errorcode-account-kit.md#section1001502001-用户未登录华为账号)；若已登录但未授权，将返回[1001502002 应用未授权](errorcode-account-kit.md#section1001502002-应用未授权)。  默认值：true。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| state | string | 否 | 是 | 请求中的state，通过与响应中的state比较，可校验是否是当前请求，用于防止跨站攻击。  支持字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  如该属性未传、传空，[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)中则不会包含属性state。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| nonce | string | 否 | 是 | 请求中的nonce，通过与响应中的ID Token包含的nonce比较，可校验是否是当前请求，用于防止重放攻击。  支持字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  如该属性未传、传空，ID Token中nonce默认值：“default”。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| idTokenSignAlgorithm | [IdTokenSignAlgorithm](account-api-authentication.md#idtokensignalgorithm) | 否 | 是 | ID Token签名算法类型，具体可参考 [IdTokenSignAlgorithm](account-api-authentication.md#idtokensignalgorithm)。开发者可根据实际安全要求、性能、系统环境兼容性进行选择。  默认值：PS256。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| supportAtomicService | boolean | 否 | 是 | 是否支持元服务。在元服务调用场景下，当传入scopes包含profile时，是否支持获取用户头像昵称。  - 如果该值为true，可以正常获取用户头像昵称。  - 如果该值为false，执行授权请求将返回[1001500003 不支持该scopes或permissions](errorcode-account-kit.md#section1001500003-不支持该scopes或permissions)。  默认值：false。  **起始版本：** 5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。  **说明：** 用于元服务场景调用。 |

**示例：**

参见[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)。

## AuthorizationWithHuaweiIDResponse

华为账号授权响应类，包含了属性data和state。属性data为用户授权凭据对象，用于获取授权码、用户信息等数据；属性state则用于防止跨站攻击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** AuthorizationWithHuaweiIDResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| data | [AuthorizationWithHuaweiIDCredential](account-api-authentication.md#authorizationwithhuaweiidcredential) | 是 | 是 | 华为账号授权凭据。包含用户授权码、用户信息等。 |
| state | string | 是 | 是 | 响应中的state，通过与请求中的state比较，可校验是否是当前请求，用于防止跨站攻击。  字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255。校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。 |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    // state为空时，归一化处理为空字符串
    const normalizedRequestState = authRequest.state || '';
    const normalizedState = state || '';
    if (normalizedRequestState !== normalizedState) {
      // state不一致，可能为跨站攻击，需重新授权
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    // 开发者处理authorizationCode, idToken等信息
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络错误，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

## AuthorizationWithHuaweiIDCredential

华为账号授权凭据。授权成功后返回的结构体，可用于获取授权码、用户信息（例如头像昵称、邮箱、匿名手机号）等数据。

推荐使用Authorization Code，通过应用服务端与华为账号服务端交互获取用户信息，可有效防范数据拦截、泄露等安全风险，交互流程可参考[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)。此外，该接口同时也包含了部分用户信息，开发者若选择直接使用，需自行保障数据安全。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authorizationCode | string | 是 | 是 | Authorization Code授权码。用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的permissions中包含'serviceauthcode'时返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| idToken | string | 是 | 是 | ID Token。用户身份凭证，JWT格式的字符串，包含用户信息，用于获取部分用户相关信息及验证签名，可参考[ID Token的使用场景与使用方法](../harmonyos-guides/account-faq-12.md)。长度限制1-2048。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的permissions中包含'idtoken'时返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| openID | string | 是 | 是 | OpenID。华为账号用户在应用/元服务的唯一标识。同一个用户在不同应用下，其OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：默认返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| unionID | string | 是 | 是 | UnionID。华为账号用户在同一个开发者账号下的唯一标识。同一个用户，在同一个开发者账号的不同应用下，其UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：默认返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| avatarUri | string | 是 | 是 | 用户头像链接，当用户更新头像后，原链接会立即失效。为确保头像正常显示，建议先将头像下载保存后再使用，避免因用户头像链接失效而影响业务流程。  没有长度限制，格式例如：https://xxx/xxx。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中包含'profile'时返回。  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| nickName | string | 是 | 是 | 用户昵称。长度限制2-20个字符。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中包含'profile'时返回。  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| email | string | 是 | 是 | 用户邮箱。长度限制4-254。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中包含'email'时返回。  **说明：** 元服务不支持该字段。 |
| authorizedScopes | string[] | 是 | 是 | 本次授权成功的scope集合。当存在多个scope时，用户可选择部分scope进行授权，该属性即会返回授权成功的scope集合。通过授权成功后返回Authorization Code来获取对应用户信息，可参考[获取用户信息](../harmonyos-guides/account-get-user-info-overview.md)。  **返回场景**：默认返回'openid'，若用户授权其他scope，则会返回所有授权成功的socpe。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| extraInfo | Record<string, Object> | 是 | 是 | 扩展信息。目前支持key值如下：  - quickLoginAnonymousPhone：一键登录匿名手机号。当[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中包含'quickLoginAnonymousPhone'时返回。  - localNumberConsistency：本地号卡一致性状态。[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中包含'quickLoginAnonymousPhone'时返回。  true：华为账号绑定的手机号与当前设备任意一个SIM卡手机号一致。  false：华为账号绑定的手机号与当前设备任意一个SIM卡手机号均不一致，或当前设备无SIM卡。  如果开发者开启了[代码混淆](../harmonyos-guides/source-obfuscation-guide.md)需要配置混淆白名单防止其中包含的属性被混淆。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**  - 在4.1.0(11)及之前版本，参数类型为object。  - 从5.0.0(12)版本开始，参数类型为Record<string, Object>。 |

**示例：**

参见[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)。

## CancelAuthorizationRequest

取消授权请求类。该类包含了属性state，用于防止跨站攻击。开发者可将请求类对象作为入参，通过调用[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)方法执行取消授权请求，主动解除用户授予应用的用户信息访问权限。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** CancelAuthorizationRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | string | 否 | 是 | 请求中的state，通过与响应中的state比较，可校验是否是当前请求，用于防止跨站攻击。  支持字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

**示例：**

参见[CancelAuthorizationResponse](account-api-authentication.md#cancelauthorizationresponse)。

## CancelAuthorizationResponse

取消授权响应类。该类包含了属性state，用于防止跨站攻击。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** CancelAuthorizationResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | string | 是 | 是 | 响应中的state，通过与请求中的state比较，可校验是否是当前请求，用于防止跨站攻击。字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。 |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建取消授权请求，并设置参数
const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
cancelRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击

// 执行取消授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(cancelRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const cancelAuthorizationResponse = data as authentication.CancelAuthorizationResponse;
    const state = cancelAuthorizationResponse.state;
    // state为空时，归一化处理为空字符串
    const normalizedRequestState = cancelRequest.state || '';
    const normalizedState = state || '';
    if (normalizedRequestState !== normalizedState) {
      // state不一致，可能为跨站攻击，需重新取消授权
      hilog.error(0x0000, 'testTag', `Failed to cancel. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in canceling.');
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to cancel. Code: ${error.code}, message: ${error.message}`);
  // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络错误，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
    // 登录失败，请尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试或者尝试使用其他方式登录
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 应用登录失败，请尝试使用其他方式登录
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 内部错误
  ERROR_CODE_INTERNAL_ERROR = 1001502009,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

## AuthenticationErrorCode

华为账号认证服务接口错误码枚举。应用可根据如下错误码进行不同的处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001500001](errorcode-account-kit.md#section1001500001-应用指纹证书校验失败) | 应用指纹证书校验失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| DUPLICATE\_REQUEST\_REJECTED | [1001500002](errorcode-account-kit.md#section1001500002-重复请求) | 重复请求，当已有相同的请求在处理时，返回此错误码，此错误码不需要处理。应用需实现点击控制，防止连续点击发起相同请求。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCOPE\_OR\_PERRMISSION\_UNSUPPORTED | [1001500003](errorcode-account-kit.md#section1001500003-不支持该scopes或permissions) | 不支持该scopes或permissions。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| UNSUPPORTED | [1001500004](errorcode-account-kit.md#section1001500004-已登录的华为账号不支持该功能) | 已登录的华为账号不支持该功能。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| REQUEST\_RESTRICTED | [1001500005](errorcode-account-kit.md#section1001500005-该功能被限制调用) | 该功能被限制调用。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001502001](errorcode-account-kit.md#section1001502001-用户未登录华为账号) | 用户未登录华为账号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| APP\_NOT\_AUTHORIZED | [1001502002](errorcode-account-kit.md#section1001502002-应用未授权) | 应用未授权。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PARAMETER\_INVALID | [1001502003](errorcode-account-kit.md#section1001502003-输入参数值无效) | 输入参数值无效，接口传参异常等。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NETWORK\_ERROR | [1001502005](errorcode-account-kit.md#section1001502005-网络错误) | 网络错误。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| INTERNAL\_ERROR | [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | 内部错误，如华为账号服务器错误或其他内部错误等。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| USER\_CANCELED | [1001502012](errorcode-account-kit.md#section1001502012-用户取消授权) | 用户取消授权。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED | [1001502014](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限) | 应用未申请scopes或permissions权限。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |

## AuthenticationController

华为账号服务的控制器类，负责接收并执行华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）、授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）、取消授权（[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)）请求。开发者可将[HuaweiIDProvider](account-api-authentication.md#huaweiidprovider)工厂类创建的请求对象作为入参，调用[executeRequest](account-api-authentication.md#executerequest-1)方法请求华为账号服务。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

### constructor

constructor(context?: common.Context)

控制器类构造器，用于构造AuthenticationController实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 否 | Context上下文，当需要拉起华为账号登录、授权页面时必须传该参数，否则会报[401](errorcode-universal.md#section401-参数检查失败)参数检查失败错误码。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |

**示例：**

参见[AuthenticationController.executeRequest](account-api-authentication.md#executerequest-1)。

### executeRequest

executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void

执行请求方法，AuthenticationController类成员函数，使用callback异步回调。该方法用于接收并执行华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）、授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）、取消授权（[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)）请求，并返回华为账号登录（[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)）、授权（[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)）、取消授权（[CancelAuthorizationResponse](account-api-authentication.md#cancelauthorizationresponse)）响应结果。

通过[createLoginWithHuaweiIDRequest](account-api-authentication.md#createloginwithhuaweiidrequest)、[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)、[createCancelAuthorizationRequest](account-api-authentication.md#createcancelauthorizationrequest)构造请求对象后，使用该方法执行请求。

**说明** 

通过该接口执行华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）或授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）请求、且属性forceLogin或forceAuthorization设置为true时，若系统未登录华为账号，则会拉起华为账号登录页面；若已登录且用户未对应用授权，则会拉起华为账号授权页面。用户在页面中可长时间停留，完成登录/授权后，Account Kit才会向应用返回成功结果，其他场景（如用户点击关闭页面）则返回对应的错误码。开发者可根据此规则，合理规划接口的调用时机，避免因接口长时间未返回结果而导致业务逻辑阻塞。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [AuthenticationRequest](account-api-authentication.md#authenticationrequest) | 是 | 华为账号认证服务请求对象。 |
| callback | AsyncCallback<[AuthenticationResponse](account-api-authentication.md#authenticationresponse), Record<string, Object>> | 是 | 执行华为账号认证服务回调函数。  当获取响应数据成功，err为undefined，data为[AuthenticationResponse](account-api-authentication.md#authenticationresponse)对象；否则为错误对象。  **说明：**  - 在4.1.0(11)及之前版本，参数类型为AsyncCallback<[AuthenticationResponse](account-api-authentication.md#authenticationresponse), { [key: string]: Object }>。  - 从5.0.0(12)版本开始，参数类型为AsyncCallback<[AuthenticationResponse](account-api-authentication.md#authenticationresponse), Record<string, Object>>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[账号管理错误码](errorcode-account.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [12300002](errorcode-account.md#section12300002-无效参数) | Invalid parameter.  适用版本：4.0.0(10)-4.1.0(11) |
| [1001500001](errorcode-account-kit.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle.  适用版本：5.0.0(12)+ |
| [1001500002](errorcode-account-kit.md#section1001500002-重复请求) | This error code is reported when a request is already being processed.  适用版本：5.0.0(12)+ |
| [1001500003](errorcode-account-kit.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported.  适用版本：5.0.0(12)+ |
| [1001502001](errorcode-account-kit.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID.  适用版本：5.0.0(12)+ |
| [1001502002](errorcode-account-kit.md#section1001502002-应用未授权) | The application is not authorized.  适用版本：5.0.0(12)+ |
| [1001502003](errorcode-account-kit.md#section1001502003-输入参数值无效) | Invalid input parameter value.  适用版本：5.0.0(12)+ |
| [1001502005](errorcode-account-kit.md#section1001502005-网络错误) | Network error.  适用版本：5.0.0(12)+ |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error.  适用版本：5.0.0(12)+ |
| [1001502012](errorcode-account-kit.md#section1001502012-用户取消授权) | The user canceled the authorization.  适用版本：5.0.0(12)+ |
| [1001502014](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions.  适用版本：5.0.0(12)+ |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
    if (error) {
      dealAllError(error);
      return;
    }
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    // state为空时，归一化处理为空字符串
    const normalizedRequestState = authRequest.state || '';
    const normalizedState = state || '';
    if (normalizedRequestState !== normalizedState) {
      // state不一致，可能为跨站攻击，需重新授权
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    // 开发者处理authorizationCode, idToken等信息
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络错误，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

### executeRequest

executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>

执行请求方法，AuthenticationController类成员函数，使用callback异步回调。该方法用于接收并执行华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）、授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）、取消授权（[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)）请求，并返回华为账号登录（[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)）、授权（[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)）、取消授权（[CancelAuthorizationResponse](account-api-authentication.md#cancelauthorizationresponse)）响应结果。 使用Promise异步回调。

通过[createLoginWithHuaweiIDRequest](account-api-authentication.md#createloginwithhuaweiidrequest)、[createAuthorizationWithHuaweiIDRequest](account-api-authentication.md#createauthorizationwithhuaweiidrequest)、[createCancelAuthorizationRequest](account-api-authentication.md#createcancelauthorizationrequest)构造请求对象后，使用该方法执行请求。

**说明** 

通过该接口执行华为账号登录（[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)）或授权（[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)）请求、且属性forceLogin或forceAuthorization设置为true时，若系统未登录华为账号，则会拉起华为账号登录页面；若已登录且用户未对应用授权，则会拉起华为账号授权页面。用户在页面中可长时间停留，完成登录/授权后，Account Kit才会向应用返回成功结果，其他场景（如用户点击关闭）则返回对应的错误码。开发者可根据此规则，合理规划接口的调用时机，避免因接口长时间未返回结果而导致业务逻辑阻塞。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [AuthenticationRequest](account-api-authentication.md#authenticationrequest) | 是 | 华为账号认证服务请求对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthenticationResponse](account-api-authentication.md#authenticationresponse)> | Promise对象，返回[AuthenticationResponse](account-api-authentication.md#authenticationresponse)对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[账号管理错误码](errorcode-account.md)和[ArkTS错误码](errorcode-account-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [12300002](errorcode-account.md#section12300002-无效参数) | Invalid parameter.  适用版本：4.0.0(10)-4.1.0(11) |
| [1001500001](errorcode-account-kit.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle.  适用版本：5.0.0(12)+ |
| [1001500002](errorcode-account-kit.md#section1001500002-重复请求) | This error code is reported when a request is already being processed.  适用版本：5.0.0(12)+ |
| [1001500003](errorcode-account-kit.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported.  适用版本：5.0.0(12)+ |
| [1001502001](errorcode-account-kit.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID.  适用版本：5.0.0(12)+ |
| [1001502002](errorcode-account-kit.md#section1001502002-应用未授权) | The application is not authorized.  适用版本：5.0.0(12)+ |
| [1001502003](errorcode-account-kit.md#section1001502003-输入参数值无效) | Invalid input parameter value.  适用版本：5.0.0(12)+ |
| [1001502005](errorcode-account-kit.md#section1001502005-网络错误) | Network error.  适用版本：5.0.0(12)+ |
| [1001502009](errorcode-account-kit.md#section1001502009-内部错误) | Internal error.  适用版本：5.0.0(12)+ |
| [1001502012](errorcode-account-kit.md#section1001502012-用户取消授权) | The user canceled the authorization.  适用版本：5.0.0(12)+ |
| [1001502014](errorcode-account-kit.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions.  适用版本：5.0.0(12)+ |

**示例：**

```typescript
import { authentication } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
authRequest.scopes = ['openid'];
authRequest.permissions = ['idtoken', 'serviceauthcode'];
authRequest.forceAuthorization = true;
authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

// 执行授权请求，并处理结果
try {
  // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
  const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
  controller.executeRequest(authRequest).then((data) => {
    const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
    const state = authorizationWithHuaweiIDResponse.state;
    // state为空时，归一化处理为空字符串
    const normalizedRequestState = authRequest.state || '';
    const normalizedState = state || '';
    if (normalizedRequestState !== normalizedState) {
      // state不一致，可能为跨站攻击，需重新授权
      hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
      return;
    }
    hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
    const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
    const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
    const idToken = authorizationWithHuaweiIDCredential?.idToken;
    // 开发者处理authorizationCode, idToken等信息
  }).catch((err: BusinessError) => {
    dealAllError(err);
  });
} catch (error) {
  dealAllError(error);
}

// 错误处理
function dealAllError(error: BusinessError): void {
  hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
  // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
  if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
    // 用户未登录华为账号，请登录华为账号并重试
  } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
    // 网络错误，请检查当前网络状态并重试
  } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
    // 用户取消授权
  } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
    // 系统服务异常，请稍后重试
  } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
    // 重复请求，应用无需处理
  } else {
    // 获取用户信息失败，请稍后重试
  }
}

export enum ErrorCode {
  // 账号未登录
  ERROR_CODE_LOGIN_OUT = 1001502001,
  // 网络错误
  ERROR_CODE_NETWORK_ERROR = 1001502005,
  // 用户取消授权
  ERROR_CODE_USER_CANCEL = 1001502012,
  // 系统服务异常
  ERROR_CODE_SYSTEM_SERVICE = 12300001,
  // 重复请求
  ERROR_CODE_REQUEST_REFUSE = 1001500002
}
```

## AuthenticationRequest

华为账号认证请求抽象基类。该类不包含实际业务属性，具体认证请求请参考其派生类。派生类包含[LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest)、[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)、[CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## AuthenticationResponse

华为账号认证响应抽象基类。该类不包含实际业务属性，具体响应结果请参考其派生类。派生类包含[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)、[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)、[CancelAuthorizationResponse](account-api-authentication.md#cancelauthorizationresponse)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## AuthenticationProvider

华为账号认证工厂抽象基类。该类不包含实际业务属性，具体实现请参考其派生类。派生类包含[HuaweiIDProvider](account-api-authentication.md#huaweiidprovider)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## IdType

华为账号用户标识类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| USER\_ID | 1 | 华为账号用户的UID。  **说明：** 该参数仅对系统应用开放。 |
| OPEN\_ID | 2 | 华为账号用户的OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| UNION\_ID | 3 | 华为账号用户的UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

## State

华为账号登录状态类型枚举。标识系统是否已登录华为账号、已登录的华为账号是否与开发者传入的用户标识（UnionID/OpenID）相一致。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| UNLOGGED\_IN | 0 | 华为账号未登录。 |
| AUTHORIZED | 1 | 华为账号已登录且传入账号的UnionID/OpenID与当前账号一致。 |
| UNAUTHORIZED | 2 | 华为账号已登录且传入账号的UnionID/OpenID与当前账号不一致。 |

## StateRequest

获取华为账号登录状态请求。请求需包含idType、idValue属性，用于指定华为账号用户标识类型并传入实际的用户标识（UnionID/OpenID）。将该请求对象作为入参，通过调用[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)方法，即可判断系统是否已登录华为账号、已登录的华为账号是否与开发者传入的用户标识相匹配。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-authentication.md#idtype) | 否 | 否 | 华为账号用户标识类型。当前非系统应用仅支持设置：IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 华为账号用户标识UnionID/OpenID值。用户标识类型通过idType属性定义。该属性不可为空，否则会报[1001502003 输入参数值无效](errorcode-account-kit.md#section1001502003-输入参数值无效)错误码。长度限制1-256。  UnionID、OpenID值可以通过[华为账号登录](account-api-authentication.md#登录华为账号)、[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)、[华为账号Panel登录组件](account-api-loginpanel.md#loginpanel)或[华为账号Button登录组件](account-api-huawei-id-button.md#loginwithhuaweiidbutton)获取。 |

**示例：**

参见[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)。

## StateResult

获取华为账号登录状态响应。[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)方法返回值。标识系统是否已登录华为账号、已登录的华为账号是否与开发者传入的用户标识（UnionID/OpenID）相匹配。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | [State](account-api-authentication.md#state) | 否 | 否 | 华为账号登录状态。 |

**示例：**

参见[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)。

## ConsistencyState

手机号一致性状态枚举。标识开发者传入的手机号、华为账号绑定手机号、当前设备SIM卡之间的关系。应用可根据结果进行相应风控处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| CONSISTENT | 0 | 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号一致。 |
| INCONSISTENT\_WITH\_DEVICES | 1 | 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号均不一致或当前设备无SIM卡。 |
| INCONSISTENT | 2 | 华为账号已登录，传入的手机号与当前账号绑定的手机号不一致。 |

## ConsistencyRequest

获取手机号一致性状态请求。请求需包含idType、idValue、mobileNumber属性。用于指定华为账号用户标识类型（UnionID/OpenID）、传入实际的用户标识UnionID/OpenID值以及手机号。将请求对象作为入参，通过调用[getMobileNumberConsistency](account-api-authentication.md#getmobilenumberconsistency)方法，即可获取开发者传入的手机号、华为账号绑定手机号、当前设备SIM卡之间的关系。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-authentication.md#idtype) | 否 | 否 | 华为账号用户标识类型。当前非系统应用仅支持设置：IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 华为账号用户标识UnionID/OpenID值。用户标识类型通过idType属性定义。长度限制1-256。  UnionID、OpenID值可以通过[华为账号登录](account-api-authentication.md#登录华为账号)、[获取华为账号用户信息](account-api-authentication.md#获取华为账号用户信息)、[华为账号Panel登录组件](account-api-loginpanel.md#loginpanel)或[华为账号Button登录组件](account-api-huawei-id-button.md#loginwithhuaweiidbutton)获取。 |
| mobileNumber | string | 否 | 否 | 手机号（明文）。通过[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)组件的一键登录功能获取到的手机号，传入完整的手机号需要添加国家码，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）为+86。手机号示例：+86xxxxxxxxxxx（明文手机号）。  长度限制1-256。 |

**示例：**

参见[getMobileNumberConsistency](account-api-authentication.md#getmobilenumberconsistency)。

## ConsistencyResult

获取手机号一致性状态响应。[getMobileNumberConsistency](account-api-authentication.md#getmobilenumberconsistency)方法返回值。标识开发者传入的手机号、华为账号绑定手机号、当前设备SIM卡之间的关系。应用可根据结果进行相应风控处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | [ConsistencyState](account-api-authentication.md#consistencystate) | 否 | 否 | 手机号一致性状态。 |

**示例：**

参见[getMobileNumberConsistency](account-api-authentication.md#getmobilenumberconsistency)。
