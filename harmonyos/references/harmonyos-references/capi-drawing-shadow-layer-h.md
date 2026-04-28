---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-shadow-layer-h
title: drawing_shadow_layer.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_shadow_layer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ffeb29a28d07f289a566b75cfbc3e07edcb78712930c3ba12d714d12d90f5a85
---

## 概述

PhonePC/2in1TabletTVWearable

声明与绘图模块中的阴影层对象相关的函数。

**引用文件：** <native\_drawing/drawing\_shadow\_layer.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShadowLayer\* OH\_Drawing\_ShadowLayerCreate(float blurRadius, float x, float y, uint32\_t color)](capi-drawing-shadow-layer-h.md#oh_drawing_shadowlayercreate) | 创建一个阴影层对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  blurRadius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_ShadowLayerDestroy(OH\_Drawing\_ShadowLayer\* shadowLayer)](capi-drawing-shadow-layer-h.md#oh_drawing_shadowlayerdestroy) | 销毁阴影层对象，并收回该对象占用的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ShadowLayerCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ShadowLayer* OH_Drawing_ShadowLayerCreate(float blurRadius, float x, float y, uint32_t color)
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

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_ShadowLayerDestroy(OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

销毁阴影层对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md)\* shadowLayer | 表示指向阴影层对象的指针。 |
