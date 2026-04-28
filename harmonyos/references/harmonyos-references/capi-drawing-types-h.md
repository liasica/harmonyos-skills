---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h
title: drawing_types.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ed248f8c5e9f6a83b21584c10082fe77cb7ab71f4100ddc3498b7e8fe280175
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了用于绘制2d图形的数据类型，包括画布、画笔、画刷、位图和路径。

**引用文件：** <native\_drawing/drawing\_types.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md) | OH\_Drawing\_Point2D | 定义一个二维的坐标点。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md) | OH\_Drawing\_Corner\_Radii | 定义一个圆角半径，该圆角半径由x轴方向和y轴方向上的半径组成。 |
| [OH\_Drawing\_Point3D](capi-drawing-oh-drawing-point3d.md) | OH\_Drawing\_Point3D | 定义一个三维的坐标点。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md) | OH\_Drawing\_Image\_Info | 定义图片信息结构体。 |
| [OH\_Drawing\_RectStyle\_Info](capi-drawing-oh-drawing-rectstyle-info.md) | OH\_Drawing\_RectStyle\_Info | 定义矩形框样式结构体。 |
| [OH\_Drawing\_String](capi-drawing-oh-drawing-string.md) | OH\_Drawing\_String | 采用UTF-16编码的字符串信息结构体。 |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md) | OH\_Drawing\_Canvas | 定义为一块矩形的画布，可以结合画笔和画刷在上面绘制各种形状、图片和文字。 |
| [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md) | OH\_Drawing\_Pen | 定义为画笔，画笔用于描述绘制图形轮廓的样式和颜色。 |
| [OH\_Drawing\_Region](capi-drawing-oh-drawing-region.md) | OH\_Drawing\_Region | 定义一个区域，用于表示画布上的封闭区域，实现更精确的图形控制。 |
| [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md) | OH\_Drawing\_Brush | 定义为画刷，画刷用于描述填充图形的样式和颜色。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md) | OH\_Drawing\_Path | 定义为路径，路径用于自定义各种形状。 |
| [OH\_Drawing\_PathIterator](capi-drawing-oh-drawing-pathiterator.md) | OH\_Drawing\_PathIterator | 定义为路径操作迭代器，可通过遍历迭代器读取path的操作指令。 |
| [OH\_Drawing\_Lattice](capi-drawing-oh-drawing-lattice.md) | OH\_Drawing\_Lattice | 定义为矩形网格，用于将图片按照矩形网格进行划分。 |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md) | OH\_Drawing\_Bitmap | 定义为位图，位图是一块内存，内存中包含了描述一张图片的像素数据。 |
| [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md) | OH\_Drawing\_Point | 定义一个点，用于描述坐标点。 |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md) | OH\_Drawing\_PixelMap | 定义像素图，用于包装图像框架支持的真实像素图。 |
| [OH\_Drawing\_ColorSpace](capi-drawing-oh-drawing-colorspace.md) | OH\_Drawing\_ColorSpace | 定义色彩空间，用于解释颜色信息。 |
| [OH\_Drawing\_PathEffect](capi-drawing-oh-drawing-patheffect.md) | OH\_Drawing\_PathEffect | 定义一个路径效果，用于影响描边路径。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md) | OH\_Drawing\_Rect | 用于描述矩形。 |
| [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md) | OH\_Drawing\_RoundRect | 用于描述圆角矩形。 |
| [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md) | OH\_Drawing\_Matrix | 定义一个矩阵，用于描述坐标变换。 |
| [OH\_Drawing\_ShaderEffect](capi-drawing-oh-drawing-shadereffect.md) | OH\_Drawing\_ShaderEffect | 定义一个着色器，用于描述绘制内容的源颜色。 |
| [OH\_Drawing\_ShadowLayer](capi-drawing-oh-drawing-shadowlayer.md) | OH\_Drawing\_ShadowLayer | 定义一个阴影层，用于描述绘制内容的阴影层。 |
| [OH\_Drawing\_Filter](capi-drawing-oh-drawing-filter.md) | OH\_Drawing\_Filter | 定义一个滤波器，用于存储颜色滤波器，蒙版滤波器和图像滤波器。 |
| [OH\_Drawing\_MaskFilter](capi-drawing-oh-drawing-maskfilter.md) | OH\_Drawing\_MaskFilter | 定义蒙版滤波器。 |
| [OH\_Drawing\_ColorFilter](capi-drawing-oh-drawing-colorfilter.md) | OH\_Drawing\_ColorFilter | 定义颜色滤波器，传入一个颜色并返回一个新的颜色。 |
| [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md) | OH\_Drawing\_Font | 用于描述字体。 |
| [OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md) | OH\_Drawing\_FontFeatures | 用于描述字体特征容器。字体特征是字体内置的排版规则，控制字形显示。例如：连字、替代字形、上下标等。 |
| [OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md) | OH\_Drawing\_MemoryStream | 用于描述内存流。 |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md) | OH\_Drawing\_FontArguments | 用于描述字型参数。 |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md) | OH\_Drawing\_Typeface | 用于描述字形。 |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md) | OH\_Drawing\_TextBlob | 定义一个文本对象，表示将多个文本组合到一个不可变的容器中。每个文本行由字形和位置组成。 |
| [OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md) | OH\_Drawing\_Image | 定义一个用于描述绘制二维像素数组的图片。 |
| [OH\_Drawing\_ImageFilter](capi-drawing-oh-drawing-imagefilter.md) | OH\_Drawing\_ImageFilter | 定义图像滤波器, 用于对构成图像像素的所有颜色位进行操作。 |
| [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md) | OH\_Drawing\_SamplingOptions | 定义一个采样选项，用于描述图片、位图等图像的采样方法。 |
| [OH\_Drawing\_TextBlobBuilder](capi-drawing-oh-drawing-textblobbuilder.md) | OH\_Drawing\_TextBlobBuilder | 定义文本构建器，用于构建文本。 |
| [OH\_Drawing\_GpuContext](capi-drawing-oh-drawing-gpucontext.md) | OH\_Drawing\_GpuContext | 定义图形处理器上下文，用于描述图形处理器后端上下文。 |
| [OH\_Drawing\_Surface](capi-drawing-oh-drawing-surface.md) | OH\_Drawing\_Surface | 定义surface，用于管理画布绘制的内容。 |
| [OH\_Drawing\_FontMgr](capi-drawing-oh-drawing-fontmgr.md) | OH\_Drawing\_FontMgr | 定义字体管理类, 用于字体管理。 |
| [OH\_Drawing\_FontStyleSet](capi-drawing-oh-drawing-fontstyleset.md) | OH\_Drawing\_FontStyleSet | 定义字体样式集, 用于字体样式族匹配。 |
| [OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md) | OH\_Drawing\_RecordCmdUtils | 定义指令录制工具，用于生成录制指令。 |
| [OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md) | OH\_Drawing\_RecordCmd | 定义录制指令类, 用于存储录制指令的集合。 |
| [OH\_Drawing\_Array](capi-drawing-oh-drawing-array.md) | OH\_Drawing\_Array | 定义数组对象, 用于存储多个同类型对象。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_ColorFormat](capi-drawing-types-h.md#oh_drawing_colorformat) | OH\_Drawing\_ColorFormat | 用于描述位图像素的存储格式。 |
| [OH\_Drawing\_AlphaFormat](capi-drawing-types-h.md#oh_drawing_alphaformat) | OH\_Drawing\_AlphaFormat | 用于描述位图像素的透明度分量。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) | OH\_Drawing\_BlendMode | 混合模式枚举。混合模式的操作会为两种颜色（源色、目标色）生成一种新的颜色。  这些操作在红、绿、蓝3个颜色通道上是相同的（透明度有另外的处理规则）。  对于这些，我们使用透明度通道作为示例，而不是单独命名每个通道。为简洁起见，我们使用以下缩写：  s : source，源的缩写。  d : destination，目标的缩写。  sa : source alpha，源透明度的缩写。  da : destination alpha，目标透明度的缩写。  计算结果用如下缩写表示：  r : 如果4个通道的计算方式相同，用r表示。  ra : 如果只操作透明度通道，用ra表示。  rc : 如果操作3个颜色通道，用rc表示。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) | OH\_Drawing\_TextEncoding | 文本编码类型枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ColorFormat

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_ColorFormat
```

**描述**

用于描述位图像素的存储格式。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| COLOR\_FORMAT\_UNKNOWN | 未知格式。 |
| COLOR\_FORMAT\_ALPHA\_8 | 每个像素用一个8位的量表示，8个比特位表示透明度。 |
| COLOR\_FORMAT\_RGB\_565 | 每个像素用一个16位的量表示，高位到低位依次是5个比特位表示红，6个比特位表示绿，5个比特位表示蓝。 |
| COLOR\_FORMAT\_ARGB\_4444 | 每个像素用一个16位的量表示，高位到低位依次是4个比特位表示透明度，4个比特位表示红，4个比特位表示绿，4个比特位表示蓝。 |
| COLOR\_FORMAT\_RGBA\_8888 | 每个像素用一个32位的量表示，高位到低位依次是8个比特位表示透明度，8个比特位表示红，8个比特位表示绿，8个比特位表示蓝。 |
| COLOR\_FORMAT\_BGRA\_8888 | 每个像素用一个32位的量表示，高位到低位依次是8个比特位表示蓝，8个比特位表示绿，8个比特位表示红，8个比特位表示透明度。 |

### OH\_Drawing\_AlphaFormat

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_AlphaFormat
```

**描述**

用于描述位图像素的透明度分量。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| ALPHA\_FORMAT\_UNKNOWN | 未知格式。 |
| ALPHA\_FORMAT\_OPAQUE | 位图无透明度。 |
| ALPHA\_FORMAT\_PREMUL | 每个像素的颜色组件由透明度分量预先乘以。 |
| ALPHA\_FORMAT\_UNPREMUL | 每个像素的颜色组件未由透明度分量预先乘以。 |

### OH\_Drawing\_BlendMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_BlendMode
```

**描述**

混合模式枚举。混合模式的操作会为两种颜色（源色、目标色）生成一种新的颜色。

这些操作在红、绿、蓝3个颜色通道上是相同的（透明度有另外的处理规则）。

对于这些，我们使用透明度通道作为示例，而不是单独命名每个通道。为简洁起见，我们使用以下缩写：

s : source，源的缩写。

d : destination，目标的缩写。

sa : source alpha，源透明度的缩写。

da : destination alpha，目标透明度的缩写。

计算结果用如下缩写表示：

r : 如果4个通道的计算方式相同，用r表示。

ra : 如果只操作透明度通道，用ra表示。

rc : 如果操作3个颜色通道，用rc表示。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| BLEND\_MODE\_CLEAR | 清除模式，r = 0。 |
| BLEND\_MODE\_SRC | r = s（result的4个通道，都等于source的4个通道，即结果等于源。） |
| BLEND\_MODE\_DST | r = d（result的4个通道，都等于destination的4个通道，即结果等于目标。） |
| BLEND\_MODE\_SRC\_OVER | r = s + (1 - sa) \* d。 |
| BLEND\_MODE\_DST\_OVER | r = d + (1 - da) \* s。 |
| BLEND\_MODE\_SRC\_IN | r = s \* da。 |
| BLEND\_MODE\_DST\_IN | r = d \* sa。 |
| BLEND\_MODE\_SRC\_OUT | r = s \* (1 - da)。 |
| BLEND\_MODE\_DST\_OUT | r = d \* (1 - sa)。 |
| BLEND\_MODE\_SRC\_ATOP | r = s \* da + d \* (1 - sa)。 |
| BLEND\_MODE\_DST\_ATOP | r = d \* sa + s \* (1 - da)。 |
| BLEND\_MODE\_XOR | r = s \* (1 - da) + d \* (1 - sa)。 |
| BLEND\_MODE\_PLUS | r = min(s + d, 1)。 |
| BLEND\_MODE\_MODULATE | r = s \* d。 |
| BLEND\_MODE\_SCREEN | 滤色模式，r = s + d - s \* d。 |
| BLEND\_MODE\_OVERLAY | 叠加模式。 |
| BLEND\_MODE\_DARKEN | 变暗模式，rc = s + d - max(s \* da, d \* sa), ra = s + (1 - sa) \* d。 |
| BLEND\_MODE\_LIGHTEN | 变亮模式，rc = s + d - min(s \* da, d \* sa), ra = s + (1 - sa) \* d。 |
| BLEND\_MODE\_COLOR\_DODGE | 颜色减淡模式。 |
| BLEND\_MODE\_COLOR\_BURN | 颜色加深模式。 |
| BLEND\_MODE\_HARD\_LIGHT | 强光模式。 |
| BLEND\_MODE\_SOFT\_LIGHT | 柔光模式。 |
| BLEND\_MODE\_DIFFERENCE | 差值模式，rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = s + (1 - sa) \* d。 |
| BLEND\_MODE\_EXCLUSION | 排除模式，rc = s + d - two(s \* d), ra = s + (1 - sa) \* d。 |
| BLEND\_MODE\_MULTIPLY | 正片叠底，r = s \* (1 - da) + d \* (1 - sa) + s \* d。 |
| BLEND\_MODE\_HUE | 色相模式。 |
| BLEND\_MODE\_SATURATION | 饱和度模式。 |
| BLEND\_MODE\_COLOR | 颜色模式。 |
| BLEND\_MODE\_LUMINOSITY | 亮度模式。 |

### OH\_Drawing\_TextEncoding

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_TextEncoding
```

**描述**

文本编码类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TEXT\_ENCODING\_UTF8 | 单字节，表示UTF-8或ASCII。 |
| TEXT\_ENCODING\_UTF16 | 双字节，表示大部分Unicode。 |
| TEXT\_ENCODING\_UTF32 | 四字节，表示所有Unicode。 |
| TEXT\_ENCODING\_GLYPH\_ID | 双字节，表示字形索引。 |
