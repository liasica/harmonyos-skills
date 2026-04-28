---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-path-h
title: drawing_path.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_path.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:471c8634e0009bcba64c4144babbb0335ca256e35bc198721d06e7373e5c689d
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与自定义路径相关的功能函数。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_path.h>

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
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) | OH\_Drawing\_PathDirection | 添加闭合轮廓方向枚举。 |
| [OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype) | OH\_Drawing\_PathFillType | 定义路径的填充类型枚举。 |
| [OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode) | OH\_Drawing\_PathAddMode | 用于指定路径添加模式的枚举类型。 |
| [OH\_Drawing\_PathOpMode](capi-drawing-path-h.md#oh_drawing_pathopmode) | OH\_Drawing\_PathOpMode | 路径操作类型枚举。 |
| [OH\_Drawing\_PathMeasureMatrixFlags](capi-drawing-path-h.md#oh_drawing_pathmeasurematrixflags) | OH\_Drawing\_PathMeasureMatrixFlags | 路径测量获取相应矩阵信息维度枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path\* OH\_Drawing\_PathCreate(void)](capi-drawing-path-h.md#oh_drawing_pathcreate) | 用于创建一个路径对象。 |
| [OH\_Drawing\_Path\* OH\_Drawing\_PathCopy(OH\_Drawing\_Path\* path)](capi-drawing-path-h.md#oh_drawing_pathcopy) | 创建一个路径对象副本[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)，用于拷贝一个已有路径对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathDestroy(OH\_Drawing\_Path\* path)](capi-drawing-path-h.md#oh_drawing_pathdestroy) | 用于销毁路径对象并回收该对象占有的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathSetPath(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other)](capi-drawing-path-h.md#oh_drawing_pathsetpath) | 将一个路径对象设置成当前的路径对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsEmpty(OH\_Drawing\_Path\* path, bool\* isEmpty)](capi-drawing-path-h.md#oh_drawing_pathisempty) | 判断一个路径对象是否为空。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsRect(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect, bool\* isRect)](capi-drawing-path-h.md#oh_drawing_pathisrect) | 判断路径对象是否构成一个矩形。 |
| [void OH\_Drawing\_PathMoveTo(OH\_Drawing\_Path\* path, float x, float y)](capi-drawing-path-h.md#oh_drawing_pathmoveto) | 用于设置自定义路径的起始点位置。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathLineTo(OH\_Drawing\_Path\* path, float x, float y)](capi-drawing-path-h.md#oh_drawing_pathlineto) | 用于添加一条从路径的最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathArcTo(OH\_Drawing\_Path\* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg)](capi-drawing-path-h.md#oh_drawing_patharcto) | 用于给路径添加一段弧线，绘制弧线的方式为角度弧，该方式首先会指定一个矩形边框，  矩形边框的内切椭圆将会被用来截取弧线，然后会指定一个起始角度和扫描度数，  从起始角度扫描截取的椭圆周长一部分即为绘制的弧线。若路径有内容则会默认添加一条从路径的最后点位置到弧线起始点位置的线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)](capi-drawing-path-h.md#oh_drawing_pathquadto) | 用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)](capi-drawing-path-h.md#oh_drawing_pathconicto) | 在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段，其控制点为 (ctrlX, ctrlY)，结束点为 (endX, endY)。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY)](capi-drawing-path-h.md#oh_drawing_pathcubicto) | 用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathRMoveTo(OH\_Drawing\_Path\* path, float x, float y)](capi-drawing-path-h.md#oh_drawing_pathrmoveto) | 用于设置一个相对于当前路径终点（若路径没有内容则默认为 (0, 0)）的路径起始点位置。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathRLineTo(OH\_Drawing\_Path\* path, float x, float y)](capi-drawing-path-h.md#oh_drawing_pathrlineto) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathRQuadTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY)](capi-drawing-path-h.md#oh_drawing_pathrquadto) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathRConicTo(OH\_Drawing\_Path\* path, float ctrlX, float ctrlY, float endX, float endY, float weight)](capi-drawing-path-h.md#oh_drawing_pathrconicto) | 使用相对位置在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathRCubicTo(OH\_Drawing\_Path\* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY)](capi-drawing-path-h.md#oh_drawing_pathrcubicto) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathAddRect(OH\_Drawing\_Path\* path, float left, float top, float right, float bottom,OH\_Drawing\_PathDirection pathDirection)](capi-drawing-path-h.md#oh_drawing_pathaddrect) | 按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddRectWithInitialCorner(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,OH\_Drawing\_PathDirection pathDirection, uint32\_t start)](capi-drawing-path-h.md#oh_drawing_pathaddrectwithinitialcorner) | 按指定方向，向路径添加矩形轮廓。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddRoundRect(OH\_Drawing\_Path\* path,const OH\_Drawing\_RoundRect\* roundRect, OH\_Drawing\_PathDirection pathDirection)](capi-drawing-path-h.md#oh_drawing_pathaddroundrect) | 按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddOvalWithInitialPoint(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect,uint32\_t start, OH\_Drawing\_PathDirection pathDirection)](capi-drawing-path-h.md#oh_drawing_pathaddovalwithinitialpoint) | 将椭圆添加到路径中，其中矩形对象作为椭圆的外切矩形区域，绘制方向用来指定绘制时是顺时针或者逆时针方向。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddOval(OH\_Drawing\_Path\* path,const OH\_Drawing\_Rect\* rect, OH\_Drawing\_PathDirection pathDirection)](capi-drawing-path-h.md#oh_drawing_pathaddoval) | 按指定方向，向路径添加椭圆。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddArc(OH\_Drawing\_Path\* path, const OH\_Drawing\_Rect\* rect, float startAngle, float sweepAngle)](capi-drawing-path-h.md#oh_drawing_pathaddarc) | 将圆弧添加到路径中，作为新轮廓的起点。从起始角度到扫描角度添加弧，添加的弧是矩形内切椭圆的一部分，如果扫描角度<= -360°，或>= 360°，并且起始角度对90取模接近于0，则添加椭圆而不是弧。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathAddPath(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-path-h.md#oh_drawing_pathaddpath) | 将源路径矩阵变换后，添加到当前路径中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathAddPathWithMatrixAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src,const OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathAddMode pathAddMode)](capi-drawing-path-h.md#oh_drawing_pathaddpathwithmatrixandmode) | 将源路径矩阵变换后，以规定模式添加到当前路径中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddPathWithMode(OH\_Drawing\_Path\* path,const OH\_Drawing\_Path\* src, OH\_Drawing\_PathAddMode pathAddMode)](capi-drawing-path-h.md#oh_drawing_pathaddpathwithmode) | 将源路径以规定模式添加到当前路径中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddPathWithOffsetAndMode(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* src, float dx, float dy,OH\_Drawing\_PathAddMode pathAddMode)](capi-drawing-path-h.md#oh_drawing_pathaddpathwithoffsetandmode) | 将源路径偏移后，以规定模式添加到当前路径中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_PathAddPolygon(OH\_Drawing\_Path\* path, const OH\_Drawing\_Point2D\* points, uint32\_t count, bool isClosed)](capi-drawing-path-h.md#oh_drawing_pathaddpolygon) | 向路径添加多边形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、points任意一个为NULL或者count等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathAddCircle(OH\_Drawing\_Path\* path,float x, float y, float radius, OH\_Drawing\_PathDirection pathDirection)](capi-drawing-path-h.md#oh_drawing_pathaddcircle) | 按指定方向，向路径添加圆形。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  radius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE；  pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [bool OH\_Drawing\_PathBuildFromSvgString(OH\_Drawing\_Path\* path, const char\* str)](capi-drawing-path-h.md#oh_drawing_pathbuildfromsvgstring) | 解析SVG字符串表示的路径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、str任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_PathContains(OH\_Drawing\_Path\* path, float x, float y)](capi-drawing-path-h.md#oh_drawing_pathcontains) | 判断指定坐标点是否被路径包含，判定是否被路径包含的规则参考[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathTransform(OH\_Drawing\_Path\* path, const OH\_Drawing\_Matrix\* matrix)](capi-drawing-path-h.md#oh_drawing_pathtransform) | 对路径进行矩阵变换。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathTransformWithPerspectiveClip(OH\_Drawing\_Path\* src, const OH\_Drawing\_Matrix\* matrix,OH\_Drawing\_Path\* dst, bool applyPerspectiveClip)](capi-drawing-path-h.md#oh_drawing_pathtransformwithperspectiveclip) | 对路径进行矩阵变换。用转换后的路径替换目标路径，如果目标路径为NULL，则替换源路径。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  src、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathSetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType pathFillType)](capi-drawing-path-h.md#oh_drawing_pathsetfilltype) | 设置路径的填充类型，这个决定了路径内部区域的定义方式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  pathFillType不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetFillType(OH\_Drawing\_Path\* path, OH\_Drawing\_PathFillType\* pathFillType)](capi-drawing-path-h.md#oh_drawing_pathgetfilltype) | 获取路径的填充类型。 |
| [float OH\_Drawing\_PathGetLength(OH\_Drawing\_Path\* path, bool forceClosed)](capi-drawing-path-h.md#oh_drawing_pathgetlength) | 获取当前路径的长度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathGetBounds(OH\_Drawing\_Path\* path, OH\_Drawing\_Rect\* rect)](capi-drawing-path-h.md#oh_drawing_pathgetbounds) | 获取包含路径的最小边界框。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathClose(OH\_Drawing\_Path\* path)](capi-drawing-path-h.md#oh_drawing_pathclose) | 用于闭合路径，会添加一条从路径起点位置到最后点位置的线段。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathOffset(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* dst, float dx, float dy)](capi-drawing-path-h.md#oh_drawing_pathoffset) | 将路径中的所有点沿着x轴和y轴方向偏移一定距离，并将结果存储到目标路径对象中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_PathReset(OH\_Drawing\_Path\* path)](capi-drawing-path-h.md#oh_drawing_pathreset) | 用于重置自定义路径数据。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_PathIsClosed(OH\_Drawing\_Path\* path, bool forceClosed)](capi-drawing-path-h.md#oh_drawing_pathisclosed) | 获取路径是否闭合。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_PathGetPositionTangent(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Point2D\* position, OH\_Drawing\_Point2D\* tangent)](capi-drawing-path-h.md#oh_drawing_pathgetpositiontangent) | 获取距路径起始点指定距离的坐标点和切线值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、position、tangent任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathGetSegment(OH\_Drawing\_Path\* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH\_Drawing\_Path\* dst, bool\* result)](capi-drawing-path-h.md#oh_drawing_pathgetsegment) | 截取路径的片段并追加到目标路径上。 |
| [bool OH\_Drawing\_PathOp(OH\_Drawing\_Path\* path, const OH\_Drawing\_Path\* other, OH\_Drawing\_PathOpMode op)](capi-drawing-path-h.md#oh_drawing_pathop) | 将两个路径按照指定的路径操作类型合并。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、srcPath任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  op不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [bool OH\_Drawing\_PathGetMatrix(OH\_Drawing\_Path\* path, bool forceClosed,float distance, OH\_Drawing\_Matrix\* matrix, OH\_Drawing\_PathMeasureMatrixFlags flag)](capi-drawing-path-h.md#oh_drawing_pathgetmatrix) | 获取距路径起始点指定距离的相应变换矩阵。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  flag不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathApproximate(OH\_Drawing\_Path\* path, float acceptableError, float\* vals,uint32\_t\* count)](capi-drawing-path-h.md#oh_drawing_pathapproximate) | 将当前路径转化为由连续直线段构成的近似路径。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other,float weight, bool\* success, OH\_Drawing\_Path\* interpolatedPath)](capi-drawing-path-h.md#oh_drawing_pathinterpolate) | 按照给定权重在当前路径与另一条路径之间进行插值，并将结果存储到目标路径对象中。  两条路径点数相同即可插值成功，目标路径按照当前路径的结构进行创建。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsInterpolate(OH\_Drawing\_Path\* path, OH\_Drawing\_Path\* other, bool\* result)](capi-drawing-path-h.md#oh_drawing_pathisinterpolate) | 检查当前路径与另一条路径（other）在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。  若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathIsInverseFillType(const OH\_Drawing\_Path\* path, bool\* isInverse)](capi-drawing-path-h.md#oh_drawing_pathisinversefilltype) | 检查路径的填充类型是否是取反类型。  取反类型即[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)中的PATH\_FILL\_TYPE\_INVERSE\_WINDING和PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PathToggleInverseFillType(OH\_Drawing\_Path\* path)](capi-drawing-path-h.md#oh_drawing_pathtoggleinversefilltype) | 切换路径的填充类型为取反类型。  取反类型即[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)中的PATH\_FILL\_TYPE\_INVERSE\_WINDING和PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PathDirection

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathDirection
```

**描述**

添加闭合轮廓方向枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PATH\_DIRECTION\_CW | 顺时针方向添加闭合轮廓。 |
| PATH\_DIRECTION\_CCW | 逆时针方向添加闭合轮廓。 |

### OH\_Drawing\_PathFillType

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathFillType
```

**描述**

定义路径的填充类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PATH\_FILL\_TYPE\_WINDING | 绘制区域中的任意一点，向任意方向射出一条射线，对于射线和路径的所有交点，初始计数为0，  遇到每个顺时针的交点（路径从射线的左边向右穿过），计数加1，遇到每个逆时针的交点（路径从射线的右边向左穿过），计数减1，若最终的计数结果不为0，则认为这个点在路径内部，需要被涂色；若计数为0则不被涂色。 |
| PATH\_FILL\_TYPE\_EVEN\_ODD | 绘制区域中的任意一点，向任意方向射出一条射线，若这条射线和路径相交的次数是奇数，则这个点被认为在路径内部，需要被涂色；若是偶数则不被涂色。 |
| PATH\_FILL\_TYPE\_INVERSE\_WINDING | PATH\_FILL\_TYPE\_WINDING 涂色规则取反。 |
| PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD | PATH\_FILL\_TYPE\_EVEN\_ODD 涂色规则取反。 |

### OH\_Drawing\_PathAddMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathAddMode
```

**描述**

用于指定路径添加模式的枚举类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PATH\_ADD\_MODE\_APPEND | 以追加的方式添加路径。 |
| PATH\_ADD\_MODE\_EXTEND | 如果之前的路径未闭合，则添加直线闭合路径。 |

### OH\_Drawing\_PathOpMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathOpMode
```

**描述**

路径操作类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| PATH\_OP\_MODE\_DIFFERENCE | 差集操作。 |
| PATH\_OP\_MODE\_INTERSECT | 交集操作。 |
| PATH\_OP\_MODE\_UNION | 并集操作。 |
| PATH\_OP\_MODE\_XOR | 异或操作。 |
| PATH\_OP\_MODE\_REVERSE\_DIFFERENCE | 反向差集操作。 |

### OH\_Drawing\_PathMeasureMatrixFlags

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_PathMeasureMatrixFlags
```

**描述**

路径测量获取相应矩阵信息维度枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| GET\_POSITION\_MATRIX | 获取位置信息对应的矩阵。 |
| GET\_TANGENT\_MATRIX | 获取切线信息对应的矩阵。 |
| GET\_POSITION\_AND\_TANGENT\_MATRIX | 获取位置和切线信息对应的矩阵。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_PathCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Path* OH_Drawing_PathCreate(void)
```

**描述**

用于创建一个路径对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* | 函数会返回一个指针，指针指向创建的路径对象。 |

### OH\_Drawing\_PathCopy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Path* OH_Drawing_PathCopy(OH_Drawing_Path* path)
```

**描述**

创建一个路径对象副本[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)，用于拷贝一个已有路径对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* | 函数返回一个指针，指针指向创建的路径对象副本[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)。 |

### OH\_Drawing\_PathDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathDestroy(OH_Drawing_Path* path)
```

**描述**

用于销毁路径对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |

### OH\_Drawing\_PathSetPath()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathSetPath(OH_Drawing_Path* path, OH_Drawing_Path* other)
```

**描述**

将一个路径对象设置成当前的路径对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* other | 用于设置的路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path或者other为空。 |

### OH\_Drawing\_PathIsEmpty()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIsEmpty(OH_Drawing_Path* path, bool* isEmpty)
```

**描述**

判断一个路径对象是否为空。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool\* isEmpty | 表示路径对象是否为空。true表示路径对象为空，false表示路径对象不为空。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path或者isEmpty为空。 |

### OH\_Drawing\_PathIsRect()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIsRect(OH_Drawing_Path* path, OH_Drawing_Rect* rect, bool* isRect)
```

**描述**

判断路径对象是否构成一个矩形。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，作为出参使用，可以为空。 |
| bool\* isRect | 表示路径是否构成矩形。true表示构成矩形，false表示不构成矩形。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path或者isRect为空。 |

### OH\_Drawing\_PathMoveTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathMoveTo(OH_Drawing_Path* path, float x, float y)
```

**描述**

用于设置自定义路径的起始点位置。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| float x | 起始点的横坐标。 |
| float y | 起始点的纵坐标。 |

### OH\_Drawing\_PathLineTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathLineTo(OH_Drawing_Path* path, float x, float y)
```

**描述**

用于添加一条从路径的最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| float x | 目标点的横坐标。 |
| float y | 目标点的纵坐标。 |

### OH\_Drawing\_PathArcTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathArcTo(OH_Drawing_Path* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg)
```

**描述**

用于给路径添加一段弧线，绘制弧线的方式为角度弧，该方式首先会指定一个矩形边框，

矩形边框的内切椭圆将会被用来截取弧线，然后会指定一个起始角度和扫描度数，

从起始角度扫描截取的椭圆周长一部分即为绘制的弧线。若路径有内容则会默认添加一条从路径的最后点位置到弧线起始点位置的线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| float x1 | 包围椭圆的矩形左上角点位置的横坐标。 |
| float y1 | 包围椭圆的矩形左上角点位置的纵坐标。 |
| float x2 | 包围椭圆的矩形右下角点位置的横坐标。 |
| float y2 | 包围椭圆的矩形右下角点位置的纵坐标。 |
| float startDeg | 起始的角度。角度的起始方向（0°）为x轴正方向。 |
| float sweepDeg | 扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。 |

### OH\_Drawing\_PathQuadTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY)
```

**描述**

用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| float ctrlX | 控制点位置的横坐标。 |
| float ctrlY | 控制点位置的纵坐标。 |
| float endX | 目标点位置的横坐标。 |
| float endY | 目标点位置的纵坐标。 |

### OH\_Drawing\_PathConicTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight)
```

**描述**

在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段，其控制点为 (ctrlX, ctrlY)，结束点为 (endX, endY)。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float ctrlX | 控制点位置的横坐标。 |
| float ctrlY | 控制点位置的纵坐标。 |
| float endX | 结束点位置的横坐标。 |
| float endY | 结束点位置的纵坐标。 |
| float weight | 表示曲线的权重，决定了曲线的形状，越大越接近控制点。  若小于等于0则等同于使用[OH\_Drawing\_PathLineTo](capi-drawing-path-h.md#oh_drawing_pathlineto)添加一条到结束点的线段，  若为1则等同于[OH\_Drawing\_PathQuadTo](capi-drawing-path-h.md#oh_drawing_pathquadto)。 |

### OH\_Drawing\_PathCubicTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY)
```

**描述**

用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |
| float ctrlX1 | 第一个控制点位置的横坐标。 |
| float ctrlY1 | 第一个控制点位置的纵坐标。 |
| float ctrlX2 | 第二个控制点位置的横坐标。 |
| float ctrlY2 | 第二个控制点位置的纵坐标。 |
| float endX | 目标点位置的横坐标。 |
| float endY | 目标点位置的纵坐标。 |

### OH\_Drawing\_PathRMoveTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathRMoveTo(OH_Drawing_Path* path, float x, float y)
```

**描述**

用于设置一个相对于当前路径终点（若路径没有内容则默认为 (0, 0)）的路径起始点位置。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float x | 相对于当前路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移。 |
| float y | 相对于当前路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移。 |

### OH\_Drawing\_PathRLineTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathRLineTo(OH_Drawing_Path* path, float x, float y)
```

**描述**

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float x | 相对于当前路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float y | 相对于当前路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

### OH\_Drawing\_PathRQuadTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathRQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY)
```

**描述**

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float ctrlX | 相对于路径终点的x轴偏移量，用于指定控制点的横坐标。 |
| float ctrlY | 相对于路径终点的y轴偏移量，用于指定控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

### OH\_Drawing\_PathRConicTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathRConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight)
```

**描述**

使用相对位置在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float ctrlX | 相对于路径终点的x轴偏移量，用于指定控制点的横坐标。 |
| float ctrlY | 相对于路径终点的y轴偏移量，用于指定控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |
| float weight | 表示曲线的权重，决定了曲线的形状，越大越接近控制点。  若小于等于0则等同于使用[OH\_Drawing\_PathRLineTo](capi-drawing-path-h.md#oh_drawing_pathrlineto)添加一条到结束点的线段，  若为1则等同于[OH\_Drawing\_PathRQuadTo](capi-drawing-path-h.md#oh_drawing_pathrquadto)。 |

### OH\_Drawing\_PathRCubicTo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathRCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY)
```

**描述**

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float ctrlX1 | 相对于路径终点的x轴偏移量，用于指定第一个控制点的横坐标。 |
| float ctrlY1 | 相对于路径终点的y轴偏移量，用于指定第一个控制点的纵坐标。 |
| float ctrlX2 | 相对于路径终点的x轴偏移量，用于指定第二个控制点的横坐标。 |
| float ctrlY2 | 相对于路径终点的y轴偏移量，用于指定第二个控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

### OH\_Drawing\_PathAddRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddRect(OH_Drawing_Path* path, float left, float top, float right, float bottom,OH_Drawing_PathDirection pathDirection)
```

**描述**

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float left | 矩形左上角的x轴坐标。 |
| float top | 矩形左上角的y轴坐标。 |
| float right | 矩形右下角的x轴坐标。 |
| float bottom | 矩形右下角的y轴坐标。 |
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) pathDirection | 路径方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |

### OH\_Drawing\_PathAddRectWithInitialCorner()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddRectWithInitialCorner(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,OH_Drawing_PathDirection pathDirection, uint32_t start)
```

**描述**

按指定方向，向路径添加矩形轮廓。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| OH\_Drawing\_PathDirection | 表示绘制方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |
| uint32\_t start | 起始点的位置，表示从矩形的哪个角开始绘制路径。0：左上角，1：右上角，2：右下角，3：左下角。 |

### OH\_Drawing\_PathAddRoundRect()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddRoundRect(OH_Drawing_Path* path,const OH_Drawing_RoundRect* roundRect, OH_Drawing_PathDirection pathDirection)
```

**描述**

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、roundRect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathDirection不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)\* roundRect | 指向圆角矩形对象[OH\_Drawing\_RoundRect](capi-drawing-oh-drawing-roundrect.md)的指针。 |
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) pathDirection | 路径方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |

### OH\_Drawing\_PathAddOvalWithInitialPoint()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddOvalWithInitialPoint(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,uint32_t start, OH_Drawing_PathDirection pathDirection)
```

**描述**

将椭圆添加到路径中，其中矩形对象作为椭圆的外切矩形区域，绘制方向用来指定绘制时是顺时针或者逆时针方向。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| uint32\_t start | 表示椭圆初始点的索引。 |
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) pathDirection | 表示绘制方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |

### OH\_Drawing\_PathAddOval()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddOval(OH_Drawing_Path* path,const OH_Drawing_Rect* rect, OH_Drawing_PathDirection pathDirection)
```

**描述**

按指定方向，向路径添加椭圆。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) pathDirection | 路径方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |

### OH\_Drawing\_PathAddArc()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddArc(OH_Drawing_Path* path, const OH_Drawing_Rect* rect, float startAngle, float sweepAngle)
```

**描述**

将圆弧添加到路径中，作为新轮廓的起点。从起始角度到扫描角度添加弧，添加的弧是矩形内切椭圆的一部分，如果扫描角度<= -360°，或>= 360°，并且起始角度对90取模接近于0，则添加椭圆而不是弧。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |
| float startAngle | 弧的起始角度，单位为度。 |
| float sweepAngle | 扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。 |

### OH\_Drawing\_PathAddPath()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddPath(OH_Drawing_Path* path, const OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix)
```

**描述**

将源路径矩阵变换后，添加到当前路径中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向源路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针，为NULL时表示单位矩阵。 |

### OH\_Drawing\_PathAddPathWithMatrixAndMode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddPathWithMatrixAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src,const OH_Drawing_Matrix* matrix, OH_Drawing_PathAddMode pathAddMode)
```

**描述**

将源路径矩阵变换后，以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向源路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针，为NULL表示单位矩阵。 |
| [OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode) pathAddMode | 路径添加模式[OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode)。 |

### OH\_Drawing\_PathAddPathWithMode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddPathWithMode(OH_Drawing_Path* path,const OH_Drawing_Path* src, OH_Drawing_PathAddMode pathAddMode)
```

**描述**

将源路径以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向源路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode) pathAddMode | 路径添加模式[OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode)。 |

### OH\_Drawing\_PathAddPathWithOffsetAndMode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddPathWithOffsetAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src, float dx, float dy,OH_Drawing_PathAddMode pathAddMode)
```

**描述**

将源路径偏移后，以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathAddMode不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向源路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float dx | 添加到目标路径横坐标的偏移量。 |
| float dy | 添加到目标路径纵坐标的偏移量。 |
| [OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode) pathAddMode | 路径添加模式[OH\_Drawing\_PathAddMode](capi-drawing-path-h.md#oh_drawing_pathaddmode)。 |

### OH\_Drawing\_PathAddPolygon()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddPolygon(OH_Drawing_Path* path, const OH_Drawing_Point2D* points, uint32_t count, bool isClosed)
```

**描述**

向路径添加多边形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、points任意一个为NULL或者count等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* points | 表示多边形的顶点坐标数组。 |
| uint32\_t count | 表示多边形顶点坐标数组的大小。 |
| bool isClosed | 是否添加连接起始点和终止点的线，true表示添加，false表示不添加。 |

### OH\_Drawing\_PathAddCircle()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathAddCircle(OH_Drawing_Path* path,float x, float y, float radius, OH_Drawing_PathDirection pathDirection)
```

**描述**

按指定方向，向路径添加圆形。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

radius小于等于0时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE；

pathDirection不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float x | 表示圆心的x轴坐标。 |
| float y | 表示圆心的y轴坐标。 |
| float radius | 表示圆形的半径。 |
| [OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection) pathDirection | 路径方向[OH\_Drawing\_PathDirection](capi-drawing-path-h.md#oh_drawing_pathdirection)。 |

### OH\_Drawing\_PathBuildFromSvgString()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathBuildFromSvgString(OH_Drawing_Path* path, const char* str)
```

**描述**

解析SVG字符串表示的路径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、str任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const char\* str | 表示SVG字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回解析SVG字符串是否成功。true表示成功，false表示不成功。 |

### OH\_Drawing\_PathContains()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathContains(OH_Drawing_Path* path, float x, float y)
```

**描述**

判断指定坐标点是否被路径包含，判定是否被路径包含的规则参考[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float x | x轴上坐标点。 |
| float y | y轴上坐标点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回true表示点在路径内，函数返回false表示点在路径外。 |

### OH\_Drawing\_PathTransform()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathTransform(OH_Drawing_Path* path, const OH_Drawing_Matrix* matrix)
```

**描述**

对路径进行矩阵变换。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针。 |

### OH\_Drawing\_PathTransformWithPerspectiveClip()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathTransformWithPerspectiveClip(OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix,OH_Drawing_Path* dst, bool applyPerspectiveClip)
```

**描述**

对路径进行矩阵变换。用转换后的路径替换目标路径，如果目标路径为NULL，则替换源路径。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

src、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* src | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| const [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 指向矩阵对象[OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* dst | 指向目标路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool applyPerspectiveClip | 表示变换路径是否应用透视裁剪。true表示应用透视裁剪，false表示不用透视裁剪。 |

### OH\_Drawing\_PathSetFillType()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathSetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType pathFillType)
```

**描述**

设置路径的填充类型，这个决定了路径内部区域的定义方式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

pathFillType不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype) pathFillType | 路径填充规则[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)。 |

### OH\_Drawing\_PathGetFillType()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathGetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType* pathFillType)
```

**描述**

获取路径的填充类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)\* pathFillType | 指向路径填充规则[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path或者pathFillType为空。 |

### OH\_Drawing\_PathGetLength()

PhonePC/2in1TabletTVWearable

```
1. float OH_Drawing_PathGetLength(OH_Drawing_Path* path, bool forceClosed)
```

**描述**

获取当前路径的长度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量。true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 函数返回当前路径的长度。 |

### OH\_Drawing\_PathGetBounds()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathGetBounds(OH_Drawing_Path* path, OH_Drawing_Rect* rect)
```

**描述**

获取包含路径的最小边界框。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针。 |

### OH\_Drawing\_PathClose()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathClose(OH_Drawing_Path* path)
```

**描述**

用于闭合路径，会添加一条从路径起点位置到最后点位置的线段。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |

### OH\_Drawing\_PathOffset()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathOffset(OH_Drawing_Path* path, OH_Drawing_Path* dst, float dx, float dy)
```

**描述**

将路径中的所有点沿着x轴和y轴方向偏移一定距离，并将结果存储到目标路径对象中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向当前路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* dst | 指向目标路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针，为NULL时会将结果存储到当前路径对象中。 |
| float dx | x轴方向的偏移量。 |
| float dy | y轴方向的偏移量。 |

### OH\_Drawing\_PathReset()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_PathReset(OH_Drawing_Path* path)
```

**描述**

用于重置自定义路径数据。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象的指针。 |

### OH\_Drawing\_PathIsClosed()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathIsClosed(OH_Drawing_Path* path, bool forceClosed)
```

**描述**

获取路径是否闭合。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回路径是否闭合。true表示路径的测量结果为已闭合，false表示路径的测量结果为未闭合。 |

### OH\_Drawing\_PathGetPositionTangent()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathGetPositionTangent(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Point2D* position, OH_Drawing_Point2D* tangent)
```

**描述**

获取距路径起始点指定距离的坐标点和切线值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、position、tangent任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float distance | 表示距离起始点的距离，小于0时会被视为0处理，大于路径长度时会被视为路径长度处理。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* position | 表示距路径起始点指定距离的坐标点。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* tangent | 表示距路径起始点指定距离的切线值，tangent.x表示该点切线的余弦值，tangent.y表示该点切线的正弦值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回测量是否成功。true表示成功，false表示失败。 |

### OH\_Drawing\_PathGetSegment()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathGetSegment(OH_Drawing_Path* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH_Drawing_Path* dst, bool* result)
```

**描述**

截取路径的片段并追加到目标路径上。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float start | 表示与路径起始点的距离，距离路径起始点start距离的位置即为截取路径片段的起始点，小于0时会被视作0，大于等于stop时会截取失败。 |
| float stop | 表示与路径起始点的距离，距离路径起始点stop距离的位置即为截取路径片段的终点，小于等于start时会截取失败，大于路径长度时会被视作路径长度。 |
| bool startWithMoveTo | 表示是否在目标路径执行[OH\_Drawing\_PathMoveTo](capi-drawing-path-h.md#oh_drawing_pathmoveto)移动到截取路径片段的起始点位置。true表示执行，false表示不执行。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* dst | 指向目标路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针，截取成功时会将得到的路径片段追加到目标路径上，截取失败时不做改变。 |
| bool\* result | 返回是否成功截取路径片段的结果。true表示截取成功，false表示截取失败。作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path、dst、result至少有一个为空指针。 |

### OH\_Drawing\_PathOp()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathOp(OH_Drawing_Path* path, const OH_Drawing_Path* other, OH_Drawing_PathOpMode op)
```

**描述**

将两个路径按照指定的路径操作类型合并。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、srcPath任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

op不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针，操作完成后的路径结果将会保存在此路径对象中。 |
| const [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* other | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_PathOpMode](capi-drawing-path-h.md#oh_drawing_pathopmode) op | 路径操作枚举类型，支持可选的具体模式可见[OH\_Drawing\_PathOpMode](capi-drawing-path-h.md#oh_drawing_pathopmode)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的路径是否为空。true表示路径不为空，false表示路径为空。 |

### OH\_Drawing\_PathGetMatrix()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_PathGetMatrix(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Matrix* matrix, OH_Drawing_PathMeasureMatrixFlags flag)
```

**描述**

获取距路径起始点指定距离的相应变换矩阵。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path、matrix任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

flag不在枚举范围内时返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float distance | 表示距离起始点的距离，小于0时会被视为0处理，大于路径长度时会被视为路径长度处理。 |
| [OH\_Drawing\_Matrix](capi-drawing-oh-drawing-matrix.md)\* matrix | 表示要获取的变换矩阵。 |
| [OH\_Drawing\_PathMeasureMatrixFlags](capi-drawing-path-h.md#oh_drawing_pathmeasurematrixflags) flag | 矩阵信息维度枚举，支持可选的具体模式可见[OH\_Drawing\_PathMeasureMatrixFlags](capi-drawing-path-h.md#oh_drawing_pathmeasurematrixflags)枚举。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回获取变换矩阵是否成功。true表示获取成功，false表示获取失败，失败的原因可能是path为NULL或者长度为0。 |

### OH\_Drawing\_PathApproximate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathApproximate(OH_Drawing_Path* path, float acceptableError, float* vals,uint32_t* count)
```

**描述**

将当前路径转化为由连续直线段构成的近似路径。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float acceptableError | 表示路径上每条线段的可接受误差，不能小于0。  1.当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。  2.当acceptableError特别大时，路径会极度简化，保留少量关键点，可能会丢失原有形状。  3.对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。 |
| float\* vals | 返回包含路径近似点的数组。  每个点由三个值组成，分别表示：  1.该点所在的位置距离路径起点的长度比例值。  2.点的x坐标。  3.点的y坐标。 |
| uint32\_t\* count | 返回数组的大小，数组大小至少为6。vals为空指针时返回拟合后的点数数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path或者count为空指针。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示参数acceptableError小于0。 |

### OH\_Drawing\_PathInterpolate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other,float weight, bool* success, OH_Drawing_Path* interpolatedPath)
```

**描述**

按照给定权重在当前路径与另一条路径之间进行插值，并将结果存储到目标路径对象中。

两条路径点数相同即可插值成功，目标路径按照当前路径的结构进行创建。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* other | 指向用于插值的另一条路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| float weight | 表示插值权重，范围为[0, 1]。 |
| bool\* success | 表示插值是否成功。true表示插值成功，false表示插值失败。作为出参使用。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* interpolatedPath | 指向用于存储插值结果的路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path、other、success或者interpolatedPath为空指针。  返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE，表示参数weight不在[0, 1]范围内。 |

### OH\_Drawing\_PathIsInterpolate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIsInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other, bool* result)
```

**描述**

检查当前路径与另一条路径（other）在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。

若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* other | 指向另一条路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool\* result | 表示当前路径与另一条路径是否兼容插值。作为出参使用。  如果路径兼容，则返回true，否则返回false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数path、other或者result为空指针。 |

### OH\_Drawing\_PathIsInverseFillType()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathIsInverseFillType(const OH_Drawing_Path* path, bool* isInverse)
```

**描述**

检查路径的填充类型是否是取反类型。

取反类型即[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)中的PATH\_FILL\_TYPE\_INVERSE\_WINDING和PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |
| bool\* isInverse | 表示填充类型是否是取反类型。作为出参使用。true表示填充类型是取反类型，false表示填充类型不是取反类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示path或isInverse是空指针。 |

### OH\_Drawing\_PathToggleInverseFillType()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_PathToggleInverseFillType(OH_Drawing_Path* path)
```

**描述**

切换路径的填充类型为取反类型。

取反类型即[OH\_Drawing\_PathFillType](capi-drawing-path-h.md#oh_drawing_pathfilltype)中的PATH\_FILL\_TYPE\_INVERSE\_WINDING和PATH\_FILL\_TYPE\_INVERSE\_EVEN\_ODD。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)\* path | 指向路径对象[OH\_Drawing\_Path](capi-drawing-oh-drawing-path.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示path是空指针。 |
