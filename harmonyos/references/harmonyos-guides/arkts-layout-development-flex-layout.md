---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:05+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:dc9f60cb06dd4ff2e417c33b6b51a8c03da1557edc2b56e7cfd8fe4c445261cf
---

## 概述

弹性布局（[Flex](../harmonyos-references/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/EkVqOiVrTaetq8BqBdtSmw/zh-cn_image_0000002821836407.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=303939F9A0B89246C9E580C5E0F0E087340F6CAF881B81103AF5262FEFCB1BD7)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/jgHZVn_KTt6SjJJoaV_Rfw/zh-cn_image_0000002821756409.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1BF2C84B1A279F1C7078D39D7E0E6AC3587F44A8FFF5D21AF787006ACF85369)

* FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。

  ```typescript
  Flex({ direction: FlexDirection.Row }) {
    Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(50).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .height(70)
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/0KXmC-zpQ-e26U8c2jG8uA/zh-cn_image_0000002793036472.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=0947B793BC391E2C0B54C952BAEAEC86A93E1EB0390F422D7E150605F2E781C7)
* FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。

  ```typescript
  Flex({ direction: FlexDirection.RowReverse }) {
    Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(50).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .height(70)
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/UUKGEC3nTNm2HLUhtXaE-Q/zh-cn_image_0000002792876504.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=84786B2AEFD1356F79A4FD27A620FF3A69EBF9421F2365DA6823406A06DC6436)
* FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。

  ```typescript
  Flex({ direction: FlexDirection.Column }) {
    Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('100%').height(50).backgroundColor('#D2B48C')
    Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  }
  .height(70)
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/o0D7jVyBQ6C8TJPVykGuWg/zh-cn_image_0000002821836409.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=614DD1AC925B9C8CE2B26F685091F7B55022DA5398D7E802B60EC2AFC0B459EA)
* FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。

  ```typescript
  Flex({ direction: FlexDirection.ColumnReverse }) {
    Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('100%').height(50).backgroundColor('#D2B48C')
    Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  }
  .height(70)
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/SzvEny8jRcquBsx6_yqpvQ/zh-cn_image_0000002821756411.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=83B4A4E06CF5F72B9DA3D4B4F08749B727D7AA7DECB91AC360E4BDD663FFC0EF)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

* FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。

  ```typescript
  Flex({ wrap: FlexWrap.NoWrap }) {
    Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('50%').height(50).backgroundColor('#D2B48C')
    Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/M2BjK3d9QoWoek40xOud0g/zh-cn_image_0000002793036474.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AFD08CA2D2593CF644573F5FDFFCC60A8D3A6529F19880D2CCA76A1470BAB80)
* FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。

  ```typescript
  Flex({ wrap: FlexWrap.Wrap }) {
    Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('50%').height(50).backgroundColor('#D2B48C')
    Text('3').width('50%').height(50).backgroundColor('#D2B48C')
  }
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/gTzEIPRuRZC6Jt7dmEUAlg/zh-cn_image_0000002792876506.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D5090FF29C938A67B9941AD934965B7D09A395864EE83D7B006E2F64974920F)
* FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。

  ```typescript
  Flex({ wrap: FlexWrap.WrapReverse }) {
    Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('50%').height(50).backgroundColor('#D2B48C')
    Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/qgxbsk0oSKmx8a9HrTVn6A/zh-cn_image_0000002821836411.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=9613EB2AEAA7428693A4C6015516685C4B275262FC65B84C2DD29DF674F8437C)

## 主轴对齐方式

通过[justifyContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/fZw5_aqfSRypeCNAF1ephA/zh-cn_image_0000002821756413.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=85B397CE9BA5059B761F160FF4A35591E617151AF1E361EA3215FCBD3B50B3B7)

* FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.Start }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/8_cZ6oo5T6qLRcXx4UlPKg/zh-cn_image_0000002793036476.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=17826DCF67E50950016DDC5C5E5D23407359C7A61C07ECCBD029F3E1BF9AEBF2)
* FlexAlign.Center：子元素在主轴方向居中对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.Center }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Ci_cvTZWTbOBNU_d1-uflQ/zh-cn_image_0000002792876508.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=A388D7D9B73BEAE41D3805697C19ADC5B5B8E8D85FD4CBD8BF1C5239021D1A39)
* FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.End }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hFlorBvoTyG-KVdAy4PNjw/zh-cn_image_0000002821836413.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DBA8DCAC7367EF79F21DB8367B843C75959DB940DE93C48621EE48FF5CB27F9)
* FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/igXjx_oDTGK-Uay52nsAlw/zh-cn_image_0000002821756415.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D829E7BE8D1FFEDA2155696BECE320095E8236FB01DF9EA0510B4691906730F)
* FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceAround }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/X_tGenpjTNKSIofJVxKJsA/zh-cn_image_0000002793036478.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=36A124BC3A79C02751F1286BFAFD9263B4B2F63BB0ED7345E1DD329A6F7B6F4D)
* FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
    Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
    Text('2').width('20%').height(50).backgroundColor('#D2B48C')
    Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  }
  .width('90%')
  .padding({ top: 10, bottom: 10 })
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZKsV80-pQc2S9UNLkU-v5Q/zh-cn_image_0000002792876510.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBF08AC7BBAD1263BBA1F1EE4C58F0A9D89E52051FEA285E88D151E564B54D81)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

* ItemAlign.Auto：使用Flex容器中默认配置。

  ```typescript
  Flex({ alignItems: ItemAlign.Auto }) {
    Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(40).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/_rxKWF_5TqCiRk5Ljhwf9A/zh-cn_image_0000002821836415.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=497E669653E6F9EC844F5EDB91372D0FECD0650D641619439079815A5B290FB2)
* ItemAlign.Start：交叉轴方向首部对齐。

  ```typescript
  Flex({ alignItems: ItemAlign.Start }) {
    Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(40).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/NELlKD81SGS2WTR0aF6QTg/zh-cn_image_0000002821756417.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=8581091DC8F75C70D9BEEE1D8E49921344559059FD4C008124AF218A2CC13E56)
* ItemAlign.Center：交叉轴方向居中对齐。

  ```typescript
  Flex({ alignItems: ItemAlign.Center }) {
    Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(40).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/b1qQ3chTQt-SrzCsqosbfw/zh-cn_image_0000002793036480.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=C39D93933050A49EB4DDA4035289039893B241E660E595F5A80A7B80A258626B)
* ItemAlign.End：交叉轴方向底部对齐。

  ```typescript
  Flex({ alignItems: ItemAlign.End }) {
    Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(40).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/W1qmr2_BT9Oqv2bhaT9BNw/zh-cn_image_0000002792876512.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=71F4E164898FF6220476D8D71B0C25730865C0F53BE8F29109D29B54C992431E)
* ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](../harmonyos-references/ts-appendix-enums.md#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。

  ```typescript
  Flex({ alignItems: ItemAlign.Stretch }) {
    Text('1').width('33%').backgroundColor('#F5DEB3')
    Text('2').width('33%').backgroundColor('#D2B48C')
    Text('3').width('33%').backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/z5L0McqrSLGvncKwEelNOA/zh-cn_image_0000002821836417.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=64242F793F070AD0A9E508DFE88EA0A10F49E78859DB8ED04B7388355167A974)
* ItemAlign.Baseline：交叉轴方向文本基线对齐。

  ```typescript
  Flex({ alignItems: ItemAlign.Baseline }) {
    Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
    Text('2').width('33%').height(40).backgroundColor('#D2B48C')
    Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  }
  .size({ width: '90%', height: 80 })
  .padding(10)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/-gHkXFdASHe96998c5z7Ew/zh-cn_image_0000002821756419.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFB83A3CBBD9CE3B467024F6D57721E8421D3BFC7A8484F0E083E96E80923F0D)

### 子元素设置交叉轴对齐

子元素的[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```typescript
Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子元素居中
  Text('alignSelf Start').width('25%').height(80)
    .alignSelf(ItemAlign.Start)
    .backgroundColor('#F5DEB3')
  Text('alignSelf Baseline')
    .alignSelf(ItemAlign.Baseline)
    .width('25%')
    .height(80)
    .backgroundColor('#D2B48C')
  Text('alignSelf Baseline').width('25%').height(100)
    .backgroundColor('#F5DEB3')
    .alignSelf(ItemAlign.Baseline)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#D2B48C')
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#F5DEB3')

}.width('90%').height(220).backgroundColor('#AFEEEE')
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Mfp7TPF5SICzvgrFMThXnA/zh-cn_image_0000002793036482.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3FC3FA04576B0346C812316445F75D071D3A6F5C8A2F138B9B082BA64F92EE4)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

* FlexAlign.Start：子元素各行与交叉轴起点对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/UfxVR3BnTPSFfr5aUBRbAg/zh-cn_image_0000002792876514.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E8D80431BB789470CA104D00C644591430CEE65267DA8AD859C0E08BE6DD702)
* FlexAlign.Center：子元素各行在交叉轴方向居中对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/hYy_PW_YT1Snk6VpqLAM6w/zh-cn_image_0000002821836419.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3C23297E167BD87E37DC88F6FBC4936C585A8C8582A37DDEDF0E3D78B71FE9F)
* FlexAlign.End：子元素各行与交叉轴终点对齐。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/52TLzFKwR92Q3iCssJ4eTQ/zh-cn_image_0000002821756421.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD99E96C3178ADB0C6CFF6B97B59A3A4C7EE986A59C7D5A28F6A7B38D6E0E50A)
* FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/lctDDWSeQmipyfyWmjPLYw/zh-cn_image_0000002793036484.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=49CE6C6518AF73B948B5221E3D20425F55225CBDAEDEB0ADDC65C7C8F83E628B)
* FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_-YaUOJuR0Kro6u6l1OD8Q/zh-cn_image_0000002792876516.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7C7D640AEEACA022A83C698B4D30F70633FCC9280E103128EBC4095BAF06CB8)
* FlexAlign.SpaceEvenly：子元素各行间距，子元素首尾行与交叉轴两端距离都相等。

  ```typescript
  Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
    Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('2').width('60%').height(20).backgroundColor('#D2B48C')
    Text('3').width('40%').height(20).backgroundColor('#D2B48C')
    Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
    Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  }
  .width('90%')
  .height(100)
  .backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/M5J7gjFjSC-yNKwSTsKsBg/zh-cn_image_0000002821836421.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D20A000A8594F88758B5AB9A4E2667041EEDE7F842E8181876B865C4D890399)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

* [flexBasis](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。

  ```typescript
  Flex() {
    Text('flexBasis("auto")')
      .flexBasis('auto')// 未设置width以及flexBasis值为auto，内容自身宽度
      .height(100)
      .backgroundColor('#F5DEB3')
    Text('flexBasis("auto")'+' width("40%")')
      .width('40%')
      .flexBasis('auto')// 设置width以及flexBasis值auto，使用width的值
      .height(100)
      .backgroundColor('#D2B48C')

    Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
      .flexBasis(100)
      .height(100)
      .backgroundColor('#F5DEB3')

    Text('flexBasis(100)')
      .flexBasis(100)
      .width(200)// flexBasis值为100，覆盖width的设置值，宽度为100vp
      .height(100)
      .backgroundColor('#D2B48C')
  }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/9TVWTSXSSZyhfwQp8_mzJA/zh-cn_image_0000002821756423.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=92617302E7B06F0F446C9D2AEF318B1189F870E0C7CAFF299D2A42A4415DA8F1)
* [flexGrow](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。

  ```typescript
  Flex() {
    Text('flexGrow(1)')
      .flexGrow(1)
      .width(100)
      .height(100)
      .backgroundColor('#F5DEB3')
    Text('flexGrow(4)')
      .flexGrow(4)
      .width(100)
      .height(100)
      .backgroundColor('#D2B48C')

    Text('no flexGrow')
      .width(100)
      .height(100)
      .backgroundColor('#F5DEB3')
  }.width(360).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/0ctY3wD9QRS7KTzVC9ornA/zh-cn_image_0000002793036486.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB007BF4A5E02636911FAF4DBADB43550F4F3C96D8CB3ED5A8DA76F70B26E814)

  父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

  第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp \* 1/5=108vp，第二个元素为100vp+40vp \* 4/5=132vp。
* [flexShrink](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexshrink)：当父容器空间不足时，子元素的压缩比例。

  ```typescript
  Flex({ direction: FlexDirection.Row }) {
    Text('flexShrink(3)')
      .flexShrink(3)
      .width(200)
      .height(100)
      .backgroundColor('#F5DEB3')

    Text('no flexShrink')
      .flexShrink(0)
      .width(200)
      .height(100)
      .backgroundColor('#D2B48C')

    Text('flexShrink(2)')
      .flexShrink(2)
      .width(200)
      .height(100)
      .backgroundColor('#F5DEB3')
  }.width(400).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/2KJscLvPSGqTjqUMP1iLzw/zh-cn_image_0000002792876518.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC6EBFE6268904A5B1DB71934E57BE8E52C54D08299839B4954A5AF2BBE368A6)

  父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。

  将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) \* 3=68vp，第三个元素为200vp - (220vp / 5) \* 2=112vp。

## 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

```typescript
@Entry
@Component
struct FlexExample {
  build() {
    Column() {
      Column({ space: 5 }) {
        Flex({
          direction: FlexDirection.Row,
          wrap: FlexWrap.NoWrap,
          justifyContent: FlexAlign.SpaceBetween,
          alignItems: ItemAlign.Center
        }) {
          Text('1').width('30%').height(50).backgroundColor('#F5DEB3')
          Text('2').width('30%').height(50).backgroundColor('#D2B48C')
          Text('3').width('30%').height(50).backgroundColor('#F5DEB3')
        }
        .height(70)
        .width('90%')
        .backgroundColor('#AFEEEE')
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/agr25UTKRoWXrSZmzChTlw/zh-cn_image_0000002821836423.png?HW-CC-KV=V1&HW-CC-Date=20261121T010942Z&HW-CC-Expire=31536000000&HW-CC-Sign=27C7AA6BCE67D374720D9D3D324EF45892365D705FE5ED63965C07DEE4C0C580)
