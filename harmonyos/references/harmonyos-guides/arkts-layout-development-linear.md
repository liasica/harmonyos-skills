---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:30+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7547d6332980f569aa1774b316606f362f23efa81a3edd021f3af77e70d433a5
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

说明

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](../best-practices/bpta-improve-layout-performance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/61RZxjFDQjWcRwp7J4THYg/zh-cn_image_0000002583437739.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=874E02007B2A53791888044A456CCF9FFB0FBF4FB5BD4784975444EA4BBE3AF9)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/XZ06cIobTaOSJW5RX5vs1A/zh-cn_image_0000002552957694.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=86AD9828F31D17A2EC3FE1D2A223E0BE007CA695CFC64F4B4F8CE3E11F248D28)

## 基本概念

* 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
* 布局子元素：布局容器内部的元素。
* 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](arkts-layout-development-flex-layout.md#基本概念)中的主轴）。
* 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](arkts-layout-development-flex-layout.md#基本概念)中的交叉轴）。
* 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5klgF0UXS9CmvNSuTa17RQ/zh-cn_image_0000002583477695.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=C91E84EDF9B862CCDFFFCDA0264650ADD0785E8CA7D2BDB02887B972820D1194)

```
1. Column({ space: 20 }) {
2. Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
3. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
4. Row().width('90%').height(50).backgroundColor(0xD2B48C)
5. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
6. }.width('100%')
```

[ColumnLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/hxxszxCXSi-Ru7NE6c6Nmw/zh-cn_image_0000002552798046.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=2AC3DE0442A7C9380DF8A635461F25FCA348ADE0FA7F05AA9B1C8F5338C96169)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bwbVni88SAGhb0wB8HEAcg/zh-cn_image_0000002583437741.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=5FF97B64BD286B7C025129EE0F05E55A3B15F2F3FBC192043002269E24A7764F)

```
1. Row({ space: 35 }) {
2. Text('space: 35').fontSize(15).fontColor(Color.Gray)
3. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
4. Row().width('10%').height(150).backgroundColor(0xD2B48C)
5. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
6. }.width('90%')
```

[RowLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/TyIUirsbQbaud146yLUbkg/zh-cn_image_0000002552957696.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=0DDB0E057CD841C4FB184A9A44B6B3972114470DD5D3FBCC7EA202F050FD7D99)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/cB5puNxNQsmqXjhCI2kXUA/zh-cn_image_0000002583477697.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=B93471C956F7B255F38D502D93971391C6A88A895D3E6D4AA3F11368F6F7DC09)

* justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  [ColumnLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentStart.ets#L20-L93)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/xwLJmXlER1ijXWkPbhlH7A/zh-cn_image_0000002552798048.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=AD522197FF154622825D3062EDCFB2C052B83494B5F8A1B398EB884216A338AA)
* justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  [ColumnLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ASMbv_BkRzWfiTrn3TExvw/zh-cn_image_0000002583437743.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=3860CB42FADD1BE7BA3F723DEFAFF0C6ED58094082837B6EBCF6412A81A4F06C)
* justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  [ColumnLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/ODHOh2PYQc-60SE5ADxsoA/zh-cn_image_0000002552957698.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=35EECEA236002BB74E53DC59CBD275D5EC07E78CF319077992309B512886495C)
* justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  [ColumnLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/9yt5dbtVSXu_Tz8vXb7ejg/zh-cn_image_0000002583477699.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=FD3DF47DE1C6404F4C7432587A2EFCC9141CF64993109AB0DE275069177B406E)
* justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  [ColumnLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/yhu5xHHHTx-6yNfA_pEZ9w/zh-cn_image_0000002552798050.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=3640CE8884AA04B34F48C164DA455AAE04CD0A6913084D992098F4B968CD1120)
* justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  [ColumnLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/PQnx-cstS1iv5nPuJ9KIBw/zh-cn_image_0000002583437745.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=7F77AF4D17799C7EFFC956A4180FEEC405E644E459D9DBA28E6B877A092EBC89)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/-H7OSUsUQIK-XVm-h8Uvpg/zh-cn_image_0000002552957700.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=055F910B5309D30D7DCF35D8AAF158994F7D23F5F5ECEA258625DE149B359617)

* justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  [RowLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentStart.ets#L20-L44)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/_hes1vtASYC9W-1JMLdBBg/zh-cn_image_0000002583477701.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=9BD8980F499D3BBBFA6BBA1E5AE7E2B5CC3F3AAFD652E03202CA6F13A8497551)
* justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  [RowLayoutJustifyContentCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/8ySxGApeRYebGG9YW4Hfnw/zh-cn_image_0000002552798052.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=20BEDBB0845EE9246AED8B9D242554D144D9A40E77679427779212507337130C)
* justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  [RowLayoutJustifyContentEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/f-Jl-Hg6TvGYBVjhBBOSxQ/zh-cn_image_0000002583437747.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=18091B44BA5180E61949A6E03DB394FD86714E0A91520452F37CC2F04457F295)
* justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  [RowLayoutJustifyContentSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Y7Mb1HlqR1qD5WnIrT6ktQ/zh-cn_image_0000002552957702.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=8ECF346377FB66B8A54F9692C5F2097BABD01C84BA346613E330295707EE84FD)
* justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  [RowLayoutJustifyContentSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ndQvSqAERrCpAtzIxYfnJw/zh-cn_image_0000002583477703.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=0128D8B9CC8A784CED3C127DFE358BCBBE87962007C44311708910F96E0980F6)
* justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  [RowLayoutJustifyContentSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/z-Mmyat1RYyOzSuVQV7DzA/zh-cn_image_0000002552798054.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=3A615EFC58430A584B1498BD0D1D0D6124273028B5B22BB7B3643D1B11CA4D44)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Sqd2LHUVS3W5B6fra5cR3g/zh-cn_image_0000002583437749.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=D8C43D48A8507321B54C52662F4AA5EA23166CA57793368B8C692C69B9EE7985)

* HorizontalAlign.Start：子元素在水平方向左对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignStart.ets#L20-L76)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ZQ1V5vpxRf-MB4odp8lh3Q/zh-cn_image_0000002552957704.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=CA15D0B6BAABF910C198DF8EA497104B2C9BD2513AAB96BECA3BEAE909FFF86A)
* HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/gSy_iONJR4KqOkPDsIqxtA/zh-cn_image_0000002583477705.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=828D98990F706EBEE3904F0D6619F4EAD9C63DF16622C99BAAFA9AA474686320)
* HorizontalAlign.End：子元素在水平方向右对齐。

  ```
  1. Column({}) {
  2. Column() {
  3. }.width('80%').height(50).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('80%').height(50).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('80%').height(50).backgroundColor(0xF5DEB3)
  10. }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutHorizontalAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/7HfublNXSiu4z9rioIHy-Q/zh-cn_image_0000002552798056.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=601DCB7FD46FCEE2269E0D85E4704D3EB3E6E79C1F03AC0E1DD589FC2AA8D870)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7vTukyV0SZOnUtWkErR1Tw/zh-cn_image_0000002583437751.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=C01C26038E8DB320D91455601423E7A735C55A37273FD813EFBD3EFB6A85E257)

* VerticalAlign.Top：子元素在垂直方向顶部对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignTop.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Ltv9PzZLQquAAVFUCB70zA/zh-cn_image_0000002552957706.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=B81557E5CFB34F1DD24301A0818C129EFF834018EC8ECAECDFD8B00AC7834B22)
* VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/LXUT4he-Tz-wFZDSoQB0kA/zh-cn_image_0000002583477707.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=44B6B3848201431A92ACE4ED2C4FB75C5DCCD60D13C76CCF085862D4D7A34529)
* VerticalAlign.Bottom：子元素在垂直方向底部对齐。

  ```
  1. Row({}) {
  2. Column() {
  3. }.width('20%').height(30).backgroundColor(0xF5DEB3)

  5. Column() {
  6. }.width('20%').height(30).backgroundColor(0xD2B48C)

  8. Column() {
  9. }.width('20%').height(30).backgroundColor(0xF5DEB3)
  10. }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
  ```

  [RowLayoutVerticalAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutVerticalAlignBottom.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/gyqzFhlZSE2TvdvurksSpQ/zh-cn_image_0000002552798058.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=7190D1C70435D682CF125ABA3C6457597E95D4D8E74FF48910566D7CC99DA02C)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](../harmonyos-references/ts-basic-components-blank.md)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```
1. @Entry
2. @Component
3. struct BlankExample {
4. build() {
5. Column() {
6. Row() {
7. Text('Bluetooth').fontSize(18)
8. Blank()
9. Toggle({ type: ToggleType.Switch, isOn: true })
10. }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
11. }.backgroundColor(0xEFEFEF).padding(20).width('100%')
12. }
13. }
```

[BlankExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/BlankExample.ets#L15-L29)

**图9** 竖屏（自适应屏幕窄边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/gwfb-ErkRxOjN0XBr2P_QA/zh-cn_image_0000002583437753.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=996F2BB3D25A7790DB0D23691741B893FEC28989094231BB2D0CE6D7ACEE9E19)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/am2OJ57XTPKALnLByT2_3w/zh-cn_image_0000002552957708.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=F906518CD48AC3DDE7E197CA02A75336E60E6A8A452918F826E1649245924BA8)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

* 父容器尺寸确定时，使用[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

  ```
  1. @Entry
  2. @Component
  3. struct LayoutWeightExample {
  4. build() {
  5. Column() {
  6. Text('1:2:3').width('100%')
  7. Row() {
  8. Column() {
  9. Text('layoutWeight(1)')
  10. .textAlign(TextAlign.Center)
  11. }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

  13. Column() {
  14. Text('layoutWeight(2)')
  15. .textAlign(TextAlign.Center)
  16. }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

  18. Column() {
  19. Text('layoutWeight(3)')
  20. .textAlign(TextAlign.Center)
  21. }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

  23. }.backgroundColor(0xffd306).height('30%')

  25. Text('2:5:3').width('100%')
  26. Row() {
  27. Column() {
  28. Text('layoutWeight(2)')
  29. .textAlign(TextAlign.Center)
  30. }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

  32. Column() {
  33. Text('layoutWeight(5)')
  34. .textAlign(TextAlign.Center)
  35. }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

  37. Column() {
  38. Text('layoutWeight(3)')
  39. .textAlign(TextAlign.Center)
  40. }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
  41. }.backgroundColor(0xffd306).height('30%')
  42. }
  43. }
  44. }
  ```

  [LayoutWeightExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/LayoutWeightExample.ets#L15-L60)

  **图11** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Q37E5NM9QlmztCjHLcKw1w/zh-cn_image_0000002583477709.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=D483FEC273E152A590F4FCD9AE7CD0B92835E7ED0B267FC2EBAE7AFEAEE1726C)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/qT9_paugSs-Yx9HXPSzQ5g/zh-cn_image_0000002552798060.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=A3BC2E51940228FF7575F634B15CF9919DF8EAAA04C8293704E207BD5CC7F0A5)
* 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

  ```
  1. @Entry
  2. @Component
  3. struct WidthExample {
  4. build() {
  5. Column() {
  6. Row() {
  7. Column() {
  8. Text('left width 20%')
  9. .textAlign(TextAlign.Center)
  10. }.width('20%').backgroundColor(0xF5DEB3).height('100%')

  12. Column() {
  13. Text('center width 50%')
  14. .textAlign(TextAlign.Center)
  15. }.width('50%').backgroundColor(0xD2B48C).height('100%')

  17. Column() {
  18. Text('right width 30%')
  19. .textAlign(TextAlign.Center)
  20. }.width('30%').backgroundColor(0xF5DEB3).height('100%')
  21. }.backgroundColor(0xffd306).height('30%')
  22. }
  23. }
  24. }
  ```

  [WidthExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/WidthExample.ets#L15-L40)

  **图13** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/OowQRcz5TCafGEAfnqDALg/zh-cn_image_0000002583437755.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=4540B185AB5BAFDB6EB3EC38BA2F3BA5D88541593A6A6405E24ECD318DF6DE1F)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/oDwbSvxsTNyCscIiMwlHsA/zh-cn_image_0000002552957710.png?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=163526601861E6E4193D202AE837945AF3DF4EFD5E6738027BEA24B7ECBE2C30)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

* [在List中添加滚动条](arkts-layout-development-create-list.md#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](../harmonyos-references/ts-container-scroll.md#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](../harmonyos-references/ts-container-scroll.md#edgeeffect)属性设置拖动到内容最末端的回弹效果。
* 使用[Scroll](../harmonyos-references/ts-container-scroll.md)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

  垂直方向布局中使用Scroll组件：

  ```
  1. @Entry
  2. @Component
  3. struct ScrollVerticalExample {
  4. scroller: Scroller = new Scroller();
  5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  7. build() {
  8. Scroll(this.scroller) {
  9. Column() {
  10. ForEach(this.arr, (item?:number|undefined) => {
  11. if(item != undefined){
  12. Text(item.toString())
  13. .width('90%')
  14. .height(150)
  15. .backgroundColor(0xFFFFFF)
  16. .borderRadius(15)
  17. .fontSize(16)
  18. .textAlign(TextAlign.Center)
  19. .margin({ top: 10 })
  20. }
  21. }, (item:number) => item.toString())
  22. }.width('100%')
  23. }
  24. .backgroundColor(0xDCDCDC)
  25. .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
  26. .scrollBar(BarState.On) // 滚动条常驻显示
  27. .scrollBarColor(Color.Gray) // 滚动条颜色
  28. .scrollBarWidth(10) // 滚动条宽度
  29. .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  30. }
  31. }
  ```

  [ScrollVerticalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollVerticalExample.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/NDrkq4UoT6eNyhbMp3fmTg/zh-cn_image_0000002583477711.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=2445E148BA0335376F433424493CFA1B4727C52072E0C9CC9FC1EBB3515440E1)

  水平方向布局中使用Scroll组件：

  ```
  1. @Entry
  2. @Component
  3. struct ScrollHorizontalExample {
  4. scroller: Scroller = new Scroller();
  5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  7. build() {
  8. Scroll(this.scroller) {
  9. Row() {
  10. ForEach(this.arr, (item?:number|undefined) => {
  11. if(item != undefined){
  12. Text(item.toString())
  13. .height('90%')
  14. .width(150)
  15. .backgroundColor(0xFFFFFF)
  16. .borderRadius(15)
  17. .fontSize(16)
  18. .textAlign(TextAlign.Center)
  19. .margin({ left: 10 })
  20. }
  21. })
  22. }.height('100%')
  23. }
  24. .backgroundColor(0xDCDCDC)
  25. .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
  26. .scrollBar(BarState.On) // 滚动条常驻显示
  27. .scrollBarColor(Color.Gray) // 滚动条颜色
  28. .scrollBarWidth(10) // 滚动条宽度
  29. .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  30. }
  31. }
  ```

  [ScrollHorizontalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ScrollHorizontalExample.ets#L15-L47)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/yM8HBdMvTEaGK2-ZdDV53w/zh-cn_image_0000002552798062.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233928Z&HW-CC-Expire=86400&HW-CC-Sign=34C66B0C7A9F9408895FA7B4F77775E097D28DB61F0576735197C2E95BECB7E9)
