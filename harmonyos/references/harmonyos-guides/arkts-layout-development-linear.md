---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear
title: 线性布局 (Row/Column)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 线性布局 (Row/Column)
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:09a42561dbdafcae626651857409513c912093799b0b1521f9f9d1b93834ba7d
---

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

**说明** 

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](arkts-layout-optimization-guidance.md)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/TaeJfyExSPO3-EQO_vP7yA/zh-cn_image_0000002815398275.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5664C61463FCA91ADADED89A7DE6DAF6C95105961F8E8CD1722266581238F5B)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/iYTzNqhVS46VNeKlRLQACA/zh-cn_image_0000002786518700.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA25710F49914EC20C87456A76ED594CB0F6C5622521E99CF1EEFE14DCE1820A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/y7FWgFs2SliPH9YtuqdITw/zh-cn_image_0000002786358772.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=99BFF791395D6EE84433585DB0CF74DF9F220B0DE93F73A15C56345C9FB1649F)

```typescript
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6KbwvkZfQWmHL6oJYXJsdw/zh-cn_image_0000002815558193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C501323928541391FB52170DE163007EC1F225A30B703BDC596E46E8E4EEAAAC)

### Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Y1JnxA3dR1uUQV1vJfxwyw/zh-cn_image_0000002815398277.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=6542D437E487343354659CD7C12F5850737C02A44B1DB82D1C6DD438EFB6EBBC)

```typescript
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/6wJsaHNARFmdEiSokpZ0Fg/zh-cn_image_0000002786518702.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C09B929F603358BD0DD6A014E5F7B670C1D6F5E5F1F2C279B59DA1D6EA3C6292)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](../harmonyos-references/ts-container-column.md#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/2814A6zPSmKA1kdeYlTFOA/zh-cn_image_0000002786358774.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CDBD59794EEE99BFB6E8D547D25F4BB18FB24B7C3A4643EBED6EE45D36C1C86)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/VV5fQ6ghRQKSQ5rCUQciAw/zh-cn_image_0000002815558195.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECBD3F068AB8282ED349D2E85880A825461DB9C05331EAFAFB468B2A0BD6B650)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/G4w70s7ZRUORRf2f5530-A/zh-cn_image_0000002815398279.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EDD34C935A3B9B08FF2011BEAB90F02F686F13CC5A8C1CFCA7A404EC731B7A4)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/gbXqJ44qRvuFeFVcaXWv7A/zh-cn_image_0000002786518704.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0D3282DF11EBF30C0113D34B1DB97238F5D37D187D25871CED44B0F47A09B7D)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/fl5Lb__2Rl2oZdhZLbF-nA/zh-cn_image_0000002786358776.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9FD0F35540ECF429C8440A5B7DC09C45FB3B98F0F94B5A73A5FC6FCBCB704D0)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/R7Fanuw6T-urLl3hN-8Ntw/zh-cn_image_0000002815558197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=82F4F60087FF03552829A4D5CA9AF7BC397C669C7B49C3EB7CF651553F477A63)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/KlCp_wy_TfKSBa2ssnq1mw/zh-cn_image_0000002815398281.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=388E658D7668E49324D0F3E56D55CF96328ED5B1CF26DCF35492064A0EE40B78)

### Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Xd_QqVdUS8yp80mW2o1FiQ/zh-cn_image_0000002786518706.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC317ED3ADB98CD92830F0C4251C5E20245548771D930C0769F11F94C713906F)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/ofvVK0dATQyMzaMSFBQepA/zh-cn_image_0000002786358778.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA84737E5827F00AA9B6BBF819D6BE7D4E12B1A9567670813FDA54760A7706A1)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/oQ9Dm52jRZyEFLz8ihVBCw/zh-cn_image_0000002815558199.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D10BA824BBEDC46DDFB82D9A1B3D77BAC6F8EAA69D81F117FF198E6982D6F75F)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/bjkRndqxQE6QKw_HkrNG0w/zh-cn_image_0000002815398283.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4FEBAC6EF63805D97AC79FECA752A2FDD0B3C25683D3C105D17F439375E9C2A)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Dp6-uENSQRWYs65W0RTW6w/zh-cn_image_0000002786518708.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA2EE71C35B22AD64B7BD07AE28A69038C7C76D6720E30B969A6C4DE710B2A4E)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/3oPgzac9Td2B8J6uRgRRsg/zh-cn_image_0000002786358780.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=79241CF96CA1B250FEFC3285DEBC9826D2BC3CDE9E18EDCBE436498CA28A00AA)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/vhxwY33tQZa90SoWRp3m0g/zh-cn_image_0000002815558201.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE039267EE8D6B14CF070712342861E2763D98CFAFF0E76A23BCB769E0AB1ED0)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](../harmonyos-references/ts-container-column.md#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](../harmonyos-references/ts-appendix-enums.md#verticalalign)类型，水平方向取值为[HorizontalAlign](../harmonyos-references/ts-appendix-enums.md#horizontalalign)类型。

[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/F51FFAd6R7mDDZiadFbztA/zh-cn_image_0000002815398285.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC0F16ABEEE223AE2983A83E128CB1D17C8E9FB557D9C555415DD66A6C23E1B0)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/5QtbpcSsR0a9OOEHRtvJyQ/zh-cn_image_0000002786518710.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=10DB3E066743F077AD0CA8D76F2B2A67FF2BF08465760EBCF3CC15E45F437F86)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/vjXNvy6cR8ySXrl_5jIluA/zh-cn_image_0000002786358782.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FF391EA5C75FE3A6BBBBCA085E45EA11693C98E23E6B2E1B7F72BCDE145B418)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/RuQ1Ks1xSEWYS2ZEDGTSXQ/zh-cn_image_0000002815558203.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=49CABE7225E051430164365841F09FEE73EDD2CD082E1970F18096A2C9A76077)

### Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/spKPMXogQl-I-_Or1vv4Lg/zh-cn_image_0000002815398287.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DA3D9F7AD1F06F28E37FF06AEF6CDF3DB805F4738EF35153F712582166ABC26)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ZgHnxhXfRNSN8TJ3FDW3-Q/zh-cn_image_0000002786518712.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=791ED3C33F91D2AEC8B0841FDBD70479F34DFE83381BBBCA6E0DEB44C87A5B56)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/-pdQpT6CQZ-e1bK7fGlj2Q/zh-cn_image_0000002786358784.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=124E34A03B6FA69BDA36BD4E5EDB905C2456C181ABA82376F9844B632B282A58)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/KdbdM-mpSTOKnx148p7eAA/zh-cn_image_0000002815558205.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=75EB0920B3172E485A35D6FE00B53872FE472EE7FE04603D06FA20C881FFBD0E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/YY0i-P7aRI-1EC-74A1K_Q/zh-cn_image_0000002815398289.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5FA9F644CDCB8493EC1A8D01B93A43C1C43151EF738AC976D5C1AFDA3DD2937)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/MLQ46okDRqy4j2K7jfgcAw/zh-cn_image_0000002786518714.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=83EBAA186F23130108D763EA6E99F421C5D9F02EFFF74FF95E1611B85D5E6757)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/zVHcsWPdS72trAzlITRANg/zh-cn_image_0000002786358786.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=3747C8155C27600C0C05B8A34A22A2E50D2E189A13420124B89F0F88F3FCBE1E)

  **图12** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/gY26PkcbQVuETR_PzrDvag/zh-cn_image_0000002815558207.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=47264AA9B45F6DF0427563CC6FC23420FE275F26153DDFD79A3B3E1047ABDFA9)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/o728QofJSHak0ML7bA1GyQ/zh-cn_image_0000002815398291.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B2CFA97206AF63AF52AE48E0EEBEFCD90145D9A1CF6F4CBD4986E4E5530A104)

  **图14** 竖屏

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/7HD8iGO1RZmZA5g-XP933g/zh-cn_image_0000002786518716.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADC4E77B4F6E66933B6713A6CE2C805162445DDD47FF2FC87BBDEA21A41220DA)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/1ee5_fQJSEWmxrDgMxBj9Q/zh-cn_image_0000002786358788.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=716D798F8625008C2D0701BE4732F67E33D48A181B33AADE10CEFA577577AE4B)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/py_RmYeXStOaTg171IEVHw/zh-cn_image_0000002815558209.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=23BBE79D760DB1C984626073BF7800FA300A70AD206CD43C6FA1D06A87990ACB)
