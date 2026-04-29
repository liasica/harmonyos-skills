---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:39+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:eeb2b68ae9fcc971d4f7279588205e3dab164d26afa892ca5cbd0ee9cd5d099d
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

说明

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](../best-practices/bpta-improve-layout-performance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/BPHu9Zq6T4yVVW8VULosmw/zh-cn_image_0000002558604528.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=0BD439A8E07658D0D5085C2993FAE5C773D9A51E9619C124ECFB7703AF3EB281)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/U8lpIzQpTHK3psR-UZWEaw/zh-cn_image_0000002589324053.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=7B8F243FEBA55B34E183F9389C04F2805FD2292F23495B8BB3D6E78E99C1A15B)

## 基本概念

* 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
* 布局子元素：布局容器内部的元素。
* 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](arkts-layout-development-flex-layout.md#基本概念)中的主轴）。
* 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](arkts-layout-development-flex-layout.md#基本概念)中的交叉轴）。
* 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过[Row](../harmonyos-references/ts-container-row.md)组件的[space](../harmonyos-references/ts-container-row.md#rowoptions18对象说明)属性或[Column](../harmonyos-references/ts-container-column.md)组件的[space](../harmonyos-references/ts-container-column.md#columnoptions18对象说明)属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/-zttnzJXQBmtVFn96Pt-Kw/zh-cn_image_0000002589243993.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5FA1758C1FD5247B1F3F1E80CC66046C164DC9618209164B4D91164D123FF45D)

```
1. Column({ space: 20 }) {
2. Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
3. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
4. Row().width('90%').height(50).backgroundColor(0xD2B48C)
5. Row().width('90%').height(50).backgroundColor(0xF5DEB3)
6. }.width('100%')
```

[ColumnLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/UT6hJMKQSeCw6_Q0YJva6g/zh-cn_image_0000002558764186.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=2D4B20C1B05D6062B2EDDAE5FE2B988420A92329A66F84BB2DAC9864DC3131CF)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/gaQ-9NE7SHqZK5B_SvwbpQ/zh-cn_image_0000002558604530.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=B102E53985532BDB24D4D50F98EAB3611C09B6D4DD5C5BD440713350E8E69EE8)

```
1. Row({ space: 35 }) {
2. Text('space: 35').fontSize(15).fontColor(Color.Gray)
3. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
4. Row().width('10%').height(150).backgroundColor(0xD2B48C)
5. Row().width('10%').height(150).backgroundColor(0xF5DEB3)
6. }.width('90%')
```

[RowLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutExample.ets#L20-L27)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/8CWXlhnzQWOsgHvKqspskw/zh-cn_image_0000002589324055.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=E937A24AAEE0CB369D59FB8A8E02E5DFDFED7BC46B4A670F1D0463C62D2AC020)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ikbHKaahSreXmS0kU29N_w/zh-cn_image_0000002589243995.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=A136837A61A71F8014881318AC600CB820FDD3B91257FEF469085F7DB4A4F42B)

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

  [ColumnLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/ColumnLayoutJustifyContentStart.ets#L20-L164)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UnEbcs19Sp6f4JtDgRJBNg/zh-cn_image_0000002558764188.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=BE9FCE5601A5F7E13AB14850719B672DE1F8A93CB0AE288A9FDCDC56BF5BAACC)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/NvzojBLsR4ypnmBehmxWdQ/zh-cn_image_0000002558604532.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=CC6674EF3E48A617D8D171CEF8584896E3178E5A7B3B655085AFA631DB69AB32)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/BvMz2mOQRgC_NwcramVHjQ/zh-cn_image_0000002589324057.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5DF67C176CCBE8A8097182E8B38DD2FD6E2E217037798A02CF1CEA16694EA175)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/B__YjFwuQG-uy0eHR8XOSg/zh-cn_image_0000002589243997.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=39DFCC6EBFB21935743F886031CED5739BB460D4D3C2F84B7195F91DC8EC1CDD)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/NRjt-iizSM2jbauZj3NRHA/zh-cn_image_0000002558764190.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5C3C979E549C6F854ECEE9763EC0AFA32C4FEC3DB11084A2930E04FCDAA9C420)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Lc_9OezgTlaHAC7pNLJEjQ/zh-cn_image_0000002558604534.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5DD334E3E8408960CA42EFFD32102E7CFC9293C3144AAB0D0F2875A474743E5D)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/iuJhoctNQt2iWx1_cYiKjA/zh-cn_image_0000002589324059.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=529FB23F13CBDE13D48CE82A9E5F547B93549EE2B32FC489AC4F55434B3F5D46)

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

  [RowLayoutJustifyContentStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutJustifyContentStart.ets#L20-L146)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/LqRpnAHRS9Se5osgdNGC3Q/zh-cn_image_0000002589243999.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=D95092DCF94E2D7E663D44ABB3A7D94D29B9BB39ED618F1706938272EFCF1834)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/iQtDnyHmTMitrW17PVKqMw/zh-cn_image_0000002558764192.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=B6AB3E5CEF9906C81C3283B018D99C93F3CCD76F071CB2E0D24BD5A66E0AE7C8)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/jghS6_S2QgeRG_QMZhOgog/zh-cn_image_0000002558604536.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=FB06777D75A76971FFEED7F9ECE7A0D99058D38C4B4C0EC569D4AA4B470C79E5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/TVMYlm5MRI6xGNWk9TCd4g/zh-cn_image_0000002589324061.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=F3A104C280B21F35347CBFD57C9ABA630AE31F7BCF946F4A0E3E1C618B8173CD)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/540PHJozR3Ksq12oHMsOjA/zh-cn_image_0000002589244001.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=4732ECCF9CBD8AF2D747AD15914203CB102C015128CE1744BA5A7770F2D24DBA)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/OXS89gkHStOd5NrsSaDeBA/zh-cn_image_0000002558764194.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=717545EC10303D5507B13528968E3A61AC5B8FEA4D1DB121AC1F4FC14792F5F5)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Hg8WFGOWRLWvYUM95dnd3Q/zh-cn_image_0000002558604538.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=414D143F20A976D61226C79C21FCE410C4B01B5C7A70209C15A9C9E5C4659981)

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

  [RowLayoutHorizontalAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/linearlayout/RowLayoutHorizontalAlignStart.ets#L20-L74)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/6U7-mzgsSxirQhYogfrxKA/zh-cn_image_0000002589324063.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5A4717BDC8DC45D8C1B6C31F5B7AF9B9612E1A5848D380E3C774FA2EDFDF61F9)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/Vv3djp_3T9eMyEyELp4rUg/zh-cn_image_0000002589244003.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=D9521BDFC54057D01C3974D85890122856B4703CA92D387E77B2045B9E48A5B0)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ZgEHoh_bTzWGVgvxOH9whA/zh-cn_image_0000002558764196.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=B297CB9F4D0BD898DAE4B7B38FB048FE82F11AF735AF9460ADE4EF3CC54479DC)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1Ixx_nNARi-wsCLLJLuUSw/zh-cn_image_0000002558604540.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=06B0F33C103A6558CA6B554F85BCDB51AEE43428773CEA8669BC6389B849ACEB)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/m0l4-PKuSZqTbbnpKbl34w/zh-cn_image_0000002589324065.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=0267E93C4EB4975AF62506DDB911E01A266B5ACAAE126B151148B10702D37C5C)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/MBj3ZtonRsyFnsneOQzmlg/zh-cn_image_0000002589244005.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=CC1D341E2946968FAC61DE3314A01223DA06C0AE87E6079AFDD67B49F6D2F4FD)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/jrkh6syRQuOCv3AIze5Ghg/zh-cn_image_0000002558764198.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=ED69E012A9C6AB32B2A36CE578EA2C6EA97939997C117D70B9689ADF0EDB5A6C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/AkmEB-wHQuGwxcg3zTz_YQ/zh-cn_image_0000002558604542.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=E010013A7D08419C41F0301EF9D02F232AABE18774589D72781CB93628D3572F)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/5lg6WXuhT8CP4KlTOwkrtg/zh-cn_image_0000002589324067.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=2F231F0B00C7E4DA23A244C8CD3A014DEB87FEFBE100C4D0063E5EB70A6B20B7)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/8r1WSO6WTvyd45L5KipifQ/zh-cn_image_0000002589244007.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=C3319124E321D1FA9C8F6CD53B77CE55EDDA09C28079B4903B887FF445290249)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Kt3rB8U-TVKChm5mIr9Ruw/zh-cn_image_0000002558764200.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3606C48286F164C11515E3BD2205B8860F3FDDEAB73BD00F0E8000A0302346D6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/g1cOH6F2Qwq71i4QTzZHwQ/zh-cn_image_0000002558604544.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5377D5F0A85A0A9AAB8B64C05C7775F9F1B1DE75C19249B0FC7A46E8773707B6)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/3-O8suVvSWuNv8FNBPqv1w/zh-cn_image_0000002589324069.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=64C4C63B441391D9B3B0DE6BBB729748DB25A23AD2B8AF98B31001AD6CC18B0F)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/7viPQkgERbudLlnOviud1A/zh-cn_image_0000002589244009.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=1DC88C9A483BE8BCEC091D5A78E178FBE792AE6C5F59C9C5D2724B2B0C825354)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/6YCmaJU_SrK5bMwVwCmgEQ/zh-cn_image_0000002558764202.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=8BB1521229F96B148139192BB6AB9C7173F2A4BFC5728B1076F2ACC778675F95)
