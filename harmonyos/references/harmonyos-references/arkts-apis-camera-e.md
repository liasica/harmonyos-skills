---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e
title: Enums
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Enums
category: harmonyos-references
scraped_at: 2026-09-02T15:02:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1f7cb8a9b6b6fdf29e42c13b075bd86bd32f3603a24c1ec9232d9b8dcffefacd
---

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## CameraPosition

枚举，相机位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_POSITION\_UNSPECIFIED | 0 | 相对于设备屏幕没有固定的朝向的相机。 |
| CAMERA\_POSITION\_BACK | 1 | 后置相机。 |
| CAMERA\_POSITION\_FRONT | 2 | 前置相机。 |
| CAMERA\_POSITION\_FOLD\_INNER(deprecated) | 3 | 折叠态相机。  从API version 11开始支持，从API version 12开始废弃。 |

## CameraType

枚举，相机类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_TYPE\_DEFAULT | 0 | 默认相机类型。 |
| CAMERA\_TYPE\_WIDE\_ANGLE | 1 | 广角相机。 |
| CAMERA\_TYPE\_ULTRA\_WIDE | 2 | 超广角相机。 |
| CAMERA\_TYPE\_TELEPHOTO | 3 | 长焦相机。 |
| CAMERA\_TYPE\_TRUE\_DEPTH | 4 | 带景深信息的相机。 |

## ConnectionType

枚举，相机连接类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_CONNECTION\_BUILT\_IN | 0 | 内置相机。 |
| CAMERA\_CONNECTION\_USB\_PLUGIN | 1 | USB连接的相机。 |
| CAMERA\_CONNECTION\_REMOTE | 2 | 远程连接的相机。 |

## HostDeviceType15+

枚举，远端相机设备类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 未知设备类型。 |
| PHONE | 0x0E | 手机设备。 |
| TABLET | 0x11 | 平板设备。 |

## CameraStatus

枚举，相机状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_STATUS\_APPEAR | 0 | 新的相机出现。 |
| CAMERA\_STATUS\_DISAPPEAR | 1 | 相机被移除。 |
| CAMERA\_STATUS\_AVAILABLE | 2 | 相机可用。 |
| CAMERA\_STATUS\_UNAVAILABLE | 3 | 相机不可用。 |

## FoldStatus12+

枚举，折叠机折叠状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NON\_FOLDABLE | 0 | 表示当前设备不可折叠。 |
| EXPANDED | 1 | 表示当前设备折叠状态为完全展开。 |
| FOLDED | 2 | 表示当前设备折叠状态为折叠。 |

## SceneMode11+

枚举，相机模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL\_PHOTO | 1 | 普通拍照模式。详情见[PhotoSession](arkts-apis-camera-photosession.md)。 |
| NORMAL\_VIDEO | 2 | 普通录像模式。详情见[VideoSession](arkts-apis-camera-videosession.md)。 |
| SECURE\_PHOTO12+ | 12 | 安全相机模式。详情见[SecureSession](arkts-apis-camera-securesession.md)。 |

## CameraErrorCode

相机错误码。

接口使用不正确以及on接口监听error状态返回。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID\_ARGUMENT | 7400101 | 参数缺失或者参数类型不对。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| OPERATION\_NOT\_ALLOWED | 7400102 | 操作流程不对，不允许。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| SESSION\_NOT\_CONFIG | 7400103 | session 未配置返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| SESSION\_NOT\_RUNNING | 7400104 | session 未运行返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| SESSION\_CONFIG\_LOCKED | 7400105 | session 配置已锁定返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| DEVICE\_SETTING\_LOCKED | 7400106 | 设备设置已锁定返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CONFLICT\_CAMERA | 7400107 | 设备重复打开返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| DEVICE\_DISABLED | 7400108 | 安全原因相机被禁用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| DEVICE\_PREEMPTED | 7400109 | 相机被抢占导致无法使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| UNRESOLVED\_CONFLICTS\_WITH\_CURRENT\_CONFIGURATIONS12+ | 7400110 | 与当前配置存在冲突。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| SERVICE\_FATAL\_ERROR | 7400201 | 相机服务异常返回。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## TorchMode11+

枚举，手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 常关模式。 |
| ON | 1 | 常开模式。 |
| AUTO | 2 | 自动模式，系统根据环境自动调节手电筒亮度。 |

## CameraFormat

枚举，输出格式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_FORMAT\_RGBA\_8888 | 3 | RGBA\_8888格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_YUV\_420\_SP | 1003 | YUV\_420\_SP格式的图片，对应为NV21格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_JPEG | 2000 | JPEG格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_YCBCR\_P01011+ | 2001 | YCBCR\_P010格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_YCRCB\_P01011+ | 2002 | YCRCB\_P010格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_HEIC13+ | 2003 | HEIF格式的图片。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_DNG24+ | 4 | DNG（数字负片）格式的图片。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| CAMERA\_FORMAT\_DNG\_XDRAW | 5 | 增强型DNG格式的图片。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## VideoCodecType13+

枚举，视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AVC | 0 | 视频编码类型AVC。 |
| HEVC | 1 | 视频编码类型HEVC。 |

## CameraConcurrentType18+

枚举，镜头并发类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_LIMITED\_CAPABILITY | 0 | 镜头受限能力并发。 |
| CAMERA\_FULL\_CAPABILITY | 1 | 镜头全量能力并发。 |

## ImageRotation

枚举，图片旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ROTATION\_0 | 0 | 图片旋转0度。 |
| ROTATION\_90 | 90 | 图片旋转90度。 |
| ROTATION\_180 | 180 | 图片旋转180度。 |
| ROTATION\_270 | 270 | 图片旋转270度。 |

## QualityLevel

枚举，图片质量。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QUALITY\_LEVEL\_HIGH | 0 | 图片质量高。 |
| QUALITY\_LEVEL\_MEDIUM | 1 | 图片质量中等。 |
| QUALITY\_LEVEL\_LOW | 2 | 图片质量差。 |

## MetadataObjectType

枚举，metadata元数据检测类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FACE\_DETECTION | 0 | 元数据的对象类型，用于人脸检测。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| HUMAN\_BODY23+ | 1 | 元数据的对象类型，用于人体检测。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| CAT\_FACE | 2 | 用于检测猫脸的metadata类型。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| CAT\_BODY | 3 | 用于检测猫的身体的metadata类型。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| DOG\_FACE | 4 | 用于检测狗脸的metadata类型。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| DOG\_BODY | 5 | 用于检测狗的身体的metadata类型。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| SALIENT\_DETECTION | 6 | 用于显著性检测。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| BAR\_CODE\_DETECTION | 7 | 用于二维码检测。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |
| BASIC\_FACE\_DETECTION | 8 | 用于基础人脸检测。  **起始版本：** 26.0.0  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## Emotion

枚举，人脸检测信息中的情绪类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEUTRAL | 0 | 平静。 |
| SADNESS | 1 | 悲伤。 |
| SMILE | 2 | 微笑。 |
| SURPRISE | 3 | 惊讶。 |

## FlashMode

枚举，闪光灯模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLASH\_MODE\_CLOSE | 0 | 闪光灯关闭。 |
| FLASH\_MODE\_OPEN | 1 | 闪光灯打开。 |
| FLASH\_MODE\_AUTO | 2 | 自动闪光灯。 |
| FLASH\_MODE\_ALWAYS\_OPEN | 3 | 闪光灯常亮。 |

## ExposureMode

枚举，曝光模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXPOSURE\_MODE\_UNSPECIFIED24+ | -1 | 曝光模式未指定。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| EXPOSURE\_MODE\_LOCKED | 0 | 锁定曝光模式。不支持曝光区域中心点设置。  设置该模式后，每次拍照时曝光都会默认锁定。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| EXPOSURE\_MODE\_AUTO | 1 | 自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](arkts-apis-camera-autoexposure.md#setmeteringpoint11)接口设置曝光区域中心点。  设置该模式后，仅设置后的首次拍照生效。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| EXPOSURE\_MODE\_CONTINUOUS\_AUTO | 2 | 连续自动曝光。不支持曝光区域中心点设置。  设置该模式后，拍照系统会根据每次的环境变化自动调整曝光。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| EXPOSURE\_MODE\_MANUAL24+ | 3 | 手动曝光。支持设置曝光时长。  设置该模式后，用户可通过[ManualExposure.setExposureDuration](arkts-apis-camera-manualexposure.md#setexposureduration24)设置曝光时长。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |

## FocusMode

枚举，焦距模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOCUS\_MODE\_MANUAL | 0 | 手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。 |
| FOCUS\_MODE\_CONTINUOUS\_AUTO | 1 | 连续自动对焦。不支持对焦点设置。 |
| FOCUS\_MODE\_AUTO | 2 | 自动对焦。支持对焦点设置，可以使用[Focus.setFocusPoint](arkts-apis-camera-focus.md#setfocuspoint11)设置对焦点，根据对焦点执行一次自动对焦。 |
| FOCUS\_MODE\_LOCKED | 3 | 对焦锁定。不支持对焦点设置。 |

## FocusState

枚举，焦距状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOCUS\_STATE\_SCAN | 0 | 触发对焦。 |
| FOCUS\_STATE\_FOCUSED | 1 | 对焦成功。 |
| FOCUS\_STATE\_UNFOCUSED | 2 | 未完成对焦。 |

## VideoStabilizationMode

枚举，视频防抖模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 关闭视频防抖功能。 |
| LOW | 1 | 使用基础防抖算法。 |
| MIDDLE | 2 | 使用防抖效果一般的防抖算法，防抖效果优于LOW类型。 |
| HIGH | 3 | 使用防抖效果最好的防抖算法，防抖效果优于MIDDLE类型。 |
| AUTO | 4 | 自动进行选择防抖算法。 |

## SmoothZoomMode11+

平滑变焦模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 贝塞尔曲线模式。 |

## PreconfigType12+

枚举，提供预配置的类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRECONFIG\_720P | 0 | 720P预配置。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| PRECONFIG\_1080P | 1 | 1080P预配置。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| PRECONFIG\_4K | 2 | 4K预配置。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| PRECONFIG\_HIGH\_QUALITY | 3 | 高质量预配置。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| PRECONFIG\_HIGH\_QUALITY\_PHOTOSESSION\_BT202023+ | 4 | 预配置支持预览高动态范围显示和HDR动图拍摄。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## PreconfigRatio12+

枚举，提供预配置的分辨率比例。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRECONFIG\_RATIO\_1\_1 | 0 | 1:1画幅。 |
| PRECONFIG\_RATIO\_4\_3 | 1 | 4:3画幅。 |
| PRECONFIG\_RATIO\_16\_9 | 2 | 16:9画幅。 |

## QualityPrioritization14+

枚举，录像质量优先级。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH\_QUALITY | 0 | 高录像质量。 |
| POWER\_BALANCE | 1 | 功耗平衡的录像质量。 |

## WhiteBalanceMode20+

枚举，白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 自动 |
| CLOUDY | 1 | 阴天 |
| INCANDESCENT | 2 | 白炽光 |
| FLUORESCENT | 3 | 荧光 |
| DAYLIGHT | 4 | 日光 |
| MANUAL | 5 | 手动 |
| LOCKED | 6 | 锁定 |

## SystemPressureLevel20+

枚举，系统压力等级。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM\_PRESSURE\_NORMAL | 0 | 系统压力正常。 |
| SYSTEM\_PRESSURE\_MILD | 1 | 系统压力升高，但是系统不会主动管控。 |
| SYSTEM\_PRESSURE\_SEVERE | 2 | 系统压力可能对图像总质量、性能产生影响。 |
| SYSTEM\_PRESSURE\_CRITICAL | 3 | 系统压力对图像质量、性能产生显著影响。 |
| SYSTEM\_PRESSURE\_SHUTDOWN | 4 | 系统压力过高，停止工作。 |

## ControlCenterEffectType20+

枚举，相机控制器支持的效果类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEAUTY | 0 | 美颜。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| PORTRAIT | 1 | 人像虚化。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| AUTO\_FRAMING24+ | 2 | 自动对焦。  **元服务API：** 从API version 24开始，该接口支持在元服务中使用。 |
| COLOR\_EFFECT | 3 | 色彩效果。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## PhotoQualityPrioritization21+

枚举，拍照画质优先策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH\_QUALITY | 0 | 画质优先，拍照需要较长的时间，以输出高画质的图片。 |
| SPEED | 1 | 性能优先，会降低画质来提升拍照的速度。 |

## SensorColorFilterArrangement24+

枚举，传感器颜色滤镜排列方式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BGGR | 0 | 蓝绿绿红（Blue-Green-Green-Red）滤镜排列方式。 |
| GBRG | 1 | 绿蓝红绿（Green-Blue-Red-Green）滤镜排列方式。 |
| GRBG | 2 | 绿红蓝绿（Green-Red-Blue-Green）滤镜排列方式。 |
| RGGB | 3 | 红绿绿蓝（Red-Green-Green-Blue）滤镜排列方式。 |

## FlashState24+

枚举，闪光灯状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLASH\_STATE\_UNAVAILABLE | 0 | 闪光灯为不可用状态，为默认值。 |
| FLASH\_STATE\_READY | 1 | 闪光灯为可用状态。 |
| FLASH\_STATE\_FLASHING | 2 | 闪光灯已经被打开。 |

## ExposureMeteringMode24+

枚举，曝光测光模式。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATRIX | 0 | 矩阵测光模式。对画面广泛区域进行测光，适合拍摄自然风光。 |
| CENTER | 1 | 中心测光模式。对整个画面进行测光，但最大比重分配给中央区域，适合拍摄人像。 |
| SPOT | 2 | 点测光模式。对画面测光点周围约2.5%进行测光，专注于特定微小区域的光线，如被摄主体的眼睛。 |

## OISMode24+

枚举，光学防抖（Optical Image Stabilization）模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 光学防抖关闭。 |
| AUTO | 1 | 光学防抖自动控制。 |
| CUSTOM | 2 | 光学防抖由应用控制。 |

## OISAxes24+

枚举，光学防抖（OIS）轴向。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PITCH | 0 | 俯仰轴。控制相机机身上下旋转，即机身围绕与镜头水平方向的轴旋转。 |
| YAW | 1 | 偏航轴。控制相机机身左右旋转，即机身围绕与镜头垂直方向的轴旋转。 |

## ExposureState

枚举，曝光状态。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXPOSURE\_STATE\_SCAN | 0 | 曝光处于扫描状态。 |
| EXPOSURE\_STATE\_CONVERGED | 1 | 曝光已经收敛。 |

## AutomotiveCameraPosition

表示Car设备摄像头位置的枚举。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_OTHER | 0 | Car设备外部其他位置摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_FRONT | 1 | Car设备外部前侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_REAR | 2 | Car设备外部后侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_LEFT | 3 | Car设备外部左侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_RIGHT | 4 | Car设备外部右侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_OTHER | 5 | Car设备内部其他位置摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_LEFT | 6 | Car设备内部第一排左侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_CENTER | 7 | Car设备内部第一排中央摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_RIGHT | 8 | Car设备内部第一排右侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_LEFT | 9 | Car设备内部第二排左侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_CENTER | 10 | Car设备内部第二排中央摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_RIGHT | 11 | Car设备内部第二排右侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_LEFT | 12 | Car设备内部第三排左侧摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_CENTER | 13 | Car设备内部第三排中央摄像头。 |
| AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_RIGHT | 14 | Car设备内部第三排右侧摄像头。 |
