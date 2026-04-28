---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-updatemanager
title: updateManager（更新功能）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > updateManager（更新功能）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:374e481efea1bdd751094c0735d746f8fa6f1b5ae5afce5397003f36af1da08e
---

提供检测新版本及升级功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { updateManager } from '@kit.AppGalleryKit';
```

## UpdateAvailableCode

PhonePC/2in1TabletTVWearable

检测更新结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LATER\_VERSION\_NOT\_EXIST | 0 | 不存在新版本。 |
| LATER\_VERSION\_EXIST | 1 | 存在新版本。 |

## ShowUpdateResultCode

PhonePC/2in1TabletTVWearable

显示升级弹框结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW\_DIALOG\_SUCCESS | 0 | 显示升级弹框成功。 |
| SHOW\_DIALOG\_FAILURE | 1 | 显示升级弹框失败。 |

## CheckUpdateResult

PhonePC/2in1TabletTVWearable

检查是否有“更新”的接口调用结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| updateAvailable | [UpdateAvailableCode](store-updatemanager.md#updateavailablecode) | 是 | 否 | 检查结果。 |
| versionName | string | 是 | 是 | 版本名称，例如1.0.0.1。  **起始版本：** 6.0.0(20)  **说明：** 用于元服务场景调用。 |
| versionCode | number | 是 | 是 | 版本号，例如1001。  **起始版本：** 6.0.0(20)  **说明：** 用于元服务场景调用。 |

## RequestErrorCode

PhonePC/2in1TabletTVWearable

监听元服务更新检查接口结果码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_UPGRADE | 0 | 无最新版本。 |
| NEED\_UPGRADE | 1 | 有最新版本。 |
| DOWNLOADED | 2 | 下载完成。 |

## UpdateSessionState

PhonePC/2in1TabletTVWearable

监听元服务更新检查接口的回调结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [RequestErrorCode](store-updatemanager.md#requesterrorcode) | 是 | 否 | 检查结果码。 |
| checkUpdateResult | [CheckUpdateResult](store-updatemanager.md#checkupdateresult) | 是 | 是 | 检查结果。  **说明：** 仅在RequestErrorCode为NEED\_UPGRADE或NO\_UPGRADE时不为空。 |

## updateManager.checkAppUpdate

PhonePC/2in1TabletTVWearable

checkAppUpdate(context: common.UIAbilityContext): Promise<CheckUpdateResult>

检查是否有更新，使用Promise方式异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**设备行为差异：** 对于5.1.1(19)之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型上该接口返回的CheckUpdateResult中updateAvailable值固定为LATER\_VERSION\_NOT\_EXIST，无法检查出应用是否有更新。对于5.1.1(19)版本，该接口在Phone、Tablet、PC/2in1、TV中可正常调用，在其他设备类型上该接口返回的CheckUpdateResult中updateAvailable值固定为LATER\_VERSION\_NOT\_EXIST，无法检查出应用是否有更新。对于6.0.0(20)及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CheckUpdateResult](store-updatemanager.md#checkupdateresult)> | Promise对象，返回是否有更新检查结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009400001 | SA connect error. |
| 1009400002 | Request to service error. |
| 1009400003 | Network error. |
| 1009400004 | The application is not in the foreground. |
| 1009400005 | Not agreeing to the privacy agreement. |
| 1009400006 | Time limited. |
| 1009400007 | Other error. |

**示例：**

```
1. import { updateManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'checkAppUpdate test'

11. build() {
12. Row() {
13. Column() {
14. Text(this.message)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. try {
19. // 检查是否有更新,并返回是否有更新的检查结果
20. updateManager.checkAppUpdate(this.getUIContext().getHostContext() as common.UIAbilityContext)
21. .then((checkResult: updateManager.CheckUpdateResult) => {
22. hilog.info(0, 'TAG', "Succeeded in checking Result updateAvailable:" + checkResult.updateAvailable);
23. }).catch((error: BusinessError) => {
24. hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
25. });
26. } catch (error) {
27. hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
28. }
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

## updateManager.showUpdateDialog

PhonePC/2in1TabletTVWearable

showUpdateDialog(context: common.UIAbilityContext): Promise<ShowUpdateResultCode>

显示升级弹框，使用Promise方式异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**设备行为差异：** 对于5.1.1(19)之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型上该接口返回的ShowUpdateResultCode值固定为SHOW\_DIALOG\_FAILURE，无法弹出应用更新弹框。对于5.1.1(19)版本，该接口在Phone、Tablet、PC/2in1、TV中可正常调用，在其他设备类型上该接口返回的ShowUpdateResultCode值固定为SHOW\_DIALOG\_FAILURE，无法弹出应用更新弹框。对于6.0.0(20)及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 调用方应用的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShowUpdateResultCode](store-updatemanager.md#showupdateresultcode)> | Promise对象，返回显示升级弹框获取结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400004 | The application is not in the foreground. |
| 1009400005 | Not agreeing to the privacy agreement. |
| 1009400007 | Other error. |

**示例：**

```
1. import { updateManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'showUpdateDialog test'

11. build() {
12. Row() {
13. Column() {
14. Text(this.message)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. try {
19. // 显示升级弹框,返回显示升级弹框获取结果
20. updateManager.showUpdateDialog(this.getUIContext().getHostContext() as common.UIAbilityContext)
21. .then((resultCode: updateManager.ShowUpdateResultCode) => {
22. hilog.info(0, 'TAG', "Succeeded in showing UpdateDialog resultCode:" + resultCode);
23. })
24. .catch((error: BusinessError) => {
25. hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
26. });
27. } catch (error) {
28. hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
29. }
30. })
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

## updateManager.on('updateChange')

PhonePC/2in1TabletTVWearable

on(type: 'updateChange', callback: Callback<UpdateSessionState>, timeout?: number): void

监听元服务更新检查接口，检查到有/无更新后，使用callback方式返回结果。

说明

同一设备下元服务的调用次数不超过6次/天、每30分钟调用次数不超过1次。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"updateChange"。 |
| callback | Callback<[UpdateSessionState](store-updatemanager.md#updatesessionstate)> | 是 | 回调函数，使用Callback方式获取结果。 |
| timeout | number | 否 | 注册监听允许的最大监听时间（单位：s），取值范围：不大于20的正整数，如果不传，取默认值20。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400007 | Other error. |
| 1009400008 | The number of parameters for the on API is incorrect. |
| 1009400009 | The type parameter for the on API is invalid. |
| 1009400010 | The callback parameter for the on API is invalid. |
| 1009400011 | The timeout parameter for the on API is invalid. |

**示例：**

```
1. import { updateManager } from '@kit.AppGalleryKit';
2. import { abilityManager, common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'on'

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => this.callOn)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }

23. private callOn() {
24. // 监听元服务更新检查接口，检查到有/无更新后，使用callback方式返回结果。
25. let callback = (state: updateManager.UpdateSessionState) => {
26. if (state.code === updateManager.RequestErrorCode.NO_UPGRADE) {
27. hilog.info (0, 'TAG', `on success, no need update`);
28. updateManager.off('updateChange');
29. } else if (state.code === updateManager.RequestErrorCode.NEED_UPGRADE) {
30. hilog.info (0, 'TAG', `on success, need update`);
31. } else if (state.code === updateManager.RequestErrorCode.DOWNLOADED) {
32. hilog.info (0, 'TAG', `on success, need update and download success`);
33. updateManager.off('updateChange');
34. abilityManager.restartSelfAtomicService(this.getUIContext().getHostContext() as common.Context);
35. }
36. };
37. try {
38. // 监听元服务更新检查接口
39. updateManager.on('updateChange', callback, 20);
40. } catch (error) {
41. hilog.error(0, 'TAG', `on Error.code is ${error.code}, message is ${error.message}`);
42. }
43. }
44. }
```

## updateManager.off('updateChange')

PhonePC/2in1TabletTVWearable

off(type: 'updateChange', callback?: Callback<UpdateSessionState>): void

取消监听元服务更新检查接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Update

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值"updateChange"。 |
| callback | Callback<[UpdateSessionState](store-updatemanager.md#updatesessionstate)> | 否 | 回调函数，使用Callback的方式获取结果。不传该参数则会取消当前应用的所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1009400001 | SA connection error. |
| 1009400002 | Request to service error. |
| 1009400007 | Other error. |
| 1009400012 | The number of parameters for the off API is incorrect. |
| 1009400013 | The type parameter for the off API is invalid. |
| 1009400014 | The callback parameter for the off API is invalid. |

**示例：**

```
1. import { updateManager } from '@kit.AppGalleryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. try {
4. // 取消监听
5. updateManager.off('updateChange');
6. } catch (error) {
7. hilog.error(0, 'TAG', `moduleInstallManager.off onError.code is ${error.code}, message is ${error.message}`);
8. }
```
