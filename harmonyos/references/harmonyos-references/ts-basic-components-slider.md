---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider
title: Slider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Slider
category: harmonyos-references
scraped_at: 2026-04-29T13:52:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f814c46e7eb8f830afbeed1a5eb7e6b4d42cc3fc79ac9f6dd863ddc37b6f456e
---

滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Slider(options?: SliderOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SliderOptions](ts-basic-components-slider.md#slideroptions对象说明) | 否 | 配置滑动条的参数。若不传入，则使用SliderOptions中各属性的默认值。 |

## SliderOptions对象说明

PhonePC/2in1TabletTVWearable

滑动条的信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 是 | 当前进度值。  默认值：与属性min的取值一致。  从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  取值范围： [min, max]  小于min时取min，大于max时取max。  $$运算符为系统组件提供TS变量的引用，使得TS变量和slider组件的value值保持同步。详细使用示例请参考[示例7设置滑动条的双向绑定](ts-basic-components-slider.md#示例7设置滑动条的双向绑定)。 |
| min | number | 否 | 是 | 设置最小值。  默认值：0 |
| max | number | 否 | 是 | 设置最大值。  默认值：100  **说明：**  min >= max异常情况，min取默认值0，max取默认值100。  value不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。 |
| step | number | 否 | 是 | 设置Slider滑动步长。  默认值：1  取值范围：[0.01, max - min]  **说明：**  若设置的step值小于0或大于max值，则按默认值显示。 |
| style | [SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明) | 否 | 是 | 设置Slider的滑块与滑轨显示样式。  默认值：SliderStyle.OutSet |
| direction8+ | [Axis](ts-appendix-enums.md#axis) | 否 | 是 | 设置滑动条滑动方向为水平或竖直方向。  默认值：Axis.Horizontal |
| reverse8+ | boolean | 否 | 是 | 设置滑动条取值范围是否反向。  true：横向Slider从右往左滑动，竖向Slider从下往上滑动；false：横向Slider从左往右滑动，竖向Slider从上往下滑动。  默认值：false |

## SliderStyle枚举说明

PhonePC/2in1TabletTVWearable

滑动条滑块在滑轨上显示的样式，具体样式请参考[Slider组件滑块与滑轨是如何对齐的](../harmonyos-guides/arkts-select-component-faq.md#slider组件滑块与滑轨是如何对齐的)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| OutSet | 滑块在滑轨上。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| InSet | 滑块在滑轨内。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NONE12+ | 无滑块  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

说明

* Slider无默认padding。
* 当Slider为水平滑动条时，默认高度为40vp，宽度为父容器的宽度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，左右间距分别为9vp，即为[blockSize](ts-basic-components-slider.md#blocksize10)宽度的一半，当滑动条的style为SliderStyle.InSet时，左右间距分别为6vp，若设置padding，padding不会覆盖左右间距。
* 当Slider为竖直滑动条时，默认宽度为40vp，高度为父容器的高度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，上下间距分别为10vp，当滑动条的style为SliderStyle.InSet时，上下间距分别为6vp，若设置padding，padding不会覆盖上下间距。

## 属性

PhonePC/2in1TabletTVWearable

支持除触摸热区以外的[通用属性](ts-component-general-attributes.md)。

### blockColor

PhonePC/2in1TabletTVWearable

blockColor(value: ResourceColor)

设置滑块的颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 滑块的颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

### blockColor21+

PhonePC/2in1TabletTVWearable

blockColor(value: ResourceColor | LinearGradient)

设置Slider滑块的颜色，支持渐变色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockColor可设置默认圆形滑块颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无填充，设置blockColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockColor可设置自定义形状的填充颜色。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10) | 是 | 滑块的颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

### trackColor

PhonePC/2in1TabletTVWearable

trackColor(value: ResourceColor | LinearGradient)

设置滑轨的背景颜色。

从API version 12开始支持利用LinearGradient设置滑轨的渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [LinearGradient12+](ts-basic-components-datapanel.md#lineargradient10) | 是 | 滑轨的背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_component\_normal')  **说明：**  1. 设置渐变色时，如果颜色断点颜色值为非法值或渐变色断点为空，渐变色将不起效果。  2. 该接口中的LinearGradient类型不支持在元服务中使用。 |

### trackColorMetrics23+

PhonePC/2in1TabletTVWearable

trackColorMetrics(color: ColorMetricsLinearGradient)

设置滑轨轨道的线性渐变背景颜色。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ColorMetricsLinearGradient](ts-basic-components-slider.md#colormetricslineargradient23) | 是 | 滑轨轨道的线性渐变背景颜色。  设置渐变色时，如果color的值为undefined，渐变色设置无效，轨道背景颜色默认取值为：$r('sys.color.ohos\_id\_color\_component\_normal')。 |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置滑轨的已滑动部分颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 滑轨的已滑动部分颜色。  默认值：$r('sys.color.ohos\_id\_color\_emphasize') |

### selectedColor18+

PhonePC/2in1TabletTVWearable

selectedColor(selectedColor: ResourceColor | LinearGradient)

设置滑轨的已滑动部分颜色。与[selectedColor](ts-basic-components-slider.md#selectedcolor)相比，新增了LinearGradient类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedColor | [ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10) | 是 | 滑轨的已滑动部分颜色。  默认值：$r('sys.color.ohos\_id\_color\_emphasize')  **说明：**  设置渐变色时，若颜色断点颜色值为非法值或者渐变色断点为空时，渐变色不起效果。 |

### showSteps

PhonePC/2in1TabletTVWearable

showSteps(value: boolean)

设置当前是否显示步长刻度值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前是否显示步长刻度值。  true：显示刻度值；false：不显示刻度值。  默认值：false |

### showTips

PhonePC/2in1TabletTVWearable

showTips(value: boolean, content?: ResourceStr)

设置滑动时是否显示气泡提示。

当direction的值为Axis.Horizontal时，tip显示在滑块上方，如果上方空间不够，则在下方显示。当值为Axis.Vertical时，tip显示在滑块左边，如果左边空间不够，则在右边显示。当不设置周边边距或者周边边距比较小时，tip会被截断。

tip的绘制区域为Slider自身节点的overlay。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 滑动时是否显示气泡提示。  true：显示气泡；false：不显示气泡。  默认值：false |
| content10+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 气泡提示的文本内容，默认显示当前百分比。 |

### trackThickness8+

PhonePC/2in1TabletTVWearable

trackThickness(value: Length)

设置滑轨的粗细。设置小于等于0的值时，取默认值。

为保证滑块和滑轨的[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明)样式，[blockSize](ts-basic-components-slider.md#blocksize10)跟随trackThickness同比例增减。

当style为[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).OutSet时，trackThickness ：[blockSize](ts-basic-components-slider.md#blocksize10) = 1 ：4，当style为[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).InSet时，trackThickness ：[blockSize](ts-basic-components-slider.md#blocksize10) = 5 ：3。

trackThickness或[blockSize](ts-basic-components-slider.md#blocksize10)的大小超过Slider组件的宽度或高度时，取默认值。

当[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明)设置为OutSet时，尽管trackThickness的大小没超过Slider组件的宽度或高度，但是[blockSize](ts-basic-components-slider.md#blocksize10)超过了，取默认值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 滑轨的粗细。  默认值：当参数style的值设置[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).OutSet 时为 4.0vp，[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).InSet时为20.0vp。 |

### blockBorderColor10+

PhonePC/2in1TabletTVWearable

blockBorderColor(value: ResourceColor)

设置滑块描边颜色。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderColor可设置默认圆形滑块描边颜色。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderColor不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderColor可设置自定义形状中线的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 滑块描边颜色。  默认值：'#00000000' |

### blockBorderWidth10+

PhonePC/2in1TabletTVWearable

blockBorderWidth(value: Length)

设置滑块描边粗细。

当滑块形状设置为SliderBlockType.DEFAULT时，blockBorderWidth可设置默认圆形滑块描边粗细。

当滑块形状设置为SliderBlockType.IMAGE时，滑块无描边，设置blockBorderWidth不生效。

当滑块形状设置为SliderBlockType.SHAPE时，blockBorderWidth可设置自定义形状中线的粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 滑块描边粗细。  **说明：**  设置string类型时，不支持百分比。 |

### stepColor10+

PhonePC/2in1TabletTVWearable

stepColor(value: ResourceColor)

设置刻度颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 刻度颜色。  默认值：  $r('sys.color.ohos\_id\_color\_foreground')混合  $r('sys.color.ohos\_id\_alpha\_normal\_bg')透明度的颜色 |

### trackBorderRadius10+

PhonePC/2in1TabletTVWearable

trackBorderRadius(value: Length)

设置底板圆角半径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 底板圆角半径。  默认值：  style值为SliderStyle.OutSet时默认值为'2vp'。  style值为SliderStyle.InSet时默认值为'10vp'。  **说明：**  设定值小于0时取默认值。 |

### selectedBorderRadius12+

PhonePC/2in1TabletTVWearable

selectedBorderRadius(value: Dimension)

设置已滑动部分（高亮）圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 已选择部分的圆角半径。  默认值：当style值为SliderStyle.InSet或SliderStyle.OutSet时，跟随底板圆角；当style值为SliderStyle.NONE时，为0。  **说明：**  不支持Percentage类型。设定值小于0时取默认值。 |

### blockSize10+

PhonePC/2in1TabletTVWearable

blockSize(value: SizeOptions)

设置滑块大小。

当滑块形状设置为SliderBlockType.DEFAULT时，取宽高的最小值作为圆形半径。

当滑块形状设置为SliderBlockType.IMAGE时，用于设置图片的尺寸大小，图片采用ObjectFit.Cover策略进行缩放。

当滑块形状设置为SliderBlockType.SHAPE时，用于设置自定义形状的大小，自定义形状也会采用ObjectFit.Cover策略进行缩放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | 是 | 滑块大小。  默认值：当参数style的值设置为[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).OutSet时为{width: 18, height: 18}，当参数style的值设置为[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).InSet时为{width: 12, height: 12}，当参数style的值设置为[SliderStyle](ts-basic-components-slider.md#sliderstyle枚举说明).NONE时为，此字段不生效。  当设置的blockSize的宽高值不相等时，取较小值的尺寸，当设置的宽高值中有一个或两个都小于等于0的时候，取默认值。 |

### blockStyle10+

PhonePC/2in1TabletTVWearable

blockStyle(value: SliderBlockStyle)

设置滑块形状参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SliderBlockStyle](ts-basic-components-slider.md#sliderblockstyle10对象说明) | 是 | 滑块形状参数。  默认值：SliderBlockType.DEFAULT，滑块形状为圆形。 |

### stepSize10+

PhonePC/2in1TabletTVWearable

stepSize(value: Length)

设置刻度大小（直径）。当值为0时，刻度点不显示，当值小于0时，取默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 刻度大小（直径）。  默认值：'4vp'  取值范围：[0, [trackThickness](ts-basic-components-slider.md#trackthickness8)) |

### sliderInteractionMode12+

PhonePC/2in1TabletTVWearable

sliderInteractionMode(value: SliderInteraction)

设置用户与滑动条组件交互方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SliderInteraction](ts-basic-components-slider.md#sliderinteraction12枚举说明) | 是 | 用户与滑动条组件交互方式。  默认值：SliderInteraction.SLIDE\_AND\_CLICK。 |

### minResponsiveDistance12+

PhonePC/2in1TabletTVWearable

minResponsiveDistance(value: number)

设置滑动响应的最小距离。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置滑动响应的最小距离，滑动超过此距离后滑块才开始滑动。  默认值：0  **说明：**  单位与[SliderOptions](ts-basic-components-slider.md#slideroptions对象说明)中的属性min以及属性max一致。  当value小于0、大于max-min或非法值时，取默认值。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<SliderConfiguration>)

定制Slider内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md)[<SliderConfiguration>](ts-basic-components-slider.md#sliderconfiguration12对象说明) | 是 | 在Slider组件上，定制内容区的方法。  ContentModifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

说明

* 设置了contentModifier后，自定义区域内点击和手势滑动均不会触发原Slider组件的onChange事件。
* 仅当调用triggerChange函数且传递正确的参数值时，才可以触发原Slider组件的onChange事件。

### slideRange12+

PhonePC/2in1TabletTVWearable

slideRange(value: SlideRange)

设置有效滑动区间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SlideRange](ts-basic-components-slider.md#sliderange12对象说明) | 是 | 设置有效滑动区间 |

### enableHapticFeedback18+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(enabled: boolean)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的[module.json5](../harmonyos-guides/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE"
4. }
5. ]
```

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置是否开启触控反馈。  true：开启触控反馈；false：不开启触控反馈。  默认值：true |

### digitalCrownSensitivity18+

PhonePC/2in1TabletTVWearable

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置旋转表冠的灵敏度。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](ts-universal-attributes-custom-property.md#optionalt)[<CrownSensitivity>](ts-appendix-enums.md#crownsensitivity18) | 是 | 旋转表冠的灵敏度。  默认值：CrownSensitivity.MEDIUM |

### prefix20+

PhonePC/2in1TabletTVWearable

prefix(content: ComponentContent, options?: SliderPrefixOptions)

设置滑动条的前缀。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 自定义组件内容，用于定义滑块前缀的可视化内容，该内容会显示在滑块的起始位置。 |
| options | [SliderPrefixOptions](ts-basic-components-slider.md#sliderprefixoptions20) | 否 | 滑块前缀的配置选项，用于设置与无障碍功能相关的属性。  默认值：null |

### suffix20+

PhonePC/2in1TabletTVWearable

suffix(content: ComponentContent, options?: SliderSuffixOptions)

设置滑动条的后缀。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 自定义组件内容，用于定义滑块后缀的可视化内容，该内容会显示在滑块的结束位置。 |
| options | [SliderSuffixOptions](ts-basic-components-slider.md#slidersuffixoptions20) | 否 | 滑块后缀的配置选项，用于设置与无障碍功能相关的属性。  默认值：null |

### showSteps20+

PhonePC/2in1TabletTVWearable

showSteps(value: boolean, options?: SliderShowStepOptions)

设置当前是否显示步长刻度值。

支持设置每个刻度点的无障碍文本信息，不设置时默认使用当前刻度点的值作为无障碍文本信息。

当显示步长时，设置的刻度点无障碍文本信息生效。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前是否显示步长刻度值。  true：显示刻度值；false：不显示刻度值。  默认值：false |
| options | [SliderShowStepOptions](ts-basic-components-slider.md#slidershowstepoptions20) | 否 | 刻度点无障碍文本的配置选项，用于设置与无障碍功能相关的属性。  默认值：null |

### minLabel(deprecated)

PhonePC/2in1TabletTVWearable

minLabel(value: string)

设置最小值。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用min替代。min是[SliderOptions](ts-basic-components-slider.md#slideroptions对象说明)中的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 最小值。 |

### maxLabel(deprecated)

PhonePC/2in1TabletTVWearable

maxLabel(value: string)

设置最大值。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用max替代。max是[SliderOptions](ts-basic-components-slider.md#slideroptions对象说明)中的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 最大值。 |

## ColorMetricsLinearGradient23+

PhonePC/2in1TabletTVWearable

滑轨轨道的线性渐变背景颜色。

### constructor23+

PhonePC/2in1TabletTVWearable

constructor(colorStops: ColorMetricsStop[])

ColorMetricsLinearGradient的构造函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorStops | [ColorMetricsStop](ts-basic-components-slider.md#colormetricsstop23)[] | 是 | 线性渐变颜色断点数组。每个元素用于描述一个颜色及其在渐变中的断点值。 |

## ColorMetricsStop23+

PhonePC/2in1TabletTVWearable

线性渐变颜色断点类型，用于描述渐进色颜色断点。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 否 | 线性渐变颜色断点的颜色值。 |
| offset | [Length](ts-types.md#length) | 否 | 否 | 线性渐变颜色断点的断点值，取值为0~1之间的比例值，如果数据值小于0则置为0，如果数据值大于1则置为1。  **说明：**  如果传入字符串类型且内容为数字，则转换为对应的数值。例如'10vp'转换为10，'10%'转换为0.1。 |

## SliderCustomContentOptions20+

PhonePC/2in1TabletTVWearable

Slider前后缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessibilityText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 用于提供辅助功能的文本，供屏幕阅读器等工具读取，增强无障碍功能。  默认值："" |
| accessibilityDescription | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 用于提供辅助功能的详细描述，描述滑块前缀或后缀的功能或用途，供屏幕阅读器等工具使用。  默认值为“单指双击即可执行”。 |
| accessibilityLevel | string | 否 | 是 | 用于控制某个组件是否可被无障碍辅助服务所识别。  支持的值为:  "auto"：当前组件会转换为“yes”。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"。 |
| accessibilityGroup | boolean | 否 | 是 | 用于标识该元素是否属于一个无障碍的组，帮助屏幕阅读器等工具将相关元素进行分组处理。  true：该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容；false：不启用无障碍分组。  默认值：false |

## SliderPrefixOptions20+

PhonePC/2in1TabletTVWearable

Slider前缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

提供前缀组件的无障碍信息，继承自[SliderCustomContentOptions](ts-basic-components-slider.md#slidercustomcontentoptions20)。

## SliderSuffixOptions20+

PhonePC/2in1TabletTVWearable

Slider后缀组件无障碍信息参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

提供后缀组件的无障碍信息，继承自[SliderCustomContentOptions](ts-basic-components-slider.md#slidercustomcontentoptions20)。

## SliderStepItemAccessibility20+

PhonePC/2in1TabletTVWearable

Slider刻度点的无障碍文本信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 用于提供辅助功能的文本，供屏幕阅读器等工具读取，增强无障碍功能。  默认值："" |

## SliderShowStepOptions20+

PhonePC/2in1TabletTVWearable

Slider刻度点的无障碍文本信息映射集。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stepsAccessibility | Map<number, [SliderStepItemAccessibility](ts-basic-components-slider.md#sliderstepitemaccessibility20)> | 否 | 是 | 用于设置刻度点提供辅助功能文本，供屏幕阅读器等工具读取，增强无障碍功能。  Key取值范围：[0, INT32\_MAX]，当Key设定为负数和小数时，设定项不生效。  默认值：{} |

## SliderBlockStyle10+对象说明

PhonePC/2in1TabletTVWearable

Slider组件滑块形状参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [SliderBlockType](ts-basic-components-slider.md#sliderblocktype10枚举说明) | 否 | 否 | 设置滑块形状。  默认值：SliderBlockType.DEFAULT，使用圆形滑块。 |
| image | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置滑块图片资源。  图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。 |
| shape | [Circle](ts-drawing-components-circle.md) | [Ellipse](ts-drawing-components-ellipse.md) | [Path](ts-drawing-components-path.md) | [Rect](ts-drawing-components-rect.md) | 否 | 是 | 设置滑块使用的自定义形状。 |

## SliderBlockType10+枚举说明

PhonePC/2in1TabletTVWearable

Slider组件滑块形状枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用默认滑块（圆形）。 |
| IMAGE | 1 | 使用图片资源作为滑块。 |
| SHAPE | 2 | 使用自定义形状作为滑块。 |

## SliderInteraction12+枚举说明

PhonePC/2in1TabletTVWearable

用户与滑动条组件交互方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SLIDE\_AND\_CLICK | 0 | 用户可拖拽滑块或者点击滑轨使滑块移动，鼠标或手指按下即发生移动。 |
| SLIDE\_ONLY | 1 | 禁止用户通过点击滑轨使滑块移动。 |
| SLIDE\_AND\_CLICK\_UP | 2 | 用户可拖拽滑块或者点击滑轨使滑块移动，当鼠标或手指抬起时，若与屏幕按压位置一致，则触发移动。 |

## SlideRange12+对象说明

PhonePC/2in1TabletTVWearable

定义SlideRange中使用的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| from | number | 否 | 是 | 设置有效滑动区间的开始。 |
| to | number | 否 | 是 | 设置有效滑动区间的结束。 |

说明

* 当前仅当min<=from<=to<=max时该接口生效(min和max不依赖于其设置的值，而取决于其实际生效的值)。
* 可只设置from或者to，也可以同时设置from和to。
* 当接口生效且设置的from处于紧邻的step整数倍的值之间，则from实际取左区间step整数倍的那个值或者min作为修正后的值。
* 当接口生效且设置的to处于紧邻的step整数倍的值之间，则to实际取右区间step整数倍的那个值或者MAX作为修正后的值。
* 在from和to取修正值后， 当value是undefined或null时，其取值与from一致; 当value是数值型且value <= from，则取from; 当value > to，则取to。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: (value: number, mode: SliderChangeMode) => void)

Slider拖动或点击时触发事件回调。

Begin和End状态当手势点击时都会触发，Moving和Click状态当value值发生变化时触发。

当连贯动作为拖动动作时，不触发Click状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前滑动进度值，变化范围为对应步长steps数组。若返回值有小数，可使用number.toFixed()方法将数据处理为预期的精度。 |
| mode | [SliderChangeMode](ts-basic-components-slider.md#sliderchangemode枚举说明) | 是 | 事件触发的相关状态值。 |

## SliderChangeMode枚举说明

PhonePC/2in1TabletTVWearable

滑块的状态值。包括按下、拖动、离开以及点击滑动条使滑块位置时。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Begin | 0 | 手势/鼠标接触或者按下滑块。 |
| Moving | 1 | 正在拖动滑块过程中。 |
| End | 2 | 手势/鼠标离开滑块。  **说明：**  异常值恢复成默认值时触发，即value设置小于min或大于max。 |
| Click8+ | 3 | 点击滑动条使滑块位置移动。 |

## SliderConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 当前进度值。 |
| min | number | 否 | 否 | 最小值。 |
| max | number | 否 | 否 | 最大值。 |
| step | number | 否 | 否 | Slider滑动步长。 |
| triggerChange | [SliderTriggerChangeCallback](ts-basic-components-slider.md#slidertriggerchangecallback12) | 否 | 否 | 触发Slider变化。 |

## SliderTriggerChangeCallback12+

PhonePC/2in1TabletTVWearable

type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void

定义SliderConfiguration中使用的回调类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置当前的进度值。  取值范围：[[min](ts-basic-components-slider.md#slideroptions对象说明)-[max](ts-basic-components-slider.md#slideroptions对象说明)] |
| mode | [SliderChangeMode](ts-basic-components-slider.md#sliderchangemode枚举说明) | 是 | 设置事件触发的相关状态值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（滑动条基础样式）

该示例通过配置style、showTips、showSteps控制气泡、刻度值、滑块和滑轨的显示。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SliderExample {
5. @State outSetValueOne: number = 40;
6. @State inSetValueOne: number = 40;
7. @State noneValueOne: number = 40;
8. @State outSetValueTwo: number = 40;
9. @State inSetValueTwo: number = 40;
10. @State vOutSetValueOne: number = 40;
11. @State vInSetValueOne: number = 40;
12. @State vOutSetValueTwo: number = 40;
13. @State vInSetValueTwo: number = 40;

15. build() {
16. Column({ space: 8 }) {
17. Text('outset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
18. Row() {
19. Slider({
20. value: this.outSetValueOne,
21. min: 0,
22. max: 100,
23. style: SliderStyle.OutSet
24. })
25. .showTips(true)
26. .onChange((value: number, mode: SliderChangeMode) => {
27. this.outSetValueOne = value;
28. console.info('value:' + value + 'mode:' + mode.toString());
29. })
30. // toFixed(0)将滑动条返回值处理为整数精度
31. Text(this.outSetValueOne.toFixed(0)).fontSize(12)
32. }
33. .width('80%')
34. Row() {
35. Slider({
36. value: this.outSetValueTwo,
37. step: 10,
38. style: SliderStyle.OutSet
39. })
40. .showSteps(true)
41. .onChange((value: number, mode: SliderChangeMode) => {
42. this.outSetValueTwo = value;
43. console.info('value:' + value + 'mode:' + mode.toString());
44. })
45. Text(this.outSetValueTwo.toFixed(0)).fontSize(12)
46. }
47. .width('80%')

49. Text('inset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
50. Row() {
51. Slider({
52. value: this.inSetValueOne,
53. min: 0,
54. max: 100,
55. style: SliderStyle.InSet
56. })
57. .blockColor('#191970')
58. .trackColor('#ADD8E6')
59. .selectedColor('#4169E1')
60. .showTips(true)
61. .onChange((value: number, mode: SliderChangeMode) => {
62. this.inSetValueOne = value;
63. console.info('value:' + value + 'mode:' + mode.toString());
64. })
65. Text(this.inSetValueOne.toFixed(0)).fontSize(12)
66. }
67. .width('80%')
68. Row() {
69. Slider({
70. value: this.inSetValueTwo,
71. step: 10,
72. style: SliderStyle.InSet
73. })
74. .blockColor('#191970')
75. .trackColor('#ADD8E6')
76. .selectedColor('#4169E1')
77. .showSteps(true)
78. .onChange((value: number, mode: SliderChangeMode) => {
79. this.inSetValueTwo = value;
80. console.info('value:' + value + 'mode:' + mode.toString());
81. })
82. Text(this.inSetValueTwo.toFixed(0)).fontSize(12)
83. }
84. .width('80%')

86. Text('none slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
87. Row() {
88. Slider({
89. value: this.noneValueOne,
90. min: 0,
91. max: 100,
92. style: SliderStyle.NONE
93. })
94. .blockColor('#191970')
95. .trackColor('#ADD8E6')
96. .selectedColor('#4169E1')
97. .showTips(true)
98. .onChange((value: number, mode: SliderChangeMode) => {
99. this.noneValueOne = value;
100. console.info('value:' + value + 'mode:' + mode.toString());
101. })
102. Text(this.noneValueOne.toFixed(0)).fontSize(12)
103. }
104. .width('80%')

106. Row() {
107. Column() {
108. Text('vertical outset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)
109. Row() {
110. Text().width('10%')
111. Slider({
112. value: this.vOutSetValueOne,
113. style: SliderStyle.OutSet,
114. direction: Axis.Vertical
115. })
116. .blockColor('#191970')
117. .trackColor('#ADD8E6')
118. .selectedColor('#4169E1')
119. .showTips(true)
120. .onChange((value: number, mode: SliderChangeMode) => {
121. this.vOutSetValueOne = value;
122. console.info('value:' + value + 'mode:' + mode.toString());
123. })
124. Slider({
125. value: this.vOutSetValueTwo,
126. step: 10,
127. style: SliderStyle.OutSet,
128. direction: Axis.Vertical
129. })
130. .blockColor('#191970')
131. .trackColor('#ADD8E6')
132. .selectedColor('#4169E1')
133. .showSteps(true)
134. .onChange((value: number, mode: SliderChangeMode) => {
135. this.vOutSetValueTwo = value;
136. console.info('value:' + value + 'mode:' + mode.toString());
137. })
138. }
139. }.width('50%').height(300)

141. Column() {
142. Text('vertical inset slider').fontSize(9).fontColor(0xCCCCCC).width('50%').margin(15)
143. Row() {
144. Slider({
145. value: this.vInSetValueOne,
146. style: SliderStyle.InSet,
147. direction: Axis.Vertical,
148. reverse: true // 竖向的Slider默认是上端是min值，下端是max值，因此想要从下往上滑动，需要设置reverse为true
149. })
150. .showTips(true)
151. .onChange((value: number, mode: SliderChangeMode) => {
152. this.vInSetValueOne = value;
153. console.info('value:' + value + 'mode:' + mode.toString());
154. })
155. Slider({
156. value: this.vInSetValueTwo,
157. step: 10,
158. style: SliderStyle.InSet,
159. direction: Axis.Vertical,
160. reverse: true
161. })
162. .showSteps(true)
163. .onChange((value: number, mode: SliderChangeMode) => {
164. this.vInSetValueTwo = value;
165. console.info('value:' + value + 'mode:' + mode.toString());
166. })
167. }
168. }.width('50%').height(300)
169. }
170. }.width('100%')
171. }
172. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Z4o-l-JSR5uD3DL2eBQCTw/zh-cn_image_0000002589326117.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=156BD313D50DF33BF6DF25DB159DEC5AA1A77F3B241EBE40B3CE50C21129F9FE)

### 示例2（设置滑动条样式）

该示例通过blockBorderColor、blockSize、blockBorderWidth、blockStyle设置滑块的样式，通过stepSize、stepColor设置刻度值的样式，通过trackBorderRadius设置底板的圆角，通过selectedBorderRadius设置已滑动部分的圆角。

```
1. @Entry
2. @Component
3. struct SliderExample {
4. @State tipsValue: number = 40;

6. build() {
7. Column({ space: 8 }) {
8. Text('block').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
9. Slider({ style: SliderStyle.OutSet, value: 40 })
10. .blockSize({ width: 40, height: 40 })
11. .blockBorderColor(Color.Red)
12. .blockBorderWidth(5)
13. Divider()
14. Text('step').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
15. Slider({ style: SliderStyle.InSet, value: 40, step: 10 })
16. .showSteps(true)
17. .stepSize(8)
18. .stepColor(Color.Yellow)
19. Divider()
20. Text('track').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
21. Slider({ style: SliderStyle.InSet, value: 40 })
22. .trackBorderRadius(2)
23. Divider()
24. Text('selected').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
25. Slider({ style: SliderStyle.InSet, value: 40 })
26. .selectedBorderRadius(2)
27. Divider()
28. Text('blockStyle').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
29. Slider({ style: SliderStyle.OutSet, value: 40 })
30. .blockStyle({ type: SliderBlockType.DEFAULT })
31. Slider({ style: SliderStyle.OutSet, value: 40 })
32. .blockStyle({ type: SliderBlockType.IMAGE, image: $r('sys.media.ohos_app_icon') })
33. Slider({ style: SliderStyle.OutSet, value: 40 })
34. .blockSize({ width: '60px', height: '60px' })
35. .blockColor(Color.Red)
36. .blockStyle({ type: SliderBlockType.SHAPE, shape: new Path({ commands: 'M60 60 M30 30 L15 56 L45 56 Z' }) })
37. Divider()
38. Text('tips').fontSize(9).fontColor(0xCCCCCC).margin(15).width('90%')
39. Slider({ style: SliderStyle.InSet, value: this.tipsValue })
40. .showTips(true, this.tipsValue.toFixed())
41. .onChange(value => {
42. this.tipsValue = value;
43. })
44. }
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vMM3DZ0MRCCqd7teb9c2Sw/zh-cn_image_0000002589246059.png?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=4F9EEEEE2301638CC64C8D060C0372CFF04B0369BD154086CFDCB5187D1548D4)

### 示例3（自定义滑动条）

该示例实现了Slider组件通过样式Builder定制内容区。点击增加按钮，进度条会按照原Slider设置的步长增加，反之点减少按钮进度条会减少，并触发原组件的onChange事件。

```
1. // xxx.ets

3. @Builder
4. function buildSlider(config: SliderConfiguration) {
5. Row() {
6. Column({ space: 30 }) {
7. Progress({ value: config.value, total: config.max, type: ProgressType.Ring })
8. .margin({ top: 20 })

10. Button('增加')
11. .onClick(() => {
12. config.value = config.value + config.step;
13. config.triggerChange(config.value, SliderChangeMode.Click);
14. })
15. .width(100)
16. .height(25)
17. .fontSize(10)
18. .enabled(config.value < config.max)

20. Button('减少')
21. .onClick(() => {
22. config.value = config.value - config.step;
23. config.triggerChange(config.value, SliderChangeMode.Click);
24. })
25. .width(100)
26. .height(25)
27. .fontSize(10)
28. .enabled(config.value > config.min)

30. Slider({
31. value: config.value,
32. min: config.min,
33. max: config.max,
34. step: config.step,
35. })
36. .width(100)
37. .visibility((config.contentModifier as MySliderStyle).showSlider ? Visibility.Visible : Visibility.Hidden)
38. .showSteps(true)
39. .onChange((value: number, mode: SliderChangeMode) => {
40. config.triggerChange(value, mode);
41. })
42. Text('当前状态：' + ((config.contentModifier as MySliderStyle).sliderChangeMode == 0 ? "Begin"
43. : ((config.contentModifier as MySliderStyle).sliderChangeMode == 1 ? "Moving"
44. : ((config.contentModifier as MySliderStyle).sliderChangeMode == 2 ? "End"
45. : ((config.contentModifier as MySliderStyle).sliderChangeMode == 3 ? "Click" : "无")))))
46. .fontSize(10)
47. Text('进度值：' + config.value)
48. .fontSize(10)
49. Text('最小值：' + config.min)
50. .fontSize(10)
51. Text('最大值：' + config.max)
52. .fontSize(10)
53. Text('步长：' + config.step)
54. .fontSize(10)
55. }
56. .width('80%')

58. }
59. .width('100%')
60. }

62. class MySliderStyle implements ContentModifier<SliderConfiguration> {
63. showSlider: boolean = true;
64. sliderChangeMode: number = 0;

66. constructor(showSlider: boolean, sliderChangeMode: number) {
67. this.showSlider = showSlider;
68. this.sliderChangeMode = sliderChangeMode;
69. }

71. applyContent(): WrappedBuilder<[SliderConfiguration]> {
72. return wrapBuilder(buildSlider);
73. }
74. }

77. @Entry
78. @Component
79. struct SliderExample {
80. @State showSlider: boolean = true;
81. @State sliderValue: number = 0;
82. @State sliderMin: number = 10;
83. @State sliderMax: number = 100;
84. @State sliderStep: number = 20;
85. @State sliderChangeMode: number = 0;

87. build() {
88. Column({ space: 8 }) {

90. Row() {
91. Slider({
92. value: this.sliderValue,
93. min: this.sliderMin,
94. max: this.sliderMax,
95. step: this.sliderStep,
96. })
97. .showSteps(true)
98. .onChange((value: number, mode: SliderChangeMode) => {
99. this.sliderValue = value;
100. this.sliderChangeMode = mode;
101. console.info('SliderLog value:' + value + 'mode:' + mode.toString());
102. })
103. .contentModifier(new MySliderStyle(this.showSlider, this.sliderChangeMode))

105. }
106. .width('100%')

108. }.width('100%')
109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/FWtA1mQcQ12RijJqEEeCTQ/zh-cn_image_0000002558766250.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=D48184D7BECCE5DBE5C6178A409C876CD89B362140639B1849915F350A332F9B)

### 示例4（设置滑动条渐变色）

该示例通过colorGradient设置滑动条渐变色，通过focusable、defaultFocus和focusOnTouch设置滑动条支持表冠操作。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SliderExample {
5. @State inSetValueOne: number = 60
6. @State colorGradient: LinearGradient = new LinearGradient([{ color: "#FF0000FF", offset: 0 }, { color: "#FFFF0000", offset: 1 }])
7. @State sensitivity: CrownSensitivity | undefined | null = CrownSensitivity.MEDIUM
8. scroller: Scroller = new Scroller()

10. getIntegerDigits(num: number): string {
11. let numRound = Math.round(num);
12. return numRound.toString();
13. }

15. build() {
16. Column() {
17. Scroll(this.scroller){
18. Column() {
19. Row() {
20. Stack({ alignContent: Alignment.Top }) {
21. Slider({
22. value: this.inSetValueOne,
23. min: 0,
24. max: 100,
25. style: SliderStyle.NONE,
26. direction: Axis.Vertical,
27. reverse: true
28. })
29. .focusable(true)
30. .defaultFocus(true)
31. .focusOnTouch(true)
32. .digitalCrownSensitivity(this.sensitivity)
33. .trackColor("#26FFFFFF")
34. .trackThickness(52)
35. .selectedColor(this.colorGradient)
36. .onChange((value: number, mode: SliderChangeMode) => {
37. this.inSetValueOne = value
38. })
39. }
40. .height(233 - 66)
41. .width(52)
42. .margin({ top: 33, bottom: 33, left: 56 })
43. Column() {
44. Text('音量')
45. .fontSize(19)
46. .fontColor("#A9FFFFFF")
47. .fontWeight(500)
48. .textAlign(TextAlign.Start)
49. .margin({ left: 20 })
50. Row() {
51. Text(this.getIntegerDigits(this.inSetValueOne))
52. .fontSize(52)
53. .fontColor("#FFFFFFFF")
54. .fontWeight(700)
55. .textAlign(TextAlign.Start)
56. .margin({ left: 20 })
57. Text('%')
58. .fontSize(19)
59. .fontColor("#FFFFFFFF")
60. .fontWeight(500)
61. .textAlign(TextAlign.Start)
62. .margin({ left: 2 })
63. }
64. }.alignItems(HorizontalAlign.Start)
65. }
66. .width(233)
67. .height(233)
68. .borderRadius(116.5)
69. .backgroundColor(Color.Black)
70. }
71. }
72. }.width('100%')
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/fQIHYEtWT72PtH2GK2AaXQ/zh-cn_image_0000002558606592.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=B99A2E61CA7AEB08628F7172F748CBDF3166639BFE627BC12816566DCFEB247E)

### 示例5（滑动条设置前后缀内容）

该示例实现了Slider组件通过prefix、suffix属性设置滑动条的前后缀内容，定制其内容区以及无障碍属性。设置无障碍属性后，屏幕阅读器将以设置的无障碍内容进行朗读。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. class NodeParams {
5. param: ResourceStr = ""

7. constructor(param: ResourceStr) {
8. this.param = param;
9. }
10. }

12. @Builder
13. function textBuilder(params: NodeParams) {
14. Text(params.param)
15. .fontSize($r('sys.float.Caption_L'))
16. .clip(true)
17. .textAlign(TextAlign.Center)
18. .fontColor(Color.Black)
19. }

21. @Entry
22. @Component
23. struct SliderExample {
24. private pre: string = '低';
25. private suf: string = '高';
26. private uiContext: UIContext = this.getUIContext();

28. private preNode1: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
29. private sufNode1: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
30. private preNode2: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
31. private sufNode2: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
32. private preNode3: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
33. private sufNode3: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
34. private preNode4: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
35. private sufNode4: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
36. private preNode5: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
37. private sufNode5: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));
38. private preNode6: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.pre));
39. private sufNode6: ComponentContent<NodeParams> = new ComponentContent(this.uiContext, wrapBuilder(textBuilder), new NodeParams(this.suf));

41. build() {
42. Column({ space: 8 }) {
43. Text('outset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
44. Row() {
45. Slider({
46. value: 50,
47. min: 0,
48. max: 100,
49. style: SliderStyle.OutSet
50. })
51. .showTips(true)
52. .prefix(this.preNode1)
53. .suffix(this.sufNode1)
54. }
55. .width('80%')

57. Row() {
58. Slider({
59. value: 50,
60. min: 0,
61. max: 100,
62. style: SliderStyle.OutSet
63. })
64. .showTips(true)
65. .prefix(this.preNode3)
66. }
67. .width('80%')

69. Row() {
70. Slider({
71. value: 50,
72. min: 0,
73. max: 100,
74. style: SliderStyle.OutSet
75. })
76. .showTips(true)
77. .suffix(this.sufNode3)
78. }
79. .width('80%')

81. Text('inset slider').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
82. Row() {
83. Slider({
84. value: 50,
85. min: 0,
86. max: 100,
87. style: SliderStyle.InSet
88. })
89. .blockColor('#191970')
90. .trackColor('#ADD8E6')
91. .selectedColor('#4169E1')
92. .showTips(true)
93. .trackThickness(36)
94. .prefix(this.preNode2)
95. .suffix(this.sufNode2)
96. }
97. .width('80%')

99. Row() {
100. Slider({
101. value: 50,
102. min: 0,
103. max: 100,
104. style: SliderStyle.InSet
105. })
106. .blockColor('#191970')
107. .trackColor('#ADD8E6')
108. .selectedColor('#4169E1')
109. .showTips(true)
110. .trackThickness(36)
111. .prefix(this.preNode4)
112. }
113. .width('80%')

115. Row() {
116. Slider({
117. value: 50,
118. min: 0,
119. max: 100,
120. style: SliderStyle.InSet
121. })
122. .blockColor('#191970')
123. .trackColor('#ADD8E6')
124. .selectedColor('#4169E1')
125. .showTips(true)
126. .trackThickness(36)
127. .suffix(this.sufNode4)
128. }
129. .width('80%')

131. Text('slider Show Step').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(15)
132. Row() {
133. Slider({
134. value: 50,
135. min: 0,
136. max: 100,
137. step:10,
138. style: SliderStyle.InSet
139. })
140. .blockColor('#191970')
141. .trackColor('#ADD8E6')
142. .selectedColor('#4169E1')
143. .showTips(true)
144. .trackThickness(36)
145. .showSteps(true)
146. .prefix(this.preNode5, {
147. accessibilityText: 'prefixText',
148. accessibilityDescription: 'prefixDescription',
149. accessibilityLevel: 'auto',
150. accessibilityGroup: true
151. })
152. .suffix(this.sufNode5, {
153. accessibilityText: 'suffixText',
154. accessibilityDescription: 'suffixDescription',
155. accessibilityLevel: 'auto',
156. accessibilityGroup: true
157. })
158. }
159. .width('80%')

161. Row() {
162. Slider({
163. value: 50,
164. min: 0,
165. max: 100,
166. step:10,
167. style: SliderStyle.InSet
168. })
169. .blockColor('#191970')
170. .trackColor('#ADD8E6')
171. .selectedColor('#4169E1')
172. .showTips(true)
173. .trackThickness(36)
174. .showSteps(true)
175. .prefix(this.preNode6, {
176. accessibilityText: 'prefixText',
177. accessibilityDescription: 'prefixDescription',
178. accessibilityLevel: 'auto',
179. accessibilityGroup: true
180. })
181. }
182. .width('80%')

184. Row() {
185. Slider({
186. value: 50,
187. min: 0,
188. max: 100,
189. step:10,
190. style: SliderStyle.InSet
191. })
192. .blockColor('#191970')
193. .trackColor('#ADD8E6')
194. .selectedColor('#4169E1')
195. .showTips(true)
196. .trackThickness(36)
197. .showSteps(true)
198. .suffix(this.sufNode6, {
199. accessibilityText: 'suffixText',
200. accessibilityDescription: 'suffixDescription',
201. accessibilityLevel: 'auto',
202. accessibilityGroup: true
203. })
204. }
205. .width('80%')
206. }.width('100%')
207. }
208. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/bX5LM3VuQNu2TQlpXJTlPQ/zh-cn_image_0000002589326119.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=130919A3BA847A769975399347B86ADDBDED3AAB158C0C5FE8C4B78E6688DB28)

### 示例6（滑动条设置刻度点无障碍文本）

该示例实现了Slider组件通过[showSteps](ts-basic-components-slider.md#showsteps20)属性设置刻度点的无障碍文本信息。设置后，屏幕阅读器将以设置的无障碍内容进行朗读。从API version 20开始，新增[showSteps](ts-basic-components-slider.md#showsteps20)属性。

```
1. class SliderBlockBorderColorModifier1 implements AttributeModifier<SliderAttribute>{
2. optionMaps:Map<number, SliderStepItemAccessibility> = new Map()
3. .set(1, {text : '123123'})
4. .set(2, {text : 'Slider无障碍文本'})
5. .set(3, {text : $r('app.string.stepItemText')})
6. .set(4, {text : '!@#$%^&*()'});
7. applyNormalAttribute(instance: SliderAttribute): void {
8. instance.showSteps(true, {stepsAccessibility: this.optionMaps})
9. }
10. }
11. @Entry
12. @Component
13. struct SliderExample {
14. @State show: boolean = true;
15. @State optionMaps:Map<number, SliderStepItemAccessibility> = new Map();
16. private  sliderModifier: SliderBlockBorderColorModifier1 =new SliderBlockBorderColorModifier1()
17. aboutToAppear(){
18. this.optionMaps.set(1, {text : '123123'})
19. this.optionMaps.set(2, {text : 'Slider无障碍文本'})
20. this.optionMaps.set(3, {text : $r('app.string.app_name')})
21. this.optionMaps.set(4, {text : '!@#$%^&*()'})
22. this.show = true;
23. }
24. build() {
25. Column({ space: 8 }) {
26. Text('This is an example for showSteps attribute').fontSize(15).fontColor(0x000000).margin(15).width('90%')
27. Row() {
28. Slider({
29. style: SliderStyle.InSet,
30. value: 20,
31. step: 10,
32. max: 50,
33. min: 0,
34. direction: Axis.Horizontal
35. })
36. .stepSize(8)
37. .stepColor(Color.Yellow)
38. .showSteps(true, {stepsAccessibility: this.optionMaps})
39. }.width('80%').height(100)
40. Divider()
41. Text('This is an example for showSteps attribute with modifier').fontSize(15).fontColor(0x000000).margin(15)
42. .width('90%')
43. Row() {
44. Slider({
45. style: SliderStyle.InSet,
46. value: 20,
47. step: 10,
48. max: 50,
49. min: 0,
50. direction: Axis.Horizontal
51. })
52. .stepSize(8)
53. .stepColor(Color.Yellow)
54. .attributeModifier(this.sliderModifier)
55. }.width('80%').height(100)
56. Divider()
57. }
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/GymUn7dyREasww9vNrXzPw/zh-cn_image_0000002589246061.png?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=91C1A3355CD938EE7697711F06DC2B1044DDB28F6FF508221033D53A6868F8CB)

### 示例7（设置滑动条的双向绑定）

从API version 11开始，通过将[SliderOptions](ts-basic-components-slider.md#slideroptions对象说明)的value属性设置为[$$](../harmonyos-guides/arkts-two-way-sync.md)绑定的变量，实现数据同步。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SliderExample {
5. @State valueWith$: number = 40
6. @State valueWithout$: number = 40
7. build() {
8. Column({ space: 20 }) {
9. Text("使用$$双向绑定: " + this.valueWith$)
10. Slider({
11. value: $$this.valueWith$,
12. min: 0,
13. max: 100,
14. })

16. Text("不使用$$双向绑定: " + this.valueWithout$)
17. Slider({
18. value: this.valueWithout$,
19. min: 0,
20. max: 100,
21. })
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/THA_W4ukTAOj66dTxhPckA/zh-cn_image_0000002558766252.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=34D3F0F23B76FC0E23012EDA10221E3F5FCC03490DCD0E0E078036291ADDB886)

### 示例8（滑块设置渐变色）

该示例实现了Slider组件通过blockColor属性设置滑块渐变色。

```
1. @Entry
2. @Component
3. struct SliderExample {
4. @State colorGradient: LinearGradient = new LinearGradient([{ color: "#FFFFFF", offset: 0 }, { color: "#007DFF", offset: 1 }])

6. build() {
7. Column({ space: 10 }) {
8. Slider({
9. style:SliderStyle.OutSet,
10. min: 0,
11. max: 100,
12. })
13. .blockColor(this.colorGradient)
14. .blockSize({width:"50vp",height:"50vp"})
15. Slider({
16. style:SliderStyle.OutSet,
17. min: 0,
18. max: 100,
19. reverse: true
20. })
21. .blockColor(this.colorGradient)
22. .blockSize({width:"50vp",height:"50vp"})
23. Slider({
24. style:SliderStyle.InSet,
25. min: 0,
26. max: 100,
27. })
28. .blockColor(this.colorGradient)
29. .blockSize({width:"50vp",height:"50vp"})
30. Slider({
31. style:SliderStyle.InSet,
32. min: 0,
33. max: 100,
34. reverse: true
35. })
36. .blockColor(this.colorGradient)
37. .blockSize({width:"50vp",height:"50vp"})
38. Slider({
39. style:SliderStyle.NONE,
40. min: 0,
41. max: 100,
42. })
43. .blockColor(this.colorGradient)
44. .blockSize({width:"50vp",height:"50vp"})
45. Slider({
46. style:SliderStyle.NONE,
47. min: 0,
48. max: 100,
49. reverse: true
50. })
51. .blockColor(this.colorGradient)
52. .blockSize({width:"50vp",height:"50vp"})

54. Row({ space: 20 }){
55. Slider({
56. style:SliderStyle.OutSet,
57. min: 0,
58. max: 100,
59. direction:Axis.Vertical
60. })
61. .blockColor(this.colorGradient)
62. .blockSize({width:"50vp",height:"50vp"})
63. Slider({
64. style:SliderStyle.OutSet,
65. min: 0,
66. max: 100,
67. reverse: true,
68. direction:Axis.Vertical
69. })
70. .blockColor(this.colorGradient)
71. .blockSize({width:"50vp",height:"50vp"})
72. Slider({
73. style:SliderStyle.InSet,
74. min: 0,
75. max: 100,
76. direction:Axis.Vertical
77. })
78. .blockColor(this.colorGradient)
79. .blockSize({width:"50vp",height:"50vp"})
80. Slider({
81. style:SliderStyle.InSet,
82. min: 0,
83. max: 100,
84. reverse: true,
85. direction:Axis.Vertical
86. })
87. .blockColor(this.colorGradient)
88. .blockSize({width:"50vp",height:"50vp"})
89. Slider({
90. style:SliderStyle.NONE,
91. min: 0,
92. max: 100,
93. direction:Axis.Vertical
94. })
95. .blockColor(this.colorGradient)
96. .blockSize({width:"50vp",height:"50vp"})
97. Slider({
98. style:SliderStyle.NONE,
99. min: 0,
100. max: 100,
101. reverse: true,
102. direction:Axis.Vertical
103. })
104. .blockColor(this.colorGradient)
105. .blockSize({width:"50vp",height:"50vp"})
106. }.height("50%")
107. }.width("100%")

109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/tlX3MQmrSPaCJ4IIb29w_A/zh-cn_image_0000002558606594.png?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=4B4026B074358F522F2ED1E68DB126243262AC2549629DBC9EC7C25CD1EC707B)

### 示例9（设置滑轨的背景颜色）

该示例通过[trackColorMetrics](ts-basic-components-slider.md#trackcolormetrics23)设置指定色域的渐变断点值，包括偏移和颜色。示例中的colorSpace使用了ColorSpace.DISPLAY\_P3类型，需要对应窗口调用setWindowColorSpace接口，将当前窗口设置为广色域模式，设置窗口色域模式为广色域参照方法[setWindowColorSpace](arkts-apis-window-window.md#setwindowcolorspace9)。

从API version 23开始，新增trackColorMetrics接口。

```
1. // xxx.ets
2. import { ColorMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SliderExample {
7. @State greenColor: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.0, 1.0, 0.0, 1);
8. @State yellowColor: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 1.0, 0.0, 1);
9. @State inSetValueOne: number = 40;
10. @State color: ColorMetricsLinearGradient =
11. new ColorMetricsLinearGradient([{ color: this.greenColor, offset: 0 }, { color: this.yellowColor, offset: 1 }])

13. build() {
14. Column({ space: 8 }) {
15. Slider({
16. value: this.inSetValueOne,
17. min: 0,
18. max: 100,
19. style: SliderStyle.InSet
20. }).margin('10')
21. .width('80%')
22. .blockColor('#FF0000')
23. .trackColorMetrics(this.color)
24. .selectedColor('#4169E1')
25. .showTips(true)
26. .onChange((value: number, mode: SliderChangeMode) => {
27. this.inSetValueOne = value;
28. console.info('value:' + value + 'mode:' + mode.toString());
29. })
30. }.alignItems(HorizontalAlign.Center)
31. .width('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/imeGKUkgTsONFDFhUU9wSQ/zh-cn_image_0000002589326121.png?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=51CE97F4D22F0DE6A0497185FE8AB2CBF5578C06F1259F021359B6D41F2E24C6)
