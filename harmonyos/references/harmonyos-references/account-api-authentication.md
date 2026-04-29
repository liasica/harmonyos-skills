---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-authentication
title: authentication (华为账号应用统一认证服务)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > authentication (华为账号应用统一认证服务)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:27f3cd597f0ae06c9367aa15cbbe363ff09f2d50928b2300e7d776da571fdc89
---

本模块提供Account Kit（华为账号服务）认证能力，包括账号登录、授权、取消授权等功能。应用可以使用该能力实现应用账号的登录注册、获取华为账号登录状态、手机号一致性校验状态、用户授权信息等。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { authentication } from '@kit.AccountKit';
```

## HuaweiIDProvider

PhonePC/2in1TabletTVWearable

该类提供实现认证服务的方法，用于创建登录、授权、取消授权请求对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** HuaweiIDProvider继承自[AuthenticationProvider](account-api-authentication.md#authenticationprovider)。

### createLoginWithHuaweiIDRequest

PhonePC/2in1TabletTVWearable

createLoginWithHuaweiIDRequest(): LoginWithHuaweiIDRequest

创建默认scope和permission登录请求对象，可通过属性值设置请求参数。作为应用使用华为账号登录场景的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LoginWithHuaweiIDRequest](account-api-authentication.md#loginwithhuaweiidrequest) | 应用登录场景定义应用使用Account Kit登录请求获取UnionID、OpenID等数据的请求对象。华为账号登录场景请求对象参数请应用根据自身实际场景进行选择。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. const huaweiIdProvider = new authentication.HuaweiIDProvider();
4. const loginWithHuaweiIDRequest = huaweiIdProvider.createLoginWithHuaweiIDRequest();
```

### createAuthorizationWithHuaweiIDRequest

PhonePC/2in1TabletTVWearable

createAuthorizationWithHuaweiIDRequest(): AuthorizationWithHuaweiIDRequest

创建一个Account Kit授权请求对象，可通过属性值设置请求参数。作为应用使用华为账号登录场景的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest) | 定义应用授权获取用户信息请求对象。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. const huaweiIdProvider = new authentication.HuaweiIDProvider();
4. const request = huaweiIdProvider.createAuthorizationWithHuaweiIDRequest();
```

### createCancelAuthorizationRequest

PhonePC/2in1TabletTVWearable

createCancelAuthorizationRequest(): CancelAuthorizationRequest

创建一个Account Kit取消授权请求对象，可通过属性值设置参数。作为应用取消华为账号授权场景的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CancelAuthorizationRequest](account-api-authentication.md#cancelauthorizationrequest) | 定义应用取消Account Kit授权请求对象。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. const huaweiIdProvider = new authentication.HuaweiIDProvider();
4. const cancelAuthorizationRequest = huaweiIdProvider.createCancelAuthorizationRequest();
```

### getHuaweiIDState

PhonePC/2in1TabletTVWearable

getHuaweiIDState(request: StateRequest): Promise<StateResult>

获取华为账号登录状态，使用Promise异步回调。在应用需要判断账号是否已登录场景下使用，不依赖网络连接。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [StateRequest](account-api-authentication.md#staterequest) | 是 | 获取华为账号登录状态请求对象，包含请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[StateResult](account-api-authentication.md#stateresult)> | Promise对象，返回[StateResult](account-api-authentication.md#stateresult)对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | Invalid input parameter value. |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 创建请求参数
6. const stateRequest: authentication.StateRequest = {
7. idType: authentication.IdType.UNION_ID,
8. idValue: '<可通过华为账号登录接口获取>' // 该值可以通过华为账号登录接口获取
9. };
10. try {
11. // 执行获取华为账号登录状态请求，并处理结果
12. new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
13. hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
14. const state = data.state;
15. // 处理state
16. }).catch((error: BusinessError) => {
17. dealAllError(error);
18. });
19. } catch (error) {
20. dealAllError(error);
21. }

23. // 错误处理
24. function dealAllError(error: BusinessError): void {
25. hilog.error(0x0000, 'testTag', `Failed to get huaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
26. }
```

### getMobileNumberConsistency

PhonePC/2in1TabletTVWearable

getMobileNumberConsistency(request: ConsistencyRequest): Promise<ConsistencyResult>

获取手机号一致性状态，使用Promise异步回调。在应用需要校验华为账号绑定的手机号是否与本机SIM卡一致场景下使用。

开发者在使用获取手机号一致性状态接口前，需要完成quickLoginMobilePhone（华为账号一键登录）的scope权限申请，详情参见[开发前提](../harmonyos-guides/account-phone-unionid-login.md#开发前提)。scope权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ConsistencyRequest](account-api-authentication.md#consistencyrequest) | 是 | 获取手机号一致性状态请求对象，包含请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ConsistencyResult](account-api-authentication.md#consistencyresult)> | Promise对象，返回[ConsistencyResult](account-api-authentication.md#consistencyresult)对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. Function getMobileNumberConsistency can not work correctly due to limited device capabilities. |
| [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001500004](account-api-error-code.md#section1001500004-已登录的华为账号不支持该功能) | The account does not support this function. |
| [1001500005](account-api-error-code.md#section1001500005-该功能被限制调用) | This function is restricted from being called. |
| [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](account-api-error-code.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502005](account-api-error-code.md#section1001502005-网络错误) | Network error. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 创建请求参数
6. const consistencyRequest: authentication.ConsistencyRequest = {
7. idType: authentication.IdType.UNION_ID,
8. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
9. mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
10. };
11. try {
12. // 执行获取手机号一致性状态请求，并处理结果
13. new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
14. .then((data: authentication.ConsistencyResult) => {
15. hilog.info(0x0000, 'testTag', `Succeeded in getting getMobileNumberConsistency result = ${data.state}`);
16. const state = data.state;
17. // 处理state
18. })
19. .catch((err: BusinessError) => {
20. dealAllError(err);
21. });
22. } catch (error) {
23. dealAllError(error);
24. }

26. // 错误处理
27. function dealAllError(error: BusinessError): void {
28. hilog.error(0x0000, 'testTag',
29. `Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}`);
30. }
```

## LoginWithHuaweiIDRequest

PhonePC/2in1TabletTVWearable

应用登录场景定义应用使用Account Kit登录请求获取UnionID、OpenID等数据的请求对象。华为账号登录场景请求对象参数请应用根据自身实际场景进行选择。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** LoginWithHuaweiIDRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| forceLogin | boolean | 否 | 是 | 表示是否需要强制拉起华为账号登录页。  如果该值为true，华为账号未登录时，则将拉起华为账号登录页。  如果该值为false，且华为账号未登录，调用[executeRequest](account-api-authentication.md#executerequest-1)将返回[1001502001 用户未登录华为账号](account-api-error-code.md#section1001502001-用户未登录华为账号)。  默认值：true。 |
| state | string | 否 | 是 | 请求体中的state参数，该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。  开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |
| nonce | string | 否 | 是 | 请求体中的nonce参数，该参数会包含在返回的ID Token中，通过校验一致性，可用于防止重放攻击。  字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  如该参数未传、传空，ID Token中nonce默认值：“default”。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |
| idTokenSignAlgorithm | [IdTokenSignAlgorithm](account-api-authentication.md#idtokensignalgorithm) | 否 | 是 | 用于指定ID Token的签名算法。应用根据实际安全要求、性能、系统环境兼容性进行选择。  默认值：PS256。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { util } from '@kit.ArkTS';

4. const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
5. // 默认值为true，若账号未登录则强制拉起账号登录页
6. loginRequest.forceLogin = true;
7. loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256; // 默认为PS256
8. loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
```

## IdTokenSignAlgorithm

PhonePC/2in1TabletTVWearable

ID Token签名算法，该类型为枚举，根据IdTokenSignAlgorithm的不同类型，对ID Token进行不同方式的加密。请应用根据实际安全要求、性能、系统环境兼容性进行选择。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PS256 | 1 | RSASSA-PSS使用SHA-256和基于SHA-256的MGF1。为保证安全性建议使用PS256。 |
| RS256 | 2 | RSASSA-PKCS1-v1\_5使用SHA-256。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
4. // 默认值为true，若账号未登录则强制拉起账号登录页
5. loginRequest.forceLogin = true;
6. loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
```

## LoginWithHuaweiIDResponse

PhonePC/2in1TabletTVWearable

Account Kit登录请求响应对象，解析响应结果可得到OpenID、UnionID、Authorization Code、ID Token数据。作为华为账号登录成功的返回结果，用于获取或关联华为账号相关信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** LoginWithHuaweiIDResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| data | [LoginWithHuaweiIDCredential](account-api-authentication.md#loginwithhuaweiidcredential) | 是 | 是 | 登录结果数据，用于获取或关联华为账号相关信息。包含openID、unionID、authorizationCode、idToken字段。 |
| state | string | 是 | 是 | 响应体中返回的state，账号服务将该字段与请求体中传入的state比较，防止跨站攻击。字符包含“0-9”、“a-z”、“A-Z”、英文点号、英文冒号、斜杠、下划线等，长度限制1-255。校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建登录请求，并设置参数
7. const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
8. // 默认值为true，若账号未登录则强制拉起账号登录页
9. loginRequest.forceLogin = true;
10. loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
11. loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击

13. // 执行登录请求，并处理结果
14. try {
15. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
16. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
17. controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
18. if (error) {
19. dealAllError(error);
20. return;
21. }
22. const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
23. const state = loginWithHuaweiIDResponse.state;
24. if (state && loginRequest.state !== state) {
25. // state不一致，可能为跨站攻击，需重新登录
26. hilog.error(0x0000, 'testTag', `Failed to login. The state is different, response state: ${state}`);
27. return;
28. }
29. hilog.info(0x0000, 'testTag', 'Succeeded in login.');
30. const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
31. const code = loginWithHuaweiIDCredential?.authorizationCode;
32. const idToken = loginWithHuaweiIDCredential?.idToken;
33. // 开发者处理code, idToken
34. });
35. } catch (error) {
36. dealAllError(error);
37. }

39. // 错误处理
40. function dealAllError(error: BusinessError<Object>): void {
41. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
42. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
43. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
44. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
45. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
46. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
47. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
48. // 登录失败，请尝试使用其他方式登录
49. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
50. // 用户取消授权
51. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
52. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
53. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
54. // 重复请求，应用无需处理
55. } else {
56. // 应用登录失败，请尝试使用其他方式登录
57. }
58. }

60. export enum ErrorCode {
61. // 账号未登录
62. ERROR_CODE_LOGIN_OUT = 1001502001,
63. // 网络错误
64. ERROR_CODE_NETWORK_ERROR = 1001502005,
65. // 内部错误
66. ERROR_CODE_INTERNAL_ERROR = 1001502009,
67. // 用户取消授权
68. ERROR_CODE_USER_CANCEL = 1001502012,
69. // 系统服务异常
70. ERROR_CODE_SYSTEM_SERVICE = 12300001,
71. // 重复请求
72. ERROR_CODE_REQUEST_REFUSE = 1001500002
73. }
```

## LoginWithHuaweiIDCredential

PhonePC/2in1TabletTVWearable

Account Kit登录成功返回的凭据，用于获取用户相关信息和关联华为账号（OpenID/UnionID）。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authorizationCode | string | 是 | 是 | Authorization Code。临时凭据，用于获取Access Token，有效时间5分钟，并且只能使用1次。长度限制1-1024。 |
| idToken | string | 是 | 是 | ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。 |
| openID | string | 是 | 否 | OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户，不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |
| unionID | string | 是 | 否 | UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建登录请求，并设置参数
7. const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
8. // 默认值为true，若账号未登录则强制拉起账号登录页
9. loginRequest.forceLogin = true;
10. loginRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
11. loginRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击

13. // 执行登录请求，并处理结果
14. try {
15. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
16. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
17. controller.executeRequest(loginRequest, (error: BusinessError<Object>, data) => {
18. if (error) {
19. dealAllError(error);
20. return;
21. }
22. const loginWithHuaweiIDResponse = data as authentication.LoginWithHuaweiIDResponse;
23. const state = loginWithHuaweiIDResponse.state;
24. if (state && loginRequest.state !== state) {
25. // state不一致，可能为跨站攻击，需重新登录
26. hilog.error(0x0000,
27. 'testTag', `Failed to login. The state is different, response state: ${state}`);
28. return;
29. }
30. hilog.info(0x0000, 'testTag', 'Succeeded in login.');

32. const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
33. const code = loginWithHuaweiIDCredential?.authorizationCode;
34. const idToken = loginWithHuaweiIDCredential?.idToken;
35. // 开发者处理code, idToken
36. });
37. } catch (error) {
38. dealAllError(error);
39. }

41. // 错误处理
42. function dealAllError(error: BusinessError<Object>): void {
43. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
44. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
45. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
46. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
47. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
48. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
49. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
50. // 登录失败，请尝试使用其他方式登录
51. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
52. // 用户取消授权
53. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
54. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
55. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
56. // 重复请求，应用无需处理
57. } else {
58. // 应用登录失败，请尝试使用其他方式登录
59. }
60. }

62. export enum ErrorCode {
63. // 账号未登录
64. ERROR_CODE_LOGIN_OUT = 1001502001,
65. // 网络错误
66. ERROR_CODE_NETWORK_ERROR = 1001502005,
67. // 内部错误
68. ERROR_CODE_INTERNAL_ERROR = 1001502009,
69. // 用户取消授权
70. ERROR_CODE_USER_CANCEL = 1001502012,
71. // 系统服务异常
72. ERROR_CODE_SYSTEM_SERVICE = 12300001,
73. // 重复请求
74. ERROR_CODE_REQUEST_REFUSE = 1001500002
75. }
```

## AuthorizationWithHuaweiIDRequest

PhonePC/2in1TabletTVWearable

该类为应用创建的授权请求对象，使用Account Kit请求授权以申请更多的用户信息，包括scopes、permissions等属性。作为向华为账号申请授权的请求对象，应用根据实际场景按需获取。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** AuthorizationWithHuaweiIDRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| scopes | string[] | 否 | 是 | scope列表，用于获取用户数据。与permissions属性不能同时为空，否则会返回[1001502003 输入参数值无效](account-api-error-code.md#section1001502003-输入参数值无效)错误码。如果传入不合法的scope（例如空值等）则直接返回OpenID和UnionID。  默认值：['openid']。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  scope取值范围：  - profile：华为账号用户的基本信息，如昵称头像等（元服务从5.1.1(19)开始，支持该scope，并需配合supportAtomicService参数使用）。  - openid：华为账号用户的OpenID、UnionID。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  - phone：华为账号快速验证手机号（元服务不能直接调用该接口获取手机号，可参考场景化控件[快速验证手机号Button](../harmonyos-guides/scenario-fusion-button-getphonenumber.md)获取。儿童账号的手机号无法通过该scope获取），使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-get-phonenumber.md#开发前提)。  - quickLoginAnonymousPhone：获取华为账号绑定的匿名手机号（该scope只能与openid同时使用，Wearable设备以及海外账号无法获取到手机号，会报[1001500003 不支持该scopes或permissions](account-api-error-code.md#section1001500003-不支持该scopes或permissions)），使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-phone-unionid-login.md#开发前提)。  **说明：** 中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）匿名手机号的返回格式不包含国际电话区号，其他国家和地区默认包含国际电话区号。  - riskLevel：获取用户风险等级，海外账号不支持获取用户风险等级。该scope 仅支持与openid、phone、profile组合使用，并且使用该scope前需要申请账号权限，具体请参考[开发前提](../harmonyos-guides/account-get-risklevel-on-demand-acquisition.md#开发前提)。  **说明：** 元服务场景下，此scope不支持与phone组合使用，如果需要同时获取手机号和风险等级可参见Scenario Fusion Kit的场景化控件[获取手机号和风险等级Button](../harmonyos-guides/scenario-fusion-button-get-risklevel.md)。 |
| permissions | string[] | 否 | 是 | permission列表，用于获取用户授权临时凭据和用户身份认证信息。与scopes属性不能同时为空，否则会返回[1001502003 输入参数值无效](account-api-error-code.md#section1001502003-输入参数值无效)错误码。如果传入不合法的permission（例如空值等）则直接返回OpenID和UnionID。  默认值为空，不返回用户授权临时凭据和用户身份认证信息。  permission取值范围：  - serviceauthcode：用户授权临时凭据。  - idtoken：用户身份认证信息。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| forceAuthorization | boolean | 否 | 是 | 表示华为账号未登录时，是否需要强制拉起华为账号登录页。  默认值：true。  如果该值为true且用户未登录或未授权，则会拉起用户登录或授权页面。  如果该值为false并且用户未登录，执行授权请求将返回[1001502001 用户未登录华为账号](account-api-error-code.md#section1001502001-用户未登录华为账号)。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| state | string | 否 | 是 | 请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| nonce | string | 否 | 是 | 请求体中的nonce参数，字符包含0-9、a-z、A-Z、点号、冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。该参数会包含在返回的ID Token中，通过校验一致性，可用于防止重放攻击。如该参数未传、传空，ID Token中nonce默认值：“default”。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| idTokenSignAlgorithm | [IdTokenSignAlgorithm](account-api-authentication.md#idtokensignalgorithm) | 否 | 是 | 默认值：PS256，用于指定ID Token的签名算法。应用根据实际安全要求、性能、系统环境兼容性进行选择。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| supportAtomicService | boolean | 否 | 是 | 在元服务场景下，当传入scopes包含profile时，是否支持获取用户头像昵称。  默认值：false。  如果该值为true，可以正常获取用户头像昵称。  如果该值为false，执行授权请求将返回[1001500003 不支持该scopes或permissions](account-api-error-code.md#section1001500003-不支持该scopes或permissions)。  **起始版本**：5.1.1(19)  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。  **说明：** 用于元服务场景调用。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { util } from '@kit.ArkTS';

4. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
5. authRequest.scopes = ['profile']; // 元服务可传supportAtomicService值为true，以使用profile授权能力
6. authRequest.permissions = ['idtoken'];
7. authRequest.forceAuthorization = true;
8. authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
9. authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;
```

## AuthorizationWithHuaweiIDResponse

PhonePC/2in1TabletTVWearable

该类封装[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)授权请求对象获取的用户信息结果。作为华为账号授权成功的返回结果，用于获取或关联华为账号用户信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** AuthorizationWithHuaweiIDResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| data | [AuthorizationWithHuaweiIDCredential](account-api-authentication.md#authorizationwithhuaweiidcredential) | 是 | 是 | 用户授权结果数据，用于获取或关联华为账号用户信息。 |
| state | string | 是 | 是 | 响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建授权请求，并设置参数
7. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
8. // 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
9. authRequest.scopes = ['openid'];
10. authRequest.permissions = ['idtoken', 'serviceauthcode'];
11. authRequest.forceAuthorization = true;
12. authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
13. authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

15. // 执行授权请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
19. controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
20. if (error) {
21. dealAllError(error);
22. return;
23. }
24. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
25. const state = authorizationWithHuaweiIDResponse.state;
26. if (state && authRequest.state !== state) {
27. // state不一致，可能为跨站攻击，需重新授权
28. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
29. return;
30. }
31. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
32. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
33. const idToken = authorizationWithHuaweiIDCredential?.idToken;
34. const code = authorizationWithHuaweiIDCredential?.authorizationCode;
35. // 开发者处理idToken, code等信息
36. });
37. } catch (error) {
38. dealAllError(error);
39. }

41. // 错误处理
42. function dealAllError(error: BusinessError<Object>): void {
43. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
44. // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
45. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
46. // 用户未登录华为账号，请登录华为账号并重试
47. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
48. // 网络异常，请检查当前网络状态并重试
49. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
50. // 用户取消授权
51. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
52. // 系统服务异常，请稍后重试
53. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
54. // 重复请求，应用无需处理
55. } else {
56. // 获取用户信息失败，请稍后重试
57. }
58. }

60. export enum ErrorCode {
61. // 账号未登录
62. ERROR_CODE_LOGIN_OUT = 1001502001,
63. // 网络错误
64. ERROR_CODE_NETWORK_ERROR = 1001502005,
65. // 用户取消授权
66. ERROR_CODE_USER_CANCEL = 1001502012,
67. // 系统服务异常
68. ERROR_CODE_SYSTEM_SERVICE = 12300001,
69. // 重复请求
70. ERROR_CODE_REQUEST_REFUSE = 1001500002
71. }
```

## AuthorizationWithHuaweiIDCredential

PhonePC/2in1TabletTVWearable

Account Kit授权成功返回的凭据，用于获取用户相关信息（头像昵称、匿名手机号等）和关联华为账号（OpenID/UnionID）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| authorizationCode | string | 是 | 是 | Authorization Code。临时凭据，用于获取Access Token。有效时间5分钟，并且只能使用1次。长度限制1-1024。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的permissions中传入'serviceauthcode'参数时返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| idToken | string | 是 | 是 | ID Token。JWT格式的字符串，包含用户信息，用于应用获取部分用户相关信息及验证签名。长度限制1-2048。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的permissions中传入'idtoken'参数时返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| openID | string | 是 | 是 | OpenID。OpenID是华为账号用户在不同类型的产品的身份ID，同一个用户不同应用，OpenID值不同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：默认返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| unionID | string | 是 | 是 | UnionID。UnionID是华为账号用户在同一个开发者账号下产品的身份ID，同一个用户，同一个开发者账号下管理的不同应用，UnionID值相同。具体格式要求请参考[OpenID和UnionID的格式说明](../harmonyos-guides/account-faq-9.md)。  **返回场景**：默认返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| avatarUri | string | 是 | 是 | 用户头像链接，有效期较短，建议先将头像下载保存后再使用。  没有长度限制，格式例如：https://xxx/xxx。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中传入'profile'参数时返回。  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| nickName | string | 是 | 是 | 用户昵称。长度限制2-20个字符。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中传入'profile'参数时返回。  **元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。 |
| email | string | 是 | 是 | 用户邮箱。长度限制4-254。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中传入'email'参数时返回。  **说明：** 元服务不支持该字段。 |
| authorizedScopes | string[] | 是 | 是 | 本次授权成功的scope清单，通过设置对应scope授权成功后返回Authorization Code来获取对应用户信息。  **返回场景**：默认返回'openid'。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| extraInfo | Record<string, Object> | 是 | 是 | 扩展信息。可能的key值有quickLoginAnonymousPhone和localNumberConsistency。  如果开发者开启了[代码混淆](../harmonyos-guides/source-obfuscation-guide.md)需要配置混淆白名单防止其中包含的属性被混淆。  **返回场景**：[AuthorizationWithHuaweiIDRequest](account-api-authentication.md#authorizationwithhuaweiidrequest)接口的scopes中传入扩展请求参数（'quickLoginAnonymousPhone'等）时返回。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**  1. 华为账号一键登录场景下，可通过"localNumberConsistency"字段获取华为账号绑定手机号和用户本机SIM卡手机号对比结果：  true：华为账号绑定的手机号和本机SIM卡手机号一致。  false：华为账号绑定的手机号和本机SIM卡手机号不一致。  2. 若用户本机无SIM卡，返回false。  若用户本机有SIM卡，只要其中有1张SIM卡手机号比对成功即返回true，否则返回false。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建授权请求，并设置参数
7. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
8. // 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
9. authRequest.scopes = ['openid'];
10. authRequest.permissions = ['idtoken', 'serviceauthcode'];
11. authRequest.forceAuthorization = true;
12. authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
13. authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

15. // 执行授权请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
19. controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
20. if (error) {
21. dealAllError(error);
22. return;
23. }
24. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
25. const state = authorizationWithHuaweiIDResponse.state;
26. if (state && authRequest.state !== state) {
27. // state不一致，可能为跨站攻击，需重新授权
28. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
29. return;
30. }
31. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
32. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
33. const idToken = authorizationWithHuaweiIDCredential?.idToken;
34. const code = authorizationWithHuaweiIDCredential?.authorizationCode;
35. // 开发者处理idToken, code等信息
36. });
37. } catch (error) {
38. dealAllError(error);
39. }

41. // 错误处理
42. function dealAllError(error: BusinessError<Object>): void {
43. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
44. // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
45. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
46. // 用户未登录华为账号，请登录华为账号并重试
47. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
48. // 网络异常，请检查当前网络状态并重试
49. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
50. // 用户取消授权
51. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
52. // 系统服务异常，请稍后重试
53. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
54. // 重复请求，应用无需处理
55. } else {
56. // 获取用户信息失败，请稍后重试
57. }
58. }

60. export enum ErrorCode {
61. // 账号未登录
62. ERROR_CODE_LOGIN_OUT = 1001502001,
63. // 网络错误
64. ERROR_CODE_NETWORK_ERROR = 1001502005,
65. // 用户取消授权
66. ERROR_CODE_USER_CANCEL = 1001502012,
67. // 系统服务异常
68. ERROR_CODE_SYSTEM_SERVICE = 12300001,
69. // 重复请求
70. ERROR_CODE_REQUEST_REFUSE = 1001500002
71. }
```

## CancelAuthorizationRequest

PhonePC/2in1TabletTVWearable

该类为应用取消Account Kit授权的请求对象，作为华为账号取消授权的请求参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** CancelAuthorizationRequest继承自[AuthenticationRequest](account-api-authentication.md#authenticationrequest)。

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | string | 否 | 是 | 请求体中的state参数，开发者可自定义，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  该参数与响应体中返回的state比较，校验是否是当前请求，可防止跨站攻击。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { util } from '@kit.ArkTS';

4. const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
5. cancelRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
```

## CancelAuthorizationResponse

PhonePC/2in1TabletTVWearable

该类为应用取消华为账号授权的响应结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**继承：** CancelAuthorizationResponse继承自[AuthenticationResponse](account-api-authentication.md#authenticationresponse)。

**属性：**

| **名称** | **类型** | **只读** | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | string | 是 | 是 | 响应体中返回的state，字符包含0-9、a-z、A-Z、英文点号、英文冒号、斜杠、下划线等，长度限制1-255，校验规则^[0-9a-zA-Z:/\.\-\_]{1,255}$。  与请求体中传入的state比较，校验是否是当前请求，防止跨站攻击。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建取消授权请求，并设置参数
7. const cancelRequest = new authentication.HuaweiIDProvider().createCancelAuthorizationRequest();
8. cancelRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击

10. // 执行取消授权请求，并处理结果
11. try {
12. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
13. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
14. controller.executeRequest(cancelRequest, (error: BusinessError<Object>, data) => {
15. if (error) {
16. dealAllError(error);
17. return;
18. }
19. const cancelAuthorizationResponse = data as authentication.CancelAuthorizationResponse;
20. const state = cancelAuthorizationResponse.state;
21. if (state && cancelRequest.state !== state) {
22. // state不一致，可能为跨站攻击，需重新授权
23. hilog.error(0x0000, 'testTag', `Failed to cancel. The state is different, response state: ${state}`);
24. return;
25. }
26. hilog.info(0x0000, 'testTag', 'Succeeded in canceling.');
27. });
28. } catch (error) {
29. dealAllError(error);
30. }

32. // 错误处理
33. function dealAllError(error: BusinessError<Object>): void {
34. hilog.error(0x0000, 'testTag', `Failed to cancel. Code: ${error.code}, message: ${error.message}`);
35. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
36. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
37. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
38. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
39. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
40. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
41. // 登录失败，请尝试使用其他方式登录
42. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
43. // 用户取消授权
44. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
45. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
46. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
47. // 重复请求，应用无需处理
48. } else {
49. // 应用登录失败，请尝试使用其他方式登录
50. }
51. }

53. export enum ErrorCode {
54. // 账号未登录
55. ERROR_CODE_LOGIN_OUT = 1001502001,
56. // 网络错误
57. ERROR_CODE_NETWORK_ERROR = 1001502005,
58. // 内部错误
59. ERROR_CODE_INTERNAL_ERROR = 1001502009,
60. // 用户取消授权
61. ERROR_CODE_USER_CANCEL = 1001502012,
62. // 系统服务异常
63. ERROR_CODE_SYSTEM_SERVICE = 12300001,
64. // 重复请求
65. ERROR_CODE_REQUEST_REFUSE = 1001500002
66. }
```

## AuthenticationErrorCode

PhonePC/2in1TabletTVWearable

该枚举为登录、授权、取消授权等接口的错误码。应用可根据如下错误码进行不同的处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | 应用指纹证书校验失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| DUPLICATE\_REQUEST\_REJECTED | [1001500002](account-api-error-code.md#section1001500002-重复请求) | 重复请求，当已有相同的请求在处理时，返回此错误码，此错误码不需要处理。你的应用需实现点击控制，防止连续点击发起相同请求。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCOPE\_OR\_PERRMISSION\_UNSUPPORTED | [1001500003](account-api-error-code.md#section1001500003-不支持该scopes或permissions) | 不支持该scopes或permissions。  **起始版本**：5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| UNSUPPORTED | [1001500004](account-api-error-code.md#section1001500004-已登录的华为账号不支持该功能) | 已登录的华为账号不支持该功能。  **起始版本**：5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| REQUEST\_RESTRICTED | [1001500005](account-api-error-code.md#section1001500005-该功能被限制调用) | 该功能被限制调用。  **起始版本**：5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | 用户未登录华为账号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| APP\_NOT\_AUTHORIZED | [1001502002](account-api-error-code.md#section1001502002-应用未授权) | 应用未授权。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PARAMETER\_INVALID | [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | 输入参数值无效，接口传参异常等。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NETWORK\_ERROR | [1001502005](account-api-error-code.md#section1001502005-网络错误) | 网络异常。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| INTERNAL\_ERROR | [1001502009](account-api-error-code.md#section1001502009-内部错误) | 内部错误，如华为账号服务器错误或其他内部错误等。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| USER\_CANCELED | [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | 用户取消授权。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED | [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | 应用未申请scopes或permissions权限。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |

## AuthenticationController

PhonePC/2in1TabletTVWearable

该类为Account Kit登录授权、取消授权请求Controller。用于执行登录授权请求方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

### constructor

PhonePC/2in1TabletTVWearable

constructor(context?: common.Context)

构造器，构造Account Kit登录授权等请求Controller实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 否 | Context上下文，当需要拉起华为账号登录、授权页面时必须传该参数，否则会报[401](errorcode-universal.md#section401-参数检查失败)参数检查失败错误码。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  - 在4.0.0(10)版本，参数类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  - 从4.1.0(11)版本开始，参数类型为[Context](js-apis-inner-application-context.md)。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
4. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
```

### executeRequest

PhonePC/2in1TabletTVWearable

executeRequest(request: AuthenticationRequest, callback: AsyncCallback<AuthenticationResponse, Record<string, Object>>): void

执行Account Kit登录、授权等请求。使用callback异步回调。用于应用向华为账号请求登录、授权、取消授权等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [AuthenticationRequest](account-api-authentication.md#authenticationrequest) | 是 | 登录授权认证请求体。  如该参数未正确传入，会抛出[401](errorcode-universal.md#section401-参数检查失败)参数检查失败错误码。 |
| callback | AsyncCallback<[AuthenticationResponse](account-api-authentication.md#authenticationresponse), Record<string, Object>> | 是 | 登录授权回调函数。  当获取响应数据成功，err为undefined，data为获取到的[AuthenticationResponse](account-api-authentication.md#authenticationresponse)对象；否则为错误对象。  如该参数未正确传入，会抛出[401](errorcode-universal.md#section401-参数检查失败)参数检查失败错误码。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](account-api-error-code.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | Invalid input parameter value. |
| [1001502005](account-api-error-code.md#section1001502005-网络错误) | Network error. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | The user canceled the authorization. |
| [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |
| [1001500002](account-api-error-code.md#section1001500002-重复请求) | This error code is reported when a request is already being processed. |
| [1001500003](account-api-error-code.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported. |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建授权请求，并设置参数
7. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
8. // 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
9. authRequest.scopes = ['openid'];
10. authRequest.permissions = ['idtoken', 'serviceauthcode'];
11. authRequest.forceAuthorization = true;
12. authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
13. authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

15. // 执行授权请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
19. controller.executeRequest(authRequest, (error: BusinessError<Object>, data) => {
20. if (error) {
21. dealAllError(error);
22. return;
23. }
24. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
25. const state = authorizationWithHuaweiIDResponse.state;
26. if (state && authRequest.state !== state) {
27. // state不一致，可能为跨站攻击，需重新授权
28. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
29. return;
30. }
31. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
32. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
33. const idToken = authorizationWithHuaweiIDCredential?.idToken;
34. const code = authorizationWithHuaweiIDCredential?.authorizationCode;
35. // 开发者处理idToken, code等信息
36. });
37. } catch (error) {
38. dealAllError(error);
39. }

41. // 错误处理
42. function dealAllError(error: BusinessError<Object>): void {
43. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
44. // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
45. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
46. // 用户未登录华为账号，请登录华为账号并重试
47. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
48. // 网络异常，请检查当前网络状态并重试
49. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
50. // 用户取消授权
51. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
52. // 系统服务异常，请稍后重试
53. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
54. // 重复请求，应用无需处理
55. } else {
56. // 获取用户信息失败，请稍后重试
57. }
58. }

60. export enum ErrorCode {
61. // 账号未登录
62. ERROR_CODE_LOGIN_OUT = 1001502001,
63. // 网络错误
64. ERROR_CODE_NETWORK_ERROR = 1001502005,
65. // 用户取消授权
66. ERROR_CODE_USER_CANCEL = 1001502012,
67. // 系统服务异常
68. ERROR_CODE_SYSTEM_SERVICE = 12300001,
69. // 重复请求
70. ERROR_CODE_REQUEST_REFUSE = 1001500002
71. }
```

### executeRequest

PhonePC/2in1TabletTVWearable

executeRequest(request: AuthenticationRequest): Promise<AuthenticationResponse>

执行Account Kit登录授权等请求，使用Promise异步回调。用于应用向华为账号请求登录、授权、取消授权等场景。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [AuthenticationRequest](account-api-authentication.md#authenticationrequest) | 是 | 登录授权认证请求体。如该参数未正确传入，会抛出[401](errorcode-universal.md#section401-参数检查失败)参数检查失败错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthenticationResponse](account-api-authentication.md#authenticationresponse)> | 登录授权Promise对象，返回[AuthenticationResponse](account-api-authentication.md#authenticationresponse)对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](errorcode-account.md)和[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12300001](errorcode-account.md#section12300001-系统服务异常) | System service works abnormally. |
| [1001502001](account-api-error-code.md#section1001502001-用户未登录华为账号) | The user has not logged in with HUAWEI ID. |
| [1001502002](account-api-error-code.md#section1001502002-应用未授权) | The application is not authorized. |
| [1001502003](account-api-error-code.md#section1001502003-输入参数值无效) | Invalid input parameter value. |
| [1001502005](account-api-error-code.md#section1001502005-网络错误) | Network error. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1001500001](account-api-error-code.md#section1001500001-应用指纹证书校验失败) | Failed to check the fingerprint of the app bundle. |
| [1001502012](account-api-error-code.md#section1001502012-用户取消授权) | The user canceled the authorization. |
| [1001502014](account-api-error-code.md#section1001502014-应用未申请scopes或permissions权限) | The app does not have the required scopes or permissions. |
| [1001500002](account-api-error-code.md#section1001500002-重复请求) | This error code is reported when a request is already being processed. |
| [1001500003](account-api-error-code.md#section1001500003-不支持该scopes或permissions) | The scopes or permissions are not supported. |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建授权请求，并设置参数
7. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
8. // 'openid'为默认值可不传，开发者若需要获取其他用户信息，可传入其他scope参数，具体请参考AuthorizationWithHuaweiIDRequest类说明
9. authRequest.scopes = ['openid'];
10. authRequest.permissions = ['idtoken', 'serviceauthcode'];
11. authRequest.forceAuthorization = true;
12. authRequest.state = util.generateRandomUUID(); // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
13. authRequest.idTokenSignAlgorithm = authentication.IdTokenSignAlgorithm.PS256;

15. // 执行授权请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
19. controller.executeRequest(authRequest).then((data) => {
20. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
21. const state = authorizationWithHuaweiIDResponse.state;
22. if (state && authRequest.state !== state) {
23. // state不一致，可能为跨站攻击，需重新授权
24. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
25. return;
26. }
27. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
28. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
29. const idToken = authorizationWithHuaweiIDCredential?.idToken;
30. const code = authorizationWithHuaweiIDCredential?.authorizationCode;
31. // 开发者处理idToken, code等信息
32. }).catch((err: BusinessError) => {
33. dealAllError(err);
34. });
35. } catch (error) {
36. dealAllError(error);
37. }

39. // 错误处理
40. function dealAllError(error: BusinessError): void {
41. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
42. // 在涉及UI交互场景下，建议按照如下错误码指导提示用户
43. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
44. // 用户未登录华为账号，请登录华为账号并重试
45. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
46. // 网络异常，请检查当前网络状态并重试
47. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
48. // 用户取消授权
49. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
50. // 系统服务异常，请稍后重试
51. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
52. // 重复请求，应用无需处理
53. } else {
54. // 获取用户信息失败，请稍后重试
55. }
56. }

58. export enum ErrorCode {
59. // 账号未登录
60. ERROR_CODE_LOGIN_OUT = 1001502001,
61. // 网络错误
62. ERROR_CODE_NETWORK_ERROR = 1001502005,
63. // 用户取消授权
64. ERROR_CODE_USER_CANCEL = 1001502012,
65. // 系统服务异常
66. ERROR_CODE_SYSTEM_SERVICE = 12300001,
67. // 重复请求
68. ERROR_CODE_REQUEST_REFUSE = 1001500002
69. }
```

## AuthenticationRequest

PhonePC/2in1TabletTVWearable

华为账号登录授权认证请求父类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## AuthenticationResponse

PhonePC/2in1TabletTVWearable

华为账号登录授权认证请求响应父类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## AuthenticationProvider

PhonePC/2in1TabletTVWearable

华为账号登录授权认证请求provider父类对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 4.0.0(10)

## IdType

PhonePC/2in1TabletTVWearable

该枚举为ID类型枚举对象，作为华为账号登录状态请求参数传入。

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

PhonePC/2in1TabletTVWearable

该枚举为华为账号登录状态枚举对象。用于保存华为账号登录状态结果。

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

PhonePC/2in1TabletTVWearable

该类为获取华为账号登录状态请求对象，作为[getHuaweiIDState](account-api-authentication.md#gethuaweiidstate)传参。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-authentication.md#idtype) | 否 | 否 | 属性idValue的ID类型，当前非系统应用只能传IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 用户获取的UnionID、OpenID值，传递的类型通过idType属性定义。不可为空，否则会报[1001502003 输入参数值无效](account-api-error-code.md#section1001502003-输入参数值无效)错误码。长度限制1-256。  UnionID、OpenID值可以通过[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)、[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)、[LoginPanel](account-api-loginpanel.md#loginpanel)或[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)接口获取，具体方法参考其示例代码。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. // 创建请求参数
4. const request: authentication.StateRequest = {
5. idType: authentication.IdType.UNION_ID,
6. idValue: '<可通过华为账号登录接口获取>' // 该值可以通过华为账号登录接口获取
7. };
```

## StateResult

PhonePC/2in1TabletTVWearable

该类为获取华为账号登录状态结果对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | [State](account-api-authentication.md#state) | 否 | 否 | 华为账号登录状态枚举对象。用于保存华为账号登录状态结果。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 创建请求参数
6. const stateRequest: authentication.StateRequest = {
7. idType: authentication.IdType.UNION_ID,
8. idValue: '<可通过华为账号登录接口获取>' // 该值可以通过华为账号登录接口获取
9. };
10. try {
11. // 执行获取华为账号登录状态请求，并处理结果
12. new authentication.HuaweiIDProvider().getHuaweiIDState(stateRequest).then((data: authentication.StateResult) => {
13. hilog.info(0x0000, 'testTag', 'Succeeded in getting huaweiIdState result.');
14. const state = data.state;
15. // 处理state
16. }).catch((err: BusinessError) => {
17. dealAllError(err);
18. });
19. } catch (error) {
20. dealAllError(error);
21. }

23. // 错误处理
24. function dealAllError(error: BusinessError): void {
25. hilog.error(0x0000, 'testTag', `Failed to getHuaweiIdState, errorCode=${error.code}, errorMsg=${error.message}`);
26. }
```

## ConsistencyState

PhonePC/2in1TabletTVWearable

该枚举为手机号一致性状态枚举对象。应用可根据结果进行相应风控处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| CONSISTENT | 0 | 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备任意一个SIM卡手机号一致。 |
| INCONSISTENT\_WITH\_DEVICES | 1 | 华为账号已登录，传入的手机号与当前账号绑定的手机号一致，与当前设备SIM卡手机号不一致或当前设备无SIM卡。 |
| INCONSISTENT | 2 | 华为账号已登录，传入的手机号与当前账号绑定的手机号不一致。 |

## ConsistencyRequest

PhonePC/2in1TabletTVWearable

该类为获取手机号一致性状态请求对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-authentication.md#idtype) | 否 | 否 | 属性idValue的ID类型，当前非系统应用只能传IdType.UNION\_ID或IdType.OPEN\_ID。 |
| idValue | string | 否 | 否 | 用户的UnionID、OpenID值，不可为空，长度限制1-256，传递的类型通过idType属性定义。  UnionID、OpenID值可以通过[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)、[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)、[LoginPanel](account-api-loginpanel.md#loginpanel)或[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)接口获取，具体方法参考其示例代码。 |
| mobileNumber | string | 否 | 否 | 通过[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)组件的一键登录功能获取到的手机号，传入完整的手机号需要添加国家码，例如中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）为+86，值不可为空，长度限制1-256。  手机号示例：+86xxxxxxxxxxx（明文手机号）。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';

3. // 创建请求参数
4. const request: authentication.ConsistencyRequest = {
5. idType: authentication.IdType.UNION_ID,
6. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
7. mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
8. };
```

## ConsistencyResult

PhonePC/2in1TabletTVWearable

该类为获取手机号一致性状态结果对象。应用可根据结果进行相应风控处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.Auth

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| state | [ConsistencyState](account-api-authentication.md#consistencystate) | 否 | 否 | 手机号一致性状态枚举对象。 |

**示例：**

```
1. import { authentication } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 创建请求参数
6. const consistencyRequest: authentication.ConsistencyRequest = {
7. idType: authentication.IdType.UNION_ID,
8. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
9. mobileNumber: '+86xxxxxxxxxxx' // 通过华为账号一键登录功能获取到的明文手机号
10. };
11. try {
12. // 执行获取手机号一致性状态请求，并处理结果
13. new authentication.HuaweiIDProvider().getMobileNumberConsistency(consistencyRequest)
14. .then((data: authentication.ConsistencyResult) => {
15. hilog.info(0x0000, 'testTag', `Succeeded in getting getMobileNumberConsistency result = ${data.state}`);
16. const state = data.state;
17. // 处理state
18. })
19. .catch((err: BusinessError) => {
20. dealAllError(err);
21. });
22. } catch (error) {
23. dealAllError(error);
24. }

26. // 错误处理
27. function dealAllError(error: BusinessError): void {
28. hilog.error(0x0000, 'testTag',
29. `Failed to get mobileNumberConsistency, errorCode=${error.code}, errorMsg=${error.message}`);
30. }
```
