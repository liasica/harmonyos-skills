---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-set-back-forward-cache
title: 设置Web组件前进后退缓存
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > 设置Web组件前进后退缓存
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6258787a8cdf245ac3b8badfd3ce71f541d1e707debcc8d41138fa2213693417
---

Web组件为开发者提供了启用和配置前进后退缓存（以下简称BFCache）的功能。启用此功能后，能够显著提升用户返回至先前浏览网页的速度，尤其对于网络条件不佳的用户，可提供更为流畅的浏览体验。

BFCache功能启用后，Web组件会在用户离开当前页面时在内存中保存该页面的快照。当用户在短期内通过Web组件的前进或后退功能重新访问同一页面时，能够迅速恢复页面状态，避免重复发起HTTP请求。

## Web组件开启BFCache

开发者需要在调用[initializeWebEngine()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)初始化ArkWeb内核之前调用[enableBackForwardCache()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#enablebackforwardcache12)来开启BFCache。enableBackForwardCache可以接收一个[BackForwardCacheSupportedFeatures](../harmonyos-references/kts-apis-webview-backforwardcachesupportedfeatures.md)参数，用于控制是否允许具备同层渲染特性和视频托管特性的页面进入BFCache。

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { webview } from '@kit.ArkWeb';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
9. let features = new webview.BackForwardCacheSupportedFeatures();
10. features.nativeEmbed = true;
11. features.mediaTakeOver = true;
12. webview.WebviewController.enableBackForwardCache(features);
13. webview.WebviewController.initializeWebEngine();
14. AppStorage.setOrCreate("abilityWant", want);
15. }
16. }
```

## 设置缓存的页面数量和页面留存的时间

启用BFCache后默认仅能存储一个页面，Web组件默认进入BFCache的页面可保持存活状态600秒。开发者可通过调用[setBackForwardCacheOptions()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setbackforwardcacheoptions12)设置每个Web实例的前进后退缓存策略。包括调整缓存中页面的最大数量，使BFCache能够容纳更多页面，从而在用户连续进行前进后退操作时，提供更快的加载速度。同时，开发者还能修改每个页面在缓存中的停留时间，延长页面在BFCache中的驻留期限，进而优化用户的浏览体验。

在下面的示例中，设置Web组件可以缓存的最大数量为10，每个页面在缓存中停留300秒。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Row() {
11. Button('Add options').onClick((event: ClickEvent) => {
12. let options = new webview.BackForwardCacheOptions();
13. options.size = 10;
14. options.timeToLive = 300;
15. this.controller.setBackForwardCacheOptions(options);
16. })
17. Button('Backward').onClick((event: ClickEvent) => {
18. this.controller.backward();
19. })
20. Button('Forward').onClick((event: ClickEvent) => {
21. this.controller.forward();
22. })
23. }
24. Web({ src: 'https://www.example.com', controller: this.controller })
25. }
26. .height('100%')
27. .width('100%')
28. }
29. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/NetReqInterceptCacheWinOps/entry2/src/main/ets/pages/Index.ets#L16-L46)
