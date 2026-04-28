---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-community-app
title: 多设备社区评论界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备社区评论界面
category: best-practices
scraped_at: 2026-04-28T08:21:27+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:26de2b7fecb21c7c12c6c502dd3ec7fcb2dbaad59cb75451a7e746a6d81ac6fa
---

## 概述

本文选择社区评论行业应用作为典型案例介绍“一多”在实际开发中的应用。社区评论应用的核心功能包括社区新闻浏览和热搜榜单查看。基于这些核心功能，案例实现了推荐热搜、热搜榜单、卡片详情、图片查看和输入评论等典型页面。文章重点介绍关键布局能力及对应实现。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。更多详细请参考[分层架构设计](bpta-layered-architecture-design.md)。

## UX设计

社交通讯类的多设备响应式设计指南，请参考[社交通讯类](../design-guides/responsive-design-examples2-0000001793536901.md)。

本章介绍社交通讯类应用中如何使用“一多”布局能力，完成页面层级的单页面和多端适配。下文将详细说明每个页面区域使用的具体布局能力，帮助开发者从零开始进行社交通讯类应用的开发。

热点页利用[响应式布局](bpta-multi-device-responsive-layout.md)中的[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)布局能力，结合[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现单列卡片变瀑布流卡片的一多布局能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fqQR88doQm6Kj8xzTcOgJQ/zh-cn_image_0000002229335777.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=A8E49604351E9C80F7445D530A1F575A312B1C60F3EE554DB0B0205A33BA0F39 "点击放大")

在卡片详情页中，使用响应式布局的栅格布局，实现图文区域和评论区域的左右及上下布局，从而达到边看边评的图文阅读效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/4ONCaQ4OTk2uPSkdTL4EGA/zh-cn_image_0000002229335781.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=C3CC13D50A918036C2E2A24C1A3965C006DA9E0213016486159482A967FDB395 "点击放大")

社区评论应用包含以下一多页面布局能力：[侧边导航](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)、[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)、[动态卡片](multi-community-app.md#zh-cn_topic_0000001758831130_li1420045031813)、[边看边评](multi-community-app.md#zh-cn_topic_0000001758831130_li11692132514198)。侧边导航参考多设备长视频界面[底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)。

## 页面开发

### 布局能力

本章节选取页面关键区域进行布局能力介绍。

**热点页布局能力**

热点页提供搜索、热搜展示、信息阅读等功能，使用列表布局和动态卡片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/rOCbUq2OQqC7eTk16chtLQ/zh-cn_image_0000002229335773.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=D5B732D7F6DA2921526956678DD8713235638B4DDD8CF1020DB3F4DB1DA4F2C0 "点击放大")

* 列表重复布局

竖向列表清晰明了地展示数据。在宽屏设备上，设计了列表重复布局以展示更多数据。

在进行有序数据展示时，使用[List](../harmonyos-references/ts-container-list.md)容器进行数据排列。通过设置List组件的布局方向listDirection和lanes属性并结合断点，实现在不同断点下显示不同列数。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. @Component
2. export struct HotColumnView {
3. @StorageLink('currentBreakpoint') currentBreakpoint: string = 'sm';
4. // ...

6. @Builder
7. HotListBuilder(index: number) {
8. List() {
9. ForEach(HOST_LIST_ARRAY[this.tab_index], (item: HotItemInterface) => {
10. if (item.index > index * 5 && item.index <= (index + 1) * 5) {
11. ListItem() {
12. HotListItemView({
13. item: item,
14. showDetail: true,
15. // ...
16. })
17. }
18. }
19. }, (item: HotItemInterface) => JSON.stringify(item))
20. }
21. }

23. build() {
24. Column() {
25. Swiper() {
26. ForEach([0, 1, 2], (item: number) => {
27. this.HotListBuilder(item)
28. }, (item: number) => JSON.stringify(item))
29. }
30. // ...
31. }
32. // ...
33. }
34. }
```

[HotColumnView.ets](https://gitcode.com/HarmonyOS_Codelabs/MultiCommunityApplication/blob/master/features/hot/src/main/ets/view/HotColumnView.ets#L25-L74)

* 动态卡片

信息卡片是显示内容的主体。使用竖向单列布局在宽屏设备上容易造成大量留白，影响视觉效果。在宽屏设备上展示两列布局可充实页面内容。瀑布流布局能紧密连接卡片，提供更紧凑的视觉效果。

动态卡片布局主要使用WaterFlow容器，在手机、折叠屏与平板设备间差异化显示。手机及折叠屏上竖向单列展示，通过分割线分隔卡片。平板设备上，WaterFlow容器显示2列，依赖断点控制。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. WaterFlow() {
2. ForEach(this.cardArrayViewModel.cardArray, (item: CardItem, index: number) => {
3. FlowItem() {
4. Column() {
5. MicroBlogView({
6. cardItem: item,
7. // ...
8. })
9. // ...

11. CommentBarView({
12. isShowInput: false,
13. // ...
14. })
15. }
16. // ...
17. }
18. }, (item: CardItem, index: number) => index + JSON.stringify(item))
19. }
20. .columnsTemplate(this.currentBreakpoint !== 'lg' ? '1fr' : '1fr 1fr')
```

[FoundView.ets](https://gitcode.com/harmonyos_codelabs/MultiCommunityApplication/blob/master/features/hot/src/main/ets/view/FoundView.ets#L103-L148)

**卡片详情区域**

卡片详情区域支持图文和评论在不同设备上显示上下或左右布局。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/EEa77zlaTRK0UoQdC6c4tQ/zh-cn_image_0000002194009952.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=B8B70B7515A0006EBADBBD9F8E6EEF9DCC1E029DB3F8D58AB87294EE9AEDC4A9 "点击放大")

* 边看边评

为了优化图文内容和图片内容的展示效果，并支持同时浏览评论，在不同设备上进行了以下布局设计：手机采用上下布局，折叠屏支持内容区和评论区的上下及左右布局切换，平板设备固定为左右布局。

边看边评功能主要通过栅格布局实现。在手机设备上，图文区和评论区同时占满设备栅格，显示为图文区在上、评论区在下的布局。折叠屏的上下布局与左右布局切换使用控制栅格数量实现。左右布局控制图文区占用栅格数为3/5，评论区占用栅格数为2/5。修改图文区及评论区栅格数为5/5时，切换为上下布局。

在lg断点下为实现固定评论区宽度，使用[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)容器重新构建页面布局。由于栅格布局与SideBarContainer容器无法兼容，使用断点分别控制两处实现的显示隐藏。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. @Component
2. export struct DetailPage {
3. // ...
4. build() {
5. Stack() {
6. Column() {
7. DetailTitleView({ isShowedButton: this.isShowedButton })
8. Scroll() {
9. GridRow({ columns: { sm: 4, md: 5, lg: 12 } }) {
10. GridCol({ span: { sm: 4, md: this.isFoldHorizontal ? 3 : 5, lg: 12 } }) {
11. if ((this.isFoldHorizontal && this.currentBreakpoint === 'md')) {
12. Scroll() {
13. MicroBlogView({
14. cardItem: this.cardItem,
15. index: this.selectCardIndex
16. })
17. // ...
18. }
19. // ...
20. } else {
21. MicroBlogView({
22. cardItem: this.cardItem,
23. index: this.selectCardIndex
24. })
25. // ...
26. }
27. }
28. // ...

30. GridCol({ span: { sm: 4, md: this.isFoldHorizontal ? 2 : 5, lg: 12 } }) {
31. CommentListView()
32. }
33. // ...
34. }
35. }
36. .visibility(this.currentBreakpoint === 'lg' ? Visibility.None : Visibility.Visible)
37. // ...

39. Column() {
40. SideBarContainer() {
41. Column() {
42. CommentListView()
43. }
44. // ...

46. Column() {
47. Scroll() {
48. MicroBlogView({
49. cardItem: this.cardItem,
50. index: this.selectCardIndex
51. })
52. // ...
53. }
54. // ...
55. }
56. .justifyContent(FlexAlign.Start)
57. }
58. // ...
59. }
60. .visibility(this.currentBreakpoint !== 'lg' ? Visibility.None : Visibility.Visible)
61. // ...
62. }
63. // ...
64. }
65. }
66. // ...
67. }
```

[DetailPage.ets](https://gitcode.com/harmonyos_codelabs/MultiCommunityApplication/blob/master/features/detail/src/main/ets/view/DetailPage.ets#L29-L189)

### 交互事件处理

**文字缩放**

详情页正文内容支持捏合手势[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)缩放文字大小。文字区域添加双指捏合手势事件，使用缩放比例计算文字大小及文字行高，实现双指缩放文字的功能。缩放事件输入方式参考[交互归一](bpta-multi-interaction.md#section088812013815)。

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/0pHjtpXYRWO2QtjijAIx_w/zh-cn_image_0000002229335757.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=B4D4B60E9D0791E9C240EE091E84C4334DD4F770420BAF03DDCFDF9D1A8D99B9 "点击放大")

```
1. @Component
2. export struct MicroBlogView {
3. // ...
4. build() {
5. Column() {
6. if (this.cardItem !== undefined) {
7. // ...

9. Row() {
10. Text(this.cardItem.content)
11. .fontSize(`${this.contentFontSize}fp`)
12. .lineHeight(`${this.contentFontHeight}vp`)
13. // ...
14. }
15. .gesture(
16. PinchGesture({ fingers: 2 })
17. .onActionUpdate((event?: GestureEvent) => {
18. if (event && (this.isDetailPage || this.isPictureDetail)) {
19. let tmp = this.pinchValue * event.scale;
20. if (tmp > 1.45) {
21. tmp = 1.45;
22. }
23. if (tmp < 0.75) {
24. tmp = 0.75;
25. }
26. this.scaleValue = tmp;
27. this.contentFontSize = 16 * this.scaleValue;
28. this.contentFontHeight = 25.6 * this.scaleValue;
29. this.pictureMarginTop = 8 * (this.scaleValue > 1 ? this.scaleValue : 1);
30. }
31. })
32. .onActionEnd(() => {
33. this.pinchValue = this.scaleValue;
34. })
35. )
36. // ...
37. }
38. }
39. // ...
40. }
41. // ...
42. }
```

[MircoBlogView.ets](https://gitcode.com/harmonyos_codelabs/MultiCommunityApplication/blob/master/features/detail/src/main/ets/view/MircoBlogView.ets#L33-L201)

## 示例代码

* [多设备社区评论界面](https://gitcode.com/harmonyos_codelabs/MultiCommunityApplication)
