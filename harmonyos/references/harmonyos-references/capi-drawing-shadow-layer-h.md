---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shadow-layer-h
title: drawing_shadow_layer.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_shadow_layer.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:31d5a82b6b3e74c99db40d67b4bb3e036d107380373992bdabe8aec19b53ce0e
---

## 概述

声明与绘图模块中的阴影层对象相关的函数。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_shadow\_layer.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShadowLayer\* OH\_Drawing\_ShadowLayerCreate(float blurRadius, float x, float y, uint32\_t color)](capi-drawing-shadow-layer-h.md#oh_drawing_shadowlayercreate) | 创建一个阴影层对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  blurRadius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_ShadowLayerDestroy(OH\_Drawing\_ShadowLayer\* shadowLayer)](capi-drawing-shadow-layer-h.md#oh_drawing_shadowlayerdestroy) | 销毁阴影层对象，并收回该对象占用的内存。 |

## 函数说明

### OH\_Drawing\_ShadowLayerCreate()

```c
OH_Drawing_ShadowLayer* OH_Drawing_ShadowLayerCreate(float blurRadius, float x, float y, uint32_t color)
```

**描述**

创建一个阴影层对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

blurRadius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| float blurRadius | 表示阴影的半径，必须大于零。 |
| float x | 表示x轴上的偏移点。 |
| float y | 表示y轴上的偏移点。 |
| uint32\_t color | 表示阴影的颜色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)\* | 返回创建的阴影层对象的指针。 |

### OH\_Drawing\_ShadowLayerDestroy()

```c
void OH_Drawing_ShadowLayerDestroy(OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

销毁阴影层对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)\* shadowLayer | 表示指向阴影层对象的指针。 |
