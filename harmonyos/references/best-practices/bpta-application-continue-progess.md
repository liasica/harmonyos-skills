---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-continue-progess
title: 常见接续最佳实践
breadcrumb: 最佳实践 > 自由流转 > 跨端迁移 > 常见接续最佳实践
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:4066b45f828ff1fbef69ad1e026c3d3619fba8551bcabbc6c80f4163d4048023
---

## 概述

接续是一种用户体验优化技术。在个人设备数量激增的当代，若用户在使用应用时附近有合适的设备，可通过该功能将应用无缝切换至新设备继续操作。本文主要针对长列表进度、媒体播放进度和Web浏览进度三个场景，实现了浏览进度的高效接续。用户切换设备时可轻松恢复之前的浏览进度，极大提升使用便捷性与连贯性，提供设备无缝切换的流畅体验。

* [长列表进度接续](bpta-application-continue-progess.md#section16702516134216)：允许用户从上次离开位置继续浏览，精准定位到目标条目附近，避免重复滚动，节省时间并减少操作成本，提升浏览体验。
* [媒体播放进度接续](bpta-application-continue-progess.md#section12439210434)：从源设备当前播放位置继续视频播放，保持播放进度、画面质量及音频设置的一致性，确保用户观影体验不被打断。支持在线视频平台的剧集、电影以及本地存储的视频文件，实现流畅接续播放。
* [Web浏览进度接续](bpta-application-continue-progess.md#section3512987460)：可快速定位至源设备浏览的网页位置，确保用户浏览连续性，避免重复查找信息的不便，提升信息获取效率。

## 实现原理

接续过程底层依赖分布式框架和软总线，开发者只需要启用接续、保存数据和恢复数据，具体运作机制可参考：[运作机制](bpta-continue-cast.md#section1218874218264)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/vlHwynjQSWmRhm3PRJjXCQ/zh-cn_image_0000002622048193.png "点击放大")

## 开发流程

进度接续的核心在于确保进度数据在不同设备间的精确传输与同步。在实际开发过程中，开发者会遇到各类复杂的接续需求，首要任务是深入分析对接续控制至关重要的数据。源设备启动接续时应保存数据，目标设备接续时需准确恢复数据，以确保进度的连续性与设备间数据的一致性。本章节将介绍如何配置应用以使用接续能力，以及如何保存和恢复数据以实现应用的无缝接续。具体开发流程如下：

1. 启用接续

   在module.json5文件的abilities中，需将continuable标签配置为"true"，以表示该UIAbility可被迁移。该配置默认值为"false"，未配置或显式配置为"false"的UIAbility将被系统识别为不可迁移。

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           // ...
           "continuable": true
         }
       ],
       // ...
     }
   }
   ```
2. 源端保存迁移数据

   当对端点击接续图标时，源端将触发UIAbility中的[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口。在此接口中，开发者可将需要迁移的数据以键值对形式保存至wantParam中，并返回AbilityConstant.OnContinueResult.AGREE，标识应用同意迁移，从而将数据迁移至对端。

   ```typescript
   async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
     // 1.1 Retrieve the data to be connected and transmit it via wantParam.
     let continueIndex = AppStorage.get('continueIndex') as number;
     wantParam.continueIndex = continueIndex;
     let currentOffset = AppStorage.get('currentOffset') as number;
     wantParam.currentOffset = currentOffset;
     let continueHeight = AppStorage.get('listItemHeight') as number;
     wantParam.continueHeight = continueHeight;
     let currentTime = AppStorage.get('currentTime') as number;
     wantParam.continueTime = currentTime;
     let videoIndex = AppStorage.get('videoIndex') as number;
     wantParam.continueItem = videoIndex;
     let flag = AppStorage.get('flag') as boolean;
     wantParam.flag = flag;
     let url = AppStorage.get('pageUrl') as string;
     wantParam.pageUrl = url;
     let distance = AppStorage.get('scrollDistance') as number;
     wantParam.scrollDistance = distance;
     let breakpoint = AppStorage.get(BreakpointConstants.BREAKPOINT_NAME) as string;
     wantParam.breakpoint = breakpoint;
     let pageInfos = AppStorage.get('pageInfos') as NavPathStack;
     let pageArr = pageInfos.getAllPathName();
     let currentPage = '';
     if (pageArr.length > 0) {
       currentPage = pageArr[pageArr.length - 1];
     }
     AppStorage.setOrCreate('continue', false);
     wantParam.currentPage = currentPage;

     return AbilityConstant.OnContinueResult.AGREE;
   }
   ```
3. 对端恢复数据

   在源端保存数据并同意迁移后，对端可启动应用，开发者可在UIAbility中的[onCreate()](../harmonyos-guides/uiability-lifecycle.md#oncreate)或[onNewWant()](../harmonyos-guides/uiability-lifecycle.md#onnewwant)生命周期回调中恢复数据。如果Ability的启动原因为LaunchReason.CONTINUATION，可从want.parameters中获取保存的键值对数据。

   ```typescript
   onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     GlobalContext.getContext().setObject('abilityWant', want);
     GlobalContext.getContext().setObject('context', this.context);
     if (want.parameters) {
       if (want.parameters.currentTime) {
         GlobalContext.getContext().setObject('currentTime', want.parameters.currentTime);
       }
     }
     try {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
     } catch (e) {
       hilog.error(0x000, 'progress', `setColorMode error ${JSON.stringify(e)}`);
     }
     if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
       if (want.parameters) {
         this.continueRestore(want);
       }
     }
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   }
   ```

   可将恢复数据的方法提取为公共方法，以便在UIAbility的onCreate()或onNewWant()中调用。

   ```typescript
   continueRestore(want: Want) {
     if (!want.parameters) {
       hilog.error(0x0000, 'EntryAbility', 'missing sessionId');
       return;
     }
     let currentPage = want.parameters.currentPage as string;
     AppStorage.setOrCreate('currentPage', currentPage);
     want.parameters.continueIndex && AppStorage.setOrCreate('continueWaterOffset', want.parameters.continueIndex);
     want.parameters.currentOffset && AppStorage.setOrCreate('continueOffset', want.parameters.currentOffset);
     want.parameters.continueHeight && AppStorage.setOrCreate('continueHeight', want.parameters.continueHeight);
     AppStorage.setOrCreate('continueEntry', true);
     AppStorage.setOrCreate('setCurrentOffset', true);
     want.parameters.continueTime && AppStorage.setOrCreate('currentTime', want.parameters.continueTime);
     want.parameters.continueItem && AppStorage.setOrCreate('videoIndex', want.parameters.continueItem);
     want.parameters.continueItem && AppStorage.setOrCreate('videoSelect', want.parameters.continueItem);
     want.parameters.flag && AppStorage.setOrCreate('flag', want.parameters.flag);
     AppStorage.setOrCreate('continue', true);
     AppStorage.setOrCreate('continueRestore', true);
     want.parameters.pageUrl && AppStorage.setOrCreate('pageUrl', want.parameters.pageUrl);
     want.parameters.scrollDistance && AppStorage.setOrCreate('scrollDistance', want.parameters.scrollDistance);
     want.parameters.breakpoint && AppStorage.setOrCreate('continueBreakpoint', want.parameters.breakpoint);

     try {
       this.context.restoreWindowStage(new LocalStorage());
     } catch (e) {
       hilog.error(0x000, 'progress', `restoreWindowStage error ${JSON.stringify(e)}`);
     }
   }
   ```

## 长列表进度接续

### 场景描述

在社交媒体、新闻资讯等应用中，用户经常需要浏览长列表内容。当用户滚动到列表的某个位置后，可能会切换设备，且切换后希望自动恢复到之前的滚动位置，避免重复操作。开发者可以利用接续能力提升此类场景的用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/aIukZAtQTGyop4ZVBBf4kw/zh-cn_image_0000002591568722.gif "点击放大")

### 实现原理

长列表通常用于存储大量信息，可以通过List、Grid、Scroll、WaterFlow等组件进行封装。系统提供了分布式迁移标识，以便在使用这些组件时恢复进度状态。这种方式调用便捷，使用示例如下：

```typescript
WaterFlow({ footer: this.footStyle, scroller: this.waterFlowScroller }) {
  // ...
}
.restoreId(1)
```

然而，该方法存在局限性，具体支持的场景和版本详见[分布式迁移标识](../harmonyos-references/ts-universal-attributes-restoreid.md)的说明。若需在开发中进行更多自定义设置以提升用户体验，可参考以下步骤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/OWpwUiFHREGKbPVcjXq2bQ/zh-cn_image_0000002622128325.jpg "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 在Scroll组件的[onDidScroll()](../harmonyos-references/ts-container-scroll.md#ondidscroll12)接口中监听长列表的浏览进度变化。

   ```typescript
   Scroll(this.scroller) {
     // ...
   .onDidScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
     if (!this.setCurrentOffset) {
       this.currentOffset = this.scroller.currentOffset().yOffset;
     }
   })
   ```
3. 在UIAbility的onContinue()回调中，将进度相关数据保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在[onDidBuild()](../harmonyos-references/ts-custom-component-new-lifecycle.md#ondidbuild)事件中恢复浏览状态。

   ```typescript
   onDidBuild(): void {
     hilog.info(0x000, 'progress', `onDidBuild ${this.setCurrentOffset} ${this.continueOffset}`);
     if (this.setCurrentOffset) {
       this.scroller.scrollTo({ xOffset: 0, yOffset: this.continueOffset });
       this.setCurrentOffset = false;
     }
   }
   ```

## 媒体播放进度接续

### 场景描述

在视频播放场景中，用户可能会在观看视频的过程中切换至其他设备，例如从手机切换到平板/PC等大屏设备。用户切换设备后期望能从之前的播放位置继续观看而非重新开始播放。针对此类场景，开发者可以通过接续功能提升用户观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eLrDxrEsRyyIyhHKqPS1QQ/zh-cn_image_0000002591728656.gif "点击放大")

### 实现原理

媒体播放接续的内容主要包括播放列表中的集数、播放状态和进度。此外，还可以接续其他播放设置，以进一步提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/PgBJAzeDQk-xhMBUxceCdQ/zh-cn_image_0000002622048215.jpg "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用avPlayer.on('timeUpdate')接口来监听媒体播放进度的变化。

   ```typescript
   this.avPlayer.on('timeUpdate', (time: number) => {
     if (this.isSliderAction) {
       return;
     }
     this.currentTime = time;
     AppStorage.set('currentTime', this.currentTime)
   });
   ```
3. 在UIAbility的onContinue()回调中，将当前播放时间this.time保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility中的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在avPlayer初始化完成后，判断当前为接续状态，调用封装的调整视频进度方法videoSeek()，恢复至接续前的播放状态。

   ```typescript
   if (this.continue) {
     this.videoSeek(continueTime);
     this.continue = false;
     AppStorage.set('continue', false);
   }
   ```

## Web浏览进度接续

### 场景描述

在Web网页浏览场景中，用户可能会在浏览网页的过程中切换至其他设备。用户切换后期望能恢复到之前的网页URL和滚动位置，以保持浏览上下文的连续性。针对此类场景，开发者可以利用接续功能，进一步提升用户的浏览体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Iq7-U7VvRFmjhxMJ0arFww/zh-cn_image_0000002591568746.gif "点击放大")

### 实现原理

系统提供的Web组件用于在应用程序中展示Web页面内容。当Web组件加载大量信息时，保持浏览进度的连续性尤为重要。为了实现内容的连续展示，需要像处理长列表一样，通过传递当前的滚动位置来维持这一连续性。这可以通过使用[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)接口来获取和恢复滚动位置来实现。具体步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sE3W7Z-KRIeuWKYQmZZh6Q/zh-cn_image_0000002622128349.jpg "点击放大")

### 开发步骤

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用onTouch()事件监听屏幕滑动，并通过runJavaScript()接口获取页面滚动条距离顶部的距离。
3. 在onContinue()回调中，将this.scrollDistance保存到wantParam中，参考[源端保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[对端恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在onPageEnd()回调中调用runJavaScript()接口以恢复进度。

   ```typescript
   Web({ src: this.pageUrl, controller: this.controller })
   // ...
     .onPageEnd(async () => {
       // ...
       if (this.pageUrl.includes('product_list') && this.continueRestore) {
         this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop = ' +
         this.scrollDistance);
       }
       this.pageUrl = this.controller.getUrl();
       let result =
         await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
       this.scrollDistance = Number(result);
     })
     // ...
     .onTouch(async (event: TouchEvent) => {
       if (event.type === TouchType.Up) {
         if (this.pageUrl.includes('product_list')) {
           let result =
             await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
           this.scrollDistance = Number(result);
         }
       }
     })
   ```

## 示例代码

* [实现浏览进度接续功能](https://gitcode.com/harmonyos_samples/continue-progress)
