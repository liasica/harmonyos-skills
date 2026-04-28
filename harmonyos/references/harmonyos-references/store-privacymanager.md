---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-privacymanager
title: privacyManager（隐私管理服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > privacyManager（隐私管理服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b3a66d9327a8a49d3f3c484d0d7c57dad2e62b7c53ba5e1658212ceafde3d3d
---

提供查询隐私链接地址、查询隐私签署状态、撤销同意记录、请求用户同意功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { privacyManager } from '@kit.AppGalleryKit';
```

## AppPrivacyMgmtType

PhonePC/2in1TabletTV

隐私管理类型的枚举。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSUPPORTED | 0 | 不支持。 |
| FULL\_MODE | 1 | 完整模式。 |

## AppPrivacyResultType

PhonePC/2in1TabletTV

隐私签署结果类型的枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISAGREED | 0 | 不同意隐私协议。 |
| FULL\_MODE\_AGREED | 1 | 同意完整模式。 |
| REQUIRE\_RESIGNING\_VERSION\_UPDATE | 2 | 协议发生变更，需要重新签署协议。 |

## AppPrivacyLinkType

PhonePC/2in1TabletTV

隐私链接类型的枚举。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIVACY\_STATEMENT\_LINK | 1 | 隐私声明链接。 |
| USER\_AGREEMENT\_LINK | 2 | 用户协议链接。 |

## AppPrivacyType

PhonePC/2in1TabletTV

隐私类型的枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIVACY\_AGREEMENT | 1 | 隐私协议。 |
| USER\_AGREEMENT | 2 | 用户协议。 |

## AppPrivacyMgmtInfo

PhonePC/2in1TabletTV

隐私管理信息。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AppPrivacyMgmtType](store-privacymanager.md#appprivacymgmttype) | 是 | 否 | 隐私管理类型。 |
| privacyInfo | [AppPrivacyLink](store-privacymanager.md#appprivacylink)[] | 是 | 否 | 隐私链接信息。 |

## AppPrivacyLink

PhonePC/2in1TabletTV

隐私链接。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AppPrivacyLinkType](store-privacymanager.md#appprivacylinktype) | 是 | 否 | 隐私链接类型。 |
| versionCode | number | 是 | 否 | 协议版本号。 |
| url | string | 是 | 否 | url地址。 |
| id | string | 是 | 否 | 隐私协议id。 |
| name | string | 是 | 是 | 用户协议的名称，当[AppPrivacyLinkType](store-privacymanager.md#appprivacylinktype)为USER\_AGREEMENT\_LINK时非可选。  **起始版本：** 5.0.2(14) |

## AppPrivacyResult

PhonePC/2in1TabletTV

隐私签署结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AppPrivacyType](store-privacymanager.md#appprivacytype) | 是 | 否 | 隐私类型。 |
| versionCode | number | 是 | 否 | 协议版本号。 |
| result | [AppPrivacyResultType](store-privacymanager.md#appprivacyresulttype) | 是 | 否 | 隐私签署结果。 |
| id | string | 是 | 否 | 隐私协议id。 |
| signingTimestamp | number | 是 | 是 | 隐私签署时间(单位:ms)。  **起始版本：** 5.0.2(14)  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |

## ConsentResult

PhonePC/2in1TabletTV

拉起标准化隐私弹框结果。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| results | [AppPrivacyResult](store-privacymanager.md#appprivacyresult)[] | 是 | 否 | 隐私签署结果。 |

## privacyManager.getAppPrivacyMgmtInfo

PhonePC/2in1TabletTV

getAppPrivacyMgmtInfo(): AppPrivacyMgmtInfo

查询隐私链接信息。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AppPrivacyMgmtInfo](store-privacymanager.md#appprivacymgmtinfo) | 隐私链接信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006700001 | System internal error. |
| 1006700003 | The application does not use privacy manager service. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { privacyManager } from '@kit.AppGalleryKit';

4. const TAG: string = 'getAppPrivacyMgmtInfo';

6. @Entry
7. @Component
8. struct GetAppPrivacyMgmtInfo {
9. @State result: string = '';
10. @State message: string = 'getAppPrivacyMgmtInfo';
11. build() {
12. Column() {
13. Button(this.message)
14. .onClick(() => {
15. this.query()
16. })
17. .width('100%')
18. Text(this.result)
19. .fontSize(15)
20. .fontWeight(FontWeight.Bold)
21. .margin(20)
22. }
23. .margin(16)
24. .height('100%')
25. .justifyContent(FlexAlign.Center)
26. }

28. query() {
29. this.result = '';
30. try {
31. // 查询隐私链接信息
32. let appPrivacyManageInfo: privacyManager.AppPrivacyMgmtInfo = privacyManager.getAppPrivacyMgmtInfo();
33. hilog.info(0, TAG, "GetAppPrivacyManageInfo type:" + appPrivacyManageInfo["type"]);
34. this.result += 'GetAppPrivacyManageInfo type：' + appPrivacyManageInfo["type"] + ";\n";
35. // 隐私链接信息数组
36. let privacyLinkInfoArray : privacyManager.AppPrivacyLink[] = appPrivacyManageInfo.privacyInfo;
37. hilog.info(0, TAG, "GetAppPrivacyManageInfo size = " + privacyLinkInfoArray.length);
38. for (let i = 0; i < privacyLinkInfoArray.length; i++) {
39. this.result += 'uri: ' + privacyLinkInfoArray[i]["url"] + ";\n";
40. }
41. } catch (error) {
42. hilog.error(0, TAG, `getAppPrivacyMgmtInfo failed. code is ${error.code}, message is ${error.message}`);
43. this.result = `getAppPrivacyMgmtInfo failed, error code: ${error.code}, error message: ${error.message}`;
44. }
45. }
46. }
```

## privacyManager.getAppPrivacyResult

PhonePC/2in1TabletTV

getAppPrivacyResult(): AppPrivacyResult[]

查询隐私签署状态。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AppPrivacyResult](store-privacymanager.md#appprivacyresult)[] | 隐私签署结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006700001 | System internal error. |
| 1006700003 | The application does not use privacy manager service. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { privacyManager } from '@kit.AppGalleryKit';

4. const TAG: string = 'getAppPrivacyResult';

6. @Entry
7. @Component
8. struct GetAppPrivacyResult {
9. @State result: string = '';
10. @State message: string = 'getAppPrivacyResult';
11. build() {
12. Column() {
13. Button(this.message)
14. .onClick(() => {
15. this.query()
16. })
17. .width('100%')
18. Text(this.result)
19. .fontSize(15)
20. .fontWeight(FontWeight.Bold)
21. .margin(20)
22. }
23. .margin(16)
24. .height('100%')
25. .justifyContent(FlexAlign.Center)
26. }

28. query() {
29. this.result = '';
30. try {
31. // 查询隐私签署状态
32. let appPrivacyResults: privacyManager.AppPrivacyResult[] = privacyManager.getAppPrivacyResult();
33. hilog.info(0, TAG, "getAppPrivacyResult size = " + appPrivacyResults.length);
34. if (appPrivacyResults.length == 0) {
35. this.result += 'privacy result is empty!';
36. return;
37. }
38. for (let i = 0; i < appPrivacyResults.length; i++) {
39. hilog.info(0, TAG, "getAppPrivacyResult type = " + appPrivacyResults[i]["type"] + ", version = " + appPrivacyResults[i]["versionCode"] + ", result = " + appPrivacyResults[i]["result"]);
40. this.result += 'getAppPrivacyResult type = ' + appPrivacyResults[i]["type"] + ", result = " + appPrivacyResults[i]["result"] + ";\n";
41. }
42. } catch (error) {
43. hilog.error(0, TAG, `getAppPrivacyResult failed. code is ${error.code}, message is ${error.message}`);
44. this.result = `getAppPrivacyResult failed, error code: ${error.code}, error message: ${error.message}`;
45. }
46. }
47. }
```

## privacyManager.disableService

PhonePC/2in1TabletTV

disableService(): void

撤销同意记录。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006700001 | System internal error. |
| 1006700002 | The specified service extension connect failed. |
| 1006700003 | The application does not use privacy manager service. |

**示例：**

```
1. import { privacyManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. privacyManager.disableService();
6. hilog.info(0, 'TAG', "Succeeded in disabling service.");
7. } catch (error) {
8. hilog.error(0, 'TAG', "DisableService exception code: " + error.code + ", exception message: " + error.message);
9. }
```

## privacyManager.requestAppPrivacyConsent

PhonePC/2in1TabletTV

requestAppPrivacyConsent(context:common.UIAbilityContext):Promise<ConsentResult>

通过拉起标准化隐私弹框请求用户同意，通过Promise异步回调。

**元服务API：** 从版本6.1.0(23)开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.PrivacyManager

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ConsentResult](store-privacymanager.md#consentresult)> | Promise对象，返回弹框结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1006700001 | System internal error. |
| 1006700003 | The application does not use privacy manager service. |

**示例：**

```
1. import { privacyManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import type { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'requestAppPrivacyConsent test'

11. build() {
12. Row() {
13. Column() {
14. Text(this.message)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. try {
19. const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
20. // 通过拉起标准化隐私弹框请求用户同意,返回弹框结果
21. privacyManager.requestAppPrivacyConsent(uiContext).then((consentResult : privacyManager.ConsentResult) => {
22. let appPrivacyResults: privacyManager.AppPrivacyResult[] = consentResult["results"];
23. for (let i = 0; i < appPrivacyResults.length; i++) {
24. hilog.info(0, 'TAG', "GetAppPrivacyResult type = " + appPrivacyResults[i]["type"] + ", version = " + appPrivacyResults[i]["versionCode"] + ", result = " + appPrivacyResults[i]["result"] + ", signingTimestamp = " + appPrivacyResults[i]["signingTimestamp"]);
25. }
26. }).catch((error: BusinessError<Object>) => {
27. hilog.error(0, 'TAG', `requestAppPrivacyConsent failed, Code: ${error.code}, message: ${error.message}`);
28. });
29. } catch (error) {
30. hilog.error(0, 'TAG', "requestAppPrivacyConsent exception code: " + error.code + ", exception message: " + error.message);
31. }
32. })
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }
```
