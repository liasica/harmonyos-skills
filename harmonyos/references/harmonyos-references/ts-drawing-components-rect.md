---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-rect
title: Rect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Rect
category: harmonyos-references
scraped_at: 2026-09-05T06:17:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:891904346af8f1b88459ebc7b263f1f6450fa58a0a91b3b005aca2b3d841d864
---

矩形绘制组件，用于在界面中绘制矩形图形，支持设置填充颜色、边框样式、圆角等属性。

**说明** 

该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

无

## 接口

### Rect

new Rect(options?: RectOptions | RoundedRectOptions)

用于绘制矩形的构造函数。调用后创建一个Rect对象，可设置宽度、高度、圆角等属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectOptions](ts-drawing-components-rect.md#rectoptions18对象说明) | [RoundedRectOptions](ts-drawing-components-rect.md#roundedrectoptions18对象说明) | 否 | Rect绘制属性，包含宽度、高度、圆角等配置。不传入时使用各属性默认值绘制矩形（宽高和圆角均为0）。  异常值undefined和null按照无效值处理，本次设置不生效。 |

### Rect

Rect(options?: RectOptions | RoundedRectOptions)

用于绘制矩形的构造函数。调用后创建一个Rect对象，可设置宽度、高度、圆角等属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectOptions](ts-drawing-components-rect.md#rectoptions18对象说明) | [RoundedRectOptions](ts-drawing-components-rect.md#roundedrectoptions18对象说明) | 否 | Rect绘制属性，包含宽度、高度、圆角等配置。不传入时使用各属性默认值绘制矩形（宽高和圆角均为0）。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## RectOptions18+对象说明

用于描述矩形绘制组件的绘制属性。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radius7+ | [Length](ts-types.md#length) | Array<any> | 否 | 是 | 圆角半径，支持分别设置四个角的圆角半径大小，取值范围≥0。  该属性和radiusWidth/radiusHeight属性效果类似，在组合使用时优先于radiusWidth/radiusHeight生效。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## RoundedRectOptions18+对象说明

用于描述圆角矩形绘制组件的绘制属性。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radiusWidth7+ | [Length](ts-types.md#length) | 否 | 是 | 圆角宽度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radiusHeight7+ | [Length](ts-types.md#length) | 否 | 是 | 圆角高度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)以及[图形绘制通用属性](ts-drawing-components-common.md)外，还支持以下属性：

### radiusWidth

radiusWidth(value: Length)

设置圆角的宽度。仅设置radiusWidth时，圆角的宽度和高度相同。该属性与[radius](ts-drawing-components-rect.md#radius)属性效果类似，当与radius组合使用时，radius属性优先于本属性生效。支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值undefined、null、NaN和Infinity按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆角的宽度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### radiusHeight

radiusHeight(value: Length)

设置圆角的高度。仅设置radiusHeight时，圆角的高度和宽度相同。该属性与[radius](ts-drawing-components-rect.md#radius)属性效果类似，当与radius组合使用时，radius属性优先于本属性生效。支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值undefined、null、NaN和Infinity按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆角的高度，取值范围≥0。  默认值：0  默认单位：vp。  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### radius

radius(value: Length | Array<any>)

设置圆角半径大小，取值范围≥0，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性与[radiusWidth](ts-drawing-components-rect.md#radiuswidth)、[radiusHeight](ts-drawing-components-rect.md#radiusheight)属性效果类似，在组合使用时优先于radiusWidth和radiusHeight生效。异常值undefined、null、NaN和Infinity按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | Array<any> | 是 | 圆角半径大小。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照[[0, 0], [0, 0], [0, 0], [0, 0]]处理。 |

## 示例

### 示例1（组件属性绘制）

使用fill、fillOpacity、stroke、radius属性分别绘制矩形的填充颜色、透明度、边框颜色、圆角。

```ts
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Text('normal').fontSize(11).fontColor(0xCCCCCC).width('90%')
      // 绘制90% * 50的矩形
      Column({ space: 5 }) {
        Text('normal').fontSize(9).fontColor(0xCCCCCC).width('90%')
        // 绘制90% * 50矩形
        Rect({ width: '90%', height: 50 })
          .fill(Color.Pink)
        // 绘制90% * 50的矩形框
        Rect()
          .width('90%')
          .height(50)
          .fillOpacity(0)
          .stroke(Color.Red)
          .strokeWidth(3)

        Text('with rounded corners').fontSize(11).fontColor(0xCCCCCC).width('90%')
        // 绘制90% * 80的矩形, 圆角宽高分别为40、20
        Rect({ width: '90%', height: 80 })
          .radiusHeight(20)
          .radiusWidth(40)
          .fill(Color.Pink)
        // 绘制90% * 80的矩形, 圆角宽高为20
        Rect({ width: '90%', height: 80 })
          .radius(20)
          .fill(Color.Pink)
          .stroke(Color.Transparent)
      }.width('100%').margin({ top: 10 })

      // 绘制90% * 80矩形, 左上圆角宽高40,右上圆角宽高20,右下圆角宽高40,左下圆角宽高20
      Rect({ width: '90%', height: 80 })
        .radius([[40, 40], [20, 20], [40, 40], [20, 20]])
        .fill(Color.Pink)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/glibJCJBTyyJS6031PL5Jw/zh-cn_image_0000002712406336.png)

### 示例2（绘制渐变色矩形）

使用通用属性[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient18)、[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape18)分别绘制渐变色矩形。

从API version 18开始，新增linearGradient、clipShape通用属性。

```ts
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      Column()
        .width(100)
        .height(100)
        .linearGradient({
          direction: GradientDirection.Right,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
        .clipShape(new Rect({ width: 100, height: 100, radius: 40 }))
      Rect()
        .width(100)
        .height(100)
        // 设置矩形填充，如果需要显示背景的渐变色，请设置区域透明度.fillOpacity(0.0)
        .fill(Color.Pink)
        // 设置圆角为40
        .radius(40)
        .stroke(Color.Black)
        // 设置渐变色，仅100*100的矩形区域生效，渐变色的边界不包含倒角
        .linearGradient({
          direction: GradientDirection.Right,
          colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/OoJ39SdXRXKiZvQzkWpOYw/zh-cn_image_0000002712246398.jpeg)

### 示例3（使用不同参数类型绘制矩形）

width、height、radius、radiusWidth、radiusHeight等属性分别使用不同的长度类型绘制图形。

```ts
// xxx.ets
@Entry
@Component
struct RectExample {
  build() {
    Column({ space: 10 }) {
      // 绘制90% * 50矩形，圆角半径为5
      Rect({ width: '90%', height: '50', radius: '5' }) // 使用string类型
        .fill(Color.Green)
      // 绘制200 * 50的矩形框，圆角半径为5
      Rect({ width: 200, height: 50, radius: 5 }) // 使用number类型
        .fillOpacity(0)
        .stroke(Color.Red)
        .strokeWidth(3)
      // 使用Resource类型从资源文件获取尺寸和圆角参数绘制矩形
      Rect({
        width: $r('app.string.RectWidth'), // 使用Resource类型，需用户自定义
        height: $r('app.string.RectHeight'),
        radius: $r('app.string.RectRadius')
      })
        .radiusWidth($r('app.string.RectRadiusWidth'))
        .radiusHeight($r('app.string.RectRadiusHeight'))
        .fill(Color.Green)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/9e2hqUTuSvCFMiS_KmI0QQ/zh-cn_image_0000002742005371.png)

### 示例4（使用attributeModifier动态设置Rect组件的属性）

以下示例展示了如何使用attributeModifier动态设置Rect组件的fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```ts
// xxx.ets
class MyRectModifier implements AttributeModifier<RectAttribute> {
  applyNormalAttribute(instance: RectAttribute): void {
    // 填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框线段长度和间隙长度均为20，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
    instance.fill("#707070")
    instance.fillOpacity(0.5)
    instance.stroke("#2787D9")
    instance.strokeDashArray([20])
    instance.strokeDashOffset("15")
    instance.strokeLineCap(LineCapStyle.Round)
    instance.strokeLineJoin(LineJoinStyle.Miter)
    instance.strokeMiterLimit(5)
    instance.strokeOpacity(0.5)
    instance.strokeWidth(10)
    instance.antiAlias(true)
  }
}

@Entry
@Component
struct RectModifierDemo {
  @State modifier: MyRectModifier = new MyRectModifier()

  build() {
    Column() {
      Rect()
        .width(200)
        .height(200)
        .attributeModifier(this.modifier)
        .offset({ x: 20, y: 20 })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/IF6vaNkCQgqjhJ86m_ESAw/zh-cn_image_0000002712406382.png)
