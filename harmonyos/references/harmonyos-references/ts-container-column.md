---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column
title: Column
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 行列与堆叠 > Column
category: harmonyos-references
scraped_at: 2026-04-29T13:51:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8bdbcc3326a5da067282e0693f2bfa2e65e237acdd75a99e7f77ad9cd4695084
---

沿垂直方向布局的容器。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

Column未设置高度或宽度时，在主轴或交叉轴方向上自适应子组件大小。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

### Column

PhonePC/2in1TabletTVWearable

Column(options?: ColumnOptions)

创建垂直方向线性布局容器，可以设置子组件的间距。

说明

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](../best-practices/bpta-improve-layout-performance.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options18+ | [ColumnOptions](ts-container-column.md#columnoptions18对象说明) | 否 | 纵向布局元素垂直方向间距，支持设置number或string类型。 |

### Column18+

PhonePC/2in1TabletTVWearable

Column(options?: ColumnOptions | ColumnOptionsV2)

创建垂直方向线性布局容器，可以设置子组件的间距。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ColumnOptions](ts-container-column.md#columnoptions18对象说明) | [ColumnOptionsV2](ts-container-column.md#columnoptionsv218对象说明) | 否 | 纵向布局元素垂直方向间距，支持设置number、string或Resource类型。 |

## ColumnOptions18+对象说明

PhonePC/2in1TabletTVWearable

设置Column组件的子组件间距属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| space7+ | string | number | 否 | 是 | 纵向布局元素垂直方向间距。  space为负数或者[justifyContent](ts-container-column.md#justifycontent8)设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，space不生效。  默认值：0  非法值：按默认值处理。  单位：vp  **说明：**  space取值是大于等于0的数字，或者可以转换为数字的字符串。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ColumnOptionsV218+对象说明

PhonePC/2in1TabletTVWearable

设置Column组件的子组件间距属性。间距类型SpaceType支持number、string或Resource类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| space | [SpaceType](ts-container-column.md#spacetype18) | 否 | 是 | 纵向布局元素垂直方向间距。  space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，space不生效。  默认值：0  单位：vp  非法值：按默认值处理。  **说明：**  space取值是大于等于0的数字，或者可以转换为数字的字符串，或者可以转换为数字的Resource类型数据。 |

## SpaceType18+

PhonePC/2in1TabletTVWearable

type SpaceType = string | number | Resource

Column组件构造函数中space支持的数据类型，取值类型为下表类型中的并集。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| number | 表示类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| [Resource](ts-types.md#resource) | 表示值为资源引用类型，取值为从系统资源或者应用资源中引入的数据值。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### alignItems

PhonePC/2in1TabletTVWearable

alignItems(value: HorizontalAlign)

设置子组件在水平方向上的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HorizontalAlign](ts-appendix-enums.md#horizontalalign) | 是 | 子组件在水平方向上的对齐格式。  默认值：HorizontalAlign.Center |

### justifyContent8+

PhonePC/2in1TabletTVWearable

justifyContent(value: FlexAlign)

设置子组件在垂直方向上的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexAlign](ts-appendix-enums.md#flexalign) | 是 | 子组件在垂直方向上的对齐格式。  默认值：FlexAlign.Start |

说明

Column布局时若子组件不设置[flexShrink](ts-universal-attributes-flex-layout.md#flexshrink)则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴，此时FlexAlign.Center和FlexAlign.End会失效。

### reverse12+

PhonePC/2in1TabletTVWearable

reverse(isReversed: Optional<boolean>)

设置子组件在垂直方向上的排列是否反转。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isReversed | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 子组件在垂直方向上的排列是否反转。  默认值：true，设置true表示子组件在垂直方向上反转排列，设置false表示子组件在垂直方向上正序排列。 |

说明

若未设置reverse属性，主轴方向不反转；若设置了reverse属性，且参数值为undefined，则视为默认值true，主轴方向反转。

通用属性direction只能改变Column交叉轴方向，不改变Column主轴方向，因此与reverse属性互不影响。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置Column组件的布局属性）

本示例展示设置Column组件的布局属性，如间距、对齐方式等属性后的效果。

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
4. struct ColumnExample {
5. build() {
6. Scroll() {
7. Column({ space: 5 }) {
8. // 设置子元素垂直方向间距为5
9. Text('space').width('90%')
10. Column({ space: 5 }) {
11. Column().width('100%').height(30).backgroundColor(0xAFEEEE)
12. Column().width('100%').height(30).backgroundColor(0x00FFFF)
13. }.width('90%').height(100).border({ width: 1 })

15. // 通过资源引用方式设置子元素垂直方向间距
16. Text('Resource space').width('90%')
17. Column({ space: $r('app.string.stringSpace') }) {
18. Column().width('100%').height(30).backgroundColor(0xAFEEEE)
19. Column().width('100%').height(30).backgroundColor(0x00FFFF)
20. }.width('90%').height(100).border({ width: 1 })

22. // 设置子元素水平方向对齐方式
23. Text('alignItems(Start)').width('90%')
24. Column() {
25. Column().width('50%').height(30).backgroundColor(0xAFEEEE)
26. Column().width('50%').height(30).backgroundColor(0x00FFFF)
27. }.alignItems(HorizontalAlign.Start).width('90%').border({ width: 1 })

29. Text('alignItems(End)').width('90%')
30. Column() {
31. Column().width('50%').height(30).backgroundColor(0xAFEEEE)
32. Column().width('50%').height(30).backgroundColor(0x00FFFF)
33. }.alignItems(HorizontalAlign.End).width('90%').border({ width: 1 })

35. Text('alignItems(Center)').width('90%')
36. Column() {
37. Column().width('50%').height(30).backgroundColor(0xAFEEEE)
38. Column().width('50%').height(30).backgroundColor(0x00FFFF)
39. }.alignItems(HorizontalAlign.Center).width('90%').border({ width: 1 })

41. // 设置子元素垂直方向的对齐方式
42. Text('justifyContent(Center)').width('90%')
43. Column() {
44. Column().width('90%').height(30).backgroundColor(0xAFEEEE)
45. Column().width('90%').height(30).backgroundColor(0x00FFFF)
46. }.height(100).border({ width: 1 }).justifyContent(FlexAlign.Center)

48. Text('justifyContent(End)').width('90%')
49. Column() {
50. Column().width('90%').height(30).backgroundColor(0xAFEEEE)
51. Column().width('90%').height(30).backgroundColor(0x00FFFF)
52. }.height(100).border({ width: 1 }).justifyContent(FlexAlign.End)
53. }.width('100%').padding({ top: 5 })
54. }.width('100%').height('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/w4Gx02HRSPCW5FiO7ydaOw/zh-cn_image_0000002589245925.png?HW-CC-KV=V1&HW-CC-Date=20260429T055138Z&HW-CC-Expire=86400&HW-CC-Sign=6E8FE8D368FFBAA39B1D900A4F258E9E25AEFA4125A1257CAC9E0A24DCB0DEDF)

### 示例2（设置反转属性）

本示例展示设置Column组件的reverse属性后的效果。

```
1. @Entry
2. @Component
3. struct ColumnReverseSample {
4. build() {
5. Column() {
6. Text("1")
7. .width(50)
8. .height(100)
9. .backgroundColor(0xAFEEEE)

11. Text("2")
12. .width(50)
13. .height(100)
14. .backgroundColor(0x00FFFF)
15. }
16. .height(300)
17. .width(100)
18. .border({ width: 1 })
19. .reverse(true)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/MtNjFIoSTyGNqS7EZ5jNUA/zh-cn_image_0000002558766116.png?HW-CC-KV=V1&HW-CC-Date=20260429T055138Z&HW-CC-Expire=86400&HW-CC-Sign=BC165AE4C78BC7C506C0BD1885BCB66EFF2B760E9FC24A0818F4A838DDFE0235)
