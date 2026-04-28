---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-pip-h
title: oh_window_pip.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_window_pip.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f3e661267815351515a14f5a7855e33743d99b82dcb42d262c70d1077e181e8
---

## 概述

PhonePC/2in1TabletTVWearable

定义画中画功能的相关接口，包含创建、删除画中画控制器，以及启动、停止画中画等。主要用于视频播放、直播、视频通话或视频会议场景下，以小窗（画中画）模式呈现内容。

**引用文件：** <window\_manager/oh\_window\_pip.h>

**库：** libnative\_window\_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 20

**相关模块：** [WindowManager](capi-windowmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) | 画中画参数配置器。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [PictureInPicture\_PipTemplateType](capi-oh-window-pip-h.md#pictureinpicture_piptemplatetype) | PictureInPicture\_PipTemplateType | 画中画模板类型。 |
| [PictureInPicture\_PipControlGroup](capi-oh-window-pip-h.md#pictureinpicture_pipcontrolgroup) | PictureInPicture\_PipControlGroup | 画中画控制面板的控件组类型。 |
| [PictureInPicture\_PipControlType](capi-oh-window-pip-h.md#pictureinpicture_pipcontroltype) | PictureInPicture\_PipControlType | 控制面板控件类型枚举。 |
| [PictureInPicture\_PipControlStatus](capi-oh-window-pip-h.md#pictureinpicture_pipcontrolstatus) | PictureInPicture\_PipControlStatus | 控制面板控件状态枚举。 |
| [PictureInPicture\_PipState](capi-oh-window-pip-h.md#pictureinpicture_pipstate) | PictureInPicture\_PipState | 画中画生命周期状态枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*WebPipStartPipCallback)(uint32\_t controllerId, uint8\_t requestId, uint64\_t surfaceId)](capi-oh-window-pip-h.md#webpipstartpipcallback) | WebPipStartPipCallback | 定义画中画窗口创建完成的回调函数。 |
| [typedef void (\*WebPipLifecycleCallback)(uint32\_t controllerId, PictureInPicture\_PipState state, int32\_t errcode)](capi-oh-window-pip-h.md#webpiplifecyclecallback) | WebPipLifecycleCallback | 定义画中画窗口的生命周期回调函数。 |
| [typedef void (\*WebPipControlEventCallback)(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,PictureInPicture\_PipControlStatus status)](capi-oh-window-pip-h.md#webpipcontroleventcallback) | WebPipControlEventCallback | 定义画中画窗口的控件点击事件回调函数。 |
| [typedef void (\*WebPipResizeCallback)(uint32\_t controllerId, uint32\_t width, uint32\_t height, double scale)](capi-oh-window-pip-h.md#webpipresizecallback) | WebPipResizeCallback | 定义画中画窗口的尺寸变化回调函数。 |
| [int32\_t OH\_PictureInPicture\_CreatePipConfig(PictureInPicture\_PipConfig\* pipConfig)](capi-oh-window-pip-h.md#oh_pictureinpicture_createpipconfig) | - | 创建画中画参数配置器。 |
| [int32\_t OH\_PictureInPicture\_DestroyPipConfig(PictureInPicture\_PipConfig\* pipConfig)](capi-oh-window-pip-h.md#oh_pictureinpicture_destroypipconfig) | - | 销毁画中画参数配置器。 |
| [int32\_t OH\_PictureInPicture\_SetPipMainWindowId(PictureInPicture\_PipConfig pipConfig, uint32\_t mainWindowId)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipmainwindowid) | - | 设置拉起画中画的主窗口Id。 |
| [int32\_t OH\_PictureInPicture\_SetPipTemplateType(PictureInPicture\_PipConfig pipConfig,PictureInPicture\_PipTemplateType pipTemplateType)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpiptemplatetype) | - | 设置画中画模板类型，默认为视频播放。 |
| [int32\_t OH\_PictureInPicture\_SetPipRect(PictureInPicture\_PipConfig pipConfig, uint32\_t width, uint32\_t height)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpiprect) | - | 设置画中画窗口大小，用于计算尺寸比例。 |
| [int32\_t OH\_PictureInPicture\_SetPipControlGroup(PictureInPicture\_PipConfig pipConfig,PictureInPicture\_PipControlGroup\* controlGroup, uint8\_t controlGroupLength)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipcontrolgroup) | - | 设置画中画控件组，需保证控件组与模板类型匹配。 |
| [int32\_t OH\_PictureInPicture\_SetPipNapiEnv(PictureInPicture\_PipConfig pipConfig, void\* env)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipnapienv) | - | 设置拉起画中画的运行时环境。 |
| [int32\_t OH\_PictureInPicture\_CreatePip(PictureInPicture\_PipConfig pipConfig, uint32\_t\* controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_createpip) | - | 创建画中画控制器。 |
| [int32\_t OH\_PictureInPicture\_DeletePip(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_deletepip) | - | 删除画中画控制器。 |
| [int32\_t OH\_PictureInPicture\_StartPip(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_startpip) | - | 开启画中画。 |
| [int32\_t OH\_PictureInPicture\_StopPip(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_stoppip) | - | 关闭画中画。 |
| [int32\_t OH\_PictureInPicture\_UpdatePipContentSize(uint32\_t controllerId, uint32\_t width, uint32\_t height)](capi-oh-window-pip-h.md#oh_pictureinpicture_updatepipcontentsize) | - | 当媒体源切换时，向画中画控制器更新媒体源尺寸信息。 |
| [int32\_t OH\_PictureInPicture\_UpdatePipControlStatus(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,PictureInPicture\_PipControlStatus status)](capi-oh-window-pip-h.md#oh_pictureinpicture_updatepipcontrolstatus) | - | 更新画中画控制面板控件功能状态。 |
| [int32\_t OH\_PictureInPicture\_SetPipControlEnabled(uint32\_t controllerId, PictureInPicture\_PipControlType controlType,bool enabled)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipcontrolenabled) | - | 设置控制面板控件使能状态。 |
| [int32\_t OH\_PictureInPicture\_RegisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_registerstartpipcallback) | - | 开启画中画surface创建完成的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterstartpipcallback) | - | 关闭画中画surface创建完成的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterAllStartPipCallbacks(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterallstartpipcallbacks) | - | 关闭所有画中画surface创建完成的监听。 |
| [int32\_t OH\_PictureInPicture\_RegisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_registerlifecyclelistener) | - | 开启画中画生命周期状态的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterLifecycleListener(uint32\_t controllerId, WebPipLifecycleCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterlifecyclelistener) | - | 关闭画中画生命周期状态的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterAllLifecycleListeners(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisteralllifecyclelisteners) | - | 关闭所有画中画生命周期状态的监听。 |
| [int32\_t OH\_PictureInPicture\_RegisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_registercontroleventlistener) | - | 开启画中画控制面板控件动作事件的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregistercontroleventlistener) | - | 关闭画中画控制面板控件动作事件的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterAllControlEventListeners(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterallcontroleventlisteners) | - | 关闭所有画中画控制面板控件动作事件的监听。 |
| [int32\_t OH\_PictureInPicture\_RegisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_registerresizelistener) | - | 开启画中画窗口尺寸变化事件的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterresizelistener) | - | 关闭画中画窗口尺寸变化事件的监听。 |
| [int32\_t OH\_PictureInPicture\_UnregisterAllResizeListeners(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_unregisterallresizelisteners) | - | 关闭所有画中画窗口尺寸变化事件的监听。 |
| [int32\_t OH\_PictureInPicture\_SetPipInitialSurfaceRect(uint32\_t controllerId, int32\_t positionX, int32\_t positionY,uint32\_t width, uint32\_t height)](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipinitialsurfacerect) | - | 设置画中画拉起动效开始时的位置和大小，可用于实现一镜到底效果。 |
| [int32\_t OH\_PictureInPicture\_UnsetPipInitialSurfaceRect(uint32\_t controllerId)](capi-oh-window-pip-h.md#oh_pictureinpicture_unsetpipinitialsurfacerect) | - | 取消已设置的画中画拉起动效的起始位置和大小。 |
| [int32\_t OH\_PictureInPicture\_SetParentWindowId(uint32\_t controllerId, uint32\_t windowId)](capi-oh-window-pip-h.md#oh_pictureinpicture_setparentwindowid) | - | 设置画中画主窗口ID。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### PictureInPicture\_PipTemplateType

PhonePC/2in1TabletTVWearable

```
1. enum PictureInPicture_PipTemplateType
```

**描述**

画中画模板类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_PLAY = 0 | 表示将要切换为画中画播放的媒体类型是视频，系统依此加载视频播放模板。 |
| VIDEO\_CALL = 1 | 表示将要切换为画中画播放的媒体类型是视频通话，系统依此加载视频通话模板。 |
| VIDEO\_MEETING = 2 | 表示将要切换为画中画播放的媒体类型是视频会议，系统依此加载视频会议模板。 |
| VIDEO\_LIVE = 3 | 表示将要切换为画中画播放的媒体类型是直播，系统依此加载直播模板。 |

### PictureInPicture\_PipControlGroup

PhonePC/2in1TabletTVWearable

```
1. enum PictureInPicture_PipControlGroup
```

**描述**

画中画控制面板的控件组类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_PLAY\_VIDEO\_PREVIOUS\_NEXT = 101 | 视频播放模板的视频上一个/下一个控件组。与视频快进/后退控件组为互斥控件组。如添加视频快进/后退控件组，则不可添加该控件组。 |
| VIDEO\_PLAY\_FAST\_FORWARD\_BACKWARD = 102 | 视频播放模板的视频快进/后退控件组。与视频上一个/下一个控件组为互斥控件组。如添加视频上一个/下一个控件组，则不可添加该控件组。 |
| VIDEO\_CALL\_MICROPHONE\_SWITCH = 201 | 视频通话模板的打开/关闭麦克风控件组。 |
| VIDEO\_CALL\_HANG\_UP\_BUTTON = 202 | 视频通话模板的挂断控件组。 |
| VIDEO\_CALL\_CAMERA\_SWITCH = 203 | 视频通话模板的打开/关闭摄像头控件组。 |
| VIDEO\_CALL\_MUTE\_SWITCH = 204 | 视频通话模板的静音控件组。 |
| VIDEO\_MEETING\_HANG\_UP\_BUTTON = 301 | 视频会议模板的挂断控件组。 |
| VIDEO\_MEETING\_CAMERA\_SWITCH = 302 | 视频会议模板的打开/关闭摄像头控件组。 |
| VIDEO\_MEETING\_MUTE\_SWITCH = 303 | 视频会议模板的静音控件组。 |
| VIDEO\_MEETING\_MICROPHONE\_SWITCH = 304 | 视频会议模板的打开/关闭麦克风控件组。 |
| VIDEO\_LIVE\_VIDEO\_PLAY\_PAUSE = 401 | 直播模板的播放/暂停直播控件组。 |
| VIDEO\_LIVE\_MUTE\_SWITCH = 402 | 直播模板的静音控件组。 |

### PictureInPicture\_PipControlType

PhonePC/2in1TabletTVWearable

```
1. enum PictureInPicture_PipControlType
```

**描述**

控制面板控件类型枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_PLAY\_PAUSE = 0 | 播放/暂停控件。 |
| VIDEO\_PREVIOUS = 1 | 视频上一个控件。 |
| VIDEO\_NEXT = 2 | 视频下一个控件。 |
| FAST\_FORWARD = 3 | 视频快进控件。 |
| FAST\_BACKWARD = 4 | 视频快退控件。 |
| HANG\_UP\_BUTTON = 5 | 挂断控件。 |
| MICROPHONE\_SWITCH = 6 | 打开/关闭麦克风控件。 |
| CAMERA\_SWITCH = 7 | 打开/关闭摄像头控件。 |
| MUTE\_SWITCH = 8 | 打开/关闭静音控件。 |

### PictureInPicture\_PipControlStatus

PhonePC/2in1TabletTVWearable

```
1. enum PictureInPicture_PipControlStatus
```

**描述**

控制面板控件状态枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| PLAY = 1 | 视频播放状态。 |
| PAUSE = 0 | 视频暂停状态。 |
| OPEN = 1 | 摄像头/麦克风/静音控件的打开状态。 |
| CLOSE = 0 | 摄像头/麦克风/静音控件的关闭状态。 |

### PictureInPicture\_PipState

PhonePC/2in1TabletTVWearable

```
1. enum PictureInPicture_PipState
```

**描述**

画中画生命周期状态枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| ABOUT\_TO\_START = 1 | 表示画中画将要启动。 |
| STARTED = 2 | 表示画中画已经启动。 |
| ABOUT\_TO\_STOP = 3 | 表示画中画将要停止。 |
| STOPPED = 4 | 表示画中画已经停止。 |
| ABOUT\_TO\_RESTORE = 5 | 表示画中画将从小窗播放恢复到原始播放界面。 |
| ERROR = 6 | 表示画中画生命周期执行过程出现了异常。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### WebPipStartPipCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebPipStartPipCallback)(uint32_t controllerId, uint8_t requestId, uint64_t surfaceId)
```

**描述**

定义画中画窗口创建完成的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| uint8\_t requestId | 请求Id，表示当前请求拉起画中画窗口的次数。 |
| uint64\_t surfaceId | 画中画内部Xcomponent组件的surfaceId，用于应用自行渲染。 |

### WebPipLifecycleCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebPipLifecycleCallback)(uint32_t controllerId, PictureInPicture_PipState state, int32_t errcode)
```

**描述**

定义画中画窗口的生命周期回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| PictureInPicture\_PipState state | 当前画中画生命周期状态。 |
| int32\_t errcode | 画中画接口的通用状态码。具体可见[WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode)。 |

### WebPipControlEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebPipControlEventCallback)(uint32_t controllerId, PictureInPicture_PipControlType controlType, PictureInPicture_PipControlStatus status)
```

**描述**

定义画中画窗口的控件点击事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| PictureInPicture\_PipControlType controlType | 画中画控制面板的控件类型。 |
| [PictureInPicture\_PipControlStatus](capi-oh-window-pip-h.md#pictureinpicture_pipcontrolstatus) status | 画中画控制面板的控件状态。 |

### WebPipResizeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*WebPipResizeCallback)(uint32_t controllerId, uint32_t width, uint32_t height, double scale)
```

**描述**

定义画中画窗口的尺寸变化回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| uint32\_t width | 画中画窗口宽度，单位为px，该参数为正整数，不大于屏幕宽。 |
| uint32\_t height | 画中画窗口高度，单位为px，该参数为正整数，不大于屏幕高。 |
| double scale | 画中画窗口缩放比，显示大小相对于width和height的缩放比，该参数为浮点数，取值范围大于0.0，小于等于1.0。等于1表示画中画窗口的实际显示宽高值与width和height一样大。 |

### OH\_PictureInPicture\_CreatePipConfig()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_CreatePipConfig(PictureInPicture_PipConfig* pipConfig)
```

**描述**

创建画中画参数配置器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md)\* pipConfig | 用于接受创建的画中画参数配置器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。 |

### OH\_PictureInPicture\_DestroyPipConfig()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_DestroyPipConfig(PictureInPicture_PipConfig* pipConfig)
```

**描述**

销毁画中画参数配置器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md)\* pipConfig | 画中画参数配置器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。 |

### OH\_PictureInPicture\_SetPipMainWindowId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipMainWindowId(PictureInPicture_PipConfig pipConfig, uint32_t mainWindowId)
```

**描述**

设置拉起画中画的主窗口Id。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| uint32\_t mainWindowId | 拉起画中画的主窗口Id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。 |

### OH\_PictureInPicture\_SetPipTemplateType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipTemplateType(PictureInPicture_PipConfig pipConfig, PictureInPicture_PipTemplateType pipTemplateType)
```

**描述**

设置画中画模板类型，默认为视频播放。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| [PictureInPicture\_PipTemplateType](capi-oh-window-pip-h.md#pictureinpicture_piptemplatetype) pipTemplateType | 画中画模板类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。 |

### OH\_PictureInPicture\_SetPipRect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipRect(PictureInPicture_PipConfig pipConfig, uint32_t width, uint32_t height)
```

**描述**

设置画中画窗口大小，用于计算尺寸比例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| uint32\_t width | 原始内容宽度，单位为px，该参数应为正整数。用于确定画中画窗口比例。 |
| uint32\_t height | 原始内容高度，单位为px，该参数应为正整数。用于确定画中画窗口比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。 |

### OH\_PictureInPicture\_SetPipControlGroup()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipControlGroup(PictureInPicture_PipConfig pipConfig, PictureInPicture_PipControlGroup* controlGroup, uint8_t controlGroupLength)
```

**描述**

设置画中画控件组，需保证控件组与模板类型匹配。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| [PictureInPicture\_PipControlGroup](capi-oh-window-pip-h.md#pictureinpicture_pipcontrolgroup)\* controlGroup | 画中画控制面板的可选控件组列表，应用可以对此进行配置以决定是否显示。应用未配置时，面板显示基础控件（如视频播放控件组的播放/暂停控件）；应用选择配置时，则最多可以选择三个控件。 |
| uint8\_t controlGroupLength | 画中画控件组数量，取值范围为0 ~ 3。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。 |

### OH\_PictureInPicture\_SetPipNapiEnv()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipNapiEnv(PictureInPicture_PipConfig pipConfig, void* env)
```

**描述**

设置拉起画中画的运行时环境。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| void\* env | napi的环境指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。 |

### OH\_PictureInPicture\_CreatePip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_CreatePip(PictureInPicture_PipConfig pipConfig, uint32_t* controllerId)
```

**描述**

创建画中画控制器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [PictureInPicture\_PipConfig](capi-pictureinpicture-pipconfig.md) pipConfig | 画中画参数配置器。 |
| uint32\_t\* controllerId | 用于接收创建画中画控制器的id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_DeletePip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_DeletePip(uint32_t controllerId)
```

**描述**

删除画中画控制器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。 |

### OH\_PictureInPicture\_StartPip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_StartPip(uint32_t controllerId)
```

**描述**

开启画中画。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL，表示画中画窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_CREATE\_FAILED，表示画中画窗口创建失败。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION，表示画中画窗口重复操作。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。 |

### OH\_PictureInPicture\_StopPip()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_StopPip(uint32_t controllerId)
```

**描述**

关闭画中画。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_DESTROY\_FAILED，表示画中画窗口销毁失败。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL，表示画中画窗口状态异常。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION，表示画中画窗口重复操作。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。 |

### OH\_PictureInPicture\_UpdatePipContentSize()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UpdatePipContentSize(uint32_t controllerId, uint32_t width, uint32_t height)
```

**描述**

当媒体源切换时，向画中画控制器更新媒体源尺寸信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| uint32\_t width | 表示媒体内容宽度，单位为px，该参数应为正整数。用于更新画中画窗口比例。 |
| uint32\_t height | 表示媒体内容高度，单位为px，该参数应为正整数。用于更新画中画窗口比例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UpdatePipControlStatus()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UpdatePipControlStatus(uint32_t controllerId, PictureInPicture_PipControlType controlType, PictureInPicture_PipControlStatus status)
```

**描述**

更新画中画控制面板控件功能状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [PictureInPicture\_PipControlType](capi-oh-window-pip-h.md#pictureinpicture_pipcontroltype) controlType | 表示画中画控制面板控件类型。目前仅支持VIDEO\_PLAY\_PAUSE、MICROPHONE\_SWITCH、CAMERA\_SWITCH和MUTE\_SWITCH这几种控件类型，传入其他控件类型无效。 |
| [PictureInPicture\_PipControlStatus](capi-oh-window-pip-h.md#pictureinpicture_pipcontrolstatus) status | 表示画中画控制面板控件状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_SetPipControlEnabled()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipControlEnabled(uint32_t controllerId, PictureInPicture_PipControlType controlType, bool enabled)
```

**描述**

设置控制面板控件使能状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [PictureInPicture\_PipControlType](capi-oh-window-pip-h.md#pictureinpicture_pipcontroltype) controlType | 表示画中画控制面板控件类型。 |
| bool enabled | 表示画中画控制面板控件使能状态。true表示控件为可使用状态，false则为禁用状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_RegisterStartPipCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_RegisterStartPipCallback(uint32_t controllerId, WebPipStartPipCallback callback)
```

**描述**

开启画中画surface创建完成的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipStartPipCallback](capi-oh-window-pip-h.md#webpipstartpipcallback) callback | 画中画窗口创建完成的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterStartPipCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterStartPipCallback(uint32_t controllerId, WebPipStartPipCallback callback)
```

**描述**

关闭画中画surface创建完成的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipStartPipCallback](capi-oh-window-pip-h.md#webpipstartpipcallback) callback | 画中画窗口创建完成的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterAllStartPipCallbacks()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterAllStartPipCallbacks(uint32_t controllerId)
```

**描述**

关闭所有画中画surface创建完成的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_RegisterLifecycleListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_RegisterLifecycleListener(uint32_t controllerId, WebPipLifecycleCallback callback)
```

**描述**

开启画中画生命周期状态的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipLifecycleCallback](capi-oh-window-pip-h.md#webpiplifecyclecallback) callback | 画中画窗口的生命周期回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterLifecycleListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterLifecycleListener(uint32_t controllerId, WebPipLifecycleCallback callback)
```

**描述**

关闭画中画生命周期状态的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipLifecycleCallback](capi-oh-window-pip-h.md#webpiplifecyclecallback) callback | 画中画窗口的生命周期回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterAllLifecycleListeners()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterAllLifecycleListeners(uint32_t controllerId)
```

**描述**

关闭所有画中画生命周期状态的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_RegisterControlEventListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_RegisterControlEventListener(uint32_t controllerId, WebPipControlEventCallback callback)
```

**描述**

开启画中画控制面板控件动作事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipControlEventCallback](capi-oh-window-pip-h.md#webpipcontroleventcallback) callback | 画中画窗口的控件点击事件回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterControlEventListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterControlEventListener(uint32_t controllerId, WebPipControlEventCallback callback)
```

**描述**

关闭画中画控制面板控件动作事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipControlEventCallback](capi-oh-window-pip-h.md#webpipcontroleventcallback) callback | 画中画窗口的控件点击事件回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterAllControlEventListeners()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterAllControlEventListeners(uint32_t controllerId)
```

**描述**

关闭所有画中画控制面板控件动作事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_RegisterResizeListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_RegisterResizeListener(uint32_t controllerId, WebPipResizeCallback callback)
```

**描述**

开启画中画窗口尺寸变化事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipResizeCallback](capi-oh-window-pip-h.md#webpipresizecallback) callback | 画中画窗口尺寸变化的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterResizeListener()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterResizeListener(uint32_t controllerId, WebPipResizeCallback callback)
```

**描述**

关闭画中画窗口尺寸变化事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| [WebPipResizeCallback](capi-oh-window-pip-h.md#webpipresizecallback) callback | 画中画窗口尺寸变化的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnregisterAllResizeListeners()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnregisterAllResizeListeners(uint32_t controllerId)
```

**描述**

关闭所有画中画窗口尺寸变化事件的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_SetPipInitialSurfaceRect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetPipInitialSurfaceRect(uint32_t controllerId, int32_t positionX, int32_t positionY,uint32_t width, uint32_t height)
```

**描述**

设置画中画拉起动效开始时的位置和大小，可用于实现一镜到底效果。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| int32\_t positionX | 拉起时画中画窗口相对页面左上角的X坐标，单位为px。 |
| int32\_t positionY | 拉起时画中画窗口相对页面左上角的Y坐标，单位为px。 |
| uint32\_t width | 拉起时画中画窗口的宽度，该参数值大于0，单位为px。 |
| uint32\_t height | 拉起时画中画窗口的高度，该参数值大于0，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_UnsetPipInitialSurfaceRect()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_UnsetPipInitialSurfaceRect(uint32_t controllerId)
```

**描述**

取消已设置的画中画拉起动效的起始位置和大小。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |

### OH\_PictureInPicture\_SetParentWindowId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_PictureInPicture_SetParentWindowId(uint32_t controllerId, uint32_t windowId)
```

**描述**

设置画中画主窗口ID。

在拉起画中画前，需调用[OH\_PictureInPicture\_SetPipMainWindowId()](capi-oh-window-pip-h.md#oh_pictureinpicture_setpipmainwindowid)设置拉起画中画的主窗口ID。

当画中画的主窗口改变时（如浏览器多个页签在同一个窗口的场景下，在此窗口的A页签下拉起画中画后，将A页签拖出形成一个新的窗口时），需调用该接口设置画中画主窗口ID为新窗口ID，以保证画中画可还原至正确的主窗口（即拉起画中画的主窗口）。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t controllerId | 画中画控制器Id，为非负整数。 |
| uint32\_t windowId | 表示画中画父窗口Id，为非负整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回结果代码。  返回OK，表示函数调用成功。  返回WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM，表示参数错误。  返回WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED，表示设备不支持画中画。  返回WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR，表示画中画内部错误。 |
