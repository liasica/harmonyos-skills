---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundpool-for-playback
title: 使用SoundPool播放短音频(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用SoundPool播放短音频(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:25+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:f0f762cfd4ee50dae852ec1a8d6ea1e53a0dd0919ac8f59d6c27bc71cdc3f3e7
---

使用[SoundPool](media-kit-intro.md#soundpool)（音频池）提供的接口，可以实现低时延短音播放。

当应用开发时，经常需要使用一些急促简短的音效（如相机快门音效、系统通知音效等），此时建议调用SoundPool，实现一次加载，多次低时延播放。

SoundPool当前支持播放解码后1MB以下的音频资源，解码后大小超过1MB的长音频将截取前面的1MB大小数据进行播放，这相当于44.1kHz的16bit位深的立体声下约5.6秒的音频时长（在较低采样率或单声道配置下，持续时间会相应延长）。

本开发指导将以SoundPool进行一次低时延播放音频的过程为例，向开发者讲解如何使用SoundPool。详细的API声明请参考[SoundPool (音频池)](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)。

过程包括：创建SoundPool实例，加载音频资源（包括资源的解封装与解码：解码格式参考[音频解码支持](audio-decoding.md)），设置播放参数（循环模式/播放优先级等），播放控制（播放/停止），释放资源。

在应用开发过程中，开发者应通过监听方法检查当前播放状态并按照一定顺序调用接口，执行对应操作，否则系统可能会抛出异常或生成其他未定义的行为。具体顺序可参考下列开发步骤及对应说明。

说明

使用SoundPool播放短音频时，涉及音频焦点管控策略的问题，请参考[音频焦点指南](audio-playback-concurrency.md)。

## 开发步骤及注意事项

1. 调用[createSoundPool](../harmonyos-references/arkts-apis-media-f.md#mediacreatesoundpool10-1)方法创建SoundPool实例。

   ```
   1. import { media } from '@kit.MediaKit';
   2. import { audio } from '@kit.AudioKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. private soundPool: media.SoundPool | undefined = undefined;
   6. // audioRenderInfo中的参数usage取值为STREAM_USAGE_UNKNOWN，STREAM_USAGE_MUSIC，STREAM_USAGE_MOVIE。
   7. // STREAM_USAGE_AUDIOBOOK时，SoundPool播放短音时为混音模式，不会打断其他音频播放。
   8. let audioRendererInfo: audio.AudioRendererInfo = {
   9. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
   10. rendererFlags: 1 // 音频渲染器标志。
   11. };

   13. // 创建soundPool实例。
   14. this.soundPool = await media.createSoundPool(14, audioRendererInfo); // 最大播放的流数为14。
   ```
2. 调用[on('loadComplete')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onloadcomplete)方法，用于监听“资源加载完成”。

   ```
   1. private soundId: number = 0;
   2. // 加载完成回调。
   3. this.soundPool!.on('loadComplete', (soundId_: number) => {
   4. this.soundId = soundId_;
   5. console.info('loadComplete soundId: ' + soundId_);
   6. })
   ```
3. 调用on('playFinished')或者on('playFinishedWithStreamId')方法，用于监听“播放完成”。

   当仅单独注册'playFinished'事件回调或者'playFinishedWithStreamId'事件回调时，当音频播放完成的时候，都会触发注册的回调。

   当同时注册'playFinished'事件回调和'playFinishedWithStreamId'事件回调时，当音频播放完成的时候，仅会触发'playFinishedWithStreamId'事件回调，不会触发'playFinished'事件回调。

   ```
   1. this.soundPool!.on('playFinished', () => {
   2. console.info("receive play finished message");
   3. // 可进行下次播放。
   4. });
   5. this.soundPool!.on('playFinishedWithStreamId', (streamId) => {
   6. console.info("receive play finished message, streamId: " + streamId);
   7. });
   ```
4. 调用on('error')方法，设置错误类型监听。

   ```
   1. this.soundPool!.on('error', (error: BusinessError) => {
   2. console.error('error happened,message is :' + error.code);
   3. console.error('error happened,message is :' + error.message);
   4. });
   ```
5. 调用load方法进行音频资源加载。

   可以传入uri或fd加载资源，此处使用传入fd的方式为例，更多方法请参考[API文档](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load)。

   当系统加载完毕音频资源文件的时候，会通过loadComplete回调，通知用户资源加载完成，请在收到回调之后，再进行后续的play操作。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. private soundId: number = 0;
   4. // 获取当前组件所在Ability的Context，以通过Context获取应用文件路径。
   5. let context = this.getUIContext().getHostContext();
   6. // 获取输入文件fd，test.ogg为rawfile目录下的预置资源，需要开发者根据实际情况进行替换。
   7. let fileDescriptor = await context!.resourceManager.getRawFd('test.ogg');
   8. this.soundId = await this.soundPool!.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
   9. console.info(`load soundPool soundId: ${this.soundId}`)
   ```
6. 配置播放参数PlayParameters，并在收到loadComplete回调通知之后，调用play方法播放音频。多次调用play播放同一个soundID，只会播放一次。

   ```
   1. private soundId: number = 0;
   2. private streamId: number = 0;
   3. let playParameters: media.PlayParameters = {
   4. loop: 1, // 循环1次，即播放2次。
   5. rate: 1, // 2倍速播放。
   6. leftVolume: 0.5, // 取值范围0.0-1.0。
   7. rightVolume: 0.5, // 取值范围0.0-1.0。
   8. priority: 0, // 最低优先级。
   9. };
   10. // 开始播放，调用play可携带播放参数PlayParameters。请在音频资源加载完毕，即收到loadComplete回调之后再执行play操作。
   11. this.soundPool!.play(this.soundId, playParameters, (error, streamID: number) => {
   12. if (error) {
   13. console.error(`play sound Error: errCode is ${error.code}, errMessage is ${error.message}`)
   14. } else {
   15. this.streamId = streamID;
   16. console.info('play success soundId:' + this.streamId);
   17. }
   18. });
   ```
7. 调用setLoop方法设置循环次数。

   ```
   1. // 设置循环播放次数。
   2. await this.soundPool!.setLoop(this.streamId, 2); // 播放3次。
   ```
8. 调用setPriority方法设置优先级。

   ```
   1. // 设置对应流的优先级。
   2. await this.soundPool!.setPriority(this.streamId, 1);
   ```
9. 调用setVolume方法设置音量。

   ```
   1. // 设置音量。
   2. await this.soundPool!.setVolume(this.streamId, 0.5, 0.5);
   ```
10. 调用stop方法终止指定流的播放。

    ```
    1. // 终止指定流的播放。
    2. await this.soundPool!.stop(this.streamId);
    ```
11. 调用unload方法卸载音频资源。

    ```
    1. // 卸载音频资源。
    2. await this.soundPool!.unload(this.soundId);
    ```
12. 调用off('loadComplete')方法注销加载完成监听。

    ```
    1. await this.soundPool!.off('loadComplete');
    ```
13. 调用off('playFinished')方法注销播放完成监听。

    ```
    1. await this.soundPool!.off('playFinished');
    ```
14. 调用off('error')方法注销错误类型监听。

    ```
    1. await this.soundPool!.off('error');
    ```
15. 调用release方法释放SoundPool实例。

    ```
    1. // 释放SoundPool。
    2. await this.soundPool!.release();
    ```

## 运行示例工程

参考以下示例，使用SoundPool进行低时延播放。

1. 新建工程，下载[完整示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/SoundPool/SoundPoolArkTS)，并将示例工程的资源复制到对应目录。

   ```
   1. SoundPoolArkTS
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
   12. │
   13. └── rawfile
   14. └── test.ogg (音频资源)
   ```
2. 编译新建工程并运行。
