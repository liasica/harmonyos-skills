---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-event-sequence
title: Web组件的生命周期
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web组件的生命周期
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4fe51f2e31bc71364cecd7c8376b1e999ef9143bf203bfedf6da9dd2e7a8538e
---

## 概述

开发者可以使用Web组件加载本地或者在线网页。

Web组件提供生命周期回调接口，用于感知状态变化和处理业务。

Web组件的状态主要包括：Controller绑定到Web组件、网页加载开始、网页加载进度、网页加载结束、页面即将可见。

Web页面保活可以参考[使用离线Web组件](web-offline-mode.md)。

自定义组件析构销毁时执行[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)函数，Web组件会被销毁，Web组件与[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)解绑，js运行环境也会一并销毁。

**图1** Web组件网页正常加载过程中的回调事件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/nF2wrMCTS4ucpz6bwby4Ww/zh-cn_image_0000002589244505.png?HW-CC-KV=V1&HW-CC-Date=20260429T052912Z&HW-CC-Expire=86400&HW-CC-Sign=DFE4F1F30392B37C21B5F0AB6B7B60092AB959CF9F78361DB4E6CA31190678C8)

## Web组件网页正常加载过程所涉及的状态说明

* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数：在创建自定义组件的新实例后，在执行其build函数前执行。建议在此设置WebDebug调试模式、自定义协议URL的权限、Cookie等。
* [onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)事件：当Controller成功绑定到Web组件时触发该回调，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出js-error异常。建议在此事件中注入JS对象、设置自定义用户代理，使用操作网页不相关的接口。但因为该回调调用时网页还未加载，因此无法在回调中使用有关操作网页的接口，例如[zoomIn](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomin)、[zoomOut](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#zoomout)等。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)事件：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。
* [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)事件：当Web组件加载url之前触发该回调，用于拦截url并返回响应数据。
* [onPageBegin](../harmonyos-references/arkts-basic-components-web-events.md#onpagebegin)事件：网页开始加载时触发该回调，且只在主frame（表示一个用于展示HTML页面的元素）触发。如果是iframe或者frameset（用于包含frame的HTML标签）的内容加载时则不会触发此回调。多frame页面可能同时加载，主frame加载结束时子frame可能仍在加载。同一页面导航或失败的导航不会触发该回调。
* [onProgressChange](../harmonyos-references/arkts-basic-components-web-events.md#onprogresschange)事件：告知开发者当前页面加载的进度。多frame页面或者子frame可能还在继续加载而主frame已经加载结束，所以在[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)事件后仍可能收到该事件。
* [onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)事件：网页加载完成时触发该回调，且只在主frame触发。多frame页面有可能同时开始加载，即使主frame已经加载结束，子frame也有可能才开始或者继续加载中。同一页面导航或失败的导航不会触发该回调。建议在此回调中执行JavaScript脚本。注意，收到该回调不能保证下一帧反映DOM状态。

## Web组件网页异常加载过程所涉及的状态说明

* [onOverrideUrlLoading](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideurlloading12)事件：当URL将要加载到当前Web中时，让宿主应用程序有机会获得控制权，回调函数返回true将导致当前Web中止加载URL，而返回false则会导致Web继续照常加载URL。onLoadIntercept接口和onOverrideUrlLoading接口行为不一致，触发时机也不同，所以在应用场景上存在一定区别。onLoadIntercept事件在LoadUrl和iframe加载时触发，但onOverrideUrlLoading事件在LoadUrl和特定iframe加载时不会触发。
* [onPageVisible](../harmonyos-references/arkts-basic-components-web-events.md#onpagevisible9)事件：Web回调事件。渲染流程中当HTTP响应的主体开始加载，新页面即将可见时触发该回调。此时文档加载还处于早期，因此链接的资源比如在线CSS、在线图片等可能尚不可用。
* [onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)事件：应用渲染进程异常退出时触发该回调，可以在此回调中进行系统资源的释放、数据的保存等操作。如果应用希望异常恢复，需要调用[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口重新加载页面。详细用法参考[应用如何避免Web组件渲染子进程异常退出导致的页面卡死问题](web-event-sequence.md#应用如何避免web组件渲染子进程异常退出导致的页面卡死问题)。
* [onDisAppear](../harmonyos-references/ts-universal-events-show-hide.md#ondisappear)事件：组件卸载消失时触发此回调。该事件在组件卸载时触发。
* 应用侧代码。

  ```
  1. // xxx.ets
  2. import { webview } from '@kit.ArkWeb';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. @Entry
  6. @Component
  7. struct WebComponent {
  8. controller: webview.WebviewController = new webview.WebviewController();
  9. responseWeb: WebResourceResponse = new WebResourceResponse();
  10. heads: Header[] = new Array();
  11. @State webData: string = "<!DOCTYPE html>\n" +
  12. "<html>\n" +
  13. "<head>\n" +
  14. "<title>intercept test</title>\n" +
  15. "</head>\n" +
  16. "<body>\n" +
  17. "<h1>intercept test</h1>\n" +
  18. "</body>\n" +
  19. "</html>";

  21. aboutToAppear(): void {
  22. try {
  23. webview.WebviewController.setWebDebuggingAccess(true);
  24. } catch (error) {
  25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  26. }
  27. }

  29. build() {
  30. Column() {
  31. Web({ src: 'www.example.com', controller: this.controller })
  32. .onControllerAttached(() => {
  33. // 推荐在此loadUrl、设置自定义用户代理、注入JS对象等
  34. console.info('onControllerAttached execute')
  35. })
  36. .onLoadIntercept((event) => {
  37. if (event) {
  38. console.info('onLoadIntercept url:' + event.data.getRequestUrl())
  39. console.info('url:' + event.data.getRequestUrl())
  40. console.info('isMainFrame:' + event.data.isMainFrame())
  41. console.info('isRedirect:' + event.data.isRedirect())
  42. console.info('isRequestGesture:' + event.data.isRequestGesture())
  43. }
  44. // 返回true表示阻止此次加载，否则允许此次加载
  45. return false;
  46. })
  47. .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
  48. if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
  49. return true;
  50. }
  51. return false;
  52. })
  53. .onInterceptRequest((event) => {
  54. if (event) {
  55. console.info('url:' + event.request.getRequestUrl());
  56. }
  57. let head1: Header = {
  58. headerKey: "Connection",
  59. headerValue: "keep-alive"
  60. }
  61. let head2: Header = {
  62. headerKey: "Cache-Control",
  63. headerValue: "no-cache"
  64. }
  65. // 将新元素追加到数组的末尾，并返回数组的新长度。
  66. let length = this.heads.push(head1);
  67. length = this.heads.push(head2);
  68. console.info('The response header result length is :' + length);
  69. this.responseWeb.setResponseHeader(this.heads);
  70. this.responseWeb.setResponseData(this.webData);
  71. this.responseWeb.setResponseEncoding('utf-8');
  72. this.responseWeb.setResponseMimeType('text/html');
  73. this.responseWeb.setResponseCode(200);
  74. this.responseWeb.setReasonMessage('OK');
  75. // 返回响应数据则按照响应数据加载，无响应数据则返回null表示按照原来的方式加载
  76. return this.responseWeb;
  77. })
  78. .onPageBegin((event) => {
  79. if (event) {
  80. console.info('onPageBegin url:' + event.url);
  81. }
  82. })
  83. .onFirstContentfulPaint(event => {
  84. if (event) {
  85. console.info("onFirstContentfulPaint:" + "[navigationStartTick]:" +
  86. event.navigationStartTick + ", [firstContentfulPaintMs]:" +
  87. event.firstContentfulPaintMs);
  88. }
  89. })
  90. .onProgressChange((event) => {
  91. if (event) {
  92. console.info('newProgress:' + event.newProgress);
  93. }
  94. })
  95. .onPageEnd((event) => {
  96. // 推荐在此事件中执行JavaScript脚本
  97. if (event) {
  98. console.info('onPageEnd url:' + event.url);
  99. }
  100. })
  101. .onPageVisible((event) => {
  102. console.info('onPageVisible url:' + event.url);
  103. })
  104. .onRenderExited((event) => {
  105. if (event) {
  106. console.info('onRenderExited reason:' + event.renderExitReason);
  107. }
  108. })
  109. .onDisAppear(() => {
  110. this.getUIContext().getPromptAction().showToast({
  111. message: 'The web is hidden',
  112. duration: 2000
  113. })
  114. })
  115. }
  116. }
  117. }
  ```

## Web组件网页加载的性能指标

网页加载过程中需要关注一些重要的性能指标。例如，FCP(First Contentful Paint)首次内容绘制，FMP(First Meaningful Paint)首次有效绘制，LCP(Largest Contentful Paint)最大内容绘制等。Web组件提供了如下接口来通知开发者，接口仅支持在线非PDF网页，不支持本地网页和PDF网页。

* [onFirstContentfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstcontentfulpaint10)事件：网页首次内容绘制的回调函数。首次绘制文本、图像、非空白[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)或SVG的时间点。
* [onFirstMeaningfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstmeaningfulpaint12)事件：网页绘制页面主要内容的回调函数。首次绘制主要内容的时间点。
* [onLargestContentfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onlargestcontentfulpaint12)事件：网页绘制页面最大内容的回调函数。绘制可视区域内最大图片、文本块或视频的时间点。

## 应用如何避免Web组件渲染子进程异常退出导致的页面卡死问题

ArkWeb（方舟Web）是一个Web组件平台，旨在为应用程序提供展示Web页面内容的功能，并向开发者提供一系列的能力，如页面加载、交互和调试等功能。使用ArkWeb相关应用时，可能因各种原因（例如前端偶现异常导致ArkWeb渲染子进程崩溃，或是打开的应用较多，系统资源紧张导致后台ArkWeb渲染子进程被终止）而出现页面卡死的问题，这时需要重新打开页面或重启应用来解决。

在ArkWeb渲染子进程异常退出导致页面卡死后，应用可通过监听[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)事件来获取具体的退出原因[RenderExitReason](../harmonyos-references/arkts-basic-components-web-e.md#renderexitreason9)，并在异常回调中根据退出的具体原因，执行相应的异常处理。

**开发实践案例**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. needReloadWhenVisible: boolean = false;  // Web组件不可见时render退出后阻止重新加载页面，在可见时重新加载页面。
7. webIsVisible: boolean = false;            // 判断Web组件是否可见。

9. // 此处是将子进程异常崩溃和其它异常原因做了区分，应用开发者可根据实际业务特点，细化对应异常的处理策略。
10. renderReloadMaxForCrashed: number = 5;    // 设置因为异常崩溃后重新加载的最大重试次数，应用可根据业务特点，自行设置试错上限。
11. renderReloadCountForCrashed: number = 0;  // 异常崩溃后重新加载的次数。
12. renderReloadMaxForOthers: number = 10;    // 设置因为其它异常原因退出的最大重试次数，应用可根据业务特点，自行设置试错上限。
13. renderReloadCountForOthers: number = 0;   // 其它异常原因退出后重新加载的次数。

15. // 创建Web组件。
16. controller: webview.WebviewController = new webview.WebviewController();

18. // 指定加载的页面。
19. url: string = "www.example.com";
20. build() {
21. Column() {
22. Web({ src: this.url, controller: this.controller })
23. .onVisibleAreaChange([0, 1.0], (isVisible) => {
24. this.webIsVisible = isVisible;
25. if (isVisible && this.needReloadWhenVisible) { // Web组件可见时重新加载页面。
26. this.needReloadWhenVisible = false;
27. this.controller.loadUrl(this.url);
28. }
29. })
30. // 应用监听渲染子进程异常退出回调，并进行异常处理。
31. .onRenderExited((event) => {
32. if (!event) {
33. return;
34. }
35. if (event.renderExitReason == RenderExitReason.ProcessCrashed) {
36. if (this.renderReloadCountForCrashed >= this.renderReloadMaxForCrashed) {
37. // 设置重试次数上限保护，避免必现问题导致页面被循环加载。
38. return;
39. }
40. console.info('renderReloadCountForCrashed: ' + this.renderReloadCountForCrashed);
41. this.renderReloadCountForCrashed++;
42. } else {
43. if (this.renderReloadCountForOthers >= this.renderReloadMaxForOthers) {
44. // 设置重试次数上限保护, 避免必现问题导致页面被循环加载。
45. return;
46. }
47. console.info('renderReloadCountForOthers: ' + this.renderReloadCountForOthers);
48. this.renderReloadCountForOthers++;
49. }
50. if (this.webIsVisible) {
51. // Web组件可见则立即重新加载。
52. this.controller.loadUrl(this.url);
53. return;
54. }
55. // Web组件不可见时不立即重新加载。
56. this.needReloadWhenVisible = true;
57. })
58. }
59. }
60. }
```
