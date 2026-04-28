---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h
title: oh_window_comm.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > oh_window_comm.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d1b62c4f2b36a86475da4202e5ed92f2305393578560763e2ba96fc869cf3e7b
---

## 概述

PhonePC/2in1TabletTVWearable

提供窗口的公共枚举、公共定义等。

**引用文件：** <window\_manager/oh\_window\_comm.h>

**库：** libnative\_window\_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 12

**相关模块：** [WindowManager](capi-windowmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [WindowManager\_Rect](capi-windowmanager-rect.md) | WindowManager\_Rect | 定义窗口矩形结构体，包含窗口位置和宽高信息。 |
| [OH\_PixelmapNative](capi-struct.md) | OH\_PixelmapNative | 定义像素图片信息。 |
| [WindowManager\_WindowProperties](capi-windowmanager-windowproperties.md) | WindowManager\_WindowProperties | 窗口属性。 |
| [WindowManager\_AvoidArea](capi-windowmanager-avoidarea.md) | WindowManager\_AvoidArea | 定义避让区域结构体。 |
| [WindowManager\_MainWindowInfo](capi-windowmanager-windowmanager-mainwindowinfo.md) | WindowManager\_MainWindowInfo | 主窗口信息。 |
| [WindowManager\_WindowSnapshotConfig](i-windowmanager-windowmanager-windowsnapshotconfig.md) | WindowManager\_WindowSnapshotConfig | 主窗口截图的配置项。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [WindowManager\_ErrorCode](capi-oh-window-comm-h.md#windowmanager_errorcode) | WindowManager\_ErrorCode | 窗口管理接口返回状态码枚举。 |
| [WindowManager\_AvoidAreaType](capi-oh-window-comm-h.md#windowmanager_avoidareatype) | WindowManager\_AvoidAreaType | 避让区域枚举类型。 |
| [WindowManager\_WindowType](capi-oh-window-comm-h.md#windowmanager_windowtype) | WindowManager\_WindowType | 窗口类型。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### WindowManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum WindowManager_ErrorCode
```

**描述**

窗口管理接口返回状态码枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OK = 0 | 成功。 |
| WINDOW\_MANAGER\_ERRORCODE\_NO\_PERMISSION = 201 | 无权限。  **起始版本：** 15 |
| WINDOW\_MANAGER\_ERRORCODE\_INVALID\_PARAM = 401 | 非法参数。  **起始版本：** 15 |
| WINDOW\_MANAGER\_ERRORCODE\_DEVICE\_NOT\_SUPPORTED = 801 | 设备不支持。  **起始版本：** 15 |
| INVAILD\_WINDOW\_ID = 1000 | 非法窗口ID。 |
| SERVICE\_ERROR = 2000 | 服务异常。 |
| WINDOW\_MANAGER\_ERRORCODE\_STATE\_ABNORMAL = 1300002 | 窗口状态异常。  **起始版本：** 15 |
| WINDOW\_MANAGER\_ERRORCODE\_SYSTEM\_ABNORMAL = 1300003 | 窗口管理器服务异常。  **起始版本：** 15 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_DESTROY\_FAILED = 1300011 | 画中画销毁失败。  **起始版本：** 20 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_STATE\_ABNORMAL = 1300012 | 画中画状态异常。  **起始版本：** 20 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_CREATE\_FAILED = 1300013 | 画中画创建失败。  **起始版本：** 20 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_INTERNAL\_ERROR = 1300014 | 画中画内部错误。可能原因：  1.画中画依赖的窗口异常，可能窗口为空；2.画中画控制器异常。  **起始版本：** 20 |
| WINDOW\_MANAGER\_ERRORCODE\_PIP\_REPEATED\_OPERATION = 1300015 | 画中画重复操作。  **起始版本：** 20 |
| WINDOW\_MANAGER\_ERRORCODE\_INCORRECT\_PARAM = 1300016 | 参数错误。 可能原因：  1.参数取值范围非法；2.参数数量非法；3.参数类型非法。  **起始版本：** 20 |

### WindowManager\_AvoidAreaType

PhonePC/2in1TabletTVWearable

```
1. enum WindowManager_AvoidAreaType
```

**描述**

避让区域枚举类型。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_SYSTEM = 0 | 系统避让区域。 |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_CUTOUT = 1 | 刘海屏避让。 |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_SYSTEM\_GESTURE = 2 | 系统手势区域。 |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_KEYBOARD = 3 | 键盘区域。 |
| WINDOW\_MANAGER\_AVOID\_AREA\_TYPE\_NAVIGATION\_INDICATOR = 4 | 导航条区域。 |

### WindowManager\_WindowType

PhonePC/2in1TabletTVWearable

```
1. enum WindowManager_WindowType
```

**描述**

窗口类型。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_APP = 0 | 子窗口。 |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_MAIN = 1 | 主窗口。 |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_FLOAT = 8 | 悬浮窗口。 |
| WINDOW\_MANAGER\_WINDOW\_TYPE\_DIALOG = 16 | 模态窗口。 |
