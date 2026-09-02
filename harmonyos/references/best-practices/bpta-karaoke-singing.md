---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-karaoke-singing
title: K歌解决方案
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > K歌解决方案
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:91fedaede0ae228dddbebfb501688a08ad27279c787529f3ce763b80d6739fd8
---

## 概述

本文适用于K歌应用的开发，针对市场上主流K歌应用的常见场景，介绍了如何基于[Interface (AudioCapturer)](../harmonyos-references/arkts-apis-audio-audiocapturer.md)、[Interface (AudioRenderer)](../harmonyos-references/arkts-apis-audio-audiorenderer.md)、[Interface (AudioLoopback)](../harmonyos-references/arkts-apis-audio-audioloopback.md)、[Interface (AudioRoutingManager)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)、[Interface (AVPlayer)](../harmonyos-references/arkts-apis-media-avplayer.md)开发一个K歌应用。本文指导开发者实现[原唱和伴奏同步播放](bpta-karaoke-singing.md#section1431816338165)、[K歌录音采集](bpta-karaoke-singing.md#section5737811161413)、[人声和伴奏混音合成](bpta-karaoke-singing.md#section16271239854)、[K歌音频耳返](bpta-karaoke-singing.md#section728015301074)、[K歌混响音效](bpta-karaoke-singing.md#section4522123111718)、[K歌设备检测管理](bpta-karaoke-singing.md#section123557411719)等K歌常见功能。

## 场景分析

K歌各功能的实现方式如下表所示：

| 功能 | 实现方式 |
| --- | --- |
| 原唱和伴奏同步播放 | [OH\_AVPlayer](../harmonyos-references/capi-avplayer-oh-avplayer.md) |
| K歌录音采集 | AudioCapturer |
| 人声和伴奏混音合成 | Native PCM混音算法，参考[人声和伴奏混音合成](bpta-karaoke-singing.md#section16271239854) |
| K歌音频耳返 | 硬件耳返：AudioLoopback  软件耳返：AudioCapturer + AudioRenderer |
| K歌混响音效 | [AudioLoopbackReverbPreset](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackreverbpreset21) |
| K歌设备检测管理 | AudioRoutingManager |

## 原唱和伴奏同步播放

### 场景描述

在K歌时，单击首页中的原唱和伴奏按钮，可以实时选择播放带人声的原版音乐或者播放纯伴奏音乐。单击首页面底部的音量按钮，弹出音量设置面板，通过设置伴奏音量可以调整播放器的音量。伴奏音量设置如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/KaW3-tknSnyPmE4atflQzA/zh-cn_image_0000002654119836.png "点击放大")

### 实现原理

使用两个独立的[OH\_AVPlayer](../harmonyos-references/capi-avplayer-oh-avplayer.md)作为原唱播放器和伴奏播放器，在原唱模式下，将伴奏播放器的音量设置为0；在伴奏模式下，将原唱播放器的音量设置为0。两个播放器同步播放，共享原唱播放器的播放位置。

| 模式 | 播放模式值 | 原唱音量 | 伴奏音量 |
| --- | --- | --- | --- |
| 原唱 | ORIGINAL | 音量调节设置的伴奏音量 | 0 |
| 伴奏 | ACCOMPANIMENT | 0 | 音量调节设置的伴奏音量 |

### 开发步骤

1. 通过[OH\_AVPlayer\_Create()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_create)创建原唱播放器和伴奏播放器。

```cpp
// Create players
g_originalPlayer = OH_AVPlayer_Create();
g_accompanimentPlayer = OH_AVPlayer_Create();
```

2. 根据播放模式，通过[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)设置原唱播放器和伴奏播放器的音量。

```cpp
if (g_playMode == PlayMode::ORIGINAL) {
    originalVolume = g_musicVolume;
    accompanimentVolume = 0.0f;
} else if (g_playMode == PlayMode::ACCOMPANIMENT) {
    originalVolume = 0.0f;
    accompanimentVolume = g_musicVolume;
}

if (g_originalPlayer) {
    OH_AVPlayer_SetVolume(g_originalPlayer, originalVolume, originalVolume);
}
if (g_accompanimentPlayer) {
    OH_AVPlayer_SetVolume(g_accompanimentPlayer, accompanimentVolume, accompanimentVolume);
}
```

3. 通过[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)设置原唱播放器的消息回调监听函数，在回调函数中获取原唱播放器的当前播放位置。

```cpp
// Set original player callback
OH_AVPlayer_SetOnInfoCallback(g_originalPlayer, OnOriginalInfo, nullptr);
```

```cpp
static void OnOriginalInfo([[maybe_unused]] OH_AVPlayer *player, AVPlayerOnInfoType type, OH_AVFormat *infoBody,
                           [[maybe_unused]] void *userData) {
    // ...
    switch (type) {
    case AV_INFO_TYPE_POSITION_UPDATE:
        OH_AVFormat_GetIntValue(infoBody, OH_PLAYER_CURRENT_POSITION, &value);
        g_position = value;
        break;
    // ...
    }
}
```

4. 通过[OH\_AVPlayer\_Seek()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_seek)设置两个播放器跳转到相同的播放位置。

```cpp
if (g_originalPlayer) {
    OH_AVPlayer_Seek(g_originalPlayer, position, AV_SEEK_PREVIOUS_SYNC);
}
if (g_accompanimentPlayer) {
    OH_AVPlayer_Seek(g_accompanimentPlayer, position, AV_SEEK_PREVIOUS_SYNC);
}
g_position = position;
```

## K歌录音采集

### 场景描述

K歌过程中需要录制麦克风采集的音频数据，用于后续人声和伴奏的混音合成、耳返以及K歌文件的保存。单击首页面底部的录制按钮，开始录音采集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/v2kdNpN_RgmMhnAkNiE9_g/zh-cn_image_0000002653959926.png "点击放大")

### 实现原理

通过[Interface (AudioCapturer)](../harmonyos-references/arkts-apis-audio-audiocapturer.md)可以录制PCM（Pulse Code Modulation）音频数据。录音参数如下：

| 参数 | 值 | 说明 |
| --- | --- | --- |
| 采样率 | 44100 Hz | CD音质标准 |
| 声道数 | 2 | 立体声 |
| 位深度 | 16-bit | S16LE格式 |
| 编码类型 | RAW | PCM原始数据 |

### 开发步骤

1. 通过[audio.createAudioCapturer()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiocapturer8)创建音频采集器。

```typescript
try {
  this.audioCapturer = await audio.createAudioCapturer({
    streamInfo: {
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
      channels: audio.AudioChannel.CHANNEL_2,
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
    },
    capturerInfo: {
      source: audio.SourceType.SOURCE_TYPE_MIC,
      capturerFlags: 0
    }
  });
  // ...
  Logger.info(TAG, 'AudioCapturer created & started');
} catch (error) {
  Logger.error(TAG, `startCapturer failed, code is ${error.code}, message is ${error.message}`);
}
```

2. 通过[on('readData')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onreaddata11)设置录音回调，将接收到的PCM音频数据保存到文件中。

```typescript
this.audioCapturer.on('readData', (buffer: ArrayBuffer): void => {
  if (!this.isCapturing || !buffer) {
    return;
  }
  // Write to file for recording
  if (this.recordingFile) {
    try {
      fs.writeSync(this.recordingFile.fd, buffer);
      this.recordedBytes += buffer.byteLength;
    } catch (error) {
      Logger.error(TAG, 'File write failed');
      fs.closeSync(this.recordingFile.fd);
      this.recordingFile = null;
    }
  }
});
```

3. 通过[start()](../harmonyos-references/arkts-apis-audio-audiocapturer.md#start8)启动录音。

```typescript
// Start AudioCapturer
await this.audioCapturer.start();
```

## 人声和伴奏混音合成

### 场景描述

录音后将人声和伴奏混音并合成一个文件，文件可以直接预览、导出或发布。单击首页面底部的音量按钮，弹出音量设置面板，打开混录模式，可以启用混音合成功能。混录模式设置如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/UdVx0AviRYqgt2ACjPMCOg/zh-cn_image_0000002684119549.png "点击放大")

### 实现原理

提取[K歌录音采集](bpta-karaoke-singing.md#section5737811161413)保存的人声PCM数据，然后与伴奏的PCM数据进行混合。混合时保持人声不变，按照伴奏的音量调整伴奏PCM数据。

**说明** 

混合公式为：PCM混音数据 = 人声PCM数据 + 伴奏PCM数据 x 伴奏音量。

### 开发步骤

1. 读取人声PCM数据。

```cpp
// Load voice pcm data
bool LoadVoicePcm(char *voicePath, std::vector<uint8_t> &voicePcmData) {
    std::ifstream voiceFile(voicePath, std::ios::binary);
    if (!voiceFile.is_open()) {
        OH_LOG_ERROR(LOG_APP, "Failed to open voice file: %{public}s", voicePath);
        return false;
    }

    voiceFile.seekg(0, std::ios::end);
    size_t voiceFileSize = voiceFile.tellg();
    voiceFile.seekg(0, std::ios::beg);

    if (voiceFileSize <= WAV_HEADER_SIZE) {
        OH_LOG_ERROR(LOG_APP, "Voice file too small: %{public}zu", voiceFileSize);
        voiceFile.close();
        return false;
    }

    size_t voicePcmSize = voiceFileSize - WAV_HEADER_SIZE;
    voicePcmData.resize(voicePcmSize);
    voiceFile.read(reinterpret_cast<char *>(voicePcmData.data()), voicePcmSize);
    if (voiceFile.gcount() != voicePcmSize) {
        OH_LOG_ERROR(LOG_APP, "Failed to read voice file");
        voiceFile.close();
        return false;
    }
    voiceFile.close();
    return true;
}
```

2. 读取伴奏PCM数据。

```cpp
RawFile *rawFile = OH_ResourceManager_OpenRawFile(g_resourceManager, wavFileName.c_str());
if (!rawFile) {
    OH_LOG_ERROR(LOG_APP, "%s not found in rawfile", wavFileName.c_str());
    napi_value result;
    napi_get_boolean(env, false, &result);
    return result;
}

int64_t wavFileSize = OH_ResourceManager_GetRawFileSize(rawFile);
if (wavFileSize <= WAV_HEADER_SIZE) {
    OH_LOG_ERROR(LOG_APP, "WAV file too small: %{public}ld", wavFileSize);
    OH_ResourceManager_CloseRawFile(rawFile);
    napi_value result;
    napi_get_boolean(env, false, &result);
    return result;
}

std::vector<uint8_t> wavData(wavFileSize);
OH_ResourceManager_ReadRawFile(rawFile, wavData.data(), wavFileSize);
OH_ResourceManager_CloseRawFile(rawFile);

size_t pcmSize = wavFileSize - WAV_HEADER_SIZE;
g_accompanimentPcmData.assign(wavData.begin() + WAV_HEADER_SIZE, wavData.end());
g_accompanimentLoaded = true;
```

3. 混合人声PCM数据和伴奏PCM数据。

```cpp
// Simple mixing: voice + accompaniment * musicVolume
// Assumes both are 16-bit PCM
for (size_t i = 0; i < mixSize; i += DEFAULT_BITS_PER_SAMPLE / SIZE_8BITS) {
    if (i + 1 < mixSize) {
        // Read voice sample (16-bit little-endian)
        int16_t voiceSample = static_cast<int16_t>(voicePcmData[i] | (voicePcmData[i + 1] << SHIFT_8BITS));
        // Read accompaniment sample
        int16_t musicSample = 0;
        if (i + 1 < accompanimentPcmData.size()) {
            musicSample =
                static_cast<int16_t>(accompanimentPcmData[i] | (accompanimentPcmData[i + 1] << SHIFT_8BITS));
        }
        // Mix (voice + accompaniment * volume)
        int32_t mixedSample = voiceSample + static_cast<int32_t>(musicSample * musicVolume);
        // Prevent overflow: clamp to 16-bit PCM range
        if (mixedSample > PCM_16BIT_MAX) {
            mixedSample = PCM_16BIT_MAX;
        } else if (mixedSample < PCM_16BIT_MIN) {
            mixedSample = PCM_16BIT_MIN;
        }
        // Write mixed sample
        int16_t finalSample = static_cast<int16_t>(mixedSample);
        mixedPcmData[i] = static_cast<uint8_t>(finalSample & 0xFF);
        mixedPcmData[i + 1] = static_cast<uint8_t>((finalSample >> SHIFT_8BITS) & 0xFF);
    }
}
```

## K歌音频耳返

### 场景描述

耳返是指通过耳机系统将音频实时传输到耳机中，让使用者能够听到自己的声音、伴奏或其它需要的信息。在K歌类应用中，将录制的人声和背景音乐实时传输到耳机中，使用户通过反馈即时调整，获得更好的使用体验。单击首页面底部的音量按钮，弹出音量设置面板，可以在耳返模式中设置硬件耳返、软件耳返，可以调节耳返音量。耳返设置如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ZQvXcyUbR9yjq_73Tvp7Ug/zh-cn_image_0000002684279371.png "点击放大")

### 实现原理

当前系统支持硬件耳返和软件耳返两种方案，具体原理可参考：[基于Audio能力实现音频耳返](bpta-audio-in-ear-monitor.md)，实现方式如下表：

| 耳返模式 | 实现方式 |
| --- | --- |
| 硬件耳返 | AudioLoopback |
| 软件耳返 | AudioCapturer + AudioRenderer |

### 开发步骤

1. 硬件耳返。

* 通过[isAudioLoopbackSupported()](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isaudioloopbacksupported20)查询当前系统是否支持音频返听模式。若支持，则调用[audio.createAudioLoopback()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudioloopback20)接口创建音频返听器。

  ```typescript
  const mode: audio.AudioLoopbackMode = audio.AudioLoopbackMode.HARDWARE;
  const streamManager = this.audioManager.getStreamManager();
  if (!streamManager.isAudioLoopbackSupported(mode)) {
    return { success: false, error: 'AudioLoopback not supported' };
  }

  this.audioLoopback = await audio.createAudioLoopback(mode);
  Logger.info(TAG, 'AudioLoopback created');
  ```
* 通过[getStatus()](../harmonyos-references/arkts-apis-audio-audioloopback.md#getstatus20)获取音频返听状态，当返听状态为[AudioLoopbackStatus](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackstatus20).AVAILABLE\_IDLE时，表示返听可用，此时可调用[enable()](../harmonyos-references/arkts-apis-audio-audioloopback.md#enable20)方法传入参数true，开启音频返听。

  ```typescript
  const status = await this.audioLoopback.getStatus();
  if (status === audio.AudioLoopbackStatus.AVAILABLE_RUNNING) {
    return { success: true };
  }
  if (status !== audio.AudioLoopbackStatus.AVAILABLE_IDLE) {
    return { success: false, error: 'AudioLoopback invalid state: ' + status };
  }
  const success = await this.audioLoopback.enable(true);
  if (!success) {
    return { success: false, error: 'AudioLoopback enable failed' };
  }
  ```
* 通过[setVolume()](../harmonyos-references/arkts-apis-audio-audioloopback.md#setvolume20)调节音频返听音量。

  ```typescript
  try {
    await this.audioLoopback.setVolume(volume);
  } catch (error) {
    Logger.error(TAG, 'AudioLoopback setVolume failed');
  }
  ```

2. 软件耳返。

* 根据[K歌录音采集](bpta-karaoke-singing.md#section5737811161413)保存录制的音频数据用于耳返播放。
* 通过[audio.createAudioRenderer()](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)创建音频播放器，播放参数与[K歌录音采集](bpta-karaoke-singing.md#section5737811161413)的录音参数相同。

  ```typescript
  this.audioRenderer = await audio.createAudioRenderer({
    streamInfo: {
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
      channels: audio.AudioChannel.CHANNEL_2,
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
    },
    rendererInfo: {
      usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
      rendererFlags: 0
    }
  });
  ```
* 通过[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)设置播放回调，将[K歌录音采集](bpta-karaoke-singing.md#section5737811161413)录制的PCM音频数据写入到回调事件中。

  ```typescript
  let bufferSize: number = this.recordedBytes;
  this.writeDataCallback = (buffer: ArrayBuffer): audio.AudioDataCallbackResult | void => {
    if (!this.rendererFile) {
      Logger.error(TAG, 'rendererFile is undefined');
      return audio.AudioDataCallbackResult.INVALID;
    }
    let options: Options = {
      offset: bufferSize,
      length: buffer.byteLength
    };
    let bufferLength = 0;
    try {
      bufferLength = fs.readSync(this.rendererFile.fd, buffer, options);
    } catch (error) {
      Logger.error(TAG, `Error reading file, code is ${error.code}, message is ${error.message}`);
      return audio.AudioDataCallbackResult.INVALID;
    }

    bufferSize += bufferLength;
    if (bufferLength < buffer.byteLength) {
      let view = new DataView(buffer);
      for (let i = bufferLength; i < buffer.byteLength; i++) {
        view.setUint8(i, 0);
      }
    }
    return audio.AudioDataCallbackResult.VALID;
  };
  ```
* 通过[start()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)启动播放。

  ```typescript
  // Start audioRenderer
  await this.audioRenderer.start();
  ```
* 通过[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)调节音频返听音量。

  ```typescript
  try {
    await this.audioRenderer.setVolume(volume);
  } catch (error) {
    Logger.error(TAG, 'AudioRenderer setVolume failed');
  }
  ```

## K歌混响音效

### 场景描述

混响是K歌核心音频美化功能，通过模拟不同的环境效果，让声音更饱满通透。单击首页面底部的音效按钮，弹出音效设置面板，可以选择不同的混响音效。音效设置面板如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/0mW4E68aTQqXIEVRw1_JLA/zh-cn_image_0000002654119838.png "点击放大")

### 实现原理

使用AudioLoopback启用硬件耳返后，通过[setReverbPreset()](../harmonyos-references/arkts-apis-audio-audioloopback.md#setreverbpreset21)可以设置耳返的混响模式。[AudioLoopbackReverbPreset](../harmonyos-references/arkts-apis-audio-e.md#audioloopbackreverbpreset21)混响预置类型如下：

| 名称 | 枚举值 | 数值 | 效果描述 |
| --- | --- | --- | --- |
| ORIGINAL | AudioLoopbackReverbPreset.ORIGINAL | 1 | 保持原始混响，不进行任何增强。 |
| KTV | AudioLoopbackReverbPreset.KTV | 2 | KTV风格混响。 |
| THEATER | AudioLoopbackReverbPreset.THEATER | 3 | 剧场风格混响。 |
| CONCERT | AudioLoopbackReverbPreset.CONCERT | 4 | 演唱会风格混响。 |

**说明** 

混响音效只在硬耳返开启时生效，软耳返不支持。

### 开发步骤

通过[setReverbPreset()](../harmonyos-references/arkts-apis-audio-audioloopback.md#setreverbpreset21)设置耳返的混响模式。

```typescript
setReverbEffect(preset: audio.AudioLoopbackReverbPreset): void {
  if (!this.audioLoopback) {
    return;
  }
  try {
    this.audioLoopback.setReverbPreset(preset);
  } catch (error) {
    Logger.error(TAG, 'AudioLoopback setReverbPreset failed');
  }
}
```

## K歌设备检测管理

### 场景描述

在K歌时，实时检测耳机的连接状态，并根据状态变化做对应处理，处理方式如下表所示：

| 场景 | 处理方法 |
| --- | --- |
| 有线耳机连接 | 更新设备状态，允许开启耳返 |
| 有线耳机断开 | 自动关闭耳返，提示用户 |
| 蓝牙耳机连接/断开 | 更新设备名称显示 |

单击首页面底部的设备按钮，弹出设备面板，用于显示设备连接状态。设备面板如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Deao9xGASuiJQCEIW3X-ZA/zh-cn_image_0000002653959928.png "点击放大")

### 实现原理

AudioRoutingManager提供管理全局音频设备的能力，包括查询设备信息、监听设备连接状态变化等。

### 开发步骤

1. 创建AudioRoutingManager实例。

```typescript
// Get AudioRoutingManager
this.audioManager = audio.getAudioManager();
this.audioRoutingManager = this.audioManager.getRoutingManager();
```

2. 通过[on('deviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#ondevicechange9)监听音频设备连接状态的变化。

```typescript
const listener = async (deviceChangeInfo: audio.DeviceChangeAction): Promise<void> => {
  Logger.info(TAG, '========== DEVICE CHANGE EVENT ==========');
  Logger.info(TAG, `Change type=${deviceChangeInfo.type}`);

  if (!deviceChangeInfo.deviceDescriptors || deviceChangeInfo.deviceDescriptors.length === 0) {
    return;
  }
  for (let i = 0; i < deviceChangeInfo.deviceDescriptors.length; i++) {
    const dev = deviceChangeInfo.deviceDescriptors[i];
    Logger.info(TAG, `Changed device type=${dev.deviceType} role=${dev.deviceRole}`);
  }

  // Record previous headset status
  const previousWiredHeadset = this.deviceState.hasWiredHeadset;

  // Query latest device status
  await this.queryAudioDevices();

  // Notify all registered callbacks
  for (const callback of this.callbacks) {
    callback(this.deviceState, previousWiredHeadset);
  }
};

this.deviceChangeListener = listener;
this.audioRoutingManager?.on('deviceChange', audio.DeviceFlag.ALL_DEVICES_FLAG, listener);
```

3. 通过[getDevices()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9)获取音频设备列表，通过设备的[DeviceType](../harmonyos-references/arkts-apis-audio-e.md#devicetype)获取有线耳机和蓝牙耳机的状态，通过设备名称获取蓝牙耳机的名称。

```typescript
const allDevices: audio.AudioDeviceDescriptors =
  await this.audioRoutingManager.getDevices(audio.DeviceFlag.ALL_DEVICES_FLAG);
Logger.info(TAG, `getDevices returned, count=${allDevices.length}`);

// Reset device status
this.deviceState.hasWiredHeadset = false;
this.deviceState.hasBluetoothHeadset = false;
this.deviceState.bluetoothDeviceName = '';

// Iterate all devices to detect wired and bluetooth headset
for (let i = 0; i < allDevices.length; i++) {
  const device: audio.AudioDeviceDescriptor = allDevices[i];
  Logger.info(TAG, `=== Device[${i}] ===`);
  Logger.info(TAG, `  type=${device.deviceType}`);
  Logger.info(TAG, `  role=${device.deviceRole}`);

  if (this.isWiredHeadsetType(device.deviceType)) {
    this.deviceState.hasWiredHeadset = true;
    Logger.info(TAG, '  >>> WIRED/USB HEADSET DETECTED!');
  } else if (this.isBluetoothHeadsetType(device.deviceType)) {
    this.deviceState.hasBluetoothHeadset = true;
    this.deviceState.bluetoothDeviceName = device.name;
    Logger.info(TAG, '  >>> BLUETOOTH HEADSET DETECTED!');
  }
}
```

```typescript
isWiredHeadsetType(deviceType: number): boolean {
  return deviceType === audio.DeviceType.WIRED_HEADSET ||
    deviceType === audio.DeviceType.WIRED_HEADPHONES ||
    deviceType === audio.DeviceType.USB_HEADSET;
}
```

```typescript
isBluetoothHeadsetType(deviceType: number): boolean {
  return deviceType === audio.DeviceType.BLUETOOTH_SCO || deviceType === audio.DeviceType.BLUETOOTH_A2DP;
}
```

4. 检测到有线耳机断开后，关闭耳返并提示用户。

```typescript
// Handle wired headset disconnect
if (previousWiredHeadset && !state.hasWiredHeadset && this.earMonitorEnabled) {
  this.setEarMonitorEnabled(false);
  AppStorage.setOrCreate(KeyConstants.KEY_EAR_ENABLED, this.earMonitorEnabled);
  this.showToast($r('app.string.wired_headset_offline'));
}
```

## 示例代码

* [开发K歌应用](https://gitcode.com/HarmonyOS_Samples/KaraokeSinging)
