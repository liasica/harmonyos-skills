---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avplayer-network-video
title: 基于AVPlayer播放网络视频实践
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 媒体开发实践 > 基于AVPlayer播放网络视频实践
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:47+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:9faa86031bd9a1300c691e9a6e8bd2c1e5f58ec1f94947d60f87db94fc6cdd0f
---

## 概述

本文适用于网络视频播放类应用开发，针对市场上主流网络视频播放类应用常见场景，介绍如何基于AVPlayer系统播放器实现网络视频播放。本文指导开发者实现以下场景：

* [通过URL设置视频源](avplayer-network-video.md#通过url设置视频源)
* [网络视频缓冲条](avplayer-network-video.md#网络视频缓冲条)
* [网络视频边缓冲边播放](avplayer-network-video.md#网络视频边缓冲边播放)

通过AVPlayer实现视频资源加载、播放、暂停、停止、退出、倍速播放、静音播放、设置窗口缩放模式、音量调节等操作。详细信息可参考[《基于AVPlayer基础播控实践》](../best-practices/bpta-avplayer-basic-control.md)。焦点管理、弹幕发送与显示、画中画、横竖屏切换与旋转感知等场景可参考[《基于AVPlayer长视频播放实践》](avplayer-long-video.md)。

## 通过URL设置视频源

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/JIjWkbigSYu0IEgrShYmGQ/zh-cn_image_0000002736433737.gif)

使用AVPlayer开发播放功能时，需根据应用场景配置URL。AVPlayer主要用于播放网络流媒体资源，包括在线流媒体链接及本地M3U8流媒体文件。在线流媒体支持以下协议：

| 流媒体协议类型 | 典型链接 |
| --- | --- |
| HLS | https://xxxx/index.m3u8 |
| DASH | https://xxxx.mpd |
| HTTP/HTTPS | https://xxxx.mp4 |
| HTTP-FLV | https://xxxx.flv |

详情可参考[使用AVPlayer播放流媒体(ArkTS)](streaming-media-playback-development-guide.md)

本章节主要介绍如何配置HLS协议和HTTP/HTTPS协议的在线链接URL，以及如何设置本地M3U8文件和MP4文件的URL，以实现视频播放功能。

### 实现原理

AVPlayer通过URL形式配置播放源，有以下两种方式：

* 一种是直接设置AVPlayer的url属性，适用于不需要额外配置项的场景，例如下文的在线视频配置URL示例。
* 另一种是调用[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)函数通过URL创建播放源，然后调用[AVPlayer.setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法设置播放源，适用于需要额外配置媒体类型或者播放策略的场景，例如下文的本地M3U8文件配置URL示例。

### 开发步骤

1. 创建AVPlayer。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
       this.avPlayer = await media.createAVPlayer();
       // ...
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```
2. 设置AVPlayer的url属性，或者调用[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)函数通过URL创建播放源，并配置到AVPlayer，之后AVPlayer将自动进入initialized状态。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
       this.avPlayer = await media.createAVPlayer();
       this.setAVPlayerCallback();
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

       if (!this.context) {
         hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
         return
       }
       switch (this.curSource.type) {
         // ...
         case VideoDataType.URL:
           this.avPlayer.url = this.curSource.videoSrc;
           hilog.info(CommonConstants.LOG_DOMAIN, TAG,
             `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
           break;
         case VideoDataType.RAW_M3U8_FILE:
           let m3u8Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
           let fdUrl = 'fd://' + m3u8Fd.fd + '?offset=' + m3u8Fd.offset + '&size=' + m3u8Fd.length;
           let mediaSource = media.createMediaSourceWithUrl(fdUrl);
           mediaSource.setMimeType(media.AVMimeTypes.APPLICATION_M3U8);
           let playbackStrategy: media.PlaybackStrategy = { preferredBufferDuration: 20, showFirstFrameOnPrepare: true };
           await this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
           hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(fdUrl)}`);
           break;
         case VideoDataType.RAW_MP4_FILE:
           let mp4Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
           let mp4FdUrl = 'fd://' + mp4Fd.fd;
           this.avPlayer.url = mp4FdUrl;
           hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(mp4FdUrl)}`);
           break;

         default:
           hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed VideoDataType is invalid`);
           break;
       }
       await this.setCaption();
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```

## 网络视频缓冲条

### 场景描述

网络视频缓冲条是影音娱乐类应用中的典型场景之一，如用户播放在线视频时，缓冲条显示当前缓冲的可播放进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Fm6vFTxNT-y2NH53fpZgtA/zh-cn_image_0000002706834586.gif)

### 实现原理

本示例基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现在线视频播放，基于[Slider](../harmonyos-references/ts-basic-components-slider.md)实现视频播放和缓冲条显示。由于Slider没有多进度特性，这里使用[Stack](arkts-layout-development-stack-layout.md)布局，将缓冲条Slider和进度条Slider重叠显示，来实现缓冲进度和播放进度同时显示的效果。

其中缓冲条Slider的value值绑定由@State修饰的状态变量currentBufferTime，并通过注册[bufferingUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#onbufferingupdate9)事件处理函数，在该函数中获取已缓冲内容预计可播放时长，结合已播放时长得到当前缓冲进度。

**说明** 

由于bufferingUpdate事件的回调函数参数中，infoType为media.BufferingInfoType.CACHED\_DURATION时，value为已缓冲内容预计可播放时长，该值为预估值，所以缓冲进度亦为预估值，并不能保证百分百精准。bufferingUpdate事件的回调函数参数详情可参考[OnBufferingUpdateHandler](../harmonyos-references/arkts-apis-media-t.md#onbufferingupdatehandler12)。

### 开发步骤

1. 创建AVPlayer，并配置好相应的播放源。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
       this.avPlayer = await media.createAVPlayer();
       this.setAVPlayerCallback();
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

       if (!this.context) {
         hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
         return
       }
       switch (this.curSource.type) {
         // ...
         case VideoDataType.URL:
           this.avPlayer.url = this.curSource.videoSrc;
           hilog.info(CommonConstants.LOG_DOMAIN, TAG,
             `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
           break;
         // ...
       }
       await this.setCaption();
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```
2. 注册[timeUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#ontimeupdate9)事件处理函数，并在函数中更新由@State修饰的状态变量currentTime。

   ```typescript
   private setAVPlayerCallback() {
     // ...
     this.avPlayer.on('timeUpdate', (time: number) => {
       this.currentTime = time;
       AppStorage.setOrCreate('CurrentTime', time);
       hilog.info(CommonConstants.LOG_DOMAIN, TAG,
         `setAVPlayerCallback timeUpdate success,and new time is = ${this.currentTime}`);
     });
     // ...
   }
   ```
3. 注册[bufferingUpdate](../harmonyos-references/arkts-apis-media-avplayer.md#onbufferingupdate9)事件处理函数，并在函数中更新由@State修饰的状态变量currentBufferTime。

   ```typescript
   private setAVPlayerCallback() {
     // ...
     this.avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG,
         `BufferedProgressBar bufferingUpdate, infoType is ${infoType}, value is ${value}.`);
       // ...
       if (infoType === media.BufferingInfoType.CACHED_DURATION && this.avPlayer) {
         this.currentBufferTime = Math.max(this.currentBufferTime, this.currentTime + value);
         hilog.info(CommonConstants.LOG_DOMAIN, TAG, `currentBufferTime: ${this.currentBufferTime}`)
       }
     });

     // ...
   }
   ```
4. 绑定currentTime到播放Slider的value属性，绑定currentBufferTime到缓冲Slider的value属性，并利用[Stack](arkts-layout-development-stack-layout.md)布局将播放[Slider](../harmonyos-references/ts-basic-components-slider.md)和缓冲Slider重叠在一起，然后设置播放Slider的trackColor为透明，缓冲Slider的style属性设为SliderStyle.NONE以隐藏滑块。

   ```typescript
   @Builder
   progressBuilder() {
     Stack() {
       Slider({
         value: this.avPlayerController.currentTime,
         min: CommonConstants.SLIDER_PROGRESS_MIN,
         max: this.avPlayerController.durationTime,
         step: CommonConstants.SLIDER_PROGRESS_STEP,
         direction: Axis.Horizontal
       })
         .blockColor(Color.White)
         .trackColor($r('app.color.track_color_show'))
         .selectedColor($r('app.color.slider_selected'))
         .trackThickness(5)
         .zIndex(1)
         .onChange((value: number) => {
           this.avPlayerController.videoSeek(value);
         })

       Slider({
         value: this.avPlayerController.currentBufferTime,
         min: CommonConstants.SLIDER_PROGRESS_MIN,
         max: this.avPlayerController.durationTime,
         step: CommonConstants.SLIDER_PROGRESS_STEP,
         direction: Axis.Horizontal,
         style: SliderStyle.NONE
       })
         .trackColor(Color.Grey)
         .selectedColor(Color.White)
         .blockColor($r('app.color.track_color_show'))
         .trackThickness(5)
         .margin({ left: 12, right: 12 })
         .zIndex(0)
     }
     .layoutWeight(1)
   }
   ```

## 网络视频边缓冲边播放

### 场景描述

网络视频边缓冲边播放是影音娱乐类应用中的典型场景之一，如用户播放在线视频时，不用等待视频资源完全加载（缓冲）后再进行播放，可以缓冲到一定资源后，就可直接起播。AVPlayer自带边缓冲边播放的特性，本章节介绍AVPlayer缓冲区相关参数配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/U3BGlQsHR8eC7P3U20RAIg/zh-cn_image_0000002736313693.gif)

### AVPlayer缓冲区工作过程

对于缓冲区而言，下载线程是生产端，读取线程则是消费端。生产端将数据写入到缓冲区中，消费端则从缓冲区读取数据，下面将介绍缓冲区中的几个水位线概念。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/bwKAL-aBQB6XuG6_IHb8Tw/zh-cn_image_0000002706674650.png)

以上四个水位线取值情况如下，其中起播水位线和下载暂停水位线（缓冲区大小）可通过配置AVPlayer的播放策略来控制，其他两个暂未提供配置接口。

| 水位线 | 默认值 | 说明 |
| --- | --- | --- |
| 起播水位线 | 若下载速率 ≥ 码率场景，起播水位线取值：0.3秒 \* 码率  若下载速率 < 码率场景，起播水位线取值：5秒 \* 码率  若起播水位线小于10KB，取10KB | 在快速起播和顺滑播放间进行一个相对合理的分割。 |
| 止播水位线 | 单次读取数据量，若小于5KB则取5KB | 避免将缓冲区中的可用数据耗尽。 |
| 下载启动水位线 | 480KB | 降低线程启动频率，进行集中下载，降低cpu及指令数消耗。 |
| 下载暂停水位线 | 缓冲区大小 | 当缓冲区写满时，停止下载，支持修改。 |

起播水位线的默认值是根据下载速率确定，下载速率 >= 码率时，取值：0.3秒 \* 码率，即缓冲速度大于播放速度时，缓冲到0.3秒，开始播放；下载速率 < 码率时，起播水位线取值：5秒 \* 码率，即在缓冲内容累计满5秒后开始播放。这样可以在网络好的情况下快起播，减少用户等待时间，在网络差的情况下慢起播，避免播放和暂停状态间频繁来回切换，影响用户体验。若开发者不满足默认设置，可通过配置AVPlayer播放策略[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)来控制起播水位线。

下载暂停水位线是指已缓冲，但还未被消费（播放）数据最大占用空间，该值的大小依赖于缓冲区大小，可通过配置缓冲区大小间接控制该参数值。该值设置太小的话，在网络波动较大的环境，可能会影响视频播放的顺滑度；设置太大的情况下，一定程度会浪费用户网络资源。该参数默认为最大值20M，开发者可根据需要自行配置[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)中的preferredBufferDuration参数来控制缓冲区大小。preferredBufferDuration的单位为秒，缓冲区大小将被设定为preferredBufferDuration \* 1MB。例如，将preferredBufferDuration设为20秒，缓冲区大小将被设置为20MB。

| 默认缓冲区大小 | 用户自定义缓冲区大小 |
| --- | --- |
| 20MB | 5MB ~ 20MB |

起播水位线和下载暂停水位线（缓冲区大小）的配置方式均由AVPlayer的播放策略控制，播放策略的配置方式有两种：

* 一种是通过AVPlayer的[setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer，详情可参考[在线视频播放卡顿优化](online-video-playback-lags-optimize.md)。
* 另一种是通过AVPlayer的[setPlaybackStrategy()](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackstrategy12)方法将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer，第二种需要在AVPlayer状态为initialized或者stopped时，才可生效。

### 通过setMediaSource()方法配置

1. 创建AVPlayer，并通过[media.createMediaSourceWithUrl()](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)方法生成MediaSource实例。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
       this.avPlayer = await media.createAVPlayer();
       this.setAVPlayerCallback();
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

       if (!this.context) {
         hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
         return
       }
       switch (this.curSource.type) {
         // ...
         case VideoDataType.URL:
           this.avPlayer.url = this.curSource.videoSrc;
           hilog.info(CommonConstants.LOG_DOMAIN, TAG,
             `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
           break;
         // ...
       }
       await this.setCaption();
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```
2. 创建PlaybackStrategy实例，并通过AVPlayer的[setMediaSource()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法，将[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例配置进AVPlayer。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       // ...
       switch (this.curSource.type) {
         // ...
         case VideoDataType.RAW_M3U8_FILE:
           let m3u8Fd = await this.context.resourceManager.getRawFd(this.curSource.videoSrc);
           let fdUrl = 'fd://' + m3u8Fd.fd + '?offset=' + m3u8Fd.offset + '&size=' + m3u8Fd.length;
           let mediaSource = media.createMediaSourceWithUrl(fdUrl);
           mediaSource.setMimeType(media.AVMimeTypes.APPLICATION_M3U8);
           let playbackStrategy: media.PlaybackStrategy = { preferredBufferDuration: 20, showFirstFrameOnPrepare: true };
           await this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
           hilog.info(CommonConstants.LOG_DOMAIN, TAG, `initPlayer videoPlay fdUrl = ${JSON.stringify(fdUrl)}`);
           break;
         // ...
       }
       await this.setCaption();
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```

### 通过setPlaybackStrategy()方法配置

1. 创建AVPlayer，并直接通过赋值AVPlayer.url属性，对AVPlayer初始化。

   ```typescript
   public async initAVPlayer(source: VideoData, surfaceId: string) {
     // ...
     try {
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay avPlayerDemo');
       this.avPlayer = await media.createAVPlayer();
       this.setAVPlayerCallback();
       hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'initPlayer videoPlay setAVPlayerCallback');

       if (!this.context) {
         hilog.error(CommonConstants.LOG_DOMAIN, TAG, `initPlayer failed context not set`);
         return
       }
       switch (this.curSource.type) {
         // ...
         case VideoDataType.URL:
           this.avPlayer.url = this.curSource.videoSrc;
           hilog.info(CommonConstants.LOG_DOMAIN, TAG,
             `initPlayer videoPlay url = ${JSON.stringify(this.avPlayer.url)}`);
           break;
         // ...
       }
       await this.setCaption();
     } catch (err) {
       hilog.error(CommonConstants.LOG_DOMAIN, TAG,
         `initPlayer initPlayer, code is ${err.code}, message is ${err.message}`);
     }

   }
   ```
2. 注册AVPlayer的状态回调函数，并在initialized状态回调中配置[PlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)实例。

   ```typescript
   this.avPlayer.on('stateChange', async (state) => {
     if (!this.avPlayer) {
       return;
     }
     switch (state) {
       // ...
       case 'initialized':
         hilog.info(CommonConstants.LOG_DOMAIN, TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
         this.avPlayer.surfaceId = this.surfaceID;
         hilog.info(CommonConstants.LOG_DOMAIN, TAG,
           `setAVPlayerCallback this.avPlayer.surfaceId = ${this.avPlayer.surfaceId}`);
         await this.avPlayer.setPlaybackStrategy({
           preferredBufferDurationForPlaying: 0.3,
           preferredBufferDuration: 20,
           showFirstFrameOnPrepare: true
         });
         this.avPlayer.prepare();
         break;
       // ...
     }
   });
   ```

## 示例代码

* [基于AVPlayer播放网络视频实践](https://gitcode.com/harmonyos_samples/avplayer-online-video)
