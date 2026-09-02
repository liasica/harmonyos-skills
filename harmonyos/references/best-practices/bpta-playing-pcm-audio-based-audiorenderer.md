---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-playing-pcm-audio-based-audiorenderer
title: 基于AudioRenderer播放PCM音频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 基于AudioRenderer播放PCM音频
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:977dfa248a39b2cd8bc7832f1fdebc01e894d80c07a81dc199a12f38dfd2ccd7
---

## 概述

AudioRenderer是用于音频播放的ArkTS API，仅支持PCM格式的音频。指导开发者使用AudioRenderer接口实现播放PCM音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。

本文是音频播放系列文章的第1篇，实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/eZikQjC4R8-F2MKw0MKLBQ/zh-cn_image_0000002555217465.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/k4MhqzdKQSSli9wwIgIoLA/zh-cn_image_0000002524217568.gif "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/KM4ojt1lTEqPVD5_kp0k5A/zh-cn_image_0000002591983530.gif "点击放大")

## 场景分析

| 场景名称 | 描述 | 实现方案 |
| --- | --- | --- |
| [基础播控](bpta-playing-pcm-audio-based-audiorenderer.md#section1764813377511) | 音频资源的加载、播放、暂停、退出等操作。 | 使用[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)接口实现。 |
| [跳转播放](bpta-playing-pcm-audio-based-audiorenderer.md#section16920851193717) | 滑动进度条精准跳转到指定时间进行播放。 | 使用[Slider](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在AudioRenderer的[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中触发进度调节。 |
| [静音播放](bpta-playing-pcm-audio-based-audiorenderer.md#section125715278533) | 点击按钮设置静音播放。 | 使用[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setSilentModeAndMixWithOthers()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12)方法控制静音状态。 |
| [切换歌曲播放](bpta-playing-pcm-audio-based-audiorenderer.md#section590418431566) | 点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。 | 在AudioRenderer的[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中，将获取到的不同的歌曲资源写入数据缓冲区，实现播放不同歌曲的功能。 |
| [倍速设置](bpta-playing-pcm-audio-based-audiorenderer.md#section189460361122) | 选择不同档位调节播放速度。 | 使用[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setSpeed()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setspeed11)设置播放倍速。 |
| [音量设置](bpta-playing-pcm-audio-based-audiorenderer.md#section88718617116) | 滑动音量调节面板调节播放音量。 | 使用[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)设置播放音量。 |
| [接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245) | 通过播控中心，控制播放、暂停、切换音频、调整播放进度、切换循环模式 | 通过[AVSession Kit（音视频播控服务）](../harmonyos-guides/avsession-kit.md)实现音频应用接入播控中心。 |
| [后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143) | 音频切换到后台播放。 | 接入播控中心，在此基础上申请后台运行权限并创建长时后台任务，从而实现音频在后台持续播放的功能。 |
| [接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517) | 应用退出后，播控中心显示历史歌单，点击播控中心播放按钮拉起应用播放，或者点击歌单拉起应用播放。 | 注册并适配后台启动模式的[接入方案](../harmonyos-guides/intents-habit-rec-access-programme.md)，即可实现接入。 |
| [低功耗音频播放](../harmonyos-guides/power-saving-for-playback.md) | 低功耗音频播放是一种通过软硬芯协同设计实现的音频渲染方案。其核心机制是增大音频渲染器的内部缓存，使系统能够一次性填充大量音频数据，从而允许主处理器长时间休眠，减少频繁处理音频数据的功耗，显著降低系统级功耗负载。 | 具体介绍和实现方案参考：[低功耗音频播放](../harmonyos-guides/power-saving-for-playback.md)。 |

## 基础播控

### 场景描述

通过[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)实现基础的音频播放控制能力，包括音频资源加载、播放、暂停、停止及退出等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/S18Zjw_YROWYFTrQbNLr5g/zh-cn_image_0000002524057574.gif "点击放大")

### 实现原理

开发者可以通过[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的接口，创建AudioRenderer实例，在AudioRenderer的[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中，将获取的歌曲资源写入回调事件中，实现资源加载。通过AudioRenderer的[start()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)、[pause()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)、[stop()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)和[release()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)接口实现音频的播放、暂停、停止和资源释放操作。

[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)中的不同接口调用和其状态的变化关系参考[使用AudioRenderer开发音频播放功能(ArkTS)](../harmonyos-guides/using-audiorenderer-for-playback.md)。

### 开发步骤

1. 创建AudioRenderer实例。

```screen
public async initAudioRenderer() {
  if (this.audioRenderer) {
    await this.audioRenderer.release();
    Logger.info(TAG, 'audioRenderer release ')
  }
  let audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
    channels: audio.AudioChannel.CHANNEL_2,
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
  };

  let audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    rendererFlags: 0,
    volumeMode: audio.AudioVolumeMode.SYSTEM_GLOBAL
  };

  let audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: audioStreamInfo,
    rendererInfo: audioRendererInfo
  };
  try {
    let audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    Logger.info(TAG, 'Invoke createAudioRenderer succeeded.');
    this.audioRenderer = audioRenderer;
    this.setAudioRendererCallbacks();
  } catch (err) {
    Logger.error(TAG, `Invoke createAudioRenderer failed, message is ${err}`);
  }
}
```

2. 加载歌曲资源。

```screen
public loadSongAsset(songRawFileDescriptor: resourceManager.RawFileDescriptor) {
  if (!songRawFileDescriptor) {
    Logger.error(TAG, `loadSongAsset failed: songRawFileDescriptor get failed`);
    return;
  }
  this.initOffset = songRawFileDescriptor.offset;
  this.currentOffset = this.initOffset;
  Logger.info(TAG, `current currentOffset is ${this.currentOffset}`)
  this.bufferNeedRead = songRawFileDescriptor.length;
  this.bufferRead = 0;
  this.songRawFileDescriptor = songRawFileDescriptor;
}
```

3. 设置[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调，将获取的歌曲资源写入回调事件中，实现资源加载。

```screen
// Set the data read retrieval call function
private setWriteDataCallback() {
  if (!this.audioRenderer) {
    Logger.error(TAG, 'writeData fail, audioRenderer is undefined');
    return;
  }
  let secondBufferWalk = SECOND_BUFFER_WALK;
  let bufferWalk = 0;
  let lastFd: number | undefined = undefined;
  let options: Options;
  try {
    this.audioRenderer.on('writeData', (buffer) => {
      if (this.isStopped || !this.songRawFileDescriptor || !this.songRawFileDescriptor.fd) {
        return;
      }
      if (lastFd !== this.songRawFileDescriptor.fd) {
        lastFd = this.songRawFileDescriptor.fd;
        bufferWalk = 0;
      }
      options = {
        offset: this.currentOffset,
        length: buffer.byteLength
      };
      try {
        fileIo.readSync(this.songRawFileDescriptor.fd, buffer, options);
      } catch (err) {
        Logger.error(TAG, `readSync failed,code is ${(err as BusinessError).code},message is ${(err as BusinessError).message}`);
        return;
      }
      this.currentOffset += buffer.byteLength;
      this.bufferRead = this.currentOffset - this.initOffset;
      bufferWalk += buffer.byteLength;
      if (this.bufferRead <= this.bufferNeedRead) {
        if (bufferWalk >= secondBufferWalk) { // 1s seek
          let curMs = MediaTools.getMsFromByteLength(this.bufferRead);
          this.seek(curMs);
          bufferWalk = 0;
        }
      } else {
        bufferWalk = 0;
        let curMs = MediaTools.getMsFromByteLength(this.songRawFileDescriptor.length);
        Logger.info(TAG, 'setWriteDataCallback CurMs is ' + curMs);
        this.seek(curMs);
        if (!this.isStopped) {
          this.isStopped = true;
          MediaControlCenterCallbackAction.getInstance().doPlayNextAction();
        }
      }
    })
  } catch (error) {
    Logger.error(`writeData Failed. ${error.code} message ${error.message}`);
  }
}
```

4. 开始播放。

```screen
// play music.
public async play() {
  if (!this.audioRenderer) {
    Logger.error(TAG, `audioRenderer is undefined.`);
    return;
  }
  try {
    this.isStopped = false;
    this.isPlaying = true;
    await this.audioRenderer.start().catch((err: BusinessError) => {
      Logger.error(TAG, `start failed,code is ${err.code},message is ${err.message}`);
      this.isStopped = true;
      this.isPlaying = false;
      MediaControlCenterCallbackAction.getInstance().doPauseAction();
    })
  } catch (e) {
    this.isStopped = true;
    this.isPlaying = false;
    MediaControlCenterCallbackAction.getInstance().doPauseAction();
    Logger.error(TAG, `start failed,audioRenderer is undefined`);
  }
}
```

5. 暂停播放。

```screen
// Pause music.
public async pause() {
  if (this.audioRenderer) {
    try {
      await this.audioRenderer.pause().catch((err: BusinessError) => {
        Logger.error(TAG, `pause failed,code is ${err.code},message is ${err.message}`);
      })
      Logger.info(TAG, 'pause success');
    } catch (e) {
      Logger.error(TAG, `pause failed,audioRenderer is undefined`);
    }
  }
}
```

6. 停止播放。

```screen
// Stop music
public async stop() {
  if (this.audioRenderer) {
    try {
      this.isStopped = true;
      this.isPlaying = false;
      await this.audioRenderer.stop().catch((err: BusinessError) => {
        Logger.error(TAG, `stop failed,code is ${err.code},message is ${err.message}`);
      })
      this.curMs = 0;
      await new Promise<void>((resolve) => setTimeout(resolve, 50));
      Logger.info(TAG, 'stop success');
    } catch (e) {
      Logger.error(TAG, `stop failed,audioRenderer is undefined`);
    }
  }
}
```

7. 释放实例，退出播放。

```screen
// Release audioRenderer
public async release() {
  this.isStopped = true;
  this.isPlaying = false;
  if (this.audioRenderer) {
    try {
      await AudioRendererController.getInstance().stop();
      await this.audioRenderer.release().catch((err: BusinessError) => {
        Logger.error(TAG, `release failed,code is ${err.code},message is ${err.message}`);
      })
      Logger.info(TAG, 'release success');
    } catch (err) {
      Logger.error(TAG,
        `release failed,audioRenderer is undefined, code is ${JSON.stringify(err.code)},
        message is ${JSON.stringify(err.message)}`);
    } finally {
      this.songRawFileDescriptor = undefined;
    }
  } else {
    this.songRawFileDescriptor = undefined;
  }
}
```

## 跳转播放

### 场景描述

通过点击或拖动进度条精准跳转到指定时间进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/zwgd-o8lQZGHwSxe0AZtrw/zh-cn_image_0000002555217467.gif "点击放大")

### 实现原理

在pcm文件中，每1秒时间对应的音频帧数是固定的，并且每音频帧的字节数是固定的，所以歌曲在不同时长对应的资源起始位置也可以计算出来。当用户拖动进度条到指定时间后，计算出当前时间对应当前资源的起始位置，在AudioRenderer的on('writeData')回调中，从对应的起始位置开始获取歌曲资源并写入回调中，从而实现跳转播放。另外一种方案可以参考[基于OHAudio播放PCM音频](bpta-playing-pcm-audio-based-ohaudio.md)中[跳转播放](bpta-playing-pcm-audio-based-ohaudio.md#section16920851193717)的[实现原理](bpta-playing-pcm-audio-based-ohaudio.md#section5752111843915)一节。

**说明** 

音频帧大小 = 通道数 \* （采样位深 / 8），单位为字节。

每1秒PCM对应的字节数 = 1秒包含的音频帧数 \* 音频帧大小 ，单位为字节。

* 采样率：等于每秒帧数，采样率为48000代表每秒包含48000音频帧。使用[audio.createAudioRenderer()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)接口创建AudioRenderer实例时，通过配置[AudioRendererOptions](../harmonyos-references/arkts-apis-audio-i.md#audiorendereroptions8)属性，设置音频流信息[AudioStreamInfo](../harmonyos-references/arkts-apis-audio-i.md#audiostreaminfo8)中的采样率[AudioSamplingRate](../harmonyos-references/arkts-apis-audio-e.md#audiosamplingrate8)来设置。
* 通道数：决定音频帧大小，1帧 = 所有声道各取1个采样点。使用[audio.createAudioRenderer()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)接口创建AudioRenderer实例时，通过配置[AudioRendererOptions](../harmonyos-references/arkts-apis-audio-i.md#audiorendereroptions8)属性，设置音频流信息[AudioStreamInfo](../harmonyos-references/arkts-apis-audio-i.md#audiostreaminfo8)中的通道数[AudioChannel](../harmonyos-references/arkts-apis-audio-e.md#audiochannel8)来设置。
* 采样位深：决定音频帧大小，单位为位（bit)，1字节 = 8位。使用[audio.createAudioRenderer()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)接口创建AudioRenderer实例时，通过配置[AudioRendererOptions](../harmonyos-references/arkts-apis-audio-i.md#audiorendereroptions8)属性，设置音频流信息[AudioStreamInfo](../harmonyos-references/arkts-apis-audio-i.md#audiostreaminfo8)中的采样格式[AudioSampleFormat](../harmonyos-references/arkts-apis-audio-e.md#audiosampleformat8)来获得，其对应关系如下表格。

按照[基础播控](bpta-playing-pcm-audio-based-audiorenderer.md#section1764813377511)的[开发步骤](bpta-playing-pcm-audio-based-audiorenderer.md#section167679401369)1创建AudioRenderer时配置的音频流信息是采样率48000，双声道，采样位深16bit。可以算出：

音频帧大小 = 2 \* （16 / 8）= 4 字节；

每1秒PCM对应的字节数 = 48000 \* 2 \* （16 / 8） = 192000字节。

| **AudioSampleFormat枚举值** | 对应采样位深 |
| --- | --- |
| SAMPLE\_FORMAT\_U8 | 8bit |
| SAMPLE\_FORMAT\_S16LE | 16bit |
| SAMPLE\_FORMAT\_S24LE | 24bit |
| SAMPLE\_FORMAT\_S32LE | 32bit |
| SAMPLE\_FORMAT\_F32LE | 32bit |

### 开发步骤

1. 计算每1秒PCM对应的字节数。

```screen
export const SECOND_BUFFER_WALK = 48000 * 2 * (16 / 8);
```

2. 计算跳转的目标时间对应的字节数。

```typescript
static getOffsetFromTime(curMs: number) {
  return (curMs / 1000) * SECOND_BUFFER_WALK;
}
```

3. 执行seek，结合文件的初始偏移值，算出目标时间对应的数据偏移位置。

```screen
// Seek play music.
public seek(ms: number) {
  if (ms < 0) {
    Logger.error(TAG, 'Invalid seek position')
  }
  this.curMs = ms;
  this.currentOffset = this.initOffset + MediaTools.getOffsetFromTime(this.curMs);
  MediaControlCenterCallbackAction.getInstance().doUpdateProgressAction(ms);
}
```

4. 在AudioRenderer的[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中，从对应的数据偏移位置开始获取歌曲资源并写入回调中。

```screen
// Set the data read retrieval call function
private setWriteDataCallback() {
  if (!this.audioRenderer) {
    Logger.error(TAG, 'writeData fail, audioRenderer is undefined');
    return;
  }
  let secondBufferWalk = SECOND_BUFFER_WALK;
  let bufferWalk = 0;
  let lastFd: number | undefined = undefined;
  let options: Options;
  try {
    this.audioRenderer.on('writeData', (buffer) => {
      if (this.isStopped || !this.songRawFileDescriptor || !this.songRawFileDescriptor.fd) {
        return;
      }
      if (lastFd !== this.songRawFileDescriptor.fd) {
        lastFd = this.songRawFileDescriptor.fd;
        bufferWalk = 0;
      }
      options = {
        offset: this.currentOffset,
        length: buffer.byteLength
      };
      try {
        fileIo.readSync(this.songRawFileDescriptor.fd, buffer, options);
      } catch (err) {
        Logger.error(TAG, `readSync failed,code is ${(err as BusinessError).code},message is ${(err as BusinessError).message}`);
        return;
      }
      this.currentOffset += buffer.byteLength;
      this.bufferRead = this.currentOffset - this.initOffset;
      bufferWalk += buffer.byteLength;
      if (this.bufferRead <= this.bufferNeedRead) {
        if (bufferWalk >= secondBufferWalk) { // 1s seek
          let curMs = MediaTools.getMsFromByteLength(this.bufferRead);
          this.seek(curMs);
          bufferWalk = 0;
        }
      } else {
        bufferWalk = 0;
        let curMs = MediaTools.getMsFromByteLength(this.songRawFileDescriptor.length);
        Logger.info(TAG, 'setWriteDataCallback CurMs is ' + curMs);
        this.seek(curMs);
        if (!this.isStopped) {
          this.isStopped = true;
          MediaControlCenterCallbackAction.getInstance().doPlayNextAction();
        }
      }
    })
  } catch (error) {
    Logger.error(`writeData Failed. ${error.code} message ${error.message}`);
  }
}
```

## 静音播放

### 场景描述

通过界面按钮快捷切换音频播放静音模式，实现一键开启或关闭静音模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/VuLvFLybRB2WYa1SwaBmeQ/zh-cn_image_0000002524217570.gif "点击放大")

### 实现原理

使用[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setSilentModeAndMixWithOthers()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12)方法来开启或关闭静音模式，参数设置为true，表示开启静音播放模式。

### 开发步骤

调用[setSilentModeAndMixWithOthers()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12)接口，开启或关闭静音模式。

```screen
// Set the silent mode
public setSilentMode(isSupportSilent: boolean = false) {
  if (!this.audioRenderer || !this.context) {
    return;
  }
  this.audioRenderer.setSilentModeAndMixWithOthers(isSupportSilent);
  AppStorage.setOrCreate(AppStorageKeyConstants.KEY_IS_SILENT_MODE, isSupportSilent);
}
```

## 切换歌曲播放

### 场景描述

点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/OqI5AQRXSyeFCsmgZZTZiQ/zh-cn_image_0000002555337439.gif "点击放大")

### 实现原理

通过加载不同的资源文件，并在AudioRenderer的[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中，读取资源数据，从而完成歌曲切换场景。

### 开发步骤

1. 停止当前播放的歌曲，并且清空缓存，防止杂音。

```screen
// Stop music
public async stop() {
  if (this.audioRenderer) {
    try {
      this.isStopped = true;
      this.isPlaying = false;
      await this.audioRenderer.stop().catch((err: BusinessError) => {
        Logger.error(TAG, `stop failed,code is ${err.code},message is ${err.message}`);
      })
      this.curMs = 0;
      await new Promise<void>((resolve) => setTimeout(resolve, 50));
      Logger.info(TAG, 'stop success');
    } catch (e) {
      Logger.error(TAG, `stop failed,audioRenderer is undefined`);
    }
  }
}
```

2. 根据切换模式，获取下一首歌曲的资源后，执行播放。

```screen
public async playNext() {
  if (this.isSwitching) {
    Logger.info(TAG, 'playNext skipped, already switching');
    return;
  }
  this.isSwitching = true;
  try {
    await this.stop();
    let nextIndex = this.musicIndex;
    switch (this.playMode) {
      case MusicPlayMode.SINGLE_CYCLE:
        break;
      case MusicPlayMode.ORDER:
        if (this.musicIndex === this.songList.length - 1) {
          nextIndex = 0;
        } else {
          nextIndex += 1;
        }
        break;
      case MusicPlayMode.RANDOM:
        nextIndex = this.setRandom();
        break;
      default:
        break;
    }
    this.updateMusicIndex(nextIndex);
    await this.loadSongAsset();
    Logger.info(TAG, `nextIndex is ${nextIndex}`);
    await this.play();
  } finally {
    this.isSwitching = false;
  }
}
```

## 倍速设置

### 场景描述

选择不同档位调节播放速度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/zlrag-N6SbOVX7XAamNUuA/zh-cn_image_0000002622303659.gif "点击放大")

### 实现原理

通过选择不同档位获取目标速度值，输入到[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setSpeed()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setspeed11)接口中，实现设置播放速度的功能。

### 开发步骤

1. 通过选择不同档位获取速度值，传入[setSpeed()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setspeed11)接口中。

```screen
@Builder
speedBuilder() {
  Menu() {
    MenuItemGroup({ header: this.speedTitle() }) {
      ForEach(this.speedArr, (speed: number, index: number) => {
        MenuItem({
          content: `${speed}x`,
          symbolEndIcon: this.speed === speed ? new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp') :
            undefined
        })
          .width('100%')
          .onClick(() => {
            this.speed = speed;
            MediaControlCenter.getInstance().setSpeed(this.speed);
          })
      })
    }
  }
  .menuItemDivider({
    strokeWidth: LengthMetrics.vp(0.5),
    mode: DividerMode.EMBEDDED_IN_MENU,
    color: 'rgba(0,0,0,0.2)'
  })
  .width(224)
}
```

2. 根据支持的倍数范围，通过[setSpeed()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setspeed11)接口设置播放的倍数值。

```screen
// Set the playback speed
public setSpeed(speed: number) {
  if (this.audioRenderer) {
    try {
      this.audioRenderer.setSpeed(speed);
    } catch (err) {
      Logger.error(TAG, `setSpeed fail, err:${JSON.stringify(err)}`)
    }
  }
}
```

## 音量设置

### 场景描述

滑动音量调节面板调节播放音量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/z91WmfbCTVO8VILcdXho8g/zh-cn_image_0000002555217469.gif "点击放大")

### 实现原理

通过调节面板获取目标音量值，输入到[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)接口中，实现设置播放音量的功能。

### 开发步骤

1. 通过调节面板获取音量值，传入[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)接口中。

```screen
Slider({
  value: this.volume * 100,
  min: 0,
  max: 100,
  step: 20,
  style: SliderStyle.OutSet
})
  .showSteps(true)
  .showTips(false)
  .layoutWeight(1)
  .onChange((value: number, mode: SliderChangeMode) => {
    this.volume = value / 100;
    // ...
  })
```

```screen
@StorageLink(AppStorageKeyConstants.KEY_CURRENT_VOLUME) @Watch('currentVolumeChange') volume: number = 0;
// ...
currentVolumeChange() {
  MediaControlCenter.getInstance().setVolume(this.volume)
}
```

2. 通过[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)接口设置播放音量。

```screen
public setVolume(volume: number) {
  if (!this.audioRenderer) {
    Logger.error(TAG, `audioRenderer is undefined`)
    return;
  }
  this.audioRenderer.setVolume(volume);
}
```

## 接入播控中心

### 场景描述

通过播控中心，控制播放、暂停、切换上一首或者下一首音频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/3PvyGzbuRoqrbUmcruIa-w/zh-cn_image_0000002524217572.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/sreJILj9TrWpXvbdWTwutQ/zh-cn_image_0000002555337441.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/lZPMgcU6RnC7tArp5HoOGg/zh-cn_image_0000002524057578.gif "点击放大")

### 实现原理

通过[AVSession Kit（音视频播控服务）](../harmonyos-guides/avsession-kit.md)实现音频应用接入播控中心。

### 开发步骤

1. 通过[avSession.createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建AVSession实例并激活媒体会话，[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)设置为audio。

```screen
public async initAVSession() {
  this.context = AppStorage.get(AppStorageKeyConstants.KEY_UI_ABILITY_CONTEXT);
  if (!this.context) {
    Logger.info(TAG, `session create failed, conext is undefined`);
    return;
  }
  this.mediaControlCenter = MediaControlCenter.getInstance();
  try {
    this.aVSession = await avSession.createAVSession(this.context, 'PLAY_AUDIO', 'audio');
    await this.aVSession.activate();
  } catch (error) {
    Logger.error(`createAVSession Failed. ${error.code} message ${error.message}`);
  }
  await this.setAVMetadata();
  this.setLaunchAbility();
  this.setListenerForMesFromController();
  if (this.musicIndex !== undefined) {
    this.getAndUpdateFavoriteState(this.musicIndex.toString());
  }
}
```

2. 通过[setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)把会话的一些元数据信息设置给系统，从而在播控中心界面进行展示。如媒体ID（assetId）、标题（title）、播控中心显示的图片（mediaImage）、媒体时长（duration）等。

```screen
// Set metadata
public async setAVMetadata() {
  this.musicIndex = AppStorage.get(AppStorageKeyConstants.KEY_SELECT_INDEX) ?
    AppStorage.get(AppStorageKeyConstants.KEY_SELECT_INDEX) : 0;
  if (!this.musicIndex || this.musicIndex < 0 || this.musicIndex >= this.songList.length) {
    this.musicIndex = 0;
  }
  try {
    if (this.context) {
      let mediaImage = await MediaTools.getPixelMapFromResource(this.context,
        this.songList[this.musicIndex].label as resourceManager.Resource);
      Logger.info(TAG, 'getPixelMapFromResource success' + JSON.stringify(mediaImage));
      let title = '';
      let artist = '';
      if (this.context) {
        if (this.songList[this.musicIndex].title !== undefined) {
          title = this.context.resourceManager.getStringSync(this.songList[this.musicIndex].title?.id);
        }
        if (this.songList[this.musicIndex].singer !== undefined) {
          artist = this.context.resourceManager.getStringSync(this.songList[this.musicIndex].singer?.id);
        }
      } else {
        title = firstSongTitle;
        artist = firstSongSinger;
      }
      let metadata: avSession.AVMetadata = {
        assetId: `${this.musicIndex}`,
        title: title,
        artist: artist,
        mediaImage: mediaImage,
        duration: this.getDuration(),
        avQueueName: 'AudioRendererQueue',
        avQueueId: 'AudioRendererQueueId',
        avQueueImage: mediaImage
      };
      let lrc = await MediaTools.getLrcFromRawFile(this.context, this.songList[this.musicIndex].lyric);
      if (lrc) {
        metadata.lyric = lrc;
      }
      if (this.aVSession) {
        this.aVSession.setAVMetadata(metadata).then(() => {
          Logger.info(TAG, 'SetAVMetadata successfully');
        }).catch((err: BusinessError) => {
          Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
        });
      }
      mediaImage?.release();
    }
  } catch (error) {
    Logger.error(TAG, `SetAVMetadata failed, code: ${(error as BusinessError).code}`);
  }
}
```

3. 设置播控中心拉起的UIAbility。

```screen
// Set LaunchAbility.
private setLaunchAbility() {
  if (!this.context) {
    return;
  }
  let wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: this.context.abilityInfo.bundleName,
        abilityName: this.context.abilityInfo.name
      }
    ],
    operationType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
    if (this.aVSession) {
      this.aVSession.setLaunchAbility(agent);
    }
  })
    .catch((err: BusinessError) => {
      Logger.error(TAG, `getWantAgent failed: code: ${err.code}, message: ${err.message}`);
    });
}
```

4. 注册播控命令事件监听，便于响应用户通过播控中心下发的播控命令，比如播放[on('play')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)、暂停[on('pause')](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10)、上一曲[on('playPrevious')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplayprevious10)、下一曲[on('playNext')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaynext10)等。

```screen
// Set listening events
setListenerForMesFromController() {
  if (!this.aVSession) {
    return;
  }
  try {
    this.aVSession.on('play', this.onPlay);
    this.aVSession.on('pause', this.onPause);
    this.aVSession.on('playNext', this.onPlayNext);
    this.aVSession.on('playPrevious', this.onPlayPrevious);
    this.aVSession.on('seek', this.onSeek);
    this.aVSession.on('setLoopMode', this.onSetLoopMode);
    this.aVSession.on('toggleFavorite', this.onToggleFavorite);
  } catch (error) {
    Logger.error(`setListenerForMesFromController Failed. ${error.code} message ${error.message}`);
  }
}
```

5. 应用状态上报播控中心，当音频状态发生改变时，需要通过[setAVPlaybackState()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)向播控中心上报音频状态，来达到播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。

```screen
// Set favorite state.
private setFavoriteState(isFavorite: boolean) {
  if (this.aVSession) {
    this.aVSession.setAVPlaybackState({ isFavorite }, (err: BusinessError) => {
      if (err) {
        Logger.error(TAG, `setFavoriteState BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        Logger.info(TAG, 'setFavoriteState successfully');
      }
    });
  }
}

// Set progress state.
public setProgressState(ms: number) {
  if (this.aVSession) {
    this.aVSession.setAVPlaybackState({
      position: {
        elapsedTime: ms,
        updateTime: new Date().getTime()
      }
    }, (err: BusinessError) => {
      if (err) {
        Logger.error(TAG, `setProgressState BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        Logger.info(TAG, 'setProgressState successfully');
      }
    });
  }
}

// Set play state.
public setPlayState(isPlay: boolean) {
  if (!this.aVSession) {
    Logger.error(TAG, 'AVSession is undefined');
    return;
  }
  this.aVSession.setAVPlaybackState({
    state: isPlay ? avSession.PlaybackState.PLAYBACK_STATE_PLAY : avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
  }, (err: BusinessError) => {
    if (err) {
      Logger.error(TAG, `setPlayState BusinessError: code: ${err.code}, message: ${err.message}`);
    } else {
      Logger.info(TAG, 'setPlayState successfully');
    }
  });
}
```

## 后台播放

### 场景描述

音频切换到后台播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/09lKbSm4RWe76QprKRv-vA/zh-cn_image_0000002624787553.gif "点击放大")

### 实现原理

首先需实现播控中心的接入，在此基础上申请后台运行权限并设置后台模式，同时为音频应用创建长时后台任务，从而实现音频在后台持续播放的功能。

### 开发步骤

1. 在module.json5配置文件中配置[ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running)权限和后台模式audioPlayback。

```typescript
{
  "module": {
    // ...
    "requestPermissions": [
      {
        "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
        "reason": "$string:reason_background",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when": "always"
        }
      },
    ],
    // ...
  }
}
```

2. 创建后台任务管理类，通过startContinuousTask申请后台长时任务（长时任务类型[BackgroundMode](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)设置为AUDIO\_PLAYBACK，以实现音频后台播放），并通过stopContinuousTask取消长时任务。

```screen
export class BackgroundUtil {
  // Start background task.
  // @param context
  public static startContinuousTask(context?: common.UIAbilityContext): void {
    if (!context) {
      Logger.error(TAG, 'startContinuousTask failed', `context undefined`);
      return;
    }
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: context.abilityInfo.bundleName,
          abilityName: context.abilityInfo.name
        }
      ],
      operationType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: Object) => {
      try {
        backgroundTaskManager.startBackgroundRunning(context,
          backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
          Logger.info(TAG, 'startBackgroundRunning succeeded');
        }).catch((error: BusinessError) => {
          Logger.error(TAG, `startBackgroundRunning failed Cause: code ${error.code}`);
        });
      } catch (error) {
        Logger.error(TAG, `startBackgroundRunning failed.message ${(error as BusinessError).message}`);
      }
    })
      .catch((error: BusinessError) => {
        Logger.error('this audioRenderer: ', `getWantAgent failed Cause: code ${error.code}`);
      });
  }

  // Stop background task.
  // @param context
  public static stopContinuousTask(context: common.UIAbilityContext): void {
    try {
      backgroundTaskManager.stopBackgroundRunning(context).then(() => {
        Logger.info('this audioRenderer: ', 'stopBackgroundRunning succeeded');
      }).catch((error: BusinessError) => {
        Logger.error('this audioRenderer: ', `stopBackgroundRunning failed Cause: code ${error.code}`);
      });
    } catch (error) {
      Logger.error(TAG, `stopBackgroundRunning failed. message ${error}`);
    }
  }
}
```

3.在播放和暂停时，分别申请和销毁后台长时任务。

```screen
public async play(index: number = this.musicIndex) {
  Logger.info(TAG, `index is ${index},musicIndex is ${this.musicIndex}`)
  if (!this.mediaControlCenterHandle) {
    Logger.error(TAG, 'mediaControlCenterHandle is undefined');
    return;
  }
  if (index !== this.musicIndex) {
    this.updateMusicIndex(index);
    await this.stop();
    await this.loadSongAsset();
  }
  this.updateIsPlay(true);
  await this.mediaControlCenterHandle.play();
  BackgroundUtil.startContinuousTask(this.context);
}

public pause() {
  if (!this.mediaControlCenterHandle) {
    Logger.error(TAG, 'mediaControlCenterHandle is undefined');
    return;
  }
  this.mediaControlCenterHandle.pause();
  this.updateIsPlay(false);
  if(this.context){
    BackgroundUtil.stopContinuousTask(this.context);
  }
}
```

## 接入播控中心冷启动和历史歌单

### 场景描述

用户在应用内播放后，上滑结束应用进程，再进入播控中心，点击播放键拉起应用播放，或者点击历史歌单拉起应用播放，播控中心正确显示当前播放信息及播放状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ZCUrdR7iQZGfY8c_uann1Q/zh-cn_image_0000002524217574.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/q38x8AlWSImOtK3x3FN7AQ/zh-cn_image_0000002624867455.gif "点击放大")

### 实现原理

注册并适配[端侧意图调用](../harmonyos-guides/intents-habit-rec-access-programme.md#端侧意图调用)，实现一键冷启动播放和历史歌单。

### 开发步骤

1. 注册播放意图。应用按照播放业务，选择PlayMusicList意图，编辑对应的意图配置PROJECT\_HOME/entry/src/main/resources/base/profile/insight\_intent.json文件，实现播放意图注册，具体步骤参考：[意图注册](../harmonyos-guides/intents-habit-rec-access-programme.md#意图注册)。

2. 注册成功后，在配置文件中设置歌曲播放方法，即可实现一键冷启动播放。触发播控冷启动播放时，系统会在意图参数intentParam的歌单id为空，即解析出的entityId为空字符串时，由应用决定播放内容。触发歌单播放时，系统会将歌单的唯一标识id传回应用，应用可以在意图调用接口中，通过解析意图参数intentParam中的entityId，获取到歌单的id，实现对应歌单的播放。

```screen
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  onExecuteInUIAbilityBackgroundMode(intentName: string, intentParam: Record<string, Object>):
    Promise<insightIntent.ExecuteResult> {
    switch (intentName) {
      case 'PlayMusicList':
        let entityId: string = (intentParam.items as EntityIdObj[])?.[0]?.entityId;
        return this.playFunc(entityId);
      case 'PlayAudio':
        let data = intentParam as Record<string, string>;
        if (data && data.entityId && typeof data.entityId === 'string' && data.entityId.length > 0) {
          return this.playFunc(data.entityId);
        }
      default:
        break;
    }
    return Promise.resolve({
      code: -1,
      result: {
        message: 'unknown intent'
      }
    } as insightIntent.ExecuteResult)
  }

  // ...
}
```

3. 设置歌单信息，通过[setAVMetadata](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)接口设置当前播放的歌单信息，系统媒体信息根据应用上报实时刷新，若应用接入歌单功能，则确保在[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)中一直携带歌单数据。

```screen
// Set metadata
public async setAVMetadata() {
  this.musicIndex = AppStorage.get(AppStorageKeyConstants.KEY_SELECT_INDEX) ?
    AppStorage.get(AppStorageKeyConstants.KEY_SELECT_INDEX) : 0;
  if (!this.musicIndex || this.musicIndex < 0 || this.musicIndex >= this.songList.length) {
    this.musicIndex = 0;
  }
  try {
    if (this.context) {
      let mediaImage = await MediaTools.getPixelMapFromResource(this.context,
        this.songList[this.musicIndex].label as resourceManager.Resource);
      Logger.info(TAG, 'getPixelMapFromResource success' + JSON.stringify(mediaImage));
      let title = '';
      let artist = '';
      if (this.context) {
        if (this.songList[this.musicIndex].title !== undefined) {
          title = this.context.resourceManager.getStringSync(this.songList[this.musicIndex].title?.id);
        }
        if (this.songList[this.musicIndex].singer !== undefined) {
          artist = this.context.resourceManager.getStringSync(this.songList[this.musicIndex].singer?.id);
        }
      } else {
        title = firstSongTitle;
        artist = firstSongSinger;
      }
      let metadata: avSession.AVMetadata = {
        assetId: `${this.musicIndex}`,
        title: title,
        artist: artist,
        mediaImage: mediaImage,
        duration: this.getDuration(),
        avQueueName: 'AudioRendererQueue',
        avQueueId: 'AudioRendererQueueId',
        avQueueImage: mediaImage
      };
      let lrc = await MediaTools.getLrcFromRawFile(this.context, this.songList[this.musicIndex].lyric);
      if (lrc) {
        metadata.lyric = lrc;
      }
      if (this.aVSession) {
        this.aVSession.setAVMetadata(metadata).then(() => {
          Logger.info(TAG, 'SetAVMetadata successfully');
        }).catch((err: BusinessError) => {
          Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
        });
      }
      mediaImage?.release();
    }
  } catch (error) {
    Logger.error(TAG, `SetAVMetadata failed, code: ${(error as BusinessError).code}`);
  }
}
```

## 示例代码

* [基于AudioRenderer播放PCM音频](https://gitcode.com/HarmonyOS_Samples/audio-renderer-play-pcm)
