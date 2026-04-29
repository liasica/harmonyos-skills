---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row
title: Row
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 行列与堆叠 > Row
category: harmonyos-references
scraped_at: 2026-04-29T13:51:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7a3e13b028e6dcd4b8fc717161e269f22b93aced1ad3a818ea51139878b839c
---

沿水平方向布局的容器。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

Row未设置宽度或高度时，在主轴或交叉轴方向上自适应子组件大小。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

### Row

PhonePC/2in1TabletTVWearable

Row(options?: RowOptions)

创建水平方向线性布局容器，可以设置子组件的间距。

说明

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](../best-practices/bpta-improve-layout-performance.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options18+ | [RowOptions](ts-container-row.md#rowoptions18对象说明) | 否 | 横向布局元素间距，支持设置number或string类型。 |

### Row18+

PhonePC/2in1TabletTVWearable

Row(options?: RowOptions | RowOptionsV2)

创建水平方向线性布局容器，可以设置子组件的间距。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RowOptions](ts-container-row.md#rowoptions18对象说明) | [RowOptionsV2](ts-container-row.md#rowoptionsv218对象说明) | 否 | 横向布局元素间距，支持设置number、string或Resource类型。 |

## RowOptions18+对象说明

PhonePC/2in1TabletTVWearable

设置Row组件的子组件间距属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| space7+ | string | number | 否 | 是 | 横向布局元素间距。  从API version 9开始，space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。  默认值：0  单位：vp  非法值：按默认值处理。  **说明：**  space取值是大于等于0的数字，或者可以转换为数字的字符串。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## RowOptionsV218+对象说明

PhonePC/2in1TabletTVWearable

设置Row组件的子组件间距属性。间距类型SpaceType支持number、string或Resource类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| space | [SpaceType](ts-container-column.md#spacetype18) | 否 | 是 | 横向布局元素间距。  space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。  默认值：0  单位：vp  非法值：按默认值处理。  **说明：**  space取值是大于等于0的数字，或者可以转换为数字的字符串，或者可以转换为数字的Resource类型数据。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### alignItems

PhonePC/2in1TabletTVWearable

alignItems(value: VerticalAlign)

设置子组件在垂直方向上的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [VerticalAlign](ts-appendix-enums.md#verticalalign) | 是 | 子组件在垂直方向上的对齐格式。  默认值：VerticalAlign.Center |

### justifyContent8+

PhonePC/2in1TabletTVWearable

justifyContent(value: FlexAlign)

设置子组件在水平方向上的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexAlign](ts-appendix-enums.md#flexalign) | 是 | 子组件在水平方向上的对齐格式。  默认值：FlexAlign.Start |

说明

Row布局时若子组件不设置[flexShrink](ts-universal-attributes-flex-layout.md#flexshrink)则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴，此时FlexAlign.Center和FlexAlign.End会失效。

### reverse12+

PhonePC/2in1TabletTVWearable

reverse(isReversed: Optional<boolean>)

设置子组件在水平方向上的排列是否反转。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isReversed | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 子组件在水平方向上的排列是否反转。  默认值：true，设置true表示子组件在水平方向上反转排列，设置false表示子组件在水平方向上正序排列。 |

说明

若未设置reverse属性，主轴方向不反转；若设置了reverse属性，且参数值为undefined，则视为默认值true，主轴方向反转。

由于主轴排列方向受通用属性direction影响，若设置了direction属性，则当reverse属性设置为true时，总在direction属性生效的结果上再做一次反转。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置Row组件的布局属性）

本示例展示设置Row组件的布局属性，如间距、对齐方式等属性后的效果。

```
1. // resources/base/element/string.json
2. {
3. "string": [
4. {
5. "name": "stringSpace",
6. "value": "5"
7. }
8. ]
9. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RowExample {
5. build() {
6. Column({ space: 5 }) {
7. // 设置子组件水平方向的间距为5
8. Text('space').width('90%')
9. Row({ space: 5 }) {
10. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
11. Row().width('30%').height(50).backgroundColor(0x00FFFF)
12. }.width('90%').height(107).border({ width: 1 })

14. // 通过资源引用方式设置子组件水平方向的间距
15. Text('Resource space').width('90%')
16. Row({ space: $r('app.string.stringSpace') }) {
17. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
18. Row().width('30%').height(50).backgroundColor(0x00FFFF)
19. }.width('90%').height(107).border({ width: 1 })

21. // 设置子元素垂直方向对齐方式
22. Text('alignItems(Bottom)').width('90%')
23. Row() {
24. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
25. Row().width('30%').height(50).backgroundColor(0x00FFFF)
26. }.width('90%').alignItems(VerticalAlign.Bottom).height('15%').border({ width: 1 })

28. Text('alignItems(Center)').width('90%')
29. Row() {
30. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
31. Row().width('30%').height(50).backgroundColor(0x00FFFF)
32. }.width('90%').alignItems(VerticalAlign.Center).height('15%').border({ width: 1 })

34. // 设置子元素水平方向对齐方式
35. Text('justifyContent(End)').width('90%')
36. Row() {
37. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
38. Row().width('30%').height(50).backgroundColor(0x00FFFF)
39. }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.End)

41. Text('justifyContent(Center)').width('90%')
42. Row() {
43. Row().width('30%').height(50).backgroundColor(0xAFEEEE)
44. Row().width('30%').height(50).backgroundColor(0x00FFFF)
45. }.width('90%').border({ width: 1 }).justifyContent(FlexAlign.Center)
46. }.width('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/cQVXkIfsSd6LMrc678_fYw/zh-cn_image_0000002558606458.png?HW-CC-KV=V1&HW-CC-Date=20260429T055138Z&HW-CC-Expire=86400&HW-CC-Sign=00F5F549C3356AF05489A6AD03CA4D315C7E09BEF07F1B625116BD6F0D465E7F)

### 示例2（设置反转属性）

本示例展示设置Row组件的reverse属性后的效果。

```
1. @Entry
2. @Component
3. struct RowReverseSample {
4. build() {
5. Row() {
6. Text("1")
7. .width(100)
8. .height(50)
9. .backgroundColor(0xAFEEEE)

11. Text("2")
12. .width(100)
13. .height(50)
14. .backgroundColor(0x00FFFF)
15. }
16. .height(100)
17. .width(300)
18. .border({ width: 1 })
19. .reverse(true)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/8s3HXY02QtmT0VnZSpHuJw/zh-cn_image_0000002589325985.png?HW-CC-KV=V1&HW-CC-Date=20260429T055138Z&HW-CC-Expire=86400&HW-CC-Sign=60573DF1C69489D9A693EF4018D7F3809F704E1D6F0913CCF89CE73E5CD1A19C)
