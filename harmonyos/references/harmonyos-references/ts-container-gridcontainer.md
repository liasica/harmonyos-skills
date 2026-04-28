---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcontainer
title: GridContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > GridContainer
category: harmonyos-references
scraped_at: 2026-04-28T08:02:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5778e71ef950b48dea849570f515b78f78a78458f9d8a1c466aaf5a4deeb0def
---

纵向排布栅格布局容器，仅在栅格布局场景中使用。

说明

从API version 9开始，该组件不再维护，推荐使用新组件[GridCol](ts-container-gridcol.md)、[GridRow](ts-container-gridrow.md)。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

GridContainer(value?: GridContainerOptions)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | GridContainerOptions | 否 | GridContainer参数。 |

## GridContainerOptions对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columns | number | 'auto' | 否 | 是 | 当前布局总列数。  默认值：'auto' |
| sizeType | SizeType | 否 | 是 | 选用设备宽度类型。  默认值：SizeType.Auto |
| gutter | number | string | 否 | 是 | 栅格布局列间距，不支持百分比。 |
| margin | number | string | 否 | 是 | 栅格布局两侧间距，不支持百分比。 |

## SizeType枚举说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| XS | 最小宽度类型设备。 |
| SM | 小宽度类型设备。 |
| MD | 中等宽度类型设备。 |
| LG | 大宽度类型设备。 |
| Auto | 根据设备类型进行选择。 |

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)和Column组件的[属性方法](ts-container-column.md#属性)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridContainerExample {
5. @State sizeType: SizeType = SizeType.XS

7. build() {
8. Column({ space: 5 }) {
9. GridContainer({ columns: 12, sizeType: this.sizeType, gutter: 10, margin: 20 }) {
10. Row() {
11. Text('1')
12. .useSizeType({
13. xs: { span: 6, offset: 0 },
14. sm: { span: 2, offset: 0 },
15. md: { span: 2, offset: 0 },
16. lg: { span: 2, offset: 0 }
17. })
18. .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
19. Text('2')
20. .useSizeType({
21. xs: { span: 2, offset: 6 },
22. sm: { span: 6, offset: 2 },
23. md: { span: 2, offset: 2 },
24. lg: { span: 2, offset: 2 }
25. })
26. .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
27. Text('3')
28. .useSizeType({
29. xs: { span: 2, offset: 8 },
30. sm: { span: 2, offset: 8 },
31. md: { span: 6, offset: 4 },
32. lg: { span: 2, offset: 4 }
33. })
34. .height(50).backgroundColor(0x4682B4).textAlign(TextAlign.Center)
35. Text('4')
36. .useSizeType({
37. xs: { span: 2, offset: 10 },
38. sm: { span: 2, offset: 10 },
39. md: { span: 2, offset: 10 },
40. lg: { span: 6, offset: 6 }
41. })
42. .height(50).backgroundColor(0x00BFFF).textAlign(TextAlign.Center)
43. }
44. }.width('90%')

46. Text('Click Simulate to change the device width').fontSize(9).width('90%').fontColor(0xCCCCCC)
47. Row() {
48. Button('XS')
49. .onClick(() => {
50. this.sizeType = SizeType.XS
51. }).backgroundColor(0x317aff)
52. Button('SM')
53. .onClick(() => {
54. this.sizeType = SizeType.SM
55. }).backgroundColor(0x317aff)
56. Button('MD')
57. .onClick(() => {
58. this.sizeType = SizeType.MD
59. }).backgroundColor(0x317aff)
60. Button('LG')
61. .onClick(() => {
62. this.sizeType = SizeType.LG
63. }).backgroundColor(0x317aff)
64. }
65. }.width('100%').margin({ top: 5 })
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2-teXGcLSSi9j-y49Pb2fg/zh-cn_image_0000002552960164.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000247Z&HW-CC-Expire=86400&HW-CC-Sign=0CE19BE4DC0A0C15A8B5381BED0FCB1FD1E0656F07F84F3C32292D3F7BF656FB)
