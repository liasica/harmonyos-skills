---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-error-code
title: AR Engine错误码
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > AR Engine错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:14:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b081e2b64fa1b8cf6823872e8ac96f5005d4b28f34944f51f10cdc6b4807ae03
---

说明

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

若您的问题仍无法解决，请选择[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)提交问题，华为支持人员会及时处理。

## 1009200001 接口调用失败状态

PhoneTabletTV

**错误信息**

Failure.

**错误描述**

API接口调用失败。

**可能原因**

该错误码表示一般运行异常，如内部创建对象失败。

**处理步骤**

请重启应用，如不能解决可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200002 会话已暂停状态

**错误信息**

Session paused.

**错误描述**

会话已暂停。

**可能原因**

当前会话处于暂停状态或当前会话未重新开始。

**处理步骤**

可调用[HMS\_AREngine\_ARSession\_Resume](arengine-capi-arengine.md#hms_arengine_arsession_resume)重新开始会话。

## 1009200003 会话未暂停状态

**错误信息**

Session not paused.

**错误描述**

会话未暂停。

**可能原因**

当前会话处于运行状态。

**处理步骤**

可调用[HMS\_AREngine\_ARSession\_Pause](arengine-capi-arengine.md#hms_arengine_arsession_pause)暂停当前会话。

## 1009200004 未跟踪状态

**错误信息**

Not tracking.

**错误描述**

获取跟踪的锚点或平面信息时，会话未处于跟踪状态。

**可能原因**

当前会话异常。

**处理步骤**

查询当前会话对象（[AREngine\_ARSession](arengine-capi-arengine.md#arengine_arsession)类型对象）是否为空。

## 1009200005 未设置纹理状态

**错误信息**

Texture not set.

**错误描述**

未设置GL纹理。

**可能原因**

未设置渲染使用的GL纹理。

**处理步骤**

查看是否使用[HMS\_AREngine\_ARSession\_SetCameraGLTexture()](arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture)接口设置正确的GL纹理。

## 1009200006 缺少GL上下文状态

**错误信息**

GL context missing.

**错误描述**

缺少OpenGL上下文。

**可能原因**

当前线程缺少OpenGL上下文，调用[eglGetCurrentContext()](https://registry.khronos.org/EGL/sdk/docs/man/html/eglGetCurrentContext.xhtml)接口获取的结果为EGL\_NO\_CONTEXT。

**处理步骤**

检查[HMS\_AREngine\_ARSession\_Update()](arengine-capi-arengine.md#hms_arengine_arsession_update)接口是否在OpenGL渲染线程下调用。

## 1009200007 不支持的配置状态

PhoneTabletTV

**错误信息**

Configuration not supported.

**错误描述**

AR Engine不支持当前配置。

**可能原因**

预览尺寸不支持。

**处理步骤**

查看预览尺寸是否支持，可调用[OH\_CameraManager\_GetSupportedCameraOutputCapability](capi-camera-manager-h.md#oh_cameramanager_getsupportedcameraoutputcapability)查看。

## 1009200008 资源耗尽状态

PhoneTabletTV

**错误信息**

Resource exhausted.

**错误描述**

内存耗尽。

**可能原因**

内存不足，分配内存失败。

**处理步骤**

检查内存是否充足，如内存不足，可提示用户清理内存；如内存充足场景，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200009 服务不可用状态

PhoneTabletTV

**错误信息**

Service unavailable.

**错误描述**

服务不可用状态。

**可能原因**

设备不支持。

**处理步骤**

查看当前设备是否在[硬件要求](../harmonyos-guides/arengine-preparations.md#硬件要求)中，如设备满足要求，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200010 相机不可用

PhoneTabletTV

**错误信息**

Camera unavailable.

**错误描述**

相机不可用状态。

**可能原因**

应用其他场景占用了相机导致AR Engine无法打开相机。

**处理步骤**

排查应用在使用AR Engine时，是否存在其他打开相机场景，如不存在，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200011 添加的图片数量超过最大数量

PhoneTabletTV

**错误信息**

The number of images added exceeds the maximum.

**错误描述**

添加的图片数量超过最大数量。

**可能原因**

将图像到跟踪图像数据库超出了最大数量限制。

**处理步骤**

排查应用在添加图像到跟踪图像数据库是否超过最大数量限制。

1. 如果使用ArkTS开发，最大数量限制可以通过[ARAugmentedImageDatabase.getCapacity](arengine-api-arengine.md#araugmentedimagedatabasegetcapacity)获取，数据库中已经存储的图像数量可通过[ARAugmentedImageDatabase.getImageCount](arengine-api-arengine.md#araugmentedimagedatabasegetimagecount)获取。
2. 如果使用C/C++开发，最大数量限制可以通过[HMS\_AREngine\_ARAugmentedImageDatabase\_GetCapacity](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getcapacity)获取，数据库中已经存储的图像数量可通过[HMS\_AREngine\_ARAugmentedImageDatabase\_GetImageCount](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_getimagecount)获取。

如符合要求，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200012 将质量不足的图像添加到图像数据库中

PhoneTabletTV

**错误信息**

Attempted to add an image with insufficient quality to the image database.

**错误描述**

将质量不足的图像添加到图像数据库中。

**可能原因**

尝试将质量不足的图像添加到图像数据库中。

**处理步骤**

排查应用是否将质量不足的图像添加到图像数据库中，可以参考[ARAddAugmentedImageReason](arengine-api-arengine.md#araddaugmentedimagereason)，如符合要求，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200013 没有有效的图像数据库

**错误信息**

No valid image database.

**错误描述**

没有有效的图像数据库。

**可能原因**

图像数据库未创建。

**处理步骤**

排查是否使用[HMS\_AREngine\_ARAugmentedImageDatabase\_Create](arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create)创建图像数据库。

如符合要求，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。

## 1009200014 跟踪状态正在运行时无法添加图片

**错误信息**

The pictures cannot be added when the tracking state is running.

**错误描述**

跟踪状态正在运行时无法添加图片。

**可能原因**

程序当前正处于跟踪状态。

**处理步骤**

检查[AREngine\_ARTrackingState](arengine-capi-arengine.md#arengine_artrackingstate)状态，置为ARENGINE\_TRACKING\_STATE\_PAUSED或者ARENGINE\_TRACKING\_STATE\_STOPPED。

## 1009200015 创建nativeBuffer失败

**错误信息**

Failed to create nativeBuffer.

**错误描述**

创建nativeBuffer失败。

**可能原因**

堆内存完全耗尽。

**处理步骤**

检查设备内存状态，确保有可用堆内存，如有空闲内存仍然报错，可重启设备。

## 1009200016 无法写入nativeBuffer

**错误信息**

Failed to write nativeBuffer.

**错误描述**

无法写入nativeBuffer。

**可能原因**

堆内存完全耗尽。

**处理步骤**

检查设备内存状态，确保有可用堆内存，如有空闲内存仍然报错，可重启设备。

## 1009200017 相机服务异常

**错误信息**

The camera service is abnormal.

**错误描述**

相机服务异常。

**可能原因**

相机服务异常，比如相机服务重启、跨进程调用异常等。

**处理步骤**

相机内部错误，出现的情况不明确，建议尝试重新创建业务。

## 1009200201 非法操作状态

PhoneTabletTV

**错误信息**

ARView invalid operation.

**错误描述**

ARView操作不规范。

**可能原因**

ARViewContext已初始化后重复进行config/callBack等相关设置。

**处理步骤**

请参考[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)示例代码，是否按照示例代码使用。

## 1009200202 缺少AR呈现场景

PhoneTabletTV

**错误信息**

Graphics3D AR scene required.

**错误描述**

缺少AR呈现场景。

**可能原因**

ARViewContext初始化时未提前设置AR呈现场景 - [ARViewContext.scene](arengine-api-arviewcontroller.md#arviewcontextscene)。

**处理步骤**

在[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)初始化之前先进行AR呈现场景设置，可以参考[管理AR会话](../harmonyos-guides/arengine-arsession.md)。

## 1009200203 ARViewContext.config未配置

PhoneTabletTV

**错误信息**

AREngine config required.

**错误描述**

ARViewContext.config未配置。

**可能原因**

ARViewContext初始化时未提前设置config - ARViewContext.config。

**处理步骤**

在[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)初始化之前先进行config配置，可以参考[管理AR会话](../harmonyos-guides/arengine-arsession.md)。

## 1009200204 AR会话初始化失败

PhoneTabletTV

**错误信息**

AR session setup failed.

**错误描述**

AR会话初始化失败。

**可能原因**

因未正确配置config等导致AR session初始化失败。

**处理步骤**

排查相关接口调用返回错误码信息，根据提示进行重新设置。

## 1009200205 AR场景相机节点创建失败

PhoneTabletTV

**错误信息**

AR scene camera setup failed.

**错误描述**

AR场景相机节点创建失败。

**可能原因**

因资源耗尽、重复创建相机等导致相机节点创建失败。

**处理步骤**

排查应用在使用ARView时，是否已调用[ARViewContext](arengine-api-arviewcontroller.md#arviewcontext)接口进行了初始化，并做了相关相机确认或者系统有充足内存，如不存在，可[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)，华为支持人员会及时处理。
