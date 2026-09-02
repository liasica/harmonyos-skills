---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay
title: "@ohos.bundle.overlay (overlay特征模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.bundle.overlay (overlay特征模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d697fd43adea8493153097e5b8262b792f6b910aa5e6506ecab7404bceb9c751
---

本模块提供overlay特征应用的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)信息查询以及禁用启用的能力。

overlay特征模块指的是当前模块中包含有overlay资源包，而当前模块所属的应用就是overlay特征应用，overlay资源包详见[overlay机制](../harmonyos-guides/resource-categories-and-access.md#overlay机制)。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅适用于stage模型，且仅适用于[静态overlay](../harmonyos-guides/resource-categories-and-access.md#静态overlay配置方式)。

## 导入模块

```ts
import { overlay } from '@kit.AbilityKit';
```

## overlay.setOverlayEnabled

setOverlayEnabled(moduleName:string, isEnabled: boolean): Promise<void>

设置当前应用中overlay特征模块的禁用启用状态。使用Promise异步回调。接口调用失败时可能返回null，需校验返回值后使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 当前应用中具有overlay特征模块名称。 |
| isEnabled | boolean | 是 | 值为true表示启用，值为false表示禁用。 |

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

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";
let isEnabled = false;

try {
  overlay.setOverlayEnabled(moduleName, isEnabled)
    .then(() => {
      console.info('setOverlayEnabled success');
    }).catch((err: BusinessError) => {
    console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
}
```

## overlay.setOverlayEnabled

setOverlayEnabled(moduleName: string, isEnabled: boolean, callback: AsyncCallback<void>): void

设置当前应用中overlay特征模块的禁用启用状态。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 当前应用中具有overlay特征模块名称。 |
| isEnabled | boolean | 是 | 值为true表示启用，值为false表示禁用。 |
| callback | AsyncCallback<void> | 是 | [AsyncCallback](js-apis-base.md#asynccallback)，当设置指定module的overlay禁用启用状态成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";
let isEnabled = false;

try {
  overlay.setOverlayEnabled(moduleName, isEnabled, (err, data) => {
    if (err) {
      console.error('setOverlayEnabled failed due to err code: ' + err.code + ' ' + 'message:' + err.message);
      return;
    }
    console.info('setOverlayEnabled success');
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('setOverlayEnabled failed due to err code: ' + code + ' ' + 'message:' + message);
}
```

## overlay.getOverlayModuleInfo

getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>

获取当前应用中overlay特征模块的OverlayModuleInfo信息。使用Promise异步回调。接口调用失败时可能返回null，需校验返回值后使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay特征模块的名称。 |

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

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

(async () => {
  try {
    let overlayModuleInfo = await overlay.getOverlayModuleInfo(moduleName);
    console.info('overlayModuleInfo is ' + JSON.stringify(overlayModuleInfo));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```

## overlay.getOverlayModuleInfo

getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void

获取当前应用中overlay特征模块的OverlayModuleInfo信息。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 指定当前应用中的overlay特征模块的名称。 |
| callback | AsyncCallback<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)> | 是 | [AsyncCallback](js-apis-base.md#asynccallback)，当获取当前应用中指定的module的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)信息成功时，err返回undefined。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700032 | The specified bundle does not contain any overlay module. |
| 17700033 | The specified module is not an overlay module. |

**示例：**

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

try {
  overlay.getOverlayModuleInfo(moduleName, (err, data) => {
    if (err) {
      console.error('getOverlayModuleInfo failed due to err code : ' + err.code + ' ' + 'message :' + err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
}
```

## overlay.getTargetOverlayModuleInfos

getTargetOverlayModuleInfos(targetModuleName: string): Promise<Array<OverlayModuleInfo>>

获取指定的目标module所关联的OverlayModuleInfo。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用Promise异步回调。接口调用失败时可能返回null，需校验返回值后使用。

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

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetModuleName = "feature";

(async () => {
  try {
    let overlayModuleInfos = await overlay.getTargetOverlayModuleInfos(targetModuleName);
    console.info('overlayModuleInfos are ' + JSON.stringify(overlayModuleInfos));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```

## overlay.getTargetOverlayModuleInfos

getTargetOverlayModuleInfos(targetModuleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void

获取指定的目标module所关联的OverlayModuleInfo。overlay特征的module一般是为设备上存在的非overlay特征的module提供覆盖的资源文件，其中非overlay特征的module被称作目标module。使用callback异步回调。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetModuleName | string | 是 | 指定当前应用中的目标module的名称。 |
| callback | AsyncCallback<Array<[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)>> | 是 | [AsyncCallback](js-apis-base.md#asynccallback)，当获取指定的目标module的[OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md)成功时，err返回undefined。否则回调函数返回具体错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[包管理子系统通用错误码](errorcode-bundle.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 17700002 | The specified module name is not found. |
| 17700034 | The specified module is an overlay module. |

**示例：**

```ts
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetModuleName = "feature";

try {
  overlay.getTargetOverlayModuleInfos(targetModuleName, (err, data) => {
    if (err) {
      console.error('getTargetOverlayModuleInfos failed due to err code : ' + err.code + ' ' + 'message :' +
      err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getTargetOverlayModuleInfos failed due to err code : ' + code + ' ' + 'message :' + message);
}
```

## OverlayModuleInfo

type OverlayModuleInfo = \_OverlayModuleInfo.OverlayModuleInfo

OverlayModuleInfo信息，包含overlay特征模块的名称、状态、目标模块等配置信息，用于描述和管理应用的资源覆盖配置。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

| 类型 | 说明 |
| --- | --- |
| [\_OverlayModuleInfo.OverlayModuleInfo](js-apis-bundlemanager-overlaymoduleinfo.md#overlaymoduleinfo-1) | OverlayModuleInfo信息。 |
