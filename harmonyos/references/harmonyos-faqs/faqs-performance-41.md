---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-41
title: 多次点击按键，声音播放有延迟
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 多次点击按键，声音播放有延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:585b76f98081dccf76c1e7ebc5116b3d4257c36c90c76e3c46b828dcbf96d642
---

## 问题现象

在乐器模拟类应用中，点击不同的按键会发出不同的声音，当快速多次点击按键时，存在声音播放延迟的情况。

## 背景知识

* [SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#soundpool)：提供短音频的播放能力，应用只需要提供音频资源来源，不负责数据解析和解码就可达成播放效果。其相关接口函数如下：

  | 函数名 | 描述 |
  | --- | --- |
  | [load](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load) | 加载音频资源 |
  | [play](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#play) | 播放音频资源 |
  | [unload](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#unload) | 卸载音频资源 |
* 点击按键播放音频相关日志关键字如下：

  | 日志关键字 | 描述 |
  | --- | --- |
  | OnLoadCompleted received soundId:N | 音频资源加载完成，N表示音频ID |
  | SoundPool::Play soundID::N | 播放音频资源，N表示音频ID |
  | SoundPool::Unload soundID::N | 卸载音频资源，N表示音频ID |
  | Invalid sound. | 无效音频 |
  | play sound failed | 播放音频资源失败 |
  | touch test hitted | 触碰测试成功，点击事件被组件捕获 |

## 问题定位

1. 在日志中搜索Play soundID|Invalid sound.|play sound failed|touch test hitted日志关键字，如下所示，从日志中可看到点击事件被组件捕获和应用调用播放音频资源接口的时间间隔为40~80ms，无较大延迟，同时可看到前几次播放音频失败，提示无效音频。

   ```screen
   04-29 18:02:32.076 54620 54620 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:1071250, touch test hitted recognizer type info: ...
   04-29 18:02:32.140 54620 56255 I C02B2F/com.hm.example/SoundPool: SoundPool::Play soundID::74 ,priority::0
   04-29 18:02:32.140 54620 56255 E C02B2F/com.hm.example/SoundPool: Invalid sound.
   04-29 18:02:32.140 54620 56255 E C02B2B/com.hm.example/CommonNapi: SignError: play sound failed
   04-29 18:02:32.255 54620 54620 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:1071257, touch test hitted recognizer type info: ...
   04-29 18:02:32.337 54620 58738 I C02B2F/com.hm.example/SoundPool: SoundPool::Play soundID::75 ,priority::0
   04-29 18:02:32.337 54620 58738 E C02B2F/com.hm.example/SoundPool: Invalid sound.
   04-29 18:02:32.337 54620 58738 E C02B2B/com.hm.example/CommonNapi: SignError: play sound failed
   04-29 18:02:32.432 54620 54620 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:1071263, touch test hitted recognizer type info: ...
   04-29 18:02:32.476 54620 55406 I C02B2F/com.hm.example/SoundPool: SoundPool::Play soundID::76 ,priority::0
   04-29 18:02:32.476 54620 58722 E C02B2F/com.hm.example/SoundPool: Invalid sound.
   04-29 18:02:32.476 54620 58722 E C02B2B/com.hm.example/CommonNapi: SignError: play sound failed
   04-29 18:02:32.935 54620 54620 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:1071278, touch test hitted recognizer type info: ...
   04-29 18:02:32.976 54620 58358 I C02B2F/com.hm.example/SoundPool: SoundPool::Play soundID::109 ,priority::0
   ```
2. 在日志中搜索SoundPool::Unload soundID::|OnLoadCompleted查看音频资源加载、卸载的相关日志，从下方日志可看到前几次点击时播放的音频资源在点击之前已被卸载，音频播放失败，而最后一次点击播放时相应的音频资源加载完成，音频播放正常，导致声音播放延迟的现象。

   ```screen
   04-29 18:02:30.235 54620 58737 I C02B2F/com.hm.example/SoundPool: SoundPool::Unload soundID::74
   04-29 18:02:30.498 54620 58738 I C02B2F/com.hm.example/SoundPool: SoundPool::Unload soundID::75
   04-29 18:02:30.498 54620 58738 I C02B2F/com.hm.example/SoundPool: SoundPool::Unload soundID::76
   04-29 18:02:32.956 54620 59616 I C02B2F/com.hm.example/SoundPoolCallBackNapi: OnLoadCompleted received soundId:109
   ```

## 分析结论

多次点击按键时，前几次音频播放的相关资源已被卸载，播放失败，后续音频播放时资源已加载完成，播放正常，导致声音播放有延迟的现象。

## 修改建议

在播放音频资源时确保相应资源已加载，如进入页面时加载音频资源并缓存，退出页面时才卸载音频资源。

```screen
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import common from '@ohos.app.ability.common';

@Entry
@Component
struct DemoPage {
  mediaSoundPool : media.SoundPool | undefined = undefined;

  soundId: number = 0;

  playParameters: media.PlayParameters = {
    loop: 0, // 仅播放一次
    rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, //正常倍速
    leftVolume: 0.5, // 左声道音量
    rightVolume: 0.5, // 右声道音量
    priority: 1, // 优先级
  };

  initSound(): void {
    // 创建音频池实例
    media.createSoundPool(8, {
      usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
      rendererFlags: 0
    }, async (error: BusinessError, soundPool: media.SoundPool) => {
      if (error) {
        return;
      }
      this.mediaSoundPool = soundPool;
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let fileDescriptor = await context.resourceManager.getRawFd('1.AAC'); // 测试需要替换成可引用到的资源
      // 加载音频资源
      this.mediaSoundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length,
        (error: BusinessError, soundId: number) => {
          if (error) {
            console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
          } else {
            this.soundId = soundId;
            console.info('Succeeded in loading soundId:' + soundId);
          }
        });
    });
  }

  releaseSound(): void {
    if (!this.mediaSoundPool) {
      return;
    }
    // 卸载音频资源
    this.mediaSoundPool.unload(this.soundId, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to unload ${this.soundId}: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.log(`Succeeded in unloading ${this.soundId}`);
      }
    });
    // 释放音频池实例
    this.mediaSoundPool.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.log(`Succeeded in releasing soundPool`);
      }
    });
  }

  aboutToAppear(): void {
    this.initSound(); // 创建音频池实例、加载音频资源
  }

  aboutToDisappear(): void {
    this.releaseSound(); // 卸载音频资源、释放音频池实例
  }

  build() {
    RelativeContainer() {
      Button('播放声音')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 播放音频资源
          this.mediaSoundPool?.play(this.soundId, this.playParameters, (error: BusinessError, streamId: number) => {
            if (error) {
              console.error('play error');
              return;
            }
            console.info('play streamId:' + streamId);
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
