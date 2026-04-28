---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex
title: Flex
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 行列与堆叠 > Flex
category: harmonyos-references
scraped_at: 2026-04-28T08:01:25+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:287d6754e34cb96a5910d37a77fc93bd7a72db57014b7378824b9de18aef8063
---

Flex是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。

具体指南请参考[弹性布局](../harmonyos-guides/arkts-layout-development-flex-layout.md)。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容将采用上角标单独标记该内容的起始版本。
* Flex组件在渲染时存在二次布局过程，因此在对性能有严格要求的场景下建议使用[Column](ts-container-column.md)、[Row](ts-container-row.md)代替。最佳实践请参考[布局优化指导-合理使用布局组件](../best-practices/bpta-improve-layout-performance.md#section12745188175420)。
* Flex组件主轴不设置长度时默认撑满父容器，如果包含设置[position](ts-universal-attributes-location.md#position)的子组件，此时Flex组件不会撑满父容器。[Column](ts-container-column.md)、[Row](ts-container-row.md)组件主轴不设置长度时默认跟随子节点大小。
* Flex、Column、Row组件在没有子节点且不设置宽高时，默认宽高为-1。
* 主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受constraintSize属性以及父容器传递的最大最小长度限制，且constraintSize属性优先级更高。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

Flex(value?: FlexOptions)

Flex布局容器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexOptions](ts-container-flex.md#flexoptions对象说明) | 否 | 弹性布局子组件参数。 |

## FlexOptions对象说明

PhonePC/2in1TabletTVWearable

设置Flex子组件的排列对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [FlexDirection](ts-appendix-enums.md#flexdirection) | 否 | 是 | 子组件在Flex容器上排列的方向，即主轴的方向。  默认值：FlexDirection.Row  异常值按默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| wrap | [FlexWrap](ts-appendix-enums.md#flexwrap) | 否 | 是 | Flex容器是单行/列还是多行/列排列。  默认值：FlexWrap.NoWrap  异常值按默认值处理。  **说明：**  在多行布局时，通过交叉轴方向，确认新行堆叠方向。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| justifyContent | [FlexAlign](ts-appendix-enums.md#flexalign) | 否 | 是 | 所有子组件在Flex容器主轴上的对齐格式。  默认值：FlexAlign.Start  异常值按默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignItems | [ItemAlign](ts-appendix-enums.md#itemalign) | 否 | 是 | 所有子组件在Flex容器交叉轴上的对齐格式。  默认值：ItemAlign.Start  异常值按默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| alignContent | [FlexAlign](ts-appendix-enums.md#flexalign) | 否 | 是 | 当交叉轴存在额外空间时，多行内容之间的对齐方式。仅在wrap为Wrap或WrapReverse下生效。  默认值：FlexAlign.Start  异常值按默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| space12+ | [FlexSpaceOptions12+](ts-container-flex.md#flexspaceoptions12) | 否 | 是 | 所有子组件在Flex容器主轴或交叉轴的间距。  默认值：{main: LengthMetrics.px(0), cross: LengthMetrics.px(0)}  非法值：按默认值处理。  space为负数、百分比或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## FlexSpaceOptions12+

PhonePC/2in1TabletTVWearable

设置Flex容器的子组件在主轴或交叉轴的间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | Flex容器主轴上的space。  默认值：LengthMetrics.px(0) |
| cross | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | Flex容器交叉轴上的space。  默认值：LengthMetrics.px(0) |

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（子组件排列方向）

该示例通过设置direction实现不同的子组件排列方向效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FlexExample1 {
5. build() {
6. Column() {
7. Column({ space: 5 }) {
8. Text('direction:Row').fontSize(9).fontColor(0xCCCCCC).width('90%')
9. Flex({ direction: FlexDirection.Row }) { // 子组件在容器主轴上行布局
10. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
11. Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
12. Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
13. Text('4').width('20%').height(50).backgroundColor(0xD2B48C)
14. }
15. .height(70)
16. .width('90%')
17. .padding(10)
18. .backgroundColor(0xAFEEEE)

20. Text('direction:RowReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
21. Flex({ direction: FlexDirection.RowReverse }) { // 子组件在容器主轴上反向行布局
22. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
23. Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
24. Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
25. Text('4').width('20%').height(50).backgroundColor(0xD2B48C)
26. }
27. .height(70)
28. .width('90%')
29. .padding(10)
30. .backgroundColor(0xAFEEEE)

32. Text('direction:Column').fontSize(9).fontColor(0xCCCCCC).width('90%')
33. Flex({ direction: FlexDirection.Column }) { // 子组件在容器主轴上列布局
34. Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)
35. Text('2').width('100%').height(40).backgroundColor(0xD2B48C)
36. Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)
37. Text('4').width('100%').height(40).backgroundColor(0xD2B48C)
38. }
39. .height(160)
40. .width('90%')
41. .padding(10)
42. .backgroundColor(0xAFEEEE)

44. Text('direction:ColumnReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
45. Flex({ direction: FlexDirection.ColumnReverse }) { // 子组件在容器主轴上反向列布局
46. Text('1').width('100%').height(40).backgroundColor(0xF5DEB3)
47. Text('2').width('100%').height(40).backgroundColor(0xD2B48C)
48. Text('3').width('100%').height(40).backgroundColor(0xF5DEB3)
49. Text('4').width('100%').height(40).backgroundColor(0xD2B48C)
50. }
51. .height(160)
52. .width('90%')
53. .padding(10)
54. .backgroundColor(0xAFEEEE)
55. }.width('100%').margin({ top: 5 })
56. }.width('100%')
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/jM4VuDk8RIGNM5ZeemY2LA/zh-cn_image_0000002552959590.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=BAA96F5725D039DACDD52E2A7ADD14EDACF99B298BB4C21689C9D0DF55437B21)

### 示例2（子组件单/多行排列）

该示例通过设置wrap实现子组件单行或多行的排列效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FlexExample2 {
5. build() {
6. Column() {
7. Column({ space: 5 }) {
8. Text('Wrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
9. Flex({ wrap: FlexWrap.Wrap }) { // 子组件多行布局
10. Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
11. Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
12. Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
13. }
14. .width('90%')
15. .padding(10)
16. .backgroundColor(0xAFEEEE)

18. Text('NoWrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
19. Flex({ wrap: FlexWrap.NoWrap }) { // 子组件单行布局
20. Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
21. Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
22. Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
23. }
24. .width('90%')
25. .padding(10)
26. .backgroundColor(0xAFEEEE)

28. Text('WrapReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
29. Flex({ wrap: FlexWrap.WrapReverse , direction:FlexDirection.Row }) { // 子组件反向多行布局
30. Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
31. Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
32. Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
33. }
34. .width('90%')
35. .height(120)
36. .padding(10)
37. .backgroundColor(0xAFEEEE)
38. }.width('100%').margin({ top: 5 })
39. }.width('100%')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/oUASN5NKQDKVX4eTTyuBjg/zh-cn_image_0000002583479591.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=A10E2AAD92E026A566E3749554744FDF343B46C921274D3DDBF6C464DF32D1AA)

### 示例3（子组件在主轴上的对齐格式）

该示例通过设置justifyContent实现子组件在主轴上不同的对齐效果。

```
1. // xxx.ets
2. @Component
3. struct JustifyContentFlex {
4. justifyContent : number = 0;

6. build() {
7. Flex({ justifyContent: this.justifyContent }) {
8. Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
9. Text('2').width('20%').height(50).backgroundColor(0xD2B48C)
10. Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
11. }
12. .width('90%')
13. .padding(10)
14. .backgroundColor(0xAFEEEE)
15. }
16. }

18. @Entry
19. @Component
20. struct FlexExample3 {
21. build() {
22. Column() {
23. Column({ space: 5 }) {
24. Text('justifyContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
25. JustifyContentFlex({ justifyContent: FlexAlign.Start }) // 子组件在容器主轴上首端对齐

27. Text('justifyContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
28. JustifyContentFlex({ justifyContent: FlexAlign.Center }) // 子组件在容器主轴上居中对齐

30. Text('justifyContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
31. JustifyContentFlex({ justifyContent: FlexAlign.End }) // 子组件在容器主轴上尾端对齐

33. Text('justifyContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')
34. JustifyContentFlex({ justifyContent: FlexAlign.SpaceBetween }) // 子组件在容器主轴上均分容器布局，第一个子组件与行首对齐，最后一个子组件与行尾对齐。

36. Text('justifyContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')
37. JustifyContentFlex({ justifyContent: FlexAlign.SpaceAround }) // 子组件在容器主轴上均分容器布局，第一个子组件到行首的距离和最后一个子组件到行尾的距离是相邻子组件之间距离的一半。

39. Text('justifyContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')
40. JustifyContentFlex({ justifyContent: FlexAlign.SpaceEvenly }) // 子组件在容器主轴上均分容器布局，子组件之间的距离与第一子组件到行首、最后一个子组件到行尾的距离相等
41. }.width('100%').margin({ top: 5 })
42. }.width('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/2KO1aZnyQnGoPERKv-__UQ/zh-cn_image_0000002552799942.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=B6AC30265603834094091D2413473A2C623C38A07A5C5D1DA796B233C3582E43)

### 示例4（子组件在交叉轴上的对齐方式）

该示例通过设置alignItems实现子组件在交叉轴上的不同的对齐效果。

```
1. // xxx.ets
2. @Component
3. struct AlignItemsFlex {
4. alignItems : number = 0;

6. build() {
7. Flex({ alignItems: this.alignItems }) {
8. Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)
9. Text('2').width('33%').height(40).backgroundColor(0xD2B48C)
10. Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
11. }
12. .size({width: '90%', height: 80})
13. .padding(10)
14. .backgroundColor(0xAFEEEE)
15. }
16. }

18. @Entry
19. @Component
20. struct FlexExample4 {
21. build() {
22. Column() {
23. Column({ space: 5 }) {
24. Text('alignItems:Auto').fontSize(9).fontColor(0xCCCCCC).width('90%')
25. AlignItemsFlex({ alignItems: ItemAlign.Auto }) // 子组件在容器交叉轴上首部对齐

27. Text('alignItems:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
28. AlignItemsFlex({ alignItems: ItemAlign.Start }) // 子组件在容器交叉轴上首部对齐

30. Text('alignItems:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
31. AlignItemsFlex({ alignItems: ItemAlign.Center }) // 子组件在容器交叉轴上居中对齐

33. Text('alignItems:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
34. AlignItemsFlex({ alignItems: ItemAlign.End }) // 子组件在容器交叉轴上尾部对齐

36. Text('alignItems:Stretch').fontSize(9).fontColor(0xCCCCCC).width('90%')
37. AlignItemsFlex({ alignItems: ItemAlign.Stretch }) // 子组件在容器交叉轴上拉伸填充

39. Text('alignItems:Baseline').fontSize(9).fontColor(0xCCCCCC).width('90%')
40. AlignItemsFlex({ alignItems: ItemAlign.Baseline }) // 子组件在容器交叉轴上与文本基线对齐
41. }.width('100%').margin({ top: 5 })
42. }.width('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/iBM_3MX0QjunezT_Ek2EzQ/zh-cn_image_0000002583439637.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=8B68FE59B284C50678550D05A6158FEC5EF7A60F89E5427960C0366FB75E6DB1)

### 示例5（多行内容的对齐方式）

该示例通过设置alignContent实现多行内容的不同对齐效果。

```
1. // xxx.ets
2. @Component
3. struct AlignContentFlex {
4. alignContent: number = 0;

6. build() {
7. Flex({ wrap: FlexWrap.Wrap, alignContent: this.alignContent }) {
8. Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)
9. Text('2').width('50%').height(20).backgroundColor(0xD2B48C)
10. Text('3').width('50%').height(20).backgroundColor(0xD2B48C)
11. }
12. .size({ width: '90%', height: 90 })
13. .padding(10)
14. .backgroundColor(0xAFEEEE)
15. }
16. }

18. @Entry
19. @Component
20. struct FlexExample5 {
21. build() {
22. Column() {
23. Column({ space: 5 }) {
24. Text('alignContent:Start').fontSize(9).fontColor(0xCCCCCC).width('90%')
25. AlignContentFlex({ alignContent: FlexAlign.Start }) // 多行布局下子组件首部对齐

27. Text('alignContent:Center').fontSize(9).fontColor(0xCCCCCC).width('90%')
28. AlignContentFlex({ alignContent: FlexAlign.Center }) // 多行布局下子组件居中对齐

30. Text('alignContent:End').fontSize(9).fontColor(0xCCCCCC).width('90%')
31. AlignContentFlex({ alignContent: FlexAlign.End }) // 多行布局下子组件尾部对齐

33. Text('alignContent:SpaceBetween').fontSize(9).fontColor(0xCCCCCC).width('90%')
34. AlignContentFlex({ alignContent: FlexAlign.SpaceBetween }) // 多行布局下第一行子组件与列首对齐，最后一行子组件与列尾对齐

36. Text('alignContent:SpaceAround').fontSize(9).fontColor(0xCCCCCC).width('90%')
37. AlignContentFlex({ alignContent: FlexAlign.SpaceAround }) // 多行布局下第一行子组件到列首的距离和最后一行子组件到列尾的距离是相邻行之间距离的一半

39. Text('alignContent:SpaceEvenly').fontSize(9).fontColor(0xCCCCCC).width('90%')
40. Flex({
41. wrap: FlexWrap.Wrap,
42. alignContent: FlexAlign.SpaceEvenly
43. }) { // 多行布局下相邻行之间的距离与第一行子组件到列首的距离、最后一行子组件到列尾的距离完全一样
44. Text('1').width('50%').height(20).backgroundColor(0xF5DEB3)
45. Text('2').width('50%').height(20).backgroundColor(0xD2B48C)
46. Text('3').width('50%').height(20).backgroundColor(0xF5DEB3)
47. Text('4').width('50%').height(20).backgroundColor(0xD2B48C)
48. Text('5').width('50%').height(20).backgroundColor(0xF5DEB3)
49. }
50. .size({ width: '90%', height: 100 })
51. .padding({ left: 10, right: 10 })
52. .backgroundColor(0xAFEEEE)
53. }.width('100%').margin({ top: 5 })
54. }.width('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/CJa_DI7_SsKW0Gcbkwf2PQ/zh-cn_image_0000002552959592.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=3CFA705F40125F0A8F978C1C4238054C081B7CC7C497EDCF6FBE87591DCBB494)

### 示例6（子组件单/多行排列时的主/交叉轴间距）

该示例通过设置space为单/多行排列的子组件确定在主/交叉轴上的间距。

```
1. import {LengthMetrics} from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct FlexExample2 {
6. build() {
7. Column() {
8. Column({ space: 5 }) {
9. Text('Wrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
10. Flex({ wrap: FlexWrap.Wrap, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) { // 子组件多行布局
11. Text('1').width('40%').height(50).backgroundColor(0xF5DEB3)
12. Text('2').width('40%').height(50).backgroundColor(0xD2B48C)
13. Text('3').width('40%').height(50).backgroundColor(0xD2B48C)
14. }
15. .width('90%')
16. .padding(10)
17. .backgroundColor(0xAFEEEE)

19. Text('NoWrap').fontSize(9).fontColor(0xCCCCCC).width('90%')
20. Flex({ wrap: FlexWrap.NoWrap, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) { // 子组件单行布局
21. Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
22. Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
23. Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
24. }
25. .width('90%')
26. .padding(10)
27. .backgroundColor(0xAFEEEE)

29. Text('WrapReverse').fontSize(9).fontColor(0xCCCCCC).width('90%')
30. Flex({ wrap: FlexWrap.WrapReverse, direction:FlexDirection.Row, space: {main: LengthMetrics.px(50), cross: LengthMetrics.px(50)} }) { // 子组件反向多行布局
31. Text('1').width('40%').height(50).backgroundColor(0xF5DEB3)
32. Text('2').width('40%').height(50).backgroundColor(0xD2B48C)
33. Text('3').width('40%').height(50).backgroundColor(0xD2B48C)
34. }
35. .width('90%')
36. .height(120)
37. .padding(10)
38. .backgroundColor(0xAFEEEE)
39. }.width('100%').margin({ top: 5 })
40. }.width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/WV_4ceKmS7O1mP1Yd81txQ/zh-cn_image_0000002583479593.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=721870FD40379B052A977B2B0FF8C0517D4D6B7E1290F6C6D2D7B8FA3294E14E)

### 示例7（宽度自适应的Flex容器）

该示例实现了Flex在宽度设置auto后可以自适应子组件布局的能力。

```
1. @Component
2. struct Demo {
3. @Require @Prop text: string

5. build() {
6. Button() {
7. Flex() {
8. Image($r('sys.media.ohos_ic_public_voice'))
9. .width(16)
10. .height(16)

12. Row() {
13. Text(this.text)
14. .margin({
15. left: 6,
16. right: 6
17. })
18. .fontSize(14)
19. .maxLines(1)
20. .textOverflow({ overflow: TextOverflow.Ellipsis })
21. }

23. Image($r('sys.media.ohos_ic_public_sound'))
24. .width(16)
25. .height(16)
26. }.width('auto')
27. }
28. .backgroundColor(0xAFEEEE)
29. .height(36)
30. .padding({ left: 16, right: 16 })
31. .constraintSize({ maxWidth: 156 })
32. .width('auto')
33. }
34. }

36. @Entry
37. @Component
38. struct Index {
39. build() {
40. Column({ space: 12 }) {
41. Text('Width does not reach max length').fontSize(11).fontColor(0XCCCCCC).width('50%')
42. Demo({ text: '123' })
43. Text('Width reaches max length').fontSize(11).fontColor(0XCCCCCC).width('50%')
44. Demo({ text: '1234567890-1234567890-1234567890-1234567890' })
45. }
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/BV9c4t6kQ_WSsPrwZMLX-A/zh-cn_image_0000002552799944.png?HW-CC-KV=V1&HW-CC-Date=20260428T000123Z&HW-CC-Expire=86400&HW-CC-Sign=C3FD338EEDB49BC3336CB88A11DAC833687B2274782B6F59F52EEC1B7C1E15F3)
