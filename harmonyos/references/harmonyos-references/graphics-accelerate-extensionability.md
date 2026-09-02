---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-extensionability
title: AssetAccelerationExtensionAbility（资源加速ExtensionAbility）
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > ArkTS API > AssetAccelerationExtensionAbility（资源加速ExtensionAbility）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c277a6f01fbf3a60190f3402c100575cda79ab9c6f79e6e70e99d10ec462d2b
---

本模块为资源包后台下载框架，为资源包后台下载提供关键的生命周期函数。在后台下载任务成功、失败、结束后支持调用相应的回调函数。

**起始版本：** 5.1.0(18)

## 约束限制

本模块存在如下约束：

* AssetAccelerationExtensionAbility为轻量、独立的子进程，不允许唤醒主进程。
* assetDownloadManager提供的接口仅支持调用如下方法：

  + [assetDownloadManager.fetchManifestUrl](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchmanifesturl)
  + [assetDownloadManager.removeAssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerremoveassetdownloadtask)
  + [assetDownloadManager.fetchAllAssetDownloadTasks](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchallassetdownloadtasks)
  + [assetDownloadManager.removeAllAssetDownloadTasks](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerremoveallassetdownloadtasks)
  + [assetDownloadManager.fetchGroupAssetDownloadTasks](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerfetchgroupassetdownloadtasks)
  + [assetDownloadManager.removeGroupAssetDownloadTasks](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerremovegroupassetdownloadtasks)
  + [assetDownloadManager.limitDownloadTaskSpeed](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerlimitdownloadtaskspeed)
  + [assetDownloadManager.reportDownloadProgress](graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerreportdownloadprogress)
* 为保障系统安全性和稳定性，防止AssetAccelerationExtensionAbility滥用系统资源，系统对其能力进行管控，不支持以下模块的引用：

  + [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)
  + [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)
  + [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md)
  + [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md)
  + [@ohos.multimedia.media (媒体服务)](arkts-apis-media.md)

## 导入模块

```typescript
import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';
```

## AssetAccelerationExtensionInfo

资源加速ExtensionAbility信息。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| maxBackgroundDownloadSize | number | 是 | 否 | 最大的资源大小，单位：Byte。只有当用户设备剩余存储空间大于maxBackgroundDownloadSize的三倍时，资源加速ExtensionAbility才会使能。  默认值：0。  maxBackgroundDownloadSize为用户在AGC平台上申请资源预下载服务时填写的包体大小。 |
| domainList | string[] | 是 | 否 | 域名白名单列表。域名不在此列表中的下载任务将直接失败。 |

## ContentRequestType

type ContentRequestType = 'INSTALL' | 'UPDATE' | 'IDLE'

内容请求类型。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**模型约束：** 本模块接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| 'INSTALL' | 安装。 |
| 'UPDATE' | 更新。 |
| 'IDLE' | 空闲。 |

## AssetAccelerationExtensionAbility

资源加速扩展能力类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| context | [AssetAccelerationExtensionContext](graphics-accelerate-extensioncontext.md) | 否 | 否 | AssetAccelerationExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onDownloadContentRequest

onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]>

安装应用、更新应用、设备闲时，执行该方法，获取资源包下载任务列表。返回任务量不超过200条。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| requestType | [ContentRequestType](graphics-accelerate-extensionability.md#contentrequesttype) | 是 | 内容请求类型。 |
| manifestUrl | string | 是 | 资源包下载URL：  - 使用华为CDN托管资源，则此参数不为空。  - 使用三方CDN，则此参数为空。  默认值：空字符串。 |
| assetAccelerationExtensionInfo | [AssetAccelerationExtensionInfo](graphics-accelerate-extensionability.md#assetaccelerationextensioninfo) | 是 | 资源加速ExtensionAbility信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[assetDownloadManager.AssetDownloadConfig[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadconfig)> | Promise对象。返回资源包下载任务的配置信息列表，最多返回200条配置信息。 |

**示例**：

```typescript
import { common } from '@kit.AbilityKit';
import { assetDownloadManager, AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string,
    _assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo):
        Promise<assetDownloadManager.AssetDownloadConfig[]> {
    const context = this.context as common.ExtensionContext; // 若接口需要使用common.Context类型的上下文，可以从this.context中获取类型为common.ExtensionContext的上下文对象。
    console.info('AssetAccelDemo', `application file directory = ${context.filesDir}`);
    console.info('AssetAccelDemo', `onDownloadContentRequest enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.`);
    // 构造资源包下载配置信息，用于函数返回值。download对象字段为演示用途，不应用于生产环境直接调用。
    let downloadList: Array<assetDownloadManager.AssetDownloadConfig> = [];
    let download: assetDownloadManager.AssetDownloadConfig = {
        identifier: 'identifier', // 下载资源标识信息。
        url: 'url', // 下载资源url。
        isEssential: false, // 是否是必要下载资源。
        groupId:'groupId', // 组ID，用于标识资源的版本信息。
        fileName: 'fileName' // 下载资源的文件名。
      };
    downloadList.push(download);
    await Promise.resolve();
    return downloadList;
  }
}
```

### onDownloadWithAppControl

onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean>

安装应用、更新应用、设备闲时，执行该方法，触发extension协同下载，如果有资源包下载任务则返回true，否则返回false。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.1(19)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| requestType | [ContentRequestType](graphics-accelerate-extensionability.md#contentrequesttype) | 是 | 内容请求类型。 |
| manifestUrl | string | 是 | 资源包下载URL：  - 使用华为CDN托管资源，则此URL由系统提供。  - 使用三方CDN，则此参数为空。  默认值：空字符串。 |
| assetAccelerationExtensionInfo | [AssetAccelerationExtensionInfo](graphics-accelerate-extensionability.md#assetaccelerationextensioninfo) | 是 | 资源加速ExtensionAbility信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。  - 返回true：应用自身下载器已开启资源包下载。  - 返回false：应用自身下载器无下载任务。 |

**示例**：

```typescript
import { common } from '@kit.AbilityKit';
import { AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string,
    _assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean> {
    const context = this.context as common.ExtensionContext; // 若接口需要使用common.Context类型的上下文，可以从this.context中获取类型为common.ExtensionContext的上下文对象。
    console.info('AssetAccelDemo', `application file directory = ${context.filesDir}`);
    console.info('AssetAccelDemo', `onDownloadWithAppControl enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.`);
    // 如果有下载任务，则调用应用自身下载器进行资源下载，并返回true，否则返回false。
    // ...
    let hasDownloadTask = true;
    await Promise.resolve();
    return hasDownloadTask;
  }
}
```

### onBackgroundDownloadSucceeded

onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask, filePath: string): Promise<void>

在系统后台下载任务成功时，执行该方法，通知资源加速ExtensionAbility下载成功。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| downloadTask | [assetDownloadManager.AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask) | 是 | 下载任务信息。 |
| filePath | string | 是 | 下载文件的本地沙箱地址。位于应用程序缓存(cache)目录下。  示例路径如下：  /data/storage/el2/base/haps/entry/cache/asset\_acceleration/1.8.2/xxx.bin  最大长度512个字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```typescript
import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 接收后台资源包下载成功消息的接口。
  async onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask,
    filePath: string): Promise<void> {
    console.info('AssetAccelDemo', `onBackgroundDownloadSucceeded enter, taskId is ${downloadTask.taskId}, filePath = ${filePath}`);
    // 添加文件转移处理逻辑。
    await Promise.resolve();
  }
}
```

### onBackgroundDownloadFailed

onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask, fault: assetDownloadManager.DownloadFault): Promise<void>

在系统后台下载任务失败时，执行该方法，通知资源加速ExtensionAbility下载失败。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| downloadTask | [assetDownloadManager.AssetDownloadTask](graphics-accelerate-assetdownloadmanager.md#assetdownloadtask) | 是 | 下载任务信息。 |
| fault | [assetDownloadManager.DownloadFault](graphics-accelerate-assetdownloadmanager.md#downloadfault) | 是 | 下载失败的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```typescript
import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 接收后台资源包下载失败消息的接口。
  async onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask,
    fault: assetDownloadManager.DownloadFault): Promise<void> {
    console.info('AssetAccelDemo', `onBackgroundDownloadFailed enter, download url: ${downloadTask.config.url}, err: ${fault}`);
    // 添加下载异常处理逻辑
    await Promise.resolve();
  }
}
```

### onExtensionWillTerminate

onExtensionWillTerminate(error?: BusinessError<void>): Promise<void>

在资源加速ExtensionAbility生命周期即将结束时、调度异常退出后，执行该方法，通知关闭资源包后台下载功能。建议在该方法中执行资源清理等操作，请避免耗时操作。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.AssetAcceleration

**起始版本：** 5.1.0(18)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 否 | 错误码：  401：参数错误。  1016600005：资源加速ExtensionAbility方法执行超时。  1016600006：资源加速ExtensionAbility生命周期方法出现异常。  1016600094：服务异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// 此处以AssetAccelExtAbility继承AssetAccelerationExtensionAbility为例
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // 当AssetAccelerationExtensionAbility生命周期即将结束时、调度异常退出，会执行该回调
  async onExtensionWillTerminate(error?: BusinessError<void>): Promise<void> {
    // 添加资源清理等处理逻辑，请避免耗时操作
    if (!error) {
      console.info('AssetAccelDemo', `onExtensionWillTerminate enter, BusinessError is null;`);
      return;
    }
    console.error('AssetAccelDemo', `onExtensionWillTerminate enter, BusinessError: ${error?.code}, msg: ${error?.message}`);
    await Promise.resolve();
  }
}
```
