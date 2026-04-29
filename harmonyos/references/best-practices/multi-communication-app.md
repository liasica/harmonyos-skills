---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-communication-app
title: 多设备即时通讯界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备即时通讯界面
category: best-practices
scraped_at: 2026-04-29T14:12:34+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:e64c5db77e3d546e1eae8c3df38e1ebad14782acf3f30168b6237784a8ce02cc
---

## 概述

本文从目前流行的垂类市场中，选择即时通讯应用作为典型案例详细介绍"一多"在实际开发中的应用。一多（一次开发多端部署）即时通讯应用的核心功能是用户交互，主要包含对话聊天、通讯录和社交圈等交互功能。开发者在开发“一多”应用时，经常会遇到多端适配的问题。本文针对即时通讯应用的常见多端适配问题，提供推荐解决方案。

* 聊天场景如何进行[页面开发](multi-communication-app.md#section10532313132614)

当前系统支持的产品形态包括手机、折叠屏、平板。下文的具体实践将围绕这三种产品形态展开，从UX设计和页面开发两个角度提供符合“一多”的参考样例，并介绍“一多”即时通讯应用在开发过程中的最佳实践。

* [架构设计](multi-communication-app.md#section73711812196)章节介绍一多项目的三层架构，开发者可以去相关链接了解。
* [UX设计](multi-communication-app.md#section18771832172516)章节介绍即时通讯应用的聊天场景的交互逻辑，对于类似的设计要点，开发者可以直接拿来使用。
* [页面开发](multi-communication-app.md#section10532313132614)章节主要介绍聊天场景的布局能力，介绍如何实现聊天场景，如何适配多设备。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，为开发者提供清晰、高效、可扩展的设计架构。更多详情请参考[分层架构设计](bpta-layered-architecture-design.md)。

## UX设计

即时通讯应用包含聊天、通讯录和社交圈等交互功能。聊天页采用分栏布局设计，以下为聊天页的业务逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/ZWewUaNrQe-6EgkW0LQLiw/zh-cn_image_0000002194010816.png?HW-CC-KV=V1&HW-CC-Date=20260429T061223Z&HW-CC-Expire=86400&HW-CC-Sign=9182B440F29E457D98C6BEA95FA77E5C3BAD4FA7D02F670226B6B2DD110FF52E "点击放大")

一多即时通讯场景包含以下设计能力：[侧边导航](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)、[分栏](multi-financial-app.md#section1796912148314)。

## 页面开发

以聊天页为典型页面进行展开，聊天页中包含侧边导航与分栏布局的设计能力，本文着重介绍聊天页如何实现分栏布局。

### 布局能力

聊天页在不同断点下的UX效果如下，涉及的设计能力是侧边导航，分栏布局。侧边导航参考[侧边导航](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)，其中会有详细介绍。

在sm断点（手机/折叠屏折叠状态）需页面跳转，md/lg断点（折叠屏展开/平板）支持分栏布局。为了提高操作便捷性，在IM对话页面中使用分栏布局实现对话功能。

示意图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

在sm断点下，显示聊天列表页，点击某条聊天记录时跳转到聊天详情页面；在md和lg断点下，左侧显示聊天列表页，右侧显示聊天详情页。

在多端部署场景下，Navigation组件能够根据窗口大小自动适配。当窗口较大时，Navigation组件会自动切换为分栏展示效果。因此，本文中的分栏布局使用Navigation组件实现。

各个设备布局图如下所示：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 效果图 | 参照上文表格 | | |
| 布局图 |  |  |  |

在Navigation组件中，定义了对话列表。出于封装的考虑，页面中不会使用NavRouter组件进行路由跳转，而是使用NavPathStack栈进行路由处理。因此，定义了pageInfo用于存储路由栈。当点击对话列表中的一条对话信息时，会向pageInfo中推送跳转路由。关系如下：

```
1. Navigation(this.pageInfo) {
2. if (this.currentPageIndex === 0) {
3. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
4. ConversationList({
5. currentConversationUserName: $currentConversationUserName,
6. currentContactUserName: $currentContactUserName
7. })
8. .flexGrow(1)
9. .width('100%')
10. HomeTab({ currentPageIndex: $currentPageIndex })
11. .width(Adaptive.HomeTabWidth(this.currentBreakpoint))
12. .height(Adaptive.HomeTabHeight(this.currentBreakpoint))
13. .visibility(this.currentBreakpoint !== 'lg' ? Visibility.Visible : Visibility.None)
14. }
15. .padding({
16. bottom: deviceInfo.deviceType !== 'tablet' && this.currentBreakpoint !== 'lg' ? '28vp' : '0vp'
17. })
18. .height('100%')
19. } else if (this.currentPageIndex === 1) {
20. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
21. ContactsList({
22. currentContactUserName: $currentContactUserName,
23. currentConversationUserName: $currentConversationUserName,
24. currentContactUserIcon: $currentContactUserIcon
25. })
26. .flexGrow(1)
27. .width('100%')
28. HomeTab({ currentPageIndex: $currentPageIndex })
29. .width(Adaptive.HomeTabWidth(this.currentBreakpoint))
30. .height(Adaptive.HomeTabHeight(this.currentBreakpoint))
31. .visibility(this.currentBreakpoint !== 'lg' ? Visibility.Visible : Visibility.None)
32. }
33. .height('100%')
34. .padding({
35. bottom: deviceInfo.deviceType !== 'tablet' && this.currentBreakpoint !== 'lg' ? '28vp' : '0vp'
36. })
37. }
38. }
```

[Index.ets](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication/blob/master/features/home/src/main/ets/pages/Index.ets#L81-L118)

```
1. List() {
2. ForEach(ConversationListData, (item: ConversationDataInterface, index: number) => {
3. ListItem() {
4. Row(){
5. ConversationItem(item)
6. }
7. .onClick(() => {
8. if (this.pageInfo && this.pageInfo.size() > 1) {
9. this.pageInfo.pop();
10. }
11. this.pageInfo.pushPath({ name: 'ConversationDetail' });
12. this.currentConversationUserName = item.name;
13. this.currentContactUserName = '';
14. this.currentIndex = index;
15. })
16. .backgroundColor(this.currentIndex === index ? '#33D8D8D8' : Color.White)
17. }
18. .height(Adaptive.ContactItemHeight(this.currentBreakpoint))
19. }, (item: ConversationDataInterface, index: number) => index + JSON.stringify(item))
20. }
```

[ConversationList.ets](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication/blob/master/features/home/src/main/ets/pages/ConversationList.ets#L36-L55)

此外，需要注意 Navigation 的模式和宽度在不同设备上有所不同。具体代码如下：

```
1. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
2. // ...

4. @Builder
5. PageMap(name: string) {
6. if (name === 'ConversationDetail') {
7. ConversationDetail({ currentConversationUserName: this.currentConversationUserName, currentFeatureIndex: 1});
8. } else if (name === 'ConversationDetailNone') {
9. ConversationDetailNone();
10. } else if (name === 'ContactsDetail') {
11. ContactsDetail({
12. currentContactUserName: this.currentContactUserName,
13. currentContactUserIcon: this.currentContactUserIcon
14. });
15. } else {
16. ConversationDetailNone();
17. }
18. }

20. build() {
21. Column() {
22. /**
23. * Home and contacts page
24. */
25. Flex() {
26. HomeTab({ currentPageIndex: $currentPageIndex })
27. .width(Adaptive.HomeTabWidth(this.currentBreakpoint))
28. .backgroundColor('#F1F3F5')
29. .padding({
30. top: '180vp',
31. bottom: '180vp',
32. left: '22vp'
33. })
34. .visibility(this.currentBreakpoint === 'lg' ? Visibility.Visible : Visibility.None)
35. Navigation(this.pageInfo) {
36. if (this.currentPageIndex === 0) {
37. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
38. ConversationList({
39. currentConversationUserName: $currentConversationUserName,
40. currentContactUserName: $currentContactUserName
41. })
42. .flexGrow(1)
43. .width('100%')
44. HomeTab({ currentPageIndex: $currentPageIndex })
45. .width(Adaptive.HomeTabWidth(this.currentBreakpoint))
46. .height(Adaptive.HomeTabHeight(this.currentBreakpoint))
47. .visibility(this.currentBreakpoint !== 'lg' ? Visibility.Visible : Visibility.None)
48. }
49. .padding({
50. bottom: deviceInfo.deviceType !== 'tablet' && this.currentBreakpoint !== 'lg' ? '28vp' : '0vp'
51. })
52. .height('100%')
53. } else if (this.currentPageIndex === 1) {
54. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
55. ContactsList({
56. currentContactUserName: $currentContactUserName,
57. currentConversationUserName: $currentConversationUserName,
58. currentContactUserIcon: $currentContactUserIcon
59. })
60. .flexGrow(1)
61. .width('100%')
62. HomeTab({ currentPageIndex: $currentPageIndex })
63. .width(Adaptive.HomeTabWidth(this.currentBreakpoint))
64. .height(Adaptive.HomeTabHeight(this.currentBreakpoint))
65. .visibility(this.currentBreakpoint !== 'lg' ? Visibility.Visible : Visibility.None)
66. }
67. .height('100%')
68. .padding({
69. bottom: deviceInfo.deviceType !== 'tablet' && this.currentBreakpoint !== 'lg' ? '28vp' : '0vp'
70. })
71. }
72. }
73. .hideTitleBar(true)
74. .hideToolBar(true)
75. .navBarWidth(this.currentBreakpoint === 'lg' ? '44.5%' : '50%')
76. .navDestination(this.PageMap)
77. .mode(this.currentBreakpoint === 'sm' ? NavigationMode.Stack : NavigationMode.Split)
78. .width('100%')
79. }
80. .visibility(this.currentPageIndex === 0 || this.currentPageIndex === 1 ? Visibility.Visible : Visibility.None)

82. // ...
83. }
84. // ...
85. }
```

[Index.ets](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication/blob/master/features/home/src/main/ets/pages/Index.ets#L31-L210)

```
1. @Component
2. export struct ConversationList {
3. @StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
4. @Link currentConversationUserName: Resource;
5. @Link currentContactUserName: string;
6. @State private currentIndex: number = 0;
7. @Consume('pageInfo') pageInfo: NavPathStack;

9. build() {
10. Flex({ direction: FlexDirection.Column }) {
11. HomeTopSearch(HomeConstants.CONVERSATION_TITLE, this.currentBreakpoint)
12. List() {
13. ForEach(ConversationListData, (item: ConversationDataInterface, index: number) => {
14. ListItem() {
15. Row(){
16. ConversationItem(item)
17. }
18. .onClick(() => {
19. if (this.pageInfo && this.pageInfo.size() > 1) {
20. this.pageInfo.pop();
21. }
22. this.pageInfo.pushPath({ name: 'ConversationDetail' });
23. this.currentConversationUserName = item.name;
24. this.currentContactUserName = '';
25. this.currentIndex = index;
26. })
27. .backgroundColor(this.currentIndex === index ? '#33D8D8D8' : Color.White)
28. }
29. .height(Adaptive.ContactItemHeight(this.currentBreakpoint))
30. }, (item: ConversationDataInterface, index: number) => index + JSON.stringify(item))
31. }
32. .padding({
33. bottom: deviceInfo.deviceType !== 'tablet' && this.currentBreakpoint === 'lg' ? '28vp' : '0vp'
34. })
35. .backgroundColor(Color.White)
36. .width('100%')
37. .height('100%')
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
```

[ConversationList.ets](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication/blob/master/features/home/src/main/ets/pages/ConversationList.ets#L24-L67)

```
1. @Component
2. export struct ConversationDetail {
3. @StorageProp('currentBreakpoint') currentBreakpoint: string = 'sm';
4. @Prop currentConversationUserName: string;
5. @Prop currentFeatureIndex: number;
6. @Consume('pageInfo') pageInfo: NavPathStack;

8. build() {
9. NavDestination() {
10. Flex({ direction: FlexDirection.Column }) {
11. ConversationDetailTopSearch({ currentConversationUserName: $currentConversationUserName, })
12. .height(Adaptive.ContactItemHeight(this.currentBreakpoint))
13. ConversationDetailItem({
14. receivedName: $currentConversationUserName,
15. isReceived: true,
16. content: $r('app.string.FF_take_tea'),
17. isAppletMsg: true,
18. currentFeatureIndex: $currentFeatureIndex
19. })
20. ConversationDetailItem({
21. receivedName: $currentConversationUserName,
22. isReceived: true,
23. content: $r('app.string.Speed'),
24. currentFeatureIndex: $currentFeatureIndex
25. })
26. ConversationDetailItem({
27. receivedName: $currentConversationUserName,
28. isReceived: false,
29. content: $r('app.string.happy_thing'),
30. currentFeatureIndex: $currentFeatureIndex
31. })
32. Blank()
33. ConversationDetailBottom()
34. }
35. .height('100%')
36. .width('100%')
37. .backgroundColor($r('app.color.background_color_grey'))
38. .padding({
39. bottom: deviceInfo.deviceType !== 'tablet' ? '28vp' : '0vp'
40. })
41. }
42. .hideTitleBar(true)
43. }
44. }
```

[ConversationDetail.ets](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication/blob/master/features/home/src/main/ets/pages/ConversationDetail.ets#L24-L68)

### 交互归一

系统已为不同类型的智能设备适配了相应的交互方式，实现了[交互归一](bpta-multi-interaction.md#section088812013815)，因此，开发者无需额外关注用户的不同交互方式。

本场景中的交互归一方式如下（以触控屏为例）：

1、单指点击对应组件。

2、单指滑动List和Scroll组件。

3、走焦（详情请参考[走焦规范](../harmonyos-guides/arkts-common-events-focus-event.md#走焦规范)）。

## 示例代码

* [多设备即时通讯界面](https://gitcode.com/harmonyos_codelabs/MultiDeviceCommunication)
