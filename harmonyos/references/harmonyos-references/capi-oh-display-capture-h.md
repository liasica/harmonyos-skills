---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-capture-h
title: oh_display_capture.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_display_capture.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:712dc6ae60e2540bf070623ae7c1e53dea29226f56c226b95a2a9cd1d0328f09
---

## 概述

提供屏幕截屏的能力。

**引用文件：** <window\_manager/oh\_display\_capture.h>

**库：** libnative\_display\_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CaptureScreenPixelmap(uint32\_t displayId, OH\_PixelmapNative \*\*pixelMap)](capi-oh-display-capture-h.md#oh_nativedisplaymanager_capturescreenpixelmap) | 获取屏幕全屏截图，可通过设置不同的屏幕ID截取指定屏幕。 |

## 函数说明

### OH\_NativeDisplayManager\_CaptureScreenPixelmap()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CaptureScreenPixelmap(uint32_t displayId, OH_PixelmapNative **pixelMap)
```

**描述**

获取屏幕全屏截图，可通过设置不同的屏幕ID截取指定屏幕。

**需要权限：**

* API版本22+：ohos.permission.CUSTOM\_SCREEN\_CAPTURE 或 ohos.permission.CUSTOM\_SCREEN\_RECORDING
* API版本14-21：ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**起始版本：** 14

**设备行为差异：** 在API version 21之前，该接口在PC/2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。从API version 21开始，该接口在Phone设备、PC/2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t displayId | 需要截屏的屏幕ID，该值为非负整数。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) \*\*pixelMap | 创建指定屏幕ID的OH\_PixelmapNative对象，此处作为出参返回。使用完成需要调用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)手动释放OH\_PixelmapNative对象资源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [NativeDisplayManager\_ErrorCode](capi-oh-display-info-h.md#nativedisplaymanager_errorcode) | 返回DISPLAY\_MANAGER\_OK，表示操作成功。  返回DISPLAY\_MANAGER\_ERROR\_NO\_PERMISSION，表示权限校验失败，应用无权限使用该API，需要申请权限。  返回DISPLAY\_MANAGER\_ERROR\_INVALID\_PARAM，表示参数检查失败。  返回DISPLAY\_MANAGER\_ERROR\_DEVICE\_NOT\_SUPPORTED，表示该设备不支持此API。  返回DISPLAY\_MANAGER\_ERROR\_SYSTEM\_ABNORMAL，表示系统服务工作异常。 |
