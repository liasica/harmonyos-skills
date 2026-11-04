---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-subtitle
title: 使用AVPlayer添加视频外挂字幕(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer添加视频外挂字幕(ArkTS)
category: harmonyos-guides
scraped_at: 2026-11-04T08:30:13+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:7feb0144275988430791fb6c08d639fe70d9a5505b774c9bd2a8005d8f6ad84b
---

当前仅支持视频播放前设置外挂字幕。

在进行应用开发的过程中，开发者可以通过AVPlayer的实例注册on('subtitleUpdate')方法监听字幕信息。

## 开发步骤及注意事项

详细的API说明请参考[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)

1. 调用[addSubtitleFromFd](../harmonyos-references/arkts-apis-media-avplayer.md#addsubtitlefromfd12)，使用视频播放的AVPlayer实例设置外挂字幕资源。

   ```typescript
   // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
   // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
   if (this.context == undefined) return;
   let fileDescriptorVideo = await this.context.resourceManager.getRawFd(this.fileName);
   let avFileDescriptor: media.AVFileDescriptor =
     { fd: fileDescriptorVideo.fd, offset: fileDescriptorVideo.offset, length: fileDescriptorVideo.length };

   if (this.avPlayer) {
     console.info(`${this.tag}: init avPlayer release2createNew`);
     this.avPlayer.release();
     await this.msleepAsync(1500);
   }
   // 创建avPlayer实例对象。
   this.avPlayer = await media.createAVPlayer();

   // 创建状态机变化回调函数。
   await this.setAVPlayerCallback((avPlayer: media.AVPlayer) => {
     this.percent = avPlayer.width / avPlayer.height;
     this.setVideoWH();
     this.durationTime = this.getDurationTime();
     setInterval(() => { // 更新当前时间。
       if (!this.isSwiping) {
         this.currentTime = this.getCurrentTime();
       }
     }, SET_INTERVAL);
   });

   // 为fdSrc赋值触发initialized状态机上报。
   this.avPlayer.fdSrc = avFileDescriptor;

   // 设定字幕。
   let fileDescriptorSub = await this.context.resourceManager.getRawFd('test1.srt');
   this.avPlayer.addSubtitleFromFd(fileDescriptorSub.fd, fileDescriptorSub.offset, fileDescriptorSub.length);
   ```
2. 调用[on('subtitleUpdate')](../harmonyos-references/arkts-apis-media-avplayer.md#onsubtitleupdate12)接口，注册字幕回调函数。

   ```typescript
   // 字幕回调函数。
   this.avPlayer.on('subtitleUpdate', (info: media.SubtitleInfo) => {
     if (!!info) {
       let text = (!info.text) ? '' : info.text;
       let startTime = (!info.startTime) ? 0 : info.startTime;
       let duration = (!info.duration) ? 0 : info.duration;
       console.info(`${this.tag}: subtitleUpdate info: text=${text} startTime=${startTime} duration=${duration}`);
       this.subtitle = text;
     } else {
       console.info(`${this.tag}: subtitleUpdate info is null`);
     }
   });
   ```
3. (可选)当需要不显示字幕的时候，使用视频播放的AVPlayer实例注销字幕回调函数。

   ```typescript
   // (可选)当需要不显示字幕的时候，使用视频播放的AVPlayer实例注销字幕回调函数。
   async avTurnOffSubtitle() {
     this.avPlayer?.off('subtitleUpdate');
   }
   ```

## 运行完整示例

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSSubtitle)，并将示例工程的以下资源复制到对应目录。

   ```text
    AVPlayerArkTSSubtitle
    entry/src/main/ets/
    └── pages
        └── Index.ets (播放界面)
    entry/src/main/resources/
    ├── base
    │   ├── element
    │   │   ├── color.json
    │   │   ├── float.json
    │   │   └── string.json
    │   └── media
    │       ├── ic_video_play.svg  (播放键图片资源)
    │       └── ic_video_pause.svg (暂停键图片资源)
    └── rawfile
        ├── test1.mp4 （视频资源）
        └── test1.srt （字幕资源）
   ```
2. 编译新建工程并运行。
