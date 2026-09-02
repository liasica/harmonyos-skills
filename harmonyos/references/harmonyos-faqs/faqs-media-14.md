---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-14
title: 切换音频后快速点击播放按钮，播放的是切换前的音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 切换音频后快速点击播放按钮，播放的是切换前的音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:35018c0c54273bf7138b0ee3f5c346e06c7ca6bd1f0b2b56518e471d0072554b
---

## 问题现象

从音频A切换到音频B后，立即点击播放按钮，有概率出现仍播放音频A的现象。

## 背景知识

* [SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)：SoundPool音频池提供了短音频的加载、播放、音量设置、循环设置、停止播放、资源卸载等功能。
* SoundPool音频池提供了[load](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load)方法，通过**异步方式**加载音频资源。

## 问题定位

1. **记录音频A（切换前）的资源id：**

   SoundPool.load方法加载完成后，回调函数中会提供音频的资源id作为参数。具体如下代码所示：

   ```ts
       soundPool.load(uri, (error: BusinessError, soundId_: number) => {
           // soundId_为加载的音频的资源id
         });
   ```

   在日志中查找关键字"OnLoadCompleted received soundId:"找到音频加载完成时打印的日志，例如："OnLoadCompleted received soundId:xx"。找到后记录下音频A对应的资源id。

   音频通过media.createSoundPool方法加载，该方法的参数maxStreams允许设置SoundPool实例的最大播放音频流个数（范围1-32）。当maxStreams设置为n（1≤n≤32）时，会加载n个不一样的资源id。

   所以若查找关键字"OnLoadCompleted received soundId:"时找到多个不同的音频资源id，都需要作为音频A对应的资源id记录下来。
2. **记录切换音频B后实际播放的资源id：**

   切换到音频B后快速点击播放按钮，然后在日志中查找关键字"SoundPool::Play soundID::"，记录切换音频后播放的音频资源id，例如："SoundPool::Play soundID::xx"。

   注意：若日志中打印多个不同的音频资源id也要记录下来。

## 分析结论

若从音频A切换到音频B后，播放的资源id仍是音频A的资源id，则说明是由于音频异步加载未完成导致在音频B的状态下播放了音频A的声音。

## 修改建议

在加载新的音频时显示遮罩或灰化播放按钮来阻止用户点击播放按钮，当加载完成后再隐藏遮罩或取消灰化播放按钮。

参考代码：

```ts
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

@Entry
@Component
struct Index {
  @State buttonEnabled: boolean = true;
  private soundPool: media.SoundPool | undefined = undefined;
  private soundId: number = 0;
  private streamId: number = 0;

  async aboutToAppear(): Promise<void> {
    this.create();
  }

  build() {
    RelativeContainer() {
      Row() {
        Button('播放')
          .width(100)
          .height(100)
          .onClick(() => {
            this.PlaySoundPool();
          })
          .enabled(this.buttonEnabled)
          .id('playSoundPoolButton')
          .type(ButtonType.Circle)
        Button('切换')
          .width(100)
          .height(100)
          .onClick(() => {
            this.changeSound();
          })
          .id('playSoundPoolButton')
          .type(ButtonType.Circle)
      }.alignRules({
        center: { anchor: '__container__', align: VerticalAlign.Center },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
    }
    .height('100%')
    .width('100%')
  }

  async create() {
    try {
      let audioRendererInfo: audio.AudioRendererInfo = {
        usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
        rendererFlags: 1 // 音频渲染器标志。
      };
      //创建soundPool实例。
      this.soundPool = await media.createSoundPool(14,audioRendererInfo);

      // 加载音频资源。
      let context = this.getUIContext().getHostContext();
      let fileDescriptor = await context!.resourceManager.getRawFd('test.ogg'); // 替换成实际文件
      this.soundId = await this.soundPool!.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
      console.info(`load soundPool soundId: ${this.soundId}`);
    } catch (e) {
      console.error('createSoundPool error: ' + e);
    }
  }

  async PlaySoundPool() {
    let playParameters: media.PlayParameters = {
      loop: 1, // 循环1次，即播放2次。
      rate: 1, // 1倍速播放。
      leftVolume: 0.5, // 取值范围0.0-1.0。
      rightVolume: 0.5, // 取值范围0.0-1.0。
      priority: 0, // 最低优先级。
    };
    // 开始播放，这边play也可带播放的参数PlayParameters，请在音频资源加载完毕，即收到loadComplete回调之后再执行play操作。
    this.soundPool!.play(this.soundId, playParameters, (error, streamID: number) => {
      if (error) {
        console.error(`play sound Error: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        this.streamId = streamID;
        console.info('play success soundid:' + this.streamId);
      }
    });
  }

  async changeSound() {
    // 加载音频时显示遮罩
    this.buttonEnabled = false;
    // 加载新音频
    let context = this.getUIContext().getHostContext();
    let fileDescriptor = await context!.resourceManager.getRawFd('test2.ogg'); // 替换成实际文件
    this.soundId = await this.soundPool!.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
    this.soundPool!.on('loadComplete', () => {
      // 加载完成关闭遮罩
      this.buttonEnabled = true;
    });
  }
}
```
