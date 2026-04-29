---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-music-app-overview
title: 多设备音乐界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备音乐界面
category: best-practices
scraped_at: 2026-04-29T14:12:22+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:e22495840998c36cd06571ff06cd7864911f070951dfd809aec43fcc37a7911b
---

## 概述

本文将介绍如何在音乐播放器的实际开发过程中实现“一次开发，多端部署”。音乐播放器是当前广受欢迎的大众娱乐应用。本文将以播放页为例，展示其在直板机、双折叠（Mate X系列）、平板、智能穿戴四种产品形态上的“一次开发，多端部署”。本文将通过架构设计、UX设计、页面开发和智能穿戴开发四个部分，介绍在开发过程中实现“一次开发，多端部署”的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

音乐应用以播放页为重点进行介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/0HKV8fXvTsSbSbm2oRbvvA/zh-cn_image_0000002471180817.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=02BDB7A77158B055A084222C3E6EBED8B5DE48882DF884F0264C83E437BCF51E "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/PwiPPWPbQOKjkOJR2FCvQg/zh-cn_image_0000002437742432.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=D76F7ACD3AE8A75D0155AAA38FC27DA4E5767BD959FB893EA4B581A8F0694C24 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/bX47A6eQR7m1r-pPpb_GJw/zh-cn_image_0000002471220981.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=EB22527B01B401B8B94146C9256D4F72E555B064E5A3756A725833AE4898E7F3 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/1x3amcxjTPObN50yKQy6fA/zh-cn_image_0000002437582588.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=9F03F9CDC064DF7B37CC20C42AEA38442E471AB56249A79FDE8814C47655087D "点击放大")

|  | sm | md | lg | 智能穿戴 |
| --- | --- | --- | --- | --- |
| **布局方式** | 单列+Swiper切换 | 左右分栏（1:1） | 左右分栏（1:1） | 圆形布局 |
| **交互特点** | 进度条拖动、按钮点击、左右滑动切换页面 | 进度条拖动、按钮点击 | | 按钮点击、旋转表冠 |

说明

由于智能穿戴设备与移动端的布局差异显著，因此需为前者单独创建[HAP](../harmonyos-guides/hap-package.md)包，而非依赖断点判断。

## 工程管理

本章将介绍如何创建“一多”工程及划分目录结构。

### 创建工程

根据三层架构进行[多设备工程部署与发布](bpta-multi-device-ide.md)，先创建出最基本的项目工程，再在基本目录结构的基础上进行修改。

由于圆形屏幕设备在形态与使用场景上的特殊性，其交互与界面设计和常规设备存在显著差异。因此，在products层中设立独立的watch模块，以实现对穿戴设备的精准适配。该模块采用分层架构设计，聚焦于穿戴设备特有的界面与交互逻辑，同时将设备无关的通用逻辑下沉至公共模块，从而确保架构清晰、复用性高。

说明

在开发穿戴应用时，需要将工程中module.json5的deviceTypes改为wearable，以确保应用能够在穿戴设备上正确部署和运行。可参考[智能穿戴应用开发](bpta-smartwatch.md)了解能力介绍。

### 工程结构

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。详细请参见[分层架构设计](bpta-layered-architecture-design.md)。

音乐应用根据一多推荐的common、features、products的“三层工程架构”划分目录。其中三个页面功能不同，互不依赖，根据页面划分为三个features（基础特性层）：直播页-live、音乐评论页-musicComment和歌曲列表页-musicList。公共常量、媒体播放工具以及窗口管理工具等需要被不同页面依赖引用的内容，划分为一个common（公共能力层）。在products（产品定制层）中，分别设立了面向智能穿戴设备开发的独立watch模块和适用于普通设备的phone模块，以适配不同设备在界面与交互方面的差异，从而实现清晰的模块化划分。

工程结构如下：

```
1. │──common                                    // 公共能力层
2. │  ├──constantsCommon/src/main/ets            // 公共常量
3. │  │  └──constants
4. │  └──mediaCommon/src/main/ets                // 公共媒体方法
5. │     └──utils
6. │     └──viewmodel
7. ├──features                                   // 基础特性层
8. │  ├──live/src/main/ets                       // 直播页
9. │  │  ├──constants
10. │  │  ├──view
11. │  │  └──viewmodel
12. │  ├──live/src/main/resources                 // 资源文件目录
13. │  ├──musicComment/src/main/ets               // 音乐评论页
14. │  │  ├──constants
15. │  │  ├──view
16. │  │  └──viewmodel
17. │  ├──musicComment/src/main/resources         // 资源文件目录
18. │  ├──musicList/src/main/ets                  // 歌曲列表页
19. │  │  ├──components
20. │  │  ├──constants
21. │  │  ├──lyric
22. │  │  ├──view
23. │  │  └──viewmodel
24. │  └──musicList/src/main/resources            // 资源文件目录
25. └──products                                   // 产品定制层
26. ├──phone/src/main/ets                      // 支持手机、平板
27. │  ├──common
28. │  ├──entryability
29. │  ├──pages
30. │  ├──phonebackupextability
31. │  └──viewmodel
32. ├──phone/src/main/resources                // 资源文件目录
33. ├──watch/src/main/ets                      // 支持智能穿戴
34. │  ├──constants
35. │  ├──pages
36. │  ├──view
37. │  ├──watchability
38. │  └──watchbackupability
39. └──watch/src/main/resources                // 资源文件目录
```

## 页面开发

本章介绍音乐应用如何使用“一多”的布局能力，完成页面层级的一套代码、多端适配。下文以播放页为例，介绍各区域使用的具体布局能力，帮助开发者快速实现“一多”开发。

### 播放页

播放页是音乐应用的主要功能页面，用于播放音乐。以下是播放页在三种设备上的显示效果图：

| 示意图 | **sm** | **md** | **lg** |
| --- | --- | --- | --- |
| **效果图** |  |  |  |

* 播放页主要包含播控区域和歌词区域。在sm断点下，通过Tabs组件或Swiper组件切换这两个区域。在md和lg断点下，播控区域和歌词区域以左右两列展示。
* 在sm断点下，使用Stack组件将区域1显示在Swiper组件上。区域2、3、4作为沿垂直方向布局的Column组件的子组件，在区域3和区域4之间使用Blank组件填充空白区域。
* 在md断点下，播控区域与歌词区域通过GridRow和GridCol组件实现。GridRow设置总栅格数为8，每个GridCol占4个栅格。
* 在lg断点下，GridRow设置总栅格数为12。播控区域占4个栅格，GridCol设置offset为1。歌词区域占6个栅格，offset为1。

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 标题区 | [Row](../harmonyos-references/ts-container-row.md)组件的justifyContent属性设置为FlexAlign.SpaceBetween实现均分能力，代码可参考[多设备长视频界面](multi-video-app.md)。 |
  | 2 | 专辑封面 | [Image](../harmonyos-references/ts-basic-components-image.md)组件设置aspectRatio属性为1使图片宽高相等。 |
  | 3 | 歌曲信息 | [Column](../harmonyos-references/ts-container-column.md)组件沿垂直方向布局展示两行文本。 |
  | 4 | 播控区域 | 使用[Slider](../harmonyos-references/ts-basic-components-slider.md)组件实现进度条。 |
  | 5 | 歌词区域 | [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)结合动画实现歌词滚动效果。 |
  | 6 | 桌面歌词按钮 | [Image](../harmonyos-references/ts-basic-components-image.md)组件显示歌词图片。 |

## 智能穿戴开发

本章将介绍音乐应用如何借助“一多”布局能力，在智能穿戴设备上实现独立应用开发，并以首页、歌单页、歌曲列表页与播放页等典型页面为例，详细阐述其设计与实现。

### 首页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/uAFFSSwiQrmi3iC3ak8okQ/zh-cn_image_0000002437582592.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=35CCAEFAC90686AB80DC209D5E8AE6E1742998C62AD979C51151DAC86EA2F6A1 "点击放大")

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 首页列表区域 | 使用[ArcList](../harmonyos-references/ts-container-arclist.md)实现弧形列表布局，多行展示列表。 |
| 2 | 首页轮播区域 | 使用[ArcSwiper](../harmonyos-references/ts-container-arcswiper.md)组件实现左右轮播效果。 |

* 首页列表区域

  通过[ArcList](../harmonyos-references/ts-container-arclist.md)实现弧形列表布局，设置scrollBar属性为BarState.Off隐藏滚动条的显示，通过space属性调整子组件之间的距离。每个子组件需要使用[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)作为容器，给子组件设置justifyContent为SpaceAround，让其内部元素沿水平方向均匀排列。

  ```
  1. Column() {
  2. ArcList({ initialIndex: 0 }) {
  3. ForEach(this.menuList, (item: Menu) => {
  4. ArcListItem() {
  5. Row() {
  6. Image(item.icon)
  7. .width($r('app.float.home_icon_width'))
  8. .height($r('app.float.home_icon_width'))
  9. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
  10. .backgroundColor($r('app.color.home_icon_background'))
  11. .padding($r('app.float.home_icon_padding'))

  13. Text(item.text)
  14. .fontColor($r('app.color.font_color'))
  15. .fontSize($r('app.float.home_font_size'))

  17. Image($r('app.media.chevron_right'))
  18. .width($r('app.float.home_icon_jump_width'))
  19. }
  20. .width(this.HOME_BTN_WIDTH)
  21. .height($r('app.float.home_btn_height'))
  22. .padding({ left: $r('app.float.list_btn_padding'), right: $r('app.float.list_btn_padding') })
  23. .justifyContent(FlexAlign.SpaceBetween)
  24. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
  25. .backgroundColor($r('app.color.home_btn_background'))
  26. // ...
  27. }
  28. }, (item: Menu, index: number) => JSON.stringify(item) + index)
  29. }
  30. .scrollBar(BarState.Off)
  31. .space(LengthMetrics.vp(5))
  32. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
  33. .focusable(true)
  34. .focusOnTouch(true)
  35. .defaultFocus(true)
  36. }
  37. .align(Alignment.Center)
  38. .width(StyleConstants.FULL_WIDTH)
  39. .height(StyleConstants.FULL_HEIGHT)
  40. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
  ```

  [Home.ets](https://gitcode.com/HarmonyOS_Codelabs/MusicHome/blob/master/products/watch/src/main/ets/view/Home.ets#L66-L114)

* 首页轮播区域

  使用[ArcSwiper](../harmonyos-references/ts-container-arcswiper.md)组件实现，通过左右滑动实现首页和歌单页的切换，并且通过indicator属性设置导航点样式。

  ```
  1. Column() {
  2. Row() {
  3. ArcSwiper(this.wearableSwiperController) {
  4. Home()
  5. PlayList()
  6. }
  7. .duration(400)
  8. .indicator(this.arcDotIndicator
  9. .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION)
  10. .selectedItemColor('#FE1B48')
  11. )
  12. // ...
  13. }
  14. .height(StyleConstants.FULL_HEIGHT)
  15. }
  16. .width(StyleConstants.FULL_WIDTH)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Codelabs/MusicHome/blob/master/products/watch/src/main/ets/pages/Index.ets#L45-L84)

### 歌单页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/of2n0TWCSeequSIg2MHKOQ/zh-cn_image_0000002471180829.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=837D45B3B7512C582880C7E485300BAF7D055B956CC48A981939EBA101A5EB2F "点击放大")

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 歌单列表区域 | 使用[ArcSwiper](../harmonyos-references/ts-container-arcswiper.md)组件实现上下滑动切换歌单。 |

歌单页使用[ArcSwiper](../harmonyos-references/ts-container-arcswiper.md)组件实现。通过将组件的vertical属性设置为true，指定滑动轴为垂直方向，从而实现竖向滑动交互。将indicator属性设置为false，隐藏默认的页面导航点，减少视觉干扰。

```
1. Column() {
2. ArcSwiper(this.wearableSwiperController) {
3. ForEach(this.playList, (item: PlayListSheet) => {
4. Column({ space: 10 }) {
5. Row() {
6. Text(item.name)
7. .fontWeight(FontWeight.Bold)
8. .fontColor($r('app.color.font_color'))
9. .fontSize($r('app.float.home_font_size'))
10. Image($r('app.media.chevron_right'))
11. .width($r('app.float.home_icon_jump_width'))
12. .margin({ left: $r('app.float.playlist_padding') })
13. }

15. Image($r('app.media.play_btn_fill'))
16. .width($r('app.float.playlist_icon'))
17. .height($r('app.float.playlist_icon'))
18. .position({ x: '25%', y: '65%' })
19. Text(item.title)
20. }
21. .width(StyleConstants.FULL_WIDTH)
22. .height(StyleConstants.FULL_HEIGHT)
23. .backgroundImage(item.background, ImageRepeat.NoRepeat)
24. .backgroundImageSize({ width: StyleConstants.FULL_WIDTH, height: StyleConstants.FULL_HEIGHT })
25. .justifyContent(FlexAlign.SpaceBetween)
26. .padding({ top: $r('app.float.playlist_row_padding'), bottom: $r('app.float.playlist_row_padding') })
27. // ...
28. }, (item: PlayListSheet, index?: number) => index + JSON.stringify(item))
29. }
30. .index(0)
31. .duration(400)
32. .focusable(true)
33. .focusOnTouch(true)
34. .defaultFocus(true)
35. .vertical(true)
36. .indicator(false)
37. // ...
38. }
39. .width(StyleConstants.FULL_WIDTH)
40. .height(StyleConstants.FULL_HEIGHT)
```

[PlayList.ets](https://gitcode.com/HarmonyOS_Codelabs/MusicHome/blob/master/products/watch/src/main/ets/view/PlayList.ets#L64-L135)

### 歌曲列表页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/DfRe75jRSxyPYikMhx23Jw/zh-cn_image_0000002437742444.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=357E0D323B8900C8C6CC9822FB266D070FB0FA1A1D8A3690B19FEE4BFEC1DB37 "点击放大")

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 歌曲列表区域 | 使用首页一致的[ArcList](../harmonyos-references/ts-container-arclist.md)实现多行展示歌曲。 |

列表页采用与首页一致的ArcList弧形列表布局。每一行歌曲项中，左侧使用Image组件展示专辑封面，并通过设置borderRadius为50%实现圆形效果；右侧歌曲信息使用Column组件，设置layoutWeight为1以占据剩余全部宽度，再结合Column组件默认居中的特性，实现剩余空间内居中对齐。

```
1. Column() {
2. ArcList({ initialIndex: 0 }) {
3. ForEach(this.songList, (item: SongItem, index: number) => {
4. ArcListItem() {
5. Row() {
6. Image(item.label)
7. .width($r('app.float.home_icon_width'))
8. .height($r('app.float.home_icon_width'))
9. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)

11. Column() {
12. Text(item.title)
13. .fontWeight(FontWeight.Bold)
14. .fontColor($r('app.color.font_color'))
15. Text(item.singer)
16. .fontColor($r('app.color.text_color'))
17. }
18. .layoutWeight(1)
19. }
20. .width(this.HOME_BTN_WIDTH)
21. .height($r('app.float.home_btn_height'))
22. .padding({ left: $r('app.float.list_btn_padding'), right: $r('app.float.list_btn_padding') })
23. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
24. .focusable(true)
25. .focusOnTouch(true)
26. .backgroundColor($r('app.color.home_btn_background'))
27. }
28. .align(Alignment.Center)
29. // ...
30. }, (item: SongItem, index: number) => JSON.stringify(item) + index)
31. }
32. .scrollBar(BarState.Off)
33. .space(LengthMetrics.vp(5))
34. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
35. .focusable(true)
36. .focusOnTouch(true)
37. .defaultFocus(true)
38. }
39. .align(Alignment.Center)
40. .width(StyleConstants.FULL_WIDTH)
41. .height(StyleConstants.FULL_HEIGHT)
42. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)
```

[SongList.ets](https://gitcode.com/harmonyos_codelabs/MusicHome/blob/master/products/watch/src/main/ets/view/SongList.ets#L45-L93)

### 播放页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/cJYk1pHtSXmYuebTTLEUyQ/zh-cn_image_0000002471220997.png?HW-CC-KV=V1&HW-CC-Date=20260429T061211Z&HW-CC-Expire=86400&HW-CC-Sign=0E3CE291A50A067433B7E328895D82DB8ED8D811177C81E040066E6F245C308F "点击放大")

| 区域编号 | 简介 | 实现方案 |
| --- | --- | --- |
| 1 | 歌曲信息及操作按钮区域 | 使用[Column](../harmonyos-references/ts-container-column.md)组件沿垂直方向布局展示歌曲信息、音乐控制按钮、操作按钮。使用[Stack](../harmonyos-references/ts-container-stack.md)和[Progress](../harmonyos-references/ts-basic-components-progress.md)实现控制按钮和环形进度条。 |
| 2 | 音量控制区域 | 使用[ArcSlider](../harmonyos-references/ohos-arkui-advanced-arcslider.md)组件实现滑动调节音量。 |

* 歌曲信息及操作按钮区域
  1. 使用[Stack](../harmonyos-references/ts-container-stack.md)组件可将多个元素堆叠在一起，实现更加灵活的布局。
  2. 使用[Progress](../harmonyos-references/ts-basic-components-progress.md)组件用于实时显示当前音乐的播放进度，帮助用户了解歌曲的播放时间及剩余时间。采用环形进度条（ProgressType.Ring），既具视觉吸引力，又能高效利用屏幕空间。

  ```
  1. Column() {
  2. Column() {
  3. Text(this.songList[this.selectIndex].title)
  4. .fontWeight(FontWeight.Bold)
  5. .fontColor($r('app.color.font_color'))
  6. Text(this.songList[this.selectIndex].singer)
  7. .fontColor($r('app.color.play_singer_color'))
  8. }

  10. Row() {
  11. Column() {
  12. Image($r('app.media.previous_btn'))
  13. .width($r('app.float.play_song_img'))
  14. }
  15. // ...
  16. Stack() {
  17. Image(this.songList[this.selectIndex].label)
  18. .width($r('app.float.play_circle_img'))
  19. .height($r('app.float.play_circle_img'))
  20. .borderRadius(StyleConstants.CIRCLE_BORDER_RADIUS)

  22. Progress({ value: this.time, total: this.max, type: ProgressType.Ring })
  23. .width($r('app.float.play_progress_width'))
  24. .backgroundColor(Color.Transparent)
  25. .color($r('app.color.font_color'))

  27. Image($r('app.media.play_btn'))
  28. .width($r('app.float.play_song_img'))
  29. .visibility(this.isPlay === true ? Visibility.None : Visibility.Visible)
  30. // ...

  32. Image($r('app.media.pause_btn'))
  33. .width($r('app.float.play_song_img'))
  34. .visibility(this.isPlay === true ? Visibility.Visible : Visibility.None)
  35. // ...
  36. }
  37. .width(this.HALF_WIDTH)
  38. .align(Alignment.Center)

  40. Column() {
  41. Image($r('app.media.next_btn'))
  42. .width($r('app.float.play_song_img'))
  43. }
  44. // ...
  45. }
  46. .justifyContent(FlexAlign.SpaceAround)
  47. .width('85%')

  49. Row() {
  50. Image($r('app.media.download'))
  51. .width($r('app.float.play_icon_width'))
  52. Image($r('app.media.repeat'))
  53. .width($r('app.float.play_icon_width'))
  54. Image($r('app.media.full_screen'))
  55. .width($r('app.float.play_icon_width'))
  56. }
  57. .width('60%')
  58. .justifyContent(FlexAlign.SpaceAround)
  59. }
  60. .width(StyleConstants.FULL_WIDTH)
  61. .height(StyleConstants.FULL_HEIGHT)
  62. .padding({ top: $r('app.float.play_column_padding'), bottom: $r('app.float.play_column_padding') })
  63. .justifyContent(FlexAlign.SpaceAround)
  ```

  [SongPage.ets](https://gitcode.com/harmonyos_codelabs/MusicHome/blob/master/products/watch/src/main/ets/view/SongPage.ets#L46-L131)
* 音量控制区域
  1. 音量控制交互通过[ArcSlider](../harmonyos-references/ohos-arkui-advanced-arcslider.md)实现。通过设置position={ top: 0, right: 0 }，将滑动条定位在界面右上角，使其层级覆盖于其他组件之上，确保良好的可见性与操作便捷性。
  2. 在滑动条旁新增麦克风图标，并通过精确的position布局进行定位，直观提示用户该控件与音频调节相关，增强功能可识别性与用户体验。

  ```
  1. Column() {
  2. ArcSlider({ options: this.arcSliderOptions })
  3. .focusable(true)
  4. .focusOnTouch(true)
  5. .defaultFocus(true)
  6. .zIndex(999)
  7. .onDigitalCrown((event: CrownEvent) => {
  8. event.stopPropagation();
  9. const STEP_DEGREE = 20;
  10. let newVolume = this.volume + event.degree / STEP_DEGREE;
  11. newVolume = Math.max(0, Math.min(100, newVolume));
  12. this.setAVPlayerVolume(newVolume);
  13. })
  14. Image($r('app.media.speaker_fill'))
  15. .width($r('app.float.volume_icon_width'))
  16. .height($r('app.float.volume_icon_width'))
  17. .rotate({ angle: '-30deg' })
  18. .position({
  19. right: $r('app.float.volume_icon_right'),
  20. top: $r('app.float.volume_icon_top'),
  21. })
  22. }
  23. .hitTestBehavior(HitTestMode.Transparent)
  24. .position({
  25. top: 0,
  26. right: 0
  27. })
  ```

  [VolumeSliderComponent.ets](https://gitcode.com/harmonyos_codelabs/MusicHome/blob/master/products/watch/src/main/ets/view/VolumeSliderComponent.ets#L76-L103)

## 示例代码

* [多设备音乐界面](https://gitcode.com/harmonyos_codelabs/MusicHome)
