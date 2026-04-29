---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-continue-progess
title: 常见接续最佳实践
breadcrumb: 最佳实践 > 自由流转 > 跨端迁移 > 常见接续最佳实践
category: best-practices
scraped_at: 2026-04-29T14:12:45+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:9e585b185c6c3295d737a5df3e28d5222f53d62fabd890d2dabed2cb45640c7d
---

## 概述

在日常生活中，随着个人设备数量的不断增加，用户在使用某个应用时，如果有更合适的设备在附近，可以利用接续功能将应用无缝切换到新设备上继续当前操作。本文主要针对长列表进度、媒体播放进度和Web浏览进度三个场景，实现了浏览进度的高效接续，提供给用户一种无缝的设备切换体验和浏览连贯性保障，确保用户在切换设备时能够轻松恢复之前的浏览进度，极大地提升了使用的便捷性和连贯性，实现了真正的无缝接续。

* [长列表进度接续](bpta-application-continue-progess.md#section16702516134216)：可以让用户从上次离开的位置继续浏览，无需从头开始，精准定位到之前的条目附近，节省时间并减少操作成本，提升浏览体验。
* [媒体播放进度接续](bpta-application-continue-progess.md#section12439210434)：从源设备当前播放的位置继续播放视频，保持播放进度、画面质量和音频设置的一致性，确保用户的观影体验不被打断。支持在线视频平台的剧集、电影以及本地存储的视频文件，实现流畅的接续播放。
* [Web浏览进度接续](bpta-application-continue-progess.md#section3512987460)：能够快速定位到源设备浏览的网页位置，确保用户浏览的连续性，避免重复查找信息的不便，提高信息获取的效率。

## 实现原理

接续过程底层依赖分布式框架和软总线，开发者只需要启用接续、保存数据和恢复数据，具体运作机制可参考：[运作机制](bpta-continue-cast.md#section1218874218264)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ShQPNVfPTryPFIMGi4Q55A/zh-cn_image_0000002314661150.png?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=CCCF2CE7DDB0CD36D40183579492054743305E46528D5662E2B3CF11042A8305 "点击放大")

## 开发流程

进度接续的核心在于确保进度数据在不同设备间的精确传输与同步。在实际开发过程中，开发者会遇到各种复杂的接续需求，首要任务是深入分析哪些数据对接续控制至关重要。在源设备启动接续时，应保存数据；在目标设备接续时，需准确恢复数据，以确保进度的连续性和设备间数据的一致性。

本章节将介绍如何配置应用以使用接续能力，以及如何保存和恢复数据以实现应用的无缝接续。具体场景包括[长列表进度接续](bpta-application-continue-progess.md#section16702516134216)、[媒体播放进度接续](bpta-application-continue-progess.md#section12439210434)和[Web浏览进度接续](bpta-application-continue-progess.md#section3512987460)。

1. 启用接续

   在module.json5文件的abilities中，将continuable标签配置为“true”，表示该UIAbility可以被迁移。配置为“false”的UIAbility将被系统识别为不可迁移，且该配置的默认值为“false”。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "continuable": true
   8. }
   9. ],
   10. // ...
   11. }
   12. }
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/module.json5#L2-L83)
2. 源端保存迁移数据

   当对端点击接续图标时，源端将触发UIAbility中的[onContinue()](../harmonyos-references/js-apis-app-ability-uiability.md#oncontinue)接口。在此接口中，开发者可以将需要迁移的数据以键值对形式保存至wantParam中，并返回AbilityConstant.OnContinueResult.AGREE，标识应用同意迁移，从而将数据迁移至对端。

   ```
   1. async onContinue(wantParam: Record<string, Object>): Promise<AbilityConstant.OnContinueResult> {
   2. // 1.1 Retrieve the data to be connected and transmit it via wantParam.
   3. let continueIndex = AppStorage.get('continueIndex') as number;
   4. wantParam.continueIndex = continueIndex;
   5. let currentOffset = AppStorage.get('currentOffset') as number;
   6. wantParam.currentOffset = currentOffset;
   7. let continueHeight = AppStorage.get('listItemHeight') as number;
   8. wantParam.continueHeight = continueHeight;
   9. let currentTime = AppStorage.get('currentTime') as number;
   10. wantParam.continueTime = currentTime;
   11. let videoIndex = AppStorage.get('videoIndex') as number;
   12. wantParam.continueItem = videoIndex;
   13. let flag = AppStorage.get('flag') as boolean;
   14. wantParam.flag = flag;
   15. let url = AppStorage.get('pageUrl') as string;
   16. wantParam.pageUrl = url;
   17. let distance = AppStorage.get('scrollDistance') as number;
   18. wantParam.scrollDistance = distance;
   19. let breakpoint = AppStorage.get(BreakpointConstants.BREAKPOINT_NAME) as string;
   20. wantParam.breakpoint = breakpoint;
   21. let pageInfos = AppStorage.get('pageInfos') as NavPathStack;
   22. let pageArr = pageInfos.getAllPathName();
   23. let currentPage = '';
   24. if (pageArr.length > 0) {
   25. currentPage = pageArr[pageArr.length - 1];
   26. }
   27. AppStorage.setOrCreate('continue', false);
   28. wantParam.currentPage = currentPage;

   30. return AbilityConstant.OnContinueResult.AGREE;
   31. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L107-L138)
3. 对端恢复数据

   在源端保存数据并同意迁移后，对端可启动应用，并在UIAbility中的onCreate()或onNewWant()生命周期回调中恢复数据。如果Ability的启动原因为LaunchReason.CONTINUATION，开发者可以从want.parameters中获取保存的键值对数据。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. GlobalContext.getContext().setObject('abilityWant', want);
   3. GlobalContext.getContext().setObject('context', this.context);
   4. if (want.parameters) {
   5. if (want.parameters.currentTime) {
   6. GlobalContext.getContext().setObject('currentTime', want.parameters.currentTime);
   7. }
   8. }
   9. try {
   10. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
   11. } catch (e) {
   12. hilog.error(0x000, 'progress', `setColorMode error ${JSON.stringify(e)}`);
   13. }
   14. if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
   15. if (want.parameters) {
   16. this.continueRestore(want);
   17. }
   18. }
   19. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
   20. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L30-L50)

   可将恢复数据的方法提取为公共方法，以便于在UIAbility的onCreate()或onNewWant()中调用。

   ```
   1. continueRestore(want: Want) {
   2. if (!want.parameters) {
   3. hilog.error(0x0000, 'EntryAbility', 'missing sessionId');
   4. return;
   5. }
   6. let currentPage = want.parameters.currentPage as string;
   7. AppStorage.setOrCreate('currentPage', currentPage);
   8. want.parameters.continueIndex && AppStorage.setOrCreate('continueWaterOffset', want.parameters.continueIndex);
   9. want.parameters.currentOffset && AppStorage.setOrCreate('continueOffset', want.parameters.currentOffset);
   10. want.parameters.continueHeight && AppStorage.setOrCreate('continueHeight', want.parameters.continueHeight);
   11. AppStorage.setOrCreate('continueEntry', true);
   12. AppStorage.setOrCreate('setCurrentOffset', true);
   13. want.parameters.continueTime && AppStorage.setOrCreate('currentTime', want.parameters.continueTime);
   14. want.parameters.continueItem && AppStorage.setOrCreate('videoIndex', want.parameters.continueItem);
   15. want.parameters.continueItem && AppStorage.setOrCreate('videoSelect', want.parameters.continueItem);
   16. want.parameters.flag && AppStorage.setOrCreate('flag', want.parameters.flag);
   17. AppStorage.setOrCreate('continue', true);
   18. AppStorage.setOrCreate('continueRestore', true);
   19. want.parameters.pageUrl && AppStorage.setOrCreate('pageUrl', want.parameters.pageUrl);
   20. want.parameters.scrollDistance && AppStorage.setOrCreate('scrollDistance', want.parameters.scrollDistance);
   21. want.parameters.breakpoint && AppStorage.setOrCreate('continueBreakpoint', want.parameters.breakpoint);

   23. try {
   24. this.context.restoreWindowStage(new LocalStorage());
   25. } catch (e) {
   26. hilog.error(0x000, 'progress', `restoreWindowStage error ${JSON.stringify(e)}`);
   27. }
   28. }
   ```

   [EntryAbility.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L75-L103)

## 长列表进度接续

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/u_yGHy5vRmeK_nBS1QbmFw/zh-cn_image_0000002348739881.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=7C5627BC150E94BC308788494788FFC47E01DF533887384BE01FCA52E068ABCB "点击放大")

长列表通常用于存储大量信息，可以通过List、Grid、Scroll、WaterFlow等组件进行封装。系统提供了分布式迁移标识，以便在使用这些组件时恢复进度状态，调用起来非常方便。使用方法如下：

```
1. WaterFlow({ footer: this.footStyle, scroller: this.waterFlowScroller }) {
2. // ...
3. }
4. .restoreId(1)
```

[WaterFlowView.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/WaterFlowView.ets#L131-L217)

使用分布式迁移标识可以快速实现接续。然而，该方法存在局限性，具体支持的场景和版本详见[分布式迁移标识](../harmonyos-references/ts-universal-attributes-restoreid.md)的说明。若需在开发中进行更多自定义设置以提升用户体验，可参考以下步骤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/nTJ3Zlj2SyybCpYSVMiaDw/zh-cn_image_0000002439543518.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=FA5C77FA2C0E78982C344B616DE59EBF7D758236FDA901211EBC1B0C6D91617B "点击放大")

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 在Scroll组件的onDidScroll()接口中监听长列表的浏览进度变化。

   ```
   1. Scroll(this.scroller) {
   2. // ...
   3. .onDidScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
   4. if (!this.setCurrentOffset) {
   5. this.currentOffset = this.scroller.currentOffset().yOffset;
   6. }
   7. })
   ```

   [HomeContent.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/HomeContent.ets#L192-L223)
3. 在UIAbility的onContinue()回调中，将进度相关数据保存到wantParam中，参考[保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在onDidBuild()事件中恢复浏览状态。

   ```
   1. onDidBuild(): void {
   2. hilog.info(0x000, 'progress', `onDidBuild ${this.setCurrentOffset} ${this.continueOffset}`);
   3. if (this.setCurrentOffset) {
   4. this.scroller.scrollTo({ xOffset: 0, yOffset: this.continueOffset });
   5. this.setCurrentOffset = false;
   6. }
   7. }
   ```

   [HomeContent.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/view/longlist/HomeContent.ets#L107-L114)

## 媒体播放进度接续

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/LRdzsFxNRSKU3dSGSlwRHQ/zh-cn_image_0000002314820978.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=CC04824D03E29DB1303E550074D5032E0FE46A1E6EBD63CD167D25A6D1F82B27 "点击放大")

媒体播放接续的内容主要包括播放列表中的集数、播放状态和进度。此外，还可以接续其他播放设置，以进一步提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/EmBLsIwySP-8f9J4vIAtew/zh-cn_image_0000002472864265.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=223D02571BEDFBC65B20602574AAA428BB832179F6723234C8B3A46E79794FC2 "点击放大")

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用avPlayer.on('timeUpdate')接口来监听媒体播放进度的变化。

   ```
   1. this.avPlayer.on('timeUpdate', (time: number) => {
   2. if (this.isSliderAction) {
   3. return;
   4. }
   5. this.currentTime = time;
   6. AppStorage.set('currentTime', this.currentTime)
   7. });
   ```

   [AvPlayManager.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/viewmodel/video/AvPlayManager.ets#L182-L188)
3. 在UIAbility的onContinue()回调中，将当前播放时间this.time保存到wantParam中，参考[保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在UIAbility中的onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在avPlayer初始化完成后，判断当前为接续状态，调用封装的调整视频进度方法videoSeek()，恢复至接续前的播放状态。

   ```
   1. if (this.continue) {
   2. this.videoSeek(continueTime);
   3. this.continue = false;
   4. AppStorage.set('continue', false);
   5. }
   ```

   [AvPlayManager.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/viewmodel/video/AvPlayManager.ets#L135-L139)

## Web浏览进度接续

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/c2DmQ0iMSciNoSNTCi6vBQ/zh-cn_image_0000002348739889.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=8990D83D9C3DB1807739BFFE3F87DBEE1BC8912E82BF0CDC36F8CA8190219319 "点击放大")

系统提供的Web组件用于在应用程序中展示Web页面内容。当Web组件加载大量信息时，保持浏览进度的连续性尤为重要。为了实现内容的连续展示，需要像处理长列表一样，通过传递当前的滚动位置来维持这一连续性。这可以通过使用runJavaScript()接口来获取和恢复滚动位置来实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/3AvwtCeaTsKwn378p-teOA/zh-cn_image_0000002439705250.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=041CAB7F79A1A80D608006434D55CCBAF38E29C868AAAFA01280C05FD9CD263F "点击放大")

1. [启用接续](bpta-application-continue-progess.md#li6149192715494)。
2. 使用onTouch()事件监听屏幕滑动，并通过runJavaScript()接口获取页面滚动条距离顶部的距离。
3. 在onContinue()回调中，将this.scrollDistance保存到wantParam中，参考[保存迁移数据](bpta-application-continue-progess.md#li1745816354491)。
4. 在onNewWant()和onCreate()回调中，从want.parameters中恢复数据，参考[恢复数据](bpta-application-continue-progess.md#li631218439498)。
5. 在onPageEnd()回调中调用runJavaScript()接口以恢复进度。

   ```
   1. Web({ src: this.pageUrl, controller: this.controller })
   2. // ...
   3. .onPageEnd(async () => {
   4. // ...
   5. if (this.pageUrl.includes('product_list') && this.continueRestore) {
   6. this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop = ' +
   7. this.scrollDistance);
   8. }
   9. this.pageUrl = this.controller.getUrl();
   10. let result =
   11. await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
   12. this.scrollDistance = Number(result);
   13. })
   14. // ...
   15. .onTouch(async (event: TouchEvent) => {
   16. if (event.type === TouchType.Up) {
   17. if (this.pageUrl.includes('product_list')) {
   18. let result =
   19. await this.controller.runJavaScript('javascript:document.getElementById("productList").scrollTop');
   20. this.scrollDistance = Number(result);
   21. }
   22. }
   23. })
   ```

   [WebPageComponent.ets](https://gitcode.com/harmonyos_samples/continue-progress/blob/master/entry/src/main/ets/view/web/WebPageComponent.ets#L130-L175)

## 常见问题

## 打开任意可接续应用后，对端未显示接续图标

在打开系统浏览器、已有内容的备忘录笔记界面或新开发的应用界面后，对端均未出现接续图标，可以按照以下步骤进行排查：

1. 检查蓝牙是否已开启；
2. 检查接续功能是否已开启：设置->多设备协同->接续；
3. 检查是否已登录相同的华为账号；
4. 通过命令行检查组网是否成功；

   ```
   1. hidumper -s 4700 -a "buscenter -l remote_device_info"
   ```

   执行完成后，RemoteDeviceInfo中列出的设备即为已成功与当前设备组网的设备。如下图所示，该设备已与两台其他设备成功组网。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/29QfXuzzQeCeJ_sumhxlBA/zh-cn_image_0000002314820982.png?HW-CC-KV=V1&HW-CC-Date=20260429T061237Z&HW-CC-Expire=86400&HW-CC-Sign=CABD8678F95FE47EFDEEE694C6AA9121C0792EA0025CBDA3EA624C0465A67E39)

## 1分钟以上无任何操作，图标将自动消失；再次操作应用时，图标将重新出现

图标显隐是系统的一项特性。根据当前的策略，图标在源端最后一次触屏操作后的1分钟内保持显示。如果超过1分钟没有进行任何操作，图标将自动隐藏，以减少对用户的干扰。同样地，当锁屏时，图标将在10秒后自动消失，这也是系统正常运行的一部分。

## 打开新接入的应用后，对端不出现图标

仅当应用配置了continuable标签，并且处于获焦且可接续状态时，才会发送接续广播，使得对端显示接续图标。可以按照以下步骤排查：

1. 确认两端均已安装应用；
2. 检查应用是否已将continuable标签设置为true；
3. 确认应用是否已调用setMissionContinueState()接口将自身的迁移状态设置为false。

## 示例代码

* [实现浏览进度接续功能](https://gitcode.com/harmonyos_samples/continue-progress)
