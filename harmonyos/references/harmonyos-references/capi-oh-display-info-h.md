---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h
title: oh_display_info.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_display_info.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:58+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:910c9cbd32b26964a2bc439091dac427a2e63ef25a45198971f06cbd31658e46
---

## 概述

PhonePC/2in1TabletTVWearable

提供屏幕的公共枚举、公共定义等。

**引用文件：** <window\_manager/oh\_display\_info.h>

**库：** libnative\_display\_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NativeDisplayManager\_Rect](capi-nativedisplaymanager-rect.md) | NativeDisplayManager\_Rect | 矩形区域。 |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](api-nativedisplaymanager-waterfalldisplayarearects.md) | NativeDisplayManager\_WaterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
| [NativeDisplayManager\_CutoutInfo](capi-nativedisplaymanager-cutoutinfo.md) | NativeDisplayManager\_CutoutInfo | 挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| [NativeDisplayManager\_DisplayHdrFormat](capi-nativedisplaymanager-displayhdrformat.md) | NativeDisplayManager\_DisplayHdrFormat | 显示设备支持的所有HDR格式。 |
| [NativeDisplayManager\_DisplayColorSpace](capi-nativedisplaymanager-displaycolorspace.md) | NativeDisplayManager\_DisplayColorSpace | 显示设备支持的所有色域类型。 |
| [NativeDisplayManager\_DisplayInfo](capi-nativedisplaymanager-displayinfo.md) | NativeDisplayManager\_DisplayInfo | 显示设备的对象属性。 |
| [NativeDisplayManager\_DisplaysInfo](capi-nativedisplaymanager-displaysinfo.md) | NativeDisplayManager\_DisplaysInfo | 多显示设备的Display对象。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_DISPLAY\_NAME\_LENGTH 32 | 屏幕名称的最大长度。  **起始版本：** 14 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NativeDisplayManager\_Rotation](capi-oh-display-info-h.md#nativedisplaymanager_rotation) | NativeDisplayManager\_Rotation | 屏幕顺时针的旋转角度。 |
| [NativeDisplayManager\_Orientation](capi-oh-display-info-h.md#nativedisplaymanager_orientation) | NativeDisplayManager\_Orientation | 屏幕的旋转方向。 |
| [NativeDisplayManager\_ErrorCode](capi-oh-display-info-h.md#nativedisplaymanager_errorcode) | NativeDisplayManager\_ErrorCode | 屏幕管理接口返回状态码枚举。 |
| [NativeDisplayManager\_FoldDisplayMode](capi-oh-display-info-h.md#nativedisplaymanager_folddisplaymode) | NativeDisplayManager\_FoldDisplayMode | 可折叠设备的显示模式枚举。 |
| [NativeDisplayManager\_DisplayState](capi-oh-display-info-h.md#nativedisplaymanager_displaystate) | NativeDisplayManager\_DisplayState | 显示设备的状态枚举。 |
| [NativeDisplayManager\_SourceMode](capi-oh-display-info-h.md#nativedisplaymanager_sourcemode) | NativeDisplayManager\_SourceMode | 设备的显示模式枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### NativeDisplayManager\_Rotation

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_Rotation
```

**描述**

屏幕顺时针的旋转角度。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_MANAGER\_ROTATION\_0 = 0 | 代表屏幕顺时针旋转角度0度。 |
| DISPLAY\_MANAGER\_ROTATION\_90 = 1 | 代表屏幕顺时针旋转角度90度。 |
| DISPLAY\_MANAGER\_ROTATION\_180 = 2 | 代表屏幕顺时针旋转角度180度。 |
| DISPLAY\_MANAGER\_ROTATION\_270 = 3 | 代表屏幕顺时针旋转角度270度。 |

### NativeDisplayManager\_Orientation

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_Orientation
```

**描述**

屏幕的旋转方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_MANAGER\_PORTRAIT = 0 | 表示设备当前以竖屏方式显示。 |
| DISPLAY\_MANAGER\_LANDSCAPE = 1 | 表示设备当前以横屏方式显示。 |
| DISPLAY\_MANAGER\_PORTRAIT\_INVERTED = 2 | 表示设备当前以反向竖屏方式显示。 |
| DISPLAY\_MANAGER\_LANDSCAPE\_INVERTED = 3 | 表示设备当前以反向横屏方式显示。 |
| DISPLAY\_MANAGER\_UNKNOWN | 表示显示未识别屏幕方向。 |

### NativeDisplayManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_ErrorCode
```

**描述**

屏幕管理接口返回状态码枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_MANAGER\_OK = 0 | 成功。 |
| DISPLAY\_MANAGER\_ERROR\_NO\_PERMISSION = 201 | 权限校验失败，应用无权限使用该API，需要申请权限。 |
| DISPLAY\_MANAGER\_ERROR\_NOT\_SYSTEM\_APP = 202 | 权限校验失败，非系统应用使用了系统API。 |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_PARAM = 401 | 参数检查失败。 |
| DISPLAY\_MANAGER\_ERROR\_DEVICE\_NOT\_SUPPORTED = 801 | 该设备不支持此API。 |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_SCREEN = 1400001 | 操作的显示设备无效。 |
| DISPLAY\_MANAGER\_ERROR\_INVALID\_CALL = 1400002 | 当前操作对象无操作权限。 |
| DISPLAY\_MANAGER\_ERROR\_SYSTEM\_ABNORMAL = 1400003 | 系统服务工作异常。 |
| DISPLAY\_MANAGER\_ERROR\_ILLEGAL\_PARAM = 1400004 | 非法参数。  **起始版本：** 20 |

### NativeDisplayManager\_FoldDisplayMode

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_FoldDisplayMode
```

**描述**

可折叠设备的显示模式枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_UNKNOWN = 0 | 表示设备当前折叠显示模式未知。 |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_FULL = 1 | 表示设备当前全屏显示。 |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_MAIN = 2 | 表示设备当前主屏幕显示。 |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_SUB = 3 | 表示设备当前子屏幕显示。 |
| DISPLAY\_MANAGER\_FOLD\_DISPLAY\_MODE\_COORDINATION = 4 | 表示设备当前双屏协同显示。 |

### NativeDisplayManager\_DisplayState

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_DisplayState
```

**描述**

显示设备的状态枚举。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_UNKNOWN = 0 | 表示显示设备状态未知。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_OFF = 1 | 表示显示设备状态为关闭。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_ON = 2 | 表示显示设备状态为开启。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_DOZE = 3 | 表示显示设备为低电耗模式。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_DOZE\_SUSPEND = 4 | 表示显示设备为睡眠模式，CPU为挂起状态。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_VR = 5 | 表示显示设备为VR模式。 |
| DISPLAY\_MANAGER\_DISPLAY\_STATE\_ON\_SUSPEND = 6 | 表示显示设备为开启状态，CPU为挂起状态。 |

### NativeDisplayManager\_SourceMode

PhonePC/2in1TabletTVWearable

```
1. enum NativeDisplayManager_SourceMode
```

**描述**

设备的显示模式枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY\_SOURCE\_MODE\_NONE = 0 | 表示设备当前未使用。 |
| DISPLAY\_SOURCE\_MODE\_MAIN = 1 | 表示设备当前为主屏。 |
| DISPLAY\_SOURCE\_MODE\_MIRROR = 2 | 表示设备当前为镜像显示模式。 |
| DISPLAY\_SOURCE\_MODE\_EXTEND = 3 | 表示设备当前为扩展显示模式。 |
| DISPLAY\_SOURCE\_MODE\_ALONE = 4 | 表示设备当前为异源显示模式。 |
