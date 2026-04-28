---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout
title: Flex布局
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > Flex布局
category: harmonyos-references
scraped_at: 2026-04-28T08:01:04+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:99a2fcdc3c5cf3beb53e0dbcd4f238941817c4c266db11e0bd48881f7717706d
---

可以灵活排列、对齐和分配容器内的子组件空间，使元素根据可用空间扩展或收缩，以满足不同屏幕尺寸下的响应式布局。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 仅[Flex](ts-container-flex.md)、[Column](ts-container-column.md)或[Row](ts-container-row.md)支持下述四种属性，[GridRow](ts-container-gridrow.md)仅支持设置[alignSelf](ts-universal-attributes-flex-layout.md#alignself)。

## flexBasis

PhonePC/2in1TabletTVWearable

flexBasis(value: number | string): T

设置组件的基准尺寸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 设置组件在父容器主轴方向上的基准尺寸。  默认值：'auto'（表示组件在主轴方向上的基准尺寸为组件原本的大小）。  string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'）或'auto'，不允许设置百分比字符串。  number：取值范围(0,+∞)，单位为vp。  异常值：默认为'auto'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## flexGrow

PhonePC/2in1TabletTVWearable

flexGrow(value: number): T

设置组件在父容器的剩余空间所占比例。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置父容器在主轴方向上的剩余空间分配给此属性所在组件的比例。  取值范围：[0, +∞)  默认值：0  设置异常值时，该属性为默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## flexShrink

PhonePC/2in1TabletTVWearable

flexShrink(value: number): T

设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

说明

使用[getInspectorByKey](ts-universal-attributes-component-id.md#getinspectorbykey9)获取flexShrink属性时，如果该节点未设置flexShrink属性，默认返回1。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置父容器压缩尺寸分配给此属性所在组件的比例。  父容器为[Column](ts-container-column.md)、[Row](ts-container-row.md)时，默认值：0，取值范围[0,+∞)。  父容器为[Flex](ts-container-flex.md)时，默认值：1  [constraintSize](ts-universal-attributes-size.md#constraintsize)限制组件的尺寸范围。[Column](ts-container-column.md)和[Row](ts-container-row.md)即使设置了[constraintSize](ts-universal-attributes-size.md#constraintsize)，在未设置主轴尺寸（[width](ts-universal-attributes-size.md#width)/[height](ts-universal-attributes-size.md#height)/[size](ts-universal-attributes-size.md#size)）时仍遵守默认布局行为，在主轴上自适应子组件尺寸，此时flexShrink不生效。  设置异常值时，该属性为默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## alignSelf

PhonePC/2in1TabletTVWearable

alignSelf(value: ItemAlign): T

子组件在父容器交叉轴的对齐格式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ItemAlign](ts-appendix-enums.md#itemalign) | 是 | 子组件在父容器交叉轴的对齐格式，会覆盖[Flex](ts-container-flex.md)、[Column](ts-container-column.md)、[Row](ts-container-row.md)、[GridRow](ts-container-gridrow.md)布局容器中的alignItems设置。  [GridCol](ts-container-gridcol.md)可以绑定alignSelf属性来改变它自身在交叉轴方向上的布局。  默认值：ItemAlign.Auto |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

通过配置flexBasis/flexGrow/flexShrink/alignSelf属性设置Flex布局。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FlexExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('flexBasis').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. // 基于主轴的基准尺寸
9. // flexBasis()值可以是字符串'auto'，表示基准尺寸是元素本来的大小，也可以是长度设置，相当于.width()/.height()
10. Flex() {
11. Text('flexBasis(100)')
12. .flexBasis(100) // 这里表示宽度为100vp
13. .height(100)
14. .backgroundColor(0xF5DEB3)
15. .textAlign(TextAlign.Center)
16. Text(`flexBasis('auto')`)
17. .flexBasis('auto') // 这里表示宽度保持原本设置的60%的宽度
18. .width('60%')
19. .height(100)
20. .backgroundColor(0xD2B48C)
21. .textAlign(TextAlign.Center)
22. }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

24. Text('flexGrow').fontSize(9).fontColor(0xCCCCCC).width('90%')
25. // flexGrow()表示剩余空间分配给该元素的比例
26. Flex() {
27. Text('flexGrow(2)')
28. .flexGrow(2) // 父容器分配给该Text的宽度为剩余宽度的2/3
29. .height(100)
30. .backgroundColor(0xF5DEB3)
31. .textAlign(TextAlign.Center)
32. Text('flexGrow(1)')
33. .flexGrow(1) // 父容器分配给该Text的宽度为剩余宽度的1/3
34. .height(100)
35. .backgroundColor(0xD2B48C)
36. .textAlign(TextAlign.Center)
37. }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

39. Text('flexShrink').fontSize(9).fontColor(0xCCCCCC).width('90%')
40. // flexShrink()表示该元素的压缩比例，基于超出的总尺寸进行计算
41. // 第一个text压缩比例是0，另外两个都是1，因此放不下时等比例压缩后两个，第一个不压缩
42. Flex({ direction: FlexDirection.Row }) {
43. Text('flexShrink(0)')
44. .flexShrink(0)
45. .width('50%')
46. .height(100)
47. .backgroundColor(0xF5DEB3)
48. .textAlign(TextAlign.Center)
49. Text('default flexShrink') // 默认值为1
50. .width('40%')
51. .height(100)
52. .backgroundColor(0xD2B48C)
53. .textAlign(TextAlign.Center)
54. Text('flexShrink(1)')
55. .flexShrink(1)
56. .width('40%')
57. .height(100)
58. .backgroundColor(0xF5DEB3)
59. .textAlign(TextAlign.Center)
60. }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)

62. Text('alignSelf').fontSize(9).fontColor(0xCCCCCC).width('90%')
63. // alignSelf会覆盖Flex布局容器中的alignItems设置
64. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
65. Text('no alignSelf,height:70')
66. .width('33%')
67. .height(70)
68. .backgroundColor(0xF5DEB3)
69. .textAlign(TextAlign.Center)
70. Text('alignSelf End')
71. .alignSelf(ItemAlign.End)
72. .width('33%')
73. .height(70)
74. .backgroundColor(0xD2B48C)
75. .textAlign(TextAlign.Center)
76. Text('no alignSelf,height:100%')
77. .width('34%')
78. .height('100%')
79. .backgroundColor(0xF5DEB3)
80. .textAlign(TextAlign.Center)
81. }.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)
82. }.width('100%').margin({ top: 5 })
83. }
84. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/H1NsIYQnTT6a9IYppl6FMg/zh-cn_image_0000002583439541.png?HW-CC-KV=V1&HW-CC-Date=20260428T000102Z&HW-CC-Expire=86400&HW-CC-Sign=707E4B8DADDD50941F974CC67169302470F713BAB98F66840880869A682E69C3)
