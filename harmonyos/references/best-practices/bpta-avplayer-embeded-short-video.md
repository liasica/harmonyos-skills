---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-embeded-short-video
title: 基于AVPlayer播放嵌入式短视频实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AVPlayer播放视频系列开发实践 > 基于AVPlayer播放嵌入式短视频实践
category: best-practices
scraped_at: 2026-04-29T14:11:21+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:62d64c937cc0905c9c0fa8b7f9832f7b53ea4c307ed014f40e2e87cae5b63858
---

## 概述

本文适用于视频播放类应用开发，针对市场上主流视频播放应用常见场景，介绍如何基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)系统播放器实现嵌入式短视频播放。本文指导开发者实现以下几种场景：

* [基础播控能力](bpta-avplayer-embeded-short-video.md#section19871518619)
* [焦点管理](bpta-avplayer-embeded-short-video.md#section9451174918313)
* [前后台感知](bpta-avplayer-embeded-short-video.md#section1560144415411)
* [横竖屏切换和旋转感知](bpta-avplayer-embeded-short-video.md#section92411245940)
* [画中画播放](bpta-avplayer-embeded-short-video.md#section17471045441)
* [视频首帧显示](bpta-avplayer-embeded-short-video.md#section11121172718716)
* [嵌入式视频列表自动播放](bpta-avplayer-embeded-short-video.md#section1243616221447)
* [视频无缝转场播放](bpta-avplayer-embeded-short-video.md#section129361938786)

## 基础播控能力

通过[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现视频资源加载、播放、暂停、停止、退出操作，包含了静音播放、倍数设置和字幕挂载等功能，实现原理详情可参考[《基于AVPlayer基础播控实践》](bpta-avplayer-basic-control.md)。

## 焦点管理

### 场景描述

前台视频播放过程中，音频被后台闹钟、电话等中断事件打断，完成播放过程音视频焦点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Zc4VLJL5Qe-VmJz2WxnkKw/zh-cn_image_0000002485843225.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=5D1EA106F88D467AE4E5F4207977B593B4F58288E5AC38C074BE1503E8A8E03E "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[焦点管理开发步骤](bpta-avplayer-long-video.md#section1716082163419)。

## 前后台感知

### 场景描述

应用从后台切回到前台时，保持原视频播放且会从之前的位置继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/gbcfU-6iQoGJdRFh53NOBQ/zh-cn_image_0000002485723289.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=0EFE73D10169B999A2A2AC3573B8EFF6D0F44ADABFD7C78C96403AFA4C439EBE "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[前后台感知开发步骤](bpta-avplayer-long-video.md#section1448773335411)。

## 横竖屏切换和旋转感知

### 场景描述

播放视频时可以手动进行横竖屏切换，也支持根据设备旋转方向自动切换横竖屏模式，以适应不同屏幕方向下的视频播放需求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/VT4s5mugSSa3hY5GDaJrIg/zh-cn_image_0000002452803500.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=250756D186F49103464192BB6E2373B2362E7D28956441B5D00C6DCC47748448 "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[横竖屏切换和旋转感知开发步骤](bpta-avplayer-long-video.md#section1257185216407)。

## 画中画播放

### 场景描述

画中画模式用户可进行其他界面操作，提升使用体验。应用场景包括视频播放、直播、视频通话和视频会议等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/yQPhyR_rQKysnd0Gl_egOQ/zh-cn_image_0000002452643884.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=1971ABA5E3CAB949D34C4026C50210B95BA194ABA5C8B7612B55F17C86ABE796 "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[画中画播放开发步骤](bpta-avplayer-long-video.md#section4691194231313)。

## 视频首帧显示

### 场景描述

视频播放列表或播放窗口中显示视频首帧作为视频描述信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/bXHR3AWASfS9jVIXrJi52Q/zh-cn_image_0000002485843233.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=50AD7698AEACD84A4E5D1568F75F1FCAF1009186FA85F6826C1D4AC8B6746AF8 "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[视频首帧显示开发步骤](bpta-avplayer-long-video.md#section27212108403)。

## 嵌入式视频列表自动播放

### 场景描述

用户浏览视频列表时自动播放视频，在用户滑动视频列表时自动切换至首个完全可见的视频播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/jdZvQpK-RUSPGRgD08EryQ/zh-cn_image_0000002485723317.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=F255150349A3879B8ECDAEF1346041BCE4366A9F9CEA24CDD8776DB048A82498 "点击放大")

### 实现原理

使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)组件实现视频播放列表页面。通过监听列表滑动[onScrollStop()](../harmonyos-references/ts-container-list.md#onscrollstop)事件，在滑动停止时获取滑动偏移量offset，计算首个可完全展示的视频的索引，切换至该视频播放，实现视频列表中首个可见视频自动播放效果。

逻辑如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/S3Zsn0qsSkmyeDmOvulGsg/zh-cn_image_0000002455462614.png?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=CB4B5AC0E3CC82E625AD15F38D43B7CF069F3DA877570585B3A1923EA67539BB "点击放大")

### 开发步骤

1. 创建视频列表的模拟数据。

   ```
   1. export const VIDEO_DATA: VideoItemData[] =
   2. [
   3. new VideoItemData($r('app.string.info_detail'), 0, '1.mp4', $r(`app.media.preview1`)),
   4. new VideoItemData($r('app.string.info_detail'), 0, '2.mp4', $r(`app.media.preview2`)),
   5. new VideoItemData($r('app.string.info_detail'), 0, '3.mp4', $r(`app.media.preview3`)),
   6. // ...
   7. ];
   ```

   [VideoItemData.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/model/VideoItemData.ets#L19-L36)

2. 声明initAVPlayer()方法初始化[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. // Creates the avPlayer instance object.
   5. this.avPlayer = await media.createAVPlayer();
   6. // Creates a callback function for state machine changes.
   7. this.setAVPlayerCallback();
   8. // ...
   9. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L50-L124)
3. 创建setStateChangeCallback()状态回调函数，[AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)状态为prepared时，使用[emitter.emit()](../harmonyos-references/js-apis-emitter.md#emitteremit)传递当前[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例的高度和宽度。

   ```
   1. private setStateChangeCallback() {
   2. // ...
   3. // Callback function for state machine changes
   4. this.avPlayer.on('stateChange', async (state) => {
   5. // ...
   6. switch (state) {
   7. // ...
   8. case 'prepared': // This state machine is reported after the prepare interface is successfully invoked.
   9. // ...
   10. let eventData: emitter.EventData = {
   11. data: {
   12. 'percent': this.avPlayer.width / this.avPlayer.height
   13. }
   14. };
   15. emitter.emit(CommonConstants.AVPLAYER_PREPARED, eventData);
   16. // ...
   17. break;
   18. // ...
   19. }
   20. });
   21. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L268-L386)
4. 使用[getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取当前屏幕宽度，以默认16:9的屏幕比例，通过屏幕宽度计算[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)组件的高度和宽度，计算[ListItem](../harmonyos-references/ts-container-listitem.md)所需高度；订阅[AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)状态为prepared的事件，获取[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例的高度和宽度。

   ```
   1. aboutToAppear() {
   2. try {
   3. this.windowClass.setWindowSystemBarProperties({
   4. // Status bar color
   5. statusBarColor: '#1A1A1A'
   6. }).catch((error: BusinessError) => {
   7. hilog.error(Constants.DOMAIN, TAG,
   8. `setWindowSystemBarProperties failed, Code:${error.code}, message:${error.message}`);
   9. });

   11. // Calculated based on screen width RelativeContainer width
   12. let winWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
   13. this.frameWidth = winWidth - Constants.LIST_ITEM_LEFT_PADDING - Constants.LIST_ITEM_RIGHT_PADDING;
   14. this.frameHeight = Math.floor(this.frameWidth / Constants.WH_RADIO);
   15. this.listItemHeight =
   16. this.frameHeight + Constants.TITLE_HEIGHT + Constants.LIST_ITEM_TOP_PADDING + Constants.INFO_AREA_HEIGHT;
   17. emitter.on('prepared', (eventData: emitter.EventData) => {
   18. let vWidth: number = eventData.data!.width;
   19. let vHeight: number = eventData.data!.height;
   20. let surfaceID: string = eventData.data!.surfaceID;
   21. if (this.playIdx < this.dataSource.totalCount()) {
   22. let playSurfaceID = this.dataSource.getData(this.playIdx).surfaceID;
   23. if (playSurfaceID === surfaceID) {
   24. this.setXComponentWH(vWidth, vHeight);
   25. }
   26. }
   27. });
   28. } catch (error) {
   29. if (error.code !== null && error.message !== null) {
   30. hilog.error(Constants.DOMAIN, TAG, `aboutToAppear failed, code is ${error.code}, message is ${error.message}`);
   31. }
   32. }
   33. }
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L341-L374)
5. 根据[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例的高度、宽度计算设置[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的高度、宽度。

   ```
   1. /*
   2. * Calculate XComponent Width&Height
   3. */
   4. setXComponentWH(vWidth: number, vHeight: number) {
   5. let radio = vWidth / vHeight;
   6. if (radio > 1) {
   7. // Horizontal video
   8. this.xWidth = this.frameWidth;
   9. this.xHeight = Math.floor(this.xWidth / radio);
   10. if (this.xHeight > this.frameHeight) {
   11. this.xHeight = this.frameHeight;
   12. this.xWidth = Math.floor(this.xHeight * radio);
   13. }
   14. } else {
   15. // Vertical video
   16. this.xHeight = this.frameHeight;
   17. this.xWidth = Math.floor(this.xHeight * radio);
   18. if (this.xWidth > this.frameWidth) {
   19. this.xWidth = this.frameWidth;
   20. this.xHeight = Math.floor(this.xWidth / radio);
   21. }
   22. }
   23. }
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L58-L81)
6. 声明avPlayerController的实例。

   ```
   1. private avPlayerController: AvPlayerController = new AvPlayerController();
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L54-L55)
7. 在页面的[onDidBuild()](../harmonyos-references/ts-custom-component-lifecycle.md#ondidbuild12)函数中加载模拟视频数据，初始化加载首个视频数据。

   ```
   1. onDidBuild(): void {
   2. this.dataSource.loadData();
   3. this.play(this.playIdx);
   4. }
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L333-L337)
8. 根据所需播放视频的索引，获取视频相关信息，使用videoReset()方法重置[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例，随后利用获取的视频信息调用[initAVPlayer()](bpta-avplayer-embeded-short-video.md#li71231589325)方法重新初始化，设置该实例的surfaceId，确保其在指定surfaceId的组件上播放。

   ```
   1. play(index: number) {
   2. this.startRender = false;
   3. // Reset AVPlayer
   4. this.avPlayerController.videoReset().then(() => {
   5. // ...
   6. this.isMuted = true;
   7. // Init AVPlayer
   8. this.avPlayerController.initAVPlayer({
   9. type: VideoDataType.RAW_FILE,
   10. videoSrc: this.dataSource.getData(index).src!,
   11. name: $r("app.string.app_name"),
   12. description: '',
   13. caption: '',
   14. index: 0,
   15. seekTime: stopTime,
   16. isMuted: true,
   17. head: $r("app.media.preview1")
   18. }, surfaceID);
   19. // ...
   20. });
   21. }
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L99-L137)
9. 用[List](../harmonyos-references/ts-container-list.md)显示视频列表，使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)对列表数据进行懒加载。

   ```
   1. List({ scroller: this.listScroller }) {
   2. LazyForEach(this.dataSource, (info: VideoInfo, index: number) => {
   3. ListItem() {
   4. this.videoItemBuilder(info, index)
   5. }
   6. // ...
   7. }, (info: VideoInfo) => info.id)
   8. }
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L384-L415)
10. 创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件，其提供用于图形绘制和媒体数据写入的Surface，负责将其嵌入视图中，用于视频播放。

    ```
    1. XComponent({
    2. type: XComponentType.SURFACE,
    3. controller: info.xController
    4. })
    ```

    [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L215-L218)
11. 在[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件的[onLoad()](../harmonyos-references/ts-basic-components-xcomponent.md#onload)加载事件中，使用[getXComponentSurfaceId()](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)获取该播放组件的Id，将其Id设置到[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)的surfaceId上，即可实现在该组件上播放视频。

    ```
    1. .onLoad(() => {
    2. let surfaceID = info.xController!.getXComponentSurfaceId();
    3. info.surfaceID = surfaceID;
    4. if (info.id === this.unloadID) {
    5. this.play(index);
    6. }
    7. })
    ```

    [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L229-L235)
12. 设置[List](../harmonyos-references/ts-container-list.md)的[onScrollStop()](../harmonyos-references/ts-container-list.md#onscrollstop)事件，在列表滑动停止时触发，根据滑动偏移量及单个[ListItem](../harmonyos-references/ts-container-listitem.md)的高度计算当前屏幕内首个可完整显示的视频索引。若计算得出的视频索引与当前播放视频索引不符，则使用play()方法重新初始化[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)，切换至计算得出的视频进行播放。

    ```
    1. .onScrollStop(() => {
    2. let yOffset = this.listScroller.currentOffset().yOffset;
    3. let curIndex = Math.floor(yOffset / (this.listItemHeight + Constants.LIST_DIVIDER_WIDTH));
    4. let offsetInItem = yOffset - curIndex * (this.listItemHeight + Constants.LIST_DIVIDER_WIDTH);
    5. if (offsetInItem > Constants.LIST_ITEM_TOP_PADDING + 34) {
    6. curIndex += 1;
    7. }
    8. this.curIndex = curIndex;
    9. if (curIndex !== this.playIdx && curIndex < this.dataSource.totalCount()) {
    10. setTimeout(() => {
    11. if (this.curIndex === curIndex && this.curIndex !== this.playIdx) {
    12. this.play(curIndex);
    13. }
    14. }, Constants.DELAY_MS);
    15. }
    16. })
    ```

    [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L435-L451)

## 视频无缝转场播放

### 场景描述

视频播放无缝转场是影音娱乐类应用中的典型场景之一，如视频列表中自动播放的热门视频，点击当前播放视频跳转至视频详情页后继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/YqSV-4ZqQaeoy1QKPDbvag/zh-cn_image_0000002452643900.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=44C50EEE873B627CA1D97F6FFFBDB2E0F553C7578210D619057CA85C10076D19 "点击放大")

### 实现原理

基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)实现视频播放，通过切换AVPlayer的surfaceId控制不同XComponent播放视频，实现转场效果，使用[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)方法跳转至指定位置播放，主要分为两部分：

**列表页面跳转到详情页面**：当点击正在播放的视频时，记录当前播放视频的索引、播放进度、总时长、surfaceId信息，并在页面跳转[pushPathByName()](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)方法中传入此视频信息。在视频播放详情页面使用[getParamByIndex()](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)接收传入信息，根据接收的视频信息使用initAVPlayer()初始化AVPlayer实例，初始化新的XComponent组件和surfaceID，将其绑定到AVPlayer上，使用seek()方法从记录的播放进度开始播放；

**详情页面返回到列表页面**：在详情页面点击返回时，记录当前播放视频的索引、播放进度、总时长、原surfaceId信息，并在页面回调[onBackPressed()](../harmonyos-references/js-apis-app-ability-uiability.md#onbackpressed10)函数中，使用[pop()](../harmonyos-references/ohos-arkui-advanced-multinavigation.md#pop)方法传入此视频信息，根据接收的视频信息，使用play(index)初始化AVPlayer，将其surfaceId设置为原surfaceId，使用seek()方法从记录的播放进度开始播放。

逻辑如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/ih8ZYW_OQOezrp-3tzqhQg/zh-cn_image_0000002485843257.png?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=134E06168969E9A51F9886BACE7B6E8567BE474D26DB5FFA728DD18A0437F019 "点击放大")

### 开发步骤

1. 创建route\_map.json路由配置文件，配置视频跳转播放页面参数信息。

   ```
   1. {
   2. "routerMap": [
   3. {
   4. "name": "DetailPage",
   5. "pageSourceFile": "src/main/ets/pages/DetailPage.ets",
   6. "buildFunction": "detailPageBuilder"
   7. }
   8. ]
   9. }
   ```

   [route\_map.json](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/resources/base/profile/route_map.json#L0-L9)
2. 创建AppRouter.ets文件，声明页面路由相关操作方法。

   ```
   1. public getPathStack(): NavPathStack {
   2. return this.pathStack;
   3. }
   ```

   [AppRouter.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/common/utils/AppRouter.ets#L33-L36)
3. 在首页的[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件中使用[getPathStack()](../harmonyos-references/ts-basic-components-navigation.md#getpathstack19)获取页面路由信息。

   ```
   1. build() {
   2. Navigation(AppRouter.getInstance().getPathStack()) {
   3. // ...
   4. }
   5. .hideTitleBar(true)
   6. .width('100%')
   7. .height('100%')
   8. .mode(NavigationMode.Stack)
   9. }
   ```

   [PlayVideo.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/pages/PlayVideo.ets#L33-L50)
4. 在[pushPathByName()](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)基础上封装pushByName()方法，用于页面跳转时的参数传递。

   ```
   1. public static pushByName(name: string, param: Object, onPop: Callback<PopInfo>): void {
   2. AppRouter.instance.pushPathByName(name, param, onPop);
   3. }
   ```

   [AppRouter.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/common/utils/AppRouter.ets#L54-L57)
5. 设置[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)的点击事件，当用户点击当前播放的视频时，保存当前播放进度，然后使用[pushByName()](bpta-avplayer-embeded-short-video.md#li1647811562593)方法，在页面跳转的同时将当前播放视频相关信息传递到视频详情页面。

   ```
   1. .onClick(() => {
   2. // Save video data
   3. AppStorage.setOrCreate(Constants.SURFACE_ID_KEY, info.surfaceID);
   4. this.avPlayerController.videoPause();

   6. info.stopTime = this.avPlayerController.currentTime;
   7. info.duration = this.avPlayerController.duration;
   8. // Jump video play detail
   9. AppRouter.pushByName(Constants.DETAIL_PAGE_NAME,
   10. new VideoParams(info, this.playIdx, index), () => {
   11. let param: VideoParams = AppStorage.get("BackParam") as VideoParams;
   12. let _index = param.index;
   13. this.dataSource.getData(_index).stopTime = param.videoInfo.stopTime;
   14. this.play(param.playIdx);
   15. })
   16. })
   ```

   [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L241-L256)
6. 基于[getParamByIndex()](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)封装getLastParams()方法，用于页面跳转后获取传递的参数。

   ```
   1. public static getLastParams(): Object {
   2. return AppRouter.instance.pathStack.getParamByIndex(AppRouter.instance.pathStack.size() - 1) as Object;
   3. }
   ```

   [AppRouter.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/common/utils/AppRouter.ets#L78-L81)
7. 在视频详情页面的[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)事件中，使用[getLastParams()](bpta-avplayer-embeded-short-video.md#li1482553124015)方法获取传递的参数信息，取消[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例的静音设置。

   ```
   1. aboutToAppear(): void {
   2. try {
   3. this.mainWin = this.windowStage.getMainWindowSync();
   4. this.windowClass = this.context.windowStage.getMainWindowSync();
   5. } catch (error) {
   6. let err = error as BusinessError;
   7. hilog.error(Constants.DOMAIN, TAG, `getMainWindowSync error, code: ${err.code};message: ${err.message};`);
   8. }

   11. this.setOrientation();
   12. // ...

   14. // Get params
   15. let params = AppRouter.getLastParams() as VideoParams;
   16. this.info = params.videoInfo;
   17. this.playIdx = params.playIdx;
   18. this.index = params.index;
   19. this.src = params.videoInfo.src as string;
   20. this.currentTime = this.info.stopTime as number;
   21. this.duration = this.info.duration;
   22. this.avPlayerController.videoMuted(false);
   23. // ...
   24. }
   ```

   [VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoDetail.ets#L568-L642)
8. 在视频详情页面创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent19)组件。

   ```
   1. XComponent({
   2. type: XComponentType.SURFACE,
   3. controller: this.xComponentController
   4. })
   5. .id(`videoXComponent_${this.info?.id}`)
   ```

   [VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoDetail.ets#L653-L657)
9. [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent19)的[onLoad()](../harmonyos-references/ts-basic-components-xcomponent.md#onload)事件中重新初始化[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实例，将跳转时的播放时间进度currentTime传递给[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)，然后使用[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)跳转到currentTime时间帧继续播放。

   ```
   1. .onLoad(() => {
   2. // Init AVPlayer
   3. this.surfaceId = this.xComponentController.getXComponentSurfaceId();
   4. if (this.avPlayerController !== undefined) {
   5. this.avPlayerController.initAVPlayer({
   6. type: VideoDataType.RAW_FILE,
   7. videoSrc: this.src,
   8. name: $r("app.string.app_name"),
   9. description: '',
   10. caption: 'captions.srt',
   11. index: 0,
   12. seekTime: this.currentTime,
   13. head: $r("app.media.preview1")
   14. }, this.surfaceId);
   15. }
   16. })
   ```

   [VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoDetail.ets#L663-L678)
10. 声明handleBackAction()方法，当在详情页面点击返回按钮时，记录当前播放视频的信息，包括视频当前进度、总时长、索引等。

    ```
    1. handleBackAction() {
    2. if (this.isLayoutFullScreen) {
    3. // Cancel full screen
    4. this.isLayoutFullScreen = false;
    5. this.setWindowDirection(window.Orientation.PORTRAIT);
    6. }

    8. this.isPIPShow = false;
    9. this.windowClass?.setWindowSystemBarProperties({
    10. // Status bar color
    11. statusBarColor: '#1A1A1A'
    12. }).catch((error: BusinessError) => {
    13. hilog.error(Constants.DOMAIN, TAG,
    14. `setWindowSystemBarProperties: Failed. code: ${error.code} ;message: ${error.message}`);
    15. });

    17. this.avPlayerController.videoPause();
    18. this.isPlaying = false;
    19. // Save params
    20. if (this.info !== undefined) {
    21. this.info.stopTime = this.avPlayerController.currentTime;
    22. }
    23. let param: VideoParams = new VideoParams(
    24. this.info as VideoInfo,
    25. this.playIdx,
    26. this.index
    27. )
    28. AppStorage.setOrCreate("BackParam", param);
    29. AppRouter.popWithParam(Object({ result: true }));
    30. }
    ```

    [VideoDetail.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoDetail.ets#L194-L224)
11. 在视频列表页面的点击跳转事件[pushByName()](bpta-avplayer-embeded-short-video.md#li1647811562593)方法中，使用回调函数接收详情页面返回参数信息，随后调用[play()](bpta-avplayer-embeded-short-video.md#li37514173917)方法，设置[seekTime](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)为currentTime以继续播放。

    ```
    1. .onClick(() => {
    2. // Save video data
    3. AppStorage.setOrCreate(Constants.SURFACE_ID_KEY, info.surfaceID);
    4. this.avPlayerController.videoPause();

    6. info.stopTime = this.avPlayerController.currentTime;
    7. info.duration = this.avPlayerController.duration;
    8. // Jump video play detail
    9. AppRouter.pushByName(Constants.DETAIL_PAGE_NAME,
    10. new VideoParams(info, this.playIdx, index), () => {
    11. let param: VideoParams = AppStorage.get("BackParam") as VideoParams;
    12. let _index = param.index;
    13. this.dataSource.getData(_index).stopTime = param.videoInfo.stopTime;
    14. this.play(param.playIdx);
    15. })
    16. })
    ```

    [VideoList.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-embeded-short-video/blob/master/entry/src/main/ets/component/VideoList.ets#L241-L256)

## 示例代码

* [基于AVPlayer实现嵌入式短视频播放](https://gitcode.com/harmonyos_samples/avplayer-embeded-short-video/tree/master/)
