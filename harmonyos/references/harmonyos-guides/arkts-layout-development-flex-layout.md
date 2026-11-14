---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:68a51f027e010559ba54ebe92138f321ac6c2707b207b329a6772f1ef7449be7
---

## 概述

弹性布局（[Flex](../harmonyos-references/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/g-sFS4Z_SCqBU1XDNDy4rQ/zh-cn_image_0000002817425887.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=D32BCD771728685DB6A21CD8D3D1B133C600EB4D40995292A53F1869E536CF55)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/b5QIg_goTtqm0cIyvXz7ng/zh-cn_image_0000002788466468.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF2FB7DE0156FBD780DE2CC219ED8EB151936D8FDC030F1E8547D8B60A36D197)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2JFP0W8yTVqMSDEewHmLgg/zh-cn_image_0000002817505955.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=28868E50A08D88A3DB4DF770FCD7F4871730BF1A75BDAF3B83DAC942984C4927)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Vf-GK9CbSwq0Sbj9G6s4cQ/zh-cn_image_0000002788306526.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=A88A4FE2CD8F60CC1D5637867115E989A7B72ED8744E42A96099F007C53040AF)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/-Ksf0eGvRvyVGICAxhCXsg/zh-cn_image_0000002817425889.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=F087676670A832382559DEE6068C22A66F0F706A2589B3C4C41119D7050A56AA)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/9urFXK6lSkufl_95ifhRww/zh-cn_image_0000002788466470.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=55060720671AD13E43AD1C974F951A56148593A7FE110903202F7C173631D1B3)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/BbaCBiRySvS_f8m2TKerzQ/zh-cn_image_0000002817505957.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1BB94A4754A914151343E89E8B1AA3D532BA9CC44788C6A09AC40B533209F93)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Mfznz7WWR-yhDuVIrGNLeQ/zh-cn_image_0000002788306528.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B1E834E8AA486619C34F0AF7E09373638C7E0668B36C1E485B17524572B8879)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/YjdHbnu_T-SS29rJjGCWBQ/zh-cn_image_0000002817425891.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4154EC55CB682CF19F35D83769CCC312B39C3A20B4493F7DF8F0B36084623E4)

## 主轴对齐方式

通过[justifyContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/tNevpJyWQVu-Clb4HJyFYg/zh-cn_image_0000002788466472.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=40006B5603EB9787F1639F916855EE6E510958453863457D2BE3372AD538DF7E)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/a26T_-e0RUuF5bnPc3qn3w/zh-cn_image_0000002817505959.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=27B43DF40054BC8B324FD8CDEB7221E63560C131D5113B18D1F5E626AAC03793)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/-LgoeSdvSmWnxkQQ-QcpQA/zh-cn_image_0000002788306530.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AAECAE13310F46BB2DE986C5861E1A002BBFC867374913C3A0F95E6EF30A0E7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/NCSiKyw7SQ6PexySXdtM7w/zh-cn_image_0000002817425893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=0721E41D76BFF68333126793B0DF600704788C702899A566AB10EA464BAB09C7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/DRukkZz6Q8WydAKbwtEcvg/zh-cn_image_0000002788466474.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B03A86CC27ACDE1B42BFECEF35FD3D858847C328829072BAC3F9DE557B31497)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/8CTwP5DPRmmMaNQoypprog/zh-cn_image_0000002817505961.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=09B6718E2B518526942213735B4C8CF6F35886BA0E4251B56A9A49B01D1FA818)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/O1eHFquVTV-eN5I2lm1ebg/zh-cn_image_0000002788306532.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EE34FE81CA219F293D634F85801795F79F1E42C12456CF815C247585F1DBC7C)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/QvDuj8juSUCwGr7vd9YfDw/zh-cn_image_0000002817425895.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=4525490F044C531B77A3CA62761D2C852582AA91C07B46A22AB61AC8AB82CF8E)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/8UR-NZpaQu2_QFKtSutSzA/zh-cn_image_0000002788466476.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=211AC857E3CA5EDDE4AE4E1B80D644617D65C7909715B4E89A85C4C5F73B376D)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Am8UJjfWROucr1btl4oEEg/zh-cn_image_0000002817505963.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=B83CE57CE612BFA258C455E7F521350F006326572880787E6CCE88AD37EF543A)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Fd_y1nCfRh6NB6aVjBahjg/zh-cn_image_0000002788306534.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FD5B9A018C7340B626696321B8006353072DF43DA80862B06F42596CABEA22F)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/ar-LulmrRiuMl88RqEe-tA/zh-cn_image_0000002817425897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=29143260EBAC393EB429E62AF1A657607827BCEC558655F9F5B14A278F809A6A)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/_KaJ7hzUR7KMFrEjsYgvnQ/zh-cn_image_0000002788466478.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CE90F6D2E973DC5285A80DE5538823D1739194564C215621AEB6FF9A7DCBE43)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/r-AbV08DSlujJFzOgoZTkw/zh-cn_image_0000002817505965.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=A21BD512EF8745FAC90D9C1EAE583297E26F288B59551F5C358C53245093DDA4)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/YP15QKSFRP6JR4IF5erKfg/zh-cn_image_0000002788306536.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=98EB02CCBE80498652F76FC02F9E1423DE6451D7CD05ED26607BD6890B8C6A37)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/KZIX0FxsT92yZOrSiQ0QtA/zh-cn_image_0000002817425899.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0954B26995DBA9DF7319B7EF0E73B9692AB7C0002115D4567ED2794B4D256D2)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/2kf8UsTmSBWo6Ho0cqK-8A/zh-cn_image_0000002788466480.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=B808D7087175D96BF8FA1C8A12F366952EB9A9C3BA692CC87185316167589B12)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/eJiy2i6xT9mGNJV1urY_-Q/zh-cn_image_0000002817505967.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E70F5324F3A267B7084A1FC0AF7B0A67630260BC1B3C8C9E3B15A299D205263)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/8XH8m9dWRxKauTGAiL0gTA/zh-cn_image_0000002788306538.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8B2789DEAF342ADD3580178A852B047C8D2BE07E68526E3B090E45103A618BD)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/-c-e_I0ORbyCP5F3o5xwYA/zh-cn_image_0000002817425901.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=5CFE9AA035AE027AC98DE3E1B8B91F7375000B997B1C9D08BA429B2633814FE2)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/o3RbopLgTRGSFLUxr_dmyg/zh-cn_image_0000002788466482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B060D685B2D2452D78763EC38B120880A3967532ECB5B1DF60B1FE645221402)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/fp2POokBSYOWK2sM6ktdAA/zh-cn_image_0000002817505969.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=66F59EE1ADF46B09C0E368CFA41056122689EE319216FAEEFACD8CF21F4F26DB)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Srerbb5GQBen05oRuKIKGw/zh-cn_image_0000002788306540.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=40D391A4F98DDBC281F67F8F8050ACF36CF250D1BF0F67E2DF873E882FA296DF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/kVVZ2enmTPmqzuekC6iY-Q/zh-cn_image_0000002817425903.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0EE906604B7746F3C8CB2B387FDB8BA2932D6820D6A56DB0CA85216C9B50FD1)
