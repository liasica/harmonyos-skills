---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/preview-arkts-openfileboost-api
title: openFileBoost（文件打开加速）（已废弃）
breadcrumb: API参考 > 应用服务 > Preview Kit（文件预览服务） > ArkTS API > openFileBoost（文件打开加速）（已废弃）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:68ed4af63a8935d22d33a820d13c912730c45d1ef6afd97dfb1c67065a8e721b
---

本模块为应用提供文件打开加速状态感知能力。应用可以通过接入对应API，感知文件的加速状态，进而应用可以实现对已加速文件给出独特的UI（user interface）标识等功能，优化用户文件打开体验。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

## 导入模块

```typescript
import { openFileBoost } from '@kit.PreviewKit';
```

## FilePreloadState(deprecated)

表示文件预加载状态的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_PRELOADED | 0 | 文件未预加载。 |
| PRELOADING | 1 | 文件预加载中。 |
| PRELOADED | 2 | 文件预加载完成。 |

## FilePreloadStatusInfo(deprecated)

文件预加载回调返回的接口实例，表示文件的预加载状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sandboxPath | string | 否 | 否 | 文件的沙箱路径，字符长度范围：[1, 1024]。 |
| progress | number | 否 | 否 | 文件预加载进度。 |
| state | [FilePreloadState](preview-arkts-openfileboost-api.md#filepreloadstatedeprecated) | 否 | 否 | 文件预加载状态。 |

## openFileBoost.on('filePreloadStateChanged')(deprecated)

on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void

文件预加载状态回调，应用通过注册回调函数获取文件预加载的状态变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'filePreloadStateChanged'，每当预加载文件状态变化时都会触发该事件并返回对应信息。如填入'filePreloadStateChanged'以外的值，将注册成功但无法获取文件预加载的状态变化。 |
| callback | Callback<[FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated)> | 是 | 回调函数，用于应用获取预加载文件状态变化信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[模块错误码](errorcode-preview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017220001 | Internal failure. |
| 1017220002 | Service unavailable. |

**示例：**

示例中的filePreloadStatusInfo是系统回调传入的参数，详见上方[FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated)接口定义。

```typescript
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
    // 预加载过程中，应用可以根据自己设计对应UX
    console.info(`file is PRELOADING, suggest to show loading animation`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
    // 预加载完成，应用可以通过UX显示提示用户加速完成
    console.info(`file is PRELOADED, suggest to show loaded animation`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT_PRELOADED) {
    // 没有预加载，应用可以不显示任何额外UX
    console.info(`file is UNPRELOADED, suggest do not show animation `);
  }
}

openFileBoost.on('filePreloadStateChanged', callback);
```

## openFileBoost.off('filePreloadStateChanged')(deprecated)

off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void

文件预加载状态注销回调，通过注销回调函数取消获取文件预加载的状态变化。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调用类型，固定为'filePreloadStateChanged'，当预加载文件状态变化时会触发该事件并返回对应信息。如填入'filePreloadStateChanged'以外的值，将无法取消获取文件预加载的状态变化。 |
| callback | Callback<[FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[模块错误码](errorcode-preview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017220001 | Internal failure. |
| 1017220002 | Service unavailable. |

**示例：**

示例中的filePreloadStatusInfo是系统回调传入的参数，详见上方[FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated)接口定义。

```typescript
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  console.info(`on filePreloadStateChanged in callback1`);
}

function callback2(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  console.info(`on filePreloadStateChanged in callback2`);
}

function callback3(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  console.info(`on filePreloadStateChanged in callback3`);
}

  openFileBoost.on('filePreloadStateChanged', callback1);
  openFileBoost.on('filePreloadStateChanged', callback2);
  openFileBoost.on('filePreloadStateChanged', callback3);
  // 单独取消callback1的监听，传入callback1作为参数，后续不会再调用callback1的回调做通知
  openFileBoost.off('filePreloadStateChanged', callback1);
  // 取消所有callback的监听，不传第二个可选参数，后续不会再调用callback2和callback3做通知
  openFileBoost.off('filePreloadStateChanged');
```

## openFileBoost.addFile(deprecated)

addFile(file: string): void

监听一个文件的预加载状态，应用传入文件路径后系统开始监听该文件的预加载状态。后续该文件状态有变化时系统通过'filePreloadStateChanged'事件回调向应用返回文件预加载状态变化。需要先调用[openFileBoost.on('filePreloadStateChanged')](preview-arkts-openfileboost-api.md#openfileboostonfilepreloadstatechangeddeprecated)接口后再调用该接口添加文件预加载状态监听，且当前一个应用最多添加50个文件监听。

当前支持加速的文件类型见[文件打开加速支持的文件类型](../harmonyos-guides/preview-introduction.md#文件打开加速支持的文件类型)，不支持的文件类型默认为未预加载状态，不需要调用该接口监听文件预加载状态变更。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径，字符长度范围：[1, 1024]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[模块错误码](errorcode-preview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017220001 | Internal failure. |
| 1017220002 | Service unavailable. |
| 1017220003 | The number of files exceeds the upper limit. |

**示例：**

示例中的filePreloadStatusInfo是系统回调传入的参数，详见上方[FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated)接口定义。

```typescript
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';

const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";

function fileStateChangedCallback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  console.info(`on filePreloadStateChanged, state: ${filePreloadStatusInfo.state}`);
}

openFileBoost.on('filePreloadStateChanged', fileStateChangedCallback);
openFileBoost.addFile(file);
```

## openFileBoost.removeFile(deprecated)

removeFile(file: string): void

取消监听一个文件的预加载状态，取消后文件的预加载状态变化不会通过回调再通知应用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径，字符长度范围：[1, 1024]。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[模块错误码](errorcode-preview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017220001 | Internal failure. |
| 1017220002 | Service unavailable. |

**示例：**

```typescript
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';

const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
openFileBoost.removeFile(file);
```

## openFileBoost.queryFilePreloadStatusInfo(deprecated)

queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo

查询文件预加载状态，传入文件路径，通过返回值返回该文件当前的预加载状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.5(17)

**废弃版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 文件的沙箱路径，字符长度范围：[1, 1024]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FilePreloadStatusInfo](preview-arkts-openfileboost-api.md#filepreloadstatusinfodeprecated) | 文件预加载状态信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[模块错误码](errorcode-preview.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 1017220001 | Internal failure. |
| 1017220002 | Service unavailable. |

**示例：**

```typescript
import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';

const file: string = "/storage/Users/currentUser/Desktop/10MB_file.docx";
let statusInfo: openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
console.info(`file, ${statusInfo.sandboxPath}, progress:${statusInfo.progress}  preloadState:${statusInfo.state}`);
```
