---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-realnameservice
title: realNameService(身份验证服务)
breadcrumb: API参考 > 应用服务 > Payment Kit（鸿蒙支付服务） > ArkTS API > realNameService(身份验证服务)
category: harmonyos-references
scraped_at: 2026-04-29T14:08:21+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:959878050cff26d5dd82ec5830170bfe65d3cb8287a65437ae6df27d64856647
---

本模块提供身份验证服务，包括“实名信息验证”、“实名信息授权”和“人脸核身实人验证”三种功能。

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

## 导入模块

PhoneTablet

```
1. import { realNameService } from '@kit.PaymentKit';
```

## startRealNameVerification

PhoneTablet

startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供实名信息验证功能，调用该方法后会拉起实名信息验证授权组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | common.[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md) | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考[实名信息预验证](payment-api-common-verification-preverify.md)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回实名信息验证ID，用于[实名信息验证结果查询](payment-api-common-verification-result.md)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { realNameService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestStartRealNameVerificationPromise() {
10. // 请使用开发者真实的预验证ID（preVerifyId）
11. let preVerifyId = '';
12. realNameService.startRealNameVerification(this.context, preVerifyId)
13. .then((verifyResultId: string) => {
14. // 验证成功
15. console.info(`succeeded in verifying, verifyResultId: ${verifyResultId}`);
16. })
17. }

19. build() {
20. Column() {
21. Button('requestStartRealNameVerificationPromise')
22. .type(ButtonType.Capsule)
23. .width('50%')
24. .margin(20)
25. .onClick(() => {
26. this.requestStartRealNameVerificationPromise();
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

## startRealNameAuth

PhoneTablet

startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>

该方法提供实名信息授权功能，调用该方法后会拉起实名信息授权组件，授权完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | common.[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md) | 是 | UIAbility上下文。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回实名信息授权ID，用于[实名信息授权结果查询](payment-api-common-auth-result.md)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { realNameService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestStartRealNameAuthPromise() {
10. realNameService.startRealNameAuth(this.context)
11. .then((realNameAuthId: string) => {
12. // 授权成功
13. console.info(`succeeded in authorizing, realNameAuthId: ${realNameAuthId}`);
14. })
15. }

17. build() {
18. Column() {
19. Button('requestStartRealNameAuthPromise')
20. .type(ButtonType.Capsule)
21. .width('50%')
22. .margin(20)
23. .onClick(() => {
24. this.requestStartRealNameAuthPromise();
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

## startFaceVerification

PhoneTablet

startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>

该方法提供人脸核身实人验证功能，调用该方法后会拉起人脸核身实人验证组件，验证完成后使用Promise异步返回。调用该方法前请确保网络已连接。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Payment.RealNameService

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | common.[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md) | 是 | UIAbility上下文。 |
| preVerifyId | string | 是 | 预验证ID。获取方式请参考[人脸核身实人预验证](payment-api-common-face-verifactaion-preverify.md)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回验证结果ID，用于[人脸核身实人验证结果查询](payment-api-common-face-verifactaion-result.md)。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](payment-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1020100000 | The application does not have the required capability. |
| 1020100001 | The user did not accept the agreement. |
| 1020100002 | The user canceled the operation. |
| 1020100003 | The pre-verify ID is invalid. |
| 1020100004 | The network is unavailable. |
| 1020100005 | System internal error. |
| 1020100006 | The camera permission is not granted. |
| 1020100007 | The liveness detection failed. |
| 1020100008 | The app ID does not match. |
| 1020100009 | The user ID does not match. |

**示例**：

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { realNameService } from '@kit.PaymentKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. requestStartFaceVerificationPromise() {
10. // 请使用开发者真实的预验证ID（preVerifyId）
11. let preVerifyId = '';
12. realNameService.startFaceVerification(this.context, preVerifyId)
13. .then((verifyResultId:string ) => {
14. // 人脸验证成功
15. console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
16. })
17. }

19. build() {
20. Column() {
21. Button('requestStartFaceVerificationPromise')
22. .type(ButtonType.Capsule)
23. .width('50%')
24. .margin(20)
25. .onClick(() => {
26. this.requestStartFaceVerificationPromise();
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```
