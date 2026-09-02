---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-i
title: Interfaces (其他)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75d3597b5cb7a7ab8c660fc28fc639e3e37f29993f2ade02e618f7a68dae21f5
---

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## CameraDevice

相机设备信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cameraId | string | 是 | 否 | 相机ID。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| cameraPosition | [CameraPosition](arkts-apis-camera-e.md#cameraposition) | 是 | 否 | 相机位置。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| cameraType | [CameraType](arkts-apis-camera-e.md#cameratype) | 是 | 否 | 相机类型。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| connectionType | [ConnectionType](arkts-apis-camera-e.md#connectiontype) | 是 | 否 | 相机连接类型。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| cameraOrientation12+ | number | 是 | 否 | 相机安装角度，不会随着屏幕旋转而改变。取值范围为[0, 360]。单位：度。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| hostDeviceName15+ | string | 是 | 否 | 远端设备名称。若当前无远端设备，返回为空。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| hostDeviceType15+ | [HostDeviceType](arkts-apis-camera-e.md#hostdevicetype15) | 是 | 否 | 远端设备类型。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| lensEquivalentFocalLength24+ | Array<number> | 是 | 是 | 相机镜头等效焦距。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| isLogicalCamera24+ | boolean | 是 | 是 | 是否为逻辑摄像头（由多个物理相机组成）, true表示是逻辑摄像头，false表示是物理摄像头。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| constituentCameraDevices24+ | Array<[CameraDevice](arkts-apis-camera-i.md#cameradevice)> | 是 | 是 | 组成此逻辑相机的物理相机列表。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| lensFocalLength24+ | number | 是 | 是 | 镜头实际焦距。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| minimumFocusDistance24+ | number | 是 | 是 | 相机最小对焦距离。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| lensDistortion24+ | Array<number> | 是 | 是 | 镜头畸变参数数组。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| lensIntrinsicCalibration24+ | Array<number> | 是 | 是 | 镜头内参标定参数数组。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| sensorPhysicalSize24+ | Array<number> | 是 | 是 | 传感器物理尺寸（宽度和高度）。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| sensorPixelArraySize24+ | Array<number> | 是 | 是 | 传感器像素阵列尺寸（宽度和高度。单位：像素）。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| sensorColorFilterArrangement24+ | [SensorColorFilterArrangement](arkts-apis-camera-e.md#sensorcolorfilterarrangement24) | 是 | 是 | 传感器颜色滤镜排列方式。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| automotiveCameraPosition | [AutomotiveCameraPosition](arkts-apis-camera-e.md#automotivecameraposition) | 是 | 是 | Car设备摄像头位置。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## CameraStatusInfo

相机管理器回调返回的接口实例，该实例表示相机状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| camera | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 否 | 否 | 相机信息。 |
| status | [CameraStatus](arkts-apis-camera-e.md#camerastatus) | 否 | 否 | 相机状态。 |

## FoldStatusInfo12+

相机管理器回调返回的接口实例，表示折叠机折叠状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| supportedCameras | [Array<CameraDevice>](arkts-apis-camera-i.md#cameradevice) | 是 | 否 | 当前折叠状态所支持的相机信息列表。 |
| foldStatus | [FoldStatus](arkts-apis-camera-e.md#foldstatus12) | 是 | 否 | 折叠屏折叠状态。 |

## Profile

相机配置信息项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | [CameraFormat](arkts-apis-camera-e.md#cameraformat) | 是 | 否 | 输出格式。 |
| size | [Size](arkts-apis-camera-i.md#size) | 是 | 否 | 分辨率。  设置的是相机的分辨率宽度和高度，而非实际输出图像的宽度和高度。 |

## FrameRateRange

帧率范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| min | number | 是 | 否 | 最小帧率。单位：fps。 |
| max | number | 是 | 否 | 最大帧率。单位：fps。 |

## VideoProfile

视频配置信息项，继承[Profile](arkts-apis-camera-i.md#profile)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| frameRateRange | [FrameRateRange](arkts-apis-camera-i.md#frameraterange) | 是 | 否 | 帧率范围。单位：fps(frames per second)。 |

## CameraOutputCapability

相机输出能力项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| previewProfiles | Array<[Profile](arkts-apis-camera-i.md#profile)> | 是 | 否 | 支持的预览配置信息集合。 |
| photoProfiles | Array<[Profile](arkts-apis-camera-i.md#profile)> | 是 | 否 | 支持的拍照配置信息集合。 |
| videoProfiles | Array<[VideoProfile](arkts-apis-camera-i.md#videoprofile)> | 是 | 否 | 支持的录像配置信息集合。 |
| supportedMetadataObjectTypes | Array<[MetadataObjectType](arkts-apis-camera-e.md#metadataobjecttype)> | 是 | 否 | 支持的metadata流类型信息集合。 |

## TorchStatusInfo11+

手电筒回调返回的接口实例，表示手电筒状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isTorchAvailable | boolean | 是 | 否 | 手电筒是否可用。true表示手电筒可用，false表示手电筒不可用。 |
| isTorchActive | boolean | 是 | 否 | 手电筒是否被激活。true表示手电筒被激活，false表示手电筒未被激活。 |
| torchLevel | number | 是 | 否 | 手电筒亮度等级，取值范围为[0,1]，越靠近1，亮度越大。 |

## Size

尺寸参数。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| height | number | 否 | 否 | 图像尺寸高（像素）。 |
| width | number | 否 | 否 | 图像尺寸宽（像素）。 |

## Point

点坐标用于对焦和曝光配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 点的x坐标。 |
| y | number | 否 | 否 | 点的y坐标。 |

## CameraConcurrentInfo18+

相机的输出并发能力信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| device | [CameraDevice](arkts-apis-camera-i.md#cameradevice) | 是 | 否 | 相机并发设备。 |
| type | [CameraConcurrentType](arkts-apis-camera-e.md#cameraconcurrenttype18) | 是 | 否 | 镜头并发类型。 |
| modes | Array<[SceneMode](arkts-apis-camera-e.md#scenemode11) > | 是 | 否 | 相机支持的模式。 |
| outputCapabilities | Array<[CameraOutputCapability](arkts-apis-camera-i.md#cameraoutputcapability) > | 是 | 否 | 相机对应模式的输出能力集。 |

## Location

图片地理位置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度（度）。取值范围：[-90, 90]。 |
| longitude | number | 否 | 否 | 经度（度）。取值范围：[-180, 180]。 |
| altitude | number | 否 | 否 | 海拔（米）。 |

## PhotoCaptureSetting

拍摄照片的设置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| quality | [QualityLevel](arkts-apis-camera-e.md#qualitylevel) | 否 | 是 | 图片质量。  当quality未下发时，默认按compressionQuality下发生效；若quality与compressionQuality同时下发则按compressionQuality下发生效；若quality与compressionQuality均未下发则图片质量默认是高等。 |
| rotation | [ImageRotation](arkts-apis-camera-e.md#imagerotation) | 否 | 是 | 图片旋转角度（默认0度，顺时针旋转）。 |
| location | [Location](arkts-apis-camera-i.md#location) | 否 | 是 | 图片地理位置信息（默认以设备硬件信息为准）。 |
| mirror | boolean | 否 | 是 | 镜像使能开关（默认关）。使用之前需要使用[isMirrorSupported](arkts-apis-camera-photooutput.md#ismirrorsupported)进行判断是否支持。true表示使能，false表示不使能。 |
| compressionQuality | number | 否 | 是 | 图片压缩质量值，取值范围为(1, 100)。  当compressionQuality未下发时，默认按quality生效；若quality与compressionQuality同时下发则按compressionQuality下发生效；若quality与compressionQuality均未下发则图片质量默认是高等。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## FrameShutterInfo

拍照帧输出信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| captureId | number | 否 | 否 | 拍照的ID。 |
| timestamp | number | 否 | 否 | 快门时间戳。单位毫秒。 |

## FrameShutterEndInfo12+

拍照曝光结束信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| captureId | number | 否 | 否 | 拍照的ID。 |

## CaptureStartInfo11+

拍照开始信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| captureId | number | 否 | 否 | 拍照的ID。 |
| time | number | 否 | 否 | 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。 |

## CaptureEndInfo

拍照停止信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| captureId | number | 否 | 否 | 拍照的ID。 |
| frameCount | number | 否 | 否 | 帧数。 |

## AutoDeviceSwitchStatus13+

自动切换镜头状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isDeviceSwitched | boolean | 是 | 否 | 自动切换镜头是否成功。true表示成功，false表示失败。 |
| isDeviceCapabilityChanged | boolean | 是 | 否 | 自动切换镜头成功后，其镜头能力值是否发生改变。true表示发生变化，false表示未发生变化。 |

## Rect

相机矩形。用于各类检测对象的矩形框绘制。返回的检测点坐标系以设备充电口在右侧时的横向设备方向为基准。该坐标系左上角为（0，0），右下角为（1，1），其中（topLeftX，topLeftY）表示矩形区域的左上角坐标，width和height分别表示矩形区域的宽和高。因此在实际使用中根据业务诉求需要裁剪或者选择人脸区域时，必须将矩形区域的x坐标和y坐标分别乘以实际相机预览输出流的宽和高，即可得到裁剪后的人脸矩形区域。

实际预览流的宽高指的是相机输出流的分辨率，请参考[profile](arkts-apis-camera-i.md#profile)中的size。

预览流的数据获取请参考[双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| topLeftX | number | 否 | 否 | 矩形区域左上角x坐标，范围[0, 1]。 |
| topLeftY | number | 否 | 否 | 矩形区域左上角y坐标，范围[0, 1]。 |
| width | number | 否 | 否 | 矩形宽，范围[0, 1]。 |
| height | number | 否 | 否 | 矩形高，范围[0, 1]。 |

## MetadataObject

相机元数据信息，[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.on('metadataObjectsAvailable')接口获取。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [MetadataObjectType](arkts-apis-camera-e.md#metadataobjecttype) | 是 | 否 | metadata 类型。 |
| timestamp | number | 是 | 否 | 当前时间戳。单位为纳秒（ns）。 |
| boundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | metadata 区域框。 |
| isLockFocusTracked | boolean | 是 | 是 | 是否已锁定焦点跟踪。true表示已锁定，false表示未锁定。**起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## MetadataBasicFaceObject

相机检测到的基础人脸元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| leftEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 是 | 左眼区域框。 |
| rightEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 是 | 右眼区域框。 |
| pitchAngle | number | 是 | 是 | 俯仰角度。取值范围为[-90, 90]，以向下为正方向。 |
| yawAngle | number | 是 | 是 | 左右旋转角度。取值范围为[-90, 90]，以向右为正方向。 |
| rollAngle | number | 是 | 是 | 平面内旋转角度。取值范围为[-180, 180]，以顺时针方向为正方向。 |

## MetadataFaceObject

相机检测到的人脸元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| leftEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 左眼区域框。 |
| rightEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 右眼区域框。 |
| emotion | [Emotion](arkts-apis-camera-e.md#emotion) | 是 | 否 | 检测到的情绪类型。 |
| emotionConfidence | number | 是 | 否 | 情绪检测置信度。取值范围为[0, 1]。 |
| pitchAngle | number | 是 | 否 | 俯仰角度。取值范围为[-90, 90]，以向下为正方向。 |
| yawAngle | number | 是 | 否 | 左右旋转角度。取值范围为[-90, 90]，以向右为正方向。 |
| rollAngle | number | 是 | 否 | 平面内旋转角度。取值范围为[-180, 180]，以顺时针方向为正方向。 |

## MetadataHumanBodyObject

相机检测到的人体元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## MetadataCatFaceObject

相机检测到的猫脸元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| leftEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 左眼区域框。 |
| rightEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 右眼区域框。 |

## MetadataCatBodyObject

相机检测到的猫的身体元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## MetadataDogFaceObject

相机检测到的狗脸元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| leftEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 左眼区域框。 |
| rightEyeBoundingBox | [Rect](arkts-apis-camera-i.md#rect) | 是 | 否 | 右眼区域框。 |

## MetadataDogBodyObject

相机检测到的狗的身体元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## MetadataSalientDetectionObject

相机检测到的显著性物体元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## MetadataBarcodeObject

相机检测到的二维码元数据信息，继承自[MetadataObject](arkts-apis-camera-i.md#metadataobject)。[CameraInput](arkts-apis-camera-camerainput.md)相机信息中的数据来源，通过metadataOutput.[on('metadataObjectsAvailable')](arkts-apis-camera-metadataoutput.md#onmetadataobjectsavailable)接口获取。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

## SmoothZoomInfo11+

平滑变焦参数信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 否 | 平滑变焦总时长。单位ms。 |

## ControlCenterStatusInfo20+

相机控制器效果激活状态信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| effectType | [ControlCenterEffectType](arkts-apis-camera-e.md#controlcentereffecttype20) | 是 | 否 | 相机控制器效果类型。 |
| isActive | boolean | 是 | 否 | 相机控制器效果激活状态。true表示已激活，false表示未激活。 |

## IsoInfo22+

感光度（ISO）参数信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iso | number | 是 | 是 | ISO值。 |

## CameraOcclusionDetectionResult23+

镜头遮挡或脏污检测回调返回的接口实例，表示镜头遮挡或脏污状态信息。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isCameraOccluded | boolean | 是 | 否 | 镜头是否被遮挡。true表示镜头被遮挡，false表示镜头无遮挡。 |
| isCameraLensDirty | boolean | 是 | 否 | 镜头是否有脏污。true表示镜头有脏污，false表示镜头无脏污。 |

## ZoomRange24+

变焦范围。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| min | number | 是 | 否 | 最小变焦值。 |
| max | number | 是 | 否 | 最大变焦值。 |

## PhysicalAperture24+

物理光圈对象。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| zoomRange | [ZoomRange](arkts-apis-camera-i.md#zoomrange24) | 否 | 否 | 特定物理光圈的变焦范围。 |
| apertures | Array<number> | 否 | 否 | 支持的物理光圈值。 |

## ExposureInfo24+

曝光信息对象。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exposureTime | number | 是 | 是 | 曝光时间值。单位：微秒。 |

## ZoomPointInfo

等效焦距信息。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| zoomRatio | number | 是 | 否 | 可变焦距比。 |
| equivalentFocalLength | number | 是 | 否 | 当前焦距比对应的等效焦距值。 |
