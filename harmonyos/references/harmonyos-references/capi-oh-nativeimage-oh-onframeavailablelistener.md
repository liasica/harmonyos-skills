---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativeimage-oh-onframeavailablelistener
title: OH_OnFrameAvailableListener
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_OnFrameAvailableListener
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6d41c25c8667c655f87d4290426c0d3560f0225b78fc2f45621a52b50c6d9ce0
---

```c
typedef struct OH_OnFrameAvailableListener {...} OH_OnFrameAvailableListener
```

## 概述

一个OH\_NativeImage的监听者，通过[OH\_NativeImage\_SetOnFrameAvailableListener](capi-native-image-h.md#oh_nativeimage_setonframeavailablelistener)接口注册该监听结构体，当有buffer可获取时，将触发回调给用户。

**起始版本：** 11

**相关模块：** [OH\_NativeImage](capi-oh-nativeimage.md)

**所在头文件：** [native\_image.h](capi-native-image-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void\* context | 用户自定义的上下文信息，会在回调触发时返回给用户。 |
| [OH\_OnFrameAvailable](capi-native-image-h.md#oh_onframeavailable) onFrameAvailable | 有buffer可获取时触发的回调函数。 |

### 成员函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_OnFrameAvailable)(void \*context)](capi-oh-nativeimage-oh-onframeavailablelistener.md#oh_onframeavailable) | OH\_OnFrameAvailable() | 有buffer可获取时触发的回调函数。  **起始版本：** 11  **系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage |

## 成员函数说明

### OH\_OnFrameAvailable()

```c
typedef void (*OH_OnFrameAvailable)(void *context)
```

**描述**

有buffer可获取时触发的回调函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*context | 用户自定义的上下文信息，会在回调触发时返回给用户。 |
