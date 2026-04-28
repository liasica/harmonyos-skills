---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e
title: Enums
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:12:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea3ef76b3138dd13ebc7a28e5bd537e9d49454ac0caeb3de26f040b1f672380c
---

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## CameraPosition

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，相机连接类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_CONNECTION\_BUILT\_IN | 0 | 内置相机。 |
| CAMERA\_CONNECTION\_USB\_PLUGIN | 1 | USB连接的相机。 |
| CAMERA\_CONNECTION\_REMOTE | 2 | 远程连接的相机。 |

## HostDeviceType15+

PhonePC/2in1TabletTVWearable

枚举，远端相机设备类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_TYPE | 0 | 未知设备类型。 |
| PHONE | 0x0E | 手机设备。 |
| TABLET | 0x11 | 平板设备。 |

## CameraStatus

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，折叠机折叠状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NON\_FOLDABLE | 0 | 表示当前设备不可折叠。 |
| EXPANDED | 1 | 表示当前设备折叠状态为完全展开。 |
| FOLDED | 2 | 表示当前设备折叠状态为折叠。 |

## SceneMode11+

PhonePC/2in1TabletTVWearable

枚举，相机模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL\_PHOTO | 1 | 普通拍照模式。详情见[PhotoSession](arkts-apis-camera-photosession.md)。 |
| NORMAL\_VIDEO | 2 | 普通录像模式。详情见[VideoSession](arkts-apis-camera-videosession.md)。 |
| SECURE\_PHOTO12+ | 12 | 安全相机模式。详情见[SecureSession](arkts-apis-camera-securesession.md)。 |

## CameraErrorCode

PhonePC/2in1TabletTVWearable

相机错误码。

接口使用不正确以及on接口监听error状态返回。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID\_ARGUMENT | 7400101 | 参数缺失或者参数类型不对。 |
| OPERATION\_NOT\_ALLOWED | 7400102 | 操作流程不对，不允许。 |
| SESSION\_NOT\_CONFIG | 7400103 | session 未配置返回。 |
| SESSION\_NOT\_RUNNING | 7400104 | session 未运行返回。 |
| SESSION\_CONFIG\_LOCKED | 7400105 | session 配置已锁定返回。 |
| DEVICE\_SETTING\_LOCKED | 7400106 | 设备设置已锁定返回。 |
| CONFLICT\_CAMERA | 7400107 | 设备重复打开返回。 |
| DEVICE\_DISABLED | 7400108 | 安全原因相机被禁用。 |
| DEVICE\_PREEMPTED | 7400109 | 相机被抢占导致无法使用。 |
| UNRESOLVED\_CONFLICTS\_WITH\_CURRENT\_CONFIGURATIONS12+ | 7400110 | 与当前配置存在冲突。 |
| SERVICE\_FATAL\_ERROR | 7400201 | 相机服务异常返回。 |

## TorchMode11+

PhonePC/2in1TabletTVWearable

枚举，手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 常关模式。 |
| ON | 1 | 常开模式。 |
| AUTO | 2 | 自动模式，系统根据环境自动调节手电筒亮度。 |

## CameraFormat

PhonePC/2in1TabletTVWearable

枚举，输出格式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_FORMAT\_RGBA\_8888 | 3 | RGBA\_8888格式的图片。 |
| CAMERA\_FORMAT\_YUV\_420\_SP | 1003 | YUV\_420\_SP格式的图片，对应为NV21格式的图片。 |
| CAMERA\_FORMAT\_JPEG | 2000 | JPEG格式的图片。 |
| CAMERA\_FORMAT\_YCBCR\_P01011+ | 2001 | YCBCR\_P010格式的图片。 |
| CAMERA\_FORMAT\_YCRCB\_P01011+ | 2002 | YCRCB\_P010格式的图片。 |
| CAMERA\_FORMAT\_HEIC13+ | 2003 | HEIF格式的图片。 |

## VideoCodecType13+

PhonePC/2in1TabletTVWearable

枚举，视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AVC | 0 | 视频编码类型AVC。 |
| HEVC | 1 | 视频编码类型HEVC。 |

## CameraConcurrentType18+

PhonePC/2in1TabletTVWearable

枚举，镜头并发类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA\_LIMITED\_CAPABILITY | 0 | 镜头受限能力并发。 |
| CAMERA\_FULL\_CAPABILITY | 1 | 镜头全量能力并发。 |

## ImageRotation

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，图片质量。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| QUALITY\_LEVEL\_HIGH | 0 | 图片质量高。 |
| QUALITY\_LEVEL\_MEDIUM | 1 | 图片质量中等。 |
| QUALITY\_LEVEL\_LOW | 2 | 图片质量差。 |

## MetadataObjectType

PhonePC/2in1TabletTVWearable

枚举，metadata流。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FACE\_DETECTION | 0 | 元数据的对象类型，用于人脸检测。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| HUMAN\_BODY23+ | 1 | 元数据的对象类型，用于人体检测。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## FlashMode

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，曝光模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXPOSURE\_MODE\_LOCKED | 0 | 锁定曝光模式。不支持曝光区域中心点设置。  设置该模式后，每次拍照时曝光都会默认锁定。 |
| EXPOSURE\_MODE\_AUTO | 1 | 自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](arkts-apis-camera-autoexposure.md#setmeteringpoint11)接口设置曝光区域中心点。  设置该模式后，仅设置后的首次拍照生效。 |
| EXPOSURE\_MODE\_CONTINUOUS\_AUTO | 2 | 连续自动曝光。不支持曝光区域中心点设置。  设置该模式后，拍照系统会根据每次的环境变化自动调整曝光。 |

## FocusMode

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，焦距状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOCUS\_STATE\_SCAN | 0 | 触发对焦。 |
| FOCUS\_STATE\_FOCUSED | 1 | 对焦成功。 |
| FOCUS\_STATE\_UNFOCUSED | 2 | 未完成对焦。 |

## VideoStabilizationMode

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

平滑变焦模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 贝塞尔曲线模式。 |

## PreconfigType12+

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，提供预配置的分辨率比例。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRECONFIG\_RATIO\_1\_1 | 0 | 1:1画幅。 |
| PRECONFIG\_RATIO\_4\_3 | 1 | 4:3画幅。 |
| PRECONFIG\_RATIO\_16\_9 | 2 | 16:9画幅。 |

## QualityPrioritization14+

PhonePC/2in1TabletTVWearable

枚举，录像质量优先级。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH\_QUALITY | 0 | 高录像质量。 |
| POWER\_BALANCE | 1 | 功耗平衡的录像质量。 |

## WhiteBalanceMode20+

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

枚举，相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEAUTY | 0 | 美颜。 |
| PORTRAIT | 1 | 人像虚化。 |

## PhotoQualityPrioritization21+

PhonePC/2in1TabletTVWearable

枚举，拍照画质优先策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH\_QUALITY | 0 | 画质优先，拍照需要较长的时间，以输出高画质的图片。 |
| SPEED | 1 | 性能优先，会降低画质来提升拍照的速度。 |
