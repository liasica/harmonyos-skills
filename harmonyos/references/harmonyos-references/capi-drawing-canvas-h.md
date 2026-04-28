---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-canvas-h
title: drawing_canvas.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_canvas.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca05e7898571566999c6d3d624f32e9cf4b34d5d5ddfceab07f0ab89c5cb67ff
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与画布相关的功能函数。

画布自带一个黑色，开启抗锯齿，不具备其他任何样式的默认画刷，当且仅当画布中主动设置的画刷和画笔都不存在时生效。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_canvas.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_SrcRectConstraint](capi-drawing-canvas-h.md#oh_drawing_srcrectconstraint) | OH\_Drawing\_SrcRectConstraint | 源矩形区域约束类型枚举。 |
| [OH\_Drawing\_PointMode](capi-drawing-canvas-h.md#oh_drawing_pointmode) | OH\_Drawing\_PointMode | 绘制多个点的方式枚举，方式分为离散点、直线或开放多边形。 |
| [OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop) | OH\_Drawing\_CanvasClipOp | 画布裁剪方式的枚举集合。 |
| [OH\_Drawing\_CanvasShadowFlags](capi-drawing-canvas-h.md#oh_drawing_canvasshadowflags) | OH\_Drawing\_CanvasShadowFlags | 阴影标志枚举。 |
| [OH\_Drawing\_VertexMode](capi-drawing-canvas-h.md#oh_drawing_vertexmode) | OH\_Drawing\_VertexMode | 用于指定如何解释给定顶点的几何形状的枚举类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreate(void)](capi-drawing-canvas-h.md#oh_drawing_canvascreate) | 用于创建一个画布对象。 |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreateWithPixelMap(OH\_Drawing\_PixelMap\* pixelMap)](capi-drawing-canvas-h.md#oh_drawing_canvascreatewithpixelmap) | 用于将一个像素图对象绑定到画布中，使得画布绘制的内容输出到像素图中（即CPU渲染）。绑定像素图对象后的画布为非录制类型画布。  像素图对象应该在销毁画布对象之后调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除绑定。 |
| [void OH\_Drawing\_CanvasDestroy(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasdestroy) | 用于销毁画布对象并回收该对象占有的内存。 |
| [void OH\_Drawing\_CanvasBind(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-canvas-h.md#oh_drawing_canvasbind) | 用于将一个位图对象绑定到画布中，使得画布绘制的内容输出到位图中（即CPU渲染）。绑定位图对象后的画布为非录制类型画布。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasAttachPen(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Pen\* pen)](capi-drawing-canvas-h.md#oh_drawing_canvasattachpen) | 用于设置画笔给画布，画布将会使用设置画笔的样式和颜色去绘制图形形状的轮廓。执行该方法后，若画笔的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、pen任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDetachPen(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasdetachpen) | 用于去除掉画布中的画笔，使用后画布将不去绘制图形形状的轮廓。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasAttachBrush(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)](capi-drawing-canvas-h.md#oh_drawing_canvasattachbrush) | 用于设置画刷给画布，画布将会使用设置的画刷样式和颜色去填充绘制的图形形状。执行该方法后，若画刷的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、brush任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDetachBrush(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasdetachbrush) | 用于去除掉画布中的画刷，使用后画布将不使用此前设置的画刷去填充图形形状。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasSave(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvassave) | 用于保存当前画布的状态（画布矩阵）到一个栈顶。需要与恢复接口[OH\_Drawing\_CanvasRestore](capi-drawing-canvas-h.md#oh_drawing_canvasrestore)配合使用。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasSaveLayer(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect, const OH\_Drawing\_Brush\* brush)](capi-drawing-canvas-h.md#oh_drawing_canvassavelayer) | 保存矩阵和裁剪区域，为后续绘制分配位图。调用恢复接口。  [OH\_Drawing\_CanvasRestore](capi-drawing-canvas-h.md#oh_drawing_canvasrestore)将放弃对矩阵和剪切区域所做的更改，并绘制位图。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasRestore(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasrestore) | 用于恢复保存在栈顶的画布状态（画布矩阵）。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_CanvasGetSaveCount(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasgetsavecount) | 用于获取栈中保存的画布状态（画布矩阵）的数量。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasRestoreToCount(OH\_Drawing\_Canvas\* canvas, uint32\_t saveCount)](capi-drawing-canvas-h.md#oh_drawing_canvasrestoretocount) | 用于恢复到指定数量的画布状态（画布矩阵）。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawLine(OH\_Drawing\_Canvas\* canvas, float x1, float y1, float x2, float y2)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawline) | 用于画一条直线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpath) | 用于画一个自定义路径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapNine(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* center, const OH\_Drawing\_Rect\* dst, OH\_Drawing\_FilterMode mode)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpixelmapnine) | 通过绘制两条水平线和两条垂直线将像素图分割成9个部分：四个边，四个角和中心。  若角落的4个区域尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形。  如果还有剩余空间，剩下的5个区域会通过拉伸或压缩来绘制，以便能够完全覆盖目标矩形。 |
| [void OH\_Drawing\_CanvasDrawPixelMapRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PixelMap\* pixelMap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpixelmaprect) | 用于将像素图的指定区域绘制到画布的指定区域。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、pixelMap、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawBackground(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Brush\* brush)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawbackground) | 用于画一个背景，此背景以画刷填充。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、brush任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawregion) | 用于画一块区域。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、region任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPoint(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point2D\* point)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpoint) | 用于画一个点。 |
| [void OH\_Drawing\_CanvasDrawPoints(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_PointMode mode,uint32\_t count, const OH\_Drawing\_Point2D\* point2D)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpoints) | 用于画多个点，绘制方式分为绘制单独的点、绘制成线段或绘制成开放多边形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、point2D任意一个为NULL或者count等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；mode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_CanvasDrawBitmap(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap, float left, float top)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawbitmap) | 用于画一个位图，位图又称为点阵图像、像素图或栅格图像，是由像素（图片元素）的单个点组成。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawBitmapRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Bitmap\* bitmap,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawbitmaprect) | 将位图的指定区域绘制到画布的指定区域。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、bitmap、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawrect) | 用于画一个矩形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、OH\_Drawing\_Rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawCircle(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Point\* point, float radius)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawcircle) | 用于画一个圆形。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、point任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  radius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawColor(OH\_Drawing\_Canvas\* canvas, uint32\_t color,OH\_Drawing\_BlendMode blendMode)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawcolor) | 用于使用指定的颜色及混合模式来填充整个画布。 |
| [void OH\_Drawing\_CanvasDrawOval(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawoval) | 用于画一个椭圆。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawArc(OH\_Drawing\_Canvas\* canvas,const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawarc) | 用于画一个弧。当扫描角度的绝对值大于360度时，本接口绘制的是一个椭圆。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawArcWithCenter(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,float startAngle, float sweepAngle, bool useCenter)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawarcwithcenter) | 绘制一段圆弧。该方法允许指定圆弧的起始角度、扫描角度以及圆弧的起点和终点是否连接圆弧的中心点。 |
| [void OH\_Drawing\_CanvasDrawRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawroundrect) | 用于画一个圆角矩形。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawNestedRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* outer,const OH\_Drawing\_RoundRect\* inner)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawnestedroundrect) | 绘制两个嵌套的圆角矩形，外部矩形边界必须包含内部矩形边界，否则无绘制效果。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacter(OH\_Drawing\_Canvas\* canvas, const char\* str,const OH\_Drawing\_Font\* font, float x, float y)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawsinglecharacter) | 用于绘制单个字符。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。 |
| [void OH\_Drawing\_CanvasDrawTextBlob(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_TextBlob\* textBlob, float x, float y)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawtextblob) | 用于画一段文字。若构造OH\_Drawing\_TextBlob的字体不支持待绘制字符，则该部分字符无法绘制。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、textBlob任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasClipRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](capi-drawing-canvas-h.md#oh_drawing_canvascliprect) | 用于裁剪一个矩形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_CanvasClipRoundRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_RoundRect\* roundRect,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](capi-drawing-canvas-h.md#oh_drawing_canvascliproundrect) | 用于裁剪一个圆角矩形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_CanvasClipPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,OH\_Drawing\_CanvasClipOp clipOp, bool doAntiAlias)](capi-drawing-canvas-h.md#oh_drawing_canvasclippath) | 用于裁剪一个自定义路径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasClipRegion(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Region\* region,OH\_Drawing\_CanvasClipOp clipOp)](capi-drawing-canvas-h.md#oh_drawing_canvasclipregion) | 用于裁剪一个区域。 |
| [void OH\_Drawing\_CanvasRotate(OH\_Drawing\_Canvas\* canvas, float degrees, float px, float py)](capi-drawing-canvas-h.md#oh_drawing_canvasrotate) | 用于画布旋转一定的角度，正数表示顺时针旋转，负数反之。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasTranslate(OH\_Drawing\_Canvas\* canvas, float dx, float dy)](capi-drawing-canvas-h.md#oh_drawing_canvastranslate) | 用于平移画布一段距离。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasScale(OH\_Drawing\_Canvas\* canvas, float sx, float sy)](capi-drawing-canvas-h.md#oh_drawing_canvasscale) | 用于画布缩放。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasSkew(OH\_Drawing\_Canvas\* canvas, float sx, float sy)](capi-drawing-canvas-h.md#oh_drawing_canvasskew) | 用于画布倾斜变换。等同于将当前画布矩阵左乘（premultiply）倾斜变换矩阵，并应用到画布上。其中倾斜变换矩阵为：  |1 sx 0|  |sy 1 0|  |0 0 1|。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [int32\_t OH\_Drawing\_CanvasGetWidth(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasgetwidth) | 获取画布宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [int32\_t OH\_Drawing\_CanvasGetHeight(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasgetheight) | 获取画布高度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasGetLocalClipBounds(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Rect\* rect)](capi-drawing-canvas-h.md#oh_drawing_canvasgetlocalclipbounds) | 获取画布裁剪区域的边界。该接口不可用于录制类型画布。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasGetTotalMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](capi-drawing-canvas-h.md#oh_drawing_canvasgettotalmatrix) | 获取画布3x3矩阵。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasConcatMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](capi-drawing-canvas-h.md#oh_drawing_canvasconcatmatrix) | 画布现有矩阵左乘以传入矩阵，不影响该接口之前的绘制操作。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawShadow(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Path\* path, OH\_Drawing\_Point3D planeParams,OH\_Drawing\_Point3D devLightPos, float lightRadius, uint32\_t ambientColor, uint32\_t spotColor,OH\_Drawing\_CanvasShadowFlags flag)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawshadow) | 绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  flag不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_CanvasClear(OH\_Drawing\_Canvas\* canvas, uint32\_t color)](capi-drawing-canvas-h.md#oh_drawing_canvasclear) | 用于使用指定颜色去清空画布。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasSetMatrix(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Matrix\* matrix)](capi-drawing-canvas-h.md#oh_drawing_canvassetmatrix) | 设置画布的矩阵状态。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasResetMatrix(OH\_Drawing\_Canvas\* canvas)](capi-drawing-canvas-h.md#oh_drawing_canvasresetmatrix) | 重置当前画布的矩阵为单位矩阵。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawImageRectWithSrc(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Image\* image,const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst, const OH\_Drawing\_SamplingOptions\* samplingOptions,OH\_Drawing\_SrcRectConstraint srcRectConstraint)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawimagerectwithsrc) | 将图片绘制到画布的指定区域上，源矩形选定的区域会缩放平移到目标矩形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、image、src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawImageRect(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\* image,OH\_Drawing\_Rect\* rect, OH\_Drawing\_SamplingOptions\* samplingOptions)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawimagerect) | 将图片绘制到画布的指定区域上。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、image、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_CanvasDrawVertices(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_VertexMode vertexMmode,int32\_t vertexCount, const OH\_Drawing\_Point2D\* positions, const OH\_Drawing\_Point2D\* texs,const uint32\_t\* colors, int32\_t indexCount, const uint16\_t\* indices, OH\_Drawing\_BlendMode mode)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawvertices) | 用于画顶点数组描述的三角网格。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas或positions为NULL、vertexCount值小于3、indexCount值小于3且不为0，存在以上任意一种情况时设置错误码为OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  vertexMmode、mode任意一个不在枚举范围内时设置错误码为OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [bool OH\_Drawing\_CanvasReadPixels(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo,void\* dstPixels, uint32\_t dstRowBytes, int32\_t srcX, int32\_t srcY)](capi-drawing-canvas-h.md#oh_drawing_canvasreadpixels) | 从画布中拷贝像素数据到指定地址。该接口不可用于录制类型画布。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、imageInfo、dstPixels任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_CanvasReadPixelsToBitmap(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_Bitmap\* bitmap, int32\_t srcX, int32\_t srcY)](capi-drawing-canvas-h.md#oh_drawing_canvasreadpixelstobitmap) | 从画布拷贝像素数据到位图中。该接口不可用于录制类型画布。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasIsClipEmpty(OH\_Drawing\_Canvas\* canvas, bool\* isClipEmpty)](capi-drawing-canvas-h.md#oh_drawing_canvasisclipempty) | 用于判断裁剪后可绘制区域是否为空。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasGetImageInfo(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_Image\_Info\* imageInfo)](capi-drawing-canvas-h.md#oh_drawing_canvasgetimageinfo) | 用于获取画布的图像信息。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmd(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawrecordcmd) | 用于绘制录制指令对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawRecordCmdNesting(OH\_Drawing\_Canvas\* canvas, OH\_Drawing\_RecordCmd\* recordCmd)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawrecordcmdnesting) | 用于绘制录制指令对象，支持嵌套。  本接口支持[OH\_Drawing\_RecordCmdUtilsBeginRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsbeginrecording)接口生成的画布对象作为入参，嵌套调用。不建议多层嵌套，会影响性能。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectPath(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Path\* path,bool\* quickReject)](capi-drawing-canvas-h.md#oh_drawing_canvasquickrejectpath) | 判断路径与画布区域是否不相交。画布区域包含边界。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasQuickRejectRect(OH\_Drawing\_Canvas\* canvas, const OH\_Drawing\_Rect\* rect,bool\* quickReject)](capi-drawing-canvas-h.md#oh_drawing_canvasquickrejectrect) | 判断矩形和画布区域是否不相交。画布区域包含边界。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapRectConstraint(OH\_Drawing\_Canvas\* canvas,OH\_Drawing\_PixelMap\* pixelMap, const OH\_Drawing\_Rect\* src, const OH\_Drawing\_Rect\* dst,const OH\_Drawing\_SamplingOptions\* samplingOptions, OH\_Drawing\_SrcRectConstraint constraint)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpixelmaprectconstraint) | 用于将像素图的指定区域绘制到画布的指定区域。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures(OH\_Drawing\_Canvas\* canvas, const char\* str,const OH\_Drawing\_Font\* font, float x, float y, OH\_Drawing\_FontFeatures\* fontFeatures)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawsinglecharacterwithfeatures) | 绘制单个字符，字符带有字体特征。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_CanvasDrawPixelMapMesh(OH\_Drawing\_Canvas\* cCanvas, OH\_Drawing\_PixelMap\* pixelMap, uint32\_t meshWidth, uint32\_t meshHeight, const float\* vertices, uint32\_t verticesSize, uint32\_t vertOffset, const uint32\_t\* colors, uint32\_t colorsSize, uint32\_t colorOffset)](capi-drawing-canvas-h.md#oh_drawing_canvasdrawpixelmapmesh) | 在网格上绘制像素图，网格均匀分布在像素图上。（只支持brush，使用pen没有绘制效果。） |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_SrcRectConstraint

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_SrcRectConstraint
```

**描述**

源矩形区域约束类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| STRICT\_SRC\_RECT\_CONSTRAINT | 严格约束，源矩形区域必须完全包含在图像中。 |
| FAST\_SRC\_RECT\_CONSTRAINT | 快速约束，源矩形区域可以部分位于图像之外。 |

### OH\_Drawing\_PointMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PointMode
```

**描述**

绘制多个点的方式枚举，方式分为离散点、直线或开放多边形。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| POINT\_MODE\_POINTS | 分别绘制每个点。 |
| POINT\_MODE\_LINES | 将每两个点绘制为线段。 |
| POINT\_MODE\_POLYGON | 将点阵列绘制为开放多边形。 |

### OH\_Drawing\_CanvasClipOp

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_CanvasClipOp
```

**描述**

画布裁剪方式的枚举集合。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| DIFFERENCE | 将指定区域裁剪（取差集）。 |
| INTERSECT | 将指定区域保留（取交集）。 |

### OH\_Drawing\_CanvasShadowFlags

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_CanvasShadowFlags
```

**描述**

阴影标志枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SHADOW\_FLAGS\_NONE | 无阴影标志。 |
| SHADOW\_FLAGS\_TRANSPARENT\_OCCLUDER | 遮挡物对象不透明标志。 |
| SHADOW\_FLAGS\_GEOMETRIC\_ONLY | 不分析阴影标志。 |
| SHADOW\_FLAGS\_ALL | 使能以上所有阴影标志。 |

### OH\_Drawing\_VertexMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_VertexMode
```

**描述**

用于指定如何解释给定顶点的几何形状的枚举类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| VERTEX\_MODE\_TRIANGLES | 每三个顶点表示一个三角形，如果顶点数不是3的倍数，则多余的顶点会被忽略。 |
| VERTEX\_MODE\_TRIANGLES\_STRIP | 相邻三个顶点表示一个三角形，每个新的顶点将与前两个顶点组成一个新的三角形。 |
| VERTEX\_MODE\_TRIANGLE\_FAN | 第一个顶点作为中心点，后续的每个顶点都与前一个顶点和中心点组成一个三角形。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_CanvasDrawSingleCharacterWithFeatures()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawSingleCharacterWithFeatures(OH_Drawing_Canvas* canvas, const char* str, const OH_Drawing_Font* font, float x, float y, OH_Drawing_FontFeatures* fontFeatures)
```

**描述**

绘制单个字符，字符带有字体特征。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const char\* str | 待绘制的单个字符。可以传入字符串，但只会以UTF-8编码解析并绘制字符串中的首个字符。 |
| [const OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| float x | 字符对象基线左端点（靠近字符左下角）的横坐标。 |
| float y | 字符对象基线左端点（靠近字符左下角）的纵坐标。 |
| [OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)\* fontFeatures | 指向字体特征容器对象[OH\_Drawing\_FontFeatures](capi-drawing-oh-drawing-fontfeatures.md)的指针。容器中未加入任何字体特征时使用TTF(TrueType Font)文件中预设的字体特征。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、str、font或者fontFeatures任意一个为NULL或者str的长度为0。 |

### OH\_Drawing\_CanvasDrawPixelMapRectConstraint()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawPixelMapRectConstraint(OH_Drawing_Canvas* canvas,OH_Drawing_PixelMap* pixelMap, const OH_Drawing_Rect* src, const OH_Drawing_Rect* dst, const OH_Drawing_SamplingOptions* samplingOptions, OH_Drawing_SrcRectConstraint constraint)
```

**描述**

用于将像素图的指定区域绘制到画布的指定区域。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
| [const OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* src | 像素图指定矩形区域，为NULL将指定整个像素图区域。 |
| [const OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 目标画布指定矩形区域。 |
| [const OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针，为NULL将使用默认采样选项。 |
| [OH\_Drawing\_SrcRectConstraint](capi-drawing-canvas-h.md#oh_drawing_srcrectconstraint) constraint | 约束类型，支持可选的具体类型可见[OH\_Drawing\_SrcRectConstraint](capi-drawing-canvas-h.md#oh_drawing_srcrectconstraint)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、pixelMap或dst为空。 |

### OH\_Drawing\_CanvasDrawRecordCmdNesting()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawRecordCmdNesting(OH_Drawing_Canvas* canvas, OH_Drawing_RecordCmd* recordCmd)
```

**描述**

用于绘制录制指令对象，支持嵌套。

本接口支持[OH\_Drawing\_RecordCmdUtilsBeginRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsbeginrecording)接口生成的画布对象作为入参，嵌套调用。不建议多层嵌套，会影响性能。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_Drawing\_Canvas\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针，仅支持录制类型画布。 |
| OH\_Drawing\_RecordCmd\* recordCmd | 指向录制指令对象[OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行操作码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者recordCmd为空。 |

### OH\_Drawing\_CanvasCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Canvas* OH_Drawing_CanvasCreate(void)
```

**描述**

用于创建一个画布对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* | 函数会返回一个指针，指针指向创建的画布对象。 |

### OH\_Drawing\_CanvasCreateWithPixelMap()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Canvas* OH_Drawing_CanvasCreateWithPixelMap(OH_Drawing_PixelMap* pixelMap)
```

**描述**

用于将一个像素图对象绑定到画布中，使得画布绘制的内容输出到像素图中（即CPU渲染）。绑定像素图对象后的画布为非录制类型画布。

像素图对象应该在销毁画布对象之后调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除绑定。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* | 函数会返回一个指针，指针指向创建的画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)，如果对象返回为NULL，则创建失败，原因可能是可用内存不足或者像素图对象为空。 |

### OH\_Drawing\_CanvasDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDestroy(OH_Drawing_Canvas* canvas)
```

**描述**

用于销毁画布对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

### OH\_Drawing\_CanvasBind()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasBind(OH_Drawing_Canvas* canvas, OH_Drawing_Bitmap* bitmap)
```

**描述**

用于将一个位图对象绑定到画布中，使得画布绘制的内容输出到位图中（即CPU渲染）。绑定位图对象后的画布为非录制类型画布。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

### OH\_Drawing\_CanvasAttachPen()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasAttachPen(OH_Drawing_Canvas* canvas, const OH_Drawing_Pen* pen)
```

**描述**

用于设置画笔给画布，画布将会使用设置画笔的样式和颜色去绘制图形形状的轮廓。执行该方法后，若画笔的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、pen任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Pen](capi-drawing-oh-drawing-pen.md)\* pen | 指向画笔对象的指针。 |

### OH\_Drawing\_CanvasDetachPen()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDetachPen(OH_Drawing_Canvas* canvas)
```

**描述**

用于去除掉画布中的画笔，使用后画布将不去绘制图形形状的轮廓。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

### OH\_Drawing\_CanvasAttachBrush()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasAttachBrush(OH_Drawing_Canvas* canvas, const OH_Drawing_Brush* brush)
```

**描述**

用于设置画刷给画布，画布将会使用设置的画刷样式和颜色去填充绘制的图形形状。执行该方法后，若画刷的效果发生改变并且开发者希望该变化生效于接下来的绘制动作，需要再次执行该方法以确保变化生效。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、brush任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

### OH\_Drawing\_CanvasDetachBrush()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDetachBrush(OH_Drawing_Canvas* canvas)
```

**描述**

用于去除掉画布中的画刷，使用后画布将不使用此前设置的画刷去填充图形形状。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

### OH\_Drawing\_CanvasSave()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasSave(OH_Drawing_Canvas* canvas)
```

**描述**

用于保存当前画布的状态（画布矩阵）到一个栈顶。需要与恢复接口[OH\_Drawing\_CanvasRestore](capi-drawing-canvas-h.md#oh_drawing_canvasrestore)配合使用。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

### OH\_Drawing\_CanvasSaveLayer()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasSaveLayer(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect, const OH_Drawing_Brush* brush)
```

**描述**

保存矩阵和裁剪区域，为后续绘制分配位图。调用恢复接口。

[OH\_Drawing\_CanvasRestore](capi-drawing-canvas-h.md#oh_drawing_canvasrestore)将放弃对矩阵和剪切区域所做的更改，并绘制位图。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，用于限制图层大小，为NULL表示无限制。 |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象[OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)的指针，绘制位图时会应用画刷对象的透明度，滤波器效果，混合模式，为NULL表示不应用任何效果。 |

### OH\_Drawing\_CanvasRestore()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasRestore(OH_Drawing_Canvas* canvas)
```

**描述**

用于恢复保存在栈顶的画布状态（画布矩阵）。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

### OH\_Drawing\_CanvasGetSaveCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_CanvasGetSaveCount(OH_Drawing_Canvas* canvas)
```

**描述**

用于获取栈中保存的画布状态（画布矩阵）的数量。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数会返回一个32位的值描述画布状态（画布矩阵）的数量，画布初始状态数量为1。 |

### OH\_Drawing\_CanvasRestoreToCount()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasRestoreToCount(OH_Drawing_Canvas* canvas, uint32_t saveCount)
```

**描述**

用于恢复到指定数量的画布状态（画布矩阵）。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| uint32\_t saveCount | 要恢复的画布状态深度。小于等于1时，恢复为初始状态；大于已保存的画布状态数量时，不执行任何操作。 |

### OH\_Drawing\_CanvasDrawLine()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawLine(OH_Drawing_Canvas* canvas, float x1, float y1, float x2, float y2)
```

**描述**

用于画一条直线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| float x1 | 线段起始点的横坐标。 |
| float y1 | 线段起始点的纵坐标。 |
| float x2 | 线段结束点的横坐标。 |
| float y2 | 线段结束点的纵坐标。 |

### OH\_Drawing\_CanvasDrawPath()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawPath(OH_Drawing_Canvas* canvas, const OH_Drawing_Path* path)
```

**描述**

用于画一个自定义路径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |

### OH\_Drawing\_CanvasDrawPixelMapNine()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawPixelMapNine(OH_Drawing_Canvas* canvas, OH_Drawing_PixelMap* pixelMap,const OH_Drawing_Rect* center, const OH_Drawing_Rect* dst, OH_Drawing_FilterMode mode)
```

**描述**

通过绘制两条水平线和两条垂直线将像素图分割成9个部分：四个边，四个角和中心。

若角落的4个区域尺寸不超过目标矩形，则会在不缩放的情况下被绘制在目标矩形，反之则会按比例缩放绘制在目标矩形。

如果还有剩余空间，剩下的5个区域会通过拉伸或压缩来绘制，以便能够完全覆盖目标矩形。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* center | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，表示分割像素图的中心矩形。矩形四条边所在的直线将像素图分成了9个部分。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，表示画布上的目标区域。 |
| [OH\_Drawing\_FilterMode](capi-drawing-sampling-options-h.md#oh_drawing_filtermode) mode | 过滤模式枚举[OH\_Drawing\_FilterMode](capi-drawing-sampling-options-h.md#oh_drawing_filtermode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、pixelMap或dst为空。 |

### OH\_Drawing\_CanvasDrawPixelMapRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawPixelMapRect(OH_Drawing_Canvas* canvas, OH_Drawing_PixelMap* pixelMap,const OH_Drawing_Rect* src, const OH_Drawing_Rect* dst, const OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

用于将像素图的指定区域绘制到画布的指定区域。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、pixelMap、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* src | 像素图指定矩形区域，为NULL将指定整个像素图区域。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 目标画布指定矩形区域。 |
| const [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针，为NULL将使用默认采样选项。 |

### OH\_Drawing\_CanvasDrawBackground()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawBackground(OH_Drawing_Canvas* canvas, const OH_Drawing_Brush* brush)
```

**描述**

用于画一个背景，此背景以画刷填充。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、brush任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Brush](capi-drawing-oh-drawing-brush.md)\* brush | 指向画刷对象的指针。 |

### OH\_Drawing\_CanvasDrawRegion()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawRegion(OH_Drawing_Canvas* canvas, const OH_Drawing_Region* region)
```

**描述**

用于画一块区域。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、region任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Region](capi-drawing-oh-drawing-region.md)\* region | 指向区域对象的指针。 |

### OH\_Drawing\_CanvasDrawPoint()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawPoint(OH_Drawing_Canvas* canvas, const OH_Drawing_Point2D* point)
```

**描述**

用于画一个点。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* point | 指向点对象[OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者point为空。 |

### OH\_Drawing\_CanvasDrawPoints()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawPoints(OH_Drawing_Canvas* canvas, OH_Drawing_PointMode mode,uint32_t count, const OH_Drawing_Point2D* point2D)
```

**描述**

用于画多个点，绘制方式分为绘制单独的点、绘制成线段或绘制成开放多边形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、point2D任意一个为NULL或者count等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；mode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| [OH\_Drawing\_PointMode](capi-drawing-canvas-h.md#oh_drawing_pointmode) mode | 绘制多个点的方式，支持方式参考[OH\_Drawing\_PointMode](capi-drawing-canvas-h.md#oh_drawing_pointmode)。 |
| uint32\_t count | 点的数量，即点数组中点的个数。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* point2D | 指向多个点的数组。 |

### OH\_Drawing\_CanvasDrawBitmap()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawBitmap(OH_Drawing_Canvas* canvas, const OH_Drawing_Bitmap* bitmap, float left, float top)
```

**描述**

用于画一个位图，位图又称为点阵图像、像素图或栅格图像，是由像素（图片元素）的单个点组成。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |
| float left | 位图对象左上角的横坐标。 |
| float top | 位图对象左上角的纵坐标。 |

### OH\_Drawing\_CanvasDrawBitmapRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawBitmapRect(OH_Drawing_Canvas* canvas, const OH_Drawing_Bitmap* bitmap,const OH_Drawing_Rect* src, const OH_Drawing_Rect* dst, const OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

将位图的指定区域绘制到画布的指定区域。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、bitmap、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* src | 源位图指定矩形区域，为NULL将指定整个源位图区域。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 目标画布指定矩形区域。 |
| const [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针，为NULL将使用默认采样选项。 |

### OH\_Drawing\_CanvasDrawRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawRect(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect)
```

**描述**

用于画一个矩形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、OH\_Drawing\_Rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

### OH\_Drawing\_CanvasDrawCircle()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawCircle(OH_Drawing_Canvas* canvas, const OH_Drawing_Point* point, float radius)
```

**描述**

用于画一个圆形。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、point任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

radius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Point](capi-drawing-oh-drawing-point.md)\* point | 指向坐标点对象的指针，表示圆心。 |
| float radius | 圆形的半径，小于等于0时无效。 |

### OH\_Drawing\_CanvasDrawColor()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawColor(OH_Drawing_Canvas* canvas, uint32_t color,OH_Drawing_BlendMode blendMode)
```

**描述**

用于使用指定的颜色及混合模式来填充整个画布。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| uint32\_t color | 表示指定的颜色，用一个32位（ARGB）的变量表示。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) blendMode | 表示指定的混合模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas为空。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示blendMode不在枚举范围内。 |

### OH\_Drawing\_CanvasDrawOval()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawOval(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect)
```

**描述**

用于画一个椭圆。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |

### OH\_Drawing\_CanvasDrawArc()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawArc(OH_Drawing_Canvas* canvas,const OH_Drawing_Rect* rect, float startAngle, float sweepAngle)
```

**描述**

用于画一个弧。当扫描角度的绝对值大于360度时，本接口绘制的是一个椭圆。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| float startAngle | 弧的起始角度，0度时起始点位于椭圆的右端点，正数时以顺时针方向放置起始点，负数时以逆时针方向放置起始点。 |
| float sweepAngle | 弧的扫描角度，正数时顺时针扫描，负数时逆时针扫描。它的有效范围在-360度到360度之间，当绝对值大于360度时，该函数绘制的是一个椭圆。 |

### OH\_Drawing\_CanvasDrawArcWithCenter()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawArcWithCenter(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect,float startAngle, float sweepAngle, bool useCenter)
```

**描述**

绘制一段圆弧。该方法允许指定圆弧的起始角度、扫描角度以及圆弧的起点和终点是否连接圆弧的中心点。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| float startAngle | 弧的起始角度，单位为度，该参数为浮点数。0度时起始点位于椭圆的右端点，为正数时以顺时针方向放置起始点，为负数时以逆时针方向放置起始点。 |
| float sweepAngle | 弧的扫描角度，单位为度，该参数为浮点数。为正数时顺时针扫描，为负数时逆时针扫描。扫描角度可以超过360度，将绘制一个完整的椭圆。 |
| bool useCenter | 表示绘制时弧形的起点和终点是否连接弧形的中心点。true表示连接，false表示不连接。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者rect为空。 |

### OH\_Drawing\_CanvasDrawRoundRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawRoundRect(OH_Drawing_Canvas* canvas, const OH_Drawing_RoundRect* roundRect)
```

**描述**

用于画一个圆角矩形。本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。canvas、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象的指针。 |

### OH\_Drawing\_CanvasDrawNestedRoundRect()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawNestedRoundRect(OH_Drawing_Canvas* canvas, const OH_Drawing_RoundRect* outer,const OH_Drawing_RoundRect* inner)
```

**描述**

绘制两个嵌套的圆角矩形，外部矩形边界必须包含内部矩形边界，否则无绘制效果。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* outer | 指向圆角矩形对象[OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)的指针，表示外部圆角矩形边界。 |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* inner | 指向圆角矩形对象[OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)的指针，表示内部圆角矩形边界。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、outer或者inner为空。 |

### OH\_Drawing\_CanvasDrawSingleCharacter()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawSingleCharacter(OH_Drawing_Canvas* canvas, const char* str,const OH_Drawing_Font* font, float x, float y)
```

**描述**

用于绘制单个字符。当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const char\* str | 待绘制的单个字符。可以传入字符串，但只会以UTF-8编码解析并绘制字符串中的首个字符。 |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字型对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| float x | 字符对象基线左端点（靠近字符左下角）的横坐标。 |
| float y | 字符对象基线左端点（靠近字符左下角）的纵坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、str、font任意一个为NULL或者str的长度为0。 |

### OH\_Drawing\_CanvasDrawTextBlob()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawTextBlob(OH_Drawing_Canvas* canvas, const OH_Drawing_TextBlob* textBlob, float x, float y)
```

**描述**

用于画一段文字。若构造OH\_Drawing\_TextBlob的字体不支持待绘制字符，则该部分字符无法绘制。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、textBlob任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* textBlob | 指向文本对象的指针。 |
| float x | 文本对象基线左端点（靠近文本左下角）的横坐标。 |
| float y | 文本对象基线左端点（靠近文本左下角）的纵坐标。 |

### OH\_Drawing\_CanvasClipRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasClipRect(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect,OH_Drawing_CanvasClipOp clipOp, bool doAntiAlias)
```

**描述**

用于裁剪一个矩形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象的指针。 |
| [OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop) clipOp | 裁剪方式。支持可选的具体裁剪方式可见[OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop)枚举。 |
| bool doAntiAlias | 值为true则做抗锯齿处理，值为false不做抗锯齿处理。 |

### OH\_Drawing\_CanvasClipRoundRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasClipRoundRect(OH_Drawing_Canvas* canvas, const OH_Drawing_RoundRect* roundRect,OH_Drawing_CanvasClipOp clipOp, bool doAntiAlias)
```

**描述**

用于裁剪一个圆角矩形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象的指针。 |
| [OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop) clipOp | 裁剪方式。支持可选的具体裁剪方式可见[OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop)枚举。 |
| bool doAntiAlias | 表示是否需要做抗锯齿处理，值为true时为需要，为false时为不需要。 |

### OH\_Drawing\_CanvasClipPath()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasClipPath(OH_Drawing_Canvas* canvas, const OH_Drawing_Path* path,OH_Drawing_CanvasClipOp clipOp, bool doAntiAlias)
```

**描述**

用于裁剪一个自定义路径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

clipOp不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| [OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop) clipOp | 裁剪方式。支持可选的具体裁剪方式可见[OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop)枚举。 |
| bool doAntiAlias | 真为抗锯齿，假则不做抗锯齿处理。 |

### OH\_Drawing\_CanvasClipRegion()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasClipRegion(OH_Drawing_Canvas* canvas, const OH_Drawing_Region* region,OH_Drawing_CanvasClipOp clipOp)
```

**描述**

用于裁剪一个区域。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Region](capi-drawing-oh-drawing-region.md)\* region | 指向区域对象[OH\_Drawing\_Region](capi-drawing-oh-drawing-region.md)的指针。 |
| [OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop) clipOp | 表示裁剪类型。支持可选的具体裁剪方式可见[OH\_Drawing\_CanvasClipOp](capi-drawing-canvas-h.md#oh_drawing_canvasclipop)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者region为空。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示clipOp不在枚举范围内。 |

### OH\_Drawing\_CanvasRotate()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasRotate(OH_Drawing_Canvas* canvas, float degrees, float px, float py)
```

**描述**

用于画布旋转一定的角度，正数表示顺时针旋转，负数反之。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| float degrees | 旋转角度。 |
| float px | 旋转中心的横坐标。 |
| float py | 旋转中心的纵坐标。 |

### OH\_Drawing\_CanvasTranslate()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasTranslate(OH_Drawing_Canvas* canvas, float dx, float dy)
```

**描述**

用于平移画布一段距离。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| float dx | x轴方向的移动距离。 |
| float dy | y轴方向的移动距离。 |

### OH\_Drawing\_CanvasScale()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasScale(OH_Drawing_Canvas* canvas, float sx, float sy)
```

**描述**

用于画布缩放。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| float sx | x轴方向的缩放比例。 |
| float sy | y轴方向的缩放比例。 |

### OH\_Drawing\_CanvasSkew()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasSkew(OH_Drawing_Canvas* canvas, float sx, float sy)
```

**描述**

用于画布倾斜变换。等同于将当前画布矩阵左乘（premultiply）倾斜变换矩阵，并应用到画布上。其中倾斜变换矩阵为：

|1 sx 0|

|sy 1 0|

|0 0 1|。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| float sx | 沿x轴的倾斜量。正值会使绘制沿y轴增量方向向右倾斜；负值会使绘制沿y轴增量方向向左倾斜。 |
| float sy | 沿y轴的倾斜量。正值会使绘制沿x轴增量方向向下倾斜；负值会使绘制沿x轴增量方向向上倾斜。 |

### OH\_Drawing\_CanvasGetWidth()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Drawing_CanvasGetWidth(OH_Drawing_Canvas* canvas)
```

**描述**

获取画布宽度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 函数返回画布宽度，单位为像素。 |

### OH\_Drawing\_CanvasGetHeight()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Drawing_CanvasGetHeight(OH_Drawing_Canvas* canvas)
```

**描述**

获取画布高度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 函数返回画布高度，单位为像素。 |

### OH\_Drawing\_CanvasGetLocalClipBounds()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasGetLocalClipBounds(OH_Drawing_Canvas* canvas, OH_Drawing_Rect* rect)
```

**描述**

获取画布裁剪区域的边界。该接口不可用于录制类型画布。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，开发者可调用[OH\_Drawing\_RectCreate](capi-drawing-rect-h.md#oh_drawing_rectcreate)接口创建。 |

### OH\_Drawing\_CanvasGetTotalMatrix()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasGetTotalMatrix(OH_Drawing_Canvas* canvas, OH_Drawing_Matrix* matrix)
```

**描述**

获取画布3x3矩阵。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针，开发者可调用[OH\_Drawing\_MatrixCreate](capi-drawing-matrix-h.md#oh_drawing_matrixcreate)接口创建。 |

### OH\_Drawing\_CanvasConcatMatrix()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasConcatMatrix(OH_Drawing_Canvas* canvas, OH_Drawing_Matrix* matrix)
```

**描述**

画布现有矩阵左乘以传入矩阵，不影响该接口之前的绘制操作。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针。 |

### OH\_Drawing\_CanvasDrawShadow()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawShadow(OH_Drawing_Canvas* canvas, OH_Drawing_Path* path, OH_Drawing_Point3D planeParams,OH_Drawing_Point3D devLightPos, float lightRadius, uint32_t ambientColor, uint32_t spotColor,OH_Drawing_CanvasShadowFlags flag)
```

**描述**

绘制射灯类型阴影，使用路径描述环境光阴影的轮廓。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、path任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

flag不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针，用于生成阴影。 |
| [OH\_Drawing\_Point3D](capi-drawing-oh-drawing-point3d.md) planeParams | 表示遮挡物相对于画布在Z轴上的偏移量，其值取决于x与y坐标。 |
| [OH\_Drawing\_Point3D](capi-drawing-oh-drawing-point3d.md) devLightPos | 光线相对于画布的位置。 |
| float lightRadius | 光源半径，需大于或等于0。 |
| uint32\_t ambientColor | 环境阴影颜色，用一个32位（ARGB）的变量表示。 |
| uint32\_t spotColor | 点阴影颜色，用一个32位（ARGB）的变量表示。 |
| [OH\_Drawing\_CanvasShadowFlags](capi-drawing-canvas-h.md#oh_drawing_canvasshadowflags) flag | 阴影标志枚举[OH\_Drawing\_CanvasShadowFlags](capi-drawing-canvas-h.md#oh_drawing_canvasshadowflags)。 |

### OH\_Drawing\_CanvasClear()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasClear(OH_Drawing_Canvas* canvas, uint32_t color)
```

**描述**

用于使用指定颜色去清空画布。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| uint32\_t color | 描述颜色的32位（ARGB）变量。 |

### OH\_Drawing\_CanvasSetMatrix()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasSetMatrix(OH_Drawing_Canvas* canvas, OH_Drawing_Matrix* matrix)
```

**描述**

设置画布的矩阵状态。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针，开发者可调用[OH\_Drawing\_MatrixCreate](capi-drawing-matrix-h.md#oh_drawing_matrixcreate)接口创建。 |

### OH\_Drawing\_CanvasResetMatrix()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasResetMatrix(OH_Drawing_Canvas* canvas)
```

**描述**

重置当前画布的矩阵为单位矩阵。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |

### OH\_Drawing\_CanvasDrawImageRectWithSrc()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawImageRectWithSrc(OH_Drawing_Canvas* canvas, const OH_Drawing_Image* image,const OH_Drawing_Rect* src, const OH_Drawing_Rect* dst, const OH_Drawing_SamplingOptions* samplingOptions,OH_Drawing_SrcRectConstraint srcRectConstraint)
```

**描述**

将图片绘制到画布的指定区域上，源矩形选定的区域会缩放平移到目标矩形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、image、src、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)\* image | 指向图片对象[OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* src | 指向源矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* dst | 指向目标矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| const [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针，为NULL将使用默认采样选项。 |
| [OH\_Drawing\_SrcRectConstraint](capi-drawing-canvas-h.md#oh_drawing_srcrectconstraint) srcRectConstraint | 约束类型，支持可选的具体类型可见[OH\_Drawing\_SrcRectConstraint](capi-drawing-canvas-h.md#oh_drawing_srcrectconstraint)枚举。 |

### OH\_Drawing\_CanvasDrawImageRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawImageRect(OH_Drawing_Canvas* canvas, OH_Drawing_Image* image,OH_Drawing_Rect* rect, OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

将图片绘制到画布的指定区域上。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、image、dst任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)\* image | 指向图片对象[OH\_Drawing\_Image](capi-drawing-oh-drawing-image.md)的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| [OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)\* samplingOptions | 指向采样选项对象[OH\_Drawing\_SamplingOptions](capi-drawing-oh-drawing-samplingoptions.md)的指针，为NULL将使用默认采样选项。 |

### OH\_Drawing\_CanvasDrawVertices()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_CanvasDrawVertices(OH_Drawing_Canvas* canvas, OH_Drawing_VertexMode vertexMmode,int32_t vertexCount, const OH_Drawing_Point2D* positions, const OH_Drawing_Point2D* texs,const uint32_t* colors, int32_t indexCount, const uint16_t* indices, OH_Drawing_BlendMode mode)
```

**描述**

用于画顶点数组描述的三角网格。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas或positions为NULL、vertexCount值小于3、indexCount值小于3且不为0，存在以上任意一种情况时设置错误码为OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

vertexMmode、mode任意一个不在枚举范围内时设置错误码为OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象的指针。 |
| [OH\_Drawing\_VertexMode](capi-drawing-canvas-h.md#oh_drawing_vertexmode) vertexMmode | 绘制顶点的连接方式，支持方式参考[OH\_Drawing\_VertexMode](capi-drawing-canvas-h.md#oh_drawing_vertexmode)。 |
| int32\_t vertexCount | 顶点数组元素的数量，值必须大于等于3。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* positions | 描述顶点位置的数组指针，不能为空，其长度必须等于vertexCount。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* texs | 描述顶点对应纹理空间坐标的数组指针，可以为空，若不为空其长度必须等于vertexCount。 |
| const uint32\_t\* colors | 描述顶点对应颜色的数组指针，用于在三角形中进行插值，可以为空，若不为空其长度必须等于vertexCount。 |
| int32\_t indexCount | 索引的数量，可以为0，若不为0则值必须大于等于3。 |
| const uint16\_t\* indices | 描述顶点对应索引的数组指针，可以为空，若不为空其长度必须等于indexCount。 |
| [OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode) mode | 混合模式枚举，支持方式参考[OH\_Drawing\_BlendMode](capi-drawing-types-h.md#oh_drawing_blendmode)。 |

### OH\_Drawing\_CanvasReadPixels()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_CanvasReadPixels(OH_Drawing_Canvas* canvas, OH_Drawing_Image_Info* imageInfo,void* dstPixels, uint32_t dstRowBytes, int32_t srcX, int32_t srcY)
```

**描述**

从画布中拷贝像素数据到指定地址。该接口不可用于录制类型画布。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、imageInfo、dstPixels任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图片信息[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。 |
| void\* dstPixels | 目标像素存储首地址。 |
| uint32\_t dstRowBytes | 一行像素的大小，小于等于0时无效。 |
| int32\_t srcX | 画布像素的x轴偏移量，单位为像素。 |
| int32\_t srcY | 画布像素的y轴偏移量，单位为像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回true表示像素成功拷贝到目标像素存储首地址，函数返回false表示拷贝失败。 |

### OH\_Drawing\_CanvasReadPixelsToBitmap()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_CanvasReadPixelsToBitmap(OH_Drawing_Canvas* canvas,OH_Drawing_Bitmap* bitmap, int32_t srcX, int32_t srcY)
```

**描述**

从画布拷贝像素数据到位图中。该接口不可用于录制类型画布。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

canvas、bitmap任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)的指针。 |
| int32\_t srcX | 画布像素的x轴偏移量，单位为像素。 |
| int32\_t srcY | 画布像素的y轴偏移量，单位为像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回true表示像素成功拷贝到位图，函数返回false表示拷贝失败。 |

### OH\_Drawing\_CanvasIsClipEmpty()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasIsClipEmpty(OH_Drawing_Canvas* canvas, bool* isClipEmpty)
```

**描述**

用于判断裁剪后可绘制区域是否为空。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| bool\* isClipEmpty | 表示裁剪后可绘制区域是否为空。true表示为空，false表示不为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者isClipEmpty为空。 |

### OH\_Drawing\_CanvasGetImageInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasGetImageInfo(OH_Drawing_Canvas* canvas, OH_Drawing_Image_Info* imageInfo)
```

**描述**

用于获取画布的图像信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图像信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者imageInfo为空。 |

### OH\_Drawing\_CanvasDrawRecordCmd()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawRecordCmd(OH_Drawing_Canvas* canvas, OH_Drawing_RecordCmd* recordCmd)
```

**描述**

用于绘制录制指令对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针，仅支持录制类型画布。 |
| [OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)\* recordCmd | 指向录制指令对象[OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas或者recordCmd为空。 |

### OH\_Drawing\_CanvasQuickRejectPath()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasQuickRejectPath(OH_Drawing_Canvas* canvas, const OH_Drawing_Path* path,bool* quickReject)
```

**描述**

判断路径与画布区域是否不相交。画布区域包含边界。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool\* quickReject | 表示路径与画布区域是否不相交，true表示路径与画布区域不相交，false表示路径与画布区域相交。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、path或者quickReject为空。 |

### OH\_Drawing\_CanvasQuickRejectRect()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasQuickRejectRect(OH_Drawing_Canvas* canvas, const OH_Drawing_Rect* rect,bool* quickReject)
```

**描述**

判断矩形和画布区域是否不相交。画布区域包含边界。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| bool\* quickReject | 表示矩形与画布区域是否不相交，true表示矩形与画布区域不相交，false表示矩形与画布区域相交。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数canvas、rect或者quickReject为空。 |

### OH\_Drawing\_CanvasDrawPixelMapMesh()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_CanvasDrawPixelMapMesh(OH_Drawing_Canvas* cCanvas, OH_Drawing_PixelMap* pixelMap, uint32_t meshWidth, uint32_t meshHeight, const float* vertices, uint32_t verticesSize, uint32_t vertOffset, const uint32_t* colors, uint32_t colorsSize, uint32_t colorOffset)
```

**描述**

在网格上绘制像素图，网格均匀分布在像素图上。（只支持brush，使用pen没有绘制效果。）

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\* cCanvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的指针。 |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
| uint32\_t meshWidth | 网格的列数，取值为大于0的整数。 |
| uint32\_t meshHeight | 网格的行数，取值为大于0的整数。 |
| const float\* vertices | 指向网格顶点数组的指针。 |
| uint32\_t verticesSize | 网格顶点数组的大小，大小必须为((meshWidth + 1) \* (meshHeight + 1) + vertoffset) \* 2。 |
| uint32\_t vertOffset | 在绘图前需要跳过的顶点数，取值为大于等于0的整数。 |
| const uint32\_t\* colors | 指向网格颜色数组的指针，可为nullptr。 |
| uint32\_t colorsSize | 网格颜色数组的大小，若存在则大小必须为(meshWidth + 1) \* (meshHeight + 1) + colorOffset。 |
| uint32\_t colorOffset | 在绘图前需要跳过的颜色数，取值为大于等于0的整数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示出现cCanvas、pixelMap、vertices等参数为空或传参不符合取值规则的情况。 |
