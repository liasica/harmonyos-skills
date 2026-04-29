---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation
title: 图形变换
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 图形变换
category: harmonyos-references
scraped_at: 2026-04-29T13:51:18+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:d5de45da3a422c2e8f0da60a47bb52468cfd0addfc5737fbad64d3aad9b2c182
---

用于对组件进行旋转、平移、缩放、矩阵变换等操作。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## rotate

PhonePC/2in1TabletTVWearable

rotate(value: RotateOptions): T

设置组件旋转。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RotateOptions](ts-universal-attributes-transformation.md#rotateoptions对象说明) | 是 | 可使组件在以组件左上角为坐标原点的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中进行旋转（坐标系如下图所示）。其中，(x, y, z）指定一个矢量，作为旋转轴。  旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。  默认值: 在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。  {  centerX: '50%',  centerY: '50%',  centerZ: 0,  perspective: 0  }  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## rotate18+

PhonePC/2in1TabletTVWearable

rotate(options: Optional<RotateOptions>): T

设置组件旋转。与[rotate](ts-universal-attributes-transformation.md#rotate)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[RotateOptions](ts-universal-attributes-transformation.md#rotateoptions对象说明)> | 是 | 可使组件在以组件左上角为坐标原点的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中进行旋转（坐标系如下图所示）。其中，(x, y, z）指定一个矢量，作为旋转轴。  旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。  默认值: 在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。  {  centerX: '50%',  centerY: '50%',  centerZ: 0,  perspective: 0  }  单位：vp  。  当options的值为undefined时，恢复为无旋转效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## rotate20+

PhonePC/2in1TabletTVWearable

rotate(options: Optional<RotateOptions | RotateAngleOptions>): T

设置组件旋转效果。与[rotate](ts-universal-attributes-transformation.md#rotate18)相比，options参数新增了对RotateAngleOptions类型的支持。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[RotateOptions](ts-universal-attributes-transformation.md#rotateoptions对象说明) | [RotateAngleOptions](ts-universal-attributes-transformation.md#rotateangleoptions20对象说明)> | 是 | RotateOptions可使组件在以组件左上角为坐标原点的坐标系中进行旋转（坐标系如下图所示）。其中，(x, y, z）指定一个矢量，作为旋转轴。  旋转轴和旋转中心点都基于[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)设定，组件发生位移时，坐标系不会随之移动。  默认值：在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。  {  centerX: '50%',  centerY: '50%',  centerZ: 0,  perspective: 0  }  RotateAngleOptions可使组件在以组件左上角为坐标原点的坐标系中进行旋转（坐标系如下图所示）。其中，(angleX, angleY, angleZ）指定三个轴方向上的旋转角。  默认值：  {  angleX:0,  angleY:0,  angleZ:0,  centerX: '50%',  centerY: '50%',  centerZ: 0,  perspective: 0  }    当options的值为undefined时，恢复为无旋转效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## translate

PhonePC/2in1TabletTVWearable

translate(value: TranslateOptions): T

设置组件平移。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明) | 是 | 可使组件在以组件左上角为坐标原点的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中进行移动（坐标系如下图所示）。其中，x，y，z的值分别表示在对应轴移动的距离，值为正时表示向对应轴的正向移动，值为负时表示向对应轴的反向移动。移动距离支持数字和字符串（比如'10px'，'10%'）两种类型。  默认值:  {  x: 0,  y: 0,  z: 0  }  单位：vp    **说明：**  z轴方向移动时由于观察点位置不变，z的值接近观察点组件会有放大效果，远离则缩小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## translate18+

PhonePC/2in1TabletTVWearable

translate(translate: Optional<TranslateOptions>): T

设置组件平移。与[translate](ts-universal-attributes-transformation.md#translate)相比，translate参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| translate | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TranslateOptions](ts-universal-attributes-transformation.md#translateoptions对象说明)> | 是 | 可使组件在以组件左上角为坐标原点的[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)中进行移动（坐标系如下图所示）。其中，x，y，z的值分别表示在对应轴移动的距离，值为正时表示向对应轴的正向移动，值为负时表示向对应轴的反向移动。移动距离支持数字和字符串（比如'10px'，'10%'）两种类型。  默认值:  {  x: 0,  y: 0,  z: 0  }  单位：vp    **说明：**  z轴方向移动时由于观察点位置不变，z的值接近观察点组件会有放大效果，远离则缩小。    当translate的值为undefined时，恢复为无平移效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## scale

PhonePC/2in1TabletTVWearable

scale(value: ScaleOptions): T

设置组件缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明) | 是 | 可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1，同时可以通过centerX和centerY设置缩放的中心点。  默认值:  {  x: 1,  y: 1,  z: 1,  centerX:'50%',  centerY:'50%'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## scale18+

PhonePC/2in1TabletTVWearable

scale(options: Optional<ScaleOptions>): T

设置组件缩放。与[scale](ts-universal-attributes-transformation.md#scale)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ScaleOptions](ts-universal-attributes-transformation.md#scaleoptions对象说明)> | 是 | 可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1，同时可以通过centerX和centerY设置缩放的中心点。  默认值:  {  x: 1,  y: 1,  z: 1,  centerX:'50%',  centerY:'50%'  }  当options的值为undefined时，恢复为无缩放效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## transform

PhonePC/2in1TabletTVWearable

transform(value: object): T

可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](ts-universal-attributes-transformation.md#transform3d20)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | object | 是 | 设置当前组件的变换矩阵。object当前仅支持[Matrix4Transit](js-apis-matrix4.md#matrix4transit)矩阵对象类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## transform18+

PhonePC/2in1TabletTVWearable

transform(transform: Optional<object>): T

可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](ts-universal-attributes-transformation.md#transform3d20)接口。与[transform](ts-universal-attributes-transformation.md#transform)相比，transform18+参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | [Optional](ts-universal-attributes-custom-property.md#optionalt)<object> | 是 | 设置当前组件的变换矩阵。object当前仅支持[Matrix4Transit](js-apis-matrix4.md#matrix4transit)矩阵对象类型。  当transform的值为undefined时，恢复为单位矩阵的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## transform3D20+

PhonePC/2in1TabletTVWearable

transform3D(transform: Optional<Matrix4Transit>): T

设置组件的三维变换矩阵。当涉及包含透视效果的三维变换时，transform接口显示效果可能有误，推荐使用transform3D接口。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Matrix4Transit](ts-universal-attributes-transformation.md#matrix4transit20)> | 是 | 三维变换矩阵。  当transform的值为undefined时，恢复为单位矩阵的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## Matrix4Transit20+

PhonePC/2in1TabletTVWearable

type Matrix4Transit = Matrix4Transit

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 单位矩阵对象。 |

## RotateOptions对象说明

PhonePC/2in1TabletTVWearable

组件旋转参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 是 | 旋转轴向量x坐标。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| y | number | 否 | 是 | 旋转轴向量y坐标。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| z | number | 否 | 是 | 旋转轴向量z坐标。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| angle | number | string | 否 | 否 | 旋转角度。取值为正时相对于旋转轴方向顺时针转动，取值为负时相对于旋转轴方向逆时针转动。取值可为string类型，如'90deg'。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| centerX | number | string | 否 | 是 | 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。取值可为string类型，如'50'，'50%'。  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| centerY | number | string | 否 | 是 | 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。取值可为string类型，如'50'，'50%'。  单位：vp  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| centerZ10+ | number | 否 | 是 | z轴锚点，即3D旋转中心点的z轴分量。  默认值：0  单位：px  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| perspective10+ | number | 否 | 是 | 相机放置的z轴坐标。数值大小表示视距，即相机到z=0平面的距离。取值的正负决定了相机观察的方向。当perspective=0，系统会自动计算适合的相机z轴位置，取值为负数。  旋转轴和旋转中心点都基于[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)设定，组件发生位移时，坐标系不会随之移动。  默认值：0  单位：px  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |

## RotateAngleOptions20+对象说明

PhonePC/2in1TabletTVWearable

指定各轴旋转角的旋转参数选项。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| angleX | number | string | 否 | 是 | X轴方向上的旋转角。取值为正时相对于旋转轴方向顺时针转动，取值为负时逆时针转动。取值可为string类型，如'90deg'。  默认值：0  取值范围：(-∞, +∞) |
| angleY | number | string | 否 | 是 | Y轴方向上的旋转角。取值为正时相对于旋转轴方向顺时针转动，取值为负时逆时针转动。取值可为string类型，如'90deg'。  默认值：0  取值范围：(-∞, +∞) |
| angleZ | number | string | 否 | 是 | Z轴方向上的旋转角。取值为正时相对于旋转轴方向顺时针转动，取值为负时逆时针转动。取值可为string类型，如'90deg'。  默认值：0  取值范围：(-∞, +∞) |
| centerX | number | string | 否 | 是 | 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。  单位：vp  默认值：'50%'  取值范围：(-∞, +∞) |
| centerY | number | string | 否 | 是 | 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。  单位：vp  默认值：'50%'  取值范围：(-∞, +∞) |
| centerZ | number | 否 | 是 | z轴锚点，即3D旋转中心点的z轴分量。  默认值：0  单位：px  取值范围：(-∞, +∞) |
| perspective | number | 否 | 是 | 相机放置的z轴坐标。数值大小表示视距，即相机到z=0平面的距离。取值的正负决定了相机观察的方向。当perspective=0，系统会自动计算适合的相机z轴位置，取值为负数。  旋转轴和旋转中心点都基于[组件坐标系](../harmonyos-guides/arkui-glossary.md#组件坐标系)设定，组件发生位移时，坐标系不会随之移动。  默认值：0  单位：px  取值范围：(-∞, +∞) |

## TranslateOptions对象说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | string | 否 | 是 | x轴的平移距离。  类型为number时，单位为vp，取值范围为(-∞, +∞)。  默认值：0  类型为string时，形式参考[Length](ts-types.md#length)的string类型。 |
| y | number | string | 否 | 是 | y轴的平移距离。  类型为number时，单位为vp，取值范围为(-∞, +∞)。  默认值：0  类型为string时，形式参考[Length](ts-types.md#length)的string类型。 |
| z | number | string | 否 | 是 | z轴的平移距离。  类型为number时，单位为vp，取值范围为(-∞, +∞)。  默认值：0  类型为string时，形式参考[Length](ts-types.md#length)的string类型。 |

## ScaleOptions对象说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 是 | x轴的缩放倍数。x>1时以x轴方向放大，0<x<1时以x轴方向缩小，x<0时沿x轴反向并缩放。 |
| y | number | 否 | 是 | y轴的缩放倍数。y>1时以y轴方向放大，0<y<1时以y轴方向缩小，y<0时沿y轴反向并缩放。 |
| z | number | 否 | 是 | z轴的缩放倍数。z>1时以z轴方向放大，0<z<1时以z轴方向缩小，z<0时沿z轴反向并缩放。 |
| centerX | number | string | 否 | 是 | 变换中心点x轴坐标。表示组件变换中心点（即锚点）的x方向坐标。取值可为string类型，如'50'，'50%'。  单位：vp |
| centerY | number | string | 否 | 是 | 变换中心点y轴坐标。表示组件变换中心点（即锚点）的y方向坐标。取值可为string类型，如'50'，'50%'。  单位：vp |

说明

当组件同时设置了[rotate](ts-universal-attributes-transformation.md#rotate)和[scale](ts-universal-attributes-transformation.md#scale)属性时，centerX和centerY的取值会发生冲突，此时centerX和centerY的值以最后设定的属性的值为准。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（为组件添加图形变换效果）

该示例通过[rotate](ts-universal-attributes-transformation.md#rotate)、[translate](ts-universal-attributes-transformation.md#translate)、[scale](ts-universal-attributes-transformation.md#scale)、[transform](ts-universal-attributes-transformation.md#transform)为组件添加旋转、平移、缩放、变换矩阵效果。

```
1. // xxx.ets
2. import { matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TransformExample {
7. build() {
8. Column() {
9. Text('rotate').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
10. Row()
11. .rotate({
12. x: 0,
13. y: 0,
14. z: 1,
15. centerX: '50%',
16. centerY: '50%',
17. angle: 300
18. })// 组件以矢量(0,0,1)为旋转轴，绕中心点顺时针旋转300度
19. .width(100).height(100).backgroundColor(0xAFEEEE)

21. Text('translate').width('90%').fontColor(0xCCCCCC).padding(10).fontSize(14)
22. Row()
23. .translate({ x: 100, y: 10 })// x轴方向平移100，y轴方向平移10
24. .width(100)
25. .height(100)
26. .backgroundColor(0xAFEEEE)
27. .margin({ bottom: 10 })

29. Text('scale').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
30. Row()
31. .scale({ x: 2, y: 0.5 })// 高度缩小一倍，宽度放大一倍，z轴在2D下无效果
32. .width(100).height(100).backgroundColor(0xAFEEEE)

34. Text('Matrix4').width('90%').fontColor(0xCCCCCC).padding(15).fontSize(14)
35. Row()
36. .width(100).height(100).backgroundColor(0xAFEEEE)
37. .transform(matrix4.identity().translate({ x: 50, y: 50 }).scale({ x: 1.5, y: 1 }).rotate({
38. x: 0,
39. y: 0,
40. z: 1,
41. angle: 60
42. }))
43. }.width('100%').margin({ top: 5 })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/wpOe8FlcSp6S0oQeUf_3rA/zh-cn_image_0000002589325897.png?HW-CC-KV=V1&HW-CC-Date=20260429T055117Z&HW-CC-Expire=86400&HW-CC-Sign=8EC60DED6CD730081F5C6EB17A6DAA64BB035AB33294E728272A28748254FEA3)

### 示例2（设置旋转视距）

该示例通过[perspective](ts-universal-attributes-transformation.md#rotateoptions对象说明)为组件添加视距效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State prep: number = 10;

7. build() {
8. Row() {
9. Column() {
10. Stack()
11. .width(100)
12. .height(100)
13. .backgroundColor(Color.Red)
14. .rotate({ y: 1, angle: 45, perspective: this.prep })
15. Button('change prep')
16. .margin({ top: 100 })
17. .onClick(() => {
18. this.getUIContext()?.animateTo({
19. duration: 2000,
20. curve: Curve.EaseIn,
21. iterations: 1,
22. playMode: PlayMode.Normal,
23. onFinish: () => {
24. console.info('play end');
25. }
26. }, () => {
27. this.prep = 500 // 组件视距从10变换到500
28. })
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/uhveTJtvQPOm0hd--gm_nw/zh-cn_image_0000002589245839.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055117Z&HW-CC-Expire=86400&HW-CC-Sign=20F46ED210D8F23EA7132A7F66908ED10F9747D641A2156EFE052A58E42AE90D)

### 示例3（按中心点旋转）

该示例通过设置[rotate](ts-universal-attributes-transformation.md#rotate)和[transform](ts-universal-attributes-transformation.md#transform)为不同的参数实现相同的旋转效果。

```
1. import { matrix4 } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MatrixExample {
6. build() {
7. Column({ space: 100 }) {
8. Text('Hello1')
9. .textAlign(TextAlign.Center)
10. .width(100)
11. .height(60)
12. .backgroundColor(0xAFEEEE)
13. .borderWidth(1)

15. Text('Hello2')
16. .textAlign(TextAlign.Center)
17. .width(100)
18. .height(60)
19. .backgroundColor(0xAFEEEE)
20. .borderWidth(1)
21. .rotate({
22. // 绕(100vp,60vp)的锚点旋转90度，rotate或scale的centerX、centerY为组件锚点
23. z: 1,
24. angle: 90,
25. centerX: 100,
26. centerY: 60
27. })

29. Text('Hello3')
30. .textAlign(TextAlign.Center)
31. .width(100)
32. .height(60)
33. .backgroundColor(0xAFEEEE)
34. .borderWidth(1)
35. .transform(matrix4.identity()
36. .rotate({
37. // 组件锚点(centerX,centerY)默认为(50%,50%)，即锚点在(50vp,30vp)
38. // transform的rotate指定(centerX,centerY)为(50vp,30vp)，相对于在组件本身锚点基础上再额外偏移(50vp,30vp)
39. // 此次变换相当于绕(100vp,60vp)旋转，和"Hello2"实现同样的旋转效果
40. z: 1,
41. angle: 90,
42. centerX: this.getUIContext().vp2px(50),
43. centerY: this.getUIContext().vp2px(30)
44. }))

46. Text('Hello4')
47. .textAlign(TextAlign.Center)
48. .width(100)
49. .height(60)
50. .backgroundColor(0xAFEEEE)
51. .borderWidth(1)
52. .scale({
53. // 当设置x或y时，centerX和centerY才能生效
54. // 设置组件锚点为(100vp,60vp)
55. x: 1,
56. y: 1,
57. centerX: 100,
58. centerY: 60
59. })// transform的rotate不指定centerX、centerY，此次旋转的中心相对于组件本身锚点没有额外偏移
60. // 该组件通过scale设置的锚点，绕(100vp,60vp)进行旋转，和"Hello2"实现同样的旋转效果
61. .transform(matrix4.identity().rotate({ z: 1, angle: 90 }))
62. }.width('100%')
63. .height('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/q0tH7hcQQqeuHu1g6JzwBw/zh-cn_image_0000002558766030.png?HW-CC-KV=V1&HW-CC-Date=20260429T055117Z&HW-CC-Expire=86400&HW-CC-Sign=EEC0CD79F02E631EC174B46D0AEC2F39D11677E9E5EF6A7FB7AD7DA2273D2F5F)

### 示例4（通过transform3D实现图形变换）

从API version 20开始，该示例通过设置[transform3D](ts-universal-attributes-transformation.md#transform3d20)实现图形变换效果。

```
1. import { matrix4 } from '@kit.ArkUI';

3. let matrix: matrix4.Matrix4Transit = matrix4.init([
4. 0.53033, 0, -0.53033, 0.00053033,
5. 0, 0.75, 0, 0,
6. 0.707107, 0, 0.707107, -0.000707107,
7. 0, 0, 0, 1
8. ])

10. @Entry
11. @Component
12. struct Tests {
13. build() {
14. Column() {
15. Stack() {
16. Stack()
17. .width(200)
18. .height(100)
19. .backgroundColor(Color.Grey)
20. Stack()
21. .width(200)
22. .height(100)
23. .backgroundColor(Color.Blue)
24. .transform3D(matrix)
25. }
26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/HzCJrq4VRjCJmzWfA9Xivw/zh-cn_image_0000002558606372.png?HW-CC-KV=V1&HW-CC-Date=20260429T055117Z&HW-CC-Expire=86400&HW-CC-Sign=53397EA645FF05AD5D49A25A0E54213F8AFD0CF01758C1DFBCA12B31E00EAFD6)

### 示例5（按各轴旋转角的方式实现旋转）

从API version 20开始，该示例通过设置rotate的[RotateAngleOptions](ts-universal-attributes-transformation.md#rotateangleoptions20对象说明)参数实现旋转效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. Stack()
9. .width(100)
10. .height(100)
11. .backgroundColor(Color.Blue)
12. .rotate({ angleZ: -45 })
13. Button('rotateAngle')
14. .width("40%")
15. .margin({ top: 100 })
16. .rotate({ angleY: 30, centerX: '90%', perspective: 10 })
17. Image($r("app.media.startIcon"))
18. .width(200)
19. .height(200)
20. .rotate({
21. angleX: 60,
22. angleY: -125,
23. angleZ: 75,
24. centerX: 100,
25. centerZ: 20
26. })
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/iE1jI9RLQXOH_WaaBAnnAg/zh-cn_image_0000002589325899.png?HW-CC-KV=V1&HW-CC-Date=20260429T055117Z&HW-CC-Expire=86400&HW-CC-Sign=23D02E2A8F92C7D8D1355BD985D6AD8EFE31DFC26BB6913AA3573B981B87B063)
