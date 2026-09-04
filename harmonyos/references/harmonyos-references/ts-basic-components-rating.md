---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating
title: Rating
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Rating
category: harmonyos-references
scraped_at: 2026-09-05T06:17:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c14d027d797d88ae4de35560ab354749a7a94d17014eb86f5afb8a8de583836b
---

提供在给定范围内选择评分的组件，通常用于商品评价、内容打分等应用场景。

**说明** 

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 当Rating的父节点有指定宽高时，需为Rating组件指定宽高，或为父节点设置值为true的[clip](ts-universal-attributes-sharp-clipping.md#clip18)属性。

## 子组件

无

## 接口

Rating(options?: RatingOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RatingOptions](ts-basic-components-rating.md#ratingoptions18对象说明) | 否 | 设置评分组件。  未设置时，则按照RatingOptions中各参数的默认值配置。 |

## 属性

### stars

stars(value: number)

设置评分总数。默认值：5。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置评分总数。  取值范围：大于0，小于等于0时按5显示。 |

### stars18+

stars(starCount: Optional<number>)

设置评分总数。与[stars](ts-basic-components-rating.md#stars)相比，starCount参数新增了对undefined类型的支持。当starCount的值为undefined时，默认值：5。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| starCount | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 设置评分总数。  取值范围：大于0，小于等于0或undefined时按5显示。 |

### stepSize

stepSize(value: number)

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。默认值：0.5。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 操作评级的步长。  取值范围：[0.1, stars] |

### stepSize18+

stepSize(size: Optional<number>)

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。与[stepSize](ts-basic-components-rating.md#stepsize)相比，size参数新增了对undefined类型的支持。当size的值为undefined时，默认值：0.5。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 操作评级的步长。  当size的值为undefined时，默认值：0.5  取值范围：[0.1, stars] |

### starStyle

starStyle(options: StarStyleOptions)

设置评分的样式。该属性所支持的图片类型能力参考[Image](ts-basic-components-image.md)组件。

支持加载本地图片和网络图片，暂不支持PixelMap类型。

默认图片加载方式为异步，暂不支持同步加载。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StarStyleOptions](ts-basic-components-rating.md#starstyleoptions18对象说明) | 是 | 评分的样式。  **说明：**  当backgroundUri、foregroundUri或secondaryUri设置的图片路径错误时，图片将保持上次的图片显示结果。如果首次设置错误，则不显示图片。  当backgroundUri或foregroundUri设置为undefined或空字符串时，Rating组件将加载系统默认星型图源。  当secondaryUri未设置或设置为undefined或空字符串时，将优先使用backgroundUri，效果等同于仅设置foregroundUri和backgroundUri。 |

### starStyle18+

starStyle(options: Optional<StarStyleOptions>)

设置评分的样式。该属性所支持的图片类型能力参考[Image](ts-basic-components-image.md)组件。

支持加载本地图片和网络图片，暂不支持PixelMap类型。

默认图片加载方式为异步，暂不支持同步加载。

与[starStyle](ts-basic-components-rating.md#starstyle)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[StarStyleOptions](ts-basic-components-rating.md#starstyleoptions18对象说明)> | 是 | 评分的样式。  **说明：**  当backgroundUri、foregroundUri或secondaryUri设置的图片路径错误时，图片将保持上次的图片显示结果。如果首次设置错误，则不显示图片。  当backgroundUri或foregroundUri设置为undefined或空字符串时，Rating组件将加载系统默认星型图源。  当secondaryUri未设置或设置为undefined或空字符串时，将优先使用backgroundUri，效果等同于仅设置foregroundUri和backgroundUri。 |

**说明** 

当Rating组件的宽高为[width, height]时，单个图片的绘制区域为[width / stars, height]。

为确保绘制区域为方形，建议自定义宽高时采用[height \* stars, height]，即width = height \* stars的方式。

### contentModifier12+

contentModifier(modifier: ContentModifier<RatingConfiguration>)

定制Rating内容区的方法。开发者需自定义class实现ContentModifier接口，并在applyContent方法中返回WrappedBuilder，以此重新定义Rating组件内容区的渲染逻辑。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | ContentModifier<[RatingConfiguration](ts-basic-components-rating.md#ratingconfiguration12对象说明)> | 是 | 在Rating组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### contentModifier18+

contentModifier(modifier: Optional<ContentModifier<RatingConfiguration>>)

定制Rating内容区的方法。与[contentModifier](ts-basic-components-rating.md#contentmodifier12)相比，modifier参数新增了对undefined类型的支持。当modifier的值为undefined时，不使用内容修改器。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<ContentModifier<[RatingConfiguration](ts-basic-components-rating.md#ratingconfiguration12对象说明)>> | 是 | 在Rating组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

## 事件

### onChange

onChange(callback:(value: number) => void)

当评分条的评分变化时触发该回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 评分条的评分值。取值范围为[0, stars]，精度受stepSize影响。 |

### onChange18+

onChange(callback:Optional<OnRatingChangeCallback>)

当评分条的评分变化时触发该回调。与[onChange](ts-basic-components-rating.md#onchange)相比，callback参数新增了对undefined类型的支持。当callback的值为undefined时，不使用回调函数。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnRatingChangeCallback](ts-basic-components-rating.md#onratingchangecallback18)> | 是 | 当评分条的评分变化时触发该回调。  当callback的值为undefined时，不使用回调函数。 |

## OnRatingChangeCallback18+

type OnRatingChangeCallback = (rating: number) => void

当评分条的评分变化时触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rating | number | 是 | 评分条的评分值。取值范围为[0, stars]。 |

## 键盘走焦规格

| 按键 | 功能描述 |
| --- | --- |
| Tab | 组件间切换焦点。 |
| 左右方向键 | 评分预览增加/减少（步长为stepSize），不改变实际分值。 |
| Home | 移动到第一个星星，不改变实际分值。 |
| End | 移动到最后一个星星，不改变实际分值。 |
| Space/Enter | 将当前预览的评分值设置为实际评分。 |

## RatingConfiguration12+对象说明

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rating | number | 否 | 否 | 设置并接收评分值。  默认值：0  取值范围： [0, stars]  小于0取0，大于[stars](ts-basic-components-rating.md#stars)的值按[stars](ts-basic-components-rating.md#stars)的值显示。  该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。 |
| indicator | boolean | 否 | 否 | 评分条是否作为指示器使用。当值为true时，表示作为指示器；当值为false时，表示不作为指示器。  默认值：false |
| stars | number | 否 | 否 | 评分条的星级总数。  默认值：5  取值范围：大于0，小于等于0时按默认值显示。  该参数同时定义了rating的最大值与stepSize的最大值。 |
| stepSize | number | 否 | 否 | 评分条的评分步长。  默认值：0.5  取值范围：[0.1, stars] |
| triggerChange | [Callback](ts-types.md#callback12)<number> | 否 | 否 | 触发评分变化的回调，参数为新的评分值。 |

## RatingOptions18+对象说明

评分组件的信息。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rating7+ | number | 否 | 否 | 设置并接收评分值。  默认值：0  取值范围： [0, stars]  小于0取0，大于[stars](ts-basic-components-rating.md#stars)取最大值stars。  该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| indicator7+ | boolean | 否 | 是 | 设置评分组件作为指示器使用。值为true时，作为指示器使用，不可改变评分；值为false时，可进行评分。  默认值：false  **说明：**  indicator=true时，默认组件高度height=12.0vp，组件width=height \* stars。  indicator=false时，默认组件高度height=28.0vp，组件width=height \* stars。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## StarStyleOptions18+对象说明

评分组件选中、未选中以及部分选中的星级样式。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中的星级的图片路径，可由用户自定义或使用系统默认图片。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该字段支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |
| foregroundUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中的星级的图片路径，可由用户自定义或使用系统默认图片。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该字段支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |
| secondaryUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 部分选中的星级的图片路径，可由用户自定义或使用系统默认图片。未设置时将优先使用backgroundUri，效果等同于仅设置foregroundUri和backgroundUri。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该字段支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |

**说明** 

string格式可用于加载网络图片和本地图片，还支持Base64字符串。当使用相对路径引用本地图片时，例如Image("common/test.jpg")，其中common目录与pages同级。

## 示例

### 示例1（设置默认评分样式）

以下示例展示了如何创建默认星型评分样式。

```ts
// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      Column() {
        // 创建评分组件，并设置初始评分与可交互模式
        Rating({ rating: this.rating, indicator: false })
          .stars(5)
          .stepSize(0.5)
          .margin({ top: 24 })
          .onChange((value: number) => {
            this.rating = value;
          })
        Text('current score is ' + this.rating)
          .fontSize(16)
          .fontColor('rgba(24,36,49,0.60)')
          .margin({ top: 16 })
      }.width(360).height(113).backgroundColor('#FFFFFF').margin({ top: 68 })

      Row() {
        Image('common/testImage.jpg')
          .width(40)
          .height(40)
          .borderRadius(20)
          .margin({ left: 24 })
        Column() {
          Text('Yue')
            .fontSize(16)
            .fontColor('#182431')
            .fontWeight(500)
          Row() {
            Rating({ rating: 3.5, indicator: false }).margin({ top: 1, right: 8 })
            Text('2021/06/02')
              .fontSize(10)
              .fontColor('#182431')
          }
        }.margin({ left: 12 }).alignItems(HorizontalAlign.Start)

        Text('1st Floor')
          .fontSize(10)
          .fontColor('#182431')
          .position({ x: 295, y: 8 })
      }.width(360).height(56).backgroundColor('#FFFFFF').margin({ top: 64 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/z8d6AifNQvu37n3_pWmHCw/zh-cn_image_0000002712406086.gif)

### 示例2（自定义评分条）

以下示例实现自定义评分条，其中每个圆圈表示0.5分。ratingIndicator为true时，评分条作为指示器使用，不可改变评分。ratingStars用于设置评分总数，ratingStepSize用于设置评分步长。

```ts
// xxx.ets
// 自定义评分样式类，实现ContentModifier接口，用于定制Rating组件内容区
class MyRatingStyle implements ContentModifier<RatingConfiguration> {
  name: string = "";
  style: number = 0;

  constructor(value1: string, value2: number) {
    this.name = value1;
    this.style = value2;
  }

  applyContent(): WrappedBuilder<[RatingConfiguration]> {
    return wrapBuilder(buildRating);
  }
}

@Builder
function buildRating(config: RatingConfiguration) {
  Column() {
    Row() {
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 0.4 ? Color.Black : Color.Red)
        // 非指示器模式下，根据步长触发对应的评分变化
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(0.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(1);
              return
            }
          }
        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 0.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(1);
          }
        }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 1.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(1.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(2);
              return
            }
          }
        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 1.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(2);
          }
        }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 2.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(2.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(3);
              return
            }
          }
        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 2.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(3);
          }
        }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 3.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(3.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(4);
              return
            }
          }
        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 3.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(4);
          }
        }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden)
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 4.4 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            if (config.stepSize === 0.5) {
              config.triggerChange(4.5);
              return
            }
            if (config.stepSize === 1.0) {
              config.triggerChange(5);
              return
            }
          }
        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
      Circle({ width: 25, height: 25 })
        .fill(config.rating >= 4.9 ? Color.Black : Color.Red)
        .onClick((event: ClickEvent) => {
          if (!config.indicator) {
            config.triggerChange(5);
          }
        }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden)
    }

    Text("分值：" + config.rating)
  }
}

@Entry
@Component
struct RatingExample {
  @State rating: number = 0;
  @State ratingIndicator: boolean = true;
  @State ratingStars: number = 0;
  @State ratingStepSize: number = 0.5;

  build() {
    Row() {
      Column() {
        Rating({
          rating: 0,
          indicator: this.ratingIndicator
        })
          .stepSize(this.ratingStepSize)
          .stars(this.ratingStars)
          .backgroundColor(Color.Transparent)
          .width('100%')
          .height(50)
          .onChange((value: number) => {
            console.info('Rating change is' + value);
            this.rating = value;
          })
          .contentModifier(new MyRatingStyle("hello", 3))
        Button(this.ratingIndicator ? "ratingIndicator : true" : "ratingIndicator : false")
          .onClick((event) => {
            if (this.ratingIndicator) {
              this.ratingIndicator = false;
            } else {
              this.ratingIndicator = true;
            }
          }).margin({ top: 5 })

        Button(this.ratingStars < 5 ? "ratingStars + 1, ratingStars =" + this.ratingStars : "ratingStars最大值为5")
          .onClick((event) => {
            if (this.ratingStars < 5) {
              this.ratingStars += 1;
            }
          }).margin({ top: 5 })

        Button(this.ratingStars > 0 ? "ratingStars - 1, ratingStars =" + this.ratingStars :
          "ratingStars小于等于0时默认等于5")
          .onClick((event) => {
            if (this.ratingStars > 0) {
              this.ratingStars -= 1;
            }
          }).margin({ top: 5 })

        Button(this.ratingStepSize == 0.5 ? "ratingStepSize : 0.5" : "ratingStepSize : 1")
          .onClick((event) => {
            if (this.ratingStepSize == 0.5) {
              this.ratingStepSize = 1;
            } else {
              this.ratingStepSize = 0.5;
            }
          }).margin({ top: 5 })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/SMJqX6jZSiCvfhS3DNtvXQ/zh-cn_image_0000002742125035.gif)

### 示例3（通过Resource资源设置评分的样式）

该示例通过Resource资源配置starStyle，实现自定义星级图片链接，API version 20之后推荐使用该方法设置样式。

```ts
// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      // 创建评分组件，并通过Resource资源设置星级样式
      Rating({ rating: this.rating, indicator: false })
        .stars(5)
        .stepSize(0.5)
        .starStyle({
          // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
          backgroundUri: $r('app.media.image1'),
          foregroundUri: $r('app.media.image2'),
          secondaryUri: $r('app.media.image3')
        })
        .margin({ top: 24 })
        .onChange((value: number) => {
          this.rating = value;
        })
      Text('current score is ' + this.rating)
        .fontSize(16)
        .fontColor('rgba(24,36,49,0.60)')
        .margin({ top: 16 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/_6kS-dRKRoqwgE-DCH9N2A/zh-cn_image_0000002712246128.gif)

### 示例4（设置评分的样式）

以下示例展示了如何通过配置starStyle实现自定义星级的图片链接。

**说明** 

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](../harmonyos-guides/ide-hvigor-build-profile.md#section754823013348)中相关介绍。

```ts
// xxx.ets
@Entry
@Component
struct RatingExample {
  @State rating: number = 3.5;

  build() {
    Column() {
      // 创建评分组件，并通过本地图片路径设置星级样式
      Rating({ rating: this.rating, indicator: false })
        .stars(5)
        .stepSize(0.5)
        .starStyle({
          backgroundUri: '/common/image1.png', // common目录与pages同级
          foregroundUri: '/common/image2.png',
          secondaryUri: '/common/image3.png'
        })
        .margin({ top: 24 })
        .onChange((value: number) => {
          this.rating = value;
        })
      Text('current score is ' + this.rating)
        .fontSize(16)
        .fontColor('rgba(24,36,49,0.60)')
        .margin({ top: 16 })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/t9TO9TwTQsmpWUoZK5DrdA/zh-cn_image_0000002712246128.gif)
