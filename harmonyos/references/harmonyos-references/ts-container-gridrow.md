---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow
title: GridRow
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 栅格与分栏 > GridRow
category: harmonyos-references
scraped_at: 2026-04-29T13:51:41+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2d8a388f3c293eb95f645689060ccfe372cc1b59ef705c85f89e43efca051f12
---

栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。

栅格容器组件，仅可以和栅格子组件([GridCol](ts-container-gridcol.md))在栅格布局场景中使用。

说明

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含GridCol子组件。

## 接口

PhonePC/2in1TabletTVWearable

GridRow(option?: GridRowOptions)

栅格行布局容器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [GridRowOptions](ts-container-gridrow.md#gridrowoptions对象说明) | 否 | 栅格布局子组件参数。 |

## GridRowOptions对象说明

PhonePC/2in1TabletTVWearable

设置栅格行布局容器的布局选项。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columns | number | [GridRowColumnOption](ts-container-gridrow.md#gridrowcolumnoption) | 否 | 是 | 设置布局列数。  取值为大于0的整数。  - API version 20之前：默认值为12。  - API version 20及之后：默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }  非法值：按默认值处理。 |
| gutter | [Length](ts-types.md#length) | [GutterOption](ts-container-gridrow.md#gutteroption) | 否 | 是 | 栅格布局间距。  默认值：0  非法值：按默认值处理。  单位：vp |
| breakpoints | [BreakPoints](ts-container-gridrow.md#breakpoints) | 否 | 是 | 设置断点值的断点数组以及基于应用窗口或容器尺寸的相应参照。  默认值：  {  value: ["320vp", "600vp", "840vp"],  reference: BreakpointsReference.WindowSize  }  非法值：按默认值处理。  单位：vp |
| direction | [GridRowDirection](ts-container-gridrow.md#gridrowdirection枚举说明) | 否 | 是 | 栅格布局排列方向。  默认值：GridRowDirection.Row  非法值：按默认值处理。 |

## GutterOption

PhonePC/2in1TabletTVWearable

栅格布局间距类型，用于描述栅格子组件不同方向的间距。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | [Length](ts-types.md#length) | [GridRowSizeOption](ts-container-gridrow.md#gridrowsizeoption) | 否 | 是 | 栅格子组件水平方向间距。 |
| y | [Length](ts-types.md#length) | [GridRowSizeOption](ts-container-gridrow.md#gridrowsizeoption) | 否 | 是 | 栅格子组件竖直方向间距。 |

## GridRowColumnOption

PhonePC/2in1TabletTVWearable

栅格在不同宽度设备类型下，栅格列数。

API version 20之前，仅配置部分断点下GridRow组件的栅格列数，取已配置的更小断点的栅格列数补全未配置的栅格列数。若未配置更小断点的栅格列数，以默认栅格列数12补全未配置的栅格列数。

```
1. columns: {xs:2, md:4, lg:8} // 等于配置 columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
2. columns: {md:4, lg:8} // 等于配置 columns: {xs:12, sm:12, md:4, lg:8, xl:8, xxl:8}
```

API version 20及以后，仅配置部分断点下GridRow组件的栅格列数，取已配置的更小断点的栅格列数补全未配置的栅格列数。若未配置更小断点的栅格列数，取已配置的更大断点的栅格列数补全未配置的栅格列数。

```
1. columns: {xs:2, md:4, lg:8} // 等于配置 columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
2. columns: {md:4, lg:8} // 等于配置 columns: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8}
```

建议手动配置不同断点下GridRow组件的栅格列数，避免默认补全的栅格列数的布局效果不符合预期。

每列栅格的宽度为GridRow的内容区大小减去栅格子组件的间距gutter，再除以总的栅格列数。比如，宽800px的GridRow设置columns为12，gutter设置为10px，padding设置为20px，那么每列栅格的宽度为(800 - 20 \* 2 - 10 \* 11) / 12。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xs | number | 否 | 是 | 在栅格大小为xs的设备上，栅格容器组件的栅格列数。 |
| sm | number | 否 | 是 | 在栅格大小为sm的设备上，栅格容器组件的栅格列数。 |
| md | number | 否 | 是 | 在栅格大小为md的设备上，栅格容器组件的栅格列数。 |
| lg | number | 否 | 是 | 在栅格大小为lg的设备上，栅格容器组件的栅格列数。 |
| xl | number | 否 | 是 | 在栅格大小为xl的设备上，栅格容器组件的栅格列数。 |
| xxl | number | 否 | 是 | 在栅格大小为xxl的设备上，栅格容器组件的栅格列数。 |

## GridRowSizeOption

PhonePC/2in1TabletTVWearable

栅格在不同宽度设备类型下，gutter的大小。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xs | [Length](ts-types.md#length) | 否 | 是 | 在最小宽度类型设备上，栅格子组件的间距。  默认值：0vp |
| sm | [Length](ts-types.md#length) | 否 | 是 | 在小宽度类型设备上，栅格子组件的间距。  默认值：0vp |
| md | [Length](ts-types.md#length) | 否 | 是 | 在中等宽度类型设备上，栅格子组件的间距。  默认值：0vp |
| lg | [Length](ts-types.md#length) | 否 | 是 | 在大宽度类型设备上，栅格子组件的间距。  默认值：0vp |
| xl | [Length](ts-types.md#length) | 否 | 是 | 在特大宽度类型设备上，栅格子组件的间距。  默认值：0vp |
| xxl | [Length](ts-types.md#length) | 否 | 是 | 在超大宽度类型设备上，栅格子组件的间距。  默认值：0vp |

## BreakPoints

PhonePC/2in1TabletTVWearable

设置栅格容器组件的断点。更多断点的说明参考[栅格容器断点](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | Array<string> | 否 | 是 | 设置断点位置的单调递增数组。  默认值：["320vp", "600vp", "840vp"]  非法值：按默认值处理。  单位：vp |
| reference | [BreakpointsReference](ts-container-gridrow.md#breakpointsreference枚举说明) | 否 | 是 | 断点切换参照物。  默认值：BreakpointsReference.WindowSize  非法值：按默认值处理。 |

```
1. // 启用xs、sm、md共3个断点
2. breakpoints: {value: ['100vp', '200vp']}
3. // 启用xs、sm、md、lg共4个断点，断点范围值必须单调递增
4. breakpoints: {value: ['320vp', '600vp', '840vp']}
5. // 启用xs、sm、md、lg、xl共5个断点，断点范围数量不可超过断点可取值数量-1
6. breakpoints: {value: ['320vp', '600vp', '840vp', '1080vp']}
```

## BreakpointsReference枚举说明

PhonePC/2in1TabletTVWearable

设置栅格容器组件的断点参照物。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WindowSize | 0 | 以窗口为参照。 |
| ComponentSize | 1 | 以容器为参照。 |

## GridRowDirection枚举说明

PhonePC/2in1TabletTVWearable

栅格元素排列方向。

说明

* 栅格元素仅支持Row/RowReverse排列，不支持column/ColumnReverse方向排列。
* 栅格子组件仅能通过span、offset计算子组件位置与大小。多个子组件span超过规定列数时自动换行。
* 单个元素span大小超过最大列数时后台默认span为最大column数。
* 新一行的Offset加上子组件的span超过总列数时，将下一个子组件在新的一行放置。
* 例：Item1: GridCol({ span: 6 })， Item2: GridCol({ span: 8, offset:11 })。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/i7d_2nspTAy9KYD1CgrNxQ/zh-cn_image_0000002589325991.png?HW-CC-KV=V1&HW-CC-Date=20260429T055139Z&HW-CC-Expire=86400&HW-CC-Sign=D3DD18D3D40E099FB3067087CC7E32036A59A0C3A91204CA0FB3DA8897F4DCA5)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Row | 0 | 栅格元素按照行方向排列。 |
| RowReverse | 1 | 栅格元素按照逆序行方向排列。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### alignItems10+

PhonePC/2in1TabletTVWearable

alignItems(value: ItemAlign)

设置GridRow中的GridCol垂直主轴方向对齐方式。GridCol本身也可通过alignSelf([ItemAlign](ts-appendix-enums.md#itemalign))设置自身对齐方式。当上述两种对齐方式都设置时，以GridCol自身设置为准。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ItemAlign](ts-appendix-enums.md#itemalign) | 是 | GridRow中的GridCol垂直主轴方向对齐方式。  默认值：ItemAlign.Start  非法值：按默认值处理。  **说明**：  ItemAlign支持的枚举：ItemAlign.Start、ItemAlign.Center、ItemAlign.End、ItemAlign.Stretch。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onBreakpointChange

PhonePC/2in1TabletTVWearable

onBreakpointChange(callback: (breakpoints: string) => void)

断点发生变化时触发回调。

说明

* 当[断点参照物](ts-container-gridrow.md#breakpointsreference枚举说明)设置为BreakpointsReference.ComponentSize时，不建议在onBreakpointChange回调中动态修改GridRow组件的[padding](ts-universal-attributes-size.md#padding)或[margin](ts-universal-attributes-size.md#margin)属性值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (breakpoints: string) => void | 是 | breakpoints取值为"xs"、"sm"、"md"、"lg"、"xl"、"xxl"。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（栅格布局的基本用法）

本示例展示GridRow组件的基本用法。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridRowExample {
5. @State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]
6. @State currentBp: string = 'unknown'

8. build() {
9. Column() {
10. GridRow({
11. columns: 5,
12. gutter: { x: 5, y: 10 },
13. breakpoints: { value: ['400vp', '600vp', '800vp'],
14. reference: BreakpointsReference.WindowSize },
15. direction: GridRowDirection.Row
16. }) {
17. ForEach(this.bgColors, (color: Color) => {
18. GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 }, offset: 0, order: 0 }) {
19. Row().width('100%').height('20vp')
20. }.borderColor(color).borderWidth(2)
21. })
22. }.width('100%').height('100%')
23. .onBreakpointChange((breakpoint) => {
24. this.currentBp = breakpoint
25. })
26. }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200)
27. .border({ color: '#880606', width: 2 })
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/AaMwOkQLSxi91vEoH16J3g/zh-cn_image_0000002589245933.png?HW-CC-KV=V1&HW-CC-Date=20260429T055139Z&HW-CC-Expire=86400&HW-CC-Sign=A02C5517BB8A3E36F3DE24CCC2EAAB5B7CFEE33265CF3CE46D37CF811CD01F74)

### 示例2（AlignItems的基本用法）

本示例展示GridCol组件在不同alignItems对齐方式下的效果。

```
1. @ComponentV2
2. struct AlignItemsDemo {
3. bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink];
4. @Param alignment: ItemAlign = ItemAlign.Start; // 接收父组件传入的alignItems属性值

6. ToString(alignment: ItemAlign): string {
7. switch (alignment) {
8. case ItemAlign.Start:
9. return "ItemAlign.Start";
10. case ItemAlign.Center:
11. return "ItemAlign.Center";
12. case ItemAlign.End:
13. return "ItemAlign.End";
14. case ItemAlign.Stretch:
15. return "ItemAlign.Stretch";
16. default:
17. return "ItemAlign.Auto";
18. }
19. }

21. build() {
22. Column() {
23. Text(this.ToString(this.alignment))
24. .fontSize(9)
25. .fontColor(0xCCCCCC)
26. .width('90%')
27. .alignSelf(ItemAlign.Start)
28. GridRow({
29. columns: 5,
30. gutter: { x: 5, y: 10 },
31. }) {
32. ForEach(this.bgColors, (color: Color, index: number) => {
33. GridCol({ span: 1 }) {
34. Row() {
35. }.width('100%').height(`${(index + 1) * 20}%`) // GridCol设置不同的高度，方便观察alignItems属性的效果
36. }.borderColor(color).borderWidth(2)
37. })
38. }
39. .border({ color: '#880606', width: 2 })
40. .alignItems(this.alignment)
41. .width('100%')
42. }
43. .height("20%")
44. }
45. }

47. @Entry
48. @ComponentV2
49. struct GridRowExample {
50. alignmentArray: ItemAlign[] = [ItemAlign.Start, ItemAlign.Center, ItemAlign.End, ItemAlign.Stretch];

52. build() {
53. Column({ space: 15 }) {
54. ForEach(this.alignmentArray, (ele: ItemAlign) => {
55. AlignItemsDemo({ alignment: ele })
56. })
57. }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height("100%")
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/89-nZ09AS-yOCPelXB29_w/zh-cn_image_0000002558766124.png?HW-CC-KV=V1&HW-CC-Date=20260429T055139Z&HW-CC-Expire=86400&HW-CC-Sign=992C8594C22E19C8047B694EE961E50CDB382707E406C83FB1A5826EE61D30AE)
