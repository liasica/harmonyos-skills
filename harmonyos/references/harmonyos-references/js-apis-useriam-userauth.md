---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth
title: "@ohos.userIAM.userAuth (用户认证)"
breadcrumb: API参考 > 系统 > 安全 > User Authentication Kit（用户认证服务） > ArkTS API > @ohos.userIAM.userAuth (用户认证)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:48+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:94bb198cd0dfb5fa491eba893d4762fc54313c93b2ee04b4a45dd338e1bef00e
---

**userAuth**模块是HarmonyOS系统中用于用户身份认证的核心模块，提供了设备解锁、支付验证、应用登录等场景下的身份认证能力。

该模块支持多种生物特征认证方式（人脸、指纹）和密码认证（PIN），并提供不同级别的安全信任等级。从API版本26.0.0开始，新增伴随设备认证的方式。

该模块主要用于以下场景：

* 设备解锁认证。
* 金融支付验证。
* 应用登录保护。
* 敏感操作确认。

**说明** 

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 关键Class/Interface介绍

### 核心枚举类型

* **[UserAuthType](js-apis-useriam-userauth.md#userauthtype8)**：认证类型枚举（PIN、FACE、FINGERPRINT、COMPANION\_DEVICE）。
* **[AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8)**：认证信任级别枚举（ATL1-ATL4）。
* **[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)**：认证结果码枚举。
* **[ReuseMode](js-apis-useriam-userauth.md#reusemode12)**：认证结果复用模式枚举。
* **[UserAuthTipCode](js-apis-useriam-userauth.md#userauthtipcode20)**：认证提示码枚举。

### 核心接口类型

* **[AuthParam](js-apis-useriam-userauth.md#authparam10)**：认证参数接口，包含挑战值、认证类型列表、信任级别、复用信息等。
* **[WidgetParam](js-apis-useriam-userauth.md#widgetparam10)**：认证组件显示参数接口，包含标题、导航按钮文本、窗口模式等。
* **[UserAuthResult](js-apis-useriam-userauth.md#userauthresult10)**：认证结果接口，包含结果码、认证令牌、认证类型等。
* **[ReuseUnlockResult](js-apis-useriam-userauth.md#reuseunlockresult12)**：认证结果复用信息接口。
* **[EnrolledState](js-apis-useriam-userauth.md#enrolledstate12)**：已注册凭据状态接口。
* **[AuthLockState](js-apis-useriam-userauth.md#authlockstate22)**：认证锁定状态接口。

### 核心类

* **[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)**：用户认证实例类，提供认证执行、取消、事件订阅等能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/hRthrbClQzuWOfeQZg1cVg/zh-cn_image_0000002706836726.png)

## API组合使用关系说明

使用userAuth模块进行身份认证的典型流程如下：

```ts
// 以下为阐述调用逻辑的伪代码，仅提供步骤说明，不提供详细的可执行代码。
// 1. 检查认证能力是否可用。
userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);

// 2. 获取认证实例。
let authInstance = userAuth.getUserAuthInstance({
  challenge: new Uint8Array([]), // challenge用于防止重放攻击，必须使用安全随机数生成器获取。
  authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
  authTrustLevel: userAuth.AuthTrustLevel.ATL3
});

// 3. 订阅认证结果事件。
authInstance.on('result', (result: userAuth.UserAuthResult) => {
  // 处理认证结果。
});

// 4. 订阅认证提示事件（可选）。
authInstance.on('authTip', (tipCode: userAuth.UserAuthTipCode) => {
  // 处理认证提示信息
});

// 5. 开始认证。
authInstance.start();

// 6. 认证完成后取消订阅（可选）。
authInstance.off('result');
authInstance.off('authTip');
```

**查询认证锁定状态流程**：

```javascript
// 以下为阐述调用逻辑的伪代码，仅提供步骤说明，不提供详细的可执行代码。
// 1. 查询认证锁定状态。
let lockState = await userAuth.getAuthLockState(userAuth.UserAuthType.FACE);

// 2. 根据锁定状态决定是否进行认证。
if (!lockState.isLocked) {
  // 执行认证流程。
}
```

## 导入模块

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
```

## 常量

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| MAX\_ALLOWABLE\_REUSE\_DURATION12+ | number | 300000 | 复用解锁认证结果最大有效时长，值为300000毫秒（5分钟）。用于限制认证结果复用的最大时长，防止长时间复用过期的认证结果带来的安全风险。该常量可作为[ReuseUnlockResult](js-apis-useriam-userauth.md#reuseunlockresult12)中reuseDuration参数的最大值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PERMANENT\_LOCKOUT\_DURATION22+ | number | 0x7fffffff | 永久冻结时间，值为0x7fffffff毫秒。当认证不通过次数达到上限后，认证器将进入永久冻结状态，此时需要通过PIN认证才能解锁。该值用于标识认证器的永久冻结状态，可通过[AuthLockState](js-apis-useriam-userauth.md#authlockstate22)的lockoutDuration字段返回。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## AuthLockState22+

认证类型的身份认证冻结状态。该接口用于查询指定认证类型（如人脸、指纹、PIN）当前的冻结状态，包括是否被冻结、剩余尝试次数和冻结时长等信息。当用户多次认证不通过后，认证器可能进入临时冻结或永久冻结状态，应用可根据冻结信息提示用户。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLocked | boolean | 否 | 否 | 表示认证是否已被冻结。true表示已冻结，此时用户无法使用该认证类型进行身份认证；false表示未冻结，用户可以正常使用该认证类型。冻结状态通常由连续多次认证不通过触发。 |
| remainingAuthAttempts | number | 否 | 否 | 认证未被冻结时的剩余尝试次数，最大为5次。每次认证不通过后该值会递减，当降为0时认证器将进入冻结状态。此字段仅在isLocked为false时有效。 |
| lockoutDuration | number | 否 | 否 | 认证被冻结时的剩余冻结时间，单位为毫秒。此字段仅在isLocked为true时有效。  当永久冻结时，值为[PERMANENT\_LOCKOUT\_DURATION](js-apis-useriam-userauth.md#常量)，表示认证器已永久锁定，需要用户通过PIN认证解锁后才能继续使用该认证类型。临时冻结时，该值为实际的剩余冻结时长，冻结结束后用户可继续尝试认证。 |

## UserAuthTipCode20+

表示身份认证中间状态的枚举。该枚举用于描述认证过程中的各种中间状态，包括认证不通过、超时、冻结状态以及认证界面的加载和释放等。应用可通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅这些中间状态，以便在认证过程中提供更精细的用户反馈和状态感知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPARE\_FAILURE | 1 | 认证不通过。表示当前认证尝试失败，用户特征与已注册凭据比对不匹配。此状态会在每次认证不通过时触发，应用可根据此状态提示用户重新尝试。 |
| TIMEOUT | 2 | 认证超时。表示认证操作超时，通常是由于用户在规定时间内未完成认证交互（如未及时输入密码、未正视摄像头等）导致。 |
| TEMPORARILY\_LOCKED | 3 | 临时冻结。表示认证器进入临时冻结状态，用户需等待冻结时长结束后才能继续尝试认证。临时冻结通常由连续多次认证失败触发。 |
| PERMANENTLY\_LOCKED | 4 | 永久冻结。表示认证器进入永久冻结状态，用户无法通过等待自动解锁，必须使用PIN认证解锁后才能继续使用该认证类型。永久冻结通常由临时冻结期间继续尝试认证不通过触发。 |
| WIDGET\_LOADED | 5 | 身份认证界面加载完毕。表示认证控件已成功加载并显示，用户可以开始进行认证交互。应用可在此状态触发后进行界面相关的初始化操作。 |
| WIDGET\_RELEASED | 6 | 当前的身份认证界面退出，切换其他认证界面或身份认证控件关闭。表示认证控件已释放，应用可在此状态触发后进行后续操作，如弹出其他窗口等。在PC/2in1设备上使用模应用弹窗方式认证时，建议订阅此状态以确保控件完全释放后再执行其他界面操作。 |
| COMPARE\_FAILURE\_WITH\_FROZEN | 7 | 认证不通过并触发了认证冻结。表示当前认证不通过，并且失败次数已达到阈值，认证器进入冻结状态。此状态同时包含认证不通过和冻结两个信息，应用可根据冻结类型（临时或永久）提示用户相应的解锁方式。 |

## EnrolledState12+

用户注册凭据的状态。该接口用于描述用户已注册的认证凭据（如人脸、指纹、伴随设备）的当前状态，包括凭据摘要和数量。应用可通过[getEnrolledState](js-apis-useriam-userauth.md#userauthgetenrolledstate12)接口查询凭据状态，用于检测用户凭据是否发生变化（如新增或删除指纹/人脸/伴随设备），以便做出相应的业务处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialDigest | number | 否 | 否 | 注册的凭据摘要，在凭据增加时随机生成。该值用于标识当前注册凭据的版本，当用户新增或删除凭据时该值会变化。应用可保存此值并在后续查询时对比，以判断凭据是否发生变化。  **注意**：当复用认证结果时，如果之前认证使用的凭据已被删除，返回的credentialDigest可能为0。 |
| credentialCount | number | 否 | 否 | 注册的凭据数量。表示当前用户已注册的该类型凭据数量，例如指纹数量或人脸数量。  **注意**：当复用认证结果时，如果之前认证使用的凭据已被删除，返回的credentialCount可能为0。 |

## ReuseMode12+

复用解锁认证结果的模式。该枚举定义了认证结果复用的四种模式，用于控制何种认证结果可以在何种条件下被复用。应用可根据业务场景选择合适的复用模式，以在安全性和用户体验之间取得平衡。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH\_TYPE\_RELEVANT | 1 | 与认证类型相关，只有当设备解锁认证结果在有效时间内，并且设备解锁的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。  例如：用户使用人脸解锁设备后，在有效时间内发起需要人脸认证的业务操作，可直接复用解锁结果；但如果发起需要指纹认证的业务操作，则无法复用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUTH\_TYPE\_IRRELEVANT | 2 | 与认证类型无关，设备解锁认证结果在有效时间内，可以重复使用。  例如：用户使用人脸解锁设备后，在有效时间内发起需要指纹或PIN认证的业务操作，均可直接复用解锁结果，无需再次认证。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT14+ | 3 | 与认证类型相关，任意身份认证（包括设备解锁）结果在有效时间内，并且身份认证的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。  例如：用户在某应用中使用人脸认证完成支付后，在有效时间内另一应用发起需要人脸认证的操作，可复用之前的认证结果；但如果发起需要指纹认证的操作，则无法复用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_IRRELEVANT14+ | 4 | 与认证类型无关，任意身份认证（包括设备解锁）结果在有效时间内，可以重复使用。  例如：用户在某应用中使用人脸认证完成操作后，在有效时间内另一应用发起任意类型的认证操作，均可复用之前的认证结果。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## ReuseUnlockResult12+

复用解锁认证结果。该接口用于配置认证结果复用的相关参数，包括复用模式和有效时长。通过合理配置认证结果复用，可以在保证安全性的前提下提升用户体验，避免用户频繁重复认证。

**说明** 

如果身份认证解锁（包括设备解锁）后，在有效时间内凭据发生了变化，身份认证的结果依然可以复用，认证结果中返回当前实际的EnrolledState。若复用认证结果时，之前认证时所使用的身份认证凭据已经被删除：

* 如果删除的是人脸、指纹，则认证结果依然可以复用，只是返回的EnrolledState中credentialCount和credentialDigest均为0。
* 如果删除的是锁屏口令，则此次复用会失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reuseMode | [ReuseMode](js-apis-useriam-userauth.md#reusemode12) | 否 | 否 | 复用解锁认证结果的模式。根据业务场景的安全需求选择合适的复用模式：  - AUTH\_TYPE\_RELEVANT(1)：仅复用匹配认证类型的设备解锁结果，安全性最高。  - AUTH\_TYPE\_IRRELEVANT(2)：复用任意类型的设备解锁结果，适用于中等安全场景。  - CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT(3)：复用匹配认证类型的任意认证结果，适用于跨应用场景。  - CALLER\_IRRELEVANT\_AUTH\_TYPE\_IRRELEVANT(4)：复用任意认证结果，安全性最低但体验最优。 |
| reuseDuration | number | 否 | 否 | 允许复用解锁认证结果的有效时长，单位为毫秒。有效时长的值应大于0，最大值为[MAX\_ALLOWABLE\_REUSE\_DURATION](js-apis-useriam-userauth.md#常量)（300000毫秒，即5分钟）。建议根据业务场景设置合理的时长：  - 高安全场景（如支付）：建议设置较短时长（如30秒至1分钟）。  - 中等安全场景（如应用登录）：建议设置中等时长（如2至3分钟）。  - 低安全场景（如数据查询）：可使用最大时长。 |

## userAuth.getAuthLockState22+

getAuthLockState(authType: UserAuthType): Promise<AuthLockState>

查询指定认证类型的冻结状态，使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthLockState](js-apis-useriam-userauth.md#authlockstate22)> | Promise对象，当查询成功时，返回值为指定认证类型的身份认证冻结状态。失败时报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500008 | The parameter is out of range. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result: userAuth.AuthLockState) => {
    authLockState = result;
    console.info('get auth lock state successfully.');
  })
  .catch((err: BusinessError) => {
    console.error(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```

## userAuth.getEnrolledState12+

getEnrolledState(authType: UserAuthType): EnrolledState

查询凭据注册的状态，以检测用户注册凭据的变更。该接口用于获取指定认证类型的凭据注册信息，包括凭据摘要和数量。应用可通过对比当前查询结果与之前保存的结果，判断用户是否新增或删除了凭据，从而采取相应的业务处理。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。用于指定查询的凭据类型，支持FACE（人脸）、FINGERPRINT（指纹）、PIN（密码）、COMPANION\_DEVICE（伴随设备）。查询PIN时返回的是密码的整体状态，而非单个密码的数量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EnrolledState](js-apis-useriam-userauth.md#enrolledstate12) | 当查询成功时，返回值为用户注册凭据的状态。包含credentialDigest（凭据摘要）和credentialCount（凭据数量）。应用可保存credentialDigest值，后续查询时对比以检测凭据变更。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
  console.info('get current enrolled state successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}`);
}
```

## AuthParam10+

用户认证相关参数。该接口用于配置用户认证的各项参数，包括挑战值、认证类型列表、认证信任等级、认证结果复用配置等。通过合理配置这些参数，可以满足不同业务场景下的认证需求。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| challenge | Uint8Array | 否 | 否 | 随机挑战值，可用于防重放攻击。最大长度为32字节，可传Uint8Array([])。建议使用[加解密算法库框架](js-apis-cryptoframework.md)生成的随机数作为挑战值，以增强安全性。认证通过后，挑战值会被包含在认证令牌中，业务可通过验证令牌中的挑战值来确认认证结果的有效性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8)[] | 否 | 否 | 认证类型列表，用来指定用户认证界面提供的认证方法。可同时指定多种认证类型，如[UserAuthType.PIN, UserAuthType.FACE, UserAuthType.FINGERPRINT]，用户可选择任意一种完成认证。认证类型的选择会影响认证结果复用的匹配条件。暂不支持同时发起伴随设备认证和其他认证类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 否 | 否 | 期望达到的认证可信等级。认证可信等级决定了认证的安全强度，应根据业务场景的安全需求选择合适的等级：  - ATL1：适用于业务风控、一般个人数据查询等低安全场景。  - ATL2：适用于应用登录、维持设备解锁状态等中等安全场景。  - ATL3：适用于设备解锁等较高安全场景。  - ATL4：适用于小额支付等高安全场景。  典型操作需要的身份认证可信等级，以及身份认证可信等级的划分请参见[认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| reuseUnlockResult12+ | [ReuseUnlockResult](js-apis-useriam-userauth.md#reuseunlockresult12) | 否 | 是 | 表示可以复用解锁认证的结果。配置后，若满足复用条件，系统将直接返回之前的认证结果，无需用户再次进行认证交互。默认为不复用。启用认证结果复用可以提升用户体验，但应根据业务场景的安全需求合理配置复用模式和有效时长。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| skipLockedBiometricAuth20+ | boolean | 否 | 是 | 是否跳过已禁用的认证方式自动切换至其他方式的认证。若无可切换的认证方式则关闭控件，返回认证冻结错误码。  - true：生物认证冻结时，跳过倒计时界面直接切换到其他方式的认证（如从冻结的指纹切换到PIN）。适用于希望快速完成认证的场景。  - false（默认）：不跳过，用户需要等待冻结倒计时结束后才能继续尝试该认证方式或手动切换。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## WidgetParam10+

用户认证界面配置相关参数。该接口用于配置认证界面的显示样式和交互方式，包括标题、导航按钮文本、窗口模式等。通过合理配置这些参数，可以为用户提供清晰的认证引导和良好的交互体验。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 否 | 用户认证界面的标题，建议传入认证目的，例如用于支付、登录应用等，不支持传空字串，最大长度为500字符。标题会显示在认证界面，帮助用户理解当前认证的目的，提升用户信任度和配合度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navigationButtonText | string | 否 | 是 | 导航按键的说明文本，最大长度为60字符。点击该按钮可触发应用自定义的操作，如跳转到自定义认证页面或取消认证等。在单指纹、单人脸场景下支持，从API版本18开始，增加支持人脸+指纹组合认证场景。默认为不展示自定义导航按键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uiContext18+ | Context | 否 | 是 | 以模应用弹窗方式显示身份认证对话框，从API版本18开始，支持在2in1设备上使用。传入有效的uiContext后，认证对话框将以模应用弹窗方式显示，认证结果返回后应用需先获取控件释放消息（订阅[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)并等待收到authTipInfo.tipCode为WIDGET\_RELEASED的回调）才能弹出其他窗口。如果没有此参数或其他类型的设备，身份认证对话框将以模系统弹窗方式显示，此时控件释放后应用可直接进行后续操作。  **默认值：** 以模系统弹窗方式显示身份认证对话框。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## UserAuthResult10+

用户认证结果。认证通过时，返回认证类型和认证通过的令牌信息；认证不通过时，返回相应的错误码。该接口用于描述认证完成后的结果信息，应用可通过[IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10)的onResult回调获取此结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 用户认证结果。若成功返回SUCCESS(12500000)，若失败返回相应错误码。错误码包括：  - FAIL(12500001)：认证不通过。  - CANCELED(12500003)：认证取消。  - TIMEOUT(12500004)：认证超时。  - LOCKED(12500009)：认证器锁定。  - NOT\_ENROLLED(12500010)：未注册凭据。  - PIN\_EXPIRED(12500013)：锁屏密码过期。  完整错误码列表参见[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)。 |
| token | Uint8Array | 否 | 是 | 认证通过时，返回认证通过的令牌信息。令牌最大长度为1024字节，包含用户身份认证的凭证，可用于后续的安全操作验证（如支付确认、敏感数据访问等）。令牌中包含认证时的挑战值，业务可通过验证挑战值来防止重放攻击。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 否 | 是 | 认证通过时，返回实际使用的认证类型。当[AuthParam](js-apis-useriam-userauth.md#authparam10)的authType指定了多种认证类型时，此字段标识用户实际选择并完成认证的类型。 |
| enrolledState12+ | [EnrolledState](js-apis-useriam-userauth.md#enrolledstate12) | 否 | 是 | 认证通过时，返回注册凭据的状态。包含当前认证类型的凭据摘要和数量。应用可通过对比此值与之前保存的值，判断用户凭据是否发生变化。若启用了认证结果复用且之前认证使用的凭据已被删除（人脸或指纹），返回的enrolledState中credentialCount和credentialDigest均为0。 |

## IAuthCallback10+

返回认证结果的回调对象。该接口定义了认证结果的回调方法，用于在认证完成后获取认证结果。应用通过实现onResult方法，可以在认证通过时获取认证令牌，在认证不通过时获取错误码和相关信息。

### onResult10+

onResult(result: UserAuthResult): void

回调函数，返回认证结果。认证通过时，可以通过UserAuthResult获取到认证通过的令牌信息，用于后续的安全操作验证；认证不通过时，可以通过result字段获取错误码，根据错误码采取相应的处理措施（如提示用户重新认证、引导用户注册凭据等）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [UserAuthResult](js-apis-useriam-userauth.md#userauthresult10) | 是 | 认证结果。包含认证结果码、认证令牌（成功时）、认证类型和凭据状态等信息。应用应检查result.result字段判断认证是否成功：  - 若result.result为SUCCESS(12500000)，表示认证通过，可使用result.token进行后续操作。  - 若result.result为其他值，表示认证不通过，应根据具体错误码进行处理。 |

**示例1：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${result.result}`);
    }
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+认证类型相关+复用设备解锁最大有效时长认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${result.result}`);
    }
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例3：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+任意应用认证类型相关+复用任意应用最大有效时长认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${result.result}`);
    }
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## AuthTipInfo20+

用户认证中间状态。该接口用于描述认证过程中产生的各种中间状态信息，包括状态对应的认证类型和具体的状态码。应用可通过[AuthTipCallback](js-apis-useriam-userauth.md#authtipcallback20)获取这些中间状态，以便在认证过程中提供更精细的用户反馈和状态感知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tipType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 否 | 否 | 中间状态对应的认证类型。表示产生当前中间状态的认证方式，如人脸认证(FACE)、指纹认证(FINGERPRINT)或PIN认证(PIN)。应用可根据认证类型为用户提供针对性的提示。 |
| tipCode | [UserAuthTipCode](js-apis-useriam-userauth.md#userauthtipcode20) | 否 | 否 | 中间状态值。表示具体的中间状态类型，如认证不通过、超时、冻结、界面加载/释放等。应用应根据tipCode为用户提供相应的反馈或执行相应的处理逻辑。 |

## AuthTipCallback20+

type AuthTipCallback = (authTipInfo: AuthTipInfo) => void

回调函数，返回认证中间状态。该回调用于在认证过程中获取各种中间状态信息，包括每次认证不通过、冻结状态、界面加载和释放等。通过订阅这些中间状态，应用可以在认证过程中提供更精细的用户交互和状态管理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authTipInfo | [AuthTipInfo](js-apis-useriam-userauth.md#authtipinfo20) | 是 | 认证中间状态。包含认证类型(tipType)和状态码(tipCode)。应用应根据tipCode执行相应处理：  - COMPARE\_FAILURE(1)：提示用户重新尝试。  - TIMEOUT(2)：提示用户操作超时。  - TEMPORARILY\_LOCKED(3)：提示用户等待冻结解除。  - PERMANENTLY\_LOCKED(4)：提示用户需PIN解锁。  - WIDGET\_LOADED(5)：认证界面已加载，可执行初始化。  - WIDGET\_RELEASED(6)：认证界面已释放，可执行后续操作。  - COMPARE\_FAILURE\_WITH\_FROZEN(7)：提示用户认证不通过且已冻结。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info('userAuthInstance callback');
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## UserAuthInstance10+

用于执行用户身份认证，并支持使用统一用户身份认证控件。该接口提供了完整的用户认证能力，包括订阅认证结果、订阅认证中间状态、启动认证和取消认证等操作。通过统一认证控件，可以为用户提供标准化的认证界面和一致的认证体验。

使用以下接口前，需先通过[getUserAuthInstance](js-apis-useriam-userauth.md#userauthgetuserauthinstance10)方法获取UserAuthInstance对象。

**说明** 

每个UserAuthInstance实例只能用于一次认证过程。若需要再次认证，必须重新获取UserAuthInstance实例。

### on('result')10+

on(type: 'result', callback: IAuthCallback): void

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证不通过尝试并不会通过该接口返回，只有最终的认证结果（成功或最终失败）会通过此接口返回。如果需要感知整个认证过程中用户的每一次认证不通过尝试和中间状态，请通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅。

**说明** 

在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](js-apis-useriam-userauth.md#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10) | 是 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |

**示例1：**

以模系统弹窗方式进行用户身份认证。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${result.result}`);
    }
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

以模应用弹窗方式进行用户身份认证。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  modelApplicationAuth(): void {
    try {
      const rand = cryptoFramework.createRandom();
      const len: number = 16;
      let randData: Uint8Array | null = null;
      let retryCount = 0;
      while(retryCount < 3){
        randData = rand?.generateRandomSync(len)?.data;
        if(randData){
          break;
        }
        retryCount++;
      }
      if(!randData){
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: [userAuth.UserAuthType.PIN],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      const uiContext: UIContext = this.getUIContext();
      const context: Context | undefined = uiContext.getHostContext();
      const widgetParam: userAuth.WidgetParam = {
        title: '请输入密码',
        uiContext: context,
      };
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      console.info('get userAuth instance successfully.');
      // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
      userAuthInstance.on('result', {
        onResult (result) {
          console.info(`userAuthInstance callback result =${result.result}`);
        }
      });
      console.info('auth on successfully.');
      userAuthInstance.start();
      console.info('auth start successfully.');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
    }
  }

  build() {
    Column() {
      Button('start auth')
        .onClick(() => {
          this.modelApplicationAuth();
        })
    }
  }
}
```

### off('result')10+

off(type: 'result', callback?: IAuthCallback): void

取消订阅用户身份认证的结果。

**说明** 

需要使用已经成功订阅事件的[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10) | 否 | 认证接口的回调函数，用于返回认证结果。当不传该参数时默认值为调用[on('result')](js-apis-useriam-userauth.md#onresult10-1)接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.off('result', {
    onResult (result) {
      console.info(`auth off result = ${result.result}`);
    }
  });
  console.info('auth off successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

### start10+

start(): void

开始认证。

**说明** 

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**需要权限：**

* API版本20+：ohos.permission.ACCESS\_BIOMETRIC 或 ohos.permission.USER\_AUTH\_FROM\_BACKGROUND（仅向系统应用开放，可在后台发起认证）
* API版本10-19：ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. Possible causes:  1.No permission to access biometric.  2.No permission to start authentication from background. |
| 401 | Parameter error. Possible causes:  1.Incorrect parameter types. |
| 12500001 | Authentication failed.  适用版本：10-19 |
| 12500002 | General operation error. |
| 12500003 | Authentication canceled. |
| 12500004 | Authentication timeout.  适用版本：10-19 |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | Authentication service is busy.  适用版本：10-19 |
| 12500009 | Authentication is locked out. |
| 12500010 | The type of credential has not been enrolled. |
| 12500011 | Switched to the customized authentication process. |
| 12500013 | Operation failed because of PIN expired.  适用版本：12+ |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

### cancel10+

cancel(): void

取消认证。

**说明** 

此时UserAuthInstance必须是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Incorrect parameter types. |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam : userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能调用cancel()接口。
  userAuthInstance.start();
  console.info('auth start successfully.');
  userAuthInstance.cancel();
  console.info('auth cancel successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

### on('authTip')20+

on(type: 'authTip', callback: AuthTipCallback): void

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证不通过尝试。使用callback异步回调。

**说明** 

在PC/2in1设备上，应用如果使用模应用弹窗方式发起认证（即配置用户界面参数[widgetParam](js-apis-useriam-userauth.md#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件类型，支持的事件为'authTip'，当[start()](js-apis-useriam-userauth.md#start10)调用完成，发起身份认证，触发该事件。 |
| callback | [AuthTipCallback](js-apis-useriam-userauth.md#authtipcallback20) | 是 | 认证接口的回调函数，用于返回认证中间状态。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info('userAuthInstance callback.');
  });
  console.info('auth on successfully.');
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

### off('authtip')20+

off(type: 'authTip', callback?: AuthTipCallback): void

取消订阅用户身份认证中间状态。

**说明** 

需要使用已经成功订阅事件的[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型，支持的事件为'authTip'，当[start()](js-apis-useriam-userauth.md#start10)调用完成，发起身份认证并调用[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)订阅该事件后，调用该方法可取消订阅，不会再触发该事件。 |
| callback | [AuthTipCallback](js-apis-useriam-userauth.md#authtipcallback20) | 否 | 认证接口的回调函数，用于返回认证中间状态。 当不传该参数时默认值为调用[on('authTip')](js-apis-useriam-userauth.md#onauthtip20)接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info('userAuthInstance callback');
  });
  console.info('auth off successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## userAuth.getUserAuthInstance10+

getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance

获取[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)对象，执行用户身份认证，并支持使用统一用户身份认证控件。该接口用于创建一个用户认证实例，配置认证参数和界面参数后，可通过返回的实例对象启动认证、订阅认证结果等。

**说明** 

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。认证完成后（无论成功或失败），该实例将无法再次使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authParam | [AuthParam](js-apis-useriam-userauth.md#authparam10) | 是 | 用户认证相关参数。包含挑战值、认证类型列表、认证可信等级、认证结果复用配置等。挑战值建议使用加密框架生成的随机数，认证类型可指定多种供用户选择，认证可信等级应根据业务场景安全需求选择。 |
| widgetParam | [WidgetParam](js-apis-useriam-userauth.md#widgetparam10) | 是 | 用户认证界面配置相关参数。包含界面标题、导航按钮文本、窗口模式（系统API）、模应用弹窗上下文等。标题建议设置为认证目的，导航按钮文本可用于自定义认证跳转。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10) | 支持用户界面的认证器对象。获取实例后，需调用[on('result')](js-apis-useriam-userauth.md#onresult10-1)订阅认证结果，再调用[start](js-apis-useriam-userauth.md#start10)启动认证。认证完成后，可通过回调获取认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified.  2.Incorrect parameter types.  3.Parameter verification failed. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

## AuthResultInfo(deprecated)

表示认证结果信息，用于描述认证结果。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](js-apis-useriam-userauth.md#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | number | 否 | 否 | 认证结果。 |
| token | Uint8Array | 否 | 是 | 用户身份认证通过的凭证。 |
| remainAttempts | number | 否 | 是 | 剩余的认证尝试次数。 |
| lockoutDuration | number | 否 | 是 | 认证操作的锁定时长，时间单位为毫秒ms。 |

## TipInfo(deprecated)

表示认证过程中的提示信息，用于提供认证过程的反馈。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[AuthTipInfo](js-apis-useriam-userauth.md#authtipinfo20)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| module | number | 否 | 否 | 发送提示信息的模块标识。 |
| tip | number | 否 | 否 | 认证过程提示信息。 |

## EventInfo(deprecated)

type EventInfo = AuthResultInfo | TipInfo

表示认证过程中事件信息的类型。

该类型为下表类型取值中的联合类型。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](js-apis-useriam-userauth.md#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| [AuthResultInfo](js-apis-useriam-userauth.md#authresultinfodeprecated) | 获取到的认证结果信息。 |
| [TipInfo](js-apis-useriam-userauth.md#tipinfodeprecated) | 认证过程中的提示信息。 |

## AuthEventKey(deprecated)

type AuthEventKey = 'result' | 'tip'

表示认证事件类型的关键字，作为[on](js-apis-useriam-userauth.md#ondeprecated)接口的参数。

该类型为下表类型取值中的联合类型。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| 'result' | [on](js-apis-useriam-userauth.md#ondeprecated)接口第一个参数为"result"时，[callback](js-apis-useriam-userauth.md#callbackdeprecated)回调返回认证的结果信息。 |
| 'tip' | [on](js-apis-useriam-userauth.md#ondeprecated)接口第一个参数为"tip"时，[callback](js-apis-useriam-userauth.md#callbackdeprecated)回调返回认证操作中的提示信息。 |

## AuthEvent(deprecated)

认证接口的异步回调对象。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[IAuthCallback](js-apis-useriam-userauth.md#iauthcallback10)替代。

### callback(deprecated)

callback(result : EventInfo) : void

通过该回调获取认证结果信息或认证过程中的提示信息。

**说明** 

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[onResult](js-apis-useriam-userauth.md#onresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [EventInfo](js-apis-useriam-userauth.md#eventinfodeprecated) | 是 | 返回的认证结果信息或提示信息。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
// 通过callback获取认证结果。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`result: ${result.result}`);
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed, error = ${error}`);
  // do error.
}
// 通过callback获取认证过程中的提示信息。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed, error = ${error}`);
  // do error.
}
```

## AuthInstance(deprecated)

执行用户认证的对象。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[UserAuthInstance](js-apis-useriam-userauth.md#userauthinstance10)替代。

### on(deprecated)

on : (name : AuthEventKey, callback : AuthEvent) => void

订阅指定类型的用户认证事件。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[on('result')](js-apis-useriam-userauth.md#onresult10-1)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [AuthEventKey](js-apis-useriam-userauth.md#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，回调函数返回认证结果；取值为"tip"时，回调函数返回认证过程中的提示信息。 |
| callback | [AuthEvent](js-apis-useriam-userauth.md#autheventdeprecated) | 是 | 认证接口的回调函数，用于返回认证结果或认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`result: ${result.result}`);
    }
  });
  // 订阅认证过程中的提示信息。
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed, error = ${error}`);
  // do error.
}
```

### off(deprecated)

off : (name : AuthEventKey) => void

取消订阅特定类型的认证事件。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[off('result')](js-apis-useriam-userauth.md#offresult10)替代。

需要使用已经成功订阅事件的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行取消订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | [AuthEventKey](js-apis-useriam-userauth.md#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，取消订阅认证结果；取值为"tip"时，取消订阅认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`result: ${result.result}`);
    }
  });
  // 取消订阅结果。
  auth.off('result');
  console.info('cancel subscribe authentication event successfully.');
} catch (error) {
  console.error(`cancel subscribe authentication event failed, error = ${error}`);
  // do error.
}
```

### start(deprecated)

start : () => void

开始认证。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[start](js-apis-useriam-userauth.md#start10)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行认证。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500001 | Authentication failed. |
| 12500002 | General operation error. |
| 12500003 | The operation is canceled. |
| 12500004 | The operation is time-out. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | The authentication task is busy. |
| 12500009 | The authenticator is locked. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed, error = ${error}`);
}
```

### cancel(deprecated)

cancel : () => void

取消认证。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[cancel](js-apis-useriam-userauth.md#cancel10)替代。

使用获取到的[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)对象调用该接口进行取消认证，此[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)需要是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.cancel();
  console.info('cancel auth successfully.');
} catch (error) {
  console.error(`cancel auth failed, error = ${error}`);
}
```

## userAuth.getAuthInstance(deprecated)

getAuthInstance(challenge : Uint8Array, authType : UserAuthType, authTrustLevel : AuthTrustLevel): AuthInstance

获取AuthInstance对象，用于执行用户身份认证。

**说明** 

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[getUserAuthInstance](js-apis-useriam-userauth.md#userauthgetuserauthinstance10)替代。

每个AuthInstance只能进行一次认证，若需要再次进行认证则需重新获取AuthInstance。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，最大长度为32字节，可以传Uint8Array([])。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated) | 认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  console.info('get auth instance successfully.');
} catch (error) {
  console.error(`get auth instance failed, error = ${error}`);
}
```

## userAuth.getAvailableStatus9+

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void

查询指定类型和等级的认证能力是否支持。该接口用于检查当前设备是否支持指定的认证类型和认证可信等级，帮助应用在发起认证前判断认证能力是否可用，从而避免不必要的认证不通过。若查询通过（无错误抛出），表示认证能力可用；若抛出错误，应用应根据错误码判断具体原因并采取相应处理。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型。用于指定查询的认证类型，支持FACE（人脸）、FINGERPRINT（指纹）、PIN（密码）、COMPANION\_DEVICE（伴随设备）。  **说明**：  从API version 11开始支持PIN查询。  从API版本26.0.0开始支持COMPANION\_DEVICE查询。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。用于指定查询的认证可信等级，有效值为ATL1(10000)、ATL2(20000)、ATL3(30000)、ATL4(40000)。等级越高，对认证方案的活体检测能力要求越高。 |

**说明** 

如果未注册对应执行器，系统不支持该认证能力，需返回12500005。

如果已注册对应执行器，功能未禁用，但认证安全等级低于业务指定时，需返回12500006。

如果已注册对应执行器，功能未禁用，但用户未注册凭据时，需返回12500010。

如果已注册对应执行器，功能未禁用，但密码过期时，需返回12500013。

**注意** 

若用户注册的锁屏口令是4位PIN时，其认证可信等级为ATL3，调用该接口查询是否支持ATL4级别的密码认证时，需返回12500010。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[用户认证错误码](errorcode-useriam.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1.Mandatory parameters are left unspecified. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500010 | The type of credential has not been enrolled. |
| 12500013 | Operation failed because of PIN expired.  适用版本：12+ |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(`current auth trust level is not supported, error = ${error}`);
}
```

## UserAuthResultCode9+

表示返回码的枚举。该枚举定义了用户认证操作可能返回的所有结果码，包括成功码和各类错误码。应用可根据返回码判断认证结果，并采取相应的处理措施。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 12500000 | 执行成功。表示用户身份认证通过，认证令牌有效。应用可使用返回的token进行后续的安全操作。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FAIL | 12500001 | 认证不通过。表示用户特征与已注册凭据比对不匹配，可能是用户输入错误或使用了未注册的凭据。建议提示用户重新尝试。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| GENERAL\_ERROR | 12500002 | 操作通用错误。表示认证过程中发生未知错误，建议稍后重试或联系系统管理员。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED | 12500003 | 认证取消。表示用户主动取消了认证操作或认证被系统取消。应用可根据业务逻辑决定是否重新发起认证。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TIMEOUT | 12500004 | 认证超时。表示用户在规定时间内未完成认证交互（如未及时输入密码、未正视摄像头等）。建议提示用户重新尝试并注意操作时限。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_NOT\_SUPPORT | 12500005 | 认证类型不支持。表示当前设备不支持指定的认证类型（如设备无指纹传感器却请求指纹认证）。建议检查设备能力或更换认证类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 12500006 | 认证等级不支持。表示指定的认证可信等级高于当前认证类型所能达到的最高等级。建议降低认证等级或使用更安全的认证类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BUSY | 12500007 | 系统繁忙。表示认证服务正忙于处理其他请求，建议稍后重试。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INVALID\_PARAMETERS20+ | 12500008 | 参数校验失败。表示传入的参数不符合要求，如参数类型错误、参数值超出范围等。建议检查参数并重新调用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| LOCKED | 12500009 | 认证器已锁定。表示认证器因连续多次认证不通过而进入冻结状态，用户需等待冻结解除或使用PIN解锁后才能继续认证。可通过[getAuthLockState](js-apis-useriam-userauth.md#userauthgetauthlockstate22)查询具体冻结状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NOT\_ENROLLED | 12500010 | 用户未录入指定的系统身份认证凭据。表示用户未注册所请求的认证类型（如请求指纹认证但用户未录入指纹）。建议引导用户先注册相应凭据。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CANCELED\_FROM\_WIDGET10+ | 12500011 | 用户取消了系统认证方式，选择应用自定义认证。表示用户点击了认证界面上的导航按钮，选择使用应用提供的自定义认证方式。应用需拉起自定义认证界面。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| PIN\_EXPIRED12+ | 12500013 | 锁屏密码过期。表示系统锁屏口令已过期（如企业策略要求定期更换密码），用户需更新锁屏密码后才能继续使用认证功能。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## UserAuth(deprecated)

认证器对象。

### constructor(deprecated)

constructor()

创建认证器对象。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAuthInstance](js-apis-useriam-userauth.md#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

### getVersion(deprecated)

getVersion() : number

获取认证器的版本信息。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 认证器版本信息。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```

### getAvailableStatus(deprecated)

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel) : number

查询指定类型和等级的认证能力是否支持。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAvailableStatus](js-apis-useriam-userauth.md#userauthgetavailablestatus9)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 查询结果，结果为SUCCESS时表示支持，其他返回值参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support successfully.');
} else {
  console.error(`check auth support failed, code = ${checkCode}`);
}
```

### auth(deprecated)

auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array

执行用户认证，使用回调函数返回结果。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| challenge | Uint8Array | 是 | 挑战值，可以传Uint8Array([])。 |
| authType | [UserAuthType](js-apis-useriam-userauth.md#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8) | 是 | 认证信任等级。 |
| callback | [IUserAuthCallback](js-apis-useriam-userauth.md#iuserauthcallbackdeprecated) | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | ContextId，作为取消认证[cancelAuth](js-apis-useriam-userauth.md#cancelauthdeprecated)接口的入参。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      } else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult failed, error = ${error}`);
    }
  }
});
```

### cancelAuth(deprecated)

cancelAuth(contextID : Uint8Array) : number

表示通过contextID取消本次认证。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[cancel](js-apis-useriam-userauth.md#canceldeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contextID | Uint8Array | 是 | 上下文的标识，通过[auth](js-apis-useriam-userauth.md#authdeprecated)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 取消认证的结果，结果为SUCCESS时表示取消成功，其他返回值参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId可通过auth接口获取，此处直接定义。
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth successfully.');
} else {
  console.error('cancel auth failed.');
}
```

## IUserAuthCallback(deprecated)

返回认证结果的回调对象。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthEvent](js-apis-useriam-userauth.md#autheventdeprecated)代替。

### onResult(deprecated)

onResult: (result : number, extraInfo : AuthResult) => void

回调函数，返回认证结果。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](js-apis-useriam-userauth.md#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | number | 是 | 认证结果，参见[ResultCode](js-apis-useriam-userauth.md#resultcodedeprecated)。 |
| extraInfo | [AuthResult](js-apis-useriam-userauth.md#authresultdeprecated) | 是 | 扩展信息，不同情况下的具体信息，  如果身份验证通过，则在extraInfo中返回用户认证令牌，  如果身份验证失败，则在extraInfo中返回剩余的用户认证次数，  如果身份验证执行器被锁定，则在extraInfo中返回冻结时间。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult failed, error = ${error}`);
    }
  }
});
```

### onAcquireInfo(deprecated)

onAcquireInfo ?: (module : number, acquire : number, extraInfo : any) => void

回调函数，返回认证过程中的提示信息，非必须实现。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](js-apis-useriam-userauth.md#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| module | number | 是 | 发送提示信息的模块标识。 |
| acquire | number | 是 | 认证执行过程中的提示信息。 |
| extraInfo | any | 是 | 预留字段。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult failed, error = ${error}`);
    }
  },
  onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
    try {
      console.info('auth onAcquireInfo successfully.');
    } catch (error) {
      console.error(`auth onAcquireInfo failed, error = ${error}`);
    }
  }
});
```

## AuthResult(deprecated)

表示认证结果的对象。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthResultInfo](js-apis-useriam-userauth.md#authresultinfodeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| token | Uint8Array | 否 | 是 | 认证通过的令牌信息。 |
| remainTimes | number | 否 | 是 | 剩余的认证操作次数。 |
| freezingTime | number | 否 | 是 | 认证操作的冻结时间。单位为毫秒。 |

## ResultCode(deprecated)

表示返回码的枚举。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAIL | 1 | 认证失败。 |
| GENERAL\_ERROR | 2 | 操作通用错误。 |
| CANCELED | 3 | 操作取消。 |
| TIMEOUT | 4 | 操作超时。 |
| TYPE\_NOT\_SUPPORT | 5 | 不支持的认证类型。 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 6 | 不支持的认证等级。 |
| BUSY | 7 | 忙碌状态。 |
| INVALID\_PARAMETERS | 8 | 无效参数。 |
| LOCKED | 9 | 认证器已锁定。 |
| NOT\_ENROLLED | 10 | 用户未录入认证信息。 |

## FaceTips(deprecated)

表示人脸认证过程中提示码的枚举。

**说明** 

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FACE\_AUTH\_TIP\_TOO\_BRIGHT | 1 | 光线太强，获取的图像太亮。 |
| FACE\_AUTH\_TIP\_TOO\_DARK | 2 | 光线太暗，获取的图像太暗。 |
| FACE\_AUTH\_TIP\_TOO\_CLOSE | 3 | 人脸距离设备过近。 |
| FACE\_AUTH\_TIP\_TOO\_FAR | 4 | 人脸距离设备过远。 |
| FACE\_AUTH\_TIP\_TOO\_HIGH | 5 | 设备太高，仅获取到人脸上部。 |
| FACE\_AUTH\_TIP\_TOO\_LOW | 6 | 设备太低，仅获取到人脸下部。 |
| FACE\_AUTH\_TIP\_TOO\_RIGHT | 7 | 设备太靠右，仅获取到人脸右部。 |
| FACE\_AUTH\_TIP\_TOO\_LEFT | 8 | 设备太靠左，仅获取到人脸左部。 |
| FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION | 9 | 在图像采集过程中，用户人脸移动太快。 |
| FACE\_AUTH\_TIP\_POOR\_GAZE | 10 | 没有正视摄像头。 |
| FACE\_AUTH\_TIP\_NOT\_DETECTED | 11 | 没有检测到人脸信息。 |

## FingerprintTips(deprecated)

表示指纹认证过程中提示码的枚举。

**说明** 

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINGERPRINT\_AUTH\_TIP\_GOOD | 0 | 获取的指纹图像良好。 |
| FINGERPRINT\_AUTH\_TIP\_DIRTY | 1 | 由于传感器上可疑或检测到的污垢，指纹图像噪音过大。 |
| FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT | 2 | 由于检测到的情况，指纹图像噪声太大，无法处理。 |
| FINGERPRINT\_AUTH\_TIP\_PARTIAL | 3 | 仅检测到部分指纹图像。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_FAST | 4 | 快速移动，指纹图像不完整。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW | 5 | 缺少运动，指纹图像无法读取。 |

## UserAuthType8+

表示身份认证的凭据类型枚举。该枚举定义了系统支持的认证类型，包括锁屏密码认证（PIN）、生物特征认证（人脸、指纹）等。应用在发起认证时需指定认证类型列表，用户可选择其中任意一种完成认证。不同认证类型具有不同的安全强度和用户体验特点，应用应根据业务场景选择合适的认证类型。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PIN10+ | 1 | 口令认证。用户通过输入锁屏密码完成认证。锁屏密码认证具有高安全性，认证可信等级可达ATL4，适用于支付、重要操作确认等高安全场景。用户需要手动输入，体验不如生物认证便捷。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FACE | 2 | 人脸认证。用户通过人脸识别完成认证，系统会验证用户面部特征与已注册人脸的匹配度。人脸认证支持不同级别的活体检测能力，详细划分原则可参考[生物认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。优点是体验便捷，缺点是对设备和光照条件有一定要求。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| FINGERPRINT | 4 | 指纹认证。用户通过指纹传感器完成认证，系统会验证用户指纹特征与已注册指纹的匹配度。指纹认证支持多种认证可信等级，详细划分原则可参考[生物认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)，适用于中等安全场景。优点是操作简单快捷，缺点是设备需配备指纹传感器，且湿手或指纹磨损可能影响识别效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COMPANION\_DEVICE | 64 | 伴随设备认证。用户通过佩戴的伴随设备完成认证。伴随设备认证支持多种认证可信等级，详细划分原则可参考[生物认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## AuthTrustLevel8+

表示认证结果的信任等级枚举。该枚举定义了四个认证可信等级，用于描述认证结果的安全强度。认证可信等级越高，表示认证方案的活体检测能力越强、用户身份识别越精确，适用于更高安全要求的业务场景。应用应根据业务场景的安全需求选择合适的认证可信等级。

典型场景及举例可参考[生物认证可信等级划分原则](../harmonyos-guides/user-authentication-overview.md#生物认证可信等级划分原则)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ATL1 | 10000 | 认证结果的信任等级级别1，表示该认证方案能够识别用户个体，具备基本的活体检测能力。安全强度较低，认证结果可能存在一定风险。适用于业务风控、一般个人数据查询、非敏感信息访问等低安全场景。建议配合其他安全措施使用。 |
| ATL2 | 20000 | 认证结果的信任等级级别2，表示该认证方案能够精确识别用户个体，具备标准的活体检测能力。安全强度中等，可有效防御简单的伪造攻击。适用于维持设备解锁状态、应用登录、一般敏感操作确认等中等安全场景。 |
| ATL3 | 30000 | 认证结果的信任等级级别3，表示该认证方案能够精确识别用户个体，具备较强的活体检测能力。安全强度较高，可有效防御照片、视频等常见伪造攻击。适用于设备解锁、重要敏感操作确认、企业级应用登录等较高安全场景。 |
| ATL4 | 40000 | 认证结果的信任等级级别4，表示该认证方案能够高精度识别用户个体，具备很强的活体检测能力。安全强度最高，可有效防御各类高级伪造攻击。适用于小额支付、金融交易、高敏感数据访问等高安全场景。仅少数高安全认证方案可支持此等级。 |

## SecureLevel(deprecated)

type SecureLevel = string

表示认证的安全级别。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthTrustLevel](js-apis-useriam-userauth.md#authtrustlevel8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示类型为字符，认证的安全级别包括：'S1' | 'S2'|'S3'|'S4'。  - 'S1'：认证结果的信任等级级别1，代表该认证方案能够识别用户个体，有一定的活体检测能力。常用的业务场景有业务风控、一般个人数据查询等。  - 'S2'：认证结果的信任等级级别2，代表该认证方案能够精确识别用户个体，有一定的活体检测能力。常用的业务场景有维持设备解锁状态，应用登录等。  - 'S3'：认证结果的信任等级级别3，代表该认证方案能够精确识别用户个体，有较强的活体检测能力。常用的业务场景有设备解锁等。  - 'S4'：认证结果的信任等级级别4，代表该认证方案能够高精度的识别用户个体，有很强的活体检测能力。常用的业务场景有小额支付等。 |

## AuthType(deprecated)

type AuthType = string

表示认证类型。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthType](js-apis-useriam-userauth.md#userauthtype8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| --- | --- |
| string | 表示认证类型为字符，认证类型包括：'ALL'|'FACE\_ONLY'。  - 'ALL'：预留参数，当前版本暂不支持ALL类型的认证。  - 'FACE\_ONLY'：人脸认证。 |

## userAuth.getAuthenticator(deprecated)

getAuthenticator(): Authenticator

获取Authenticator对象，用于执行用户身份认证。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[getAuthInstance](js-apis-useriam-userauth.md#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Authenticator](js-apis-useriam-userauth.md#authenticatordeprecated) | 认证器对象。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```

## Authenticator(deprecated)

认证器对象。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthInstance](js-apis-useriam-userauth.md#authinstancedeprecated)替代。

### execute(deprecated)

execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void

执行用户认证，使用callback方式作为异步方法。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE\_ONLY"。  ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。  具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。  具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |
| callback | AsyncCallback<number> | 是 | 回调函数。number表示认证结果，参见[AuthenticationResult](js-apis-useriam-userauth.md#authenticationresultdeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE_ONLY', 'S2', (error, code)=>{
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth successfully.');
    return;
  }
  console.error(`auth failed, code = ${code}`);
});
```

### execute(deprecated)

execute(type : AuthType, level : SecureLevel): Promise<number>

执行用户认证，使用promise方式作为异步方法。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](js-apis-useriam-userauth.md#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | AuthType | 是 | 认证类型，当前只支持"FACE\_ONLY"。  ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | SecureLevel | 是 | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。  具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。  具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回携带一个number的Promise。number 为认证结果，参见[AuthenticationResult](js-apis-useriam-userauth.md#authenticationresultdeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE_ONLY', 'S2').then((code)=>{
    console.info('auth successfully.');
  })
} catch (error) {
  console.error(`auth failed, code = ${error}`);
}
```

## AuthenticationResult(deprecated)

表示认证结果的枚举。

**说明** 

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthResultCode](js-apis-useriam-userauth.md#userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_SUPPORT | -1 | 设备不支持当前的认证方式。 |
| SUCCESS | 0 | 认证成功。 |
| COMPARE\_FAILURE | 1 | 比对失败。 |
| CANCELED | 2 | 用户取消认证。 |
| TIMEOUT | 3 | 认证超时。 |
| CAMERA\_FAIL | 4 | 开启相机失败。 |
| BUSY | 5 | 认证服务忙，请稍后重试。 |
| INVALID\_PARAMETERS | 6 | 认证参数无效。 |
| LOCKED | 7 | 认证失败次数过多，已锁定。 |
| NOT\_ENROLLED | 8 | 未录入认证凭据。 |
| GENERAL\_ERROR | 100 | 其他错误。 |
