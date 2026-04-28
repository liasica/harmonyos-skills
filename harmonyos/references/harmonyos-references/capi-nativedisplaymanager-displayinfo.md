---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo
title: NativeDisplayManager_DisplayInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:40+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f9d7bf401bd761f5698392fff981eb31b1fb10ee57a2097e0343c826ed832591
---

```
1. typedef struct {...} NativeDisplayManager_DisplayInfo
```

## 概述

PhonePC/2in1TabletTVWearable

显示设备的对象属性。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t id | 显示设备的屏幕id号，为非负整数。 |
| char name[[OH\_DISPLAY\_NAME\_LENGTH](capi-oh-display-info-h.md#宏定义) + 1] | 显示设备的名称。 |
| bool isAlive | 显示设备是否启用：true表示设备启动，false表示设备未启用。 |
| int32\_t width | 显示设备的屏幕宽度，单位为px，该参数应为非负整数。 |
| int32\_t height | 显示设备的屏幕高度，单位为px，该参数应为非负整数。 |
| int32\_t physicalWidth | 显示设备的物理宽度，单位为px，该参数应为非负整数。 |
| int32\_t physicalHeight | 显示设备的物理高度，单位为px，该参数应为非负整数。 |
| uint32\_t refreshRate | 显示设备的刷新率，单位为Hz，该参数应为非负整数。 |
| uint32\_t availableWidth | 2in1设备上屏幕的可用区域宽度，单位为px，该参数为非负整数。 |
| uint32\_t availableHeight | 2in1设备上屏幕的可用区域高度，单位为px，该参数为大于0的整数。 |
| float densityDPI | 显示设备屏幕的物理像素密度，表示每英寸上的像素点数。该参数为大于0的浮点数，单位为px。一般取值160.0、480.0等，实际能取到的值取决于不同设备设置里提供的可选值。 |
| float densityPixels | 显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数。该参数为大于0的浮点数，受densityDPI范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDPI。 |
| float scaledDensity | 显示设备的显示字体的缩放因子。该参数为大于0的浮点数，通常与densityPixels相同。 |
| float xDPI | 显示设备x方向中每英寸屏幕的确切物理像素值，该参数为大于0的浮点数。 |
| float yDPI | 显示设备y方向中每英寸屏幕的确切物理像素值，该参数为大于0的浮点数。 |
| [NativeDisplayManager\_Rotation](capi-oh-display-info-h.md#nativedisplaymanager_rotation) rotation | 显示设备的屏幕顺时针旋转角度。 |
| [NativeDisplayManager\_DisplayState](capi-oh-display-info-h.md#nativedisplaymanager_displaystate) state | 显示设备的状态。 |
| [NativeDisplayManager\_Orientation](capi-oh-display-info-h.md#nativedisplaymanager_orientation) orientation | 表示屏幕当前显示的方向。 |
| [NativeDisplayManager\_DisplayHdrFormat](capi-nativedisplaymanager-displayhdrformat.md)\* hdrFormat | 显示设备支持的所有HDR格式。 |
| [NativeDisplayManager\_DisplayColorSpace](capi-nativedisplaymanager-displaycolorspace.md)\* colorSpace | 显示设备支持的所有色域类型。 |
