---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-animator-h
title: image_animator.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > image_animator.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1660b916cf1e8f6e369d16298b74bbcdc18c0807b4b24e6bee46a825b3f0b095
---

## 概述

为NativeNode API提供ImageAnimator节点类型定义。

**引用文件：** <arkui/node\_attributes/image\_animator.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md) | ArkUI\_ImageAnimatorFrameInfo | 定义图片动画帧信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_AnimationStatus](capi-image-animator-h.md#arkui_animationstatus) | ArkUI\_AnimationStatus | 定义帧动画的播放状态。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString(char\* src)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_createfromstring) | 使用图片路径创建帧图片信息，图片格式为svg、png和jpg。支持应用沙箱内的相对路径和绝对路径。 |
| [ArkUI\_ImageAnimatorFrameInfo\* OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor(ArkUI\_DrawableDescriptor\* drawable)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_createfromdrawabledescriptor) | 使用DrawableDescriptor对象创建帧图片信息，图片格式为Resource和PixelMap。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_dispose) | 销毁帧图片对象指针。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t width)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_setwidth) | 设置图片宽度。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_getwidth) | 获取图片宽度。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t height)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_setheight) | 设置图片高度。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_getheight) | 获取图片高度。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t top)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_settop) | 设置图片相对于组件左上角的纵向坐标。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_gettop) | 获取图片相对于组件左上角的纵向坐标。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t left)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_setleft) | 设置图片相对于组件左上角的横向坐标。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_getleft) | 获取图片相对于组件左上角的横向坐标。 |
| [void OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo, int32\_t duration)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_setduration) | 设置图片的播放时长。 |
| [int32\_t OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration(ArkUI\_ImageAnimatorFrameInfo\* imageInfo)](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_getduration) | 获取图片的播放时长。 |

## 枚举类型说明

### ArkUI\_AnimationStatus

```c
enum ArkUI_AnimationStatus
```

**描述**

定义帧动画的播放状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_STATUS\_INITIAL = 0 | 动画初始状态。 |
| ARKUI\_ANIMATION\_STATUS\_RUNNING = 1 | 动画处于播放状态。 |
| ARKUI\_ANIMATION\_STATUS\_PAUSED = 2 | 动画处于暂停状态。 |
| ARKUI\_ANIMATION\_STATUS\_STOPPED = 3 | 动画处于停止状态。 |

## 函数说明

### OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromString()

```c
ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromString(char* src)
```

**描述**

使用图片路径创建帧图片信息，图片格式为svg、png和jpg。支持应用沙箱内的相对路径和绝对路径。返回的帧图片对象使用完毕后需调用[OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_dispose)释放，避免内存泄漏。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* src | 图片路径，支持应用沙箱内的相对路径和绝对路径。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* | 帧图片对象指针。使用完毕后需调用[OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_dispose)释放，避免内存泄漏；src为NULL时返回NULL。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_CreateFromDrawableDescriptor()

```c
ArkUI_ImageAnimatorFrameInfo* OH_ArkUI_ImageAnimatorFrameInfo_CreateFromDrawableDescriptor(ArkUI_DrawableDescriptor* drawable)
```

**描述**

使用[ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)对象创建帧图片信息，图片格式为Resource和PixelMap。返回的帧图片对象使用完毕后需调用[OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_dispose)释放，避免内存泄漏。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_DrawableDescriptor](capi-arkui-nativemodule-arkui-drawabledescriptor.md)\* drawable | 使用Resource或PixelMap创建的ArkUI\_DrawableDescriptor对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* | 帧图片对象指针。使用完毕后需调用[OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose](capi-image-animator-h.md#oh_arkui_imageanimatorframeinfo_dispose)释放，避免内存泄漏；drawable为NULL时返回NULL。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_Dispose()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_Dispose(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

销毁帧图片对象指针。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetWidth()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_SetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t width)
```

**描述**

设置图片宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t width | 图片宽度，单位为px，取值范围[0, +∞)。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetWidth()

```c
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetWidth(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

获取图片宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片宽度，单位为px，imageInfo为空指针或该字段未设置时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetHeight()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_SetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t height)
```

**描述**

设置图片高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t height | 图片高度，单位为px，取值范围[0, +∞)。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetHeight()

```c
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetHeight(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

获取图片高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片高度，单位为px，imageInfo为空指针或该字段未设置时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetTop()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_SetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t top)
```

**描述**

设置图片相对于组件左上角的纵向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t top | 图片相对于组件左上角的纵向坐标，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetTop()

```c
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetTop(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

获取图片相对于组件左上角的纵向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片相对于组件左上角的纵向坐标，单位为px，imageInfo为空指针或该字段未设置时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetLeft()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_SetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t left)
```

**描述**

设置图片相对于组件左上角的横向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t left | 图片相对于组件左上角的横向坐标，单位为px。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetLeft()

```c
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetLeft(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

获取图片相对于组件左上角的横向坐标。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片相对于组件左上角的横向坐标，单位为px，imageInfo为空指针或该字段未设置时返回0。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_SetDuration()

```c
void OH_ArkUI_ImageAnimatorFrameInfo_SetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo, int32_t duration)
```

**描述**

设置图片的播放时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |
| int32\_t duration | 图片的播放时长，单位为ms，取值范围[0, +∞)。 |

### OH\_ArkUI\_ImageAnimatorFrameInfo\_GetDuration()

```c
int32_t OH_ArkUI_ImageAnimatorFrameInfo_GetDuration(ArkUI_ImageAnimatorFrameInfo* imageInfo)
```

**描述**

获取图片的播放时长。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImageAnimatorFrameInfo](capi-arkui-nativemodule-arkui-imageanimatorframeinfo.md)\* imageInfo | 帧图片对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 图片的播放时长，单位为ms，imageInfo为空指针或该字段未设置时返回0。 |
