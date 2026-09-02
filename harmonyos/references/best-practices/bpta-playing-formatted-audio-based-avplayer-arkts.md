---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-playing-formatted-audio-based-avplayer-arkts
title: 基于AVPlayer播放格式化音频（ArkTS）
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 基于AVPlayer播放格式化音频（ArkTS）
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:94903365fe4af26eebfe9c1b98debf729509fe4da0d8e8c532dfe091e53fa6b4
---

## 概述

AVPlayer可以用于播放格式化音频，支持WAV、MP3和FLAC等格式的音频。AVPlayer提供了ArkTS API和Native API，本文指导开发者使用AVPlayer的ArkTS API实现播放格式化音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。

本文是音频播放系列文章的第3篇，实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/TK2AUjGeRd2aAcop0kIQSQ/zh-cn_image_0000002555217523.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/-7JoaTcPTn2NUhiOIow9bQ/zh-cn_image_0000002524217626.gif "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/RbI0jrvARIC_Q1I7d-nC7w/zh-cn_image_0000002555337497.gif "点击放大")

## 场景分析

| 场景名称 | 描述 | 实现方案 |
| --- | --- | --- |
| [基础播控](bpta-playing-formatted-audio-based-avplayer-arkts.md#section1764813377511) | 音频资源的加载、播放、暂停、退出等操作。 | 使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)接口实现。 |
| [跳转播放](bpta-playing-formatted-audio-based-avplayer-arkts.md#section16920851193717) | 滑动进度条精准跳转到指定时间进行播放。 | 使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在[onChange()](../harmonyos-references/ts-basic-components-slider.md#onchange)回调中触发进度调节获取目标时间，使用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口，跳转到目标时间。 |
| [静音播放](bpta-playing-formatted-audio-based-avplayer-arkts.md#section125715278533) | 点击按钮设置静音播放。 | 使用AVPlayer的[setMediaMuted()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)控制静音状态。 |
| [切换歌曲播放](bpta-playing-formatted-audio-based-avplayer-arkts.md#section590418431566) | 点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。 | 使用[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)接口重置播放器状态，给AVPlayer的fd或fdSrc属性赋值为新的歌曲资源，实现播放不同的功能。 |
| [倍速设置](bpta-playing-formatted-audio-based-avplayer-arkts.md#section189460361122) | 滑动倍速调节面板调节播放速度。 | 使用[setSpeed()](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)接口设置播放倍速。 |
| [音量设置](bpta-playing-formatted-audio-based-avplayer-arkts.md#section88718617116) | 滑动音量调节面板调节播放音量。 | 使用[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)设置播放音量。 |
| [接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245) | 通过播控中心，控制播放、暂停、切换音频、调整播放进度、切换循环模式 | 具体原理、方案和开发步骤参考[接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245)。本篇文章不再赘述。 |
| [后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143) | 音频切换到后台播放。 | 具体原理、方案和开发步骤参考[后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143)。本篇文章不再赘述。 |
| [接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517) | 应用退出后，播控中心显示历史歌单，点击播控中心播放按钮拉起应用播放，或者点击歌单拉起应用播放。 | 具体原理、方案和开发步骤参考[接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517)。本篇文章不再赘述。 |

## 基础播控

### 场景描述

通过[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现核心音频播放控制能力，包括音频资源加载、播放、暂停、停止及退出等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/R2knoSn6QfSdfgEXC10EaQ/zh-cn_image_0000002524057632.gif "点击放大")

### 实现原理

核心原理是使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)接口实现播放、暂停等功能，需要特别注意的是，AVPlayer播放器在执行不同的操作前，必须要保证此时处于正确的状态，比如执行播放操作前，只有当前状态在prepared/paused/completed时，才能正确执行，否则系统可能会抛出异常或生成其他未定义的行为。AVPlayer的播放状态和不同接口间的关系参考[使用AVPlayer播放视频](../harmonyos-guides/video-playback.md)一节中的播放状态变化示意图。

主要的开发步骤如下：

1. 开发者可以通过[createAVPlayer()](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)构建一个AVPlayer实例，创建成功后，此时播放器处于idle状态。
2. 注册[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)回调，主动获取当前状态变化。

   **注意** 

   因为AVPlayer播放器的接口是否能正常执行和当前的播放器状态有必然联系，建议开发者务必注册[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)状态监听或者使用AVPlayer的state属性主动获取当前状态，保证在正确的状态下执行对应操作。以免发生异常，影响开发效率。
3. 注册[on('error')](../harmonyos-references/arkts-apis-media-avplayer.md#onerror9)回调，发生异常后，监听错误事件，可以快速根据报错信息进行定位。
4. 通过url、fdSrc等属性设置播放资源，设置成功后，播放器会进入initialized状态。
5. 执行[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口准备播放音频。需在[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)事件中，监听到播放器成功触发至initialized状态后，才能调用。执行完[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口后，播放器会进入prepared状态。
6. 执行[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)接口，播放音频资源。

   **注意** 

   第4步设置完url、fdSrc等属性后，播放器并不是就立刻进入initialized状态；第5步执行完[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，播放器也不是立刻进入prepared，都是需在[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)事件中，监听到播放器成功触发至initialized状态后，才能执行下一步的操作，否则接口会执行异常。

   7. 执行[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)接口，暂停音频资源。

   8. 执行[stop()](../harmonyos-references/arkts-apis-media-avplayer.md#stop9)接口，停止播放音频资源。

   9. 执行[release()](../harmonyos-references/arkts-apis-media-avplayer.md#release9)，销毁播放资源。

### 开发步骤

1. 通过[createAVPlayer()](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)创建一个AVPlayer实例。

```typescript
// Initialize the player
public async initAVPlayer() {
  if (this.avPlayer) {
    Logger.info(TAG, 'avPlayer already created');
    return;
  }
  this.avPlayer = await media.createAVPlayer();
  this.genSpeedMap();
  Logger.info(TAG, `createAVPlayer success， curState is ${this.avPlayer?.state}`);
  this.setAVPlayerCallbacks();
  Logger.info(TAG, `setAVPlayerCallbacks success，curState is ${this.avPlayer?.state}`);
}
```

2. 注册[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)回调，主动获取当前状态变化。

```typescript
// Watch state
private stateChangeCallback() {
  if (!this.avPlayer) {
    Logger.error(TAG, `stateChangeCallback , avPlayer is undefined`);
    return;
  }
  this.avPlayer.on('stateChange', async (state: media.AVPlayerState, reason: media.StateChangeReason) => {
    this.currentState = state;
    switch (state) {
      case 'idle':
        Logger.info(TAG, `state idle called , resson is ${reason}`);
        break;
      case 'initialized':
        Logger.info(TAG, `state initialized called , resson is ${reason}`);
        this.setAudioRendererInfo();
        this.prepare();
        break;
      case 'prepared':
        Logger.info(TAG, `state prepared called , resson is ${reason}`);
        if (this.waitPlay) {
          this.play();
        }
        break;
      // ...
    }
  });
  Logger.info(TAG, `set stateChangeCallback success`);
}
```

3. 注册[on('error')](../harmonyos-references/arkts-apis-media-avplayer.md#onerror9)回调，发生异常后，监听错误事件。

```typescript
private errorCallback() {
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.on('error', (error: BusinessError) => {
    Logger.error(TAG, `errorCallback , code is ${error.code} message is ${error.message}`);
  });
}
```

4. 通过[url](../harmonyos-references/arkts-apis-media-avplayer.md#属性)、[fdSrc](../harmonyos-references/arkts-apis-media-avplayer.md#属性)等属性设置播放资源。

```typescript
async loadSongAssent(songRawFileDescriptor: resourceManager.RawFileDescriptor) {
  if (!songRawFileDescriptor) {
    Logger.error(TAG, `loadSongAssent faile : songRawFileDescriptor get failed`);
    return;
  }
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.fdSrc = songRawFileDescriptor;
  Logger.info(TAG, `set avPlayer url is ${this.avPlayer.fdSrc}，curState is ${this.avPlayer?.state}`);
}
```

5. 执行[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口准备播放音频。

```typescript
// Prepare the player
public async prepare() {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  await this.avPlayer.prepare().then(() => {
    Logger.info(TAG, `prepare success , curState is ${this.avPlayer?.state}`);
    AppStorage.setOrCreate('totalTime', MediaTools.msToCountdownTime(this.avPlayer?.duration!));
    AppStorage.setOrCreate('totalMsTime', this.avPlayer?.duration!);
    AppStorage.setOrCreate('progressMax', this.avPlayer?.duration!);
  });
}
```

6. 执行[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)接口，开始播放音频资源。

```typescript
public async play() {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  if (this.currentState !== 'prepared' && this.currentState !== 'paused' && this.currentState !== 'stopped' &&
    this.currentState !== 'completed') {
    this.waitPlay = true;
    Logger.info(TAG, 'avPlayer current playState is not prepared')
    return;
  }
  await this.avPlayer.play();
  this.waitPlay = false;
  Logger.info(TAG, 'play success');
  this.updateIsPlay(true);
  Logger.info(TAG, `curState is ${this.avPlayer?.state}`);
}
```

7. 执行[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)接口，暂停播放。

```typescript
public pause() {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  this.avPlayer.pause();
  this.updateIsPlay(false);
}
```

8. 执行[stop()](../harmonyos-references/arkts-apis-media-avplayer.md#stop9)接口，停止播放音频。

```typescript
public async stop() {
  if (!this.avPlayer) {
    Logger.error(TAG, 'avPlayer is undefined')
    return;
  }
  await this.avPlayer.stop();
  await this.avPlayer.reset();
  Logger.info(TAG, 'avPlayer stop success')
}
```

9. 执行[release()](../harmonyos-references/arkts-apis-media-avplayer.md#release9)，销毁播放资源。

```typescript
public release() {
  if (!this.avPlayer) {
    Logger.error(TAG, 'avPlayer is undefined')
    return;
  }
  this.avPlayer.release();
  Logger.error(TAG, 'avPlayer release success');
}
```

## 跳转播放

### 场景描述

通过点击或拖动进度条精准跳转到指定时间进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/aHLoNHDkRB-ghVyLbdlkxg/zh-cn_image_0000002555217525.gif "点击放大")

### 实现原理

使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在[onChange()](../harmonyos-references/ts-basic-components-slider.md#onchange)回调中触发进度调节获取目标时间，使用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口，跳转到目标时间。

### 开发步骤

使用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口，跳转到目标时间。

```typescript
public seek(ms: number) {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  this.avPlayer.seek(ms);
}
```

## 静音播放

### 场景描述

通过界面按钮快捷切换音频播放静音状态，实现一键开启或关闭静音。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/PxIghX2RQae-kUml3auiFg/zh-cn_image_0000002524217628.gif "点击放大")

### 实现原理

使用AVPlayer的[setMediaMuted()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)接口，第二个参数设置为true为开启静音播放，设置为false为取消静音播放。

### 开发步骤

调用AVPlayer的[setMediaMuted()](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)设置静音。

```typescript
public setSilentMode(isSilentMode: boolean) {
  if (!this.avPlayer) {
    Logger.error(TAG, 'avPlayer is undefined')
    return;
  }
  this.avPlayer.setMediaMuted(media.MediaType.MEDIA_TYPE_AUD, isSilentMode);
  Logger.info(TAG, `avPlayer setMediaMuted is ${isSilentMode} success`)
}
```

## 切换歌曲播放

### 场景描述

点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/n2P4llyWRWmdKxMSu9XFSQ/zh-cn_image_0000002555337501.gif "点击放大")

### 实现原理

使用[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)接口重置播放器状态，给AVPlayer的fd或fdSrc属性赋值为新的歌曲资源，实现播放不同歌曲的功能。

### 开发步骤

1. 停止当前播放的歌曲， 用[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)接口重置播放器状态。

```typescript
public async stop() {
  if (!this.avPlayer) {
    Logger.error(TAG, 'avPlayer is undefined')
    return;
  }
  await this.avPlayer.stop();
  await this.avPlayer.reset();
  Logger.info(TAG, 'avPlayer stop success')
}
```

2. 给AVPlayer的fd或fdSrc属性赋值为新的歌曲资源。

```typescript
async loadSongAssent(songRawFileDescriptor: resourceManager.RawFileDescriptor) {
  if (!songRawFileDescriptor) {
    Logger.error(TAG, `loadSongAssent faile : songRawFileDescriptor get failed`);
    return;
  }
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.fdSrc = songRawFileDescriptor;
  Logger.info(TAG, `set avPlayer url is ${this.avPlayer.fdSrc}，curState is ${this.avPlayer?.state}`);
}
```

## 倍速设置

### 场景描述

滑动倍速调节面板调节播放速度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/H8d0QWNSS9COQsStfqnn4g/zh-cn_image_0000002524057634.gif "点击放大")

### 实现原理

通过调节面板获取目标速度值，输入到[setSpeed()](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)接口中，实现设置播放速度的功能。

### 开发步骤

1. 通过调节面板获取速度值，传入[setSpeed()](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)接口中。

```typescript
Slider({
  value: this.speed,
  min: 0.25,
  max: 2,
  step: 0.25,
  style: SliderStyle.OutSet
})
  .layoutWeight(1)
  .showTips(true, this.speed.toString())
  .showSteps(true)
  .onChange((value: number, mode: SliderChangeMode) => {
    this.speed = value;
    MediaControlCenter.getInstance().setSpeed(this.speed);
    console.info('value:' + value + 'mode:' + mode.toString());
  })
```

2. 使用[setSpeed()](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)接口设置播放速度。

```typescript
// Set Speed
public setSpeed(speed: number) {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  Logger.info(TAG, `set speed is ${speed}`)
  this.avPlayer.setSpeed(this.switchSpeed(speed));
}
```

## 音量设置

### 场景描述

滑动音量调节面板调节播放音量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Na6xpfvjRzmHXn7LCPgNXA/zh-cn_image_0000002555217531.gif "点击放大")

### 实现原理

通过调节面板获取目标音量值，输入到[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)接口中，实现设置播放音量的功能。

### 开发步骤

1. 通过调节面板获取音量值，传入[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)接口中。

```typescript
Slider({
  value: this.volume,
  min: 0,
  max: 100,
  step: 1,
  style: SliderStyle.OutSet
})
  .showTips(false)
  .layoutWeight(1)
  .onChange((value: number, mode: SliderChangeMode) => {
    this.volume = value;
    if (this.volume === 0) {
      this.isSilentMode = true
    } else {
      this.isSilentMode = false;
    }
  })
```

2. 使用[setVolume()](../harmonyos-references/arkts-apis-media-avplayer.md#setvolume9)设置播放音量。

```typescript
// Set Volume
public setVolume(volume: number) {
  if (!this.avPlayer) {
    Logger.info(TAG, 'avPlayer is undefined')
    return;
  }
  Logger.info(TAG, `set volume is ${volume}`)
  this.avPlayer.setVolume(volume / 100);
}
```

## 常见问题

### 执行AVPlayer的方法时失败，返回错误信息“Operation not allowed.”

**问题现象**

在调用AVPlayer的prepare、play、stop等方法时，会执行失败，返回错误信息“Operation not allowed.”。如以下场景。

* 设置完url、fdSrc等属性后，代码下一行就立刻执行[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，执行出错，返回错误信息“Operation not allowed.”。
* 同样，执行完[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，代码下一行立刻执行[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)接口，执行出错，返回错误信息“Operation not allowed.”。

**可能原因**

AVPlayer的当前状态不支持此操作，执行接口前检查下当前AVPlayer的播放状态。AVPlayer播放器在执行不同的操作前，必须要保证此时处于正确的状态，比如执行播放操作前，只有当前状态在prepared/paused/completed时，才能正确执行。针对问题现象中举例的两种场景，其错误的原因可能如下。

* 设置完url、fdSrc等属性后，AVPlayer并不是就立刻进入initialized状态，如果设置完url属性后就立刻执行[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，当代码运行此行时，AVPlayer的播放状态可能还是处于idle的状态，并没有变成initialized，这时就可能产生“Operation not allowed.”的错误。
* 同样，执行完[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，AVPlayer也不是立刻进入prepared状态，如果此时立刻执行[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)接口，AVPlayer的播放状态可能还没有变成prepared状态，执行就可能报错。

**解决方案**

1. 先了解在AVPlayer的不同播放状态下，可以执行哪些接口。熟悉AVPlayer的播放状态和不同接口间的关系，可以参考[使用AVPlayer播放视频](../harmonyos-guides/video-playback.md)一节中的播放状态变化示意图。

2. 保证在在正确的播放状态下，执行对应的接口。建议开发者务必注册[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)状态监听，当监听到AVPlayer的播放状态到达目标状态时，执行对应的接口。在[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)中监听到AVPlayer处于initialized状态时，再执行[prepare()](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口，监听到AVPlayer处于prepared状态时，再执行[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)接口。

```typescript
// Watch state
private stateChangeCallback() {
  if (!this.avPlayer) {
    Logger.error(TAG, `stateChangeCallback , avPlayer is undefined`);
    return;
  }
  this.avPlayer.on('stateChange', async (state: media.AVPlayerState, reason: media.StateChangeReason) => {
    this.currentState = state;
    switch (state) {
      case 'idle':
        Logger.info(TAG, `state idle called , resson is ${reason}`);
        break;
      case 'initialized':
        Logger.info(TAG, `state initialized called , resson is ${reason}`);
        this.setAudioRendererInfo();
        this.prepare();
        break;
      case 'prepared':
        Logger.info(TAG, `state prepared called , resson is ${reason}`);
        if (this.waitPlay) {
          this.play();
        }
        break;
      // ...
    }
  });
  Logger.info(TAG, `set stateChangeCallback success`);
}
```

## 示例代码

* [基于AVPlayer播放格式化音频（ArkTS）](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-arkts)
