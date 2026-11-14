---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color
title: 前景色设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 前景色设置
category: harmonyos-references
scraped_at: 2026-11-14T08:50:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d7fd68dc1395ecde0f757d48da88137ec8faeb551d5d5bb124cd7d8b78d4fcff
---

设置组件的前景色。与背景色相对应，前景色会影响绘制组件内容的颜色。主要影响文字的颜色、形状绘制组件（如Circle、Rect、Path等）的填充色。

**说明** 

* 从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。

## foregroundColor

foregroundColor(value: ResourceColor | ColoringStrategy): T

设置组件的前景色。当组件未设置前景色时，默认继承父组件的前景色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [ColoringStrategy](ts-appendix-enums.md#coloringstrategy10) | 是 | 设置组件的前景色或者根据智能取色策略设置前景色。使用[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10).INVERT时前景色为背景色的反色，需配合设置[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)。不支持[属性动画](ts-animatorproperty.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## foregroundColor18+

foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T

设置组件的前景色。当组件未设置前景色时，默认沿组件树向上继承祖先组件的前景色。与[foregroundColor](ts-universal-attributes-foreground-color.md#foregroundcolor)相比，color参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor) | [ColoringStrategy](ts-appendix-enums.md#coloringstrategy10)> | 是 | 设置组件的前景色或者根据智能取色策略设置前景色。使用[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10).INVERT时前景色为背景色的反色，需配合设置[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)。不支持[属性动画](ts-animatorproperty.md)。  当color的值为undefined时，若组件之前已设置前景色则维持之前的前景色取值，若组件之前未设置前景色则使用组件默认前景色取值。不同组件的默认前景色取值可能存在差异，建议开发者使用确定颜色或[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## 示例

### 示例1（使用前景色设置）

该示例主要演示通过foregroundColor设置前景色。

```ts
// xxx.ets
@Entry
@Component
struct ForegroundColorExample {
  build() {
    Column({ space: 100 }) {
      // 绘制一个直径为150的圆，默认填充色为黑色
      Circle({ width: 150, height: 200 }).margin(20)
      // 绘制一个直径为150的圆，设置前景色为橙色
      Circle({ width: 150, height: 200 }).foregroundColor(Color.Orange)
    }.width('100%').backgroundColor(Color.Gray)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/toGcGMNcTHiaatOHFICXvw/zh-cn_image_0000002788468688.png?HW-CC-KV=V1&HW-CC-Date=20261114T005005Z&HW-CC-Expire=31536000000&HW-CC-Sign=870714F94C3150B4DD1386FAAFB9D66BC7C6F5BB9A2162ACE351E2E9311FEFA0)

### 示例2（设置前景色为组件背景色反色）

该示例通过[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10).INVERT将前景色设置为背景色反色。

```ts
// xxx.ets
@Entry
@Component
struct ColoringStrategyExample {
  build() {
    Column({ space: 100 }) {
      // 绘制一个直径为150的圆，默认填充色为黑色
      Circle({ width: 150, height: 200 })
      // 绘制一个直径为150的圆，设置前景色为组件背景色的反色
      Circle({ width: 150, height: 200 })
        .backgroundColor(Color.Black)
        .foregroundColor(ColoringStrategy.INVERT)
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/3IkZFt8GQ8WlTIEFLJIOLA/zh-cn_image_0000002817508177.png?HW-CC-KV=V1&HW-CC-Date=20261114T005005Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E3C93C263C526CEE57CD68631F77FD739B2ADB9E7BC5DE54EA76710BB21840E)

### 示例3（前景色未继承父组件）

该示例主要演示组件同时设置前景色和背景色与只设置背景色的效果对比。

```ts
// xxx.ets
@Entry
@Component
struct ForegroundColorInherit {
  build() {
    Column() {
      Button('设置前景色为橙色').fontSize(20).foregroundColor(Color.Orange).backgroundColor(Color.Gray)
      Divider()
      Button('未设置前景色继承自父组件').fontSize(20).backgroundColor(Color.Gray)
    }.foregroundColor(Color.Pink)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/_xp-UUHuR6iMSOCIJgakDQ/zh-cn_image_0000002788308746.png?HW-CC-KV=V1&HW-CC-Date=20261114T005005Z&HW-CC-Expire=31536000000&HW-CC-Sign=739EB51A9E73E5D8A91AD52376ABE18725D983A5EBD4584D8CAC581AABEF1928)
