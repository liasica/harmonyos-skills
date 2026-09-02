---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-metadataoutput
title: Interface (MetadataOutput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (MetadataOutput)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4a17d70e2798aaaadead55caca7981ca13570bc6cf3628ea93e618ff73b44d21
---

metadata流。继承[CameraOutput](arkts-apis-camera-cameraoutput.md)。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## start

start(callback: AsyncCallback<void>): void

开始输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始输出metadata成功，err为undefined，否则为错误对象。错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start metadata output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with metadata output started.');
  });
}
```

## start

start(): Promise<void>

开始输出metadata。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.start().then(() => {
    console.info('Callback returned with metadata output started.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to metadata output start, error code: ${error.code}`);
  });
}
```

## stop

stop(callback: AsyncCallback<void>): void

停止输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止输出metadata成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the metadata output, error code: ${err.code}.`);
      return;
    }
    console.info('Callback returned with metadata output stopped.');
  })
}
```

## stop

stop(): Promise<void>

停止输出metadata。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.stop().then(() => {
    console.info('Callback returned with metadata output stopped.');
  }).catch((error: BusinessError) => {
    console.error(`Failed to metadata output stop, error code: ${error.code}`);
  });
}
```

## on('metadataObjectsAvailable')

on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void

监听检测到的metadata对象，通过注册回调函数获取结果。使用callback异步回调。

**说明** 

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'metadataObjectsAvailable'，metadataOutput创建成功后可监听。  检测到有效的metadata数据时，触发该事件发生并返回相应的metadata数据。如果输入错误字段，则不会创建有效监听。 |
| callback | AsyncCallback<Array<[MetadataObject](arkts-apis-camera-i.md#metadataobject)>> | 是 | 回调函数，用于获取metadata数据。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info('metadata output metadataObjectsAvailable');
}

function registerMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.on('metadataObjectsAvailable', callback);
}
```

## off('metadataObjectsAvailable')

off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void

注销监听检测到的metadata对象。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'metadataObjectsAvailable'，metadataOutput创建成功后可监听。 |
| callback | AsyncCallback<Array<[MetadataObject](arkts-apis-camera-i.md#metadataobject)>> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ts
function unregisterMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.off('metadataObjectsAvailable');
}
```

## on('error')

on(type: 'error', callback: ErrorCallback): void

监听metadata流的错误，通过注册回调函数获取结果。使用callback异步回调。

**说明** 

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，metadataOutput创建成功后可监听。metadata接口使用错误时触发该事件并返回对应错误码，比如调用[start](arkts-apis-camera-metadataoutput.md#start-1)，[CameraOutput.release](arkts-apis-camera-cameraoutput.md#release-1)接口时发生错误返回对应错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function callback(metadataOutputError: BusinessError): void {
  console.error(`Metadata output error code: ${metadataOutputError.code}`);
}

function registerMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.on('error', callback);
}
```

## off('error')

off(type: 'error', callback?: ErrorCallback): void

注销监听metadata流的错误。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，metadataOutput创建成功后可监听。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```ts
function unregisterMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
  metadataOutput.off('error');
}
```

## addMetadataObjectTypes23+

addMetadataObjectTypes(types: Array<MetadataObjectType>): void

新增需要上报的检测对象类型。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array<[MetadataObjectType](arkts-apis-camera-e.md#metadataobjecttype)> | 是 | metadata流类型信息，通过getSupportedOutputCapability接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function addMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
  try {
    metadataOutput.addMetadataObjectTypes(types);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`addMetadataObjectTypes error. error code: ${err.code}`);
  }
}
```

## removeMetadataObjectTypes23+

removeMetadataObjectTypes(types: Array<MetadataObjectType>): void

删除需要上报的检测对象类型。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array<[MetadataObjectType](arkts-apis-camera-e.md#metadataobjecttype)> | 是 | metadata流类型信息，通过getSupportedOutputCapability接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function removeMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
  try {
    metadataOutput.removeMetadataObjectTypes(types);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`removeMetadataObjectTypes error. error code: ${err.code}`);
  }
}
```

## isLockMetadataObjectTrackingSupported

isLockMetadataObjectTrackingSupported(): boolean

检查设备是否支持锁定元数据对象（如猫脸、狗脸）追踪功能。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否支持锁定元数据对象追踪功能。true表示支持，false表示不支持。 |

**示例：**

```ts
function checkLockMetadataSupport(metadataOutput: camera.MetadataOutput): void {
  let isSupported: boolean = metadataOutput.isLockMetadataObjectTrackingSupported();
  console.info(`Lock metadata object tracking supported: ${isSupported}`);
}
```

## lockMetadataObjectTracking

lockMetadataObjectTracking(point: Point): void

锁定对特定元数据对象（如猫脸、狗脸）的追踪。

**说明** 

* 该功能以point所指向的点所在的对象为追踪对象，如果该点不存在追踪对象，则功能不生效。
* 被锁定追踪的对象离开取景范围超过三秒或调用解锁追踪后，锁定追踪自动取消。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](arkts-apis-camera-i.md#point) | 是 | 锁定元数据对象追踪的点位。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function lockMetadata(metadataOutput: camera.MetadataOutput, point: camera.Point): void {
  try {
    metadataOutput.lockMetadataObjectTracking(point);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`lockMetadataObjectTracking error. error code: ${err.code}`);
  }
}
```

## unlockMetadataObjectTracking

unlockMetadataObjectTracking(): void

解锁元数据对象（如猫脸、狗脸）追踪。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |
| 7400201 | Camera service fatal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function unlockMetadata(metadataOutput: camera.MetadataOutput): void {
  try {
    metadataOutput.unlockMetadataObjectTracking();
  } catch (error) {
    let err = error as BusinessError;
    console.error(`unlockMetadataObjectTracking error. error code: ${err.code}`);
  }
}
```
