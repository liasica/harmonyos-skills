---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout
title: 弹性布局 (Flex)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 弹性布局 (Flex)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:31+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:849f56a968ea169d39f730fd910a24c1fa66dc3b6504dc3e1179f2906eecdbb2
---

## 概述

弹性布局（[Flex](../harmonyos-references/ts-container-flex.md)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wZb8V7A4T8-eyNQo190GEw/zh-cn_image_0000002583477715.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=FF49E12D6431B064F6081ED8FAA3EEBF2E6C306E015E578121837E79DDC80BE5)

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/jL3AoJagTB6G6fRBCqV9Bg/zh-cn_image_0000002552798066.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=18540D01AF88DB0E75F99EAAC10B9CC9D37D3F42DFE7CD2E1A71A7CE14509339)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/amMd64z1Ri62n93hVBqf4g/zh-cn_image_0000002583437761.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=17B638A02C44139D08E124814469C10EDBDCF98AFC6FF1B3D89A14F9D88BE193)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/b1JR2MkKQUGtmC9Lr9A0fw/zh-cn_image_0000002552957716.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=9D20CD10778B322F216CF7A527382DD3425BD9DEC177724A74418D5FF8C9941E)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/FUejOBioQ1qUFrFWgovQAA/zh-cn_image_0000002583477717.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=3D48D314CBFB9F9AE6C38C81BADC885981D701833286286EEA97670DE26F5986)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ntcLY_0oSQCo9KDTz-5khA/zh-cn_image_0000002552798068.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=0D4A8B42520DFE8E54027F47FD6670A992EE0A4119C91979D3607A256A61888C)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/M8qCu851RiyvkLT8V7-PzQ/zh-cn_image_0000002583437763.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=5650E34FDC180CDCEBC7A38F8F67F6C9B86D764E5875A480C34C2091D8B19B5D)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/swAcno06Ra2_Xzd4eL6Pcw/zh-cn_image_0000002552957718.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=232EFA6034F078F6DDAFC905032DAB34D5F51E1B2C9254F8B517664C2D67BAF6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/xzHF0EBBTliqelQrwYbI2Q/zh-cn_image_0000002583477719.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=63059ABE067A5CDBC8D1BB01F5A589827CC27426284F35F25914FDEF5E5FE0BC)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Rdt9kS4RTUGHtE4Vhy4Vdw/zh-cn_image_0000002552798070.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=97CD4B7619369AA27884C37180945BC8134BCA557EF5522797C4751895650E3D)

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

  [FlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignStart.ets#L20-L129)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/H3-W90t3QryAaDBd07oaqQ/zh-cn_image_0000002583437765.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=5F513EDEC9C71FDA111B0C64C8836E1D3B794B8D63C8CF3CE9EBC704CA87CA30)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/StiYEZrtToyZm15nakY6iA/zh-cn_image_0000002552957720.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=C93FFB79DACD3061673CDD81E4787645633C7F1D6DDFD6A124D105218ABD26CC)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/KCq1--9ARHeM4fw9Wb6l0g/zh-cn_image_0000002583477721.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=3A206A2556C38F4F578EBF01273E88A6AFE314FAC620A0DD95B79B6056E0EF66)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/84QzY2rcRgezDLIlLedemA/zh-cn_image_0000002552798072.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=887D59826B64FC47E94AB85657A75BA8D80056CA1E3B9F96F6880E1B250039FC)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/D3xqb14PSY2rwLjt_U_sMQ/zh-cn_image_0000002583437767.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=809DEFAA2998266CD820E38076AEA2A739B044867259546F65D48C5E3F7816BD)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ggPe0zO6QdOHCwThQFWzDg/zh-cn_image_0000002552957722.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=18C0F6BDB81E6B07544385B61E0AD4D14B2760804019B90524C01C11201913F1)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/-nuGMrlFSmeXmuAi1GEOsw/zh-cn_image_0000002583477723.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=90356C59BA80877C90AC362A0E874ABD4FB6BC98260A0EA873BF46B250F4E7EC)
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

  [FlexItemAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStart.ets#L20-L49)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ZAsE-BIoQsiu9aFfCzIygw/zh-cn_image_0000002552798074.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=1D78D1E6ED6F96AA3302A927E1ED6C83AE03BF85FD75EBE3C90352C82C6BDB94)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/HZpKkk5LRP6jQe_Bd0YWmQ/zh-cn_image_0000002583437769.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=A34B1A98DBE2F2221D9FCBCE324D6E1BE260B4B1132E00F35125E6E1578D52EA)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/CpBF4U4GRO6cdBz6GrzB5A/zh-cn_image_0000002552957724.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=38C9F961D8DB4B42BA403FE2413D788F7ACCFF3CD00034D64C2E7E68636518C6)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/sdhDxwdrRn-hYcAY_qxqqw/zh-cn_image_0000002583477725.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=EE08264A40E1F93228E2127BB6420939EA9F285E88F935C6D349BDE8DD495D39)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/vW7o0EeaQ3yslp1M-t5VzQ/zh-cn_image_0000002552798076.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=93FF77C2652375D61005CB7B518EC74616B4857FA3D1A6C83C702D14827C9D3E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/7oJ2BKKcTHSA6Q6Y2xrB1w/zh-cn_image_0000002583437771.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=913078189063CDDE1E44151975E8222FDA816915387D12C8F232CC37173EDCB2)

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

  [FlexAlignCenterFlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignStart.ets#L20-L80)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/PkMppq-3QuGETIrxzjqVfA/zh-cn_image_0000002552957726.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=EFA72CC2447CDD1BD9E7119FB08AC9B34C4CCC336BFE3EE0DFF0537C34090CB1)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/zQtKXKK5TvO8BS7f832Ccw/zh-cn_image_0000002583477727.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=3052F09688A010DFD9C2AA0E1D0AFB566790DBD25082329DAC078C2AFE6A994F)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/_0ER6eSOTwuRhf246mXe-A/zh-cn_image_0000002552798078.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=BFBB7C1CDD91A5B204D6FCEC31A392111E235890DFEF7F46EDF4FEC273D616CA)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Xfo_pdIAQ8-6CL7BwvKSDw/zh-cn_image_0000002583437773.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=B0042F513B86D04BDDE7C43805A68F7F5D981717632C70D14C416FAA494E2007)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Y2Q0XJI6TtGcbGb3fcq8AA/zh-cn_image_0000002552957728.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=1D0BF4C29D22DFF614840561C2B78638435E509004ED60F5A9611ADC5B5927CE)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/0ukMyGlMRY6g1Qk2aMiZNw/zh-cn_image_0000002583477729.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=2332F6571C4730E1BA990265FF0A05D4B6C22DEA41A10469DE4D65B0B4892A2C)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/m9mErdDIQ5yiAuaacGXFFA/zh-cn_image_0000002552798080.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=08A73B495698D004905A2BA1DD0458D452EA528ED92893BA826D0449D1F6494F)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/l-Abr8IpTImnX31MdEklqw/zh-cn_image_0000002583437775.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=9BCF1BFB4AD5648090CB4E884B1912027A42FB015C5C2165B1AA4C70E00C195F)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5Zh3H1lVRoCTreUYej_Ltw/zh-cn_image_0000002552957730.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=15F52A03F3097AA79A32DFD6042AB0627EE93ACA8C2B834EC12B5A4C7BFE88D3)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/MWdiUu1DRwuxcGRoc0lGWQ/zh-cn_image_0000002583477731.png?HW-CC-KV=V1&HW-CC-Date=20260427T233930Z&HW-CC-Expire=86400&HW-CC-Sign=3EF1E105021861169E8B40F9152440FE5BFCCFDFA79E3F7F7CF56D6047E300D4)
