---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-embeded-network-video
title: 基于AVPlayer播放网络视频实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AVPlayer播放视频系列开发实践 > 基于AVPlayer播放网络视频实践
category: best-practices
scraped_at: 2026-04-29T14:11:18+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:95c29ec93133d6ad7dafac09f45108939e774bf3c5862c35187dc94ef7e19551
---

## 概述

本文适用于网络视频播放类应用开发，针对市场上主流网络视频播放类应用常见场景，介绍如何基于AVPlayer系统播放器实现网络视频播放。本文指导开发者实现以下场景：

* [基础播控](bpta-avplayer-embeded-network-video.md#section102791912878)
* [焦点管理](bpta-avplayer-embeded-network-video.md#section878625410102)
* [弹幕发送与显示](bpta-avplayer-embeded-network-video.md#section28801440152211)
* [画中画播放](bpta-avplayer-embeded-network-video.md#section16229471226)
* [横竖屏切换与旋转感知](bpta-avplayer-embeded-network-video.md#section178071122418)
* [网络视频URL设置](bpta-avplayer-embeded-network-video.md#section269016599556)
* [网络视频缓冲条](bpta-avplayer-embeded-network-video.md#section14584123411115)
* [网络视频边缓冲边播放](bpta-avplayer-embeded-network-video.md#section1383513409117)

## 基础播控

### 场景描述

通过AVPlayer实现视频资源加载、播放、暂停、停止、退出、倍速播放、静音播放、窗口缩放模式、音量调节等操作。详细信息可参考[《基于AVPlayer基础播控实践》](bpta-avplayer-basic-control.md)。

## 焦点管理

### 场景描述

通过正确设置音频流类型、中断事件处理和自定义焦点策略，完成播放过程中的音频焦点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/JfjMBz3-SLeoEfT4N6MrsA/zh-cn_image_0000002486230889.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=0FEA50B8FDD1A826FF8469D0F699BBA4A2ADA08633EF887F976557C38611F44F "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[焦点管理开发步骤](bpta-avplayer-long-video.md#section1716082163419)。

## 弹幕发送与显示

### 场景描述

视频弹幕发送与显示是影音娱乐类应用中的高频使用场景之一，如用户在播放视频、观看直播时可以发送弹幕，实时评论互动，增强用户参与度。

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[弹幕发送与显示开发步骤](bpta-avplayer-long-video.md#section168137393711)。

## 画中画播放

### 场景描述

应用在视频播放时，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/EOy9lgwTQ7KkYlwY4CsriA/zh-cn_image_0000002453191104.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=F3980B034D77E7C604266C65C6EC6AB09ED83F07F14F9D0DAFB024855FD50214 "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[画中画播放开发步骤](bpta-avplayer-long-video.md#section4691194231313)。

## 横竖屏切换与旋转感知

### 场景描述

用户播放视频时可以根据实际需求进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/4QCeC4jNRQ-3z9rzSP__MA/zh-cn_image_0000002453031500.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=7C3E51E707059DF8C6DE3AEAD0DFA7C755C2745CC6C0A9344E7B22386CC166F4 "点击放大")

### 开发步骤

具体开发步骤可参考基于AVPlayer播放长视频实践的[横竖屏切换和旋转感知开发步骤](bpta-avplayer-long-video.md#section1257185216407)。

## 通过URL设置视频源

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/rB_VsjpVTrqdYz_I9Gefww/zh-cn_image_0000002486350845.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=0334D196050C057BD6483A53EC1BF2E7533D9DCEFA112B975730145440259613 "点击放大")

用AVPlayer开发播放功能，在不同场景下如何设置URL。该特性主要用于AVPlayer播放网络流媒体资源，包括在线流媒体链接及本地m3u8流媒体记录文件。在线流媒体支持以下协议：

| 流媒体协议类型 | 典型链接 |
| --- | --- |
| HLS | https://xxxx/index.m3u8 |
| DASH | https://xxxx.mpd |
| HTTP/HTTPS | https://xxxx.mp4 |
| HTTP-FLV | https://xxxx.flv |

详情可参考[使用AVPlayer播放流媒体(ArkTS)](../harmonyos-guides/streaming-media-playback-development-guide.md)

本章节主要介绍如何配置HLS协议和HTTP/HTTPS协议的在线链接URL，以及如何设置本地M3U8文件和MP4文件的URL，以实现视频播放功能。

### 实现原理

AVPlayer通过URL形式配置播放源，有以下两种方式：

* 一种是直接设置AVPlayer的url属性，适用于不需要额外配置项的场景，例如下文的在线视频配置URL示例。
* 另一种是调用[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)函数通过URL创建播放源，然后调用[AVPlayer.setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法设置播放源，适用于需要额外配置媒体类型或者播放策略的场景，例如下文的本地M3U8文件配置URL示例。

### 开发步骤

1. 创建AVPlayer。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
   6. // Creates the avPlayer instance object.
   7. this.avPlayer = await media.createAVPlayer();
   8. // ...
   9. } catch (err) {
   10. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   11. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   12. }

   14. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L52-L169)
2. 设置AVPlayer的url属性，或者调用[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)函数通过URL创建播放源，并配置到AVPlayer，之后AVPlayer将自动进入initialized状态。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
   6. // Creates the avPlayer instance object.
   7. this.avPlayer = await media.createAVPlayer();
   8. // Creates a callback function for state machine changes.
   9. this.setAVPlayerCallback();
   10. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

   12. if (!this.context) {
   13. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
   14. return
   15. }
   16. switch (this.curSource.type) {
   17. // ...
   18. // Set online video source by url
   19. case VideoDataType.URL:
   20. this.avPlayer.url = this.curSource.videoSrc;
   21. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   22. `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
   23. break;
   24. // Set the mediaSource by url with playbackStrategy
   25. case VideoDataType.RAW_M3U8_FILE:
   26. let m3u8Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
   27. let fdUrl = 'fd://' + m3u8Fd.fd + '?offset=' + m3u8Fd.offset + '&size=' + m3u8Fd.length;
   28. // create mediaSource by the URL instead of an assigned URL
   29. let mediaSource = media.createMediaSourceWithUrl(fdUrl);
   30. mediaSource.setMimeType(media.AVMimeTypes.APPLICATION_M3U8);
   31. // create PlaybackStrategy
   32. let playbackStrategy: media.PlaybackStrategy = { preferredBufferDuration: 20, showFirstFrameOnPrepare: true };
   33. await this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
   34. hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(fdUrl)}`);
   35. break;
   36. // Set local video source by url
   37. case VideoDataType.RAW_MP4_FILE:
   38. let mp4Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
   39. let mp4FdUrl = 'fd://' + mp4Fd.fd;
   40. this.avPlayer.url = mp4FdUrl;
   41. hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(mp4FdUrl)}`);
   42. break;

   44. default:
   45. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed VideoDataType is invalid`);
   46. break;
   47. }
   48. await this.setCaption();
   49. } catch (err) {
   50. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   51. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   52. }

   54. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L51-L170)

## 网络视频缓冲条

### 场景描述

网络视频缓冲进度条是影音娱乐类应用中的典型场景之一，如用户播放在线视频时，进度条显示当前缓冲的可播放进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/ViHNThhiS7C5wy7LcM83QA/zh-cn_image_0000002486230901.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=D971AACAEAF4347C27426BAE874EA84C04CD48E8E83A2EC1B7BBDF8B056A8743 "点击放大")

### 实现原理

本示例基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现在线视频播放，基于[Slider](../harmonyos-references/ts-basic-components-slider.md)实现视频播放和缓冲进度条显示。由于Slider没有多进度特性，这里使用[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)布局，将缓冲条Slider和进度条Slider重叠显示，来实现缓冲进度和播放进度同时显示的效果。

其中缓冲条Slider的value值绑定由@State修饰的状态变量currentBufferTime，并通过注册[bufferingUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#onbufferingupdate9)事件处理函数，在该函数中获取已缓冲内容预计可播放时长，结合已播放时长得到当前缓冲进度。

说明

由于bufferingUpdate事件的回调函数参数中，infoType为media.BufferingInfoType.CACHED\_DURATION时，value为已缓冲内容预计可播放时长，该值为预估值，所以缓冲进度亦为预估值，并不能保证百分百精准。bufferingUpdate事件的回调函数参数详情可参考[OnBufferingUpdateHandler](../harmonyos-references/arkts-apis-media-t.md#onbufferingupdatehandler12)。

### 开发步骤

1. 创建AVPlayer，并配置好相应的播放源。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
   6. // Creates the avPlayer instance object.
   7. this.avPlayer = await media.createAVPlayer();
   8. // Creates a callback function for state machine changes.
   9. this.setAVPlayerCallback();
   10. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

   12. if (!this.context) {
   13. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
   14. return
   15. }
   16. switch (this.curSource.type) {
   17. // ...
   18. // Set online video source by url
   19. case VideoDataType.URL:
   20. this.avPlayer.url = this.curSource.videoSrc;
   21. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   22. `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
   23. break;
   24. // ...
   25. }
   26. await this.setCaption();
   27. } catch (err) {
   28. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   29. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   30. }

   32. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L56-L171)
2. 注册[timeUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#ontimeupdate9)事件处理函数，并在函数中更新由@State修饰的状态变量currentTime。

   ```
   1. private setAVPlayerCallback() {
   2. // ...
   3. this.avPlayer.on('timeUpdate', (time: number) => {
   4. this.currentTime = time;
   5. AppStorage.setOrCreate('CurrentTime', time);
   6. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   7. `setAVPlayerCallback timeUpdate success,and new time is = ${this.currentTime}`);
   8. });
   9. // ...
   10. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L187-L286)
3. 注册[bufferingUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#onbufferingupdate9)事件处理函数，并在函数中更新由@State修饰的状态变量currentBufferTime。

   ```
   1. private setAVPlayerCallback() {
   2. // ...
   3. // Listen to the streaming media buffer status and the estimated playback duration of the buffered data
   4. this.avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   6. `BufferedProgressBar bufferingUpdate, infoType is ${infoType}, value is ${value}.`);
   7. // ...
   8. if (infoType === media.BufferingInfoType.CACHED_DURATION && this.avPlayer) {
   9. this.currentBufferTime = Math.max(this.currentBufferTime, this.currentTime + value);
   10. hilog.info(CommonConstants.LOG_DOMAIN, TAG, `currentBufferTime: ${this.currentBufferTime}`)
   11. }
   12. });

   14. // ...
   15. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L188-L287)
4. 绑定currentTime到播放Slider的value属性，绑定currentBufferTime到缓冲Slider的value属性，并利用[Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)布局将播放[Slider](../harmonyos-references/ts-basic-components-slider.md)和缓冲Slider重叠在一起，然后设置播放Slider的trackColor为透明，缓冲Slider的style属性设为SliderStyle.NONE以隐藏滑块。

   ```
   1. @Builder
   2. progressBuilder() {
   3. Stack() {
   4. Slider({
   5. value: this.avPlayerController.currentTime,
   6. min: CommonConstants.SLIDER_PROGRESS_MIN,
   7. max: this.avPlayerController.durationTime,
   8. step: CommonConstants.SLIDER_PROGRESS_STEP,
   9. direction: Axis.Horizontal
   10. })
   11. .blockColor(Color.White)
   12. .trackColor($r('app.color.track_color_show'))
   13. .selectedColor($r('app.color.slider_selected'))
   14. .trackThickness(5)
   15. .zIndex(1)
   16. .onChange((value: number) => {
   17. this.avPlayerController.videoSeek(value);
   18. })

   20. Slider({
   21. value: this.avPlayerController.currentBufferTime,
   22. min: CommonConstants.SLIDER_PROGRESS_MIN,
   23. max: this.avPlayerController.durationTime,
   24. step: CommonConstants.SLIDER_PROGRESS_STEP,
   25. direction: Axis.Horizontal,
   26. style: SliderStyle.NONE
   27. })
   28. .trackColor(Color.Grey)
   29. .selectedColor(Color.White)
   30. .blockColor($r('app.color.track_color_show'))
   31. .trackThickness(5)
   32. .margin({ left: 12, right: 12 })
   33. .zIndex(0)
   34. }
   35. .layoutWeight(1)
   36. }
   ```

   [BufferBarPlayer.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/pages/BufferBarPlayer.ets#L34-L70)

## 网络视频边缓冲边播放

### 场景描述

网络视频边缓冲边播放是影音娱乐类应用中的典型场景之一，如用户播放在线视频时，不用等待视频资源完全加载（缓冲）后再进行播放，可以缓冲到一定资源后，就可直接起播。AVPlayer自带边缓冲边播放的特性，本章节介绍AVPlayer缓冲区相关参数配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/cVSnf28IRBevvIwh2RtbXg/zh-cn_image_0000002453191116.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=586C67A1B0B6A7435E6E897110A2716D1D5855045241328BA35BA3D46C81C9C0 "点击放大")

### AVPlayer缓冲区工作过程

对于缓冲区而言，下载线程是生产端，读取线程则是消费端。生产端将数据写入到缓冲区中，消费端则从缓冲区读取数据，下面将介绍缓冲区中的几个水位线概念。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/y_oov6GFRVOvIz5delUG6w/zh-cn_image_0000002453031512.png?HW-CC-KV=V1&HW-CC-Date=20260429T061114Z&HW-CC-Expire=86400&HW-CC-Sign=004583A0F1612546657BE51E336C5F9F5461661AD7728882BB25D584E5741D13 "点击放大")

以上四个水位线取值情况如下，其中起播水位线，和下载暂停水位线（缓冲区大小）可通过配置AVPlayer的播放策略来控制，其他两个暂未提供配置接口。

| 水位线 | 默认值 | 说明 |
| --- | --- | --- |
| 起播水位线 | 若下载速率 >= 码率场景，起播水位线取值：0.3秒 \* 码率  若下载速率 < 码率场景，起播水位线取值：5秒 \* 码率  若起播水位线小于10KB，取10KB | 在快速起播和顺滑播放间进行一个相对合理的分割。 |
| 止播水位线 | 单次读取数据量，若小于5KB则取5KB | 避免将缓冲区中的可用数据耗尽。 |
| 下载启动水位线 | 480KB | 降低线程启动频率，进行集中下载，降低cpu及指令数消耗。 |
| 下载暂停水位线 | 缓冲区大小 | 当缓冲区写满时，停止下载，支持修改。 |

起播水位线的默认值是根据下载速率确定，下载速率 >= 码率时，取值：0.3秒 \* 码率，即缓冲速度大于播放速度时，缓冲到0.3秒，开始播放；下载速率 < 码率时，起播水位线取值：5秒 \* 码率，即在缓冲内容累计满5秒后开始播放。这样可以在网络好的情况下快起播，减少用户等待时间，在网络差的情况下慢起播，避免播放和暂停状态间频繁来回切换，影响用户体验。若开发者不满足默认设置，可通过配置AVPlayer播放策略[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)来控制起播水位线。

下载暂停水位线是指已缓冲，但还未被消费（播放）数据最大占用空间，该值的大小依赖于缓冲区大小，可通过配置缓冲区大小间接控制该参数值。该值设置太小的话，在网络波动较大的环境，可能会影响视频播放的顺滑度；设置太大的情况下，一定程度会浪费用户网络资源。该参数默认为最大值20M，开发者可根据需要自行配置[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)中的preferredBufferDuration参数来控制缓冲区大小。preferredBufferDuration的单位为秒，缓冲区大小将被设定为preferredBufferDuration \* 1MB。例如，将preferredBufferDuration设为20秒，缓冲区大小将被设置为20MB。

| 默认缓冲区大小 | 用户自定义缓冲区大小 |
| --- | --- |
| 20MB | 5MB ~ 20MB |

起播水位线和下载暂停水位线（缓冲区大小）的配置方式均由AVPlayer的播放策略控制，播放策略的配置方式有两种：

* 一种是通过AVPlayer的[setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer，详情可参考[在线视频播放卡顿优化](bpta-online-video-playback-lags-practice.md#section1411814743015)。
* 另一种是通过AVPlayer的[setPlaybackStrategy()](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackstrategy12)方法将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer，第二种需要在AVPlayer状态为initialized或者stopped时，才可生效。

### 通过setMediaSource()方法配置

1. 创建AVPlayer，并通过[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)方法生成MediaSource实例。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
   6. // Creates the avPlayer instance object.
   7. this.avPlayer = await media.createAVPlayer();
   8. // Creates a callback function for state machine changes.
   9. this.setAVPlayerCallback();
   10. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

   12. if (!this.context) {
   13. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
   14. return
   15. }
   16. switch (this.curSource.type) {
   17. // ...
   18. // Set online video source by url
   19. case VideoDataType.URL:
   20. this.avPlayer.url = this.curSource.videoSrc;
   21. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   22. `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
   23. break;
   24. // ...
   25. }
   26. await this.setCaption();
   27. } catch (err) {
   28. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   29. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   30. }

   32. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L56-L171)
2. 创建PlaybackStrategy实例，并通过AVPlayer的[setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法，将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. // ...
   6. switch (this.curSource.type) {
   7. // ...
   8. // Set the mediaSource by url with playbackStrategy
   9. case VideoDataType.RAW_M3U8_FILE:
   10. let m3u8Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
   11. let fdUrl = 'fd://' + m3u8Fd.fd + '?offset=' + m3u8Fd.offset + '&size=' + m3u8Fd.length;
   12. // create mediaSource by the URL instead of an assigned URL
   13. let mediaSource = media.createMediaSourceWithUrl(fdUrl);
   14. mediaSource.setMimeType(media.AVMimeTypes.APPLICATION_M3U8);
   15. // create PlaybackStrategy
   16. let playbackStrategy: media.PlaybackStrategy = { preferredBufferDuration: 20, showFirstFrameOnPrepare: true };
   17. await this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
   18. hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(fdUrl)}`);
   19. break;
   20. // ...
   21. }
   22. await this.setCaption();
   23. } catch (err) {
   24. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   25. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   26. }

   28. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L55-L174)

### 通过setPlaybackStrategy()方法配置

1. 创建AVPlayer，并直接通过赋值AVPlayer.url属性，对AVPlayer初始化。

   ```
   1. // Create an AVPlayer instance
   2. public async initAVPlayer(source: VideoData, surfaceId: string) {
   3. // ...
   4. try {
   5. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
   6. // Creates the avPlayer instance object.
   7. this.avPlayer = await media.createAVPlayer();
   8. // Creates a callback function for state machine changes.
   9. this.setAVPlayerCallback();
   10. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

   12. if (!this.context) {
   13. hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
   14. return
   15. }
   16. switch (this.curSource.type) {
   17. // ...
   18. // Set online video source by url
   19. case VideoDataType.URL:
   20. this.avPlayer.url = this.curSource.videoSrc;
   21. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   22. `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
   23. break;
   24. // ...
   25. }
   26. await this.setCaption();
   27. } catch (err) {
   28. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   29. `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
   30. }

   32. }
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L56-L171)
2. 注册AVPlayer的状态回调函数，并在initialized状态回调中配置[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例。

   ```
   1. // Callback function for state machine changes
   2. this.avPlayer.on('stateChange', async (state) => {
   3. if (!this.avPlayer) {
   4. return;
   5. }
   6. switch (state) {
   7. // ...
   8. case 'initialized': // This status is reported after the playback source is set on the AVPlayer.
   9. hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
   10. // Set the display screen. This parameter is not required when the resource to be played is audio-only.
   11. this.avPlayer.surfaceId = this.surfaceID;
   12. hilog.info(CommonConstants.LOG_DOMAIN, TAG,
   13. `setAVPlayerCallback this.avPlayer.surfaceId = ${this.avPlayer.surfaceId}`);
   14. await this.avPlayer.setPlaybackStrategy({
   15. preferredBufferDurationForPlaying: 0.3,
   16. preferredBufferDuration: 20,
   17. showFirstFrameOnPrepare: true
   18. });
   19. this.avPlayer.prepare();
   20. break;
   21. // ...
   22. }
   23. });
   ```

   [AvPlayerController.ets](https://gitcode.com/harmonyos_samples/avplayer-online-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L360-L449)

## 示例代码

* [基于AVPlayer播放网络视频实践](https://gitcode.com/harmonyos_samples/avplayer-online-video)
