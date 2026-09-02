---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-audiorenderer-for-playback
title: 使用AudioRenderer开发音频播放功能(ArkTS)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 使用AudioRenderer开发音频播放功能(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce907ac0928bba38d624b9cf9054d43218173f4dc2b2154dc3dc6a5b1de5e382
---

AudioRenderer是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据，相比[AVPlayer](using-avplayer-for-playback.md)而言，可以在输入前添加数据预处理，更适合有音频开发经验的开发者，以实现更灵活的播放功能。

## 开发指导

使用AudioRenderer播放音频涉及到AudioRenderer实例的创建、音频渲染参数的配置、渲染的开始与停止、资源的释放等。本开发指导将以一次渲染音频数据的过程为例，向开发者讲解如何使用AudioRenderer进行音频渲染，建议搭配[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的API说明阅读。

下图展示了AudioRenderer的状态变化，在创建实例后，调用对应的方法可以进入指定的状态实现对应的行为。需要注意的是在确定的状态执行不合适的方法可能导致AudioRenderer发生错误，建议开发者在调用状态转换的方法前进行状态检查，避免程序运行产生预期以外的结果。

为保证UI线程不被阻塞，大部分AudioRenderer调用都是异步的。对于每个API均提供了callback函数和Promise函数，以下示例均采用callback函数。

在进行应用开发的过程中，建议开发者通过[on('stateChange')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onstatechange8)方法订阅AudioRenderer的状态变更。因为针对AudioRenderer的某些操作，仅在音频播放器在固定状态时才能执行。如果应用在音频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。

* prepared状态：通过调用[audio.createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)方法进入到该状态。
* running状态：正在进行音频数据播放，可以在prepared状态通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入此状态，也可以在paused状态和stopped状态通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入此状态。
* paused状态：在running状态可以通过调用[pause](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)方法暂停音频数据的播放并进入paused状态，暂停播放之后可以通过调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法继续音频数据播放。
* stopped状态：在paused/running状态可以通过[stop](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)方法停止音频数据的播放。
* released状态：在prepared、paused、stopped等状态，用户均可通过[release](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)方法释放掉所有占用的硬件和软件资源，并且不会再进入其他任何状态。

当音频流处于工作状态（非released状态）时，会占用系统的音频流资源。由于系统对音频流数量有限制，所以当客户端暂时不使用音频流时，调用release()回收音频资源，做好资源利用，避免后续创建音频流失败。

**图1** AudioRenderer状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Ucqwt7SqQOeJDBB_ggQt5g/zh-cn_image_0000002736313579.png)

### 开发步骤及注意事项

以下各步骤示例为代码片段，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

1. 配置音频渲染参数并创建AudioRenderer实例，音频渲染参数的详细信息可以查看[AudioRendererOptions](../harmonyos-references/arkts-apis-audio-i.md#audiorendereroptions8)。

   ```typescript
   import { audio } from '@kit.AudioKit';
   // ...
   // 从API版本26.0.0开始，参数samplingRate支持number类型。
   // 音频渲染扩展支持8000Hz到384000Hz范围内以10Hz为步长的采样率值。具体设备支持的采样率规格会存在差异。
   let audioStreamInfo: audio.AudioStreamInfo = {
     samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
     channels: audio.AudioChannel.CHANNEL_2, // 通道。
     sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
     encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
   };
   let audioRendererInfo: audio.AudioRendererInfo = {
     usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
     rendererFlags: 0 // 音频渲染器标志。
   };
   let audioRendererOptions: audio.AudioRendererOptions = {
     streamInfo: audioStreamInfo,
     rendererInfo: audioRendererInfo
   };
   // ...
     audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例。
       if (!err) {
         console.info('Succeeded in creating audio renderer.');
         // ...
         audioRenderer = renderer;
         if (audioRenderer !== undefined) {
           audioRenderer.on('writeData', writeDataCallback);
           // ...
         }
       } else {
         console.error(`Failed to create audio renderer. Code: ${err.code}, message: ${err.message}`);
         globalLogUpdate(`Failed to create audio renderer. Code: ${err.code}, message: ${err.message}`, false);
       }
     });
   ```
2. 调用[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)方法，订阅音频数据写入回调，推荐使用API version 12支持返回回调结果的方式。

   * API version 12开始该方法支持返回回调结果，系统可以根据开发者返回的值来决定此次回调中的数据是否播放。

     **注意** 

     + 能填满回调所需长度数据的情况下，返回audio.AudioDataCallbackResult.VALID，系统会取用完整长度的数据缓冲进行播放。请不要在未填满数据的情况下返回audio.AudioDataCallbackResult.VALID，否则会导致杂音、卡顿等现象。
     + 在无法填满回调所需长度数据的情况下，建议开发者返回audio.AudioDataCallbackResult.INVALID，系统不会处理该段音频数据，然后会再次向应用请求数据，确认数据填满后返回audio.AudioDataCallbackResult.VALID。
     + 回调函数结束后，音频服务会把缓冲中数据放入队列里等待播放，因此请勿在回调外再次更改缓冲中的数据。对于最后一帧，如果数据不够填满缓冲长度，开发者需要使用剩余数据拼接空数据的方式，将缓冲填满，避免缓冲内的历史脏数据对播放效果产生不良的影响。

     ```typescript
     import { audio } from '@kit.AudioKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { fileIo as fs } from '@kit.CoreFileKit';
     import { common } from '@kit.AbilityKit';
     // ...
     class Options {
       public offset?: number;
       public length?: number;
     }
     // ...
       let bufferSize: number = 0;
       let file = await context.resourceManager.getRawFd('S16LE_2_48000.pcm');
       writeDataCallback = (buffer: ArrayBuffer) => {
         let options: Options = {
           offset: bufferSize + file.offset,
           length: buffer.byteLength
         };
         if (bufferSize > file.length) {
           return audio.AudioDataCallbackResult.INVALID;
         }
         try {
           let bufferLength = fs.readSync(file.fd, buffer, options);
           bufferSize += buffer.byteLength;
           // 系统会判定buffer有效，正常播放。
           // ...
           return audio.AudioDataCallbackResult.VALID;
         } catch (error) {
           console.error(`Failed to read file. Code: ${error.code}, message: ${error.message}`);
           // 系统会判定buffer无效，不播放。
           // ...
           return audio.AudioDataCallbackResult.INVALID;
         }
       };
       // ...
             audioRenderer.on('writeData', writeDataCallback);
     ```
   * API version 11该方法不支持返回回调结果，系统默认回调中的数据均为有效数据。

     **注意** 

     + 开发者应避免在主线程中注册回调，以免被其他业务阻塞导致响应回调不及时造成卡顿。建议使用独立的异步线程池处理回调。
     + 请确保填满回调所需长度数据，否则会导致杂音、卡顿等现象。
     + 在无法填满回调所需长度数据的情况下，建议开发者选择暂时停止写入数据（不暂停音频流），阻塞回调函数，等待数据充足时，再继续写入数据，确保数据填满。在阻塞回调函数后，如需调用AudioRenderer相关接口，需先解阻塞。
     + 开发者如果不希望播放本次回调中的音频数据，可以主动将回调中的数据块置空（置空后，也会被系统统计到已写入的数据，播放静音帧）。
     + 回调函数结束后，音频服务会把缓冲中数据放入队列里等待播放，因此请勿在回调外再次更改缓冲中的数据。对于最后一帧，如果数据不够填满缓冲长度，开发者需要使用剩余数据拼接空数据的方式，将缓冲填满，避免缓冲内的历史脏数据对播放效果产生不良的影响。
     + 在写数据回调中，避免与耗时业务耦合或等待其他业务操作，例如写数据时不要等待UI绘制。否则，可能会导致数据传输不及时，从而产生卡顿现象。

     ```typescript
     import { BusinessError } from '@kit.BasicServicesKit';
     import { fileIo as fs } from '@kit.CoreFileKit';
     import { common } from '@kit.AbilityKit';
     // ...
     class Options {
       public offset?: number;
       public length?: number;
     }
     // ...
       let bufferSize: number = 0;
       let file = await context.resourceManager.getRawFd('S16LE_2_48000.pcm');
       writeDataCallback = (buffer: ArrayBuffer) => {
         let options: Options = {
           offset: bufferSize + file.offset,
           length: buffer.byteLength
         };
         // ...
             audioRenderer.on('writeData', writeDataCallback);
     ```
3. 调用[start](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法进入running状态，开始渲染音频。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...
       audioRenderer.start((err: BusinessError) => {
         if (err) {
           console.error(`Failed to start audio renderer. Code: ${err.code}, message: ${err.message}`);
           // ...
         } else {
           console.info('Succeeded in starting audio renderer.');
           // ...
         }
       });
   ```
4. 调用[stop](../harmonyos-references/arkts-apis-audio-audiorenderer.md#stop8)方法停止渲染。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...
       audioRenderer.stop((err: BusinessError) => {
         if (err) {
           console.error(`Failed to stop audio renderer. Code: ${err.code}, message: ${err.message}`);
           // ...
         } else {
           console.info('Succeeded in stopping audio renderer.');
           // ...
         }
       });
   ```
5. 调用[release](../harmonyos-references/arkts-apis-audio-audiorenderer.md#release8)方法销毁实例，释放资源。

   应用需根据实际业务需求合理使用AudioRenderer实例，按需创建并及时释放，避免占用过多音频资源导致异常。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...
       audioRenderer.release((err: BusinessError) => {
         if (err) {
           console.error(`Failed to release audio renderer. Code: ${err.code}, message: ${err.message}`);
           // ...
         } else {
           console.info('Succeeded in releasing audio renderer.');
           // ...
         }
       });
       // 关闭沙箱文件。
       await context.resourceManager.closeRawFd('S16LE_2_48000.pcm');
   ```

### 选择正确的StreamUsage

创建AudioRenderer实例时，开发者需要根据应用场景指定播放器的StreamUsage，选择正确的StreamUsage可以避免用户遇到不符合预期的行为。

在音频API文档[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)介绍中，列举了每一种类型推荐的应用场景。例如音乐场景推荐使用STREAM\_USAGE\_MUSIC，电影或者视频场景推荐使用STREAM\_USAGE\_MOVIE，游戏场景推荐使用STREAM\_USAGE\_GAME，等等。

如果开发者配置了不正确的StreamUsage，可能带来一些不符合预期的行为。例如以下场景。

* 游戏场景错误使用STREAM\_USAGE\_MUSIC类型，游戏应用将无法和其他音乐应用并发播放，而游戏场景通常可以与其他音乐应用并发播放。
* 导航场景错误使用STREAM\_USAGE\_MUSIC类型，导航应用播报时会导致正在播放的音乐停止播放，而导航场景我们通常期望正在播放的音乐仅降低音量播放。

### 配置合适的音频采样率

采样率：指音频每秒单个声道样点数，单位为Hz。

重采样：根据输入输出音频采样率的差异，进行上采样（通过插值增加样点数）或下采样（通过抽取减少样点数）。

AudioRenderer支持枚举类型[AudioSamplingRate](../harmonyos-references/arkts-apis-audio-e.md#audiosamplingrate8)中定义的所有采样率。

若通过AudioRenderer设置的输入音频采样率与设备输出采样率不一致，系统会将输入音频重采样为设备输出采样率。

若为减少重采样功耗，可使用采样率与输出设备采样率一致的输入音频。推荐使用48k采样率。

### 完整示例

下面展示了使用AudioRenderer渲染音频文件的示例代码。

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
// ...
class Options {
  public offset?: number;
  public length?: number;
}
// ...

let audioRenderer: audio.AudioRenderer | undefined = undefined;
// 从API版本26.0.0开始，参数samplingRate支持number类型。
// 音频渲染扩展支持8000Hz到384000Hz范围内以10Hz为步长的采样率值。具体设备支持的采样率规格会存在差异。
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};
let writeDataCallback: audio.AudioRendererWriteDataCallback;

async function initArguments(context: common.UIAbilityContext) {
  let bufferSize: number = 0;
  let file = await context.resourceManager.getRawFd('S16LE_2_48000.pcm');
  writeDataCallback = (buffer: ArrayBuffer) => {
    let options: Options = {
      offset: bufferSize + file.offset,
      length: buffer.byteLength
    };
    if (bufferSize > file.length) {
      return audio.AudioDataCallbackResult.INVALID;
    }
    try {
      let bufferLength = fs.readSync(file.fd, buffer, options);
      bufferSize += buffer.byteLength;
      // 系统会判定buffer有效，正常播放。
      if (bufferSize > file.length) {
        let view = new DataView(buffer);
        for (let i = bufferSize - file.length; i < buffer.byteLength; i++) {
          // 空白区域填充静音数据。当使用音频采样格式为SAMPLE_FORMAT_U8时0x80为静音数据，使用其他采样格式时0为静音数据。
          view.setUint8(i, 0);
        }
      }
      // API version 11不支持返回回调结果，从API version 12开始支持返回回调结果。
      // 如果开发者不希望播放某段buffer，返回audio.AudioDataCallbackResult.INVALID即可。
      return audio.AudioDataCallbackResult.VALID;
    } catch (error) {
      console.error(`Failed to read file. Code: ${error.code}, message: ${error.message}`);
      // ...
      // API version 11不支持返回回调结果，从API version 12开始支持返回回调结果。
      return audio.AudioDataCallbackResult.INVALID;
    }
  };
}

// 初始化，创建实例，设置监听事件。
async function init() {
  audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建AudioRenderer实例。
    if (!err) {
      console.info('Succeeded in creating audio renderer.');
      // ...
      audioRenderer = renderer;
      if (audioRenderer !== undefined) {
        audioRenderer.on('writeData', writeDataCallback);
        // ...
      }
    } else {
      console.error(`Failed to create audio renderer. Code: ${err.code}, message: ${err.message}`);
      // ...
    }
  });
}

// 开始一次音频渲染。
async function start() {
  if (audioRenderer !== undefined) {
    let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
    if (stateGroup.indexOf(audioRenderer.state.valueOf()) === -1) { // 当且仅当状态为prepared、paused和stopped之一时才能启动渲染。
      console.error('Audio renderer state is invalid.');
      // ...
      return;
    }
    // 启动渲染。
    audioRenderer.start((err: BusinessError) => {
      if (err) {
        console.error(`Failed to start audio renderer. Code: ${err.code}, message: ${err.message}`);
        // ...
      } else {
        console.info('Succeeded in starting audio renderer.');
        // ...
      }
    });
  }
}

async function pause() {
  // 暂停渲染。
  if (audioRenderer !== undefined) {
    // 只有渲染器状态为running的时候才能暂停。
    if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING) {
      console.info('Audio renderer state is not running.');
      // ...
      return;
    }
    // 暂停渲染。
    audioRenderer.pause((err: BusinessError) => {
      if (err) {
        console.error(`Failed to pause audio renderer. Code: ${err.code}, message: ${err.message}`);
        // ...
      } else {
        console.info('Succeeded in pausing audio renderer.');
        // ...
      }
    });
  }
}

// 停止渲染。
async function stop() {
  if (audioRenderer !== undefined) {
    // 只有渲染器状态为running或paused的时候才可以停止。
    if (audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING &&
      audioRenderer.state.valueOf() !== audio.AudioState.STATE_PAUSED) {
      console.info('Audio renderer state is not running or paused.');
      // ...
      return;
    }
    // 停止渲染。
    audioRenderer.stop((err: BusinessError) => {
      if (err) {
        console.error(`Failed to stop audio renderer. Code: ${err.code}, message: ${err.message}`);
        // ...
      } else {
        console.info('Succeeded in stopping audio renderer.');
        // ...
      }
    });
  }
}

// 销毁实例，释放资源。
async function release(context: common.UIAbilityContext) {
  if (audioRenderer !== undefined) {
    // 渲染器状态不是released状态，才能release。
    if (audioRenderer.state.valueOf() === audio.AudioState.STATE_RELEASED) {
      console.info('Audio renderer state is released.');
      // ...
      return;
    }

    // ...

    // 释放资源。
    audioRenderer.release((err: BusinessError) => {
      if (err) {
        console.error(`Failed to release audio renderer. Code: ${err.code}, message: ${err.message}`);
        // ...
      } else {
        console.info('Succeeded in releasing audio renderer.');
        // ...
      }
    });
    // 关闭沙箱文件。
    await context.resourceManager.closeRawFd('S16LE_2_48000.pcm');
  }
}
```

当同优先级或高优先级音频流要使用输出设备时，当前音频流会被中断，应用可以自行响应中断事件并做出处理。具体的音频并发处理方式可参考[处理音频焦点事件](audio-playback-concurrency.md)。
