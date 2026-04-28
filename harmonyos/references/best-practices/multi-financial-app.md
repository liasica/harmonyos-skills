---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-financial-app
title: 多设备银行理财界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备银行理财界面
category: best-practices
scraped_at: 2026-04-28T08:21:26+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:e9b2cb5423de3b4b51786f411d2feb6ec0df5daeb93a83abf695dcfaea371edf
---

## 概述

本文以银行理财应用作为典型案例详细介绍“一多”在实际开发中的应用。银行理财应用在大屏幕设备上使用时，不仅要保障用户在办理金融业务过程中的正常使用，还要提升屏幕的交互效率。具体功能包括首页推荐、产品专题、产品详情、产品对比和收益明细。

当前示例适配的产品形态包括直板机、双折叠（Mate X系列）、平板三种。下面的章节将分别从[架构设计](multi-financial-app.md#section54591344599)、[UX设计](multi-financial-app.md#section17338114012)、[页面开发](multi-financial-app.md#section542810436010)三个角度给出推荐的参考样例，介绍“一多”银行理财应用在开发过程中的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## 架构设计

HarmonyOS的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详细信息请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## UX设计

参考[金融理财类](../design-guides/responsive-design-examples6-0000001793536905.md)的多设备响应式设计指南。

银行理财应用包含以下设计要点：[弹窗](multi-financial-app.md#section7407927311)、[延伸布局](multi-financial-app.md#section279819344216)、[分栏](multi-financial-app.md#section1796912148314)、[底部/侧边页签](multi-video-app.md#zh-cn_topic_0000001744653537_li1226615201361)、[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。底部/侧边页签、列表重复布局在其他的“一多”案例中有详细的介绍，本案例以弹窗和延伸布局以及分栏为重点进行介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/hFAWsO6sQwGOGH4XODMBWQ/zh-cn_image_0000002194010120.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=39C447D054EDF1B3012F9953C515AA8D03AAFD4992621B4FD5E96250DC328385 "点击放大")

弹窗使用自定义弹窗CustomDialog实现，首次打开应用时通过CustomDialogController类显示自定义弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/gpx2BBs5Rqm7FwHMo_J8Zw/zh-cn_image_0000002229335949.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=633E623F82A7C85D3725230CD9C48EC401843D8C4EB54A792896E3C0C30F3F69 "点击放大")

使用list组件实现产品专题页面中的稳健增长信息。通过设置不同断点下的列数，实现延伸布局，以便在大屏上显示更多信息，提升屏幕交互效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/UxXEorN2RQu0Xto8kaMLRw/zh-cn_image_0000002229335945.png?HW-CC-KV=V1&HW-CC-Date=20260428T002114Z&HW-CC-Expire=86400&HW-CC-Sign=A8E657877CDCC9C6D160C5A5A51B9CC88E2BF166DF0BD55FE51F1724F71767D5 "点击放大")

产品详情页面使用 Navigation 实现分栏效果。在手机上，内容单栏显示；在平板等大屏设备上，内容分栏显示，左侧为导航区，右侧为内容区。点击“稳健增长”下的内容可控制右侧内容区的信息展示。

## 页面开发

本章节选取页面关键区域进行“一多”页面布局能力介绍。

### 弹窗

弹窗使用[自定义弹窗 (CustomDialog)](../harmonyos-references/ts-methods-custom-dialog-box.md)实现，在初始化弹窗时设置customStyle为true，则弹窗样式由开发者自定义，在sm、md、lg不同的断点设置固定的宽高值，使弹窗的大小在不同设备显示相差不大。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. @Entry
2. @Component
3. struct Index {
4. // ...
5. dialogController: CustomDialogController = new CustomDialogController({
6. builder: AdvertisementDialog(),
7. backgroundColor: $r('app.color.dialog_background'),
8. alignment: DialogAlignment.Center,
9. maskColor: $r('app.color.dialog_mask'),
10. customStyle: true
11. });

13. aboutToAppear() {
14. this.dialogController.open();
15. }
16. // ...
17. }
```

[Index.ets](https://gitcode.com/harmonyos_codelabs/MultiFinancialManagement/blob/master/product/phone/src/main/ets/pages/Index.ets#L28-L263)

### 延伸布局

延伸布局使用[List](../harmonyos-references/ts-container-list.md)列表来实现，在不同断点条件下，使用list加载不同数量的数据，并设置list的lanes属性以显示不同列数：sm、md、lg下分别显示2列、3列、5列。这样可以确保数据在不同设备上显示合适数量，提高屏幕交互效率。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. List() {
2. ForEach(new BreakpointUtil({
3. sm: FundingViewModel.getAllFundInfo(0, 2),
4. md: FundingViewModel.getAllFundInfo(0, 4),
5. lg: FundingViewModel.getAllFundInfo(0, 6)
6. }).getValue(this.currentPoint), (item: FundDetail) => {
7. ListItem() {
8. Row() {
9. Text(item.amplitude)
10. .fontSize('24fp')
11. .fontColor('#E84026')
12. .fontWeight(700)
13. Text(item.name)
14. .fontSize('16fp')
15. .fontWeight(500)
16. .fontFamily('HarmonyHeiTi-Medium')
17. .margin({ left: '16vp' })
18. }
19. .justifyContent(FlexAlign.SpaceAround)
20. }
21. })
22. }
23. .lanes(new BreakpointUtil({ sm: 1, md: 2, lg: 3 }).getValue(this.currentPoint))
24. .width(CommonConstants.FULL_WIDTH_PERCENT)
```

[FundComponent.ets](https://gitcode.com/harmonyos_codelabs/MultiFinancialManagement/blob/master/features/fund/src/main/ets/view/FundComponent.ets#L157-L180)

### 分栏

分栏布局通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)实现，在断点为lg时，设置mode属性为NavigationMode.Split，实现分栏效果。在其他断点下，设置mode属性为NavigationMode.Stack，显示单栏效果。

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 设计能力点 |  | | |
| 效果图 |  |  |  |

```
1. Navigation(this.pageInfo) {
2. FundNavigationComponent({ listIndex: this.index })
3. }
4. .navDestination(this.buildNavDestination)
5. .hideTitleBar(true)
6. .hideBackButton(true)
7. .mode(this.breakPoint === 'lg' ? NavigationMode.Split : NavigationMode.Stack)
8. .navBarWidth('40%')
```

[FundingDetail.ets](https://gitcode.com/harmonyos_codelabs/MultiFinancialManagement/blob/master/features/fund/src/main/ets/view/FundingDetail.ets#L60-L67)

```
1. @Builder
2. buildNavDestination(name: string, param: object) {
3. if (name === 'detail') {
4. if (typeof param === 'number') {
5. DetailComponent({ indexList: param })
6. }
7. } else if (name === 'comparison') {
8. ComparisonComponent()
9. } else if (name === 'comparisonDetail') {
10. NavDestination() {
11. ComparisonDetailComponent({ chooseComparison: (param as ComparisonInfo[]) })
12. }
13. .hideTitleBar(true)
14. } else if (name === 'buying') {
15. if (typeof param === 'number') {
16. TransactionComponent({ indexList: param })
17. }
18. }
19. }
```

[FundingDetail.ets](https://gitcode.com/harmonyos_codelabs/MultiFinancialManagement/blob/master/features/fund/src/main/ets/view/FundingDetail.ets#L113-L131)

## 示例代码

* [多设备银行理财界面](https://gitcode.com/harmonyos_codelabs/MultiFinancialManagement)
