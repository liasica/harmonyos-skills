---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-24
title: 点击音频播放按钮，应用无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 点击音频播放按钮，应用无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8503c8ace3e0a0dc21d84f5fef882a7bf7cae09957483bbd3054a79f214ace8b
---

## 问题现象

当用户尝试通过点击音频播放控件以启动音频播放功能时，系统未能触发预期的音频输出行为，交互操作表现为无响应状态。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)主要工作是将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听的音频模拟信号，并通过输出设备进行播放。
* AVPlayer播放状态变化示意图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/PD9zFPeEQ2a_imtHu-hVhw/zh-cn_image_0000002628554884.png "点击放大")
* 每个状态的状态码如下：

  ```screen
  enum AudioState {
      STATE_INVALID = -1,    // 无效状态
      STATE_NEW = 0,         // 创建新实例状态
      STATE_PREPARED = 1,    // 准备状态
      STATE_RUNNING = 2,     // 运行状态
      STATE_STOPPED = 3,     // 停止状态
      STATE_RELEASED = 4,    // 释放状态
      STATE_PAUSED = 5       // 暂停状态
  }
  ```
* 在应用播放或录制声音时，常出现与其他音频流的并发或中断情况。在播放或录制的过程中，需[处理音频焦点变化](../harmonyos-guides/audio-playback-concurrency.md#处理音频焦点变化)，并在接收到音频焦点中断事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)）时，采取相应的处理措施。

## 问题定位

1. 在hilog日志中搜索关键字Click accepted，查看点击事件发生之后应用的相关日志。

   ```screen
   11-29 13:26:31.782 29373 29373 I C0391E/com.hx.example/AceGesture: [(100000:100000:scope)] Click try accept
   11-29 13:26:31.782 29373 29373 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: Image
   11-29 13:26:31.787 29373 29373 I C03905/com.hx.example/AceDrag: [(100000:100000:scope)] Trigger pan onReject
   11-29 13:26:31.787 29373 29373 I C03905/com.hx.example/AceDrag: [(100000:100000:scope)] Trigger pan onReject
   11-29 13:26:31.787 29373 29373 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Id:349078, parallel 0 type: 1
   11-29 13:26:31.787 29373 29373 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Id:349078, sequenced 0 type: 1
   11-29 13:26:31.787 29373 29373 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Id:349078, LongPress 0 up, state: 6
   11-29 13:26:31.787 29373 29373 I C03951/com.hx.example/InputKeyFlow: [(100000:100000:scope)] Id:349078, LongPress 0 up, state: 6
   11-29 13:26:31.787 29373 29373 I C03919/com.hx.example/AceInputTracking: [(100000:100000:scope)] Consumed new event id=349078 in ace_container, lastEventInfo: id:349077
   11-29 13:26:31.788 29373  9667 I C02B83/com.hx.example/AudioRenderer: [Pause]StreamClientState for Renderer::Pause. id: 101167
   11-29 13:26:31.788 29373  9667 E C02B83/com.hx.example/AudioRenderer: [Pause]State of stream is not running. Illegal state:5
   ```
2. 可以看到日志中出现错误信息：[Pause]State of stream is not running. Illegal state:5. Illegal state:5。表示当前播放状态处于暂停状态，无法继续暂停。

   ```screen
   11-29 13:26:31.788 29373  9667 I C02B83/com.hx.example/AudioRenderer: [Pause]StreamClientState for Renderer::Pause. id: 101167
   11-29 13:26:31.788 29373  9667 E C02B83/com.hx.example/AudioRenderer: [Pause]State of stream is not running. Illegal state:5
   ```
3. 搜索包含id：101167的日志，可以看到在13:13:58:839音频start成功，在13:23:35.184收到OnInterrupt事件，音频失去焦点进入pause状态。

   ```screen
   11-29 13:13:58.812   786  1802 I C02B8B/audio_server/AudioInterruptService: [ActivateAudioInterrupt]sessionId: 101167 pid: 29373 streamType: 1 usage: 1 source: -1
   11-29 13:13:58.830 29373 63964 I C02B83/com.hx.example/AudioRenderer: [OnDeviceChangeWithInfo]sessionId: 101167, deviceType: 8 reason: 0 size: 0
   11-29 13:13:58.830   786  1802 I C02B83/audio_server/RendererInServer: [Start]sessionId: 101167
   11-29 13:13:58.839 29373 64840 I C02B83/com.hx.example/RendererInClientInner: [StartAudioStream]Start SUCCESS, sessionId: 101167, uid: 20020268
   11-29 13:13:58.840   893 64866 I C01724/resource_schedule_service/TASK_DETECTION: [UpdateAudioRecord:70]Get Audio info uid: 20020268, sessionId: 101167, State: 2, type: player, streamType: 1
   ......
   11-29 13:23:35.078   786   808 I C02B8B/audio_server/AudioInterruptService: [ResumeAudioFocusList]Remove focus info from focus list, streamId: 101167
   11-29 13:23:35.136   786  1057 I C02B8B/audio_server/AudioInterruptService: [ShouldCallbackToClient]uid: 20020268, sessionId: 101167, hintType: 1
   11-29 13:23:35.184 29373 63964 I C02B83/com.hx.example/AudioRenderer: [OnInterrupt]sessionId: 101167, forceType: 0, hintType: 1
   ```
4. 排查应用是否未监听音频焦点中断事件（[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)），导致音频处于pause状态时应用依然认为音频处于播放状态，此时点击播放按钮，应用会执行暂停操作，从而暂停失败。

## 分析结论

应用点击播放时，实际执行的还是暂停操作，所以出现无响应。

## 修改建议

参考[处理音频焦点变化](../harmonyos-guides/audio-playback-concurrency.md#处理音频焦点变化)，在应用重新获取到音频焦点时，执行start操作。
