---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avplayer-long-video
title: 基于AVPlayer播放长视频实践
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 媒体开发实践 > 基于AVPlayer播放长视频实践
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0746d43cd4da417159ea1b431c5f49f204ab3f5602ef22c2e0f0791c7071cf80
---

## 概述

本文适用于视频播放类应用的开发，针对市场上主流视频播放类应用的常见场景，介绍了如何基于AVPlayer系统播放器实现长视频播放。本文指导开发者实现亮度控制、焦点管理、前后台感知、弹幕发送与显示、视频截图、画中画播放、后台播放与接入播控中心、视频首帧显示等开发场景。

基本播控、精准跳转、静音播放、窗口缩放设置、倍速播放、音量控制、字幕挂载场景参见[《基于AVPlayer基础播控实践》](../best-practices/bpta-avplayer-basic-control.md)。

本篇文章主要介绍以下内容：

* [亮度控制](avplayer-long-video.md#亮度控制)
* [焦点管理](avplayer-long-video.md#焦点管理)
* [前后台感知](avplayer-long-video.md#前后台感知)
* [弹幕发送与显示](avplayer-long-video.md#弹幕发送与显示)
* [视频截图](avplayer-long-video.md#视频截图)
* [画中画播放](avplayer-long-video.md#画中画播放)
* [接入播控中心](avplayer-long-video.md#接入播控中心)
* [后台播放](avplayer-long-video.md#后台播放)
* [视频首帧显示](avplayer-long-video.md#视频首帧显示)
* [横竖屏切换与旋转感知](avplayer-long-video.md#横竖屏切换与旋转感知)
* [视频无缝转场播放](avplayer-long-video.md#视频无缝转场播放)

## 亮度控制

### 场景描述

用户在横屏播放视频时可通过手势滑动调节屏幕亮度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/XlBCuCW_RXyaVQAMfTkt2A/zh-cn_image_0000002736433727.gif)

### 实现原理

使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)设置亮度面板，绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，当Pan手势在移动过程中调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)方法，实现上滑增加亮度、下滑减少亮度的功能。

### 开发步骤

1. 当进入全屏播放模式时，在视频播放界面右侧区域添加Slider组件，用来展示屏幕亮度变化情况。

   ```typescript
   Column() {
     Stack() {
       Slider({
         value: this.screenBrightness,
         min: 0,
         max: 1,
         step: 0.05,
         style: SliderStyle.NONE,
         direction: Axis.Vertical,
         reverse: true
       })
         .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
         .height(160)
         .selectedColor(Color.White)
         .trackColor(Color.Black)
         .trackThickness(40)
         .onChange(async (value: number) => {
           this.screenBrightness = value;
           let windowStage: window.WindowStage = AppStorage.get(KeyConstants.KEY_WINDOW_STAGE) as window.WindowStage;
           try {
             let mainWin: window.Window = windowStage.getMainWindowSync();
             await mainWin.setWindowBrightness(value);
           } catch (exception) {
             Logger.error(TAG, `getMainWindowSync failed: code: ${exception.code}, message: ${exception.message}`);
           }
         })

       Image($r('app.media.sun_max_fill'))
         .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
         .margin({ top: 120 })
         .width(20)
         .height(20)
     }
     .margin({
       top: 0,
       right: 0
     })
   }
   .width('50%')
   .alignItems(HorizontalAlign.End)
   .justifyContent(FlexAlign.Center)
   .padding({
     right: 30,
     bottom: 20
   })
   ```
2. 在视频播放界面绑定PanGesture滑动手势事件，设置触发条件为仅在屏幕右侧区域且垂直方向滑动Pan手势时，调用setWindowBrightness()方法，实现亮度的调节。此处setScreenBrightness()为setWindowBrightness()的封装。

   ```typescript
   private processGesture(event: GestureEvent) {
     if (event.fingerList.length === 0) {
       return;
     }
     if (event.fingerList[0].globalX > (this.getUIContext().px2vp(this.screenWidth / 2))) {
       if (this.isInputtingBulletComment) {
         return;
       }
       this.visible = true;
       let curBrightness = this.screenBrightness - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
       curBrightness = this.getValidValue(curBrightness, 0.0, 1.0);
       this.screenBrightness = curBrightness;
       this.setScreenBrightness(this.screenBrightness);
     } else {
       this.visible = false;
       let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
       curVolume = this.getValidValue(curVolume, 0.0, 15.0);
       this.volume = curVolume;
     }
   }
   ```

   ```typescript
   .gesture(
     PanGesture({ direction: PanDirection.Vertical })
       .onActionStart(() => {
       })
       .onActionUpdate((event: GestureEvent) => {
         this.processGesture(event);
       })
       .onActionEnd(() => {
         setTimeout(() => {
           this.visible = false;
         }, 3000)
       })
   )
   ```

## 焦点管理

### 场景描述

通过正确设置音频流类型、中断事件处理和自定义焦点策略，完成播放过程中的音频焦点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/lymKddczTBy4GEcOzEnF0g/zh-cn_image_0000002706834576.gif)

### 实现原理

通过AVPlayer的[on('audioInterrupt')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiointerrupt9)方法，监听音频焦点变化，根据不同的[打断类型](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)和[中断提示](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)作相应的处理，更多焦点管理相关说明可参考[音频焦点管理](../best-practices/bpta-audio-focus-management.md)。

* 当闹钟或电话等外部打断事件发生时，打断类型为强制打断（INTERRUPT\_FORCE），视频会自动中断播放。
* 当闹钟或电话提示音结束后，系统会发送一个打断事件，其打断类型为共享打断（INTERRUPT\_SHARE），中断提示为音频可继续播放（INTERRUPT\_HINT\_RESUME）。应用监听到该事件后，应调用AVPlayer的play()函数恢复播放。

### 开发步骤

1. 通过AVPlayer实例注册[on('audioInterrupt')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiointerrupt9)方法，监听外部打断事件，当打断类型为INTERRUPT\_FORCE时，视频会自动中断播放。
2. 当打断类型为INTERRUPT\_SHARE、中断提示为INTERRUPT\_HINT\_RESUME时，调用videoPlay()函数恢复播放视频。此处videoPlay()为[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)的封装。

   ```typescript
   private setInterruptCallback() {
     if (!this.avPlayer) {
       return;
     }
     this.avPlayer.on('audioInterrupt', async (interruptEvent: audio.InterruptEvent) => {
       if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
         switch (interruptEvent.hintType) {
           case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
           case audio.InterruptHint.INTERRUPT_HINT_STOP:
             this.isPlaying = false;
             this.updateIsPlay();
             break;
           case audio.InterruptHint.INTERRUPT_HINT_DUCK:
           case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
             break;
           default:
             break;
         }
       } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
         switch (interruptEvent.hintType) {
           case audio.InterruptHint.INTERRUPT_HINT_RESUME:
             this.videoPlay();
             break;
           default:
             break;
         }
       }
     });
   }
   ```

## 前后台感知

### 场景描述

应用从前台切到后台，再从后台切回前台时，能够保持原有进度继续播放原视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/X2YXFuTjTti0V-uXmYvjBg/zh-cn_image_0000002736313683.gif)

### 实现原理

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)。

### 开发步骤

1. 在主页面的onPageShow()和onPageHide()里变更状态变量。

   ```typescript
   onPageHide(): void {
     this.isPageShow = false;
   }
   ```

   ```typescript
   onPageShow(): void {
     this.isPageShow = true;
   }
   ```
2. 在视频播放组件里对该状态变量添加@Watch装饰器。

   ```typescript
   @Prop @Watch('onPageShowChange') isPageShow: boolean = false;
   ```
3. 通过监听事件onPageShowChange调用AVPlayer的播放/暂停方法，以实现切换到后台时视频暂停播放、切回前台时视频恢复播放。此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，resumePlayback()和pausePlay()分别为[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)和[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)的封装。

   ```typescript
   onPageShowChange() {
     if (!this.isPIPShow && this.curIndex === this.index) {
       this.isPageShow ? this.resumePlayback() : this.pausePlay();
     }
   }
   ```

   ```typescript
   private resumePlayback() {
     if (!this.avPlayerController.isPlaying) {
       this.avPlayerController.videoPlay();
     }
   }
   ```

   ```typescript
   private pausePlay() {
     if (this.avPlayerController.isPlaying) {
       this.avPlayerController.videoPause();
     }
   }
   ```

## 弹幕发送与显示

### 场景描述

视频弹幕发送与显示是影音娱乐类应用中的高频使用场景之一，如用户在播放视频、观看直播时可以发送弹幕，实时评论互动，增强用户参与度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/LB5lOkV-Q2Kn5ByibE-sdQ/zh-cn_image_0000002706674640.gif)

### 实现原理

通过数组保存实现弹幕发送，基于[setInterval()](../harmonyos-references/js-apis-timer.md#setinterval)函数和[translate](../harmonyos-references/ts-page-transition-animation.md#translate)属性实现弹幕水平移动的动画效果。

### 开发步骤

1. 在视频播放组件里定义一个空数组，用来保存发送的弹幕，用户输入弹幕点击发送后将输入内容存入当前数组中。

   ```typescript
   private sendBulletComment() {
     if (this.bulletCommentInput.trim()) {
       this.bulletComments = [...this.bulletComments, new BulletComment(this.bulletCommentInput, true)];
       this.bulletCommentInput = '';
       if (this.bulletComments.length > 50) {
         this.bulletComments = this.bulletComments.slice(1);
       }
     }
     this.resumePlayback();
   }
   ```
2. 在弹幕展示组件中，通过调用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)函数设置定时器，定时器定时刷新承载弹幕内容的Text组件的[translate](../harmonyos-references/ts-page-transition-animation.md#translate)属性，刷新所有弹幕位置。

   ```typescript
   private startAnimation() {
     if (this.timerId > 0) {
       clearInterval(this.timerId);
     }
     this.timerId = setInterval(() => {
       let needUpdate = false;
       this.bulletComments.forEach(item => {
         const positionX = item.translateX - item.speed;
         if (positionX !== item.translateX) {
           item.translateX = positionX;
           needUpdate = true;
         }
       });
       const beforeLength = this.bulletComments.length;
       this.bulletComments =
         this.bulletComments.filter(item => item.translateX > -20);
       if (needUpdate || this.bulletComments.length !== beforeLength) {
         this.forceUpdate = !this.forceUpdate;
       }
     }, 16);
   }
   ```

## 视频截图

### 场景描述

视频截图是影音娱乐类应用中的典型场景之一，如用户可在观看视频时截取画面，并对截图的前后帧进行微调，避免所截图片与预期不符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/tzEKClbURnuHdrfFHeOrlw/zh-cn_image_0000002736433729.gif)

### 实现原理

以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件，通过[ComponentSnapshot](arkts-uicontext-component-snapshot.md)对象获取组件截图的能力。

### 开发步骤

1. 通过getUIContext().getComponentSnapshot().get()方法获取视频播放组件XComponent当前截图。

   ```typescript
   private async screenshot() {
     try {
       this.pixmap = await this.getUIContext().getComponentSnapshot().get(`videoXComponent_${this.curSource.index}`);
     } catch (exception) {
       Logger.error(TAG, `screenshot failed: code: ${exception.code}, message: ${exception.message}`);
     }
   }
   ```
2. 调用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)方法跳转到视频播放的上一秒或下一秒，再次通过步骤1的方法获取当前截图。此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，videoSeek()为seek()的封装。

   ```typescript
   private async clickPreviousFrame() {
     this.avPlayerController?.videoSeek(this.screenshotTime - 1000 / ScreenShotConstants.FRAME_RATE);
     this.pausePlay();
     if (this.previousFrameTimerId) {
       clearTimeout(this.previousFrameTimerId);
     }
     this.previousFrameTimerId = setTimeout(() => {
       this.screenshot()
     }, 500)
     this.screenshotTime -= 1000 / ScreenShotConstants.FRAME_RATE;
     this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
   }
   ```

   ```typescript
   private async clickNextFrame() {
     this.avPlayerController?.videoSeek(this.screenshotTime + 1000 / ScreenShotConstants.FRAME_RATE);
     this.pausePlay();
     if (this.nextFrameTimerId) {
       clearTimeout(this.nextFrameTimerId);
     }
     this.nextFrameTimerId = setTimeout(() => {
       this.screenshot()
     }, 500)
     this.screenshotTime += 1000 / ScreenShotConstants.FRAME_RATE;
     this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
   }
   ```

## 画中画播放

### 场景描述

应用在视频播放时，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/kklakGtERwqGu5WHP61wEw/zh-cn_image_0000002706834578.gif)

### 实现原理

以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件，通过[PiPWindow](../harmonyos-references/js-apis-pipwindow.md#导入模块)模块实现画中画基础功能。

**说明** 

* 仅支持以XComponent作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。
* 在API version 20之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从API version 20开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。

### 开发步骤

1. 创建画中画控制器，设置[setAutoStartEnabled()](../harmonyos-references/js-apis-pipwindow.md#setautostartenabled)为true以在应用返回桌面时启动画中画。

   ```typescript
   async createPipController() {
     if (!this.pipController) {
       try {
         this.pipController = await PiPWindow.create({
           context: this.context,
           componentController: this.xComponentController,
           templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY
         });
       } catch (exception) {
         Logger.error(TAG,
           `pipController init failed, Code:${exception.code}, message:${exception.message}`);
       }
     }
     this.pipController?.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
       this.onStateChange(state, reason);
     });

     this.pipController?.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
       this.onActionEvent(event, status);
     });
     this.pipController?.setAutoStartEnabled(true);
   }
   ```
2. 注册生命周期事件和控制事件回调。

   ```typescript
   onStateChange(state: PiPWindow.PiPState, reason: string) {
     switch (state) {
       case PiPWindow.PiPState.ABOUT_TO_START:
         this.curState = 'ABOUT_TO_START';
         break;
       case PiPWindow.PiPState.STARTED:
         this.curState = 'STARTED';
         let status: PiPWindow.PiPControlStatus =
           this.avPlayerController?.isPlaying ? PiPWindow.PiPControlStatus.PLAY : PiPWindow.PiPControlStatus.PAUSE;
         this.pipController?.updatePiPControlStatus(PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE, status);
         break;
       case PiPWindow.PiPState.ABOUT_TO_STOP:
         this.curState = 'ABOUT_TO_STOP';
         break;
       case PiPWindow.PiPState.STOPPED:
         this.curState = 'STOPPED';
         break;
       case PiPWindow.PiPState.ABOUT_TO_RESTORE:
         this.curState = 'ABOUT_TO_RESTORE';
         break;
       case PiPWindow.PiPState.ERROR:
         this.curState = 'ERROR';
         break;
       default:
         break;
     }
   }
   ```

   ```typescript
   onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
     switch (event) {
       case 'playbackStateChanged':
         if (status === 0) {
           this.avPlayerController?.videoPause();
         } else if (status === 1) {
           this.avPlayerController?.videoPlay();
         }
         break;
       default:
         break;
     }
   }
   ```
3. 销毁画中画控制器，设置setAutoStartEnabled()为false以关闭画中画。

   ```typescript
   destroyPipController() {
     if (!this.pipController) {
       return;
     }
     this.pipController.setAutoStartEnabled(false);
     this.pipController.off('stateChange');
     this.pipController.off('controlPanelActionEvent');
     this.pipController = undefined;
   }
   ```

## 接入播控中心

### 场景描述

通过播控中心，控制视频的播放、暂停和上下切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/bTUf-rl_SMqn0XGOvONTPw/zh-cn_image_0000002736313685.gif)

### 实现原理

通过[AVSessionKit](avsession-kit.md)音频播控服务实现视频应用接入播控中心。

### 开发步骤

1. 通过[createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建AVSession实例并激活媒体会话，[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)设置为“video”。

   ```typescript
   public initAvSession() {
     this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
     if (!this.context) {
       Logger.error(TAG, 'session create failed : context is undefined');
       return;
     }
     avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
       this.avSession = avSession;
       BackgroundTaskManager.startContinuousTask(this.context);
       this.setLaunchAbility();
       this.avSession.activate().catch((err: BusinessError) => {
         Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
       });
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
     });
   }
   ```
2. 通过[setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)把会话的一些元数据信息设置给系统，从而在播控中心界面进行展示。如媒体ID（assetId）、标题（title）、播控中心显示的图片（mediaImage）、媒体时长（duration）等。

   ```typescript
   public async setAVMetadata(curSource: VideoData, duration: number) {
     if (curSource === undefined) {
       Logger.error(TAG, 'SetAVMetadata Error, curSource is null');
       return;
     }
     let metadata: avSession.AVMetadata = {
       assetId: `${curSource.index}`,
       title: curSource.name,
       duration: duration
     };
     if (this.avSession) {
       this.avSession.setAVMetadata(metadata).then(() => {
         this.avSessionMetadata = metadata;
       }).catch((err: BusinessError) => {
         Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
       });
     }
   }
   ```
3. 设置用于被播控中心拉起的UIAbility。

   ```typescript
   private setLaunchAbility() {
     if (!this.context) {
       return;
     }
     const wantAgentInfo: wantAgent.WantAgentInfo = {
       wants: [
         {
           bundleName: this.context.abilityInfo.bundleName,
           abilityName: this.context.abilityInfo.name
         }
       ],
       actionType: wantAgent.OperationType.START_ABILITIES,
       requestCode: 0,
       wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
     };
     wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
       if (this.avSession) {
         this.avSession.setLaunchAbility(agent).catch((err: BusinessError) => {
           Logger.error(TAG, `setLaunchAbility failed: code: ${err.code}, message: ${err.message}`);
         });
       }
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `getWantAgent failed: code: ${err.code}, message: ${err.message}`);
     });
   }
   ```
4. 注册播控命令事件监听，便于响应用户通过播控中心下发的播控命令，比如播放[on('play')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)、暂停[on('pause')](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10)、上一曲[on('playPrevious')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplayprevious10)、下一曲[on('playNext')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaynext10)等。

   ```typescript
   public async setAvSessionListener() {
     if (!this.avSessionController) {
       return;
     }
     try {
       this.avSessionController.getAvSession()?.on('play', () => this.sessionPlayCallback());
       this.avSessionController.getAvSession()?.on('pause', () => this.sessionPauseCallback());
       this.avSessionController.getAvSession()?.on('seek', (seekTime: number) => this.sessionSeekCallback(seekTime));
       this.avSessionController.getAvSession()?.on('setLoopMode', (mode: avSession.LoopMode) => {
         Logger.info(`on setLoopMode: ${mode}`);
       });
       this.avSessionController.getAvSession()?.on('playPrevious', () => {
         this.sessionPlayPreviousCallback();
       });
       this.avSessionController.getAvSession()?.on('playNext', () => {
         this.sessionPlayNextCallback();
       });
     } catch (exception) {
       Logger.error(TAG,
         `Invoke setAvSessionListener failed, code is ${exception.code}, message is ${exception.message}`);
     }
   }
   ```
5. 应用状态上报播控中心，当视频状态发生改变时，需要通过[setAVPlaybackState()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)向播控中心上报视频状态，来达到播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。

   ```typescript
   private updateIsPlay() {
     this.avSessionController.setAvSessionPlayState({
       state: this.isPlaying ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
         avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
       position: {
         elapsedTime: this.currentTime,
         updateTime: new Date().getTime()
       },
       duration: this.durationTime,
       speed: this.curSpeed
     });
   }
   ```

   ```typescript
   public setAvSessionPlayState(playbackState: avSession.AVPlaybackState) {
     if (this.avSession) {
       this.avSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
         if (err) {
           Logger.error(TAG, `SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
         } else {
           Logger.info(TAG, 'SetAVPlaybackState successfully');
         }
       });
     }
   }
   ```

## 后台播放

### 场景描述

视频切换到后台播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/5c033Bt_TNOOsuYP5-ePRA/zh-cn_image_0000002706674642.gif)

### 实现原理

首先需实现播控中心的接入，在此基础上申请后台运行权限并设置后台模式，同时为视频应用创建长时后台任务，从而实现视频在后台持续播放的功能。

**说明** 

后台播放的实现依赖于播控中心，建议开发者先完成[接入播控中心](avplayer-long-video.md#接入播控中心)章节的学习。

### 开发步骤

1. 在module.json5配置文件中配置ohos.permission.KEEP\_BACKGROUND\_RUNNING权限和后台模式为“audioPlayback”。

   ```json5
   "requestPermissions": [
     {
       "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
       "reason": "$string:reason_background",
       "usedScene": {
         "abilities": [
           "AvplayerlongvideoAbility"
         ],
         "when": "always"
       }
     }
   ],
   ```

   ```json5
   "backgroundModes": [
     "audioPlayback"
   ],
   ```
2. 创建后台任务管理类，实现后台任务的申请（startContinuousTask）与取消（stopContinuousTask），长时任务类型选择[AUDIO\_PLAYBACK](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)，表示视频后台播放。

   ```typescript
   public static startContinuousTask(context?: common.UIAbilityContext): void {
     if (!context) {
       return;
     }
     let wantAgentInfo: wantAgent.WantAgentInfo = {
       wants: [
         {
           bundleName: context.abilityInfo.bundleName,
           abilityName: context.abilityInfo.name
         }
       ],
       actionType: wantAgent.OperationType.START_ABILITY,
       requestCode: 0,
       wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
     };
     wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
       if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
         backgroundTaskManager.startBackgroundRunning(context,
           backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
         }).catch((err: BusinessError) => {
           Logger.error(TAG, `startBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
         });
       }
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `getWantAgent failed, code is ${err.code}, message is ${err.message}`);
     });
   }
   ```

   ```typescript
   public static stopContinuousTask(context?: common.UIAbilityContext): void {
     if (!context) {
       return;
     }
     if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
       backgroundTaskManager.stopBackgroundRunning(context).then(() => {
       }).catch((err: BusinessError) => {
         Logger.error(TAG, `stopBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
       });
     }
   }
   ```
3. 在AVSession创建和释放时，分别申请和销毁后台长时任务。

   ```typescript
   public initAvSession() {
     this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
     if (!this.context) {
       Logger.error(TAG, 'session create failed : context is undefined');
       return;
     }
     avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
       this.avSession = avSession;
       BackgroundTaskManager.startContinuousTask(this.context);
       this.setLaunchAbility();
       this.avSession.activate().catch((err: BusinessError) => {
         Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
       });
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
     });
   }
   ```

   ```typescript
   async unregisterSessionListener() {
     if (!this.avSession) {
       return;
     }
     try {
       this.avSession.off('play');
       this.avSession.off('pause');
       this.avSession.off('playNext');
       this.avSession.off('playPrevious');
       this.avSession.off('setLoopMode');
       this.avSession.off('seek');
     } catch (exception) {
       Logger.error(TAG, `unregisterSessionListener failed: code: ${exception.code}, message: ${exception.message}`);
     }
     BackgroundTaskManager.stopContinuousTask(this.context);
   }
   ```

## 视频首帧显示

### 场景描述

在播放列表或者窗口中显示视频的首帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/8KnRgMQCS1WTD6Y5Zya7Vw/zh-cn_image_0000002736433731.gif)

### 实现原理

* 通过[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12)方法获取本地视频的首帧图片在视频列表展示。
* 通过设置播放策略[setPlaybackStrategy](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackstrategy12)的showFirstFrameOnPrepare属性为true来实现AVPlayer显示视频起播首帧。

### 开发步骤

**播放列表中显示视频首帧的实现**：

使用media.AVImageGenerator实例的[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12)方法获取本地视频的首帧图片在列表展示。

```typescript
public static async getThumbnailFromVideo(src: string, timeUs: number) {
  let pixelMap: image.PixelMap | undefined;
  let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
  let param: media.PixelMapParams = {
    width: 540,
    height: 304
  };
  let generator: media.AVImageGenerator | null = null;
  try {
    let fileDescriptor = await uiContext?.getHostContext()?.resourceManager?.getRawFd(src);
    if (!fileDescriptor) {
      Logger.error(TAG, 'Failed to get file descriptor');
      return null;
    }
    generator = await media.createAVImageGenerator();
    generator.fdSrc = fileDescriptor;
    pixelMap = await generator.fetchFrameByTime(timeUs, queryOption, param);
    await generator.release();
  } catch (exception) {
    Logger.error(TAG, `getThumbnailFromVideo failed, code is ${exception.code}, message is ${exception.message}`);
  }
  return pixelMap;
}
```

**播放窗口中显示视频首帧的实现**：

1. 确认AVPlayer实例中的[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)方法在prepared状态下没有调用this.avPlayer.play()，如有调用，则去掉，避免视频在加载完毕后自动播放。
2. 在on('stateChange')方法中initialized状态下，设置播放策略[setPlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)的showFirstFrameOnPrepare为true。

   ```typescript
   case 'initialized':
     Logger.info(TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
     await this.onInitialized();
     break;
   ```

   ```typescript
   private async onInitialized() {
     if (!this.avPlayer) {
       return;
     }
     this.avPlayer.surfaceId = this.surfaceID;
     try {
       await this.avPlayer.setPlaybackStrategy({
         preferredBufferDuration: 20,
         showFirstFrameOnPrepare: true
       });
     } catch (exception) {
       Logger.error(TAG,
         `setPlaybackStrategy failed. Cause code: ${exception.code}, message: ${exception.message}`);
     }
     this.avPlayer.prepare().catch((err: BusinessError) => {
       Logger.error(TAG, `prepare failed. Code:${err.code}, message:${err.message}`);
     });
   }
   ```

## 横竖屏切换与旋转感知

### 场景描述

用户播放视频时可以根据实际需求进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/EqpjiBZZRs2v6EjLhH51BQ/zh-cn_image_0000002706834580.gif)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/SBRZ66liS1KJrQZncgu1KA/zh-cn_image_0000002736313687.png)

### 实现原理

* 通过设置orientation为auto\_rotation\_restricted实现传感器自动感知。
* 通过设置window.Orientation为USER\_ROTATION\_LANDSCAPE/USER\_ROTATION\_PORTRAIT实现横竖屏的手动切换。

### 开发步骤

**通过传感器旋转自动感知切换**：

在模块级配置文件module.json5中设置[窗口显示方向](../harmonyos-references/arkts-apis-window-e.md#orientation9)为AUTO\_ROTATION\_RESTRICTED。

```json5
"orientation": "auto_rotation_restricted",
```

**通过点击按钮实现横竖屏切换**：

1. 封装横竖屏切换的实现方法。

   ```typescript
   setMainWindowOrientation(orientation: window.Orientation, callback?: Function): void {
     if (this.mainWindowClass === undefined) {
       Logger.error(TAG, 'MainWindowClass is undefined');
       return;
     }
     this.mainWindowClass.setPreferredOrientation(orientation).then(() => {
       callback?.();
     }).catch((err: BusinessError) => {
       Logger.error(TAG, `Failed to set the ${orientation} of main window. Code:${err.code}, message:${err.message}`);
     });
   }
   ```
2. 点击横屏播放按钮时，设置window.Orientation为USER\_ROTATION\_LANDSCAPE。

   ```typescript
   this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);
   ```
3. 点击返回按钮时，设置window.Orientation为USER\_ROTATION\_PORTRAIT。

   ```typescript
   this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
   ```

## 视频无缝转场播放

### 场景描述

用户在横竖屏切换后，视频保持原有进度继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/X6OUw6f_T3GzsTQmTR9QuQ/zh-cn_image_0000002706674644.gif)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/eNo3oNScS6OQwMGaCMcvBQ/zh-cn_image_0000002736433733.png)

### 实现原理

基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)实现视频播放，在横竖屏来回切换时，[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)本身具有保持原有进度继续播放的特性，开发者无需进行额外开发。

## 示例代码

[基于AVPlayer实现长视频播放](https://gitcode.com/harmonyos_samples/avplayer-long-video)
