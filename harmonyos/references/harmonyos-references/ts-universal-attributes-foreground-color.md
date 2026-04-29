---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color
title: 前景色设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 前景色设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:53875092afa270f71fabdf3059b01506b012dd0d3fa6b2bdccabd85beacf16b4
---

设置组件的前景色。与背景色相对应，前景色会影响绘制组件内容的颜色。主要影响文字的颜色、形状绘制组件的填充色。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## foregroundColor

PhonePC/2in1TabletTVWearable

foregroundColor(value: ResourceColor | ColoringStrategy): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [ColoringStrategy](ts-appendix-enums.md#coloringstrategy10) | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持[属性动画](ts-animatorproperty.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## foregroundColor18+

PhonePC/2in1TabletTVWearable

foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。与[foregroundColor](ts-universal-attributes-foreground-color.md#foregroundcolor)相比，color参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor) | [ColoringStrategy](ts-appendix-enums.md#coloringstrategy10)> | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持属性动画。  当color的值为undefined时，维持之前取值或组件默认取值，具体行为不同组件可能会有差异，建议开发者使用确定颜色或[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用前景色设置）

该示例主要演示通过foregroundColor设置前景色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ForegroundColorExample {
5. build() {
6. Column({ space: 100 }) {
7. // 绘制一个直径为150的圆，默认填充色为黑色
8. Circle({ width: 150, height: 200 }).margin(20)
9. // 绘制一个直径为150的圆，设置前景色为橙色
10. Circle({ width: 150, height: 200 }).foregroundColor(Color.Orange)
11. }.width('100%').backgroundColor(Color.Gray)
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/5V0O7JuoSBOKhA_kyeg7kw/zh-cn_image_0000002589325909.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=014AA268748FC4E40655C2B418363F7AB57BE48BCD70D467D64D6FB163FD72D5)

### 示例2（设置前景色为组件背景色反色）

该示例通过[ColoringStrategy](ts-appendix-enums.md#coloringstrategy10).INVERT将前景色设置为背景色反色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColoringStrategyExample {
5. build() {
6. Column({ space: 100 }) {
7. // 绘制一个直径为150的圆,默认填充色为黑色
8. Circle({ width: 150, height: 200 })
9. // 绘制一个直径为150的圆，设置前景色为组件背景色的反色
10. Circle({ width: 150, height: 200 })
11. .backgroundColor(Color.Black)
12. .foregroundColor(ColoringStrategy.INVERT)
13. }.width('100%')
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/4BwjAlueS2iTDzz6aVPuuw/zh-cn_image_0000002589245851.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=7708A2DC094C20A56A69C4B2A4A72B839DC6ABD919399D3E152087FEBC6E2CE1)

### 示例3（前景色未继承父组件）

该示例主要演示组件同时设置前景色和背景色与只设置背景色的效果对比。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ForegroundColorInherit {
5. build() {
6. Column() {
7. Button('设置前景色为橘色').fontSize(20).foregroundColor(Color.Orange).backgroundColor(Color.Gray)
8. Divider()
9. Button('未设置前景色继承自父组件').fontSize(20).backgroundColor(Color.Gray)
10. }.foregroundColor(Color.Pink)
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/V0tJH74LRJuLPAyzN5GzUg/zh-cn_image_0000002558766042.png?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=56350ADF8F9B6C514CFFBF4B5265C58AAB65F266665B5FAECD70DC4A5E17DF0F)
