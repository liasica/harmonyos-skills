---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-progress-h
title: progress.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > progress.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:49d90f865669edc0667953249f7efe802de512e9d7c2037cbd7862908ec757be
---

## 概述

定义Progress相关的枚举和接口，支持线性、环形、圆形、胶囊等多种进度条类型，并提供线性进度条样式选项的自定义能力（平滑动效、扫光效果、宽度、圆角），适用于需要展示任务进度、加载状态等场景，帮助开发者快速实现多样化的进度展示和交互反馈。

**引用文件：** <arkui/node\_attributes/progress.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md) | ArkUI\_ProgressLinearStyleOption | 定义线性进度条的样式选项，适用于需要自定义线性进度条显示样式的场景。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ProgressType](capi-progress-h.md#arkui_progresstype) | ArkUI\_ProgressType | 定义进度条类型枚举值。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption\* OH\_ArkUI\_ProgressLinearStyleOption\_Create(void)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_create) | 创建线性进度条样式信息。使用完毕后必须调用[OH\_ArkUI\_ProgressLinearStyleOption\_Destroy](capi-progress-h.md#oh_arkui_progresslinearstyleoption_destroy)释放资源，避免内存泄漏。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_Destroy(ArkUI\_ProgressLinearStyleOption\* option)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_destroy) | 销毁线性进度条样式信息。必须与[OH\_ArkUI\_ProgressLinearStyleOption\_Create](capi-progress-h.md#oh_arkui_progresslinearstyleoption_create)配对使用，参数option应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()获取，调用OH\_ArkUI\_ProgressLinearStyleOption\_Destroy()后不应再使用该对象。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_setsmootheffectenabled) | 设置进度平滑动效的开关。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option, bool enabled)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_setscaneffectenabled) | 设置扫光效果的开关。适用于需要增强进度条视觉反馈效果的加载场景，如数据加载、文件上传等。扫光效果指进度条上有光线扫描移动的动态视觉效果。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option, float strokeWidth)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_setstrokewidth) | 设置进度条宽度。 |
| [void OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option, float strokeRadius)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_setstrokeradius) | 设置进度条圆角半径。 |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_getsmootheffectenabled) | 获取进度平滑动效的开关信息。 |
| [bool OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled(ArkUI\_ProgressLinearStyleOption\* option)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_getscaneffectenabled) | 获取扫光效果的开关信息。 |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth(ArkUI\_ProgressLinearStyleOption\* option)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_getstrokewidth) | 获取进度条宽度。 |
| [float OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius(ArkUI\_ProgressLinearStyleOption\* option)](capi-progress-h.md#oh_arkui_progresslinearstyleoption_getstrokeradius) | 获取进度条圆角半径值。 |

## 枚举类型说明

### ArkUI\_ProgressType

```c
enum ArkUI_ProgressType
```

**描述**

定义进度条类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PROGRESS\_TYPE\_LINEAR = 0 | 线性样式。 |
| ARKUI\_PROGRESS\_TYPE\_RING = 1 | 环形无刻度样式，环形圆环逐渐显示直至完全填充。 |
| ARKUI\_PROGRESS\_TYPE\_ECLIPSE = 2 | 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。 |
| ARKUI\_PROGRESS\_TYPE\_SCALE\_RING = 3 | 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。 |
| ARKUI\_PROGRESS\_TYPE\_CAPSULE = 4 | 胶囊样式，头尾两端圆弧处的进度展示效果与ARKUI\_PROGRESS\_TYPE\_ECLIPSE相同，中段的进度展示效果与ARKUI\_PROGRESS\_TYPE\_LINEAR相同。 |

## 函数说明

### OH\_ArkUI\_ProgressLinearStyleOption\_Create()

```c
ArkUI_ProgressLinearStyleOption* OH_ArkUI_ProgressLinearStyleOption_Create(void)
```

**描述**

创建线性进度条样式信息。使用完毕后必须调用[OH\_ArkUI\_ProgressLinearStyleOption\_Destroy](capi-progress-h.md#oh_arkui_progresslinearstyleoption_destroy)释放资源，避免内存泄漏。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption\*](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md) | ArkUI\_ProgressLinearStyleOption实例，可用于配置线性进度条的平滑动效、扫光效果、宽度和圆角等显示样式。  如果返回空指针，可能是因为内存不足。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_Destroy()

```c
void OH_ArkUI_ProgressLinearStyleOption_Destroy(ArkUI_ProgressLinearStyleOption* option)
```

**描述**

销毁线性进度条样式信息。必须与[OH\_ArkUI\_ProgressLinearStyleOption\_Create](capi-progress-h.md#oh_arkui_progresslinearstyleoption_create)配对使用，参数option应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()获取，调用OH\_ArkUI\_ProgressLinearStyleOption\_Destroy()后不应再使用该对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()获取。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetSmoothEffectEnabled()

```c
void OH_ArkUI_ProgressLinearStyleOption_SetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

**描述**

设置进度平滑动效的开关。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |
| bool enabled | 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。  true：表示开启进度平滑动效。  false：表示关闭进度平滑动效。  默认值：true。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetScanEffectEnabled()

```c
void OH_ArkUI_ProgressLinearStyleOption_SetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option, bool enabled)
```

**描述**

设置扫光效果的开关。适用于需要增强进度条视觉反馈效果的加载场景，如数据加载、文件上传等。扫光效果指进度条上有光线扫描移动的动态视觉效果。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |
| bool enabled | 扫光效果的开关。  true：表示开启扫光效果。  false：表示关闭扫光效果。  默认值：false。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeWidth()

```c
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeWidth(ArkUI_ProgressLinearStyleOption* option, float strokeWidth)
```

**描述**

设置进度条宽度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |
| float strokeWidth | 进度条宽度值（不支持百分比设置），单位为vp，取值需大于0，传入不合法值时使用默认值。默认值：4.0vp。设置strokeWidth会影响strokeRadius的取值范围，strokeRadius取值范围为[0, strokeWidth/2]。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_SetStrokeRadius()

```c
void OH_ArkUI_ProgressLinearStyleOption_SetStrokeRadius(ArkUI_ProgressLinearStyleOption* option, float strokeRadius)
```

**描述**

设置进度条圆角半径。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |
| float strokeRadius | 进度条圆角半径值，单位为vp，取值范围[0, strokeWidth/2]。值为0时进度条显示直角，值越大圆角越明显，最大值时显示为完全圆角。超出范围时自动修正为边界值。默认值：strokeWidth/2。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetSmoothEffectEnabled()

```c
bool OH_ArkUI_ProgressLinearStyleOption_GetSmoothEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

**描述**

获取进度平滑动效的开关信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启平滑动效。true：表示开启进度平滑动效。false：表示关闭进度平滑动效。默认值：true。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetScanEffectEnabled()

```c
bool OH_ArkUI_ProgressLinearStyleOption_GetScanEffectEnabled(ArkUI_ProgressLinearStyleOption* option)
```

**描述**

获取扫光效果的开关信息。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否开启扫光效果。true：表示开启扫光效果。false：表示关闭扫光效果。默认值：false。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeWidth()

```c
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeWidth(ArkUI_ProgressLinearStyleOption* option)
```

**描述**

获取进度条宽度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 进度条宽度值，单位为vp。 |

### OH\_ArkUI\_ProgressLinearStyleOption\_GetStrokeRadius()

```c
float OH_ArkUI_ProgressLinearStyleOption_GetStrokeRadius(ArkUI_ProgressLinearStyleOption* option)
```

**描述**

获取进度条圆角半径值。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ProgressLinearStyleOption](capi-arkui-nativemodule-arkui-progresslinearstyleoption.md)\* option | 线性进度条样式信息。应通过OH\_ArkUI\_ProgressLinearStyleOption\_Create()创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 进度条圆角半径值，单位为vp。 |
