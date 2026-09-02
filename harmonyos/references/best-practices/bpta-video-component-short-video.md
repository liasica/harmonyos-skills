---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-component-short-video
title: 基于Video组件播放短视频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于Video播放视频系列开发实践 > 基于Video组件播放短视频
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:64a9a4ce3a42b81cf4a9fed4e7010ead0c50044d0d9ede1c58c0a3406d33b84a
---

## 概述

短视频通常以移动智能终端为播放载体，通过社交或视频平台快速传播。本文围绕主流短视频应用的常见场景，包括基础播控、横竖屏切换与旋转感知、短视频列表流畅切换、长按视频倍速播放、前后台感知、音量设置、自动连播等，指导开发者基于[Video](../harmonyos-references/ts-media-components-video.md)组件实现短视频播放功能。

* [基础播控](bpta-video-component-short-video.md#section8262152281415)
* [横竖屏切换与旋转感知](bpta-video-component-short-video.md#section10921503198)
* [短视频列表流畅切换](bpta-video-component-short-video.md#section68130286511)
* [长按视频倍速播放](bpta-video-component-short-video.md#section107981344143717)
* [前后台感知](bpta-video-component-short-video.md#section7933653553)
* [音量设置](bpta-video-component-short-video.md#section1611719321814)
* [自动连播](bpta-video-component-short-video.md#section25891771761)

## 基础播控

### 场景描述

通过Video组件实现视频基础播放控制能力，包括播放视频、暂停播放等操作。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/PbF7y7OgRrGdIT0noSAZEw/zh-cn_image_0000002555239530.gif "点击放大")

### 实现原理

具体实现原理可参考《基于Video组件播放长视频》的基础播控[实现原理](bpta-video-component-long-video.md#section1669421012353)。

### 开发步骤

具体开发步骤可参考《基于Video组件播放长视频》的基础播控[开发步骤](bpta-video-component-long-video.md#section18477202813352)。

## 横竖屏切换与旋转感知

### 场景描述

当用户需要全屏播放视频时，可以通过点击按钮全屏播放，或通过旋转设备进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/DnynPApxQU-WKyG3sZkXPQ/zh-cn_image_0000002585679465.gif "点击放大")

### 实现原理

* 自动旋转：在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置"orientation"字段，设置[自动旋转方向类型](../harmonyos-guides/window-rotation.md#自动旋转方向类型)为AUTO\_ROTATION\_RESTRICTED，应用会跟随传感器自动旋转。

  **说明** 

  须提前打开设备的控制中心，取消旋转锁定，否则自动旋转不生效。
* 手动切换：通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置应用的主窗口显示方向[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：
  + USER\_ROTATION\_LANDSCAPE：旋转到横屏。
  + USER\_ROTATION\_PORTRAIT：旋转到竖屏。

### 开发步骤

开发步骤详情可参考《基于Video组件播放长视频》的横竖屏切换和旋转感知[开发步骤](bpta-video-component-long-video.md#section3703101910168)。

## 短视频列表流畅切换

### 场景描述

在用户上下滑动时，视频能快速切换到下一个或上一个，且加载和播放流畅、无卡顿。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/goEta1XYRgm1kxk5kWARiw/zh-cn_image_0000002555079910.gif "点击放大")

### 实现原理

设置[Swiper](../harmonyos-references/ts-container-swiper.md)组件的[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount15)属性预加载子组件个数，提前加载并缓存下一个视频内容，确保滑动时无卡顿，提升短视频切换的流畅性。

### 开发步骤

1. 设置Swiper组件预加载子组件个数cachedCount为1，预加载当前、上一个和下一个视频。

   ```typescript
   Swiper(this.swiperController) {
     LazyForEach(new MyDataSource(this.videoInfoList), (item: VideoDataModel, index: number) => {
       VideoPlayer({
         isFullLandscapeScreen: this.isFullLandscapeScreen, // fullLandscapeScreen state
         videoIndex: index, // Video index
         activeIndex: this.currentIndex, // Index of the currently playing video
         screenWidth: this.screenWidth // Screen width
       })
     }, (item: string) => item)
   }
   .cachedCount(CommonConstants.CACHED_COUNT)
   ```
2. 滑动切换视频时，同步更新当前视频的索引值currentIndex，具体步骤请参考自动连播[开发步骤](bpta-video-component-short-video.md#section6406358972)的2、3、4。

## 长按视频倍速播放

### 场景描述

通过长按屏幕实现视频2倍速播放。如下图所示，长按触屏时，显示"2.0X快进中"，同时视频以2倍速进行播放；抬起后，视频以默认的1倍速进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/2f_usip6RTmh5BUx3bhMNw/zh-cn_image_0000002585799527.gif "点击放大")

### 实现原理

绑定长按手势事件[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)，当用户长按视频边缘时，动态设置[VideoOptions对象说明](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)中的视频播放倍速currentProgressRate，从而实现视频倍速播放功能。

### 开发步骤

1. 绑定LongPressGesture长按手势事件，在[onAction()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onaction)方法中设置视频播放倍速值为2倍速，即PlaybackSpeed.Speed\_Forward\_2\_00\_X，在[onActionEnd()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onactionend)方法中，恢复初始播放速度为PlaybackSpeed.Speed\_Forward\_1\_00\_X。具体视频播放倍速选项请参考[PlaybackSpeed枚举说明](../harmonyos-references/ts-media-components-video.md#playbackspeed8枚举说明)。

   ```typescript
   Column()
     .width('20%')
     .height('100%')
     .gesture(
       LongPressGesture({ repeat: true })
         .onAction((event: GestureEvent | undefined) => {
           // The fast forward icon changes between visible and invisible states.
           this.leftRateOpacity = 1;
           this.rightRateOpacity = 0;
           if (!event) {
             return;
           }
           if (event.repeat) {
             this.isAccelerate = true;
             this.curRate = PlaybackSpeed.Speed_Forward_2_00_X;
             if (!this.isStart) {
               this.isStart = true;
               this.controller.start();
             }
           }
         })
         .onActionEnd(() => {
           this.isAccelerate = false;
           this.curRate = PlaybackSpeed.Speed_Forward_1_00_X;
         })
     );
   ```
2. 同步更新Video组件的currentProgressRate参数，设置视频播放倍速。

   ```typescript
   Video({
     src: this.videoInfoList[this.activeIndex].uri,
     controller: this.controller,
     currentProgressRate: this.curRate
   })
   ```

## 前后台感知

### 场景描述

应用从前台切到后台，再从后台切回前台时，能够保持原有进度继续播放原视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/1c1_eUAATTagfDVDoc1PTg/zh-cn_image_0000002555239532.gif "点击放大")

### 实现原理

通过[onForeground()](../harmonyos-guides/uiability-lifecycle.md#onforeground)和[onBackground()](../harmonyos-guides/uiability-lifecycle.md#onbackground)生命周期方法监听应用前后台状态变化，根据状态变化播放或暂停视频：

* 当应用从前台切到后台时，调用[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)的[pause()](../harmonyos-references/ts-media-components-video.md#pause)方法暂停视频；
* 当应用回到前台时，调用VideoController的[start()](../harmonyos-references/ts-media-components-video.md#start)方法继续播放视频。

### 开发步骤

1. 在EntryAbility.ets文件中，使用[setOrCreate()](../harmonyos-references/ts-state-management.md#setorcreate10)设置并缓存应用前后台状态isForeGround：
   * 当应用处于前台时，isForeGround为true。
   * 当应用处于后台时，isForeGround为false。

   ```typescript
   onForeground(): void {
     // Ability has brought to foreground
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     AppStorage.setOrCreate('isForeGround', true);
   }

   onBackground(): void {
     // Ability has back to background
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     AppStorage.setOrCreate('isForeGround', false);
   }
   ```
2. 在VideoPlayer自定义组件里对状态变量isForeGround添加[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)，通过回调函数foregroundStatus监听状态变量的变化。

   ```typescript
   @Watch('foregroundStatus') @StorageLink('isForeGround') isForeGround: boolean = false;
   ```
3. 在回调函数foregroundStatus中调用Video组件的播放/暂停方法，以实现切换到后台时视频暂停播放、切回前台时视频恢复播放。

   ```typescript
   // Perception of foreground and background.
   foregroundStatus() {
     if (this.isForeGround) {
       this.controller.start(); // Start playing when in the foreground.
       this.isStart = true;
     } else {
       this.controller.pause(); // Pause playback when in the background.
       this.isStart = false;
     }
   }
   ```

## 音量设置

### 场景描述

音量设置在视频应用中是一种常见功能，允许用户在不离开视频播放界面的情况下，通过长按结合滑动手势即可调节音量，以获得更佳的观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/POM_xo_gSbKdk_4F_xWhpg/zh-cn_image_0000002585679469.gif "点击放大")

### 实现原理

系统音量面板[@ohos.multimedia.avVolumePanel (音量面板)](../harmonyos-references/ohos-multimedia-avvolumepanel.md)提供了展示和调节系统音量的功能。结合[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)长按手势事件和[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，设置滑动方向为竖直方向，长按触屏后，上滑增大音量，下滑减小音量，实现控制系统音量功能。

### 开发步骤

1. 创建AVVolumePanel系统音量面板。

   ```typescript
   @Prop volume: number = CommonConstants.INITIAL_VOLUME; // volume level
   @Prop volumeVisible: boolean = false; // Whether to show the volume component.
   @Prop isFullLandscapeScreen: boolean = false; // FullLandscapeScreen or not

   build() {
     Column() {
       AVVolumePanel({
         volumeLevel: this.volume,
         volumeParameter: {
           position: {
             x: this.isFullLandscapeScreen ? CommonConstants.AV_VOLUME_PANEL_X_IN_FULL :
               CommonConstants.AV_VOLUME_PANEL_X,
             y: this.isFullLandscapeScreen ? CommonConstants.AV_VOLUME_PANEL_Y_IN_FULL :
               CommonConstants.AV_VOLUME_PANEL_Y
           }
         }
       })
         .width(10)
     }
     .visibility(this.volumeVisible ? Visibility.Visible : Visibility.Hidden)
     .height('50%')
   }
   ```
2. 绑定[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)和[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)组合而成的Sequence组合手势。
   * 长按触发LongPressGesture时，显示AVVolumePanel音量调节组件。

     ```typescript
     LongPressGesture({ repeat: true })
       .onAction((event: GestureEvent | undefined) => {
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'LongPressGesture:' + event);
         if (event) {
           this.volumeVisible = true;
         }
       })
       .onActionEnd(() => {
         this.volumeVisible = false;
       }),
     ```
   * 长按后滑动触发PanGesture时，根据手势滑动距离计算并同步刷新音量值volume。

     ```typescript
     // When dragging after a long press, the PanGesture gesture is triggered.
     PanGesture({ direction: PanDirection.Vertical })
       .onActionUpdate((event: GestureEvent) => {
         let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.windowHeight;
         curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
         curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
         this.volume = curVolume;
       })
       .onActionEnd(() => {
         setTimeout(() => {
           this.volumeVisible = false;
         }, 5000)
       })
     ```

## 自动连播

### 场景描述

当前视频播放结束后，播放器将自动加载并播放下一个视频，无需用户手动操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/AcsrzoQRRs-yrFj8MVO-TQ/zh-cn_image_0000002555079912.gif "点击放大")

### 实现原理

1. 在视频播放结束时，触发[onFinish()](../harmonyos-references/ts-media-components-video.md#onfinish)事件，通过Swiper组件的[showNext()](../harmonyos-references/ts-container-swiper.md#shownext)切换下一个视频。
2. 在Swiper的[onAnimationStart()](../harmonyos-references/ts-container-swiper.md#onanimationstart9)回调中更新视频索引值。
3. 监听视频索引值变化，使用[reset()](../harmonyos-references/ts-media-components-video.md#reset12)、start()分别重置和播放视频。

### 开发步骤

1. 在Video组件的onFinish()事件中，调用Swiper组件的showNext()方法。

   ```typescript
   .onFinish(() => {
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'onFinish and showNext.');
     this.swiperController?.showNext();
   })
   ```
2. 在Swiper组件的onAnimationStart()回调中，更新当前视频的索引值currentIndex。

   ```typescript
   Swiper(this.swiperController) {
     LazyForEach(new MyDataSource(this.videoInfoList), (item: VideoDataModel, index: number) => {
       VideoPlayer({
         isFullLandscapeScreen: this.isFullLandscapeScreen, // fullLandscapeScreen state
         videoIndex: index, // Video index
         activeIndex: this.currentIndex, // Index of the currently playing video
         screenWidth: this.screenWidth // Screen width
       })
     }, (item: string) => item)
   }
   // ...
   .onAnimationStart((index: number, targetIndex: number) => {
     hilog.info(DOMAIN, 'testTag', '%{public}s',
       `onAnimationStart index:${index} , targetIndex: ${targetIndex}`);
     this.currentIndex = targetIndex; // Update current video index.
   })
   ```
3. 在VideoPlayer自定义组件里对状态变量activeIndex添加@Watch装饰器，通过回调函数activeIndexChange监听当前视频的索引值的变化。

   ```typescript
   @Prop @Watch('activeIndexChange') activeIndex: number = 0; // Index of the currently playing video
   ```
4. 在回调函数activeIndexChange中重置播放进度显示值为0，然后依次调用Video组件的reset()、start()方法重置和播放下一个视频。

   ```typescript
   // Monitor the change of activeIndex when the onchange event occurs.
   activeIndexChange() {
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'activeIndexChange.' + this.activeIndex);
     this.currentTime = 0; // Reset currentTime
     this.controller.reset(); // Reset VideoController
     this.controller.start(); // Start playing
   }
   ```

## 示例代码

* [基于Video组件播放短视频](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent)
