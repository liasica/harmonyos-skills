---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-44
title: 快速多次点击按键，声音播放有卡顿的情况
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 快速多次点击按键，声音播放有卡顿的情况
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b0f94b9262911fa25cfe9ae163d9f4e8528acd483676ddd6266e43b180bb28de
---

## 问题现象

在乐器模拟类应用中，点击不同的按键会发出不同的声音，当快速多次点击按键时，存在声音播放卡顿的情况。

## 背景知识

[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#soundpool)：提供短音频的播放能力，应用只需要提供音频资源来源，不负责数据解析和解码就可达到播放效果。其提供的接口函数如下：

| 函数名 | 描述 |
| --- | --- |
| [load](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load) | 加载音频资源 |
| [play](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#play) | 播放音频资源 |
| [stop](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#stop) | 停止播放音频资源 |
| [setVolume](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#setvolume) | 设置音频流播放音量 |
| [unload](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#unload) | 卸载音频资源 |

## 问题定位

1. 在日志中搜索SoundPool::Play|SoundPool::SetVolume，查看点击两次按键时应用播放音频资源、设置播放音量的情况，如下可以看到应用播放音频资源两次，多次设置播放音量，由于播放音量变化无规律，变大又变小，导致音量忽高忽低，出现卡顿的情况。

   ```ts
   07-18 15:48:58.598   3033-6630    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::Play soundID::1 ,priority::1
   07-18 15:48:58.600   3033-6630    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::Play streamID::1
   07-18 15:48:58.631   3033-6631    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.950000, rightVolume:0.950000
   07-18 15:48:58.662   3033-6269    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.900000, rightVolume:0.900000
   07-18 15:48:58.693   3033-6617    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.850000, rightVolume:0.850000
   07-18 15:48:58.724   3033-6618    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.800000, rightVolume:0.800000
   07-18 15:48:58.753   3033-4149    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.750000, rightVolume:0.750000
   07-18 15:48:58.766   3033-6622    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::Play soundID::1 ,priority::1
   07-18 15:48:58.766   3033-6622    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::Play streamID::1
   07-18 15:48:58.783   3033-6619    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.700000, rightVolume:0.700000
   07-18 15:48:58.798   3033-6621    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.950000, rightVolume:0.950000
   07-18 15:48:58.814   3033-6623    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.650000, rightVolume:0.650000
   07-18 15:48:58.830   3033-6620    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.900000, rightVolume:0.900000
   07-18 15:48:58.845   3033-6624    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.600000, rightVolume:0.600000
   07-18 15:48:58.859   3033-6625    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.850000, rightVolume:0.850000
   07-18 15:48:58.875   3033-6628    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.550000, rightVolume:0.550000
   07-18 15:48:58.889   3033-6629    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.800000, rightVolume:0.800000
   07-18 15:48:58.905   3033-6630    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.500000, rightVolume:0.500000
   07-18 15:48:58.920   3033-6631    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.750000, rightVolume:0.750000
   07-18 15:48:58.935   3033-6269    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.450000, rightVolume:0.450000
   07-18 15:48:58.951   3033-6617    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.700000, rightVolume:0.700000
   07-18 15:48:58.966   3033-6618    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.400000, rightVolume:0.400000
   07-18 15:48:58.982   3033-4149    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.650000, rightVolume:0.650000
   07-18 15:48:58.997   3033-6622    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.350000, rightVolume:0.350000
   07-18 15:48:59.013   3033-6619    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.600000, rightVolume:0.600000
   07-18 15:48:59.028   3033-6621    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.300000, rightVolume:0.300000
   07-18 15:48:59.045   3033-6623    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.550000, rightVolume:0.550000
   07-18 15:48:59.060   3033-6620    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.250000, rightVolume:0.250000
   07-18 15:48:59.075   3033-6624    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.500000, rightVolume:0.500000
   07-18 15:48:59.089   3033-6625    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.200000, rightVolume:0.200000
   07-18 15:48:59.106   3033-6628    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.450000, rightVolume:0.450000
   07-18 15:48:59.120   3033-6629    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.150000, rightVolume:0.150000
   07-18 15:48:59.136   3033-6630    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.400000, rightVolume:0.400000
   07-18 15:48:59.152   3033-6631    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.100000, rightVolume:0.100000
   07-18 15:48:59.167   3033-6269    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.350000, rightVolume:0.350000
   07-18 15:48:59.182   3033-6617    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.050000, rightVolume:0.050000
   07-18 15:48:59.196   3033-6618    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.300000, rightVolume:0.300000
   07-18 15:48:59.228   3033-6622    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.250000, rightVolume:0.250000
   07-18 15:48:59.258   3033-6619    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.200000, rightVolume:0.200000
   07-18 15:48:59.287   3033-6621    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.150000, rightVolume:0.150000
   07-18 15:48:59.318   3033-6623    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.100000, rightVolume:0.100000
   07-18 15:48:59.349   3033-6620    C02B2F/com.exa...ion/SoundPool com.examp...lication  I     SoundPool::SetVolume streamID:1, leftVolume:0.050000, rightVolume:0.050000
   ```
2. 根据上述日志情况可在代码中搜索setVolume确认是否存在多次设置音量的情况，从以下示例可看到在播放音频资源时有调用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)设置的重复定时任务，设置不同的音量值，当音频未播放完时点击按钮会设置较高的音量值，引起音量跳变。

   ```ts
   import { media } from '@kit.MediaKit';
   import { audio } from '@kit.AudioKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   class VolumeController {
     streamId: number = 0;
     soundId: number = 0;
     duration: number = 0;
     interval: number = 0;
     volume: number = 0;
     soundPool : media.SoundPool | undefined = undefined;
     intervalNum: number = 0;
     volumeUnit: number = 0;

     constructor(streamId: number, soundId: number, duration: number, interval: number,
       soundPool : media.SoundPool | undefined = undefined, volume: number) {
       this.streamId = streamId;
       this.soundId = soundId;
       this.duration = duration;
       this.interval = interval;
       this.volume = volume;
       this.volumeUnit = volume / ( duration / interval );
       this.soundPool = soundPool;
     }

     start() {
       this.intervalNum = setInterval(() => {
         this.duration = this.duration - this.interval;
         if (this.duration <= 0) {
           // 当播放结束时，停止播放并清除定时器
           this.soundPool?.stop(this.streamId);
           clearInterval(this.intervalNum);
         } else {
           // 每次将音量减少一个volumeUnit单位
           this.volume = this.volume - this.volumeUnit;
           this.soundPool?.setVolume(this.streamId, this.volume, this.volume);
         }
       }, this.interval);
     }

     stop() {
       clearInterval(this.intervalNum);
     }
   }

   @Entry
   @Component
   struct VolumeControllerPage {
     soundPool : media.SoundPool | undefined = undefined;
     soundId: number = 0;
     streamId: number = 0;
     context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     playParameters: media.PlayParameters = {
       loop: 0, // 循环3次。
       rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
       leftVolume: 0.5,
       rightVolume: 0.5,
       priority: 1, // 最低优先级。
     };
     volumeController?: VolumeController;

     aboutToAppear(): void {
       media.createSoundPool(8, {
         usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
         rendererFlags: 0
       }, async (error: BusinessError, soundPool_: media.SoundPool) => {
         if (error) {
           return;
         }
         this.soundPool = soundPool_;
         let fileDescriptor = await this.context.resourceManager.getRawFd('50.AAC'); // 50.AAC为测试的音频文件，可替换
         this.soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length,
           (error: BusinessError, soundId_: number) => {
           if (error) {
             console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
           } else {
             this.soundId = soundId_;
             console.info(`Succeeded in loading soundId: ${soundId_}`);
           }
         });
       });
     }

     build() {
       Column({ space: 15 }) {
         Button('播放声音')
           .onClick(() => {
             // 点击播放
             this.soundPool?.play(this.soundId, this.playParameters, (error: BusinessError, streamId: number) => {
               if (error) {
                 console.error('play error');
                 return;
               }
               console.info(`play streamId: ${streamId}`);
               this.streamId = streamId;
               this.volumeController = new VolumeController(this.streamId, this.soundId, 600, 30, this.soundPool, 1);
               this.volumeController.start();
             });
           })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```

## 分析结论

快速点击按键播放音频资源时，有多次设置播放音量，播放音量变化无规律，变大又变小，导致音量忽高忽低，出现卡顿的情况。

## 修改建议

1. 使用音量有变化的音频资源，避免多次修改音量。
2. 缩短修改音量的定时器任务的总时长，在定时器未执行完成前，不播放新的音频资源。

   ```ts
   import { media } from '@kit.MediaKit';
   import { audio } from '@kit.AudioKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   class VolumeController {
     streamId: number = 0;
     soundId: number = 0;
     duration: number = 0;
     interval: number = 0;
     volume: number = 0;
     soundPool: media.SoundPool | undefined = undefined;
     intervalNum: number = 0;
     volumeUnit: number = 0;
     isStop: boolean = true;

     constructor(streamId: number, soundId: number, duration: number, interval: number,
       soundPool: media.SoundPool | undefined = undefined, volume: number) {
       this.streamId = streamId;
       this.soundId = soundId;
       this.duration = duration;
       this.interval = interval;
       this.volume = volume;
       this.volumeUnit = volume / (duration / interval);
       this.soundPool = soundPool;
     }

     start() {
       this.isStop = false;
       this.intervalNum = setInterval(() => {
         this.duration = this.duration - this.interval;
         if (this.duration <= 0) {
           // 当播放结束时，停止播放并清除定时器
           this.soundPool?.stop(this.streamId);
           clearInterval(this.intervalNum);
           this.isStop = true;
         } else {
           // 每次将音量减少一个volumeUnit单位
           this.volume = this.volume - this.volumeUnit;
           this.soundPool?.setVolume(this.streamId, this.volume, this.volume);
         }
       }, this.interval);
     }

     stop() {
       this.isStop = true;
       clearInterval(this.intervalNum);
     }
   }

   @Entry
   @Component
   struct VolumeControllerPage {
     soundPool: media.SoundPool | undefined = undefined;
     soundId: number = 0;
     streamId: number = 0;
     context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     playParameters: media.PlayParameters = {
       loop: 0, // 循环3次。
       rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
       leftVolume: 0.5,
       rightVolume: 0.5,
       priority: 1, // 最低优先级。
     };
     volumeController?: VolumeController;

     aboutToAppear(): void {
       media.createSoundPool(8, {
         usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
         rendererFlags: 0
       }, async (error: BusinessError, soundPool_: media.SoundPool) => {
         if (error) {
           return;
         }
         this.soundPool = soundPool_;
         let fileDescriptor = await this.context.resourceManager.getRawFd('50.AAC'); // 50.AAC为测试的音频文件，可替换
         this.soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length,
           (error: BusinessError, soundId_: number) => {
             if (error) {
               console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
             } else {
               this.soundId = soundId_;
               console.info(`Succeeded in loading soundId: ${soundId_}`);
             }
           });
       });
     }

     build() {
       Column({ space: 15 }) {
         Button('播放声音')
           .onClick(() => {
             // 使用isStop变量，控制定时器未执行完成前，不播放新的音频资源
             if (!this.volumeController || this.volumeController?.isStop) {
               this.soundPool?.play(this.soundId, this.playParameters, (error: BusinessError, streamId: number) => {
                 if (error) {
                   console.error('play error');
                   return;
                 }
                 console.info(`play streamId: ${streamId}}`);
                 this.streamId = streamId;
                 this.volumeController = new VolumeController(this.streamId, this.soundId, 600, 30, this.soundPool, 1);
                 this.volumeController.start();
               });
             }
           })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
