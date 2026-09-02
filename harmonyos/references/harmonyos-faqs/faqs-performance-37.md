---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-37
title: 开启倒计时铃声播放，后台音乐播放不流畅
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 开启倒计时铃声播放，后台音乐播放不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8643090a98a5c3484daf45d41c90fc88c60cc3c4456ff46f2d7bff38bfb8eff6
---

## 问题现象

后台播放音乐时，开启应用的倒计时功能并打开铃声播放，后台音乐播放不流畅。

## 背景知识

* [SoundPool](../harmonyos-guides/media-kit-intro.md#soundpool)：提供短音频的播放能力，可用于实现一些短音效比如相机快门音效、系统通知音效等。当使用SoundPool播放短音频，且[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)指定为Music、Movie、AudioBook等类型，在播放短音频申请焦点时默认为并发模式，不会影响其他音频。
* 在播放音乐音频流（[STREAM\_USAGE\_MUSIC](../harmonyos-guides/using-right-streamusage-for-playback.md)）时如果有通知音频流（[STREAM\_USAGE\_NOTIFICATION](../harmonyos-guides/using-right-streamusage-for-playback.md)）播放，系统会降低正在播放的音乐音频流音量，通知音频流播放停止后，音乐音频流音量将恢复至原样。

## 问题定位

1. 在日志中搜索Renderer::Start|Renderer::Stop关键字查看应用播放音频的情况，可看到应用有频繁播放、暂停音频播放，streamType值为7，对应的[音频流使用类型](../harmonyos-references/arkts-apis-audio-e.md#streamusage)为通知音STREAM\_USAGE\_NOTIFICATION。

   ```screen
   07-29 11:43:35.646   29512-29730  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:35.710   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   07-29 11:43:36.650   29512-29731  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:36.727   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   07-29 11:43:37.649   29512-29732  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:37.731   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   07-29 11:43:38.650   29512-29733  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:38.729   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   07-29 11:43:39.650   29512-29729  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:39.730   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   07-29 11:43:40.651   29512-29730  C02B87/com.hm...AudioRenderer com.hm.example  I     [Start]StreamClientState for Renderer::Start. id: 100446, streamType: 7, volume: 1.000000, interruptMode: 0
   07-29 11:43:40.730   29512-29734  C02B87/com.hm...AudioRenderer com.hm.example  I     [Stop]StreamClientState for Renderer::Stop. id: 100446
   ```
2. .在日志中搜索SoundPool::Play看到有相关日志打印，应用有使用SoundPool播放音频，同时从上述分析得知音频流类型为通知音，可知打开铃声播放时，应用有频繁播放通知短音频，导致后台播放的音乐音量频繁降低、升高，播放不流畅。

   ```screen
   07-29 11:43:35.642   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:35.644   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   07-29 11:43:36.643   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:36.650   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   07-29 11:43:37.646   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:37.648   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   07-29 11:43:38.646   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:38.649   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   07-29 11:43:39.647   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:39.650   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   07-29 11:43:40.647   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #106 SoundPool::Play soundID::1 ,priority::0
   07-29 11:43:40.651   29512-49188  C02B2F/com.hm...ple/SoundPool com.hm.example  I     #117 SoundPool::Play streamID::2
   ```

## 分析结论

使用SoundPool频繁播放通知流类型短音频实现倒计时铃声提示音效，导致后台播放的音乐音量频繁降低、升高，播放不流畅。

## 修改建议

创建SoundPool实例时设置音频流使用类型为音乐。

```screen
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import common from '@ohos.app.ability.common';

@Entry
@Component
struct SoundPoolDemoPage {
  mediaSoundPool : media.SoundPool | undefined = undefined;

  soundId: number = 0;

  intervalNum: number = 0;

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
        console.info(`Succeeded in unloading ${this.soundId}`);
      }
    });
    // 释放音频池实例
    this.mediaSoundPool.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info(`Succeeded in releasing soundPool`);
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
        .onClick(() => {
          this.mediaSoundPool?.play(this.soundId, this.playParameters, (error: BusinessError, streamId: number) => {
            if (error) {
              console.error('play error');
              return;
            }
            console.info('play streamId:' + streamId);
          });
        })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
