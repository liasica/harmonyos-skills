---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay
title: @ohos.bundle.overlay (overlay模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.overlay (overlay模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:34+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:705f696fc9a73e04cd4a0e32527e7bfbf92b36787dce4d9f64ea7d9ca9a6db8d
---

本模块提供overlay特征应用的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)信息查询以及禁用使能的能力。

overlay特征应用指应用中包含有overlay资源包，overlay资源包详见[overlay机制](../harmonyos-guides/resource-categories-and-access.md#overlay机制)。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅适用于stage模型，且仅适用于[静态overlay](../harmonyos-guides/resource-categories-and-access.md#静态overlay配置方式)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { overlay } from '@kit.AbilityKit';
```

## overlay.setOverlayEnabled

PhonePC/2in1TabletTVWearable

setOverlayEnabled(moduleName:string, isEnabled: boolean): Promise<void>

设置当前应用中overlay特征module的禁用使能状态。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | overlay特征module的名称。 |
| isEnabled | boolean | 是 | 值为true表示使能，值为false表示禁用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let moduleName = "feature";
5. let isEnabled = false;

7. try {
8. overlay.setOverlayEnabled(moduleName, isEnabled)
9. .then(() => {
10. console.info('setOverlayEnabled success');
11. }).catch((err: BusinessError) => {
12. console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
13. });
14. } catch (err) {
15. let code = (err as BusinessError).code;
16. let message = (err as BusinessError).message;
17. console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
18. }
```

## overlay.setOverlayEnabled

PhonePC/2in1TabletTVWearable

setOverlayEnabled(moduleName: string, isEnabled: boolean, callback: AsyncCallback<void>): void

设置当前应用中overlay module的禁用使能状态。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | overlay特征module的名称。 |
| isEnabled | boolean | 是 | 值为true表示使能，值为false表示禁用。 |
| callback | AsyncCallback<void> | 是 | [回调函数](js-apis-base.md#asynccallback)，当设置指定module的overlay禁用使能状态成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let moduleName = "feature";
5. let isEnabled = false;

7. try {
8. overlay.setOverlayEnabled(moduleName, isEnabled, (err, data) => {
9. if (err) {
10. console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
11. return;
12. }
13. console.info('setOverlayEnabled success');
14. });
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
19. }
```

## overlay.getOverlayModuleInfo

PhonePC/2in1TabletTVWearable

getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay module的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)> | Promise对象，返回[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700032 | The specified bundle does not contain any overlay module. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let moduleName = "feature";

6. (async () => {
7. try {
8. let overlayModuleInfo = await overlay.getOverlayModuleInfo(moduleName);
9. console.info('overlayModuleInfo is ' + JSON.stringify(overlayModuleInfo));
10. } catch (err) {
11. let code = (err as BusinessError).code;
12. let message = (err as BusinessError).message;
13. console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
14. }
15. })();
```

## overlay.getOverlayModuleInfo

PhonePC/2in1TabletTVWearable

getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay特征module的名称。 |
| callback | AsyncCallback<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)> | 是 | [回调函数](js-apis-base.md#asynccallback)，当获取当前应用中指定的module的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)信息成功时，err返回undefined。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700032 | The specified bundle does not contain any overlay module. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let moduleName = "feature";

6. try {
7. overlay.getOverlayModuleInfo(moduleName, (err, data) => {
8. if (err) {
9. console.error('getOverlayModuleInfo failed due to err code : ' + err.code + ' ' + 'message :' + err.message);
10. return;
11. }
12. console.info('overlayModuleInfo is ' + JSON.stringify(data));
13. });
14. } catch (err) {
15. let code = (err as BusinessError).code;
16. let message = (err as BusinessError).message;
17. console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
18. }
```

## overlay.getTargetOverlayModuleInfos

PhonePC/2in1TabletTVWearable

getTargetOverlayModuleInfos(targetModuleName: string): Promise<Array<OverlayModuleInfo>>

获取指定的目标module所关联的OverlayModuleInfo。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用Promise异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetModuleName | string | 是 | 指定当前应用中的目标module的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)>> | Promise对象，返回<Array<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)>>。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700034 | The specified module is an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let targetModuleName = "feature";

6. (async () => {
7. try {
8. let overlayModuleInfos = await overlay.getTargetOverlayModuleInfos(targetModuleName);
9. console.info('overlayModuleInfos are ' + JSON.stringify(overlayModuleInfos));
10. } catch (err) {
11. let code = (err as BusinessError).code;
12. let message = (err as BusinessError).message;
13. console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
14. }
15. })();
```

## overlay.getTargetOverlayModuleInfos

PhonePC/2in1TabletTVWearable

getTargetOverlayModuleInfos(targetModuleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void

获取指定的目标module所关联的OverlayModuleInfo。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetModuleName | string | 是 | 指定当前应用中的目标module的名称。 |
| callback | AsyncCallback<Array<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)>> | 是 | [回调函数](js-apis-base.md#asynccallback)，当获取指定的目标module的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)成功时，err返回undefined。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700034 | The specified module is an overlay module. |

**示例：**

```
1. import { overlay } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let targetModuleName = "feature";

6. try {
7. overlay.getTargetOverlayModuleInfos(targetModuleName, (err, data) => {
8. if (err) {
9. console.error('getTargetOverlayModuleInfos failed due to err code : ' + err.code + ' ' + 'message :' +
10. err.message);
11. return;
12. }
13. console.info('overlayModuleInfo is ' + JSON.stringify(data));
14. });
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
19. }
```

## OverlayModuleInfo

PhonePC/2in1TabletTVWearable

type OverlayModuleInfo = \_OverlayModuleInfo.OverlayModuleInfo

OverlayModuleInfo信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

| 类型 | 说明 |
| --- | --- |
| [\_OverlayModuleInfo.OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md#overlaymoduleinfo-1) | OverlayModuleInfo信息。 |
