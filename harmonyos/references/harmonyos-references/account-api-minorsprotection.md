---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-minorsprotection
title: minorsProtection (华为账号未成年人模式)
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > ArkTS API > minorsProtection (华为账号未成年人模式)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0547c4188adc02c11445b9538ae2c419aaf164bf76f279b2b8cc265ed7a081cd
---

当前模块提供Account Kit未成年人模式的相关能力，包括开启/关闭系统未成年人模式、获取系统未成年人模式的开启状态、年龄段信息等。开发者可调用本模块的能力，与系统未成年人模式联动，快速实现应用的未成年人模式的切换。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { minorsProtection } from '@kit.AccountKit';
```

## MinorsProtectionInfo

PhonePC/2in1TabletTV

该类提供未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minorsProtectionMode | boolean | 否 | 否 | 是否开启未成年人模式。  返回true表示未成年人模式为开启状态。  返回false表示未成年人模式为关闭状态。 |
| ageGroup | [AgeGroup](account-api-minorsprotection.md#agegroup) | 否 | 是 | 年龄段信息。  **说明：**  1. 仅当未成年人模式开启时才返回此字段。  2. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）儿童账号（14周岁及以下）开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)或[12,16)。  1. 如用户登录4周岁儿童账号，则返回年龄段信息为[3,8)。  2. 如用户登录9周岁儿童账号，则返回年龄段信息为[8,12)。  3. 当登录中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）非儿童账号开启未成年人模式，则可能返回年龄段信息为[0,3)、[3,8)、[8,12)、[12,16)或[16,18)。  1. 如用户创建13岁临时使用者，则返回年龄段信息为[12,16)。  2. 如用户创建17岁临时使用者，则返回年龄段信息为[16,18)。 |

## AgeGroup

PhonePC/2in1TabletTV

该类为年龄段信息对象。开发者可根据当前年龄段信息，展示适龄内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lowerAge | number | 否 | 否 | 年龄段下限，包含下限值。  **说明：** 该字段取值范围：0、3、8、12或16。 |
| upperAge | number | 否 | 否 | 年龄段上限，不包含上限值。  **说明：** 该字段取值范围：3、8、12、16或18。 |

## MinorsModeErrorCode

PhonePC/2in1TabletTV

该枚举为未成年人模式模块的错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| MINORS\_MODE\_NOT\_ENABLED | [1009900002](account-api-error-code.md#section1009900002-未成年人模式未开启) | 未成年人模式未开启。 |
| USER\_CANCELED | [1009900003](account-api-error-code.md#section1009900003-用户取消操作) | 用户取消操作。 |
| MINORS\_MODE\_ALREADY\_ON | [1009900005](account-api-error-code.md#section1009900005-未成年人模式已经开启) | 未成年人模式已经开启。 |
| MINORS\_MODE\_ALREADY\_OFF | [1009900006](account-api-error-code.md#section1009900006-未成年人模式已经关闭) | 未成年人模式已经关闭。 |
| UNSUPPORTED\_ACCOUNT | [1009900007](account-api-error-code.md#section1009900007-不支持的账号) | 不支持的账号。 |
| SERVICE\_NOT\_AVAILABLE | [1009900011](account-api-error-code.md#section1009900011-服务不可用) | 服务不可用。 |

## supportMinorsMode

PhonePC/2in1TabletTV

supportMinorsMode(): boolean

该方法为同步方法，调用该方法判断当前设备环境是否支持未成年人模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回boolean值。  返回true表示支持未成年人模式。  返回false表示不支持未成年人模式。  **说明：** 当登录海外华为账号、隐私空间均会返回false，其他场景均为true。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
5. try {
6. const supportMinorsMode: boolean = minorsProtection.supportMinorsMode();
7. hilog.info(0x0000, 'testTag', `Succeeded in getting supportMinorsMode is: ${supportMinorsMode.valueOf()}`);
8. } catch (error) {
9. hilog.error(0x0000, 'testTag',
10. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
11. }
12. } else {
13. hilog.info(0x0000, 'testTag',
14. 'The current device does not support the invoking of the supportMinorsMode interface.');
15. }
```

## getMinorsProtectionInfoSync

PhonePC/2in1TabletTV

getMinorsProtectionInfoSync(): MinorsProtectionInfo

该方法为同步方法，调用该方法获取未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo) | 返回[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)对象。用于获取未成年人模式开启状态、年龄段信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
5. try {
6. if (minorsProtection.supportMinorsMode()) {
7. const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
8. minorsProtection.getMinorsProtectionInfoSync();
9. // 获取未成年人模式开启状态
10. const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
11. // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
12. hilog.info(0x0000, 'testTag',
13. `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
14. // 未成年人模式已开启，获取年龄段信息
15. if (minorsProtectionMode) {
16. const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
17. if (ageGroup) {
18. hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
19. hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
20. // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
21. }
22. } else {
23. // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
24. }
25. } else {
26. hilog.info(0x0000, 'testTag',
27. 'The current device environment does not support the youth mode, please check the current device environment.');
28. }
29. } catch (error) {
30. hilog.error(0x0000, 'testTag',
31. `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
32. errMessage: ${error.message}`);
33. }
34. } else {
35. hilog.info(0x0000, 'testTag',
36. 'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
37. }
```

## getMinorsProtectionInfo

PhonePC/2in1TabletTV

getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>

调用该方法获取未成年人模式的开启状态，以及年龄段信息。应用可跟随未成年人模式开启状态，进行开启/关闭应用的未成年人模式，使用年龄段信息，展示适龄内容。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)> | Promise对象，返回[MinorsProtectionInfo](account-api-minorsprotection.md#minorsprotectioninfo)对象。用于获取未成年人模式开启状态、年龄段信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
6. try {
7. if (minorsProtection.supportMinorsMode()) {
8. minorsProtection.getMinorsProtectionInfo()
9. .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
10. // 获取未成年人模式开启状态
11. const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
12. // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
13. hilog.info(0x0000, 'testTag',
14. `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
15. // 未成年人模式已开启，获取年龄段信息
16. if (minorsProtectionMode) {
17. const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
18. if (ageGroup) {
19. hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
20. hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
21. // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
22. }
23. } else {
24. // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
25. }
26. })
27. .catch((error: BusinessError<Object>) => {
28. dealGetMinorsInfoAllError(error);
29. });
30. } else {
31. hilog.info(0x0000, 'testTag',
32. 'The current device environment does not support the youth mode, please check the current device environment.');
33. }
34. } catch (error) {
35. hilog.error(0x0000, 'testTag',
36. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
37. }
38. } else {
39. hilog.info(0x0000, 'testTag',
40. 'The current device does not support the invoking of the getMinorsProtectionInfo interface.');
41. }

43. function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
44. hilog.error(0x0000, 'testTag', `Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}`);
45. }
```

## verifyMinorsProtectionCredential

PhonePC/2in1TabletTV

verifyMinorsProtectionCredential(context: common.Context): Promise<boolean>

当用户需要调整应用的未成年人模式相关设置时，调用该方法拉起未成年人模式密码验证页面，验证身份。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示密码验证通过；返回false表示密码验证未通过。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1009900002](account-api-error-code.md#section1009900002-未成年人模式未开启) | The minors mode is not enabled. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
6. try {
7. if (minorsProtection.supportMinorsMode()) {
8. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
9. minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
10. .then((result: boolean) => {
11. hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
12. // 使用结果判断验密是否通过，执行后续流程
13. })
14. .catch((error: BusinessError<Object>) => {
15. dealVerifyAllError(error);
16. });
17. } else {
18. hilog.info(0x0000, 'testTag',
19. 'The current device environment does not support the youth mode, please check the current device environment.');
20. }
21. } catch (error) {
22. hilog.error(0x0000, 'testTag',
23. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
24. }
25. } else {
26. hilog.info(0x0000, 'testTag',
27. 'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
28. }

30. function dealVerifyAllError(error: BusinessError<Object>): void {
31. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
32. }
```

## leadToTurnOnMinorsMode

PhonePC/2in1TabletTV

leadToTurnOnMinorsMode(context: common.Context): Promise<void>

应用提供开启未成年人模式入口，调用该方法拉起开启未成年人模式页面，引导用户开启未成年人模式。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1009900003](account-api-error-code.md#section1009900003-用户取消操作) | The user canceled the operation. |
| [1009900005](account-api-error-code.md#section1009900005-未成年人模式已经开启) | The minors mode is already on. |
| [1009900007](account-api-error-code.md#section1009900007-不支持的账号) | Unsupported HUAWEI ID. |
| [1009900011](account-api-error-code.md#section1009900011-服务不可用) | Service not available. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
6. try {
7. if (minorsProtection.supportMinorsMode()) {
8. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
9. minorsProtection.leadToTurnOnMinorsMode(this.getUIContext().getHostContext())
10. .then(() => {
11. // 接口调用完成，如需显示弹窗，请在此处处理
12. })
13. .catch((error: BusinessError<Object>) => {
14. dealTurnOnAllError(error);
15. });
16. } else {
17. hilog.info(0x0000, 'testTag',
18. 'The current device environment does not support the youth mode, please check the current device environment.');
19. }
20. } catch (error) {
21. hilog.error(0x0000, 'testTag',
22. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
23. }
24. } else {
25. hilog.info(0x0000, 'testTag',
26. 'The current device does not support the invoking of the leadToTurnOnMinorsMode interface.');
27. }

29. function dealTurnOnAllError(error: BusinessError<Object>): void {
30. hilog.error(0x0000, 'testTag', `Failed to leadToTurnOnMinorsMode. Code: ${error.code}, message: ${error.message}`);
31. }
```

## leadToTurnOffMinorsMode

PhonePC/2in1TabletTV

leadToTurnOffMinorsMode(context: common.Context): Promise<void>

应用提供关闭未成年人模式入口，调用该方法拉起关闭未成年人模式页面，引导用户关闭未成年人模式。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | Context上下文。  应用可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)和[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。不支持应用在半模态、弹出框、子窗口等非全页面组件中使用[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)调用。  元服务可支持的Context有：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS错误码](account-api-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1001502009](account-api-error-code.md#section1001502009-内部错误) | Internal error. |
| [1009900003](account-api-error-code.md#section1009900003-用户取消操作) | The user canceled the operation. |
| [1009900006](account-api-error-code.md#section1009900006-未成年人模式已经关闭) | The minors mode is already off. |
| [1009900011](account-api-error-code.md#section1009900011-服务不可用) | Service not available. |

**示例：**

```
1. import { minorsProtection } from '@kit.AccountKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
6. try {
7. if (minorsProtection.supportMinorsMode()) {
8. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
9. minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
10. .then(() => {
11. // 接口调用完成，如需显示弹窗，请在此处处理
12. })
13. .catch((error: BusinessError<Object>) => {
14. dealTurnOffAllError(error);
15. });
16. } else {
17. hilog.info(0x0000, 'testTag',
18. 'The current device environment does not support the youth mode, please check the current device environment.');
19. }
20. } catch (error) {
21. hilog.error(0x0000, 'testTag',
22. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
23. }
24. } else {
25. hilog.info(0x0000, 'testTag',
26. 'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
27. }

29. function dealTurnOffAllError(error: BusinessError<Object>): void {
30. hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
31. }
```
