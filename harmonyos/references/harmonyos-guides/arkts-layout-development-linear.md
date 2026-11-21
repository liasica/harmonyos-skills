---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4f3c5f676bcf31828a31f4f638b693f9fb556ec6b808f0db703d30b547835bde
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

**说明** 

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](arkts-layout-optimization-guidance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Yax-xrTfQZ2jp4fzbvV6gQ/zh-cn_image_0000002793036450.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=38C7948F90D3A34112A47201F6CA850E4BEC6F5CF832820888F97E1EBFB0069F)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Q884A0ITRDCxxJMt3QfrRQ/zh-cn_image_0000002792876482.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C48984E2184256504818AA748C4E29AB25A5DB5CFCF410B1E5E47596EE062C2D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/7lehqsIuTzOAeXNMOUq8fA/zh-cn_image_0000002821836387.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F5C901BF00FC3BBB96038536E57D339376B97ADA45BB7D798A2C9C0E6DC2464)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/FdIw53AESCWHWaR7wL9BoA/zh-cn_image_0000002821756389.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9C775C9A7B7C558B39F7598913BF334B091FF5C283A04F7A52F9D805D0E4D85)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6syzx_JEQIGoL65m1xFQVw/zh-cn_image_0000002793036452.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=694DD86C46207696C742C4FD05F20114AB6AC253919D5A8CF2DD934EF086D2D8)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/O1l9a22_TeSFKQ4WOKXZ5A/zh-cn_image_0000002792876484.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C167B3339E963AE6BF0B112C4C8C084482D8AD4730F5026A53FDABE894B9DD95)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Aqa4Pn8PT8CzFKATuylVew/zh-cn_image_0000002821836389.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C802EDADD6E2B0C3DA24DF113D79A86F9307E571AE584FC0DF24F015591D93D2)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/xewcMvJdS1eq8_BO-4NEoQ/zh-cn_image_0000002821756391.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4E1E805D9C4A54B6B04846F40D688D4596E2DDA6275CF986A73E4E1CCD60F13)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Pt8edf3ETsOBlaGKzXw-dg/zh-cn_image_0000002793036454.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2382CF07641B26C8509A43888CE0D20825F7AD0F958D51EBDC17B1F6290CED6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/o9UreHPsSmmedqlYNG0Qvw/zh-cn_image_0000002792876486.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBACF3831EA5C229CBF39FDAEB24DCE1BC3EAC76D23AE9B468188813D6E92096)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nYoy2sfSTRCHhosAj2hAhQ/zh-cn_image_0000002821836391.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1C95A310B3507D7DE485AF8A96626102E6F69177A013DB7328DA8BD2547C471)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/zOknGj6hSmiHG53c55yvfw/zh-cn_image_0000002821756393.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C98FEFC76EBD4E8160B566F7FD1CF5FBB00C0D9F2063F127BB8DD967E563C194)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/r6X9BIGLQ8CVtNEdjSy3MQ/zh-cn_image_0000002793036456.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BE693062D2121B4C4785BC8F6FF4F886B6EC0A3CF40CF8E03016133C5A7F576)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/01tpyNkQSSKQQdBWt8hXkQ/zh-cn_image_0000002792876488.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BFC15E575CB8F1EA71FCC8C80AEC8F285DB09ECF5BADC8DD66ADD99AB843A6E)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/mxFCs6Z-Ty6n__cmnpm8_g/zh-cn_image_0000002821836393.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=8018DEC2BEE16B06D65146114145845638149E3403C08F023D1448159D6E2383)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2U3sW6QrSiqKHOPVZKpp9g/zh-cn_image_0000002821756395.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=07279769CAAD298E010E7092EE69EF9FB0E269B815D3E4A9BB441662A7762583)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-fgBJ-YnSW2PUS9caXA2PA/zh-cn_image_0000002793036458.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=70C32519452A7BCCD21346CE679A3DA98AFF4A9D77D53E202F2F97650D0F6FE7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/VmwgkdSSS-S6AYlLcVzK1A/zh-cn_image_0000002792876490.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=07CE3CF9C4ED8E5BE46C13CC049105015FFFB4E350C69B3FB35DD484BEFB71A9)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/-oIq0dibQ_CxzT8513t79Q/zh-cn_image_0000002821836395.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=240DD519B1F255235B99E8F36B218E80A5878E4F610045A45C4A2939F92771EF)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/wcB5JMh_RTiq-npnXc8JZw/zh-cn_image_0000002821756397.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=B16521F061B6B194A54757DD6A815249EFA94B688117FC0F24B3CF294559BA52)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Cgy0VUSqTqOFxoJ9bgXSRg/zh-cn_image_0000002793036460.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=44E9AA7996874EDA48DA2385BF12A7AB5E3E5AD51B5CE73ACB9C2D1552E740AD)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/9McW1qwVTrarYtjVHPYDTQ/zh-cn_image_0000002792876492.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D407D31D1F769038F6169906F47FCC95704263394071229B6A91FA28C4C5938)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/cI0NgomsRrWUqtikEE8Svg/zh-cn_image_0000002821836397.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=52338CB9CDF6A8BCF09B20F0EFAEBF6DC4F305B73D4F38CA4880E826F807FEE6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/OtiWKp3VTpm6lp_HgLes7w/zh-cn_image_0000002821756399.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=220FBBF56989CEF0168CD43300007EE59AEA66F4D032D4252F7D6A2D995C258A)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/qlHvt1zsQc2E3Tc3wgDP-w/zh-cn_image_0000002793036462.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D02B34D4B01A6382FAA44D0010B86E5FA2ECFE563837C22C5C89217B595457)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/gMjqdEO8SIOnjTX0I9kMlQ/zh-cn_image_0000002792876494.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=A63D699D41B039052521BEECA4471A0BC94766C6893A7C9DE0253B9852DD91D1)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/SAIyjMdsQ_imPahTB0sJaw/zh-cn_image_0000002821836399.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A46A8D65ABB0A6DA1ADF1EF34E6FE765D5D32DDBDF0CD0A2904023D784CE945)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/dtER04e2TNmVSeSzZFnb2A/zh-cn_image_0000002821756401.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E78DFFF5262B765492478BF08131F452C72151DD9B8BF9EF6A5201FFBBB4DD0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Ou2VmKOvQuKzHX8AgECacQ/zh-cn_image_0000002793036464.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E1064A0FD43F66BF3BBB7854BDB3FA31AFC0382A32E05C7911E26EBC4163678)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/-_jvbmMmSfC2eKBtAJxzyw/zh-cn_image_0000002792876496.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=C51D9C92DD7EA9FC74354FF1BE590CEAAAED97C424471B84770957B3C17AFD92)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/lI6jcCzHSDCsoELM3suHTw/zh-cn_image_0000002821836401.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=2713961782A86DF313D89C94B4656E6F3CAA8215E4E7362E51948C8FE5158991)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bGZP53QgQBWAGKzL2azqiA/zh-cn_image_0000002821756403.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B795884DE8F7DF8B8D5F2E82322039959165377B4A67786C3046B4023071DB5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/ubhxW26AT2uiK3lpu1o02g/zh-cn_image_0000002793036466.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C16301C4504A736E9D6F1CE3EE6906BC3B764712A1F3D9BA84B7D2D65205B4C)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_G4KXDjlRquIAIkkw52jiQ/zh-cn_image_0000002792876498.png?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=7424B1DAEFCC54CEC2CF3DA5BF7B0C3D8556FD4D459C4465B85010DB05D3AC5A)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/G5zccTczQb-3uQDd0XrqKA/zh-cn_image_0000002821836403.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=81A97ECD53C41EB43B412EB6BF1D696C6A27C12F81447478842C254CBCB41958)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/hX4X3fcjR4m2mEcc3ZGn9g/zh-cn_image_0000002821756405.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010941Z&HW-CC-Expire=31536000000&HW-CC-Sign=66BBFB3B5F2573F956362DD02D112B26CE286EF488EE1035D1A8FB6FA7C70535)
