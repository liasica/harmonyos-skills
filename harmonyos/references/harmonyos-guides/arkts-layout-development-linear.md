---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:94b60f0546dc184979711dba7f26fa23d02af5b05348ffe5a7810a37b977431b
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

**说明** 

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](arkts-layout-optimization-guidance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bJuOayk5T5uxTHoYNgtmUA/zh-cn_image_0000002820524783.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD27B3C43312DCADBA925A052613CD14060814E2F49A5B19A908635DFDD6FAF6)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ewKWMND8SnWaCA1UDIdwrg/zh-cn_image_0000002820404781.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A3D5A051DA445A84339F76896B6489D95772734E69A962A5388A3DBCFC42ABB)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Z_VfqVw3QKqLmlR0mCa1eA/zh-cn_image_0000002791724804.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=B57506896BCE67935E37A7EE0FAE76F8014F5326C8EB73EC7CE3E4FFD2EC4367)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/w-fn2vHlSJ6dQXS3Ivu_Bg/zh-cn_image_0000002791564832.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFE4BD40A0AA9AAA2B6D9D9D2AF08D2232A2B539C240513AC6141C1BA1A25C08)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-h2nlSEGRAKcxIJbICFwBw/zh-cn_image_0000002820524785.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=E79B7384A7983C78A5B0FFCED95A2FE1F0B3ED94119159F4AC27992A65BCE051)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/yR0PpWA9TOKj7nv95aQQXg/zh-cn_image_0000002820404783.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=76FD81CFD953DC695254FC96140E3C97006FD63818578BDF65C31C43EDC3A9AD)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/7d2smoxKRQCMEVSl6lKN_A/zh-cn_image_0000002791724806.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA435ADF80B67EE7A5896C585B555F27A8C4D52D00EF73B481F52CC55BED7963)

* justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zMd2vmFnQfG3_dVax-AspQ/zh-cn_image_0000002791564834.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A377D0135672986516F0FA54887594123BAD55694E955596A70CF2A4947F712)
* justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/1BqjTUY9SpqaaZzgZHUA1g/zh-cn_image_0000002820524787.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD5C8073EEEDABB0DD14E82A782CDF1989D2A17A50EC28585F65CBF564BE5A8D)
* justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/FFmMBijsTqqdLpZnbmtACQ/zh-cn_image_0000002820404785.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F8E86BF7A58D9E28DECFA5131726374F8A4A0965BF76F8B5A4CB6A121A24B15)
* justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/eNI9JUfbSZySAa7_rVT2vw/zh-cn_image_0000002791724808.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCB02DCA8194777F7C004DB19DE1C189B17AB351CF63765505A8E3335ED04CC9)
* justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/xqs30nF2Rm2xDNBQRqbCLg/zh-cn_image_0000002791564836.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=619B258F8D46D30FB16FDBDCE8DCDAEF06933C5D1C181950F0BA422FB5A682C1)
* justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/XSCvWgRURPG3-QXbR0pbuA/zh-cn_image_0000002820524789.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AB96A9D2185E32C4FF279F084C55162F46D34603C352DC2E9E13FE5DD460D53)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/1EKfU5iCQW6VBDvw0DukkQ/zh-cn_image_0000002820404787.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CB64D63BD06786CAAE3FF0EE02D04330C7D4970DB0AA3DE4FEEB46A95375FEC)

* justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/G3FUXzCRS7Ob9azdiQvMTw/zh-cn_image_0000002791724810.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB7A48F837BD006E60CAC232709F81F7232823D7D21AD85ECDE41AC41B617E44)
* justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/naD1EwjGRPOlV2Bt_nw-Gg/zh-cn_image_0000002791564838.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C81A57D7BD08B17D07E8FB4F564D2F34207659ACEBB2C708E6975D4D5C65AE8)
* justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/7b5X-UbxTZSQv5j2voj1kA/zh-cn_image_0000002820524791.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FF2508D3237C854C57287C56AE75AB5FD188946B954F102DD09B06601215667)
* justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UNySABYiQy21xNg2x7BXuQ/zh-cn_image_0000002820404789.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=E80DA1AC9229DCD49911DE781CA79E339E6F302C2EE881104CA99B1B3DF91875)
* justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/N4bEcU5GRSa2BfnFudGrVQ/zh-cn_image_0000002791724812.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EA20074DA5906B8B9643D6BF17DDF13B1013DD1D9F9BA876CFA9DA08FC962D0)
* justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/e8LKMEm2RSCmlSu9oAysrg/zh-cn_image_0000002791564840.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=061BD7DDF34CFD9CA5551CCE7DAE0C23F101C72B330FCF95FF9603B0E75B55BE)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/EVOjmEloRgmwnZAmm50h4w/zh-cn_image_0000002820524793.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B4B016BF3E5AD75FEA909329A09E428C7F41CA643DDEEA666057ECE4591C142)

* HorizontalAlign.Start：子元素在水平方向左对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/OK02xutyTb-trCZadGO14A/zh-cn_image_0000002820404791.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=C08DA98483BECD6F12FC98FF9990A082E2D2BF08036C71DC734B51713B77E4D9)
* HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/FNWXShoGT1q_9qJ7TPhu_g/zh-cn_image_0000002791724814.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=76B3E5A731F0084735406CB87D37D7B63EB1EAB02B79C336AE909BC4F0D51EDD)
* HorizontalAlign.End：子元素在水平方向右对齐。

  ```typescript
  Column({}) {
    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)

    Column() {
    }.width('80%').height(50).backgroundColor(0xD2B48C)

    Column() {
    }.width('80%').height(50).backgroundColor(0xF5DEB3)
  }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/WF-srh5UR2-XYLCsM5La0Q/zh-cn_image_0000002791564842.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=65D4D2B5427EB4E9290A03F1555780AFEBF728C050F05E4B2BC8B2BA80470853)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/XXXknQCcTTiXgBtrH3g8Tg/zh-cn_image_0000002820524795.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E1A4CC830B338FB2AB9804115F151C021D0ACDED98F9DE9E35A0C72A1BD63B7)

* VerticalAlign.Top：子元素在垂直方向顶部对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/xi6L7HnLSq-NzgS3l27oHg/zh-cn_image_0000002820404793.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=E61391B776F989593815ED4F184118068AA8F1795AF2A664D3D7C170A213F03C)
* VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Yqo7Pby0QtC2xU65KvR5kQ/zh-cn_image_0000002791724816.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=4873EA08EA9553E779711A673DD149832CC8CA52663330C2F209470EFACA0EA8)
* VerticalAlign.Bottom：子元素在垂直方向底部对齐。

  ```typescript
  Row({}) {
    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)

    Column() {
    }.width('20%').height(30).backgroundColor(0xD2B48C)

    Column() {
    }.width('20%').height(30).backgroundColor(0xF5DEB3)
  }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/msRRlKkiRoSovlS5fnPcSg/zh-cn_image_0000002791564844.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=D68FE69B8113797564DA51AE0927F285451B73D953CAB096E639E2AB40565491)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](../harmonyos-references/ts-basic-components-blank.md)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```typescript
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

**图9** 竖屏（自适应屏幕窄边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/leS1xWf0QD6XDoZ61RJ2iA/zh-cn_image_0000002820524797.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F8069A63F1F7EA9C9B8D594D2EC9ABE6AD442E5A7156A4027B4922EEC0B6202)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/_f0ESitwSRClSPGjPKWyiA/zh-cn_image_0000002820404795.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1D304CC9E41880F0DE743C2700A65952D0C21535719F57F1A27AC9FBD9FE4B6)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

* 父容器尺寸确定时，使用[layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

  ```typescript
  @Entry
  @Component
  struct LayoutWeightExample {
    build() {
      Column() {
        Text('1:2:3').width('100%')
        Row() {
          Column() {
            Text('layoutWeight(1)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

          Column() {
            Text('layoutWeight(2)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

          Column() {
            Text('layoutWeight(3)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

        }.backgroundColor(0xffd306).height('30%')

        Text('2:5:3').width('100%')
        Row() {
          Column() {
            Text('layoutWeight(2)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

          Column() {
            Text('layoutWeight(5)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

          Column() {
            Text('layoutWeight(3)')
              .textAlign(TextAlign.Center)
          }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
        }.backgroundColor(0xffd306).height('30%')
      }
    }
  }
  ```

  **图11** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/zRm7oKKfSpCb69YYWWkVNQ/zh-cn_image_0000002791724818.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BD3D8A7A72C0F3F5AEEF729CB72B256EA1218875989B12CA170F9122AF4BC1A)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/mVb0Xv7URnWuRcQNP9YxlQ/zh-cn_image_0000002791564846.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BCCF9E3AE5BC33491479D1078137AD510010B1D6545411B2F528FA36B6059A0)
* 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使它们在任意尺寸的设备下保持固定的自适应占比。

  ```typescript
  @Entry
  @Component
  struct WidthExample {
    build() {
      Column() {
        Row() {
          Column() {
            Text('left width 20%')
              .textAlign(TextAlign.Center)
          }.width('20%').backgroundColor(0xF5DEB3).height('100%')

          Column() {
            Text('center width 50%')
              .textAlign(TextAlign.Center)
          }.width('50%').backgroundColor(0xD2B48C).height('100%')

          Column() {
            Text('right width 30%')
              .textAlign(TextAlign.Center)
          }.width('30%').backgroundColor(0xF5DEB3).height('100%')
        }.backgroundColor(0xffd306).height('30%')
      }
    }
  }
  ```

  **图13** 横屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/bkqaDGQxSx-kAjXBz2NZ3w/zh-cn_image_0000002820524799.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A92E9B35A66CA41D740D50BEB9F09A3DF9B515A84302A9B4476A19FDD8C1839)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/1Y2AeyRaTM6gAf0QDODLFQ/zh-cn_image_0000002820404797.png?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BB2A77DB4439E7E51AB16D8A5F9070D44AFFEA16ED9273445FBC0EB55FC9E14)

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

* [在List中添加滚动条](arkts-layout-development-create-list.md#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](../harmonyos-references/ts-container-scroll.md#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](../harmonyos-references/ts-container-scroll.md#edgeeffect)属性设置拖动到内容最末端的回弹效果。
* 使用[Scroll](../harmonyos-references/ts-container-scroll.md)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。

  垂直方向布局中使用Scroll组件：

  ```typescript
  @Entry
  @Component
  struct ScrollVerticalExample {
    scroller: Scroller = new Scroller();
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    build() {
      Scroll(this.scroller) {
        Column() {
          ForEach(this.arr, (item?:number|undefined) => {
            if(item != undefined){
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            }
          }, (item:number) => item.toString())
        }.width('100%')
      }
      .backgroundColor(0xDCDCDC)
      .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/KH462egBRfeywzOQTn13kA/zh-cn_image_0000002791724820.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=D68E4A28D9F5156A952630763C71C43382A6A8614936BFF10566149F5B0A3421)

  水平方向布局中使用Scroll组件：

  ```typescript
  @Entry
  @Component
  struct ScrollHorizontalExample {
    scroller: Scroller = new Scroller();
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    build() {
      Scroll(this.scroller) {
        Row() {
          ForEach(this.arr, (item?:number|undefined) => {
            if(item != undefined){
              Text(item.toString())
                .height('90%')
                .width(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ left: 10 })
            }
          })
        }.height('100%')
      }
      .backgroundColor(0xDCDCDC)
      .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
      .scrollBar(BarState.On) // 滚动条常驻显示
      .scrollBarColor(Color.Gray) // 滚动条颜色
      .scrollBarWidth(10) // 滚动条宽度
      .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/m1BWyV4SS7ymHuHjuyKBbw/zh-cn_image_0000002791564848.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014739Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A7DF2CEB4F1559329EED06E60971AF0823294B22CB84E68C0AB1223F77CECF1)
