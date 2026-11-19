---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:39+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:8ac81d229413fdd59fd4432d8346bed16ec8fd8f9867e847929da36c80ff2521
---

## 概述

弹性布局（[Flex](../harmonyos-references/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/gdT0ZT8rRbKFIV1zGdbDEA/zh-cn_image_0000002791724824.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DA85416E880FACA75606B87CB3F41CAD48707294F8BDDC32C21EE18AB9224BD)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/0PcwDdyoQwqRlLBaPYX0CQ/zh-cn_image_0000002791564852.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED6472FDE5E096C69876633F7CE59898370541439035984EA8671A6770D2CE63)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Fh8duEskR6KEPQ1x8C0gXA/zh-cn_image_0000002820524805.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=B200F7430A9323BD7B0C3857D9E2A7E3552B7E9E7F2A0A4CD7ACF8F0420D6388)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/b_2UAKmfSxawh_d3Xmk2gg/zh-cn_image_0000002820404803.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=969C822DC50C5C65D34CC09F9E635C559ADDE0CC4B0D6E943E33616BAB89BE62)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/v1pJwpSIQVmrWb282SLRbA/zh-cn_image_0000002791724826.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=B89EAD6A27169983BD3BA0C607F96F23433FA9C0C3EAEEF54DD286D6F5D91B88)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ofqd69ubRui5rnP6bfUaVg/zh-cn_image_0000002791564854.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=107C631A2490D03481E6114392378A4257D8ACA3FBE0D5D74F940F5561AE8C18)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/rgKvmX-DTBeHQzmCL2vzzQ/zh-cn_image_0000002820524807.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=71075623AA6BF58CFDEE93243DC8E7284D49D81F8BB3038F1267778E3DA3AC01)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/sbB0oq1VTj2IKHEoH9P1wg/zh-cn_image_0000002820404805.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=32827BD1CDAB960FB59D0880E7B7D779EE3BCA9B220B05D7166D8736130E7F19)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/79Nss2gGQjKzwYef1chwyQ/zh-cn_image_0000002791724828.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=68321E3827060A15764D1367247F96586B6DFA3E01BFB9CF4C8871646965DA97)

## 主轴对齐方式

通过[justifyContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/9hYOeUN1SE2qTnleBgNurg/zh-cn_image_0000002791564856.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FECD4D27C76B9C318A583B4562BF353F46E3E2FF944792961E5001C65881201)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/JvfkGsZsQXmi89MJxAphwQ/zh-cn_image_0000002820524809.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=99BE057C073689D4B50D4B93CD692C81E692B0B9C018F3CC2E3947D0841067B6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/bD23aY0MRlm-v9ZP8Xy_KA/zh-cn_image_0000002820404807.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=93EEC88034CF7E12FFC3DA2CCBC1062CB9B65E9BAEE1AFA6ADE2ACB049747568)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/tdvcJ4niSfSgnE1lxHqxUA/zh-cn_image_0000002791724830.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=85D9A57CFBB3A4000F8F209792E7F633730408A7B5B2F520CA74B63EE9B3AC92)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/41VHQexNQ926P43nx7yhPQ/zh-cn_image_0000002791564858.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=119B7C75C327F1C1DAD9D594BB9B7D61DAF9197F6208285163D75F3817D5AA3B)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/mFp-HRumRFWYlh49ZQ0mkw/zh-cn_image_0000002820524811.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=4147A72DA2DABC7DB9587795D7478937F838299612149FFEE06D889BF988AD22)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TNibMUpGSrOf5sW_DEy_cw/zh-cn_image_0000002820404809.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=2042BBCFC2F1731902825DFC557B3C12A0E9EDCCF93685489BD0980EA63F21A6)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/jqQfIqOmRGifo_maKMXMJw/zh-cn_image_0000002791724832.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=4592811ED4FB0E2C70F70AD9850965BBEA0263FECE51D0D84F9523FB29605FE0)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/hhkmlmBcRjeJZKsBHr-5kA/zh-cn_image_0000002791564860.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=DADAC5316C56C0EAA63C70BC8D9F8F53B7565B2FBBEA5B2489A3A8462E0C4546)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ABBQ7HCbRSanb1BllGBexg/zh-cn_image_0000002820524813.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=368F391A9F6D63F323CB0D8D4111F5924A3909571FC82B7CDA1F1E10AB963F14)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/LmyV43BpTz2UnmPxmokJ9Q/zh-cn_image_0000002820404811.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=569BF731DC39E29FB6129D779F798F462DBA7E0537A2EA0995A35EB8271412FB)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/3gOYjhY3Q02ek9nIVrsnlg/zh-cn_image_0000002791724834.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=73DB1330ABBA616E44BA5B7FA8F1B6F167B9FB07ECAA2BF56A01CCAC923961D3)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/b6HcK0ECSSG1DsAMQD3ejQ/zh-cn_image_0000002791564862.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DF70747F1AF2D52CE2B60E2DEF2DF7C9B084E8A9472066AEDEC61E56589589A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/u6HGF4SHTz20T_F7hNtyxw/zh-cn_image_0000002820524815.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=58AA3ADA7193D6FC8DB6EFCCF39D4BA000C6D11CEC71553713DD12EB3BC14104)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/yPN0l9TQSnK58ujDZQfaXw/zh-cn_image_0000002820404813.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=85158D97B868BC6BE5A9A9711D20F7DBC5BC80F71B8082CD8A4379715491BBCE)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/VdA2pI7iQBa6Duti_GowVQ/zh-cn_image_0000002791724836.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=A31A666DF999BBECD9518B9E3F03889F60615D9046B7B6A04FE5EBAFBA3EDC42)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CeFPz7tfTmGisq2h9pXsXg/zh-cn_image_0000002791564864.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7C67D630A4C190A896042C0D4B5188780F4625AF4CD346D474783A696467A1E)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/UtEZqlCyT8GrjpiAS395Hw/zh-cn_image_0000002820524817.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=60C8ADE6F998838FF664F390A17EA394D18258B9D73573FDDB7C3F1B1E216E54)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/IS4FqIkNR2eYdv6BH348pw/zh-cn_image_0000002820404815.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A8C29F6948200B36A37E2B876A5C4E8A4574DFB14536F2BA7E18677C36A5B6D)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Su9ObTT9SWCVr7uLFrTaCA/zh-cn_image_0000002791724838.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA951B66D4F3FAB4EC7E3A457D21B1D0D17BEDCED336B5C5587908FDC717FF82)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/P9UFvAwDQh-UoINxtpnW7g/zh-cn_image_0000002791564866.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=8100C8707D771722275343EB042968D07195F2CFA240507AAF9E7BE226D54D01)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/W9lV_8TvSo686xSFfsxFfg/zh-cn_image_0000002820524819.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B3B296265DD10D7FB66AA7ED6D20024C5469C6163CAA1A97384E91C6515F366)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/01WGF13gTLWE4JoUQaWZ1Q/zh-cn_image_0000002820404817.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED7DD84BB7D42531E6C3574BCEF074DFC2C6964E5710D86ED4A57C252C16BEA3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/wzAYOntFR9OqDHQ9RzGfJQ/zh-cn_image_0000002791724840.png?HW-CC-KV=V1&HW-CC-Date=20261119T014649Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA41FE4910AE733C32AE159032836B056D1551EF519C297C39E094D731843B63)
