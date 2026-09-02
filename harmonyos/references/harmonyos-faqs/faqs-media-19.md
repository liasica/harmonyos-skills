---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-19
title: 应用下发音频数据不及时导致音频卡顿或有杂音
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 应用下发音频数据不及时导致音频卡顿或有杂音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e718bd22ab470406a02f41bc6962f2645278853d65d923bde424fb6fdc4079c
---

## 问题现象

在使用应用中语音播放功能时，切换播放语音，同时又通过手势点击另一个播放语音时，音频播放混乱，且有pop音。

## 背景知识

[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#soundpool)（音频池）提供了短音频的加载、播放等功能。当应用开发时，经常需要使用一些急促简短的音效（如点击键盘、系统通知音效等），此时建议调用SoundPool，实现一次加载，多次低时延播放。

## 问题定位

获取问题发生时的hilog日志。下发音频数据不及时判定方法：

* 应用下发音频不及时判定：通过在hilog中查找tallyUnderrunFrames关键字来识别是否应用下发音频数据不及时，存在连续的该关键字打印。

  ```shell
  04-06 23:55:09.037   1874    1292 W AudioTrackShared::tallyUnderrunFrames(108) at uf = 24014, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(435) at uf = 24449, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(435) at uf = 24449, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(435) at uf = 24804, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(435) at uf = 24804, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(435) at uf = 24804, bump mNumberUnderrunCount for Id 
  04-06 23:55:09.038   1874    1292 W AudioTrackShared::tallyUnderrunFrames(13) at uf = 25877, bump mNumberUnderrunCount for Id 
  04-06 23:55:10.005   1874    1292 W AudioTrackShared::tallyUnderrunFrames(714) at uf = 27555, bump mNumberUnderrunCount for Id
  ```
* frk和hal下发数据不及时：应用下发音频数据不及时，在hilog中查找writing block|write data cost|underrun关键字来识别。正常耗时60ms左右，日志如下：

  ```shell
  15:32:08.611  14706 14762 I APolicyManager(): outputStop(), stream 13, session 482689, portId 2755

  15:32:08.611  14706 14981 W audio_hw_primary [out_write_1206]: write data cost : 57 ms 
  15:32:08.435  14706 14981 W audio_hw_primary [out_write_1206]: write data cost : 58 ms  
  15:32:08.696  14706 14981 W audio_hw_primary [out_write_1206]: write data cost : 55 ms   
  15:32:09.075  14706 14981 W audio_hw_primary [out_write_1206]: write data cost : 55 ms    
  15:32:09.235  14706 14981 W audio_hw_primary [out_write_1206]: write data cost : 55 ms
  ```

  观察hilog日志，查找write data cost关键字，发现有连续的打印write data cost，远超60ms左右时间，表明是应用写入数据写慢了，导致出现播放混乱。

  ```shell
  07-08 14:14:33.451  1372-35728 C@C2560/audio_h...io_hw_primary     audio_host          W      [out_write:1276] write data cost: 145 ms
  07-08 14:14:59.256  1372-35728 C@C2560/audio_h...io_hw_primary     audio_host          W       [out_write:1276] write data cost: 137 ms 
  07-08 14:15:52.458  1372-1409  C@C2560/audio_h...io_hw_primary     audio_host          W         [out_write:1276] write data cost: 97 ms
  07-08 14:17:40.249  1372-35727 C@C2560/audio_h...io_hw-primary     audio_host          W         [out_write:1276] write data cost: 127 ms
  07-08 14:17:54.813  1372-1409  C@C2560/audio_h..iow_hw_primary     audio_host          W         [out_write:1276] write data cost: 133 ms
  ```

## 分析结论

由于应用下发音频数据不及时导致出现卡顿问题。

## 修改建议

针对连续快速下发两次音频时出现的pop音问题，已知底层音频处理采用了淡入淡出效果，并且音频播放限于单一路流的原则。基于此现状，提出以下优化方案以提升用户体验和系统稳定性：

* 集成防抖逻辑以平滑音频下发频率：

  实施策略应考虑将两次连续的音频下发合并在一次指令中，以此避免短时间内对音频下发操作的频繁调用，进而缓解系统资源压力。建议根据应用实际下发音频数据的长度来调整下发频率间隔，适当延长这一间隔有助于优化音频处理过程。

  ```ts
  import { SoundPoolUtil } from './SoundPoolUtil';
  import { common } from '@kit.AbilityKit';

  // 防抖 在一段时间内函数被多次触发，防抖让函数在一段时间后最终只执行一次
  export function debounce(func: (event: ClickEvent) => void, delay?: number) {
    let timer: number;
    return (event: ClickEvent) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        func(event);
      }, delay ? delay : 1000);
    };
  }

  @Entry
  @Component
  struct Index {
    aboutToAppear(): void {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // 需在src/main/resources/resfile目录下预置对应音频文件
      let file = context.resourceDir + "/default.wav";
      const instance = SoundPoolUtil.getInstance();
      instance.init().then(() => {
        instance.loadSound(file);
      });
    }

    build() {
      Column({ space: 20 }) {
        Button("单次播放音频")
          .onClick(() => {
            // 按太快会有破音。
            this.play();
          });

        Button("模拟连续点击2次播放按钮")
          .onClick(() => {
            this.play();
            this.play();
          });

        // 按太快会有破音。正面是模拟快速调用的，直接调用两次
        Button("防抖函数：连续点击2次播放按钮")
          .onClick(() => {
            debounce((event) => {
              this.play();
              console.info(`防抖拦截 == ${event.displayX}`);
            }, 40);
            this.play();
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }

    play() {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // 需在src/main/resources/resfile目录下预置对应音频文件
      let file = context.resourceDir + "/default.wav";
      SoundPoolUtil.playSound(file, 1);
    }
  }
  ```
* 运用播放完成回调机制：

  引入SoundPool播放完成回调功能，即在上一路音频流的播放彻底完成后，再执行下一次音频流数据的下发动作。该机制能够确保各音频指令按序无误地执行，避免因未等前一音频播放结束就下发新音频而导致的音质问题（以下示例所用音频资源在实际使用可替换为已有资源）。

  ```ts
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { audio } from '@kit.AudioKit';
  import { media } from '@kit.MediaKit';

  export class SoundPoolUtil {
    private static instance: SoundPoolUtil | null = null;
    private soundPool: media.SoundPool | null = null;
    private soundMap: Map<string, number> = new Map();
    private streamMap: Map<number, number> = new Map();
    private currentPlayingKey: string | null = null;
    private isPlaying: boolean = false;

    // 初始化SoundPool
    async init() {
      const audioRendererInfo: audio.AudioRendererInfo = {
        usage: audio.StreamUsage.STREAM_USAGE_NOTIFICATION,
        rendererFlags: 0
      };

      try {
        this.soundPool = await media.createSoundPool(5, audioRendererInfo);
        this.registerListeners();
        console.info('SoundPool初始化成功');
      } catch (error) {
        console.error(`SoundPool初始化失败:  error.code: ${error.code}, error.message: ${error.message}`);
      }
    }

    private registerListeners() {
      if (!this.soundPool) {
        return;
      }

      this.soundPool.on('loadComplete', (soundId: number) => {
        console.info(`音频加载完成, soundId: ${soundId}`);
      });

      this.soundPool.on('playFinished', () => {
        console.info('音频播放完成');
        this.isPlaying = false;
        this.currentPlayingKey = null;
      });

      this.soundPool.on('error', (error) => {
        console.error(`发生错误: error.code: ${error.code}, error.message: ${error.message}`);
      });
    }

    // 加载音频
    async loadSound(filePath: string): Promise<number> {
      if (!this.soundPool) {
        return -1;
      }
      if (this.soundMap.get(filePath)) {
        console.warn(`已装载该音频，本次跳过装载。`);
        return -1;
      }
      try {
        let uri = "";
        await fs.open(filePath, fs.OpenMode.READ_ONLY).then((file: fs.File) => {
          console.info(`文件描述符: ${file.fd}`);
          uri = 'fd://' + (file.fd).toString();
        });
        const soundId = await this.soundPool.load(uri);
        this.soundMap.set(filePath, soundId);
        console.info(`音频加载成功: ${filePath}, soundId: ${soundId}`);
        return soundId;
      } catch (error) {
        console.error(`音频加载失败: error.code: ${error.code}, error.message: ${error.message}`);
        return -1;
      }
    }

    // 播放音频
    async play(key: string, params?: media.PlayParameters): Promise<number | undefined> {
      if (!this.soundPool) {
        return undefined;
      }

      // 如果当前正在播放同一个音频，直接返回
      if (this.isPlaying && this.currentPlayingKey === key) {
        console.warn(`当前已在播放，本次不播放。`);
        return undefined;
      }

      const soundId = this.soundMap.get(key);
      if (!soundId) {
        console.error(`未找到音频: ${key}`);
        return undefined;
      }

      const defaultParams: media.PlayParameters = {
        loop: 0,
        rate: audio.AudioRendererRate.RENDER_RATE_NORMAL,
        leftVolume: 1.0,
        rightVolume: 1.0,
        priority: 10
      };

      //播放前，先停止所有声音
      await this.fadeOutAudio();

      try {
        this.isPlaying = true;
        this.currentPlayingKey = key;
        let pro: Promise<number> = this.soundPool.play(soundId, params || defaultParams);
        pro.then((streamId) => {
          this.streamMap.set(soundId, streamId);
          console.info(`音频播放完成: streamId: ${streamId}`);
        }).catch(() => {
          this.isPlaying = false;
        });
        return pro;
      } catch (error) {
        console.error(`播放失败:  error.code: ${error.code}, error.message: ${error.message}`);
        this.isPlaying = false;
        return undefined;
      }
    }

    // 方法用来处理音频淡出
    async fadeOutAudio() {
      if (!this.soundPool) {
        return;
      }

      const stopPromises = Array.from(this.streamMap.values()).map(streamId => this.soundPool!.stop(streamId));
      await Promise.all(stopPromises);
    }

    // 停止播放
    async stop(key: string) {
      if (!this.soundPool) {
        return;
      }

      const soundId = this.soundMap.get(key);
      if (!soundId) {
        return;
      }

      const streamId = this.streamMap.get(soundId);
      if (streamId) {
        this.soundPool.stop(streamId);
      }
    }

    // 释放资源
    async release() {
      if (!this.soundPool) {
        return;
      }
      // 停止所有播放
      for (const entry of this.streamMap.entries()) {
        const streamId = entry[1];
        await this.soundPool.stop(streamId);
      }
      // 卸载所有音频
      for (const soundId of this.soundMap.values()) {
        await this.soundPool.unload(soundId);
      }
      // 移除监听
      this.soundPool.off('loadComplete');
      this.soundPool.off('playFinished');
      this.soundPool.off('error');
      // 释放SoundPool
      await this.soundPool.release();
      // 清空映射
      this.soundMap.clear();
      this.streamMap.clear();
      this.soundPool = null;
    }

    // 获取单例实例
    public static getInstance(): SoundPoolUtil {
      if (!SoundPoolUtil.instance) {
        SoundPoolUtil.instance = new SoundPoolUtil();
      }
      return SoundPoolUtil.instance;
    }

    // 静态播放方法
    public static async playSound(uri: string, volume: number = 1): Promise<number | undefined> {
      const instance = SoundPoolUtil.getInstance();
      // 确保 SoundPool 已初始化
      if (!instance.soundPool) {
        instance.init();
      }
      // 加载并播放声音
      instance.loadSound(uri);

      const params: media.PlayParameters = {
        loop: 0,
        rate: audio.AudioRendererRate.RENDER_RATE_NORMAL,
        leftVolume: volume,
        rightVolume: volume,
        priority: 1
      };
      return instance.play(uri, params);
    }
  }
  ```
