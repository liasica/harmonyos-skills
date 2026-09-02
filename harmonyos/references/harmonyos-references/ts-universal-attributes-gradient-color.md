---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color
title: 颜色渐变
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 颜色渐变
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6fa20cede353e9cd0d8152fc2b33c0f28fe004ab6c0572d7b290e9554d2bed64
---

设置组件的颜色渐变效果。

**说明** 

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 颜色渐变属于组件内容，绘制在背景上方。
* 颜色渐变不支持宽高显式动画，执行宽高动画时颜色渐变会直接过渡到终点。
* 同一组件上只能设置一种类型的颜色渐变效果（线性渐变、角度渐变或径向渐变），后调用的渐变方法会覆盖之前设置的渐变效果。如需切换渐变类型，应先使用对应方法传入undefined清除原渐变效果后再设置新渐变。

## linearGradient

linearGradient(value: LinearGradientOptions): T

设置组件的线性渐变效果，沿指定方向或角度进行颜色渐变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明) | 是 | 线性渐变的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## linearGradient18+

linearGradient(options: Optional<LinearGradientOptions>): T

设置组件的线性渐变效果，沿指定方向或角度进行颜色渐变。与[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LinearGradientOptions](ts-universal-attributes-gradient-color.md#lineargradientoptions18对象说明)> | 是 | 线性渐变的配置选项。  当options的值为undefined时，恢复为无线性渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## LinearGradientOptions18+对象说明

线性渐变的参数。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| angle7+ | number | string | 否 | 是 | 线性渐变的角度，number类型时单位为度（°）。角度为0度时渐变方向从下往上，顺时针旋转为正向角度。  取值范围：(-∞,+∞)，设置的值大于0时，按顺时针方向，小于0时，按逆时针方向。  默认值：180  角度为字符串时，合法的取值为数字（默认单位为度，即deg）或数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位，例如："90"、 "90deg"、"1.57rad"。传入非法格式的字符串时，按默认值180处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| direction7+ | [GradientDirection](ts-appendix-enums.md#gradientdirection) | 否 | 是 | 线性渐变的方向，设置angle为非undefined后，direction不生效。设置为GradientDirection.None时，按默认方向渐变。默认值：GradientDirection.Bottom。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色和其对应的百分比位置的数组，设置不符合ResourceColor格式要求的颜色值时，该颜色项直接跳过不生效。设置metricsColors时此参数失效。ResourceColor表示颜色，number表示该颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示需要设置渐变色的开始处，1.0表示渐变色的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| repeating7+ | boolean | 否 | 是 | 设置渐变颜色是否在组件范围内循环重复填充。  默认值：false。  true：渐变效果在组件范围内循环重复。  false：渐变效果仅在指定范围内显示一次。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

## sweepGradient

sweepGradient(value: SweepGradientOptions): T

设置组件的角度渐变效果，围绕中心点按角度旋转进行颜色渐变，仅绘制0-360度范围内的角度，超出0-360度范围时不绘制渐变过渡效果，仅以渐变边界处对应的颜色填充（即渐变终止位置对应的颜色）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SweepGradientOptions](ts-universal-attributes-gradient-color.md#sweepgradientoptions18对象说明) | 是 | 角度渐变的配置参数，仅绘制0-360度范围内的角度，超出0-360度范围时不绘制渐变过渡效果，仅以渐变边界处对应的颜色填充。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## sweepGradient18+

sweepGradient(options: Optional<SweepGradientOptions>): T

设置组件的角度渐变效果，围绕中心点按角度旋转进行颜色渐变。与[sweepGradient](ts-universal-attributes-gradient-color.md#sweepgradient)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SweepGradientOptions](ts-universal-attributes-gradient-color.md#sweepgradientoptions18对象说明)> | 是 | 角度渐变的配置选项。仅绘制0-360度范围内的角度，超出0-360度范围时不绘制渐变过渡效果，仅以渐变边界处对应的颜色填充。  当options的值为undefined时，恢复为无角度渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## SweepGradientOptions18+对象说明

角度渐变参数。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center7+ | [[Length](ts-types.md#length), [Length](ts-types.md#length)] | 否 | 否 | 为角度渐变的中心点，即相对于当前组件左上角的坐标，number类型时单位为vp。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| start7+ | number | string | 否 | 是 | 角度渐变的起点。未设置start时，默认值为0，即起始角度为0度。  角度为字符串时，合法的取值为数字（默认单位为度，即deg）或数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。传入非法格式的字符串时，按默认值0处理。取值有0到360度的限制，转换为度的单位之后，值在0到360度之间，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| end7+ | number | string | 否 | 是 | 角度渐变的终点。取值范围：[0, 360]。转换为度的单位之后，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。默认值：0。  角度为字符串时，合法的取值为数字（默认单位为度，即deg）或数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。传入非法格式的字符串时，按默认值0处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| rotation7+ | number | string | 否 | 是 | 角度渐变的旋转角度。未设置rotation时，默认值为0，即不旋转。  角度为字符串时，合法的取值为数字或数字后带"deg"（度）、"rad"（弧度）、"grad"（梯度）、"turn"（圈）单位。例如："90"、 "90deg"、"1.57rad"。传入非法格式的字符串时，按默认值0处理。取值有0到360度的限制，转换为度的单位之后，值在0到360度之间，设置为小于0度的值时，按值为0度处理，设置为大于360度的值时，按值为360度处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色和其对应的百分比位置的数组，设置不符合ResourceColor格式要求的颜色值时，该颜色项直接跳过不生效。设置metricsColors时此参数失效。ResourceColor表示颜色。number表示该颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示需要设置渐变色的开始处，1.0表示渐变色的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| metricsColors20+ | Array<[[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12), number]> | 否 | 是 | 指定渐变颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。当需要使用广色域（如P3色域）颜色时，应使用metricsColors代替colors。设置metricsColors时colors失效。每个渐变ColorMetrics的色域属性应当统一，设置不同色域属性则认为非法。使用广色域（如DISPLAY\_P3）时，需先通过setColorSpace接口将当前窗口设置为广色域。默认不设置，不设置时使用colors参数。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| repeating7+ | boolean | 否 | 是 | 设置渐变颜色是否在组件范围内循环重复填充。  默认值：false。  true：渐变效果在组件范围内循环重复。  false：渐变效果仅在指定范围内显示一次。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

**说明** 

metricsColors参数的约束：

[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)表示填充的颜色，可以使用[colorWithSpace](js-apis-arkui-graphics.md#colorwithspace20)方法构造指定色域属性的颜色。number表示指定颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示当前组件渐变区域的开始处，1.0表示渐变区域的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。

## radialGradient

radialGradient(value: RadialGradientOptions): T

设置组件的径向渐变效果，从中心点向外辐射进行颜色渐变。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明) | 是 | 径向渐变的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## radialGradient18+

radialGradient(options: Optional<RadialGradientOptions>): T

设置组件的径向渐变效果，从中心点向外辐射进行颜色渐变。与[radialGradient](ts-universal-attributes-gradient-color.md#radialgradient)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[RadialGradientOptions](ts-universal-attributes-gradient-color.md#radialgradientoptions18对象说明)> | 是 | 径向渐变的配置选项。  当options的值为undefined时，恢复为无径向渐变的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## RadialGradientOptions18+对象说明

径向渐变参数。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| center7+ | [[Length](ts-types.md#length), [Length](ts-types.md#length)] | 否 | 否 | 径向渐变的中心点，即相对于当前组件左上角的坐标，number类型时单位为vp。第一个元素为x坐标，第二个元素为y坐标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| radius7+ | [Length](ts-types.md#length) | 否 | 否 | 径向渐变的半径，number类型时单位为vp。  取值范围：[0,+∞)。设置的值小于0时，按值为0处理。设置的值为undefined时，系统将根据组件尺寸自动计算渐变半径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| colors7+ | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色和其对应的百分比位置的数组，设置非法颜色直接跳过。ResourceColor表示颜色，number表示该颜色所处的位置，取值范围为[0, 1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示需要设置渐变色的开始处，1.0表示渐变色的结束处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置。如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。  默认值：[]，无渐变效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| repeating7+ | boolean | 否 | 是 | 设置渐变颜色是否在组件范围内循环重复填充。  默认值：false。  true：渐变效果在组件范围内循环重复。  false：渐变效果仅在指定范围内显示一次。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |

**说明** 

colors参数的约束：

[ResourceColor](ts-types.md#resourcecolor)表示填充的颜色，number表示指定颜色所处的位置，取值范围为[0,1.0]，设置的值小于0时，按0处理，设置的值大于1.0时，按1.0处理。0表示当前组件渐变区域的开始处，1.0表示渐变区域的结尾处。为了实现多个颜色渐变效果，多个数组中的number类型参数应递增设置，如果后一个数组中的number类型参数小于前一个数组的number类型参数，将按照等于前一个数组number值处理。

## 示例

### 示例1（颜色线性渐变）

该示例通过[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient)来实现组件的颜色线性渐变。

```ts
// xxx.ets
@Entry
@Component
struct ColorGradientExample {
  build() {
    Column({ space: 5 }) {
      Text('linearGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width('90%')
        .height(50)
        .linearGradient({
          angle: 90,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
      Text('linearGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width('90%')
        .height(50)
        .linearGradient({
          direction: GradientDirection.Left, // 渐变方向
          repeating: true, // 渐变颜色是否重复
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
        })
    }
    .width('100%')
    .padding({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/nzfzzBS2SXqSN2scTO3-oQ/zh-cn_image_0000002706835652.png)

### 示例2（颜色按旋转角度渐变）

该示例通过[sweepGradient](ts-universal-attributes-gradient-color.md#sweepgradient)来实现组件颜色旋转角度渐变。

```ts
// 设置P3色域时需要在ets/entryability/EntryAbility.ets中，通过setColorSpace接口将当前窗口设置为广色域。
import { ColorMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ColorGradientExample {
  @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1, 0, 0, 1);
  @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 1, 0, 1);
  @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0, 1, 1);

  build() {
    Column({ space: 5 }) {
      Text('sweepGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(100)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 359,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
      
      Text('sweepGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(100)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 359,
          rotation: 45, // 旋转角度
          repeating: true, // 渐变颜色是否重复
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
        })

      Text('sweepGradient with metricsColors').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(100)
        .sweepGradient({
          center: [50, 50],
          start: 0,
          end: 359,
          rotation: 45,
          repeating: true,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]], // 数组末尾元素占比小于1时满足重复着色效果
          metricsColors: [[this.p3Red, 0.0], [this.p3Green, 0.5], [this.p3Blue, 1.0]]  // 设置metricsColors时colors设置的颜色失效，metricsColors的颜色生效
        })
    }
    .width('100%')
    .padding({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/J5n9A4ecSCWS-Po0e7Ku6Q/zh-cn_image_0000002736314757.png)

### 示例3（颜色按径向渐变）

该示例通过[radialGradient](ts-universal-attributes-gradient-color.md#radialgradient)来实现组件颜色径向渐变。

```ts
// xxx.ets
@Entry
@Component
struct ColorGradientExample {
  build() {
    Column({ space: 5 }) {
      Text('radialGradient').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(100)
        .radialGradient({
          center: [50, 50],
          radius: 60,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
      Text('radialGradient Repeat').fontSize(12).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(100)
        .radialGradient({
          center: [50, 50],
          radius: 60,
          repeating: true,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]] // 数组末尾元素占比小于1时满足重复着色效果
        })
    }
    .width('100%')
    .padding({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/h6itk_ZxS9iQnJWOF7IVZg/zh-cn_image_0000002706675714.png)
