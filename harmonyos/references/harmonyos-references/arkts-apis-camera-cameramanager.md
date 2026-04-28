---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-cameramanager
title: Interface (CameraManager)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (CameraManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8f57d041fbece826e2ec5b4e5119e7af667e6c28a92e4ce56591a7e601fd9bb
---

相机管理器类，使用前需要通过[getCameraManager](arkts-apis-camera-f.md#cameragetcameramanager)接口获取相机管理实例。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getSupportedCameras

PhonePC/2in1TabletTVWearable

getSupportedCameras(): Array<CameraDevice>

获取支持的相机设备对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[CameraDevice](arkts-apis-camera-i.md#cameradevice)> | 相机设备列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getSupportedCameras(cameraManager: camera.CameraManager): Array<camera.CameraDevice> {
4. let cameras: Array<camera.CameraDevice> = [];
5. try {
6. cameras = cameraManager.getSupportedCameras();
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The getSupportedCameras call failed. error code: ${err.code}`);
10. }
11. return cameras;
12. }
```

## getSupportedSceneModes11+

PhonePC/2in1TabletTVWearable

getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>

获取指定的相机设备对象支持的模式，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | 相机设备，通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口获取。传参异常时，会返回错误码[7400101](errorcode-camera.md#section7400101-无效入参)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SceneMode](arkts-apis-camera-e.md#scenemode11)> | 相机支持的模式列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getSupportedSceneModes(cameraManager: camera.CameraManager, camera: camera.CameraDevice): Array<camera.SceneMode> {
4. let modes: Array<camera.SceneMode> = [];
5. try {
6. modes = cameraManager.getSupportedSceneModes(camera);
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The getSupportedSceneModes call failed. error code: ${err.code}`);
10. }
11. return modes;
12. }
```

## getSupportedOutputCapability11+

PhonePC/2in1TabletTVWearable

getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability

查询相机设备在指定模式下支持的输出能力，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | 相机设备，通过 [getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras) 接口获取。 |
| mode | [SceneMode](arkts-apis-camera-e.md#scenemode11) | 是 | 相机模式，通过 [getSupportedSceneModes](arkts-apis-camera-cameramanager.md#getsupportedscenemodes11) 接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraOutputCapability](arkts-apis-camera-i.md#cameraoutputcapability) | 相机输出能力。 |

**示例：**

```
1. function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): camera.CameraOutputCapability {
2. let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, sceneMode);
3. return cameraOutputCapability;
4. }
```

## getSupportedFullOutputCapability23+

PhonePC/2in1TabletTVWearable

getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability

查询指定相机在指定模式下支持的完整输出能力，包括未压缩图（YUV）、HEIF和HDR等能力。

说明

使用YUV，HEIF或HDR等能力前，需要先显式调用此方法确保获取完整输出能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | 相机设备信息，通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口获取。 |
| mode | [SceneMode](arkts-apis-camera-e.md#scenemode11) | 是 | 相机模式，通过[getSupportedSceneModes](arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraOutputCapability](arkts-apis-camera-i.md#cameraoutputcapability) | 相机输出能力。 |

**示例：**

```
1. import { camera } from '@kit.CameraKit';

3. function getSupportedFullOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager, sceneMode: camera.SceneMode): camera.CameraOutputCapability {
4. let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedFullOutputCapability(camera, sceneMode);
5. return cameraOutputCapability;
6. }
```

## isCameraMuted

PhonePC/2in1TabletTVWearable

isCameraMuted(): boolean

查询当前相机是否禁用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示相机被禁用，返回false表示相机未被禁用。 |

**示例：**

```
1. function isCameraMuted(cameraManager: camera.CameraManager): boolean {
2. let isMuted: boolean = cameraManager.isCameraMuted();
3. return isMuted;
4. }
```

## createCameraInput

PhonePC/2in1TabletTVWearable

createCameraInput(camera: CameraDevice): CameraInput

使用CameraDevice对象创建CameraInput实例，同步返回结果。

该接口使用前首先通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询当前设备支持的相机设备信息列表，开发者需要根据具体使用场景选择符合需求的相机设备，然后使用该接口创建CameraInput实例。

**需要权限：** ohos.permission.CAMERA

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | CameraDevice对象，通过 [getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras) 接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraInput](arkts-apis-camera-camerainput.md) | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
4. let cameraInput: camera.CameraInput | undefined = undefined;
5. try {
6. cameraInput = cameraManager.createCameraInput(camera);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The createCameraInput call failed. error code: ${err.code}`);
11. }
12. return cameraInput;
13. }
```

## createCameraInput

PhonePC/2in1TabletTVWearable

createCameraInput(position: CameraPosition, type: CameraType): CameraInput

根据相机位置和类型创建CameraInput实例，同步返回结果。

该接口使用前需要开发者根据应用具体使用场景自行指定相机位置和类型，例如打开前置相机进入自拍功能。

**需要权限：** ohos.permission.CAMERA

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-apis-camera-e.md#cameraposition) | 是 | 相机位置，首先通过 [getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras) 接口获取支持的相机设备对象，然后根据返回的相机设备对象获取设备位置信息。 |
| type | [CameraType](arkts-apis-camera-e.md#cameratype) | 是 | 相机类型，首先通过 [getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras) 接口获取支持的相机设备对象，然后根据返回的相机设备对象获取设备类型信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraInput](arkts-apis-camera-camerainput.md) | 返回CameraInput实例。接口调用失败会返回相应错误码，错误码类型为[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createCameraInput(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraInput | undefined {
4. let position: camera.CameraPosition = camera.cameraPosition;
5. let type: camera.CameraType = camera.cameraType;
6. let cameraInput: camera.CameraInput | undefined = undefined;
7. try {
8. cameraInput = cameraManager.createCameraInput(position, type);
9. } catch (error) {
10. // 失败返回错误码error.code并处理。
11. let err = error as BusinessError;
12. console.error(`The createCameraInput call failed. error code: ${err.code}`);
13. }
14. return cameraInput;
15. }
```

## createPreviewOutput

PhonePC/2in1TabletTVWearable

createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput

创建预览输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [Profile](arkts-apis-camera-i.md#profile) | 是 | 支持的预览配置信息，通过[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取。 |
| surfaceId | string | 是 | 从[XComponent](ts-basic-components-xcomponent.md)或者[ImageReceiver](arkts-apis-image-imagereceiver.md)组件获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PreviewOutput](arkts-apis-camera-previewoutput.md) | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createPreviewOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
4. let profile: camera.Profile = cameraOutputCapability.previewProfiles[0];
5. let previewOutput: camera.PreviewOutput | undefined = undefined;
6. try {
7. previewOutput = cameraManager.createPreviewOutput(profile, surfaceId);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The createPreviewOutput call failed. error code: ${err.code}`);
12. }
13. return previewOutput;
14. }
```

## createPreviewOutput12+

PhonePC/2in1TabletTVWearable

createPreviewOutput(surfaceId: string): PreviewOutput

创建无配置信息的预览输出对象，同步返回结果。该接口需配合[preconfig](arkts-apis-camera-photosession.md#preconfig12)一起使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 从[XComponent](ts-basic-components-xcomponent.md)或者[ImageReceiver](arkts-apis-image-imagereceiver.md)组件获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PreviewOutput](arkts-apis-camera-previewoutput.md) | PreviewOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createPreviewOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.PreviewOutput | undefined {
4. let previewOutput: camera.PreviewOutput | undefined = undefined;
5. try {
6. previewOutput = cameraManager.createPreviewOutput(surfaceId);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The createPreviewOutput call failed. error code: ${err.code}`);
11. }
12. return previewOutput;
13. }
```

## createPhotoOutput11+

PhonePC/2in1TabletTVWearable

createPhotoOutput(profile?: Profile): PhotoOutput

创建拍照输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [Profile](arkts-apis-camera-i.md#profile) | 否 | 支持的拍照配置信息，通过[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取。  API version 11时，该参数必填；从API version 12开始，如果使用[preconfig](arkts-apis-camera-photosession.md#preconfig12)进行预配置，传入profile参数会覆盖preconfig的预配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoOutput](arkts-apis-camera-photooutput.md) | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager): camera.PhotoOutput | undefined {
4. let profile: camera.Profile = cameraOutputCapability.photoProfiles[0];
5. let photoOutput: camera.PhotoOutput | undefined = undefined;
6. try {
7. photoOutput = cameraManager.createPhotoOutput(profile);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The createPhotoOutput call failed. error code: ${err.code}`);
12. }
13. return photoOutput;
14. }
```

## createVideoOutput

PhonePC/2in1TabletTVWearable

createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput

创建录像输出对象，同步返回结果。

在录像模式下，使能SDR或HDR\_VIVID拍摄效果时，CameraFormat与ColorSpace必须按照下列表格中的对应关系配置，若不满足表格中CameraFormat与ColorSpace配置，会导致预览异常等问题。

| SDR/HDR拍摄 | CameraFormat | ColorSpace |
| --- | --- | --- |
| SDR | CAMERA\_FORMAT\_YUV\_420\_SP | BT709\_LIMIT |
| HDR\_VIVID | CAMERA\_FORMAT\_YCRCB\_P010  CAMERA\_FORMAT\_YCBCR\_P010 | BT2020\_HLG\_LIMIT  BT2020\_HLG\_FULL |

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [VideoProfile](arkts-apis-camera-i.md#videoprofile) | 是 | 支持的录像配置信息，通过[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取。 |
| surfaceId | string | 是 | 从[AVRecorder](arkts-apis-media-avrecorder.md)获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoOutput](arkts-apis-camera-videooutput.md) | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createVideoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
4. let profile: camera.VideoProfile = cameraOutputCapability.videoProfiles[0];
5. let videoOutput: camera.VideoOutput | undefined = undefined;
6. try {
7. videoOutput = cameraManager.createVideoOutput(profile, surfaceId);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The createVideoOutput call failed. error code: ${err.code}`);
12. }
13. return videoOutput;
14. }
```

## createVideoOutput12+

PhonePC/2in1TabletTVWearable

createVideoOutput(surfaceId: string): VideoOutput

创建无配置信息的录像输出对象，同步返回结果。该接口需配合[preconfig](arkts-apis-camera-videosession.md#preconfig12)功能一起使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 从[AVRecorder](arkts-apis-media-avrecorder.md)获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoOutput](arkts-apis-camera-videooutput.md) | VideoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createVideoOutput(cameraManager: camera.CameraManager, surfaceId: string): camera.VideoOutput | undefined {
4. let videoOutput: camera.VideoOutput | undefined = undefined;
5. try {
6. videoOutput = cameraManager.createVideoOutput(surfaceId);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The createVideoOutput call failed. error code: ${err.code}`);
11. }
12. return videoOutput;
13. }
```

## createMetadataOutput

PhonePC/2in1TabletTVWearable

createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput

创建metadata流输出对象，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| metadataObjectTypes | Array<[MetadataObjectType](arkts-apis-camera-e.md#metadataobjecttype)> | 是 | metadata流类型信息，通过[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MetadataOutput](arkts-apis-camera-metadataoutput.md) | MetadataOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createMetadataOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): void {
4. let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
5. let metadataOutput: camera.MetadataOutput | undefined = undefined;
6. try {
7. metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`createMetadataOutput error. error code: ${err.code}`);
12. }
13. }
```

## createSession11+

PhonePC/2in1TabletTVWearable

createSession<T extends Session>(mode: SceneMode): T

创建指定SceneMode的Session实例，同步返回结果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SceneMode](arkts-apis-camera-e.md#scenemode11) | 是 | 相机支持的模式。如果传入的参数异常（如超出范围、传入null或未定义等），实际接口不会生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [T](arkts-apis-camera-session.md) | Session实例。接口调用失败会返回相应的错误码，错误码类型为[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3.Parameter verification failed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createSession(cameraManager: camera.CameraManager, mode: camera.SceneMode): camera.Session | undefined {
4. let photoSession: camera.PhotoSession | undefined = undefined;
5. try {
6. photoSession = cameraManager.createSession(mode) as camera.PhotoSession;
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`createCaptureSession error. error code: ${err.code}`);
11. }
12. return photoSession;
13. }
```

## on('cameraStatus')

PhonePC/2in1TabletTVWearable

on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void

相机设备状态回调，通过注册回调函数获取相机的状态变化。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。目前只支持对设备打开或者关闭会触发该事件并返回对应信息。 |
| callback | AsyncCallback<[CameraStatusInfo](arkts-apis-camera-i.md#camerastatusinfo)> | 是 | 回调函数，用于获取镜头状态变化信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error('cameraStatus with errorCode = ' + err.code);
6. return;
7. }
8. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
9. console.info(`status: ${cameraStatusInfo.status}`);
10. }

12. function registerCameraStatus(cameraManager: camera.CameraManager): void {
13. cameraManager.on('cameraStatus', callback);
14. }
```

## off('cameraStatus')

PhonePC/2in1TabletTVWearable

off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void

相机设备状态注销回调，通过注销回调函数取消获取相机的状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'cameraStatus'。cameraManager对象获取成功后可监听。 |
| callback | AsyncCallback<[CameraStatusInfo](arkts-apis-camera-i.md#camerastatusinfo)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterCameraStatus(cameraManager: camera.CameraManager): void {
2. cameraManager.off('cameraStatus');
3. }
```

## on('foldStatusChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void

注册折叠设备折叠状态变化的监听。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | AsyncCallback<[FoldStatusInfo](arkts-apis-camera-i.md#foldstatusinfo12)> | 是 | 回调函数。返回折叠设备折叠信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, foldStatusInfo: camera.FoldStatusInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error('foldStatusChange with errorCode = ' + err.code);
6. return;
7. }
8. console.info(`camera length: ${foldStatusInfo.supportedCameras.length}`);
9. console.info(`foldStatus: ${foldStatusInfo.foldStatus}`);
10. }

12. function registerFoldStatusChange(cameraManager: camera.CameraManager): void {
13. cameraManager.on('foldStatusChange', callback);
14. }
```

## off('foldStatusChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void

关闭折叠设备折叠状态变化的监听。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'foldStatusChange'。表示折叠设备折叠状态发生变化。 |
| callback | AsyncCallback<[FoldStatusInfo](arkts-apis-camera-i.md#foldstatusinfo12)> | 否 | 回调函数，返回折叠设备折叠信息。如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterFoldStatusChange(cameraManager: camera.CameraManager): void {
2. cameraManager.off('foldStatusChange');
3. }
```

## isTorchSupported11+

PhonePC/2in1TabletTVWearable

isTorchSupported(): boolean

检测设备是否支持手电筒。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示设备是否支持手电筒，true表示设备支持手电筒，false表示设备不支持手电。  如果返回false，则[isTorchModeSupported](arkts-apis-camera-cameramanager.md#istorchmodesupported11)、[getTorchMode](arkts-apis-camera-cameramanager.md#gettorchmode11)、[setTorchMode](arkts-apis-camera-cameramanager.md#settorchmode11)都不会生效。  若接口调用失败，返回undefined。 |

**示例：**

```
1. function isTorchSupported(cameraManager: camera.CameraManager): boolean {
2. let isSupported = cameraManager.isTorchSupported();
3. return isSupported;
4. }
```

## isTorchModeSupported11+

PhonePC/2in1TabletTVWearable

isTorchModeSupported(mode: TorchMode): boolean

检测是否支持设置的手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-apis-camera-e.md#torchmode11) | 是 | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示设备支持设置的手电筒模式，返回false表示设备不支持的手电筒模式。若接口调用失败，返回undefined。 |

**示例：**

```
1. function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): boolean {
2. let isSupported = cameraManager.isTorchModeSupported(torchMode);
3. return isSupported;
4. }
```

## getTorchMode11+

PhonePC/2in1TabletTVWearable

getTorchMode(): TorchMode

获取当前设备手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TorchMode](arkts-apis-camera-e.md#torchmode11) | 返回设备当前手电筒模式。 |

**示例：**

```
1. function getTorchMode(cameraManager: camera.CameraManager): camera.TorchMode | undefined {
2. let torchMode: camera.TorchMode | undefined = undefined;
3. torchMode = cameraManager.getTorchMode();
4. return torchMode;
5. }
```

## setTorchMode11+

PhonePC/2in1TabletTVWearable

setTorchMode(mode: TorchMode): void

设置设备手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [TorchMode](arkts-apis-camera-e.md#torchmode11) | 是 | 手电筒模式。传参为null或者undefined，作为0处理，手电筒关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setTorchMode(cameraManager: camera.CameraManager, torchMode: camera.TorchMode): void {
4. try {
5. cameraManager.setTorchMode(torchMode);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setTorchMode call failed. error code: ${err.code}`);
10. }
11. }
```

## on('torchStatusChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void

手电筒状态变化回调，通过注册回调函数获取手电筒状态变化。使用callback异步回调。

说明

当前注册监听接口，不支持在on监听的回调方法里，调用off注销回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。目前只支持手电筒打开，手电筒关闭，手电筒不可用，手电筒恢复可用会触发该事件并返回对应信息。 |
| callback | AsyncCallback<[TorchStatusInfo](arkts-apis-camera-i.md#torchstatusinfo11)> | 是 | 回调函数，用于获取手电筒状态变化信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function callback(err: BusinessError, torchStatusInfo: camera.TorchStatusInfo): void {
4. if (err !== undefined && err.code !== 0) {
5. console.error(`Callback Error, errorCode: ${err.code}`);
6. return;
7. }
8. console.info(`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.isTorchActive}, level: ${torchStatusInfo.torchLevel}`);
9. }

11. function registerTorchStatusChange(cameraManager: camera.CameraManager): void {
12. cameraManager.on('torchStatusChange', callback);
13. }
```

## off('torchStatusChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void

手电筒状态变化注销回调，通过注销回调函数取消获取手电筒状态变化。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'torchStatusChange'。cameraManager对象获取成功后可监听。 |
| callback | AsyncCallback<[TorchStatusInfo](arkts-apis-camera-i.md#torchstatusinfo11)> | 否 | 回调函数，如果指定参数则取消对应callback（callback对象不可是匿名函数），否则取消所有callback。 |

**示例：**

```
1. function unregisterTorchStatusChange(cameraManager: camera.CameraManager): void {
2. cameraManager.off('torchStatusChange');
3. }
```

## getCameraDevice18+

PhonePC/2in1TabletTVWearable

getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice

根据相机位置和相机类型查询对应相机。

获取指定[CameraPosition](arkts-apis-camera-e.md#cameraposition)和[CameraType](arkts-apis-camera-e.md#cameratype)的相机镜头，如果该接口返回结果为undefined，表示当前设备未查询到该镜头。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-apis-camera-e.md#cameraposition) | 是 | 需要得到的CameraDevice对象对应的CameraPosition条件。 |
| type | [CameraType](arkts-apis-camera-e.md#cameratype) | 是 | 需要得到的CameraDevice对象对应的CameraType条件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 根据相机位置和相机类型查询的对应相机。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function getCameraDevice(cameraManager: camera.CameraManager, position: camera.CameraPosition, type: camera.CameraType): void {
5. try {
6. let curCameraDev: camera.CameraDevice | undefined = undefined;
7. curCameraDev = cameraManager.getCameraDevice(position, type);
8. } catch (error) {
9. // 失败返回错误码并处理。
10. let err = error as BusinessError;
11. console.error(`The getCameraDevice call failed. error code: ${err.code}`);
12. }
13. }
```

## getCameraDevices23+

PhonePC/2in1TabletTVWearable

getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>

根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-apis-camera-e.md#cameraposition) | 是 | 相机的位置。 |
| types | Array<[CameraType](arkts-apis-camera-e.md#cameratype)> | 是 | 相机类型数组。 |
| connectType | [ConnectionType](arkts-apis-camera-e.md#connectiontype) | 是 | 相机的连接类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[CameraDevice](arkts-apis-camera-i.md#cameradevice)> | 根据相机位置、相机类型数组和连接类型查询符合条件的相机列表。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function getCameraDevices(cameraManager: camera.CameraManager, position: camera.CameraPosition, types: Array<camera.CameraType>, connectType: camera.ConnectionType): void {
5. try {
6. let cameraDevs: Array<camera.CameraDevice> = [];
7. cameraDevs = cameraManager.getCameraDevices(position, types, connectType);
8. } catch (error) {
9. // 失败返回错误码并处理。
10. let err = error as BusinessError;
11. console.error(`The getCameraDevices call failed. error code: ${err.code}`);
12. }
13. }
```

## getCameraConcurrentInfos18+

PhonePC/2in1TabletTVWearable

getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>

获取指定相机设备的并发信息。返回空数组表示不支持并发。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cameras | Array<[CameraDevice](arkts-apis-camera-i.md#cameradevice)> | 是 | 一组CameraDevice相机设备，并得到与这一组CameraDevice对应的并发信息，推荐设置为由[getCameraDevice](arkts-apis-camera-cameramanager.md#getcameradevice18)获取的前置与后置两个用于并发的相机设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[CameraConcurrentInfo](arkts-apis-camera-i.md#cameraconcurrentinfo18)> | 一组CameraDevice相机设备对象对应的并发信息，与CameraDevice相机设备一一对应。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function getCameraConcurrentInfos(cameraManager: camera.CameraManager,
5. cameraDeviceArray: Array<camera.CameraDevice>): Array<camera.CameraConcurrentInfo> {
6. let cameraConcurrentInfos: Array<camera.CameraConcurrentInfo> = [];
7. try {
8. cameraConcurrentInfos = cameraManager.getCameraConcurrentInfos(cameraDeviceArray);
9. } catch (error) {
10. // 失败返回错误码并处理。
11. let err = error as BusinessError;
12. console.error(`The getCameraConcurrentInfos call failed. error code: ${err.code}`);
13. }
14. return cameraConcurrentInfos;
15. }
```

## getSupportedOutputCapability(deprecated)

PhonePC/2in1TabletTVWearable

getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability

查询相机设备支持的输出能力，同步返回结果。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | 相机设备，通过 [getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras) 接口获取。传参异常时，会返回错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CameraOutputCapability](arkts-apis-camera-i.md#cameraoutputcapability) | 相机输出能力。 |

**示例：**

```
1. function getSupportedOutputCapability(camera: camera.CameraDevice, cameraManager: camera.CameraManager): camera.CameraOutputCapability {
2. let cameraOutputCapability: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camera);
3. return cameraOutputCapability;
4. }
```

## createPhotoOutput(deprecated)

PhonePC/2in1TabletTVWearable

createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput

创建拍照输出对象，同步返回结果。

说明

* 从API version 10开始支持，从API version 11开始废弃。建议使用[createPhotoOutput](arkts-apis-camera-cameramanager.md#createphotooutput11)替代。
* 该接口只支持创建JPEG格式的拍照输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [Profile](arkts-apis-camera-i.md#profile) | 是 | 支持的拍照配置信息，通过[getSupportedOutputCapability](arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取。 |
| surfaceId | string | 是 | 从[ImageReceiver](arkts-apis-image-imagereceiver.md)获取的surfaceId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PhotoOutput](arkts-apis-camera-photooutput.md) | PhotoOutput实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createPhotoOutput(cameraOutputCapability: camera.CameraOutputCapability, cameraManager: camera.CameraManager, surfaceId: string): camera.PhotoOutput | undefined {
4. let profile: camera.Profile = cameraOutputCapability.photoProfiles[0];
5. let photoOutput: camera.PhotoOutput | undefined = undefined;
6. try {
7. photoOutput = cameraManager.createPhotoOutput(profile, surfaceId);
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The createPhotoOutput call failed. error code: ${err.code}`);
12. }
13. return photoOutput;
14. }
```

## createCaptureSession(deprecated)

PhonePC/2in1TabletTVWearable

createCaptureSession(): CaptureSession

创建CaptureSession实例，同步返回结果。

说明

从 API version 10开始支持，从API version 11开始废弃。建议使用[createSession](arkts-apis-camera-cameramanager.md#createsession11)替代。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CaptureSession](arkts-apis-camera-capturesession.md) | CaptureSession实例。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function createCaptureSession(cameraManager: camera.CameraManager): camera.CaptureSession | undefined {
4. let captureSession: camera.CaptureSession | undefined = undefined;
5. try {
6. captureSession = cameraManager.createCaptureSession();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`createCaptureSession error. error code: ${err.code}`);
11. }
12. return captureSession;
13. }
```
