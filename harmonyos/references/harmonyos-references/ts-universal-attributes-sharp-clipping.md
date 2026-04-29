---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping
title: 形状裁剪
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 形状裁剪
category: harmonyos-references
scraped_at: 2026-04-29T13:51:19+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:ebb80e8c33b1fbe89799639737339239a23a063863ff7089bb78fe72263f5fae
---

用于对组件进行裁剪、遮罩处理。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## clip12+

PhonePC/2in1TabletTVWearable

clip(value: boolean): T

是否对子组件超出当前组件范围外的区域进行裁剪。不设置该接口时，默认不对子组件超出当前组件范围外的区域进行裁剪。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置子组件是否按照当前组件边缘轮廓进行裁剪。  true表示子组件按照当前组件边缘轮廓进行裁剪，false表示不对子组件进行裁剪。  **说明：** 设置为true后，子组件超出当前组件范围外的区域将不响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## clip18+

PhonePC/2in1TabletTVWearable

clip(clip: Optional<boolean>): T

是否对子组件超出当前组件范围外的区域进行裁剪。不设置该接口时，默认不对子组件超出当前组件范围外的区域进行裁剪。与[clip12+](ts-universal-attributes-sharp-clipping.md#clip12)相比，新增了对undefined类型的支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clip | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置子组件是否按照当前组件边缘轮廓进行裁剪。  **说明：** 设置为true后，子组件超出当前组件范围外的区域将不响应绑定的手势事件。  当clip的值为undefined时，恢复为不对子组件超出当前组件范围外的区域进行裁剪。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## clip(deprecated)

PhonePC/2in1TabletTVWearable

clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T

按指定的形状对当前组件进行裁剪。

说明

从API version 7开始支持，从API version 12开始废弃，建议使用[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | [CircleAttribute](ts-drawing-components-circle.md) | [EllipseAttribute](ts-drawing-components-ellipse.md) | [PathAttribute](ts-drawing-components-path.md) | [RectAttribute](ts-drawing-components-rect.md) | 是 | 参数为相应类型的组件，按指定的形状对当前组件进行裁剪；参数为boolean类型时，设置是否按照父容器边缘轮廓进行裁剪。  默认值：false  **说明：** 参数为对应类型的组件时，裁剪不会导致被裁剪区域无法响应绑定的手势事件。参数为boolean类型时，裁剪会导致被裁剪区域无法响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## clipShape12+

PhonePC/2in1TabletTVWearable

clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。

说明

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。

形状中的[fill](js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12) | 是 | 参数为相应类型的组件，按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。  **说明：** 裁剪不会导致被裁剪区域无法响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## clipShape18+

PhonePC/2in1TabletTVWearable

clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。与[clipShape12+](ts-universal-attributes-sharp-clipping.md#clipshape12)相比，新增了对undefined类型的支持。

说明

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。

形状中的[fill](js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12)> | 是 | 参数为相应类型的组件，按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。  **说明：** 裁剪不会导致被裁剪区域无法响应绑定的手势事件。  当shape的值为undefined时，会重置当前值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## CircleShape12+

PhonePC/2in1TabletTVWearable

type CircleShape = CircleShape

导入CircleShape类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [CircleShape](js-apis-arkui-shape.md#circleshape) | 圆形形状。 |

## EllipseShape12+

PhonePC/2in1TabletTVWearable

type EllipseShape = EllipseShape

导入EllipseShape类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [EllipseShape](js-apis-arkui-shape.md#ellipseshape) | 椭圆形状。 |

## PathShape12+

PhonePC/2in1TabletTVWearable

type PathShape = PathShape

导入PathShape类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [PathShape](js-apis-arkui-shape.md#pathshape) | 路径形状。 |

## RectShape12+

PhonePC/2in1TabletTVWearable

type RectShape = RectShape

导入RectShape类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [RectShape](js-apis-arkui-shape.md#rectshape) | 矩形形状。 |

## mask12+

PhonePC/2in1TabletTVWearable

mask(value: ProgressMask): T

为组件上添加可调节进度的遮罩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10) | 是 | 在当前组件上加上可动态设置进度、最大值和颜色的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## mask18+

PhonePC/2in1TabletTVWearable

mask(mask: Optional<ProgressMask>): T

为组件上添加可调节进度的遮罩。与[mask12+](ts-universal-attributes-sharp-clipping.md#mask12)相比，新增了对undefined类型的支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mask | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10)> | 是 | 在当前组件上加上可动态设置进度、最大值和颜色的遮罩。  当mask的值为undefined时，恢复为无进度遮罩效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## mask(deprecated)

PhonePC/2in1TabletTVWearable

mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T

为组件上添加指定形状的遮罩。

说明

从API version 7开始支持，从API version 12开始废弃，建议使用[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleAttribute](ts-drawing-components-circle.md) | [EllipseAttribute](ts-drawing-components-ellipse.md) | [PathAttribute](ts-drawing-components-path.md) | [RectAttribute](ts-drawing-components-rect.md) | [ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10)10+ | 是 | 在当前组件上加上指定形状的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## maskShape12+

PhonePC/2in1TabletTVWearable

maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

为组件上添加指定形状的遮罩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12) | 是 | 在当前组件上加上指定形状的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## maskShape18+

PhonePC/2in1TabletTVWearable

maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

为组件上添加指定形状的遮罩。与[maskShape12+](ts-universal-attributes-sharp-clipping.md#maskshape12)相比，新增了对undefined类型的支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12)> | 是 | 在当前组件上加上指定形状的遮罩。  当shape的值为undefined时，会重置当前值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ProgressMask10+

PhonePC/2in1TabletTVWearable

ProgressMask设置遮罩的进度、最大值和颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor10+

PhonePC/2in1TabletTVWearable

constructor(value: number, total: number, color: ResourceColor)

构造ProgressMask对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 进度遮罩的当前值。  取值范围：[0.0, +∞) |
| total | number | 是 | 进度遮罩的最大值。  取值范围：[0.0, +∞) |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 进度遮罩的颜色。 |

### updateProgress10+

PhonePC/2in1TabletTVWearable

updateProgress(value: number): void

更新进度遮罩的进度值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 进度遮罩的当前值。 |

### updateColor10+

PhonePC/2in1TabletTVWearable

updateColor(value: ResourceColor): void

更新进度遮罩的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 进度遮罩的颜色。 |

### enableBreathingAnimation12+

PhonePC/2in1TabletTVWearable

enableBreathingAnimation(value: boolean): void

进度满时的呼吸光晕动画开关。不设置该接口时，默认关闭呼吸光晕动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启呼吸光晕动画。  true：开启呼吸光晕动画。  false：关闭呼吸光晕动画。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用不同裁剪属性）

该示例通过[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)、[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)实现图片的裁剪和遮罩。

```
1. // xxx.ets
2. import { CircleShape, RectShape } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ClipAndMaskExample {
7. build() {
8. Column({ space: 15 }) {
9. Text('clip').fontSize(12).width('75%').fontColor('#DCDCDC')
10. Row() {
11. // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
12. Image($r('app.media.testImg')).width('500px').height('280px')
13. }
14. .clip(true) // 如这里不设置clip为true，则Row组件的圆角不会限制其中的Image组件，Image组件的四个角会超出Row
15. .borderRadius(20)

17. // 用一个280px直径的圆对图片进行裁剪
18. // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
19. Image($r('app.media.testImg'))
20. .clipShape(new CircleShape({ width: '280px', height: '280px' }))
21. .width('500px').height('280px')

23. Text('mask').fontSize(12).width('75%').fontColor('#DCDCDC')
24. // 给图片添加了一个500px*280px的方形遮罩
25. // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
26. Image($r('app.media.testImg'))
27. .maskShape(new RectShape({ width: '500px', height: '280px' }).fill(Color.Gray))
28. .width('500px').height('280px')

30. // 给图片添加了一个280px*280px的圆形遮罩
31. // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
32. Image($r('app.media.testImg'))
33. .maskShape(new CircleShape({ width: '280px', height: '280px' }).fill(Color.Gray))
34. .width('500px').height('280px')
35. }
36. .width('100%')
37. .margin({ top: 15 })
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/YTJpGID4QFifx9iHeTQDmA/zh-cn_image_0000002558606380.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=F0780711851681F60015DEBFFC3F7411AE402C74F2DD71958B3854D6B811A4B4)

### 示例2（实现组件遮罩）

该示例通过[mask](ts-universal-attributes-sharp-clipping.md#mask12)实现图片的遮罩。

```
1. @Entry
2. @Component
3. struct ProgressMaskExample {
4. @State progressFlag1: boolean = true;
5. @State color: Color = 0x01006CDE;
6. @State value: number = 10.0;
7. @State enableBreathingAnimation: boolean = false;
8. @State progress: ProgressMask = new ProgressMask(10.0, 100.0, Color.Gray);

10. build() {
11. Column({ space: 15 }) {
12. Text('progress mask').fontSize(12).width('75%').fontColor('#DCDCDC')
13. // 给图片添加了一个280px*280px的进度遮罩
14. // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
15. Image($r('app.media.testImg'))
16. .width('500px').height('280px')
17. .mask(this.progress)
18. .animation({
19. duration: 2000, // 动画时长
20. curve: Curve.Linear, // 动画曲线
21. delay: 0, // 动画延迟
22. iterations: 1, // 播放次数
23. playMode: PlayMode.Normal // 动画模式
24. }) // 对Button组件的宽高属性进行动画配置

26. // 更新进度遮罩的进度值
27. Button('updateProgress')
28. .onClick((event?: ClickEvent) => {
29. this.value += 10;
30. this.progress.updateProgress(this.value);
31. }).width(200).height(50).margin(20)

33. // 更新进度遮罩的颜色
34. Button('updateColor')
35. .onClick((event?: ClickEvent) => {
36. if (this.progressFlag1) {
37. this.progress.updateColor(0x9fff0000);
38. } else {
39. this.progress.updateColor(0x9f0000ff);
40. }
41. this.progressFlag1 = !this.progressFlag1
42. }).width(200).height(50).margin(20)

44. // 开关呼吸光晕动画
45. Button('enableBreathingAnimation:' + this.enableBreathingAnimation)
46. .onClick((event?: ClickEvent) => {
47. this.enableBreathingAnimation = !this.enableBreathingAnimation;
48. this.progress.enableBreathingAnimation(this.enableBreathingAnimation);
49. }).width(200).height(50).margin(20)

51. // 恢复进度遮罩
52. Button('click reset!')
53. .onClick((event?: ClickEvent) => {
54. this.value = 0;
55. this.progress.updateProgress(this.value);
56. }).width(200).height(50).margin(20)
57. }
58. .width('100%')
59. .margin({ top: 15 })
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/T_pbstZLQfKAT3oxXbBkiw/zh-cn_image_0000002589325907.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=03256E37CC30D32454E8197C4FC2A59F789E3652E435163A64673E70814287AB)
