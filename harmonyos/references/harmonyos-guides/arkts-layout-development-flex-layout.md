---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ebbc3ecc2da765ac49b377005568cdf2cf6884a9799fb1f4880dfb88505e170e
---

## 概述

弹性布局（[Flex](../harmonyos-references/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/sAuP89_3QNujeHPpV7hTSA/zh-cn_image_0000002589244013.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=FFA341DF240A3B032D219C24F19E9CD4661F6E3E1978961992E9E5D026F866C6)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/x1kw1pe6S8W8iNEIik9opA/zh-cn_image_0000002558764206.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=4B975C68FC99E6197F7B723A78829E6A7C20D968EFC369D7C53E196A76CFD7B2)

* FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.Row }) {
  2. Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionRow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRow.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/s0Etgnb5TrCGhTkxDOB3sQ/zh-cn_image_0000002558604550.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=80D5C91767B9CFD9B29843FA6C1A63AA2421343CBD32E38E1E70E48C76A94D51)
* FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.RowReverse }) {
  2. Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionRowReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRowReverse.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/jUllqCWAT1egbiM9HNQ8Ww/zh-cn_image_0000002589324075.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3B4D695B5E9860A5685E3331F4D6DF6C18EF974ADAE49A2710BEC84C7140FA9A)
* FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.Column }) {
  2. Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('100%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionColumn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumn.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/V26mEahWQR21vrivzTyeTw/zh-cn_image_0000002589244015.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=A6743D17EF4C7BCC0BC4D4842BE705C5D1E0D729B2BCCDDC3D4A718D35C85C6F)
* FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。

  ```
  1. Flex({ direction: FlexDirection.ColumnReverse }) {
  2. Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('100%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .height(70)
  7. .width('90%')
  8. .padding(10)
  9. .backgroundColor('#AFEEEE')
  ```

  [FlexDirectionColumnReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumnReverse.ets#L20-L30)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/HcDpsSX2QhqL5ikkBGBv2Q/zh-cn_image_0000002558764208.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=1F8A02FED855A0B0B4E2273EE9FF6203C80799AB6F00DFD3C53DA3A009C3CD81)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

* FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。

  ```
  1. Flex({ wrap: FlexWrap.NoWrap }) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapNoWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapNoWrap.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/N20TKJOgTe2mLzenoAGvmQ/zh-cn_image_0000002558604552.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=9EA8A9321B84363A6958BE86CF0397B93001E47BD33CB90EFC940897AD32A3C6)
* FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。

  ```
  1. Flex({ wrap: FlexWrap.Wrap }) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#D2B48C')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrap.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/luYggbs6Re6lx9Y0O3qUqw/zh-cn_image_0000002589324077.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=0000F62951D473A945555E81E751EAEDE0A4736D810B9DE70B75179AA4B07E48)
* FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。

  ```
  1. Flex({ wrap: FlexWrap.WrapReverse}) {
  2. Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('50%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexWrapWrapReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrapReverse.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ot_3frkpRyad8iiACt12KQ/zh-cn_image_0000002589244017.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3A650577EA7B17B13E99B4793BF75F681AB5E2A0FAC5172B1ED51E713304D9AA)

## 主轴对齐方式

通过[justifyContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/74PXR4mITWqCuIvGGBZFeQ/zh-cn_image_0000002558764210.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=BD8CFDEF262697C5874C8CEB87EE95A2A0DA114429CA75E5A0A38F97A3301F5C)

* FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.Start }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignStart.ets#L20-L78)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/3r-fqYWvT0m11hc2khV9fQ/zh-cn_image_0000002558604554.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=08D370D2C7261195785B47E27A927869A9B6E9E4F4F9D490BDDE442453ED5D40)
* FlexAlign.Center：子元素在主轴方向居中对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.Center }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenter.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/BLK5aKiWSNW7ZsAqf07shg/zh-cn_image_0000002589324079.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=284FCE3509844478678F3A8C210C7D4D580AE7A677DDE4497C10FED0FBE55999)
* FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.End }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignEnd.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/yXvAru78SL6eB95TtCNjcA/zh-cn_image_0000002589244019.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=1177A66706C774902F0F6199D41D69696228DD325265A1921F34645B8E42C2EE)
* FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceBetween.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/qpvP7TMUSPC4pOQkr0fibg/zh-cn_image_0000002558764212.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=E547037F40C9FEEEC707E27C2CB75121DDD19E7FD16E0A2DC1A840FEDAC90A1C)
* FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceAround }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceAround.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/wMBPOkLvQc-Inc4MZLHHGw/zh-cn_image_0000002558604556.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=EBABB64B442650238B391F94177130CA7981B35C0A3D80FC09019F72274BB48A)
* FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
  2. Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
  3. Text('2').width('20%').height(50).backgroundColor('#D2B48C')
  4. Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .width('90%')
  7. .padding({ top: 10, bottom: 10 })
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceEvenly.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/k1H2OOSdRrGlugqRLyfzHA/zh-cn_image_0000002589324081.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=556BE8D5AFBB37C1A8321E59515F35E94D4B4CA113588FA8DCF2C6EBF220A625)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

* ItemAlign.Auto：使用Flex容器中默认配置。

  ```
  1. Flex({ alignItems: ItemAlign.Auto }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignAuto.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignAuto.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/xNCFOhAQQ-qwZhuCmknpxA/zh-cn_image_0000002589244021.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=05867A5092B758307E30855684928BBEA91ADBAFF37EB55C55A08627C93DA4FF)
* ItemAlign.Start：交叉轴方向首部对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Start }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStart.ets#L20-L155)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/cVpBuAd9Ra-SQyhZjSjJgw/zh-cn_image_0000002558764214.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=AFF628A6CE904655733B29AEFAE17349E91136CCBB559147ECFA1097C03601ED)
* ItemAlign.Center：交叉轴方向居中对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Center }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignCenter.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/W1tq7d8VTrOhRKgujYf7hw/zh-cn_image_0000002558604558.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=B90E2EABDDCBE253A98CCF9D298F62F8C8C0F93457DC7AECD4B9DFF59967C39C)
* ItemAlign.End：交叉轴方向底部对齐。

  ```
  1. Flex({ alignItems: ItemAlign.End }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignEnd.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/MkPkfr1qTCO0wbwOpF7v9A/zh-cn_image_0000002589324083.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=4CBB582DF9EA1E0DD94AFD01B88BC67E114634E4C9665553E71F26979B21AB92)
* ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](../harmonyos-references/ts-appendix-enums.md#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。

  ```
  1. Flex({ alignItems: ItemAlign.Stretch }) {
  2. Text('1').width('33%').backgroundColor('#F5DEB3')
  3. Text('2').width('33%').backgroundColor('#D2B48C')
  4. Text('3').width('33%').backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignStretch.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStretch.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Ku6YUKlRQiiQLbnMLafMMQ/zh-cn_image_0000002589244023.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=EA924EF9CE8EBEAF1AB9F9FCE4612F2B032C53F7D1BB9EE4B6D2FA218F3B2703)
* ItemAlign.Baseline：交叉轴方向文本基线对齐。

  ```
  1. Flex({ alignItems: ItemAlign.Baseline }) {
  2. Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
  3. Text('2').width('33%').height(40).backgroundColor('#D2B48C')
  4. Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
  5. }
  6. .size({ width: '90%', height: 80 })
  7. .padding(10)
  8. .backgroundColor('#AFEEEE')
  ```

  [FlexItemAlignBaseline.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignBaseline.ets#L20-L29)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/__MlbswgSMmvH_5krzWWKA/zh-cn_image_0000002558764216.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=5E9BFE1664E62DB5C938F276224ADAEF16863D5DB524C7384C9A18852696904E)

### 子元素设置交叉轴对齐

子元素的[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```
1. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子元素居中
2. Text('alignSelf Start').width('25%').height(80)
3. .alignSelf(ItemAlign.Start)
4. .backgroundColor('#F5DEB3')
5. Text('alignSelf Baseline')
6. .alignSelf(ItemAlign.Baseline)
7. .width('25%')
8. .height(80)
9. .backgroundColor('#D2B48C')
10. Text('alignSelf Baseline').width('25%').height(100)
11. .backgroundColor('#F5DEB3')
12. .alignSelf(ItemAlign.Baseline)
13. Text('no alignSelf').width('25%').height(100)
14. .backgroundColor('#D2B48C')
15. Text('no alignSelf').width('25%').height(100)
16. .backgroundColor('#F5DEB3')

18. }.width('90%').height(220).backgroundColor('#AFEEEE')
```

[FlexAlignSelf.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSelf.ets#L20-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jtsgx8APT9aaLteyHkF81A/zh-cn_image_0000002558604560.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=D53D37BB5030E4FAAC0D6FFB0F7D329E58B2027B99C79664C7C47181E2D10629)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

* FlexAlign.Start：子元素各行与交叉轴起点对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignStart.ets#L20-L36)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/GOQRg1TdSpefkHNpe3OPwQ/zh-cn_image_0000002589324085.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3A12B271EB996B791A02902238AD390DEB3951C25D2C5FDC2DB8BE6A22DEA42B)
* FlexAlign.Center：子元素各行在交叉轴方向居中对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignCenter.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/r81nxSg2QLuooiTplLDDfA/zh-cn_image_0000002589244025.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=6FD07E578D711DC815A6D4FF04E24355E7B25249949FBE6E5C078200527F2BCA)
* FlexAlign.End：子元素各行与交叉轴终点对齐。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignEnd.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/7zUAW8D2RLmsLO8TW6GOxw/zh-cn_image_0000002558764218.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=1D86E7E36409027BA8E62E90A2815E7BC9723076ED7933DF387799CD4EEC7C30)
* FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceBetween.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/u2PmA-BZSVuds4bOJ-pJNQ/zh-cn_image_0000002558604562.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=E614496DF359B7599B760FC60459E6520C30F001ACD543CB674544293EA995AF)
* FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceAround.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ts-pAcFEQ0agIA_hePMwIA/zh-cn_image_0000002589324087.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=2FA8EF959A43487C3A0B62512BCB9D6305A7330F6CE256ADEE5334F5670468F0)
* FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。

  ```
  1. Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
  2. Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
  3. Text('2').width('60%').height(20).backgroundColor('#D2B48C')
  4. Text('3').width('40%').height(20).backgroundColor('#D2B48C')
  5. Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
  6. Text('5').width('20%').height(20).backgroundColor('#D2B48C')
  7. }
  8. .width('90%')
  9. .height(100)
  10. .backgroundColor('#AFEEEE')
  ```

  [FlexAlignCenterFlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceEvenly.ets#L20-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/2EofXzxsRVeKN0zGK06mzw/zh-cn_image_0000002589244027.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=35E8E2ACD8430AFCBA813459B8F5F5A2428EF4C34FB060DE2ED4FD0ED2BCFE02)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

* [flexBasis](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。

  ```
  1. Flex() {
  2. Text('flexBasis("auto")')
  3. .flexBasis('auto')// 未设置width以及flexBasis值为auto，内容自身宽度
  4. .height(100)
  5. .backgroundColor('#F5DEB3')
  6. Text('flexBasis("auto")'+' width("40%")')
  7. .width('40%')
  8. .flexBasis('auto')// 设置width以及flexBasis值auto，使用width的值
  9. .height(100)
  10. .backgroundColor('#D2B48C')

  12. Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
  13. .flexBasis(100)
  14. .height(100)
  15. .backgroundColor('#F5DEB3')

  17. Text('flexBasis(100)')
  18. .flexBasis(100)
  19. .width(200)// flexBasis值为100，覆盖width的设置值，宽度为100vp
  20. .height(100)
  21. .backgroundColor('#D2B48C')
  22. }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexBasis.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexBasis.ets#L20-L43)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ljeLz2lDQEuaRRDNJb1okA/zh-cn_image_0000002558764220.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3D207B6D17D544F005C68A2E47D47D37D203603215782356480DA30E3291CE73)
* [flexGrow](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。

  ```
  1. Flex() {
  2. Text('flexGrow(1)')
  3. .flexGrow(1)
  4. .width(100)
  5. .height(100)
  6. .backgroundColor('#F5DEB3')
  7. Text('flexGrow(4)')
  8. .flexGrow(4)
  9. .width(100)
  10. .height(100)
  11. .backgroundColor('#D2B48C')

  13. Text('no flexGrow')
  14. .width(100)
  15. .height(100)
  16. .backgroundColor('#F5DEB3')
  17. }.width(360).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexGrow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexGrow.ets#L20-L38)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/KANmfjkPStyjsh3Y2BrCoA/zh-cn_image_0000002558604564.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=133822CABC7D574F2A9A64649D1D21DBBD460B5ADDFFB64359E9D40A7D9C8549)

  父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

  第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp \* 1/5=108vp，第二个元素为100vp+40vp \* 4/5=132vp。
* [flexShrink](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexshrink): 当父容器空间不足时，子元素的压缩比例。

  ```
  1. Flex({ direction: FlexDirection.Row }) {
  2. Text('flexShrink(3)')
  3. .flexShrink(3)
  4. .width(200)
  5. .height(100)
  6. .backgroundColor('#F5DEB3')

  8. Text('no flexShrink')
  9. .width(200)
  10. .height(100)
  11. .backgroundColor('#D2B48C')

  13. Text('flexShrink(2)')
  14. .flexShrink(2)
  15. .width(200)
  16. .height(100)
  17. .backgroundColor('#F5DEB3')
  18. }.width(400).height(120).padding(10).backgroundColor('#AFEEEE')
  ```

  [FlexShrink.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexShrink.ets#L20-L39)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/sJnp8tQkSwKydfCR5r0q_g/zh-cn_image_0000002589324089.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=DCA3AD027F2508DF45DF8C70BD9D6DC7E2F1F3A9AFAA6D8AF2FBA65C9490FD51)

  父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。

  将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) \* 3=68vp，第三个元素为200vp - (220vp / 5) \* 2=112vp。

## 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

```
1. @Entry
2. @Component
3. struct FlexExample {
4. build() {
5. Column() {
6. Column({ space: 5 }) {
7. Flex({
8. direction: FlexDirection.Row,
9. wrap: FlexWrap.NoWrap,
10. justifyContent: FlexAlign.SpaceBetween,
11. alignItems: ItemAlign.Center
12. }) {
13. Text('1').width('30%').height(50).backgroundColor('#F5DEB3')
14. Text('2').width('30%').height(50).backgroundColor('#D2B48C')
15. Text('3').width('30%').height(50).backgroundColor('#F5DEB3')
16. }
17. .height(70)
18. .width('90%')
19. .backgroundColor('#AFEEEE')
20. }.width('100%').margin({ top: 5 })
21. }.width('100%')
22. }
23. }
```

[FlexExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexExample.ets#L15-L39)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/9EZOCdbxTlSd8dgmtrcqng/zh-cn_image_0000002589244029.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=2BD17F159A322942C5E5A77DAF973063139CA2D57807B5B52BAD54473AF31C5E)
