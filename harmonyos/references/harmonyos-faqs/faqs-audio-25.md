---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-25
title: 静音模式下有提示音
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 静音模式下有提示音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d69b1dcbf5c9e5c50ee79b74b38f140776a85e297132bcb2208f4d5f80830570
---

## 问题现象

手机设置成静音模式，应用仍会有提示音。

## 背景知识

音频流是指音频系统中一个具备音频格式和音频使用场景信息的独立音频数据处理单元。可以表示播放，也可以表示录制，并且具备独立音量调节和音频设备路由切换能力。对于播放流，其类型由[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)确定；对于录制流，则由[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)决定。

* 音频流类型在音量控制、音频焦点管理、输入/输出设备选择等方面有决定性影响。
* 应用需要根据自身的业务场景和实际需求，[使用合适的音频流类型](../harmonyos-guides/using-right-sourcetype-for-recording.md)。

## 问题定位

查看日志，搜索关键字StreamUsage，查看应用使用的音频流类型。如下面日志所示，应用设置的StreamUsage值为4，对应音频流类型为闹钟。当StreamUsage的值不为6（铃声）或7（通知音）时，在设备处于静音模式下，系统仍会发出提示音。仅当StreamUsage为6或7时，在静音模式下不会播放提示音。

```txt
03-06 16:38:15.457   782-2437      C02B85/audio_server/AudioEffectChain      audio_server      I     [SetEffectParamToHandle]set param to handle, sceneType: 5, effectMode: 1, rotation: 0, volume: 700, extraSceneType: 0, spatialDeviceType: 5, spatializationSceneType: 1, spatializationEnabled: 0, streamUsage: 4,absVolumeState = 1
```

## 分析结论

应用设置了错误的音频流类型。例如，闹钟类型的音频流在静音模式下仍会有提醒，不符合用户预期。

## 修改建议

根据业务场景使用合适的音频流。设置音频流类型为STREAM\_USAGE\_RINGTONE（铃声类型）或STREAM\_USAGE\_NOTIFICATION（通知音），静音模式下应用将不会发出提示音。

```ts
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct NotificationSoundPlayer {
  private soundPool: media.SoundPool | undefined = undefined;
  private soundId: number = -1;

  // 创建SoundPool实例并加载音频
  async initSoundPool() {
    try {
      // 设置音频流类型为铃声或通知音，仅当usage设置为STREAM_USAGE_RINGTONE和STREAM_USAGE_NOTIFICATION时可以实现静音
      const audioRendererInfo: audio.AudioRendererInfo = {
        usage: audio.StreamUsage.STREAM_USAGE_RINGTONE, // 设置为铃声类型
        rendererFlags: 0
      };

      // 创建SoundPool实例（最大并发数8）
      this.soundPool = await media.createSoundPool(8, audioRendererInfo);

      // 注册音频加载完成回调
      this.soundPool.on('loadComplete', (soundId: number) => {
        this.soundId = soundId;
        console.info(`Sound loaded ID: ${soundId}`);
      });

      // 从资源文件加载音频
      const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileDescriptor =
        await context.resourceManager.getRawFd('notification.mp3'); // 此处'notification'仅作示例，请开发者自行替换

      this.soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
    } catch (error) {
      console.error(`Init failed: ${(error as BusinessError).message}`);
    }
  }

  // 播放提示音
  playNotification() {
    if (!this.soundPool || this.soundId === -1) {
      return;
    }

    const playParams: media.PlayParameters = {
      loop: 0, // 不循环
      rate: audio.AudioRendererRate.RENDER_RATE_NORMAL,
      leftVolume: 1.0, // 左声道音量
      rightVolume: 1.0, // 右声道音量
    };

    try {
      this.soundPool.play(this.soundId, playParams);
    } catch (error) {
      console.error(`Play failed: ${(error as BusinessError).message}`);
    }
  }

  // 组件初始化时加载音频
  aboutToAppear() {
    this.initSoundPool();
  }

  // 组件销毁时释放资源
  aboutToDisappear() {
    this.soundPool?.release();
  }

  build() {
    Column() {
      Button('播放提示音')
        .onClick(() => this.playNotification())
        .margin(20)
    }
  }
}
```
