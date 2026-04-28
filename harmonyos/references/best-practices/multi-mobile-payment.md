---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-mobile-payment
title: 多设备移动支付界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备移动支付界面
category: best-practices
scraped_at: 2026-04-28T08:21:36+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:2e4305ce8c2470ed04a1b86fa67c8180a9d128785d23068eac59e467ce055850
---

## 概述

本文从目前流行的垂类市场中，选择移动支付应用作为典型案例详细介绍“一多”在实际开发中的应用，同时提供该垂类应用在多设备上的界面设计与实现参考。本文选择移动支付首页作为典型页面进行开发，涉及的核心功能包括支付、收款、扫码等。

本文重点内容如下：

* 扫一扫功能实现。
* 收付款功能实现。

下面的章节将分别从[UX设计](multi-mobile-payment.md#section329281918912)、[架构设计](multi-mobile-payment.md#section197441250917)、[页面开发](multi-mobile-payment.md#section189941330999)三个角度给出推荐的参考样例，介绍“一多”移动支付应用在开发过程中的最佳实践。

说明

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

[移动支付类](../design-guides/mobile-payment-0000001957421613.md)的多设备响应式设计指南。

## 架构设计

HarmonyOS应用的分层架构主要包括三个层次：产品定制层、基础特性层和公共能力层，为开发者构建了一个清晰、高效、可扩展的设计架构。更多详细信息，请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍移动支付应用中如何使用“一多”的布局能力，完成页面层级的一套代码、多端适配。下文将从不同页面展开，介绍每个页面区域使用到具体的布局能力，帮助开发者从零到一进行移动支付应用的开发。

### 首页

移动应用首页主要涉及扫一扫、支付、收付款等能力。观察首页在多设备上的UX设计图，可以进行如下设计：

* 将首页划分为6个部分，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 底部/侧边页签 | 借助[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化改变位置。同多设备长视频界面[顶部页签及搜索框](multi-video-app.md#zh-cn_topic_0000001744653537_li1346175796)。 |
  | 2 | 城市及搜索框 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。同多设备长视频界面[搜索发现](multi-video-app.md#zh-cn_topic_0000001744653537_li311217374149)。 |
  | 3 | 金刚区 | 使用[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)结合断点变化改变快捷功能的形态。 |
  | 4 | 功能入口合集 | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，在更大尺寸设备上显示更多的功能入口。同多设备社区评论界面[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
  | 5 | 服务卡片 | 采用[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，手机上的单列信息，在折叠屏和平板上重复布局。同多设备社区评论界面[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
  | 6 | 财富精选 | 采用[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)，在更大尺寸设备上显示更多列数。 |

* 金刚区

  使用栅格布局配合断点控制对应的快捷功能的显示形态，在sm断点下按钮显示为圆形图标且上图标下文字的形式，在md、lg断点下显示为圆角矩形且左图标右文字形式。

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  ```
  1. GridRow({
  2. columns: 12,
  3. gutter: {
  4. x: {
  5. sm: '30vp',
  6. md: '41vp',
  7. lg: '58vp'
  8. }
  9. }
  10. }) {
  11. ForEach(this.quickFunctions, (item: QuickFunctionItem) => {
  12. GridCol({ span: 3 }) {
  13. if (this.curBp === 'sm') {
  14. QuickFunctionCardCircle({ quickFunctionItem: item })
  15. } else {
  16. QuickFunctionCardSquare({ quickFunctionItem: item })
  17. }
  18. }
  19. // ...
  20. }, (item: QuickFunctionItem, index: number) => JSON.stringify(item.getText()) + index)
  21. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L211-L237)

* 功能入口合集

  使用重复布局，配合栅格布局控制不同设备上的显示列数。在sm断点下设置GridRow的columns属性为4，在md断点下设置GridRow的columns属性为6，在lg断点下设置GridRow的columns属性为8。同时通过GridRow的onBreakpointChange()回调控制渲染数据源的条数，在sm、md、lg断点下分别渲染8、12、16条数据。

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 设计能力点 |  | | |
  | 效果图 |  |  |  |

  ```
  1. GridRow({
  2. columns: {
  3. sm: 4,
  4. md: 6,
  5. lg: 8
  6. },
  7. gutter: {
  8. x: {
  9. sm: '45vp',
  10. md: '50vp',
  11. lg: '55vp'
  12. },
  13. y: {
  14. sm: '16vp',
  15. md: '24vp',
  16. lg: '28vp'
  17. }
  18. }
  19. }) {
  20. ForEach(this.functions, (item: QuickFunctionItem) => {
  21. GridCol() {
  22. FunctionCard({ data: item })
  23. }
  24. }, (item: QuickFunctionItem, index: number) => index + JSON.stringify(item))
  25. }
  26. // ...
  27. .onBreakpointChange((breakpoints: string) => {
  28. this.functions = new PayHubViewModel().getFunctionsByBreakpoints(breakpoints);
  29. // close dialog.
  30. if (this.isDialogOpen) {
  31. this.isDialogOpen = false;
  32. }
  33. })
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L266-L302)

* 服务卡片

  使用重复布局配合栅格布局控制不同设备尺寸下的显示列数。在sm断点下设置GridCol的span属性为12，在md断点下设置GridCol的span属性为6，在lg断点下设置GridCol的span属性为3。同时配合GridRow的onBreakpointChange()回调控制渲染的数据条数，使得在sm、md、lg断点下分别渲染1、2、4条数据。

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 设计能力点 |  | | |
  | 效果图 |  |  |  |

  ```
  1. GridRow({
  2. columns: 12,
  3. gutter: { x: { sm: '15vp' } }
  4. }) {
  5. ForEach(this.sampleImages, (item: Resource) => {
  6. GridCol({
  7. span: {
  8. sm: 12,
  9. md: 6,
  10. lg: 3
  11. }
  12. }) {
  13. Image(item)
  14. .width('100%')
  15. }
  16. }, (item: Resource, index: number) => index + JSON.stringify(item))
  17. }
  18. // ...
  19. .onBreakpointChange((breakpoints: string) => {
  20. this.sampleImages = new ServiceCardViewModel().getImagesByBreakpoints(breakpoints);
  21. })
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L328-L357)

* 财富精选

  使用栅格布局控制不同设备尺寸下显示列数，在sm断点下设置GridCol的span属性为12，在md断点下设置GridCol的span属性为6，在lg断点下设置GridCol的span属性为3。

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  ```
  1. GridRow({
  2. columns: 12,
  3. gutter: { x: { sm: '15vp' }, y: { sm: '15vp' } }
  4. }) {
  5. ForEach(this.fortunePicks, (item: Resource) => {
  6. GridCol({
  7. span: {
  8. sm: 12,
  9. md: 6,
  10. lg: 3
  11. }
  12. }) {
  13. Image(item)
  14. .width('100%')
  15. }
  16. }, (item: Resource, index: number) => index + JSON.stringify(item))

  18. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L371-L388)

* 收付款功能

  收付款功能在手机设备上以单独的界面进行呈现，而在折叠屏及更大尺寸设备上以弹窗的方式进行呈现。UX设计图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  收付款功能在实现上，需要根据当前设备的断点尺寸，来决定是使用路由跳转到收付款页，还是以弹窗的方式弹出收付款对话框，代码参考如下：

  ```
  1. private receivePayment = () => {
  2. if (this.curBp === 'sm') {
  3. this.pathInfos.pushPath({ name: 'ReceivePaymentPage' });
  4. } else if (!this.isDialogOpen) {
  5. this.isDialogOpen = true;
  6. }
  7. };
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L57-L63)

  自定义收款码生成需要使用到Scan Kit中的[通过文本生成码图](../harmonyos-guides/scan-barcodegenerate.md)，关键为使用[generateBarcode.createBarcode()](../harmonyos-references/scan-generatebarcode.md#section1841142919352)接口依照收款所需的关键信息生成对应的二维码。参考代码如下：

  ```
  1. let content: string = this.getQRCode();
  2. const options: generateBarcode.CreateOptions = {
  3. scanType: scanCore.ScanType.QR_CODE,
  4. height: Constants.QRCODE_SIZE,
  5. width: Constants.QRCODE_SIZE
  6. };
  7. generateBarcode.createBarcode(content, options, (error: BusinessError, pixelMap: image.PixelMap) => {
  8. if (error) {
  9. Logger.error(`Callback error: ${JSON.stringify(error)}`);
  10. return;
  11. }
  12. this.pixelMap = pixelMap;
  13. });
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L441-L453)

  收付款界面开发时常见的问题如下：

  第一个问题是二维码定时动态刷新。解决方案为在组件展示或弹窗开启时，启动一个定时器并在回调中传入一个更新二维码的函数，定时地向服务端发起请求获取最新的二维码并对本地二维码进行更新，在组件销毁或弹窗关闭时需要销毁定时器。组件情况下解决二维码定时动态刷新可参考如下代码：

  ```
  1. private timer: number | null = null;
  2. private getQRCode = () => (new Date()).valueOf().toString();

  4. private getAndUpdateQRCode(): void {
  5. // ...
  6. }

  8. aboutToAppear(): void {
  9. this.getAndUpdateQRCode();
  10. this.timer = setInterval(() => {
  11. this.getAndUpdateQRCode();
  12. }, 60 * 1000);
  13. }

  15. aboutToDisappear(): void {
  16. this.timer = null;
  17. }
  ```

  [ReceivePaymentPage.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/ReceivePaymentPage.ets#L31-L65)

  弹窗情况下解决二维码定时动态刷新可参考如下代码：

  ```
  1. private timer: number | null = null;
  2. private getQRCode = () => (new Date()).valueOf().toString();

  4. aboutToAppear(): void {
  5. this.getAndUpdateQRCode();
  6. this.timer = setInterval(() => {
  7. this.getAndUpdateQRCode();
  8. }, 60 * 1000);
  9. }

  11. private getAndUpdateQRCode(): void {
  12. // ...
  13. }

  15. aboutToDisappear(): void {
  16. this.pixelMap = undefined;
  17. this.timer = null;
  18. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L428-L461)

  第二个问题是折叠屏在折叠态与展开态变化时，页面切换流畅。如果应用处在收付款界面，折叠屏从折叠态到展开态，如果不做特殊操作，应用将仍然处在收付款的界面，只是整体尺寸被拉大，同样的，在从展开态到折叠态如果已有弹窗，也会导致整个界面错乱。解决方案为在断点变化时，监听当前路由状态并且控制弹出框的显示与关闭。

  ```
  1. @StorageProp('currentBreakpoint') @Watch('onBreakpointChange') curBp: string = 'sm';
  2. @State @Watch('onDialogStatusChange') isDialogOpen: boolean = false;
  3. // ...
  4. onDialogStatusChange() {
  5. if (this.isDialogOpen) {
  6. this.dialogController.open();
  7. } else {
  8. this.dialogController.close();
  9. }
  10. }

  12. onScanDialogStatusChange() {
  13. if (this.isScanDialogOpen) {
  14. this.scanDialogController.open();
  15. } else {
  16. this.scanDialogController.close();
  17. }
  18. }

  20. onBreakpointChange() {
  21. const allPath = this.pathInfos.getAllPathName();
  22. const currentName: string = allPath[this.pathInfos.size() - 1];

  24. if (this.curBp !== 'sm' && currentName === 'ReceivePaymentPage') {
  25. this.pathInfos.clear();
  26. setTimeout(() => {
  27. this.isDialogOpen = true;
  28. }, 1000);
  29. }

  31. if (this.isDialogOpen && this.curBp === 'sm') {
  32. this.isDialogOpen = false;
  33. this.pathInfos.pushPath({ name: 'ReceivePaymentPage' });
  34. }
  35. // ...
  36. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/multi-mobile-payment/blob/master/entry/src/main/ets/pages/Home.ets#L38-L140)

  第三个问题是应用窗口尺寸动态变化时二维码可能会产生变形，该问题可以通过设置二维码的大小为固定百分比或者使用[aspectRatio()](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)固定宽高比的方式来解决。

  点击[generateBarcode.createBarcode()](../harmonyos-references/scan-generatebarcode.md#section1841142919352)获取更多该接口使用指导。
* 扫一扫

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  扫一扫功能主要使用Scan Kit中的[自定义界面扫码](../harmonyos-guides/scan-customscan.md)能力来自定义扫码的界面设计。具体实现可以参考：多设备移动支付界面[收付款功能](multi-mobile-payment.md#li9776152192816)。
* 第三方支付链接

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  第三方支付页面使用断点控制不同的付款展示方式，在sm断点下以单独付款界面展示，在md、lg断点下以弹窗的方式展示。具体实现可以参考多设备移动支付界面[收付款功能](multi-mobile-payment.md#li9776152192816)。
* 卡包

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  使用[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)布局，控制卡片在不同设备上的span占用，在sm断点下span占用为12，在md断点下span占用为6，在lg断点下span占用为4，使其分别在sm、md、lg断点下显示1、2、3列。具体实现可以参考：多设备长视频界面[推荐视频](multi-video-app.md#zh-cn_topic_0000001744653537_li19261618201020)。
* 银行卡

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  | 区域编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部栏 | 顶部栏空白区域使用Blank组件实现拉伸能力。同多设备长视频界面[搜索发现](multi-video-app.md#zh-cn_topic_0000001744653537_li311217374149)。 |
  | 2 | 卡片集合 | 使用栅格布局，在sm、md、lg设备尺寸下分别显示1、2、3列。同多设备长视频界面[搜索页](multi-video-app.md#section1932711221013)。 |
  | 3 | 功能入口 | 使用栅格布局实现[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，在sm设备上显示4列，在md设备上显示7列，在lg设备上显示9列。同多设备社区评论界面[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
  | 4 | 银行卡优惠 | 使用栅格布局实现[重复布局](bpta-multi-device-responsive-layout.md#section1653271133613)，在sm设备上显示1列，在md设备上显示2列，在lg设备上显示3列。同多设备社区评论界面[列表重复布局](multi-community-app.md#zh-cn_topic_0000001758831130_li118141522111817)。 |
* 添加银行卡

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 效果图 |  |  |  |

  添加银行卡功能可以使用[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)，默认情况下在sm设备下可以自动从底部进行弹窗，在sm断点以上不包括sm断点以居中弹窗方式显示内容。

## 示例代码

* [多设备移动支付界面](https://gitcode.com/harmonyos_samples/multi-mobile-payment)
