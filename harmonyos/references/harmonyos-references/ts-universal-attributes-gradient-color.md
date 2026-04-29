---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color
title: 颜色渐变
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 颜色渐变
category: harmonyos-references
scraped_at: 2026-04-29T13:51:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cdf33725c665b18ec9c097a188816a9735b2d8ef2ec6b8999c7374923de76e9b
---

设置组件的颜色渐变效果。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 颜色渐变属于组件内容，绘制在背景上方。
* 颜色渐变不支持宽高显式动画，执行宽高动画时颜色渐变会直接过渡到终点。

## linearGradient

PhonePC/2in1TabletTVWearable

linearGradient(value: LinearGradientOptions): T

线性渐变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明) | 是 | 线性渐变。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## linearGradient18+

PhonePC/2in1TabletTVWearable

linearGradient(options: Optional<LinearGradientOptions>): T

线性渐变。与[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明)> | 是 | 线性渐变。  当options的值为undefined时，恢复为无线性渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## LinearGradientOptions18+对象说明

PhonePC/2in1TabletTVWearable

线性渐变的参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| angle7+ | number | string | 否 | 是 | 线性渐变的起始角度。角度为0度时渐变方向为从下往上（即0点方向）。0点方向顺时针旋转为正向角度。  取值范围：(-∞,+∞)，设置的值大于0时，按顺时针方向，小于0时，按逆时针方向。  默认值：180  角度为字符串时，合法的取值为纯数字或纯数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位，例如："90"、 "90deg"、"1.57rad"。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| direction7+ | [GradientDirection](ts-appendix-enums.md#gradientdirection) | 否 | 是 | 线性渐变的方向，设置angle为非undefined后不生效。设置为GradientDirection.None时，按默认方向渐变。默认值：GradientDirection.Bottom。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。ResourceColor表示颜色，number表示该颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示需要设置渐变色的开始处，1.0表示渐变色的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| repeating7+ | boolean | 否 | 是 | 为渐变的颜色重复着色。  默认值：false。  true：允许为渐变的颜色重复着色。  false：不允许为渐变的颜色重复着色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

## sweepGradient

PhonePC/2in1TabletTVWearable

sweepGradient(value: SweepGradientOptions): T

角度渐变。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SweepGradientOptions](ts-universal-attributes-gradient-color.md#sweepgradientoptions18对象说明) | 是 | 角度渐变，仅绘制0-360度范围内的角度，超出时不绘制渐变色，只绘制纯色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sweepGradient18+

PhonePC/2in1TabletTVWearable

sweepGradient(options: Optional<SweepGradientOptions>): T

角度渐变。与[sweepGradient](ts-universal-attributes-gradient-color.md#sweepgradient)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SweepGradientOptions](ts-universal-attributes-gradient-color.md#sweepgradientoptions18对象说明)> | 是 | 角度渐变。  当options的值为undefined时，恢复为无角度渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## SweepGradientOptions18+对象说明

PhonePC/2in1TabletTVWearable

角度渐变参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center7+ | [[Length](ts-types.md#length), Length] | 否 | 否 | 为角度渐变的中心点，即相对于当前组件左上角的坐标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| start7+ | number | string | 否 | 是 | 角度渐变的起点。 默认值：0。  角度为字符串时，合法的取值为纯数字或纯数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。取值有0到360度的限制，转换为度的单位之后，值在0到360度之间，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| end7+ | number | string | 否 | 是 | 角度渐变的终点。 默认值：0。  角度为字符串时，合法的取值为纯数字或纯数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。取值有0到360度的限制，转换为度的单位之后，值在0到360度之间，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| rotation7+ | number | string | 否 | 是 | 角度渐变的旋转角度。默认值：0。  角度为字符串时，合法的取值为纯数字或纯数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。取值有0到360度的限制，转换为度的单位之后，值在0到360度之间，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。ResourceColor表示颜色。number表示该颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示需要设置渐变色的开始处，1.0表示渐变色的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| metricsColors20+ | Array<[[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12), number]> | 否 | 是 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。设置metricsColors时colors失效。每个渐变ColorMetrics的色域属性应当统一，设置不同色域属性则认为非法。默认值为透明色。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| repeating7+ | boolean | 否 | 是 | 为渐变的颜色重复着色。  默认值：false  true：允许为渐变的颜色重复着色。  false：不允许为渐变的颜色重复着色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

说明

metricsColors参数的约束：

[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)表示填充的颜色，可以使用[colorWithSpace](js-apis-arkui-graphics.md#colorwithspace20)方法构造指定色域属性的颜色。number表示指定颜色所处的位置，取值范围为[0, 1.0]，0表示需要设置渐变色的容器开始处，1.0表示容器的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。

## radialGradient

PhonePC/2in1TabletTVWearable

radialGradient(value: RadialGradientOptions): T

径向渐变。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明) | 是 | 径向渐变。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## radialGradient18+

PhonePC/2in1TabletTVWearable

radialGradient(options: Optional<RadialGradientOptions>): T

径向渐变。与[radialGradient](ts-universal-attributes-gradient-color.md#radialgradient)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明)> | 是 | 径向渐变。  当options的值为undefined时，恢复为无径向渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## RadialGradientOptions18+对象说明

PhonePC/2in1TabletTVWearable

径向渐变参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center7+ | [[Length](ts-types.md#length), Length] | 否 | 否 | 径向渐变的中心点，即相对于当前组件左上角的坐标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| radius7+ | [Length](ts-types.md#length) | 否 | 否 | 径向渐变的半径。  取值范围：[0,+∞)。设置的值小于0时，按值为0处理。设置的值为undefined时，系统会自适应渐变半径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| repeating7+ | boolean | 否 | 是 | 为渐变的颜色重复着色。默认值：false。  true：允许为渐变的颜色重复着色。  false：不允许为渐变的颜色重复着色。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

说明

colors参数的约束：

[ResourceColor](ts-types.md#resourcecolor)表示填充的颜色，number表示指定颜色所处的位置，取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，多个数组中number参数建议递增设置，如后一个数组number参数比前一个数组number小的话，按照等于前一个数组number的值处理。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（颜色从右向左线性渐变）

该示例通过[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient)来实现组件的颜色线性渐变。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColorGradientExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('linearGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
8. Row()
9. .width('90%')
10. .height(50)
11. .linearGradient({
12. angle: 90,
13. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
14. })
15. Text('linearGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
16. Row()
17. .width('90%')
18. .height(50)
19. .linearGradient({
20. direction: GradientDirection.Left, // 渐变方向
21. repeating: true, // 渐变颜色是否重复
22. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
23. })
24. }
25. .width('100%')
26. .padding({ top: 5 })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/d-o6xkHaQi-TuA_qAQnO3w/zh-cn_image_0000002589245849.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=302F545D33B446548CAC5C00F8DDF03729BDAF5631EBB8889C58346B005D8FA3)

### 示例2（颜色按旋转角度渐变）

该示例通过[sweepGradient](ts-universal-attributes-gradient-color.md#sweepgradient)来实现组件颜色旋转角度渐变。

```
1. // 设置P3色域时需要在ets/entryability/EntryAbility.ets中，通过setColorSpace接口将当前窗口设置为广色域。
2. import { ColorMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ColorGradientExample {
7. @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1, 0, 0, 1);
8. @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 1, 0, 1);
9. @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0, 1, 1);

11. build() {
12. Column({ space: 5 }) {
13. Text('sweepGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
14. Row()
15. .width(100)
16. .height(100)
17. .sweepGradient({
18. center: [50, 50],
19. start: 0,
20. end: 359,
21. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
22. })

24. Text('sweepGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
25. Row()
26. .width(100)
27. .height(100)
28. .sweepGradient({
29. center: [50, 50],
30. start: 0,
31. end: 359,
32. rotation: 45, // 旋转角度
33. repeating: true, // 渐变颜色是否重复
34. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
35. })

37. Text('sweepGradient with metricsColors').fontSize(12).width('90%').fontColor(0xCCCCCC)
38. Row()
39. .width(100)
40. .height(100)
41. .sweepGradient({
42. center: [50, 50],
43. start: 0,
44. end: 359,
45. rotation: 45,
46. repeating: true,
47. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]], // 数组末尾元素占比小于1时满足重复着色效果
48. metricsColors: [[this.p3Red, 0.0], [this.p3Green, 0.5], [this.p3Blue, 1.0]]  // 设置metricsColors时colors设置的颜色失效，metricsColors的颜色生效
49. })
50. }
51. .width('100%')
52. .padding({ top: 5 })
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/2dDEgzmkSmqLe2ay3tykRA/zh-cn_image_0000002558766040.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=F5E9F7B3B12CCD4A430D6983A737A4DF86CBA92A0FE27DC8E80FFDD1EC620F5C)

### 示例3（颜色按径向渐变）

该示例通过[radialGradient](ts-universal-attributes-gradient-color.md#radialgradient)来实现组件颜色径向渐变。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColorGradientExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('radialGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
8. Row()
9. .width(100)
10. .height(100)
11. .radialGradient({
12. center: [50, 50],
13. radius: 60,
14. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
15. })
16. Text('radialGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
17. Row()
18. .width(100)
19. .height(100)
20. .radialGradient({
21. center: [50, 50],
22. radius: 60,
23. repeating: true,
24. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
25. })
26. }
27. .width('100%')
28. .padding({ top: 5 })
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Zf3zJkmUSFmZzmViOkBPKQ/zh-cn_image_0000002558606382.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=8A89DF142377119814C24777CAB093C77B517148D774417A559BDE54FDDF81EB)
