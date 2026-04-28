---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-extendservice
title: extendService (华为账号增强服务)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > extendService (华为账号增强服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccc5de00e8c2012328bb36cc26caf9f447b8e298768f930d70954d7fdcf64be5
---

本模块提供Account Kit的增强能力，包括身份验证、跳转账号中心等功能。

**起始版本：** 4.0.0(10)

说明

该服务目前仅对系统应用开放。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { extendService } from '@kit.AccountKit';
```

## IdType

PhonePC/2in1TabletTVWearable

该枚举为ID类型枚举对象。

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

PhonePC/2in1TabletTVWearable

该枚举为风险值枚举对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| LOW | 1 | 低风险 |
| HIGH | 2 | 高风险 |

## VerifyRequest

PhonePC/2in1TabletTVWearable

该类为身份验证请求对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| idType | [IdType](account-api-extendservice.md#idtype) | 否 | 否 | 属性idValue的ID类型。 |
| idValue | string | 否 | 否 | 用户获取的UnionID、OpenID值，传递的类型通过idType属性定义。长度限制1-256。  UnionID、OpenID值可以通过使用[LoginWithHuaweiIDResponse](account-api-authentication.md#loginwithhuaweiidresponse)、[AuthorizationWithHuaweiIDResponse](account-api-authentication.md#authorizationwithhuaweiidresponse)、[LoginPanel](account-api-loginpanel.md#loginpanel)或[LoginWithHuaweiIDButton](account-api-huawei-id-button.md#loginwithhuaweiidbutton)接口获取，具体方法参考其示例代码。 |
| sceneId | string | 否 | 否 | 身份验证的场景值，该值与riskLevel属性一起代表了应用在华为账号服务器上的一组配置，包括验证次数、首次验证方式、二次验证方式等。长度限制1-10。 |
| riskLevel | [RiskLevel](account-api-extendservice.md#risklevel) | 否 | 否 | 风险等级，该值与sceneId一起代表了应用在华为账号服务器上的一组配置，一般风险等级高的场景，需要进行二次验证。 |
| nonce | string | 否 | 否 | 请求体中的nonce参数，长度限制1-64。该参数会包含在返回的verifyToken中，通过校验一致性，可用于防止重放攻击。  推荐开发者用随机数并做一致性校验。建议生成方式：[util.generateRandomUUID()](js-apis-util.md#utilgeneraterandomuuid9)。 |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { util } from '@kit.ArkTS';

4. // 创建请求参数
5. const request: extendService.VerifyRequest = {
6. idType: extendService.IdType.UNION_ID,
7. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
8. sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
9. riskLevel: extendService.RiskLevel.LOW,
10. nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
11. }
```

## VerifyResult

PhonePC/2in1TabletTVWearable

该类为身份验证请求结果对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| verifyToken | string | 是 | 否 | 身份验证返回的Token，JWT格式的数据。 |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建请求参数
7. const request: extendService.VerifyRequest = {
8. idType: extendService.IdType.UNION_ID,
9. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录或授权接口获取
10. sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID
11. riskLevel: extendService.RiskLevel.LOW,
12. nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
13. }

15. // 执行身份验证请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error: BusinessError, data) => {
19. if (error) {
20. dealAllError(error);
21. return;
22. }
23. const verifyResult = data as extendService.VerifyResult;
24. hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
25. const verifyToken = verifyResult.verifyToken;
26. // 开发者处理verifyToken
27. });
28. } catch (error) {
29. dealAllError(error);
30. }

32. // 错误处理
33. function dealAllError(error: BusinessError): void {
34. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
35. }
```

## ExtendErrorCode

PhonePC/2in1TabletTVWearable

该枚举定义了Account Kit扩展模块错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.ExtendService

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INVALID\_PARAMETER | [401](errorcode-universal.md#section401-参数检查失败) | 参数检查失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| NETWORK\_ERROR | [1001600001](account-api-error-code.md#section1001600001-网络不可用) | 网络不可用。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| ACCOUNT\_NOT\_LOGGED\_IN | [1001600002](account-api-error-code.md#section1001600002-账号未登录) | 用户未登录华为账号。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PACKAGE\_FINGERPRINT\_CHECK\_ERROR | [1001600003](account-api-error-code.md#section1001600003-应用指纹证书校验失败) | 应用指纹证书校验失败。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| PERMISSION\_CHECK\_ERROR | [1001600004](account-api-error-code.md#section1001600004-应用未申请对应permissions权限) | 应用未申请对应permissions权限。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| USER\_CANCELED | [1001600005](account-api-error-code.md#section1001600005-用户取消当前操作) | 用户取消当前操作。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| VERIFICATION\_FACTOR\_UNAVAILABLE | [1001600006](account-api-error-code.md#section1001600006-当前设备不支持此验证要素) | 当前设备不支持此验证要素。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| INTERNAL\_ERROR | [1001600007](account-api-error-code.md#section1001600007-内部错误) | 内部错误。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| DEVICE\_NOT\_SUPPORTED | [1001600011](account-api-error-code.md#section1001600011-该设备不支持此api) | 该设备不支持此API。  **起始版本**：6.1.0(23)  **元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。 |

## verifyAccount

PhonePC/2in1TabletTVWearable

verifyAccount(context: common.Context, request: VerifyRequest, callback: AsyncCallback<VerifyResult>): void

执行Account Kit身份验证请求，使用Callback异步回调。

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

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1001600001](account-api-error-code.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](account-api-error-code.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](account-api-error-code.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](account-api-error-code.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600005](account-api-error-code.md#section1001600005-用户取消当前操作) | The user canceled the current operation. |
| [1001600006](account-api-error-code.md#section1001600006-当前设备不支持此验证要素) | The requested verification factors are unavailable on the device. |
| [1001600007](account-api-error-code.md#section1001600007-内部错误) | Internal error. |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建请求参数
7. const request: extendService.VerifyRequest = {
8. idType: extendService.IdType.UNION_ID,
9. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
10. sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
11. riskLevel: extendService.RiskLevel.LOW,
12. nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
13. }

15. // 执行身份验证请求，并处理结果
16. try {
17. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
18. extendService.verifyAccount(this.getUIContext().getHostContext(), request, (error, data) => {
19. if (error) {
20. dealAllError(error);
21. return;
22. }
23. const verifyResult = data as extendService.VerifyResult;
24. hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
25. const verifyToken = verifyResult.verifyToken;
26. // 开发者处理verifyToken
27. });
28. } catch (error) {
29. dealAllError(error);
30. }

32. // 错误处理
33. function dealAllError(error: BusinessError): void {
34. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
35. }
```

## verifyAccount

PhonePC/2in1TabletTVWearable

verifyAccount(context: common.Context, request: VerifyRequest): Promise<VerifyResult>

执行Account Kit身份验证请求，使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1001600001](account-api-error-code.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](account-api-error-code.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](account-api-error-code.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](account-api-error-code.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600005](account-api-error-code.md#section1001600005-用户取消当前操作) | The user canceled the current operation. |
| [1001600006](account-api-error-code.md#section1001600006-当前设备不支持此验证要素) | The requested verification factors are unavailable on the device. |
| [1001600007](account-api-error-code.md#section1001600007-内部错误) | Internal error. |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 创建请求参数
7. const request: extendService.VerifyRequest = {
8. idType: extendService.IdType.UNION_ID,
9. idValue: '<可通过华为账号登录接口获取>', // 该值可以通过华为账号登录接口获取
10. sceneId: '<触发身份认证的场景ID>', // 触发身份验证的场景ID，通过配置申请获取
11. riskLevel: extendService.RiskLevel.LOW,
12. nonce: util.generateRandomUUID() // 建议使用generateRandomUUID生成nonce
13. }

15. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
16. // 执行身份验证请求，并处理结果
17. extendService.verifyAccount(this.getUIContext().getHostContext(), request).then(data => {
18. const verifyResult = data as extendService.VerifyResult;
19. hilog.info(0x0000, 'testTag', 'Succeeded in verifying.');
20. const verifyToken = verifyResult.verifyToken;
21. // 开发者处理verifyToken
22. }).catch((error: BusinessError) => {
23. dealAllError(error);
24. })

26. // 错误处理
27. function dealAllError(error: BusinessError): void {
28. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
29. }
```

## startAccountCenter

PhonePC/2in1TabletTVWearable

startAccountCenter(context: common.Context, callback: AsyncCallback<void>): void

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Callback异步回调。

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

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001600001](account-api-error-code.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](account-api-error-code.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](account-api-error-code.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](account-api-error-code.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600007](account-api-error-code.md#section1001600007-内部错误) | Internal error. |
| [1001600011](account-api-error-code.md#section1001600011-该设备不支持此api) | This device does not support this API. |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 执行打开账号中心请求，并处理结果
6. try {
7. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
8. extendService.startAccountCenter(this.getUIContext().getHostContext(), (error: BusinessError) => {
9. if (error) {
10. dealAllError(error);
11. return;
12. }
13. hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
14. });
15. } catch (error) {
16. dealAllError(error);
17. }

19. // 错误处理
20. function dealAllError(error: BusinessError): void {
21. hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
22. }
```

## startAccountCenter

PhonePC/2in1TabletTVWearable

startAccountCenter(context: common.Context): Promise<void>

当开发者需要实现查看当前登录的华为账号的基本信息时，执行打开账号中心请求，会拉起账号中心页面，使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001600001](account-api-error-code.md#section1001600001-网络不可用) | The network is unavailable. |
| [1001600002](account-api-error-code.md#section1001600002-账号未登录) | The user has not logged in with HUAWEI ID. |
| [1001600003](account-api-error-code.md#section1001600003-应用指纹证书校验失败) | Failed to check the fingerprint of the application bundle. |
| [1001600004](account-api-error-code.md#section1001600004-应用未申请对应permissions权限) | The application does not have the required permissions. |
| [1001600007](account-api-error-code.md#section1001600007-内部错误) | Internal error. |
| [1001600011](account-api-error-code.md#section1001600011-该设备不支持此api) | This device does not support this API. |

**示例：**

```
1. import { extendService } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
6. // 执行打开账号中心请求，并处理结果
7. extendService.startAccountCenter(this.getUIContext().getHostContext()).then(() => {
8. hilog.info(0x0000, 'testTag', 'Succeeded in starting account center');
9. }).catch((error: BusinessError<Object>) => {
10. dealAllError(error);
11. })

13. // 错误处理
14. function dealAllError(error: BusinessError<Object>): void {
15. hilog.error(0x0000, 'testTag', `Failed to startAccountCenter. Code: ${error.code}, message: ${error.message}`);
16. }
```
