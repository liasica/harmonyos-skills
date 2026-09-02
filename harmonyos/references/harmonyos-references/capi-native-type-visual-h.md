---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-visual-h
title: native_type_visual.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_type_visual.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8b2674e112eb6f4fb56cbaeb8fcfe0506b9ba616c78a26c4ad328bf117f6b6ef
---

## 概述

提供NativeModule视觉相关的类型定义。

**引用文件：** <arkui/native\_type\_visual.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_TranslationOptions](capi-arkui-nativemodule-arkui-translationoptions.md) | ArkUI\_TranslationOptions | 定义组件转场时平移效果的配置选项，用于设置组件在转场过程中横向、纵向和深度方向的平移距离。 |
| [ArkUI\_ScaleOptions](capi-arkui-nativemodule-arkui-scaleoptions.md) | ArkUI\_ScaleOptions | 定义组件转场时的缩放选项。 |
| [ArkUI\_RotationOptions](capi-arkui-nativemodule-arkui-rotationoptions.md) | ArkUI\_RotationOptions | 定义组件转场时的旋转配置选项。 |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md) | ArkUI\_MotionPathOptions | 定义路径动画的运动路径配置项，用于配置组件在动画过程中沿指定路径运动的轨迹及相关参数，使组件能够按照预设的运动路径进行位移动画。 |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md) | ArkUI\_Matrix4 | 四阶矩阵对象，用于描述UI组件的平移、旋转、缩放等矩阵变换操作，详细使用说明请参见[ArkUI\_NativeModule](capi-arkui-nativemodule.md)。 |
| [ArkUI\_PointF](capi-arkui-nativemodule-arkui-pointf.md) | ArkUI\_PointF | 定义一个二维坐标点结构体，用于描述组件位置或偏移等坐标信息，坐标以浮点类型存储。 |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md) | ArkUI\_Matrix4RotationOptions | 定义矩阵旋转变换的参数配置对象。 |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md) | ArkUI\_Matrix4ScaleOptions | 定义4×4矩阵缩放变换的参数配置对象，各参数及其取值原则详见成员变量说明。 |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md) | ArkUI\_Matrix4TranslationOptions | 定义矩阵平移变换的参数配置对象。 |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md) | OH\_ArkUI\_ShadowOptions | 定义阴影选项。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ShadowType](capi-native-type-visual-h.md#arkui_shadowtype) | ArkUI\_ShadowType | 定义阴影类型枚举值。 |
| [ArkUI\_ShadowStyle](capi-native-type-visual-h.md#arkui_shadowstyle) | ArkUI\_ShadowStyle | 阴影效果枚举值。 |
| [ArkUI\_AnimationCurve](capi-native-type-visual-h.md#arkui_animationcurve) | ArkUI\_AnimationCurve | 动画曲线枚举值。 |
| [ArkUI\_AnimationPlayMode](capi-native-type-visual-h.md#arkui_animationplaymode) | ArkUI\_AnimationPlayMode | 定义动画播放模式。 |
| [ArkUI\_BlurStyle](capi-native-type-visual-h.md#arkui_blurstyle) | ArkUI\_BlurStyle | 定义背景模糊样式。 |
| [ArkUI\_BlurStyleActivePolicy](capi-native-type-visual-h.md#arkui_blurstyleactivepolicy) | ArkUI\_BlurStyleActivePolicy | 定义背景模糊激活策略。 |
| [ArkUI\_BlendMode](capi-native-type-visual-h.md#arkui_blendmode) | ArkUI\_BlendMode | 混合模式枚举值。 |
| [ArkUI\_ColorStrategy](capi-native-type-visual-h.md#arkui_colorstrategy) | ArkUI\_ColorStrategy | 前景和阴影颜色的枚举值。 |
| [ArkUI\_MaskType](capi-native-type-visual-h.md#arkui_masktype) | ArkUI\_MaskType | 遮罩类型枚举。遮罩是一种用于限制组件显示区域的手段，它利用特定的形状对组件内容进行裁剪，从而实现只有遮罩区域内的内容才可见的效果。 |
| [ArkUI\_ClipType](capi-native-type-visual-h.md#arkui_cliptype) | ArkUI\_ClipType | 裁剪类型枚举。 |
| [ArkUI\_ShapeType](capi-native-type-visual-h.md#arkui_shapetype) | ArkUI\_ShapeType | 定义形状类型的枚举值。 |
| [ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection) | ArkUI\_LinearGradientDirection | 定义渐变方向枚举值。 |
| [ArkUI\_TransitionEdge](capi-native-type-visual-h.md#arkui_transitionedge) | ArkUI\_TransitionEdge | 定义转场从边缘滑入和滑出的效果。 |
| [ArkUI\_FinishCallbackType](capi-native-type-visual-h.md#arkui_finishcallbacktype) | ArkUI\_FinishCallbackType | 在动画中定义[OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_animatoroption_registeronfinishcallback)回调的类型。 |
| [ArkUI\_BlendApplyType](capi-native-type-visual-h.md#arkui_blendapplytype) | ArkUI\_BlendApplyType | 定义混合模式应用于视图内容的方式的枚举值。 |
| [ArkUI\_RenderFit](capi-native-type-visual-h.md#arkui_renderfit) | ArkUI\_RenderFit | 定义动画终态内容大小与位置的枚举值。 |
| [ArkUI\_AnimationDirection](capi-native-type-visual-h.md#arkui_animationdirection) | ArkUI\_AnimationDirection | 动画播放方向。 |
| [ArkUI\_AnimationFillMode](capi-native-type-visual-h.md#arkui_animationfillmode) | ArkUI\_AnimationFillMode | 定义帧动画组件在动画开始前和结束后的状态。 |

### 函数

| 名称 | 返回值 | 描述 |
| --- | --- | --- |
| [ArkUI\_Matrix4ScaleOptions\* OH\_ArkUI\_Matrix4ScaleOptions\_Create()](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_create) | - | 创建指向矩阵运算的缩放参数对象的指针。新创建的对象中，x、y和z方向的缩放系数默认值为1，单次矩阵变换中心点相对于组件变换中心点的x轴偏移值centerX和y轴偏移值centerY默认值为0。 |
| [void OH\_ArkUI\_Matrix4ScaleOptions\_Dispose(ArkUI\_Matrix4ScaleOptions\* options)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_dispose) | - | 销毁指向矩阵运算的缩放参数对象的指针。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_SetX(ArkUI\_Matrix4ScaleOptions\* options, const float scaleX)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_setx) | - | 设置矩阵运算的缩放参数对象x方向的缩放因子。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_GetX(const ArkUI\_Matrix4ScaleOptions\* options, float\* scaleX)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_getx) | - | 获取矩阵运算的缩放参数对象x方向的缩放因子。如果从未设置x的值，则x方向的缩放因子默认值为1。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_SetY(ArkUI\_Matrix4ScaleOptions\* options, const float scaleY)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_sety) | - | 设置矩阵运算的缩放参数对象y方向的缩放因子。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_GetY(const ArkUI\_Matrix4ScaleOptions\* options, float\* scaleY)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_gety) | - | 获取矩阵运算的缩放参数对象y方向的缩放因子。如果从未设置y的值，则y方向的缩放因子默认值为1。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_SetZ(ArkUI\_Matrix4ScaleOptions\* options, const float scaleZ)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_setz) | - | 设置矩阵运算的缩放参数对象z方向的缩放因子。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_GetZ(const ArkUI\_Matrix4ScaleOptions\* options, float\* scaleZ)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_getz) | - | 获取矩阵运算的缩放参数对象z方向的缩放因子。如果从未设置z的值，则z方向的缩放因子默认值为1。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_SetCenterX(ArkUI\_Matrix4ScaleOptions\* options, const float centerX)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_setcenterx) | - | 设置矩阵运算的缩放参数对象变换中心点的x轴坐标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_GetCenterX(const ArkUI\_Matrix4ScaleOptions\* options, float\* centerX)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_getcenterx) | - | 获取矩阵运算的缩放参数对象变换中心点的x轴坐标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_SetCenterY(ArkUI\_Matrix4ScaleOptions\* options, const float centerY)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_setcentery) | - | 设置矩阵运算的缩放参数对象变换中心点的y轴坐标。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4ScaleOptions\_GetCenterY(const ArkUI\_Matrix4ScaleOptions\* options, float\* centerY)](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_getcentery) | - | 获取矩阵运算的缩放参数对象变换中心点的y轴坐标。 |
| [ArkUI\_Matrix4RotationOptions\* OH\_ArkUI\_Matrix4RotationOptions\_Create()](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_create) | - | 创建矩阵运算的旋转参数对象的指针。在新创建的对象中，centerX（单次矩阵变换中心点相对于组件变换中心点的x轴偏移值）、centerY（y轴偏移值）和旋转角度angle默认值为0。如果未指定x、y、z方向向量，则默认x=0、y=0、z=1（绕z轴旋转）；一旦指定了任意一个方向向量，其余未指定的值等同于0。 |
| [void OH\_ArkUI\_Matrix4RotationOptions\_Dispose(ArkUI\_Matrix4RotationOptions\* options)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_dispose) | - | 销毁指向矩阵运算的旋转参数对象的指针。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetX(ArkUI\_Matrix4RotationOptions\* options, const float x)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_setx) | - | 设置矩阵运算的旋转参数对象x方向的方向向量。一旦指定了任一方向向量（x、y或z），其余未指定的方向向量值将等同于0；若全部未指定，则默认等同于x=0、y=0、z=1，表示绕z轴旋转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetX(const ArkUI\_Matrix4RotationOptions\* options, float\* x)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_getx) | - | 获取矩阵运算的旋转参数对象x方向的方向向量。如果从未设置过x值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。请先通过OH\_ArkUI\_Matrix4RotationOptions\_SetX设置x值后再调用此函数获取。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetY(ArkUI\_Matrix4RotationOptions\* options, const float y)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_sety) | - | 设置矩阵运算的旋转参数对象y方向的方向向量。一旦指定了任一方向向量（x、y或z），其余未指定的方向向量值将等同于0；若全部未指定，则默认等同于x=0、y=0、z=1，表示绕z轴旋转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetY(const ArkUI\_Matrix4RotationOptions\* options, float\* y)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_gety) | - | 获取矩阵运算的旋转参数对象y方向的方向向量。如果从未设置过y值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetZ(ArkUI\_Matrix4RotationOptions\* options, const float z)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_setz) | - | 设置矩阵运算的旋转参数对象z方向的方向向量。一旦指定了任一方向向量（x、y或z），其余未指定的方向向量值将等同于0；若全部未指定，则默认等同于x=0、y=0、z=1，表示绕z轴旋转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetZ(const ArkUI\_Matrix4RotationOptions\* options, float\* z)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_getz) | - | 获取矩阵运算的旋转参数对象z方向的方向向量。如果从未设置过z值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetAngle(ArkUI\_Matrix4RotationOptions\* options, const float angle)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_setangle) | - | 设置矩阵运算的旋转参数对象中旋转角度的值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetAngle(const ArkUI\_Matrix4RotationOptions\* options, float\* angle)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_getangle) | - | 获取矩阵运算的旋转参数对象中旋转角度的值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetCenterX(ArkUI\_Matrix4RotationOptions\* options, const float centerX)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_setcenterx) | - | 设置单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetCenterX(const ArkUI\_Matrix4RotationOptions\* options, float\* centerX)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_getcenterx) | - | 获取单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_SetCenterY(ArkUI\_Matrix4RotationOptions\* options, const float centerY)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_setcentery) | - | 设置单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4RotationOptions\_GetCenterY(const ArkUI\_Matrix4RotationOptions\* options, float\* centerY)](capi-native-type-visual-h.md#oh_arkui_matrix4rotationoptions_getcentery) | - | 获取单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。 |
| [ArkUI\_Matrix4TranslationOptions\* OH\_ArkUI\_Matrix4TranslationOptions\_Create()](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_create) | - | 创建指向矩阵运算的平移对象的指针。在新创建的对象中，x轴的平移距离x、y轴的平移距离y和z轴的平移距离z的默认值为0。 |
| [void OH\_ArkUI\_Matrix4TranslationOptions\_Dispose(ArkUI\_Matrix4TranslationOptions\* options)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_dispose) | - | 销毁指向矩阵运算的平移对象的指针。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_SetX(ArkUI\_Matrix4TranslationOptions\* options, const float x)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_setx) | - | 设置矩阵运算的平移对象x轴方向的平移值，单位为px。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_GetX(const ArkUI\_Matrix4TranslationOptions\* options, float\* x)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_getx) | - | 获取矩阵运算的平移对象x轴方向的平移值，单位为px。如果从未设置x的值，其默认值为0。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_SetY(ArkUI\_Matrix4TranslationOptions\* options, const float y)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_sety) | - | 设置矩阵运算的平移对象y轴方向的平移值，单位为px。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_GetY(const ArkUI\_Matrix4TranslationOptions\* options, float\* y)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_gety) | - | 获取矩阵运算的平移对象y轴方向的平移值，单位为px。如果从未设置y的值，其默认值为0。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_SetZ(ArkUI\_Matrix4TranslationOptions\* options, const float z)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_setz) | - | 设置矩阵运算的平移对象z轴方向的平移值，单位为px。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4TranslationOptions\_GetZ(const ArkUI\_Matrix4TranslationOptions\* options, float\* z)](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_getz) | - | 获取矩阵运算的平移对象z轴方向的平移值，单位为px。如果从未设置z的值，其默认值为0。 |
| [ArkUI\_Matrix4\* OH\_ArkUI\_Matrix4\_CreateIdentity()](capi-native-type-visual-h.md#oh_arkui_matrix4_createidentity) | - | 创建一个单位四阶矩阵对象。当该对象不再使用时，请调用[OH\_ArkUI\_Matrix4\_Dispose](capi-native-type-visual-h.md#oh_arkui_matrix4_dispose)销毁。 |
| [ArkUI\_Matrix4\* OH\_ArkUI\_Matrix4\_CreateByElements(const float\* elements)](capi-native-type-visual-h.md#oh_arkui_matrix4_createbyelements) | - | 通过指定矩阵的每个元素来创建一个四阶矩阵对象。当该对象不再使用时，请调用[OH\_ArkUI\_Matrix4\_Dispose](capi-native-type-visual-h.md#oh_arkui_matrix4_dispose)销毁。 |
| [void OH\_ArkUI\_Matrix4\_Dispose(ArkUI\_Matrix4\* matrix)](capi-native-type-visual-h.md#oh_arkui_matrix4_dispose) | - | 销毁矩阵对象的指针。 |
| [ArkUI\_Matrix4\* OH\_ArkUI\_Matrix4\_Copy(const ArkUI\_Matrix4\* matrix)](capi-native-type-visual-h.md#oh_arkui_matrix4_copy) | - | 创建四阶矩阵对象的副本。用于对同一矩阵进行操作，以获取不同的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Invert(ArkUI\_Matrix4\* matrix)](capi-native-type-visual-h.md#oh_arkui_matrix4_invert) | - | 对输入矩阵执行逆矩阵变换，变换后将修改输入的矩阵对象。此函数将修改输入的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Combine(ArkUI\_Matrix4\* oriMatrix, const ArkUI\_Matrix4\* anotherMatrix)](capi-native-type-visual-h.md#oh_arkui_matrix4_combine) | - | 将另一个矩阵与原始矩阵合并，并将结果矩阵存储在oriMatrix中。结果矩阵相当于先应用oriMatrix的变换，然后再应用anotherMatrix的变换。此函数将修改oriMatrix对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Translate(ArkUI\_Matrix4\* matrix, const ArkUI\_Matrix4TranslationOptions\* translate)](capi-native-type-visual-h.md#oh_arkui_matrix4_translate) | - | 对原始矩阵应用平移变换以获取平移后的矩阵。每次平移变换都是在先前的矩阵上累积的。变换后将修改输入的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Scale(ArkUI\_Matrix4\* matrix, const ArkUI\_Matrix4ScaleOptions\* scale)](capi-native-type-visual-h.md#oh_arkui_matrix4_scale) | - | 对原始矩阵应用缩放变换以获取缩放后的矩阵。每次缩放变换都是在先前的矩阵上累积的。此函数将修改输入的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Rotate(ArkUI\_Matrix4\* matrix, const ArkUI\_Matrix4RotationOptions\* rotate)](capi-native-type-visual-h.md#oh_arkui_matrix4_rotate) | - | 对原始矩阵应用旋转变换以获取旋转后的矩阵。每次旋转变换都是在先前的矩阵上累积的。此函数将修改输入的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_Skew(ArkUI\_Matrix4\* matrix, const float skewX, const float skewY)](capi-native-type-visual-h.md#oh_arkui_matrix4_skew) | - | 对原始矩阵应用倾斜变换以获取倾斜后的矩阵。每次倾斜变换都是在先前的矩阵上累积的。变换后将修改输入的矩阵对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_TransformPoint(const ArkUI\_Matrix4\* matrix, const ArkUI\_PointF\* oriPoint, ArkUI\_PointF\* result)](capi-native-type-visual-h.md#oh_arkui_matrix4_transformpoint) | - | 计算一个点经过矩阵变换后的新坐标位置。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_SetPolyToPoly(ArkUI\_Matrix4\* matrix, const ArkUI\_PointF\* src, const ArkUI\_PointF\* dst, const uint32\_t pointCount)](capi-native-type-visual-h.md#oh_arkui_matrix4_setpolytopoly) | - | 将一个多边形的顶点坐标映射到另一个多边形的顶点坐标，并计算所需的矩阵。pointCount的值决定了计算的变换类型：0表示单位矩阵变换，1表示平移变换，2表示旋转或缩放变换，3表示仿射变换，4表示透视变换。传入其他值时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_Matrix4\_GetElements(const ArkUI\_Matrix4\* matrix, float\* result)](capi-native-type-visual-h.md#oh_arkui_matrix4_getelements) | - | 获取四阶矩阵的16个元素。数组按行优先顺序存储，长度必须大于或等于16，否则将导致未定义行为。 |
| [ArkUI\_MotionPathOptions\* OH\_ArkUI\_MotionPathOptions\_Create()](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_create) | - | 创建路径动画的运动路径配置项。当该对象不再使用时，请调用[OH\_ArkUI\_MotionPathOptions\_Dispose](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_dispose)销毁。 |
| [void OH\_ArkUI\_MotionPathOptions\_Dispose(ArkUI\_MotionPathOptions\* options)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_dispose) | - | 销毁路径动画的运动路径配置项。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_SetPath(ArkUI\_MotionPathOptions\* options, const char\* svgPath)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setpath) | - | 设置路径动画的运动路径。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_GetPath(const ArkUI\_MotionPathOptions\* options, char\* svgPathBuffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_getpath) | - | 获取路径动画的运动路径配置项中存储的运动路径字符串。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_SetFrom(ArkUI\_MotionPathOptions\* options, const float from)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setfrom) | - | 设置路径动画起点进度。进度指已移动路径长度与总路径长度的比值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_GetFrom(const ArkUI\_MotionPathOptions\* options, float\* from)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_getfrom) | - | 获取路径动画的运动路径配置项中的路径动画起点进度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_SetTo(ArkUI\_MotionPathOptions\* options, const float to)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setto) | - | 设置路径动画终点进度。进度指已移动路径长度与总路径长度的比值。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_GetTo(const ArkUI\_MotionPathOptions\* options, float\* to)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_getto) | - | 获取路径动画的运动路径配置项中的路径动画终点进度。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_SetRotatable(ArkUI\_MotionPathOptions\* options, const bool rotatable)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setrotatable) | - | 设置组件是否沿运动路径旋转。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_MotionPathOptions\_GetRotatable(const ArkUI\_MotionPathOptions\* options, bool\* rotatable)](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_getrotatable) | - | 获取组件是否沿运动路径旋转。 |
| [OH\_ArkUI\_ShadowOptions\* OH\_ArkUI\_ShadowOptions\_Create()](capi-native-type-visual-h.md#oh_arkui_shadowoptions_create) | - | 创建一个阴影选项对象。在新创建的对象中，模糊半径radius默认值为0，阴影类型type默认值为ARKUI\_SHADOW\_TYPE\_COLOR，阴影颜色color默认值为0xFF000000，x轴偏移量offsetX默认值为0，y轴偏移量offsetY默认值为0，是否填充isFill默认值为false。当该对象不再使用时，请调用[OH\_ArkUI\_ShadowOptions\_Destroy](capi-native-type-visual-h.md#oh_arkui_shadowoptions_destroy)销毁。 |
| [void OH\_ArkUI\_ShadowOptions\_Destroy(OH\_ArkUI\_ShadowOptions\* options)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_destroy) | - | 销毁阴影选项对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetRadius(OH\_ArkUI\_ShadowOptions\* options, float radius)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setradius) | - | 设置阴影选项的模糊半径。取值范围：[0, +∞)，单位为vp。传入负数时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetRadius(OH\_ArkUI\_ShadowOptions\* options, float\* radius)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_getradius) | - | 获取阴影选项的模糊半径。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetType(OH\_ArkUI\_ShadowOptions\* options, ArkUI\_ShadowType type)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_settype) | - | 设置阴影选项的阴影类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetType(OH\_ArkUI\_ShadowOptions\* options, ArkUI\_ShadowType\* type)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_gettype) | - | 获取阴影选项的阴影类型。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetColor(OH\_ArkUI\_ShadowOptions\* options, uint32\_t color)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setcolor) | - | 设置阴影选项的阴影颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetColor(OH\_ArkUI\_ShadowOptions\* options, uint32\_t\* color)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_getcolor) | - | 获取阴影选项的阴影颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetOffsetX(OH\_ArkUI\_ShadowOptions\* options, float offsetX)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setoffsetx) | - | 设置阴影在x轴上的偏移量。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetOffsetX(OH\_ArkUI\_ShadowOptions\* options, float\* offsetX)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_getoffsetx) | - | 获取阴影在x轴上的偏移量。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetOffsetY(OH\_ArkUI\_ShadowOptions\* options, float offsetY)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setoffsety) | - | 设置阴影在y轴上的偏移量。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetOffsetY(OH\_ArkUI\_ShadowOptions\* options, float\* offsetY)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_getoffsety) | - | 获取阴影在y轴上的偏移量。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_SetFill(OH\_ArkUI\_ShadowOptions\* options, bool isFill)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setfill) | - | 设置是否用阴影填充组件内部。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_ShadowOptions\_GetFill(OH\_ArkUI\_ShadowOptions\* options, bool\* isFill)](capi-native-type-visual-h.md#oh_arkui_shadowoptions_getfill) | - | 获取是否用阴影填充组件内部。 |

## 枚举类型说明

### ArkUI\_ShadowType

```c
enum ArkUI_ShadowType
```

**描述：**

定义阴影类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHADOW\_TYPE\_COLOR = 0 | 彩色阴影。 |
| ARKUI\_SHADOW\_TYPE\_BLUR = 1 | 模糊阴影。 |

### ArkUI\_ShadowStyle

```c
enum ArkUI_ShadowStyle
```

**描述：**

阴影效果枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_XS = 0 | 超小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_SM = 1 | 小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_MD = 2 | 中阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_DEFAULT\_LG = 3 | 大阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_SM = 4 | 浮动小阴影。 |
| ARKUI\_SHADOW\_STYLE\_OUTER\_FLOATING\_MD = 5 | 浮动中阴影。 |

### ArkUI\_AnimationCurve

```c
enum ArkUI_AnimationCurve
```

**描述：**

动画曲线枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CURVE\_LINEAR = 0 | 动画从头到尾的速度都是相同。 |
| ARKUI\_CURVE\_EASE = 1 | 动画以低速开始，然后加快，在结束前变慢。 |
| ARKUI\_CURVE\_EASE\_IN = 2 | 动画以低速开始。 |
| ARKUI\_CURVE\_EASE\_OUT = 3 | 动画以低速结束。 |
| ARKUI\_CURVE\_EASE\_IN\_OUT = 4 | 动画以低速开始和结束，提供平滑自然的动画过渡效果。 |
| ARKUI\_CURVE\_FAST\_OUT\_SLOW\_IN = 5 | 动画标准曲线。 |
| ARKUI\_CURVE\_LINEAR\_OUT\_SLOW\_IN = 6 | 动画减速曲线。 |
| ARKUI\_CURVE\_FAST\_OUT\_LINEAR\_IN = 7 | 动画加速曲线。 |
| ARKUI\_CURVE\_EXTREME\_DECELERATION = 8 | 动画极缓曲线。 |
| ARKUI\_CURVE\_SHARP = 9 | 动画锐利曲线。 |
| ARKUI\_CURVE\_RHYTHM = 10 | 动画节奏曲线。 |
| ARKUI\_CURVE\_SMOOTH = 11 | 动画平滑曲线。 |
| ARKUI\_CURVE\_FRICTION = 12 | 动画阻尼曲线。 |

### ArkUI\_AnimationPlayMode

```c
enum ArkUI_AnimationPlayMode
```

**描述：**

定义动画播放模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_PLAY\_MODE\_NORMAL = 0 | 动画正向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_REVERSE = 1 | 动画反向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE = 2 | 动画交替循环播放，在奇数次正向播放，在偶数次反向播放。 |
| ARKUI\_ANIMATION\_PLAY\_MODE\_ALTERNATE\_REVERSE = 3 | 动画反向交替循环播放，在奇数次反向播放，在偶数次正向播放。 |

### ArkUI\_BlurStyle

```c
enum ArkUI_BlurStyle
```

**描述：**

定义背景模糊样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLUR\_STYLE\_THIN = 0 | 轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_REGULAR = 1 | 普通厚度材质模糊。 |
| ARKUI\_BLUR\_STYLE\_THICK = 2 | 厚材质模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THIN = 3 | 近距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_REGULAR = 4 | 中距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_THICK = 5 | 远距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_BACKGROUND\_ULTRA\_THICK = 6 | 超远距景深模糊。 |
| ARKUI\_BLUR\_STYLE\_NONE = 7 | 关闭模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THIN = 8 | 组件超轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THIN = 9 | 组件轻薄材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_REGULAR = 10 | 组件普通材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_THICK = 11 | 组件厚材质模糊。 |
| ARKUI\_BLUR\_STYLE\_COMPONENT\_ULTRA\_THICK = 12 | 组件超厚材质模糊。 |

### ArkUI\_BlurStyleActivePolicy

```c
enum ArkUI_BlurStyleActivePolicy
```

**描述：**

定义背景模糊激活策略。

**起始版本：** 19

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_FOLLOWS\_WINDOW\_ACTIVE\_STATE = 0 | 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。 |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_ACTIVE = 1 | 一直有模糊效果。 |
| ARKUI\_BLUR\_STYLE\_ACTIVE\_POLICY\_ALWAYS\_INACTIVE = 2 | 一直无模糊效果。 |

### ArkUI\_BlendMode

```c
enum ArkUI_BlendMode
```

**描述：**

混合模式枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_BLEND\_MODE\_NONE = 0 | 将上层图像直接覆盖到下层图像上，不进行任何混合操作。 |
| ARKUI\_BLEND\_MODE\_CLEAR = 1 | 将源像素覆盖的目标像素清除为完全透明。 |
| ARKUI\_BLEND\_MODE\_SRC = 2 | r = s，只显示源像素。 |
| ARKUI\_BLEND\_MODE\_DST = 3 | r = d，只显示目标像素。 |
| ARKUI\_BLEND\_MODE\_SRC\_OVER = 4 | r = s + (1 - sa) \* d，将源像素按照透明度进行混合，覆盖在目标像素上。 |
| ARKUI\_BLEND\_MODE\_DST\_OVER = 5 | r = d + (1 - da) \* s，将目标像素按照透明度进行混合，覆盖在源像素上。 |
| ARKUI\_BLEND\_MODE\_SRC\_IN = 6 | r = s \* da，只显示源像素中与目标像素重叠的部分。 |
| ARKUI\_BLEND\_MODE\_DST\_IN = 7 | r = d \* sa，只显示目标像素中与源像素重叠的部分。 |
| ARKUI\_BLEND\_MODE\_SRC\_OUT = 8 | r = s \* (1 - da)，只显示源像素中与目标像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_DST\_OUT = 9 | r = d \* (1 - sa)，只显示目标像素中与源像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_SRC\_ATOP = 10 | r = s \* da + d \* (1 - sa)，在源像素和目标像素重叠的地方绘制源像素，在源像素和目标像素不重叠的地方绘制目标像素。 |
| ARKUI\_BLEND\_MODE\_DST\_ATOP = 11 | r = d \* sa + s \* (1 - da)，在源像素和目标像素重叠的地方绘制目标像素，在源像素和目标像素不重叠的地方绘制源像素。 |
| ARKUI\_BLEND\_MODE\_XOR = 12 | r = s \* (1 - da) + d \* (1 - sa)，只显示源像素与目标像素不重叠的部分。 |
| ARKUI\_BLEND\_MODE\_PLUS = 13 | r = min(s + d, 1)，将源像素值与目标像素值相加，并将结果作为新的像素值。 |
| ARKUI\_BLEND\_MODE\_MODULATE = 14 | r = s \* d，将源像素与目标像素进行乘法运算，并将结果作为新的像素值。 |
| ARKUI\_BLEND\_MODE\_SCREEN = 15 | r = s + d - s \* d，将两个图像的像素值相加，然后减去它们的乘积来实现混合。 |
| ARKUI\_BLEND\_MODE\_OVERLAY = 16 | 根据目标像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI\_BLEND\_MODE\_DARKEN = 17 | rc = s + d - max(s \* da, d \* sa), ra = kSrcOver，当两个颜色重叠时，较暗的颜色会覆盖较亮的颜色。 |
| ARKUI\_BLEND\_MODE\_LIGHTEN = 18 | rc = s + d - min(s \* da, d \* sa), ra = kSrcOver，将源图像和目标图像中的像素进行比较，选取两者中较亮的像素作为最终的混合结果。 |
| ARKUI\_BLEND\_MODE\_COLOR\_DODGE = 19 | 使目标像素变得更亮来反映源像素。 |
| ARKUI\_BLEND\_MODE\_COLOR\_BURN = 20 | 使目标像素变得更暗来反映源像素。 |
| ARKUI\_BLEND\_MODE\_HARD\_LIGHT = 21 | 根据源像素的值来决定目标像素变得更亮或者更暗。根据源像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| ARKUI\_BLEND\_MODE\_SOFT\_LIGHT = 22 | 根据源像素来决定使用LIGHTEN混合模式还是DARKEN混合模式。 |
| ARKUI\_BLEND\_MODE\_DIFFERENCE = 23 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生高对比度的效果。 |
| ARKUI\_BLEND\_MODE\_EXCLUSION = 24 | rc = s + d - 2 \* (s \* d), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生柔和的效果。 |
| ARKUI\_BLEND\_MODE\_MULTIPLY = 25 | r = s \* (1 - da) + d \* (1 - sa) + s \* d，将源图像与目标图像进行乘法混合，得到一张新的图像。 |
| ARKUI\_BLEND\_MODE\_HUE = 26 | 保留源图像的亮度和饱和度，但会使用目标图像的色调来替换源图像的色调。 |
| ARKUI\_BLEND\_MODE\_SATURATION = 27 | 保留目标像素的亮度和色调，但会使用源像素的饱和度来替换目标像素的饱和度。 |
| ARKUI\_BLEND\_MODE\_COLOR = 28 | 保留源像素的饱和度和色调，但会使用目标像素的亮度来替换源像素的亮度。 |
| ARKUI\_BLEND\_MODE\_LUMINOSITY = 29 | 保留目标像素的色调和饱和度，但会用源像素的亮度替换目标像素的亮度。 |

### ArkUI\_ColorStrategy

```c
enum ArkUI_ColorStrategy
```

**描述：**

前景和阴影颜色的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_COLOR\_STRATEGY\_INVERT = 0 | 前景色为控件背景色的反色。 |
| ARKUI\_COLOR\_STRATEGY\_AVERAGE = 1 | 控件背景阴影色为控件背景阴影区域的平均色。 |
| ARKUI\_COLOR\_STRATEGY\_PRIMARY = 2 | 控件背景阴影色为控件背景阴影区域的主色。 |

### ArkUI\_MaskType

```c
enum ArkUI_MaskType
```

**描述：**

遮罩类型枚举。遮罩是一种用于限制组件显示区域的手段，它利用特定的形状对组件内容进行裁剪，从而实现只有遮罩区域内的内容才可见的效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MASK\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_MASK\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_MASK\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_MASK\_TYPE\_PATH = 3 | 路径类型。 |
| ARKUI\_MASK\_TYPE\_PROGRESS = 4 | 进度类型。 |

### ArkUI\_ClipType

```c
enum ArkUI_ClipType
```

**描述：**

裁剪类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CLIP\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_CLIP\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_CLIP\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_CLIP\_TYPE\_PATH = 3 | 路径类型。 |

### ArkUI\_ShapeType

```c
enum ArkUI_ShapeType
```

**描述：**

定义形状类型的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SHAPE\_TYPE\_RECTANGLE = 0 | 矩形类型。 |
| ARKUI\_SHAPE\_TYPE\_CIRCLE = 1 | 圆形类型。 |
| ARKUI\_SHAPE\_TYPE\_ELLIPSE = 2 | 椭圆形类型。 |
| ARKUI\_SHAPE\_TYPE\_PATH = 3 | 路径类型。 |

### ArkUI\_LinearGradientDirection

```c
enum ArkUI_LinearGradientDirection
```

**描述：**

定义线性渐变方向枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT = 0 | 向左渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_TOP = 1 | 向上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT = 2 | 向右渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_BOTTOM = 3 | 向下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_TOP = 4 | 向左上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM = 5 | 向左下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_TOP = 6 | 向右上渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_RIGHT\_BOTTOM = 7 | 向右下渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_NONE = 8 | 不渐变。 |
| ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM = 9 | 自定义渐变方向。 |

### ArkUI\_TransitionEdge

```c
enum ArkUI_TransitionEdge
```

**描述：**

定义转场从边缘滑入和滑出的效果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TRANSITION\_EDGE\_TOP = 0 | 转场从窗口的上边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_BOTTOM = 1 | 转场从窗口的下边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_START = 2 | 转场从窗口的左边缘滑入和滑出。 |
| ARKUI\_TRANSITION\_EDGE\_END = 3 | 转场从窗口的右边缘滑入和滑出。 |

### ArkUI\_FinishCallbackType

```c
enum ArkUI_FinishCallbackType
```

**描述：**

在动画中定义[OH\_ArkUI\_AnimatorOption\_RegisterOnFinishCallback](capi-native-animate-h.md#oh_arkui_animatoroption_registeronfinishcallback)回调的类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_FINISH\_CALLBACK\_REMOVED = 0 | 当整个动画结束并立即删除时，将触发回调。 |
| ARKUI\_FINISH\_CALLBACK\_LOGICALLY = 1 | 当动画在逻辑上已完成，但可能仍处于其长尾状态时，将触发回调。长尾状态是指动画即将完全停止前的残余变化过程，此时动画的数值变化已非常微小，接近目标值。 |

### ArkUI\_BlendApplyType

```c
enum ArkUI_BlendApplyType
```

**描述：**

指定的混合模式应用于视图的内容选项。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| BLEND\_APPLY\_TYPE\_FAST = 0 | 在目标图像上按顺序混合视图的内容。 |
| BLEND\_APPLY\_TYPE\_OFFSCREEN = 1 | 将此组件和子组件内容绘制到离屏画布上，然后整体进行混合。 |

### ArkUI\_RenderFit

```c
enum ArkUI_RenderFit
```

**描述：**

定义动画终态内容大小与位置的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_RENDER\_FIT\_CENTER = 0 | 保持动画终态的内容大小，并且内容始终与组件保持中心对齐。 |
| ARKUI\_RENDER\_FIT\_TOP = 1 | 保持动画终态的内容大小，并且内容始终与组件保持顶部中心对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM = 2 | 保持动画终态的内容大小，并且内容始终与组件保持底部中心对齐。 |
| ARKUI\_RENDER\_FIT\_LEFT = 3 | 保持动画终态的内容大小，并且内容始终与组件保持左侧对齐。 |
| ARKUI\_RENDER\_FIT\_RIGHT = 4 | 保持动画终态的内容大小，并且内容始终与组件保持右侧对齐。 |
| ARKUI\_RENDER\_FIT\_TOP\_LEFT = 5 | 保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。 |
| ARKUI\_RENDER\_FIT\_TOP\_RIGHT = 6 | 保持动画终态的内容大小，并且内容始终与组件保持右上角对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM\_LEFT = 7 | 保持动画终态的内容大小，并且内容始终与组件保持左下角对齐。 |
| ARKUI\_RENDER\_FIT\_BOTTOM\_RIGHT = 8 | 保持动画终态的内容大小，并且内容始终与组件保持右下角对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_FILL = 9 | 不考虑动画终态内容的宽高比，并且内容始终缩放到组件的大小。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN = 10 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内，且与组件保持中心对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_TOP\_LEFT = 11 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持左侧对齐，当组件高方向有剩余时，内容与组件保持顶部对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_CONTAIN\_BOTTOM\_RIGHT = 12 | 保持动画终态内容的宽高比进行缩小或放大，使内容完整显示在组件内。当组件宽方向有剩余时，内容与组件保持右侧对齐，当组件高方向有剩余时，内容与组件保持底部对齐。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER = 13 | 保持动画终态内容的宽高比进行缩小或放大，使内容两边都大于或等于组件两边，且与组件保持中心对齐，显示内容的中间部分。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_TOP\_LEFT = 14 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持左侧对齐，显示内容的左侧部分。当内容高方向有剩余时，内容与组件保持顶部对齐，显示内容的顶侧部分。 |
| ARKUI\_RENDER\_FIT\_RESIZE\_COVER\_BOTTOM\_RIGHT = 15 | 保持动画终态内容的宽高比进行缩小或放大，使内容的两边都恰好大于或等于组件两边。当内容宽方向有剩余时，内容与组件保持右侧对齐，显示内容的右侧部分。当内容高方向有剩余时，内容与组件保持底部对齐，显示内容的底侧部分。 |

### ArkUI\_AnimationDirection

```c
enum ArkUI_AnimationDirection
```

**描述：**

动画播放方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_DIRECTION\_NORMAL = 0 | 动画正向循环播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_REVERSE = 1 | 动画反向循环播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE = 2 | 动画交替循环播放，在奇数次正向播放，在偶数次反向播放。 |
| ARKUI\_ANIMATION\_DIRECTION\_ALTERNATE\_REVERSE = 3 | 动画反向交替循环播放，在奇数次反向播放，在偶数次正向播放。 |

### ArkUI\_AnimationFillMode

```c
enum ArkUI_AnimationFillMode
```

**描述：**

定义帧动画组件在动画开始前和结束后的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ANIMATION\_FILL\_MODE\_NONE = 0 | 动画未执行时不会将任何样式应用于目标，动画播放完成之后恢复初始默认状态。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS = 1 | 目标将保留动画执行期间最后一个关键帧的状态。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS = 2 | 动画将在应用于目标时立即应用第一个关键帧中定义的值，并在[delay](capi-native-animate-h.md#oh_arkui_animateoption_setdelay)期间保留此值。 |
| ARKUI\_ANIMATION\_FILL\_MODE\_BOTH = 3 | 动画将遵循[ARKUI\_ANIMATION\_FILL\_MODE\_FORWARDS](capi-native-type-visual-h.md#arkui_animationfillmode)和[ARKUI\_ANIMATION\_FILL\_MODE\_BACKWARDS](capi-native-type-visual-h.md#arkui_animationfillmode)的规则，从而在两个方向上扩展动画属性。 |

## 函数说明

### OH\_ArkUI\_Matrix4\_CreateIdentity()

```c
ArkUI_Matrix4* OH_ArkUI_Matrix4_CreateIdentity()
```

**描述：**

创建一个单位四阶矩阵对象。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* | 返回指向创建的单位四阶矩阵对象的指针。 |

### OH\_ArkUI\_Matrix4\_CreateByElements()

```c
ArkUI_Matrix4* OH_ArkUI_Matrix4_CreateByElements(const float* elements)
```

**描述：**

通过指定矩阵的每个元素来创建一个四阶矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const float\* elements | 指向预期矩阵元素数据的数组指针。数组长度应大于或等于16，若不足16可能导致未定义行为。该参数不可为空指针，若为空指针函数将返回空值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* | 返回通过指定矩阵元素创建的四阶矩阵对象。如果elements指针为空，函数将返回NULL。 |

### OH\_ArkUI\_Matrix4\_Dispose()

```c
void OH_ArkUI_Matrix4_Dispose(ArkUI_Matrix4* matrix)
```

**描述：**

销毁矩阵对象的指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向要销毁的四阶矩阵对象的指针。 |

### OH\_ArkUI\_Matrix4\_Copy()

```c
ArkUI_Matrix4* OH_ArkUI_Matrix4_Copy(const ArkUI_Matrix4* matrix)
```

**描述：**

创建四阶矩阵对象的副本。通过复制原始矩阵，可以对其进行独立操作以获取不同矩阵变换结果。当该副本对象不再使用时，请调用[OH\_ArkUI\_Matrix4\_Dispose](capi-native-type-visual-h.md#oh_arkui_matrix4_dispose)销毁。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向原始四阶矩阵对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* | 返回四阶矩阵对象的副本对象。 |

### OH\_ArkUI\_Matrix4\_Invert()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Invert(ArkUI_Matrix4* matrix)
```

**描述：**

对输入矩阵执行逆矩阵变换，变换后将修改输入的矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向要逆矩阵变换的四阶矩阵对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常（如传入空指针），返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_Combine()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Combine(ArkUI_Matrix4* oriMatrix, const ArkUI_Matrix4* anotherMatrix)
```

**描述：**

将另一个矩阵与原始矩阵合并，并将结果矩阵存储在oriMatrix中。结果矩阵相当于先应用oriMatrix的变换，然后再应用anotherMatrix的变换。此函数将修改oriMatrix对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* oriMatrix | 指向原始四阶矩阵对象的指针。 |
| const [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* anotherMatrix | 指向要合并的另一个矩阵对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果oriMatrix或anotherMatrix为空指针，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_Translate()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Translate(ArkUI_Matrix4* matrix, const ArkUI_Matrix4TranslationOptions* translate)
```

**描述：**

对原始矩阵应用平移变换以获取平移后的矩阵。每次平移变换都是在先前的矩阵上累积的。变换后将修改输入的矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向待平移四阶矩阵对象的指针。 |
| const [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* translate | 指向平移对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果matrix或translate为空指针，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_Scale()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Scale(ArkUI_Matrix4* matrix, const ArkUI_Matrix4ScaleOptions* scale)
```

**描述：**

对原始矩阵应用缩放变换以获取缩放后的矩阵。每次缩放变换都是在先前的矩阵上累积的。此函数将修改输入的矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向待缩放四阶矩阵对象的指针。 |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* scale | 指向缩放对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果options为空指针，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)，请确保传入有效的缩放参数对象指针。 |

### OH\_ArkUI\_Matrix4\_Rotate()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Rotate(ArkUI_Matrix4* matrix, const ArkUI_Matrix4RotationOptions* rotate)
```

**描述：**

对原始矩阵应用旋转变换以获取旋转后的矩阵。每次旋转变换都是在先前的矩阵上累积的。此函数将修改输入的矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向待旋转四阶矩阵对象的指针。 |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* rotate | 指向旋转对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果matrix或rotate为空指针，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)，请确保传入有效的对象指针。 |

### OH\_ArkUI\_Matrix4\_Skew()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_Skew(ArkUI_Matrix4* matrix, const float skewX, const float skewY)
```

**描述：**

对原始矩阵应用倾斜变换以获取倾斜后的矩阵。每次倾斜变换都是在先前的矩阵上累积的。变换后将修改输入的矩阵对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向待倾斜四阶矩阵对象的指针。 |
| const float skewX | x方向的倾斜系数。取值范围：(-∞, +∞)。0表示无倾斜，正值使内容沿x方向正向倾斜，负值使内容沿x方向负向倾斜。 |
| const float skewY | y方向的倾斜系数。取值范围：(-∞, +∞)。0表示无倾斜，正值使内容沿y方向正向倾斜，负值使内容沿y方向负向倾斜。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_TransformPoint()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_TransformPoint(const ArkUI_Matrix4* matrix, const ArkUI_PointF* oriPoint, ArkUI_PointF* result)
```

**描述：**

计算一个点经过矩阵变换后的新坐标位置。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向四阶矩阵对象的指针。不能为空。 |
| const [ArkUI\_PointF](capi-arkui-nativemodule-arkui-pointf.md)\* oriPoint | 指向原始坐标点的指针。不能为空。 |
| [ArkUI\_PointF](capi-arkui-nativemodule-arkui-pointf.md)\* result | 指向结果点的指针。不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_SetPolyToPoly()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_SetPolyToPoly(ArkUI_Matrix4* matrix, const ArkUI_PointF* src, const ArkUI_PointF* dst, const uint32_t pointCount)
```

**描述：**

将一个多边形的顶点坐标映射到另一个多边形的顶点坐标，并计算所需的矩阵。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向四阶矩阵对象的指针，用于存放结果矩阵。 |
| const [ArkUI\_PointF](capi-arkui-nativemodule-arkui-pointf.md)\* src | 指向原始多边形坐标点数组的指针。数组长度应至少为pointCount，否则将导致未定义行为。 |
| const [ArkUI\_PointF](capi-arkui-nativemodule-arkui-pointf.md)\* dst | 指向映射后多边形坐标点数组的指针。数组长度应至少为pointCount，否则将导致未定义行为。 |
| const uint32\_t pointCount | 多边形点的数量，必须是0、1、2、3或4中的一个值。传入其他值时将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4\_GetElements()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4_GetElements(const ArkUI_Matrix4* matrix, float* result)
```

**描述：**

获取四阶矩阵的16个元素。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4](capi-arkui-nativemodule-arkui-matrix4.md)\* matrix | 指向四阶矩阵对象的指针。 |
| float\* result | 指向可容纳16个浮点数的数组的指针。不能为空。若缓冲区容量不足16个浮点数，可能导致未定义行为。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_Create()

```c
ArkUI_Matrix4ScaleOptions* OH_ArkUI_Matrix4ScaleOptions_Create()
```

**描述：**

创建指向矩阵运算的缩放参数对象的指针。在新创建的对象中，x、y和z轴方向的缩放系数默认值为1。变换中心点的x轴坐标centerX、变换中心点的y轴坐标centerY默认值为0。当该对象不再使用时，请调用[OH\_ArkUI\_Matrix4ScaleOptions\_Dispose](capi-native-type-visual-h.md#oh_arkui_matrix4scaleoptions_dispose)销毁。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* | 返回指向新创建的[ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)的指针，用于配置矩阵运算的缩放参数。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_Dispose()

```c
void OH_ArkUI_Matrix4ScaleOptions_Dispose(ArkUI_Matrix4ScaleOptions* options)
```

**描述：**

销毁指向矩阵运算的缩放参数对象的指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向要销毁的[ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)对象的指针。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_SetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_SetX(ArkUI_Matrix4ScaleOptions* options, const float scaleX)
```

**描述：**

设置矩阵运算的缩放参数对象x方向的缩放因子。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| const float scaleX | x方向的缩放因子。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_GetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_GetX(const ArkUI_Matrix4ScaleOptions* options, float* scaleX)
```

**描述：**

获取矩阵运算的缩放参数对象x方向的缩放因子。如果从未设置x的值，则x方向的缩放因子默认值为1。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| float\* scaleX | x方向的缩放因子。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_SetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_SetY(ArkUI_Matrix4ScaleOptions* options, const float scaleY)
```

**描述：**

设置矩阵运算的缩放参数对象y方向的缩放因子。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| const float scaleY | y方向的缩放因子。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_GetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_GetY(const ArkUI_Matrix4ScaleOptions* options, float* scaleY)
```

**描述：**

获取矩阵运算的缩放参数对象y方向的缩放因子。如果从未设置y的值，则y方向的缩放因子默认值为1。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| float\* scaleY | y方向的缩放因子。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_SetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_SetZ(ArkUI_Matrix4ScaleOptions* options, const float scaleZ)
```

**描述：**

设置矩阵运算的缩放参数对象z方向的缩放因子。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| const float scaleZ | z方向的缩放因子。取值范围：(-∞, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_GetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_GetZ(const ArkUI_Matrix4ScaleOptions* options, float* scaleZ)
```

**描述：**

获取矩阵运算的缩放参数对象z方向的缩放因子。如果从未设置z的值，则z方向的缩放因子默认值为1。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| float\* scaleZ | z方向的缩放因子。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_SetCenterX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_SetCenterX(ArkUI_Matrix4ScaleOptions* options, const float centerX)
```

**描述：**

设置矩阵运算的缩放参数对象变换中心点的x轴坐标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| const float centerX | 变换中心点的x轴坐标。取值范围：(-∞, +∞)。0表示在变换中心基础上没有x方向偏移。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_GetCenterX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_GetCenterX(const ArkUI_Matrix4ScaleOptions* options, float* centerX)
```

**描述：**

获取矩阵运算的缩放参数对象变换中心点的x轴坐标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| float\* centerX | 变换中心点的x轴坐标。单位为px。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_SetCenterY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_SetCenterY(ArkUI_Matrix4ScaleOptions* options, const float centerY)
```

**描述：**

设置矩阵运算的缩放参数对象变换中心点的y轴坐标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| const float centerY | 变换中心点的y轴坐标。取值范围：(-∞, +∞)。0表示在变换中心基础上没有y方向偏移。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4ScaleOptions\_GetCenterY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4ScaleOptions_GetCenterY(const ArkUI_Matrix4ScaleOptions* options, float* centerY)
```

**描述：**

获取矩阵运算的缩放参数对象变换中心点的y轴坐标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4ScaleOptions](capi-arkui-nativemodule-arkui-matrix4scaleoptions.md)\* options | 指向矩阵运算的缩放参数对象的指针。 |
| float\* centerY | 变换中心点的y轴坐标。单位为px。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_Create()

```c
ArkUI_Matrix4RotationOptions* OH_ArkUI_Matrix4RotationOptions_Create()
```

**描述：**

创建矩阵运算的旋转参数对象的指针。在新创建的对象中，单次矩阵变换中心点相对于组件变换中心点的x轴偏移值centerX、单次矩阵变换中心点相对于组件变换中心点的y轴偏移值centerY、旋转角度angle的默认值，为0。如果未指定x、y、z方向的方向向量中的任何一个，旋转效果等同于绕z轴旋转（即计算时方向向量取x=0、y=0、z=1）。一旦指定了x、y、z方向的方向向量中的任意一个，以指定的方向向量生效。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* | 返回指向新创建的[ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)的指针，用于配置矩阵运算的旋转参数。 |

### OH\_ArkUI\_Matrix4RotationOptions\_Dispose()

```c
void OH_ArkUI_Matrix4RotationOptions_Dispose(ArkUI_Matrix4RotationOptions* options)
```

**描述：**

销毁指向矩阵运算的旋转参数对象的指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetX(ArkUI_Matrix4RotationOptions* options, const float x)
```

**描述：**

设置矩阵运算的旋转参数对象x方向的方向向量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float x | x轴方向的方向向量的值。取值范围：(-∞, +∞)。与y、z方向向量共同构成旋转轴，如x=1且y=0、z=0时表示绕x轴旋转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetX(const ArkUI_Matrix4RotationOptions* options, float* x)
```

**描述：**

获取矩阵运算的旋转参数对象x方向的方向向量。如果从未设置过x值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* x | x轴方向的方向向量的值。如果从未设置x的值，其值将未定义。该参数与y、z方向向量共同构成旋转轴。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetY(ArkUI_Matrix4RotationOptions* options, const float y)
```

**描述：**

设置矩阵运算的旋转参数对象y方向的方向向量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float y | y轴方向的方向向量的值。取值范围：(-∞, +∞)。与x、z方向向量共同构成旋转轴，如y=1且x=0、z=0时表示绕y轴旋转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetY(const ArkUI_Matrix4RotationOptions* options, float* y)
```

**描述：**

获取矩阵运算的旋转参数对象y方向的方向向量。如果从未设置过y值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* y | y轴方向的方向向量的值。如果从未设置y的值，其值将未定义。该参数与x、z方向向量共同构成旋转轴。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetZ(ArkUI_Matrix4RotationOptions* options, const float z)
```

**描述：**

设置矩阵运算的旋转参数对象z方向的方向向量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float z | z轴方向的方向向量的值。取值范围：(-∞, +∞)。与x、y方向向量共同构成旋转轴，如z=1且x=0、y=0时表示绕z轴旋转（默认行为）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetZ(const ArkUI_Matrix4RotationOptions* options, float* z)
```

**描述：**

获取矩阵运算的旋转参数对象z方向的方向向量。如果从未设置过z值，其值将处于未定义状态，此时函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* z | z轴方向的方向向量的值。如果从未设置z的值，其值将未定义。该参数与x、y方向向量共同构成旋转轴。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetAngle()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetAngle(ArkUI_Matrix4RotationOptions* options, const float angle)
```

**描述：**

设置矩阵运算的旋转参数对象中旋转角度的值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float angle | 旋转角度的值。取值范围：(-∞, +∞)。单位为度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetAngle()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetAngle(const ArkUI_Matrix4RotationOptions* options, float* angle)
```

**描述：**

获取矩阵运算的旋转参数对象中旋转角度的值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* angle | 旋转角度的值。单位为度。如果从未设置angle的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetCenterX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetCenterX(ArkUI_Matrix4RotationOptions* options, const float centerX)
```

**描述：**

设置单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float centerX | 单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。取值范围：(-∞, +∞)。0表示在变换中心基础上没有x方向偏移。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetCenterX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetCenterX(const ArkUI_Matrix4RotationOptions* options, float* centerX)
```

**描述：**

获取单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* centerX | 单次矩阵变换中心点相对于组件变换中心点的x轴偏移值。单位为px。如果从未设置centerX的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_SetCenterY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_SetCenterY(ArkUI_Matrix4RotationOptions* options, const float centerY)
```

**描述：**

设置单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| const float centerY | 单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。取值范围：(-∞, +∞)。0表示在变换中心基础上没有y方向偏移。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4RotationOptions\_GetCenterY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4RotationOptions_GetCenterY(const ArkUI_Matrix4RotationOptions* options, float* centerY)
```

**描述：**

获取单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4RotationOptions](capi-arkui-nativemodule-arkui-matrix4rotationoptions.md)\* options | 指向矩阵运算的旋转参数对象的指针。 |
| float\* centerY | 单次矩阵变换中心点相对于组件变换中心点的y轴偏移值。单位为px。如果从未设置centerY的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_Create()

```c
ArkUI_Matrix4TranslationOptions* OH_ArkUI_Matrix4TranslationOptions_Create()
```

**描述：**

创建指向矩阵运算的平移对象的指针。在新创建的对象中，x轴的平移距离x、y轴的平移距离y和z轴的平移距离z的默认值为0。当该对象不再使用时，请调用[OH\_ArkUI\_Matrix4TranslationOptions\_Dispose](capi-native-type-visual-h.md#oh_arkui_matrix4translationoptions_dispose)销毁。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* | 返回指向新创建的[ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)的指针，用于配置矩阵运算的平移参数。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_Dispose()

```c
void OH_ArkUI_Matrix4TranslationOptions_Dispose(ArkUI_Matrix4TranslationOptions* options)
```

**描述：**

销毁指向矩阵运算的平移对象的指针。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向要销毁的[ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)对象的指针。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_SetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_SetX(ArkUI_Matrix4TranslationOptions* options, const float x)
```

**描述：**

设置矩阵运算的平移对象x轴方向的平移值，单位为px。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| const float x | x轴方向的平移值。取值范围：(-∞, +∞)。单位为px。如果从未设置x的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_GetX()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_GetX(const ArkUI_Matrix4TranslationOptions* options, float* x)
```

**描述：**

获取矩阵运算的平移对象x轴方向的平移值，单位为px。如果从未设置x的值，其默认值为0。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| float\* x | x轴方向的平移值。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_SetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_SetY(ArkUI_Matrix4TranslationOptions* options, const float y)
```

**描述：**

设置矩阵运算的平移对象y轴方向的平移值，单位为px。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| const float y | y轴方向的平移值。取值范围：(-∞, +∞)。单位为px。如果从未设置y的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_GetY()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_GetY(const ArkUI_Matrix4TranslationOptions* options, float* y)
```

**描述：**

获取矩阵运算的平移对象y轴方向的平移值，单位为px。如果从未设置y的值，其默认值为0。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| float\* y | y轴方向的平移值。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_SetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_SetZ(ArkUI_Matrix4TranslationOptions* options, const float z)
```

**描述：**

设置矩阵运算的平移对象z轴方向的平移值，单位为px。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| const float z | z轴方向的平移值。取值范围：(-∞, +∞)。单位为px。如果从未设置z的值，其默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_Matrix4TranslationOptions\_GetZ()

```c
ArkUI_ErrorCode OH_ArkUI_Matrix4TranslationOptions_GetZ(const ArkUI_Matrix4TranslationOptions* options, float* z)
```

**描述：**

获取矩阵运算的平移对象z轴方向的平移值，单位为px。如果从未设置z的值，其默认值为0。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_Matrix4TranslationOptions](capi-arkui-nativemodule-arkui-matrix4translationoptions.md)\* options | 指向矩阵运算的平移参数对象的指针。 |
| float\* z | z轴方向的平移值。单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_MotionPathOptions\_Create()

```c
ArkUI_MotionPathOptions* OH_ArkUI_MotionPathOptions_Create()
```

**描述：**

创建路径动画的运动路径配置项。当该对象不再使用时，请调用[OH\_ArkUI\_MotionPathOptions\_Dispose](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_dispose)销毁。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。  新建的[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)对象中，路径动画的运动路径path值为空字符串，路径动画起点进度from值为0，路径动画终点进度to值为1，组件是否沿路径旋转rotatable值为false。 |

### OH\_ArkUI\_MotionPathOptions\_Dispose()

```c
void OH_ArkUI_MotionPathOptions_Dispose(ArkUI_MotionPathOptions* options)
```

**描述：**

销毁路径动画的运动路径配置项。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |

### OH\_ArkUI\_MotionPathOptions\_SetPath()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetPath(ArkUI_MotionPathOptions* options, const char* svgPath)
```

**描述：**

设置路径动画的运动路径。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const char\* svgPath | 路径动画的运动路径字符串。  该路径支持使用"start"和"end"作为起点和终点的占位符，例如："Mstart.x start.y L50 50 Lend.x end.y Z"。路径字符串格式请参考[绘制路径](../harmonyos-guides/ui-js-components-svg-path.md)。若设置为空字符串，等效于未设置路径动画。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) options为空指针或svgPath为空指针，请确保传入有效的运动路径配置项指针和路径字符串。 |

### OH\_ArkUI\_MotionPathOptions\_GetPath()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetPath(const ArkUI_MotionPathOptions* options, char* svgPathBuffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述：**

获取路径动画的运动路径配置项中存储的运动路径字符串。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| char\* svgPathBuffer | 存储运动路径字符串的缓冲区指针。不能为空指针，缓冲区大小须足够容纳路径字符串。 |
| const int32\_t bufferSize | svgPathBuffer参数的缓冲区大小，必须大于0。传入0或负数时返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| int32\_t\* writeLength | 返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示实际写入缓冲区的字符串长度（含终止符）。  返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，如果为入参异常，writeLength不会被赋值；如果为拷贝异常，writeLength为可容纳目标字符串的最小缓冲区大小。  返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)时，表示可容纳目标字符串的最小缓冲区大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  如果操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果发生参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  如果缓冲区大小不足，返回[ARKUI\_ERROR\_CODE\_BUFFER\_SIZE\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_MotionPathOptions\_SetFrom()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetFrom(ArkUI_MotionPathOptions* options, const float from)
```

**描述：**

设置路径动画起点进度。进度指已移动路径长度与总路径长度的比值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const float from | 路径动画的起点进度，取值范围为[0.0, 1.0]，且需满足from小于或等于终点进度to，否则将返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)错误码。  to的含义参考[OH\_ArkUI\_MotionPathOptions\_SetTo](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setto)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) from超出[0.0, 1.0]范围，或from大于终点进度to，请将from值设置在[0.0, 1.0]范围内且确保from不大于终点进度to。 |

### OH\_ArkUI\_MotionPathOptions\_GetFrom()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetFrom(const ArkUI_MotionPathOptions* options, float* from)
```

**描述：**

获取路径动画的运动路径配置项中的路径动画起点进度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| float\* from | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中起点进度值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_SetTo()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetTo(ArkUI_MotionPathOptions* options, const float to)
```

**描述：**

设置路径动画终点进度。进度指已移动路径长度与总路径长度的比值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const float to | 路径动画的终点进度，取值范围为[0.0, 1.0]，且需满足to大于或等于起点进度from；否则将返回[ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)错误码。  from的含义参考[OH\_ArkUI\_MotionPathOptions\_SetFrom](capi-native-type-visual-h.md#oh_arkui_motionpathoptions_setfrom)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。  [ARKUI\_ERROR\_CODE\_PARAM\_OUT\_OF\_RANGE](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) to超出[0.0, 1.0]范围，或to小于起点进度from。 |

### OH\_ArkUI\_MotionPathOptions\_GetTo()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetTo(const ArkUI_MotionPathOptions* options, float* to)
```

**描述：**

获取路径动画的运动路径配置项中的路径动画终点进度。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| float\* to | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中终点进度值的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_SetRotatable()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_SetRotatable(ArkUI_MotionPathOptions* options, const bool rotatable)
```

**描述：**

设置组件是否沿运动路径旋转。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| const bool rotatable | 组件是否沿路径旋转。true表示组件沿路径旋转；false表示组件不沿路径旋转。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_MotionPathOptions\_GetRotatable()

```c
ArkUI_ErrorCode OH_ArkUI_MotionPathOptions_GetRotatable(const ArkUI_MotionPathOptions* options, bool* rotatable)
```

**描述：**

获取组件是否沿运动路径旋转。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)\* options | 指向路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)的指针。 |
| bool\* rotatable | 用于接收路径动画的运动路径配置项[ArkUI\_MotionPathOptions](capi-arkui-nativemodule-arkui-motionpathoptions.md)中rotatable参数值的指针，表示组件是否沿路径旋转。  true表示组件沿路径旋转；false表示组件不沿路径旋转。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_ShadowOptions\_Create()

```c
OH_ArkUI_ShadowOptions* OH_ArkUI_ShadowOptions_Create()
```

**描述：**

创建一个阴影选项对象。在新创建的对象中，模糊半径radius的默认值为0，阴影在x轴上的偏移量offsetX的默认值为0，阴影在y轴上的偏移量offsetY的默认值为0，阴影颜色color的默认值为0xFF000000，阴影类型type的默认值为ARKUI\_SHADOW\_TYPE\_COLOR，是否用阴影填充组件内部isFill的默认值为false。当该对象不再使用时，请调用[OH\_ArkUI\_ShadowOptions\_Destroy](capi-native-type-visual-h.md#oh_arkui_shadowoptions_destroy)销毁。

**起始版本：** 24

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions\*](capi-arkui-nativemodule-oh-arkui-shadowoptions.md) | 指向新创建的[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针，用于配置阴影的模糊半径、类型、颜色和偏移量等属性。 |

### OH\_ArkUI\_ShadowOptions\_Destroy()

```c
void OH_ArkUI_ShadowOptions_Destroy(OH_ArkUI_ShadowOptions* options)
```

**描述：**

销毁阴影选项对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向新创建的[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针，用于配置阴影的模糊半径、类型、颜色和偏移量等属性。 |

### OH\_ArkUI\_ShadowOptions\_SetRadius()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetRadius(OH_ArkUI_ShadowOptions* options, float radius)
```

**描述：**

设置阴影选项的模糊半径。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float radius | 阴影的模糊半径，取值范围：(-∞, +∞)，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若options为空指针，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)，请确保传入有效的阴影选项对象指针。 |

### OH\_ArkUI\_ShadowOptions\_GetRadius()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetRadius(OH_ArkUI_ShadowOptions* options, float* radius)
```

**描述**

获取阴影选项的模糊半径。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float\* radius | 阴影的模糊半径，单位为px。值为0时无模糊效果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_SetType()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetType(OH_ArkUI_ShadowOptions* options, ArkUI_ShadowType type)
```

**描述**

设置阴影选项的阴影类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| [ArkUI\_ShadowType](capi-native-type-visual-h.md#arkui_shadowtype) type | 阴影类型[ArkUI\_ShadowType](capi-native-type-visual-h.md#arkui_shadowtype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_GetType()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetType(OH_ArkUI_ShadowOptions* options, ArkUI_ShadowType* type)
```

**描述**

获取阴影选项的阴影类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| [ArkUI\_ShadowType](capi-native-type-visual-h.md#arkui_shadowtype)\* type | 阴影类型[ArkUI\_ShadowType](capi-native-type-visual-h.md#arkui_shadowtype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_SetColor()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetColor(OH_ArkUI_ShadowOptions* options, uint32_t color)
```

**描述**

设置阴影选项的阴影颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| uint32\_t color | 阴影颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_GetColor()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetColor(OH_ArkUI_ShadowOptions* options, uint32_t* color)
```

**描述**

获取阴影选项的阴影颜色。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| uint32\_t\* color | 阴影颜色，0xARGB格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_SetOffsetX()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetOffsetX(OH_ArkUI_ShadowOptions* options, float offsetX)
```

**描述**

设置阴影在x轴上的偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float offsetX | 阴影在x轴上的偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_GetOffsetX()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetOffsetX(OH_ArkUI_ShadowOptions* options, float* offsetX)
```

**描述**

获取阴影在x轴上的偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float\* offsetX | 阴影在x轴上的偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_SetOffsetY()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetOffsetY(OH_ArkUI_ShadowOptions* options, float offsetY)
```

**描述**

设置阴影在y轴上的偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float offsetY | 阴影在y轴上的偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_GetOffsetY()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetOffsetY(OH_ArkUI_ShadowOptions* options, float* offsetY)
```

**描述**

获取阴影在y轴上的偏移量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| float\* offsetY | 阴影在y轴上的偏移量，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_SetFill()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_SetFill(OH_ArkUI_ShadowOptions* options, bool isFill)
```

**描述**

设置是否用阴影填充组件内部。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| bool isFill | 是否用阴影填充组件内部。true表示用阴影填充组件内部，false表示不用阴影填充组件内部。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

### OH\_ArkUI\_ShadowOptions\_GetFill()

```c
ArkUI_ErrorCode OH_ArkUI_ShadowOptions_GetFill(OH_ArkUI_ShadowOptions* options, bool* isFill)
```

**描述**

获取是否用阴影填充组件内部。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)\* options | 指向[OH\_ArkUI\_ShadowOptions](capi-arkui-nativemodule-oh-arkui-shadowoptions.md)对象的指针。 |
| bool\* isFill | 是否用阴影填充组件内部。true表示用阴影填充组件内部，false表示不用阴影填充组件内部。默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | 返回结果码。  若操作成功，返回[ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。  若参数异常，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
