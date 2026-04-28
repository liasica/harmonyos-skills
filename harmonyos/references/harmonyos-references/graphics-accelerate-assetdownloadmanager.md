---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager
title: assetDownloadManager（资源包下载管理）
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > ArkTS API > assetDownloadManager（资源包下载管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:15:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf6929942497f7bd41a5938cf9deed18fcd2271a9d0f4068530d064cfaf691d7
---

本模块提供资源包下载管理能力。

**起始版本：** 5.1.0(18)

## 导入模块

PhoneTablet

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
```

## DownloadFault

PhoneTablet

资源包下载失败原因的枚举。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAULT\_FILE\_ALREADY\_EXISTS | 0 | 资源包已存在。 |
| FAULT\_FILE\_ERROR | 1 | 文件操作失败。 |
| FAULT\_INSUFFICIENT\_SPACE | 2 | 用户设备的内存空间不足。 |
| FAULT\_DISCONNECT | 3 | 下载过程中链接丢失或断开。 |
| FAULT\_TIMEOUT | 4 | 下载超时，例如HTTP 408请求超时、或504网关超时。 |
| FAULT\_PROTOCOL | 5 | HTTP协议错误，例如HTTP 500服务器内部错误、或HTTP 400错误请求。 |
| FAULT\_DNS | 6 | DNS域名解析错误，无法解析服务器地址。 |
| FAULT\_SSL | 7 | SSL/TLS证书错误。 |
| FAULT\_REDIRECT | 8 | 重定向错误，例如超出最大重定向限制或无效的重定向URL。 |
| FAULT\_UNKNOWN | 9 | 未知错误。 |

## State

PhoneTablet

资源包下载任务状态的枚举。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CREATED | 0 | 已创建的下载任务。 |
| WAITING | 1 | 等待执行的下载任务。 |
| DOWNLOADING | 2 | 正在下载中的任务。 |
| PAUSED | 3 | 处于暂停状态的下载任务。 |
| FINISHED | 4 | 下载任务已完成。 |
| FAILED | 5 | 任务下载失败。 |

## AssetDownloadConfig

PhoneTablet

资源包下载任务的配置信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| identifier | string | 否 | 否 | 任务ID。下载任务的唯一标识。  最大长度64个字节。 |
| url | string | 否 | 否 | 当前下载任务URL，要求以http或者https开头，最大长度512个字节。  URL的域名需要符合域名白名单要求：  - 三方CDN：请前往AppGallery Connect查看已配置的CDN域名白名单。具体操作步骤请参见[创建下载任务](../harmonyos-guides/graphics-accelerate-assetdownload-release.md#创建下载任务)。  - 华为CDN：域名白名单将基于资源包下载任务自动配置。 |
| isEssential | boolean | 否 | 否 | 是否为必需资源：  - false：非必需资源。默认值。  - true：必需资源。  下载必需资源的优先级高于非必需资源。 |
| groupId | string | 否 | 是 | 组ID，用于标识资源的版本信息。  最大长度32个字节。  默认值：空字符串。 |
| fileName | string | 否 | 是 | 下载资源的文件名。若输入文件名，系统下载的临时文件将以该文件名命名，否则，文件名将以任务ID命名。  最大长度128个字节。  默认值：空字符串。 |
| begins | number | 否 | 是 | HTTP范围请求的起始字节位置。  默认值：0。 |
| ends | number | 否 | 是 | HTTP范围请求的结束字节位置。  默认值：0。  最小值需要大于等于begins。 |
| userData | string | 否 | 是 | 允许用户自定义的扩展字段。  最大长度1024个字节。  默认值：空字符串。 |

## AssetDownloadTask

PhoneTablet

资源包下载任务的信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| config | [AssetDownloadConfig](graphics-accelerate-assetdownloadmanager.md#assetdownloadconfig) | 是 | 否 | 资源包下载任务的配置信息，包含任务ID、URL、下载优先级等信息。 |
| taskId | string | 是 | 否 | 系统自动生成的任务ID，用于唯一标识下载任务。  最大长度36个字节。 |
| state | [State](graphics-accelerate-assetdownloadmanager.md#state) | 是 | 否 | 资源包下载任务的状态。 |

## DownloadProgressInfo

PhoneTablet

资源包下载任务的进度信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| downloadTask | [AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask) | 是 | 否 | 资源包下载任务的信息。 |
| totalBytesWritten | number | 是 | 否 | 待下载的资源总大小，单位：字节。  默认值：0。 |
| totalExpectedBytes | number | 是 | 否 | 已下载的资源总大小，单位：字节。  默认值：0。 |

## DownloadCompletedInfo

PhoneTablet

资源包下载任务的完成信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| downloadTask | [AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask) | 是 | 否 | 资源包下载任务的信息。 |
| filePath | string | 是 | 否 | 下载文件的本地沙箱地址。  最大长度512个字节。 |

## DownloadFailedInfo

PhoneTablet

资源包下载任务的失败信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| downloadTask | [AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask) | 是 | 否 | 资源包下载任务的信息。 |
| fault | [DownloadFault](graphics-accelerate-assetdownloadmanager.md#downloadfault) | 是 | 否 | 资源包下载失败的原因。 |

## assetDownloadManager.on('progress')

PhoneTablet

on(type: 'progress', callback: Callback<DownloadProgressInfo[]>): void

订阅资源包下载进度事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'progress'，表示资源包下载进度。 |
| callback | Callback<[DownloadProgressInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#downloadprogressinfo)> | 是 | 回调函数。返回任务进度信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo[]) => {
4. console.info('AssetAccelDemo', `onProgressCallback progressArray length: ${progressArray.length}`);
5. // 添加资源包下载进度处理逻辑。
6. };
7. // 订阅资源包下载进度事件。
8. assetDownloadManager.on("progress", onProgressCallback);
```

## assetDownloadManager.off('progress')

PhoneTablet

off(type: 'progress', callback?: Callback<DownloadProgressInfo[]>): void

取消订阅资源包下载进度事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'progress'，表示资源包下载进度。 |
| callback | Callback<[DownloadProgressInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#downloadprogressinfo)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo[]) => {
4. console.info('AssetAccelDemo', `onProgressCallback progressArray length: ${progressArray.length}`);
5. // 添加资源包下载进度处理逻辑。
6. };
7. // 取消订阅资源包下载进度事件。
8. assetDownloadManager.off("progress", onProgressCallback);
```

## assetDownloadManager.on('pause')

PhoneTablet

on(type: 'pause', callback: Callback<AssetDownloadTask>): void

订阅资源包下载暂停事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'pause'，表示资源暂停事件。 |
| callback | Callback<[AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask)> | 是 | 回调函数。返回任务信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
4. console.info('AssetAccelDemo', `task identifier = ${downloadTaskInfo.config.identifier} has paused.`);
5. // 添加资源包下载暂停处理逻辑。
6. };
7. // 订阅资源包下载暂停事件。
8. assetDownloadManager.on("pause", onPauseCallback);
```

## assetDownloadManager.off('pause')

PhoneTablet

off(type: 'pause', callback?: Callback<AssetDownloadTask>): void

取消订阅资源包下载暂停事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'pause'，表示资源暂停事件。 |
| callback | Callback<[AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
4. console.info('AssetAccelDemo', `task identifier = ${downloadTaskInfo.config.identifier} has paused.`);
5. // 添加资源包下载暂停处理逻辑。
6. };
7. // 取消订阅资源包下载暂停事件.
8. assetDownloadManager.off("pause", onPauseCallback);
```

## assetDownloadManager.on('complete')

PhoneTablet

on(type: 'complete', callback: Callback<DownloadCompletedInfo>): void

订阅资源包下载成功事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'complete'，表示资源包下载成功事件。 |
| callback | Callback<[DownloadCompletedInfo](graphics-accelerate-assetdownloadmanager.md#downloadcompletedinfo)> | 是 | 回调函数。返回任务完成信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
4. console.info('AssetAccelDemo', `task identifier = ${completeInfo.downloadTask.config.identifier} has completed.`);
5. // 添加资源包下载成功处理逻辑。
6. };
7. // 订阅资源包下载成功事件。
8. assetDownloadManager.on("complete", onCompleteCallback);
```

## assetDownloadManager.off('complete')

PhoneTablet

off(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void

取消订阅资源包下载成功事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'complete'，表示资源包下载成功事件。 |
| callback | Callback<[DownloadCompletedInfo](graphics-accelerate-assetdownloadmanager.md#downloadcompletedinfo)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
4. console.info('AssetAccelDemo', `task identifier = ${completeInfo.downloadTask.config.identifier} has completed.`);
5. // 添加资源包下载成功处理逻辑。
6. };
7. // 取消订阅资源包下载成功事件。
8. assetDownloadManager.off("complete", onCompleteCallback);
```

## assetDownloadManager.on('fail')

PhoneTablet

on(type: 'fail', callback: Callback<DownloadFailedInfo>): void

订阅资源包下载失败事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'fail'，表示资源包下载失败事件。 |
| callback | Callback<[DownloadFailedInfo](graphics-accelerate-assetdownloadmanager.md#downloadfailedinfo)> | 是 | 回调函数。返回任务失败信息。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
4. console.info('AssetAccelDemo', `task identifier = ${failedInfo.downloadTask.config.identifier} has failed.`);
5. // 添加资源包下载失败处理逻辑。
6. };
7. // 订阅资源包下载失败事件。
8. assetDownloadManager.on("fail", onFailedCallback);
```

## assetDownloadManager.off('fail')

PhoneTablet

off(type: 'fail', callback?: Callback<DownloadFailedInfo>): void

取消订阅资源包下载失败事件。使用callback形式返回结果。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 取消事件回调类型，固定为'fail'，表示资源包下载失败事件。 |
| callback | Callback<[DownloadFailedInfo](graphics-accelerate-assetdownloadmanager.md#downloadfailedinfo)> | 否 | 需要取消监听的回调函数，需与订阅时传入的回调函数一致。若不填，则取消当前监听该事件的所有回调函数。 |

**错误码**：

错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
4. console.info('AssetAccelDemo', `task identifier = ${failedInfo.downloadTask.config.identifier} has failed.`);
5. // 添加资源包下载失败处理逻辑。
6. };
7. // 取消订阅资源包下载失败事件。
8. assetDownloadManager.off("fail", onFailedCallback);
```

## assetDownloadManager.fetchManifestUrl

PhoneTablet

fetchManifestUrl(): Promise<string>

获取资源包下载列表。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。  - 若资源托管至华为CDN，返回资源包下载清单manifestUrl。  - 若资源托管至三方CDN，则返回空字符串。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

3. async fetchManifestUrl() {
4. let manifestUrl : string = '';
5. try {
6. manifestUrl = await assetDownloadManager.fetchManifestUrl();
7. console.info('AssetAccelDemo', `Succeeded in fetching manifestUrl, manifestUrl = ${manifestUrl}`);
8. } catch (error) {
9. console.error('AssetAccelDemo', `Failed to fetch manifestUrl, errCode: ${error.code}, errMessage: ${error.message}`);
10. return;
11. }
12. }
```

## assetDownloadManager.addAssetDownloadTask

PhoneTablet

addAssetDownloadTask(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string>

新增资源包下载任务。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.BaseContext](js-apis-inner-application-basecontext.md) | 是 | 应用程序上下文。 |
| downloadConfig | [AssetDownloadConfig](graphics-accelerate-assetdownloadmanager.md#assetdownloadconfig) | 是 | 资源包下载任务的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回下载任务taskID。  最大长度36个字节。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600001 | The domain name of the download task is not in the domain name trustlist. |
| 1016600004 | The application task queue is full. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async addAssetDownloadTask() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. try {
14. // 添加资源包下载任务。
15. // 根据实际代码上下文自行传入合适的context。
16. const taskId: string = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
17. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
18. } catch (error) {
19. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
20. }
21. }
```

## assetDownloadManager.pauseAssetDownloadTask

PhoneTablet

pauseAssetDownloadTask(taskId: string): Promise<void>

暂停资源包下载任务。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。  最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600003 | The current task status does not support the current operator. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async pauseAssetDownloadTask() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 根据taskId暂停资源包下载任务
25. await assetDownloadManager.pauseAssetDownloadTask(taskId);
26. console.info('AssetAccelDemo', `Succeeded in pausing assetDownloadTask`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. }
```

## assetDownloadManager.resumeAssetDownloadTask

PhoneTablet

resumeAssetDownloadTask(taskId: string): Promise<void>

恢复资源包下载任务。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。  最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600003 | The current task status does not support the current operator. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async resumeAssetDownloadTask() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 根据taskId暂停资源包下载任务
25. assetDownloadManager.pauseAssetDownloadTask(taskId);
26. console.info('AssetAccelDemo', `Succeeded in pausing assetDownloadTask`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. try {
32. // 根据taskId恢复资源包下载任务
33. await assetDownloadManager.resumeAssetDownloadTask(taskId);
34. console.info('AssetAccelDemo', `Succeeded in resuming assetDownloadTask`);
35. } catch (error) {
36. console.error('AssetAccelDemo', `Failed to resume assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
37. return;
38. }
39. }
```

## assetDownloadManager.removeAssetDownloadTask

PhoneTablet

removeAssetDownloadTask(taskId: string): Promise<void>

移除资源包下载任务。使用Promise异步回调。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| taskId | string | 是 | 任务ID。  最大长度36个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async removeAssetDownloadTask() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 根据taskId删除资源包下载任务
25. await assetDownloadManager.removeAssetDownloadTask(taskId);
26. console.info('AssetAccelDemo', `Succeeded in removing assetDownloadTask`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to remove assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. }
```

## assetDownloadManager.fetchAllAssetDownloadTasks

PhoneTablet

fetchAllAssetDownloadTasks(): Promise<AssetDownloadTask[]>

获取所有资源包下载任务，已下载完成的任务除外。使用Promise异步回调。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AssetDownloadTask[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadtask)> | Promise对象。返回资源包下载任务列表。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async fetchAllAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
24. try {
25. // 获取所有资源包下载任务信息。
26. downloadTaskArr = await assetDownloadManager.fetchAllAssetDownloadTasks();
27. console.info('AssetAccelDemo', `Succeeded in fetching allAssetDownloadTasks success, downloadTaskArr length:${downloadTaskArr.length}.`);
28. } catch (error) {
29. console.error('AssetAccelDemo', `Failed to fetch allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
30. return;
31. }
32. }
```

## assetDownloadManager.pauseAllAssetDownloadTasks

PhoneTablet

pauseAllAssetDownloadTasks(): Promise<void>

暂停所有资源包下载任务。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async pauseAllAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 暂停所有资源包下载任务。
25. await assetDownloadManager.pauseAllAssetDownloadTasks();
26. console.info('AssetAccelDemo', `Succeeded in pausing allAssetDownloadTasks`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. }
```

## assetDownloadManager.resumeAllAssetDownloadTasks

PhoneTablet

resumeAllAssetDownloadTasks(): Promise<void>

恢复所有资源包下载任务。使用Promise异步回调。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async resumeAllAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 暂停所有资源包下载任务。
25. await assetDownloadManager.pauseAllAssetDownloadTasks();
26. console.info('AssetAccelDemo', `Succeeded in pausing allAssetDownloadTasks`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. try {
32. // 恢复所有资源包下载任务。
33. await assetDownloadManager.resumeAllAssetDownloadTasks();
34. console.info('AssetAccelDemo', `Succeeded in resuming allAssetDownloadTasks`);
35. } catch (error) {
36. console.error('AssetAccelDemo', `Failed to resume allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
37. return;
38. }
39. }
```

## assetDownloadManager.removeAllAssetDownloadTasks

PhoneTablet

removeAllAssetDownloadTasks(): Promise<void>

移除所有资源包下载任务。使用Promise异步回调。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async removeAllAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. // 移除所有资源包下载任务。
25. await assetDownloadManager.removeAllAssetDownloadTasks();
26. console.info('AssetAccelDemo', `Succeeded in removing allAssetDownloadTasks`);
27. } catch (error) {
28. console.error('AssetAccelDemo', `Failed to remove allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
29. return;
30. }
31. }
```

## assetDownloadManager.fetchGroupAssetDownloadTasks

PhoneTablet

fetchGroupAssetDownloadTasks(groupId: string): Promise<AssetDownloadTask[]>

获取同一组的资源包下载任务。使用Promise异步回调。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。  最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AssetDownloadTask[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadtask)> | Promise对象。返回资源包下载任务列表。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async fetchGroupAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. let groupId = 'groupId';
24. let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
25. try {
26. // 获取同一groupId下的资源包下载任务信息。
27. downloadTaskArr = await assetDownloadManager.fetchGroupAssetDownloadTasks(groupId);
28. console.info('AssetAccelDemo', `Succeeded in fetching groupAssetDownloadTasks`);
29. } catch (error) {
30. console.error('AssetAccelDemo', `Failed to fetch groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
31. return;
32. }
33. }
```

## assetDownloadManager.pauseGroupAssetDownloadTasks

PhoneTablet

pauseGroupAssetDownloadTasks(groupId: string): Promise<void>

暂停同一组的资源包下载任务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。  最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async pauseGroupAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. let groupId = 'groupId';
24. try {
25. // 暂停同一groupId下的资源包下载任务。
26. await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
27. console.info('AssetAccelDemo', `Succeeded in pausing groupAssetDownloadTasks`);
28. } catch (error) {
29. console.error('AssetAccelDemo', `Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
30. return;
31. }
32. }
```

## assetDownloadManager.resumeGroupAssetDownloadTasks

PhoneTablet

resumeGroupAssetDownloadTasks(groupId: string): Promise<void>

恢复同一组的资源包下载任务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。  最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600000 | The API call from an ExtensionAbility is not allowed. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async resumeGroupAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. let groupId = 'groupId';
24. try {
25. // 暂停同一groupId下的资源包下载任务。
26. await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
27. console.info('AssetAccelDemo', `Succeeded in pausing groupAssetDownloadTasks`);
28. } catch (error) {
29. console.error('AssetAccelDemo', `Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
30. return;
31. }
32. try {
33. // 恢复同一groupId下的资源包下载任务。
34. await assetDownloadManager.resumeGroupAssetDownloadTasks(groupId);
35. console.info('AssetAccelDemo', `Succeeded in resuming groupAssetDownloadTasks`);
36. } catch (error) {
37. console.error('AssetAccelDemo', `Failed to resume groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
38. return;
39. }
40. }
```

## assetDownloadManager.removeGroupAssetDownloadTasks

PhoneTablet

removeGroupAssetDownloadTasks(groupId: string): Promise<void>

移除同一组的资源包下载任务。使用Promise异步回调。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| groupId | string | 是 | 组ID，用于标识资源的版本信息。  最大长度32个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1016600002 | The task ID or group ID entered during operations such as pause, resume, and fetch does not exist. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async removeGroupAssetDownloadTasks() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. let groupId = 'groupId';
24. try {
25. // 移除同一groupId下的资源包下载任务。
26. await assetDownloadManager.removeGroupAssetDownloadTasks(groupId);
27. console.info('AssetAccelDemo', `Succeeded in removing groupAssetDownloadTasks`);
28. } catch (error) {
29. console.error('AssetAccelDemo', `Failed to remove groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}`);
30. return;
31. }
32. }
```

## NetSpeedLevel

PhoneTablet

网络限速等级的枚举。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_LIMIT | 0 | 无速度限制。 |
| LIMIT\_MEDIUM | 1 | 中等速度限制。 |
| LIMIT\_LOW | 2 | 低等速度限制。 |

## assetDownloadManager.limitDownloadTaskSpeed

PhoneTablet

limitDownloadTaskSpeed(taskIds: string[], speedLimit: NetSpeedLevel): Promise<void>

限制资源包下载的速度。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| taskIds | string[] | 是 | 任务ID列表。 |
| speedLimit | [NetSpeedLevel](graphics-accelerate-assetdownloadmanager.md#netspeedlevel) | 是 | 网络限速等级。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | No Internet permission. |
| 401 | Parameter error. |
| 1016600094 | Task service ability error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { common } from '@kit.AbilityKit';

4. async limitDownloadTaskSpeed() {
5. // 构造资源包下载配置信息。
6. let assetDownload: assetDownloadManager.AssetDownloadConfig = {
7. fileName: 'fileName', // 下载资源的文件名。
8. url: 'url', // 下载资源url。
9. isEssential: false, // 是否是必要下载资源。
10. identifier: 'identifier', // 下载资源标识信息。
11. groupId: 'groupId' // 组ID，用于标识资源的版本信息。
12. }
13. let taskId: string = '';
14. try {
15. // 添加资源包下载任务。
16. // 根据实际代码上下文自行传入合适的context。
17. taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
18. console.info('AssetAccelDemo', `Succeeded in adding assetDownloadTask`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}`);
21. return;
22. }
23. try {
24. const taskIds: string[] = [taskId];
25. // 限制资源包下载任务的下载速度。
26. assetDownloadManager.limitDownloadTaskSpeed(taskIds, assetDownloadManager.NetSpeedLevel.LIMIT_MEDIUM);
27. console.info('AssetAccelDemo', `Succeeded in limiting downloadTaskSpeed`);
28. } catch (error) {
29. console.error('AssetAccelDemo', `Failed to limit downloadTaskSpeed, errCode:${error.code}, errMessage:${error.message}`);
30. return;
31. }
32. }
```

## AppDownloadStatus

PhoneTablet

应用自身下载器中资源包下载状态的枚举。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.1(19)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IN\_PROGRESS | 0 | 下载中。 |
| FINISH | 1 | 已完成下载。 |

## ResourceType

PhoneTablet

资源类型，影响下载完成通知的内容样式。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RELEASED | 0 | 已发布的资源，即已公开发布过的资源。  完成下载后，通知栏展示“xxx 游戏资源包已更新”。 |
| PRE\_RELEASE | 1 | 预发布的资源，即未公开发布过的资源。  完成下载后，通知栏展示“xxx 游戏资源包预下载已完成” |

## AppDownloadProgress

PhoneTablet

应用自身下载器中资源包的下载进度信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.1(19)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalBytesWritten | number | 否 | 否 | 已下载的资源总大小，单位：字节。取值范围：大于等于0。  默认值：0。 |
| totalExpectedBytes | number | 否 | 否 | 待下载的资源总大小，单位：字节。取值大于等于0，异常值按0处理。  默认值：0。 |
| totalFiles | number | 否 | 否 | 资源文件总数。取值大于等于0，异常值按0处理。  默认值：0。 |
| successCount | number | 否 | 否 | 已成功下载的文件数。取值大于等于0，异常值按0处理。  默认值：0。 |
| failureCount | number | 否 | 否 | 下载失败的文件数。取值大于等于0，异常值按0处理。  默认值：0。 |
| status | [AppDownloadStatus](graphics-accelerate-assetdownloadmanager.md#appdownloadstatus) | 否 | 否 | 当前应用自身下载器中的下载状态。 |
| resourceType | [ResourceType](graphics-accelerate-assetdownloadmanager.md#resourcetype) | 否 | 是 | 后台正在下载的资源类型，不同的资源类型决定了后台下载通知的内容样式。  默认值为RELEASED。  **起始版本：** 6.1.0(23) |

## assetDownloadManager.reportDownloadProgress

PhoneTablet

reportDownloadProgress(progressInfo: AppDownloadProgress): void

上报应用自身下载器中资源包的下载进度信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| progressInfo | [AppDownloadProgress](graphics-accelerate-assetdownloadmanager.md#appdownloadprogress) | 是 | 应用自身下载器中的下载进度信息。 |

**错误码**：

错误码的详细介绍请参见[ArkTS API错误码](graphics-accelerate-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1016600094 | Task service ability error. |
| 1016600401 | Parameter error. |

**示例**：

```
1. import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
2. import { deviceInfo } from '@kit.BasicServicesKit';

4. try {
5. let progressInfo: assetDownloadManager.AppDownloadProgress = {
6. totalBytesWritten: 0,
7. totalExpectedBytes: 0,
8. totalFiles: 0,
9. successCount: 0,
10. failureCount: 0,
11. status:assetDownloadManager.AppDownloadStatus.IN_PROGRESS
12. }
13. // 判断当前HarmonyOS SDK版本是否为6.1.0(23)及以上版本
14. if (deviceInfo.sdkApiVersion >= 23) {
15. progressInfo.resourceType = assetDownloadManager.ResourceType.RELEASED
16. }
17. assetDownloadManager.reportDownloadProgress(progressInfo);
18. console.info('AssetAccelDemo', `Succeeded in reporting downloadProgress`);
19. } catch (error) {
20. console.error('AssetAccelDemo', `Failed to report downloadProgress, errCode:${error.code}, errMessage:${error.message}`);
21. }
```
