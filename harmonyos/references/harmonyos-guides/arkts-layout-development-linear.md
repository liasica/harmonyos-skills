---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:398199f7e90065cd5f832b48ec642c708cddb1b6450c8708fb9934edc97881ce
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

**说明** 

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](arkts-layout-optimization-guidance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/XhcwG7csRbCyVZ1hxIYsew/zh-cn_image_0000002817505933.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D366CA1883D9F3852B95900C6FADF5159BA439F51FDA0B5C20F9E88D07F2A20)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7NwrZOS8Qv2BLMZKMkhgLQ/zh-cn_image_0000002788306504.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCC8B59273A7E346B24D367FBB0A3CBF3EA54D98A83C896DC627DEF3DAEB6888)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/E1xoDGF2RNe8WRcCL4clig/zh-cn_image_0000002817425867.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC82B3E3F85B565DC31B5E1CF45DB4A9AF5190352C06FB8D6DBB165A2F75BC6D)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ebPP9hBhTQOWE2g3PQujUQ/zh-cn_image_0000002788466448.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=47540DDB92B10E95FAC0C1A0902928805DB4B5C8AF713BA21D435F8F4A259CBE)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/rpcwSfF-RGa4IAdCYB24Uw/zh-cn_image_0000002817505935.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=6165E712332041F6E90033AF7F5C6473D8B0D11592200A735C6831935882059A)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/flyEXMpTTamhXCfRoJ388w/zh-cn_image_0000002788306506.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=D53C52908C886624DE055BB0A029B679A6C8175F33416E1C25A52E3E1D60B77D)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/muPunEyUQYSwEqzjaDU5uQ/zh-cn_image_0000002817425869.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD0A8CBF0AF2035092ACBDDD805ABA0FC1C9336CA50403841A33C8D0A994C3B6)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xl28pTflQ7OfeEDpJ4_Oog/zh-cn_image_0000002788466450.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A0F0715D6F212910D6780AD6CF15F57357046F93C0A9525F57D0BEA8C4B4C88)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/srSUuQPyQ-qDhb3q-_cjvg/zh-cn_image_0000002817505937.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A67E085EAEFA489A864340EAA28F7DA105F6892531231FAC2B0089F177A6805)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/3HSbUH2MRTOQOIaquCka0w/zh-cn_image_0000002788306508.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAA441FB2FEE9507777C3869FBE8BF3D7E842BC3AE726466A2E81CA4AF24C982)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/SS4hvvyKQtqXK8QNrMBnCw/zh-cn_image_0000002817425871.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=A88F421DB80490A0909F0C1106065BFA64DFB34BD0321D8AE506B136B4475338)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/2Vy82nqfQ06xK1jeYtkYfQ/zh-cn_image_0000002788466452.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=A70051D105C6DF8BB62F7EDCECD3D990BDFB4C58D38C081FFB23DB964626DE32)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/THbZvXmGRv2WKw67HdpmMA/zh-cn_image_0000002817505939.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=964739578404AC10DF2088EF136230C4B2D7C1AD4D776A9DF5FFD0D3EF33A979)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/bbZ6DhwjRNaHdQspZI6zFw/zh-cn_image_0000002788306510.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD33439D8CE2B1D3B23C18D8CFD2B36CAAF973BDF48ED11FBACB568A26E055A7)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/qlfxVRpbStKV7qG39sk3rQ/zh-cn_image_0000002817425873.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5658B396AC94E0067EC791AE45E1CADD84C7D2FF970885537748C86741DC520)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/joUsoe5GT1GyjcSslCcSZw/zh-cn_image_0000002788466454.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=41D6EC663864364374BFE4D78C7B5907201F689679DF56CDF72822AFD62E3CD7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/HYGPiZjJRT6j43j-4dtdSw/zh-cn_image_0000002817505941.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E2A8997DC06BD0A57B75C66C5415E9E992B9296530A0E6B075B8647B012BB2C)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/PrpS3R8KQDa-RaIcP2oQDg/zh-cn_image_0000002788306512.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=1277DBDD4FCEB864AE5C0B59DEE40927C4879D729FB37F32BC5D5280759CC9F5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/dmvm4Y9uSbuctf-BycPaBA/zh-cn_image_0000002817425875.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=86BF2D5FBD8340811E238498A675FD1B07C36C8E35A3874D3C91B186927A1043)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/4GcckbJvQtWjQ7Zs_nuiag/zh-cn_image_0000002788466456.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FBC66DD3EEB5D727D63C0BAC8FFF5EBD4FC3B1316C61D518E59197FCA1700C8)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Rm6VSEgXTIC1I8tb6S6WkQ/zh-cn_image_0000002817505943.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E6590789DE6DA2B0D0B49C52B226E72E5FD124F21E4541032FBB319754C2819)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/TicAUsvGTPSIeT1hbF9GrQ/zh-cn_image_0000002788306514.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AC69967B59D9A91942025EBE45B4B42A38C00554548CB07413D56FEAAFFEAC1)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/eEFO4njiT86sQLLjPNuSwQ/zh-cn_image_0000002817425877.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=87523D9C2C07C7AF2975D60915F4B55BDF0F3DD156A2FECE1E4CBE50CC440A71)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/BwFo6LPLRlmRSRIj6VQWJg/zh-cn_image_0000002788466458.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=655384EB455FA000241652E6CF2E21FB8F2EA79D1354910C5EFCFB414B9A56C3)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/lIIAWVnQRqqe6TFPGUCbnw/zh-cn_image_0000002817505945.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=74BE02AFD12F43439DC8BE72A40ABC500392CDDF750F98C655FC1A59AEB9807A)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/6a0gg8k0QheU9u5SzWYMIg/zh-cn_image_0000002788306516.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=A277F0F7F8B4D07C998CAB48A2E5DEA983CCE268BB62733E17F0BE91AC4B5A1A)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/qdW4iQrdRMSK0qOnCXWJTg/zh-cn_image_0000002817425879.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9AE2B92AEA3BC43E7D1BBEA73881F368A6E45777660C52323D23BDA9A1A3624)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/UR0OMlg4RhC3txRI1VoH0w/zh-cn_image_0000002788466460.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA92F1EBCE3961DF8DE611FAC791A3C0AF9C92B110FC52C8DBB2AB4CA18D1E96)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/21AqtMdCTSG4VVXlZu_s_A/zh-cn_image_0000002817505947.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DDC6D26B29F00AA8E87BED8C051F5B7AEF36E46C8E42D6385B9AD70C9E0CF5A)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/bTyomu28TyKyaLQQhi8uig/zh-cn_image_0000002788306518.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=5297E21D4DE6C775556705A77F950BC79E50CDAC4D6595F5DFA1C59D842E0648)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qK1PTxIeQ1CzOJQWPEDa8g/zh-cn_image_0000002817425881.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=8310D802A3653BC9AFF1374C08933697D2D37098BCA554334F058E8736F3EF71)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Wp31WaaTQsuss8-kyzKhjg/zh-cn_image_0000002788466462.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=21FD44F59C1EAB8749CD4F31111D38FD0212ED40674849E500ED26705CE72297)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Fxbwt0GHStefWtoepRCciw/zh-cn_image_0000002817505949.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=56CCA54E94B34E265F3405DB8D3CF188CEE88B921FFA19CE116AECEC31DC775E)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/bmBLZUhhQZeAi67qP4S0YQ/zh-cn_image_0000002788306520.png?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2F200499EA7E9176B01F2079EB6D4053CB7593E496D3E711EFD3A17DF909FC0)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xM7QulM3RROA8mMFMuiHKw/zh-cn_image_0000002817425883.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3DAA834AC242DBE020A4C5239267499C9221B3F312A5B745C6A6DBB1532D15F)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/numalEVSSJ-wXbtwKWlaIg/zh-cn_image_0000002788466464.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004524Z&HW-CC-Expire=31536000000&HW-CC-Sign=B47E9AFC848A5086B6D58643ECD48BB8CCB08F592EC0D1FDD6ECD1BF67A57CDE)
