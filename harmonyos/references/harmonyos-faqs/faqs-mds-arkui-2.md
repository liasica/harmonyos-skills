---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mds-arkui-2
title: 画中画如何获取当前视频播放状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 画中画如何获取当前视频播放状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e0584f441715021d1cc27795692def6664e8730c01cfa1813bc828d90b130b79
---

## 问题现象

画中画播放视频时，会出现画中画中视频在播放，播放控件还是暂停的情况，画中画如何获取当前视频播放状态来手动修改播放控件？

问题现象图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/YiVDCZglRKKEgB65EbXqhg/zh-cn_image_0000002655968546.png "点击放大")

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/BrgWrj9HQBiepa7XfR_4KQ/zh-cn_image_0000002655808762.png "点击放大")

## 背景知识

* [on('stateChange')](../harmonyos-references/js-apis-pipwindow.md#onstatechange)：开启画中画生命周期状态的监听。
* [AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)：AVPlayer的状态机，可通过state属性主动获取当前视频播放、暂停等状态。
* [updatePiPControlStatus](../harmonyos-references/js-apis-pipwindow.md#updatepipcontrolstatus12)：更新控制面板控件功能状态。

## 解决方案

* 拉起画中画前，可以调用updatePiPControlStatus接口，更新播放控件状态，来保持视频状态和播放控件状态一致。
* 使用on('stateChange')监听画中画生命周期，在画中画启动状态STARTED生命周期中使用AVPlayerState获取当前视频的播放状态，根据当前视频的播放状态使用updatePiPControlStatus方法通过[PiPControlType](../harmonyos-references/js-apis-pipwindow.md#pipcontroltype12)和[PiPControlStatus](../harmonyos-references/js-apis-pipwindow.md#pipcontrolstatus12)两个参数，分别设置当前画中画的控制面板控件类型和控制面板控件状态。

  示例代码如下：

  ```ts
  this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
          switch (state) {
            case PiPWindow.PiPState.ABOUT_TO_START:
              this.curState = 'ABOUT_TO_START';
              this.curError = $r('app.string.current_error_hint');
              break;
            case PiPWindow.PiPState.STARTED:
              this.curState = 'STARTED';
              this.curError = $r('app.string.current_error_hint');
              if (this.player?.State == "playing") { // 如果视频正在播放，设置视频播放控制面板中播放/暂停控件为播放状态
                let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE;
                let status: PiPWindow.PiPControlStatus = PiPWindow.PiPControlStatus.PLAY;
                if (this.pipController != undefined) {
                  this.pipController.updatePiPControlStatus(controlType, status);
                }
              } else if (this.player?.State == "paused") { // 如果视频正在暂停，设置视频播放控制面板中播放/暂停控件为暂停状态
                let controlType: PiPWindow.PiPControlType = PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE;
                let status: PiPWindow.PiPControlStatus = PiPWindow.PiPControlStatus.PAUSE;
                if (this.pipController != undefined) {
                  this.pipController.updatePiPControlStatus(controlType, status);
                }
              }
              break;
            case PiPWindow.PiPState.ABOUT_TO_STOP:
              this.curState = 'ABOUT_TO_STOP';
              this.curError = $r('app.string.current_error_hint');
              break;
            case PiPWindow.PiPState.STOPPED:
              this.player?.updatePlayStatus(true);
              this.player?.play();
              this.curState = 'STOPPED';
              this.curError = $r('app.string.current_error_hint');
              break;
            case PiPWindow.PiPState.ABOUT_TO_RESTORE:
              this.curState = 'ABOUT_TO_RESTORE';
              this.curError = $r('app.string.current_error_hint');
              break;
            case PiPWindow.PiPState.ERROR:
              this.curState = 'ERROR';
              this.curError = reason;
              break;
            default:
              break;
          }
          Logger.info(`[${TAG}] onStateChange: ${this.curState}, reason: ${reason}`);
        });
  ```

  详细代码，参考：[实现画中画效果。](https://gitee.com/harmonyos_samples/window-pip/repository/archive/master.zip)

## 常见FAQ

Q：如何实现一个类似于语音通话时，缩小画中画可以全屏幕拖拽的效果，且点击不会出现任何按钮。

A：将[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)的参数[PiPTemplateType](../harmonyos-references/js-apis-pipwindow.md#piptemplatetype)设置成VIDEO\_MEETING（或者VIDEO\_CALL），且controlGroups: []设置为空，可以实现点击不出现按钮，且能拖动。

Q：有A和B两个页面，从A页面进入B页面之后，在B页面进行视频通话功能，此时点击开启画中画会返回A页面，再次点击画中画，此时会重新进入B页面，进入B页面就会打断进行中的视频通话，导致视频通话功能异常，这个问题要怎么解决？

A：点击画中画小窗，进入B页面，相当于重新router.push，B页面的参数此时处于初始化状态，修改了进行中的视频通话状态，导致进行中的视频通话被打断，功能异常。

需要修改B页面的初始化参数，增加判断，如果此时处于视频通话中，则不进行视频通话状态参数初始化操作，反之则进行初始化操作。

Q：如何实现：在小窗播放时，切换视频通过原页面列表操作，保持小窗不关闭；切换为视频时显示快进快退按钮，切换为直播时则不显示。

A：画中画页面组件视频或直播通过这两个配置项去修改：

templateType: PiPWindow. PiPTemplateType. VIDEO\_LIVE //对于视频通话、视频会议等场景，需要设置相应的模板类型。

controlGroups:PiPWindow.VideoLiveControlGroup.VIDEO\_PLAY\_PAUSE //对于视频通话、视频会议和视频直播；画中画控制面板的可选控件组列表，应用可以配置是否显示可选控件。

实现方案：

1. 移除现有的画中画控制器。
2. 调整相关配置参数，重新创建新的画中画控制器。

Q：如何判断当前设备是否支持画中画功能？

A：可以使用[PiPWindow.isPiPEnabled](../harmonyos-references/js-apis-pipwindow.md#pipwindowispipenabled)判断当当前设备是否支持画中画功能。

Q：视频通话挂断后，再次开启画中画小窗时全屏画面不消失，如何解决？

A：该问题与画中画小窗本身无关，属于路由管理问题。全屏画面消失需要应用侧针对业务逻辑进行路由跳转（如调用[router.pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)跳转至其他页面）或者应用退后台（调用[minimize](../harmonyos-references/arkts-apis-window-window.md#minimize11)）来实现。
