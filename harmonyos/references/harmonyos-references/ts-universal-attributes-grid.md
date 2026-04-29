---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-grid
title: 栅格设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > 栅格设置
category: harmonyos-references
scraped_at: 2026-04-29T13:53:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fa4037fd9e3b449e165267b8b8e85551735a96aa819d4e29fdaa6430097afcea
---

栅格设置可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 从API version 9开始，该模块不再维护，推荐使用新组件[GridCol](ts-container-gridcol.md)、[GridRow](ts-container-gridrow.md)替代。
* 栅格布局的列宽、列间距由距离最近的GridContainer父组件决定。使用栅格属性的组件树上至少需要有1个GridContainer容器组件。
* gridSpan、gridOffset属性调用时其父组件或祖先组件必须是GridContainer。

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 参数类型 | 描述 |
| --- | --- | --- |
| useSizeType(deprecated) | {  xs?: number | { span: number, offset: number },  sm?: number | { span: number, offset: number },  md?: number | { span: number, offset: number },  lg?: number | { span: number, offset: number }  } | 设置在特定设备宽度类型下的占用列数和偏移列数，span：占用列数；offset：偏移列数。  当值为number类型时，仅设置列数，当格式如{"span": 1, "offset": 0}时，指同时设置占用列数与偏移列数。  - xs：指设备宽度类型为SizeType.XS时的占用列数和偏移列数。  - sm：指设备宽度类型为SizeType.SM时的占用列数和偏移列数。  - md：指设备宽度类型为SizeType.MD时的占用列数和偏移列数。  - lg：指设备宽度类型为SizeType.LG时的占用列数和偏移列数。  该属性从API version 9开始废弃，推荐使用新组件[GridCol](ts-container-gridcol.md)、[GridRow](ts-container-gridrow.md)。 |
| gridSpan(deprecated) | number | 默认占用列数，指useSizeType属性没有设置对应尺寸的列数(span)时，占用的栅格列数。  **说明：**  设置了栅格span属性，组件的宽度由栅格布局决定。  默认值：1  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  该属性从API version 14开始废弃，推荐使用新组件[GridCol](ts-container-gridcol.md)、[GridRow](ts-container-gridrow.md)。 |
| gridOffset(deprecated) | number | 默认偏移列数，指useSizeType属性没有设置对应尺寸的偏移(offset)时，当前组件沿着父组件Start方向，偏移的列数，也就是当前组件位于第n列。  **说明：**  - 配置该属性后，当前组件在父组件水平方向的布局不再跟随父组件原有的布局方式，而是沿着父组件的Start方向偏移一定位移。  - 偏移位移 = （列宽 + 间距）\* 列数。  - 设置了偏移(gridOffset)的组件之后的兄弟组件会根据该组件进行相对布局，类似相对布局。  默认值：0  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  该属性从API version 14开始废弃，推荐使用新组件[GridCol](ts-container-gridcol.md)、[GridRow](ts-container-gridrow.md)。 |

## 示例

PhonePC/2in1TabletTVWearable

设置不同设备类型的宽度，以及单独设置组件的span和offset，在sm尺寸大小的设备上使用useSizeType中sm的数据实现一样的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridContainerExample1 {
5. build() {
6. Column() {
7. Text('useSizeType').fontSize(15).fontColor(0xCCCCCC).width('90%')
8. GridContainer() {
9. Row() {
10. Row() {
11. Text('Left').fontSize(25)
12. }
13. .useSizeType({
14. xs: { span: 1, offset: 0 }, sm: { span: 1, offset: 0 },
15. md: { span: 1, offset: 0 }, lg: { span: 2, offset: 0 }
16. })
17. .height("100%")
18. .backgroundColor(0x66bbb2cb)

20. Row() {
21. Text('Center').fontSize(25)
22. }
23. .useSizeType({
24. xs: { span: 1, offset: 0 }, sm: { span: 2, offset: 1 },
25. md: { span: 5, offset: 1 }, lg: { span: 7, offset: 2 }
26. })
27. .height("100%")
28. .backgroundColor(0x66b6c5d1)

30. Row() {
31. Text('Right').fontSize(25)
32. }
33. .useSizeType({
34. xs: { span: 1, offset: 0 }, sm: { span: 1, offset: 3 },
35. md: { span: 2, offset: 6 }, lg: { span: 3, offset: 9 }
36. })
37. .height("100%")
38. .backgroundColor(0x66bbb2cb)
39. }
40. .height(200)

42. }
43. .backgroundColor(0xf1f3f5)
44. .margin({ top: 10 })

46. // 单独设置组件的span和offset,在sm尺寸大小的设备上使用useSizeType中sm的数据实现一样的效果
47. Text('gridSpan,gridOffset').fontSize(15).fontColor(0xCCCCCC).width('90%')
48. GridContainer() {
49. Row() {
50. Row() {
51. Text('Left').fontSize(25)
52. }
53. .gridSpan(1)
54. .height("100%")
55. .backgroundColor(0x66bbb2cb)

57. Row() {
58. Text('Center').fontSize(25)
59. }
60. .gridSpan(2)
61. .gridOffset(1)
62. .height("100%")
63. .backgroundColor(0x66b6c5d1)

65. Row() {
66. Text('Right').fontSize(25)
67. }
68. .gridSpan(1)
69. .gridOffset(3)
70. .height("100%")
71. .backgroundColor(0x66bbb2cb)
72. }.height(200)
73. }
74. }
75. }
76. }
```

**图1** 设备宽度为SM

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/9U4WlLvPQ7K690VPjKfdwQ/zh-cn_image_0000002589326559.png?HW-CC-KV=V1&HW-CC-Date=20260429T055312Z&HW-CC-Expire=86400&HW-CC-Sign=2C70499479D6B6D547CB6EA7926B2DF331718ACF6D107802B181FB97ED56EF27)

**图2** 设备宽度为MD

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/kGGg88F-RJSFA1gpa7RAng/zh-cn_image_0000002589246501.png?HW-CC-KV=V1&HW-CC-Date=20260429T055312Z&HW-CC-Expire=86400&HW-CC-Sign=961EB418703278C8F3BC99C274EAB6DF309FCA1386337ACFA55AA653FF72F626)

**图3** 设备宽度为LG

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/obbiB8itRg6cCMGnhwZ5xw/zh-cn_image_0000002558766694.png?HW-CC-KV=V1&HW-CC-Date=20260429T055312Z&HW-CC-Expire=86400&HW-CC-Sign=17EE60B5B772FDE01A165FA917E283F9247AEF8428F1F771A1754A54B934D1F1)

**图4** 单独设置gridSpan和gridOffset在特定屏幕大小下的效果与useSizeType效果一致

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Gq-SUvtSSkmJ_nYAVlYEMA/zh-cn_image_0000002558607034.png?HW-CC-KV=V1&HW-CC-Date=20260429T055312Z&HW-CC-Expire=86400&HW-CC-Sign=BF8DDD28913C8EC19DF574EE4196AFCD9F395BDC64C6FE7CDDB8DB46E1BFBC55)
