---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-subtitle
title: 使用AVPlayer添加视频外挂字幕(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer添加视频外挂字幕(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7ecfdb8a44fa384d8f3b317fc084e1bdd5ec4e9fdfb271b826dbee57a2d0afa7
---

当前仅支持视频播放前设置外挂字幕。

在进行应用开发的过程中，开发者可以通过AVPlayer的实例注册on('subtitleUpdate')方法监听字幕信息。

## 开发步骤及注意事项

详细的API说明请参考[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)

1. 调用[addSubtitleFromFd](../harmonyos-references/arkts-apis-media-avplayer.md#addsubtitlefromfd12)，使用视频播放的AVPlayer实例设置外挂字幕资源。

   ```
   1. import { media } from '@kit.MediaKit';
   2. import { common } from '@kit.AbilityKit';
   3. // 类成员定义avPlayer和context。
   4. private avPlayer: media.AVPlayer | null = null;
   5. private context: common.UIAbilityContext | undefined = undefined;

   7. // 在业务函数中（示例工程函数名为avSetupVideoAndSubtitle）：
   8. // 创建avPlayer实例对象。
   9. this.avPlayer = await media.createAVPlayer();
   10. this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   11. // 设定视频源（此处省略）。

   13. // 设定字幕。
   14. let fileDescriptorSub = await this.context?.resourceManager.getRawFd('xxx.srt');
   15. this.avPlayer.addSubtitleFromFd(fileDescriptorSub.fd, fileDescriptorSub.offset, fileDescriptorSub.length);
   ```
2. 调用[on('subtitleUpdate')](../harmonyos-references/arkts-apis-media-avplayer.md#onsubtitleupdate12)接口，注册字幕回调函数。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 类成员定义用来显示的字幕字符串。
   3. @State subtitle: string = 'subtitleUpdate info';
   4. private avPlayer: media.AVPlayer | null = null;
   5. private tag: string = '';

   7. // 创建avPlayer实例对象。
   8. this.avPlayer = await media.createAVPlayer();
   9. // 字幕回调函数。
   10. this.avPlayer.on('subtitleUpdate', (info: media.SubtitleInfo) => {
   11. if (!!info) {
   12. let text = (!info.text) ? '' : info.text;
   13. let startTime = (!info.startTime) ? 0 : info.startTime;
   14. let duration = (!info.duration) ? 0 : info.duration;
   15. console.info(`${this.tag}: text=${text} startTime=${startTime} duration=${duration}`);
   16. this.subtitle = text;
   17. } else {
   18. console.info(`${this.tag}: subtitleUpdate info is null`);
   19. }
   20. });
   ```
3. (可选)当需要不显示字幕的时候，使用视频播放的AVPlayer实例注销字幕回调函数。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 类成员定义avPlayer和context。
   3. private avPlayer: media.AVPlayer | null = null;
   4. // 创建avPlayer实例对象。
   5. this.avPlayer = await media.createAVPlayer();
   6. this.avPlayer?.off('subtitleUpdate');
   ```

## 运行完整示例

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSSubtitle)，并将示例工程的以下资源复制到对应目录。

   ```
   1. AVPlayerArkTSSubtitle
   2. entry/src/main/ets/
   3. └── pages
   4. └── Index.ets (播放界面)
   5. entry/src/main/resources/
   6. ├── base
   7. │   ├── element
   8. │   │   ├── color.json
   9. │   │   ├── float.json
   10. │   │   └── string.json
   11. │   └── media
   12. │       ├── ic_video_play.svg  (播放键图片资源)
   13. │       └── ic_video_pause.svg (暂停键图片资源)
   14. └── rawfile
   15. ├── test1.mp4 （视频资源）
   16. └── test1.srt （字幕资源）
   ```
2. 编译新建工程并运行。
