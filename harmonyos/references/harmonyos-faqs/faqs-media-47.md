---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-47
title: 媒体服务报错5400102问题定位
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 媒体服务报错5400102问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dd9decbd0a3418c80e1437de564a1b8a47a5b14f4eb592e7e74fe2b88e5aba84
---

## 问题现象

使用Media Kit（媒体服务）提供的模块（AVPlayer、SoundPool）开发音视频播放功能时报错5400102，Operate Not Permit。本文介绍该类错误的排查思路。

## 背景知识

* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)提供功能完善一体化播放能力，应用只需提供流媒体来源，不负责数据解析和解码就可达成播放效果。
* [SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)提供短音频的播放能力，应用只需要提供音频资源来源，不负责数据解析和解码就可达成播放效果。
* [5400102-当前状态不支持此操作](../harmonyos-references/errorcode-media.md#section5400102-当前状态不支持此操作)：当前状态不支持此操作，需要把实例切换到正确的状态进行正确的操作。

## 问题定位

使用AVPlayer、SoundPool开发音视频播放功能时，必须按照一定的顺序调用接口，执行对应操作。如果没有在对应的状态下执行操作，系统将会抛出异常（5400102，Operate Not Permit）或产生其他未定义的行为。

可以通过AVPlayer、SoundPool的API参考获取每个接口调用时的状态限制。AVPlayer可以通过的state[属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)主动获取当前状态，或使用[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)方法监听状态变化。SoundPool可以通过[on('loadComplete')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onloadcomplete)等监听方法检查当前播放状态。

常见的报错5400102的问题场景和原因如下：

1. AVPlayer播放沙箱文件，设置url[属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)时报错5400102。

   ```txt
   03-12 11:09:18.944   1519-1519     A03D00/com.hua...ication/JSAPP  com.huawe...lication  E     5400102, Operate Not Permit: failed to SetSourceFd
   ```

   ```ts
   async example(avPlayer: media.AVPlayer, videoFilePath: string) {
     let videoFile: fileIo.File | undefined = undefined;
       try {
         videoFile = await fileIo.open(videoFilePath, fileIo.OpenMode.READ_ONLY);
       } catch (error) {
         console.error(`${error.code}, ${error.message}`);
         return;
       } finally {
         await fileIo.close(videoFile); // 设置媒体资源前关闭文件
       }
       avPlayer.url = `fd://${videoFile.fd}`;
   }
   ```

   通过AVPlayer播放沙箱文件时，需要打开沙箱文件，并将资源句柄（fd）传递给AVPlayer。在整个播放过程中，必须确保资源句柄（fd）是已可读方式打开的。关闭文件后，资源句柄（fd）不再有实际意义，不能用于读写文件。将关闭的资源句柄（fd）设置给AVPlayer的url属性时，会报错5400102。
2. AVPlayer设置播放资源后，调用[prepare](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口准备播放报错5400102。

   ```txt
   03-12 11:11:22.779   3819-3819     A03D00/com.hua...ication/JSAPP  com.huawe...lication  E     5400102, current state is not stopped or initialized, unsupport prepare operation
   ```

   ```ts
   async example(avPlayer: media.AVPlayer, videoFilePath: string) {
     let videoFile: fileIo.File | undefined = undefined;
     try {
       videoFile = await fileIo.open(videoFilePath, fileIo.OpenMode.READ_ONLY);
       avPlayer.url = `fd://${videoFile.fd}`;
       await avPlayer.prepare(); // 设置媒体资源后立刻调用prepare
     } catch (error) {
       console.error(`${error.code}, ${error.message}`);
       return;
     }
   }
   ```

   AVPlayer的prepare接口需要在[stateChange](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)事件成功触发至initialized状态后，才能调用，否则会抛出异常5400102。需要注意的是，AVPlayer在设置播放资源后，不会立刻进入initialized状态，必须stateChange事件，确认AVPlayer成功进入initialized状态后才可以调用prepare接口准备播放。
3. SoundPool调用[load](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load)加载音频资源后，调用[play](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#play)开始播放报错5400102。

   ```txt
   03-12 11:16:18.518   7502-7502     A03D00/com.sam...olArkTS/JSAPP  com.sampl...oolArkTS  E     5400102, play sound failed
   ```

   ```ts
   async example(soundPool: media.SoundPool, uri: string) {
     try {
       let soundId = await soundPool.load(uri);
       await soundPool.play(soundId); // 在调用load完成后立刻调用play播放
     } catch (error) {
       console.error(`${error.code}, ${error.message}`);
     }
   }
   ```

   SoundPool的play接口需要在[loadComplete](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onloadcomplete)事件触发，音视频资源加载完成后，才能正常调用。调用load接口完成后，不代表音频资源加载完成，如果此时调用play接口开始播放会报错5400102。

## 分析结论

未按照正确的调用顺序调用接口，在当前播放状态下执行了不允许的操作，导致报错5400102。

## 修改建议

在调用接口执行相关操作前，需要检查当前的播放状态，确保在正确的状态下执行操作。
