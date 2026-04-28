---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-metadataoutput
title: Interface (MetadataOutput)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (MetadataOutput)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d24996289afe824e6fab55c4ae327ca86a23dba360ba7970a1387648f730ede6
---

metadata流。继承[CameraOutput](arkts-apis-camera-cameraoutput.md)。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## start

PhonePC/2in1TabletTVWearable

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
4. metadataOutput.start((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to start metadata output, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback returned with metadata output started.');
10. });
11. }
```

## start

PhonePC/2in1TabletTVWearable

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function startMetadataOutput(metadataOutput: camera.MetadataOutput): void {
4. metadataOutput.start().then(() => {
5. console.info('Callback returned with metadata output started.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to metadata output start, error code: ${error.code}`);
8. });
9. }
```

## stop

PhonePC/2in1TabletTVWearable

stop(callback: AsyncCallback<void>): void

停止输出metadata，通过注册回调函数获取结果。使用callback异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止输出metadata成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
4. metadataOutput.stop((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to stop the metadata output, error code: ${err.code}.`);
7. return;
8. }
9. console.info('Callback returned with metadata output stopped.');
10. })
11. }
```

## stop

PhonePC/2in1TabletTVWearable

stop(): Promise<void>

停止输出metadata。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function stopMetadataOutput(metadataOutput: camera.MetadataOutput): void {
4. metadataOutput.stop().then(() => {
5. console.info('Callback returned with metadata output stopped.');
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to metadata output stop, error code: ${error.code}`);
8. });
9. }
```

## on('metadataObjectsAvailable')

PhonePC/2in1TabletTVWearable

on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void

监听检测到的metadata对象，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'metadataObjectsAvailable'，metadataOutput创建成功后可监听。  检测到有效的metadata数据时，触发该事件发生并返回相应的metadata数据。如果输入错误字段，则不会创建有效监听。 |
| callback | AsyncCallback<Array<[MetadataObject](arkts-apis-camera-i.md#metadataobject)>> | 是 | 回调函数，用于获取metadata数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info('metadata output metadataObjectsAvailable');
9. }

11. function registerMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
12. metadataOutput.on('metadataObjectsAvailable', callback);
13. }
```

## off('metadataObjectsAvailable')

PhonePC/2in1TabletTVWearable

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

```
1. function unregisterMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
2. metadataOutput.off('metadataObjectsAvailable');
3. }
```

## on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

监听metadata流的错误，通过注册回调函数获取结果。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'error'，metadataOutput创建成功后可监听。metadata接口使用错误时触发该事件并返回对应错误码，比如调用[start](arkts-apis-camera-metadataoutput.md#start-1)，[CameraOutput.release](arkts-apis-camera-cameraoutput.md#release-1)接口时发生错误返回对应错误信息。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数，用于获取错误信息。返回错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(metadataOutputError: BusinessError): void {
4. console.error(`Metadata output error code: ${metadataOutputError.code}`);
5. }

7. function registerMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
8. metadataOutput.on('error', callback);
9. }
```

## off('error')

PhonePC/2in1TabletTVWearable

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

```
1. function unregisterMetadataOutputError(metadataOutput: camera.MetadataOutput): void {
2. metadataOutput.off('error');
3. }
```

## addMetadataObjectTypes23+

PhonePC/2in1TabletTVWearable

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function addMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
4. try {
5. metadataOutput.addMetadataObjectTypes(types);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`addMetadataObjectTypes error. error code: ${err.code}`);
10. }
11. }
```

## removeMetadataObjectTypes23+

PhonePC/2in1TabletTVWearable

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function removeMetadataObjectTypes(metadataOutput: camera.MetadataOutput, types: Array<camera.MetadataObjectType>): void {
4. try {
5. metadataOutput.removeMetadataObjectTypes(types);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`removeMetadataObjectTypes error. error code: ${err.code}`);
10. }
11. }
```
