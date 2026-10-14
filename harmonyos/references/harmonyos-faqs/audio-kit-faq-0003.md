---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/audio-kit-faq-0003
title: 音频录制功能实现与状态检测常见问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 常见问题 > 音频录制功能实现与状态检测常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:39+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:5d34d0591ac6950afe7648ea68c5aa2668aa759008c8a64410c8f5d965f144c5
---

**Q：使用AVRecorder录制WAV封装格式的音频文件，编码格式只能使用Audio\_G711MU，采样率只能选择8000Hz。语音识别要求输入数据为16000Hz采样率、PCM编码格式的音频数据。使用AVRecorder录制WAV音频后，如何将音频文件识别为文字？**

**A**：[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)录制WAV封装格式的音频文件时，目前只支持采样率为8000Hz的G711MU编码格式，不支持录制采样率16000Hz的PCM编码格式的WAV音频文件。可以通过三方库[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令，将AVRecorder录制G711MU编码的音频文件转换为语音识别支持的PCM音频文件，然后通过语音识别将录制的音频文件识别为文字。

1. 使用[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)录制WAV封装格式的音频文件，编码格式为G711MU、采样率8000Hz、单声道、比特率64000bps：

   ```ts
   let avProfile: media.AVRecorderProfile = {
         audioChannels: 1, // 音频声道数目，单声道
         audioBitrate: 64000, // 音频比特率
         audioSampleRate: 8000, // 音频采样率
         audioCodec: media.CodecMimeType.AUDIO_G711MU, // 音频编码格式
         fileFormat: media.ContainerFormatType.CFT_WAV, // 音频封装格式
       };
   ```
2. 使用[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令，生成采样率16000Hz、采样位数16位、单通道的PCM音频文件用于语音识别：

   ```ts
   async convert2PCM(wavFilePath: string, pcmFilePath: string) {
       try {
         if (fileIo.accessSync(pcmFilePath)) {
           fileIo.unlinkSync(pcmFilePath);
         }
       } catch (err) {
         console.error(`Failed to unlink ${pcmFilePath}, ${JSON.stringify(err)}`);
         return;
       }

       let callback: ICallBack = {
         callBackResult: (code: number) => {
           if (code === 0) {
             console.info(`Convert succeed`);
           } else {
             console.info(`Convert failed`);
           }
         },
       };
       let cmd = `ffmpeg -i ${wavFilePath} -acodec pcm_s16le -ar 16000 -ac 1 -f s16le ${pcmFilePath}`;
       MP4Parser.ffmpegCmd(cmd, callback);
     }
   ```
3. 启动语音识别，读取PCM音频文件，通过[writeAudio](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)接口持续写入待识别音频数据，并监听识别结果：

   ```ts
   onStart: (sessionId: string, eventMessage: string) => {
           console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
           let audioBuf = new Uint8Array(bufSize);
           try {
             this.pcmFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY);
           } catch (err) {
             console.error(`Failed to open pcm file ${pcmFilePath}, ${JSON.stringify(err)}`);
             this.asrEngine?.finish(this.sessionId);
           }
           let intervalId = setInterval(() => {
             try {
               if (this.asrEngine?.isBusy()) {
                 return;
               }
               let readLen = fileIo.readSync(this.pcmFile?.fd, audioBuf.buffer.slice(0));
               if (readLen === 0) {
                 clearInterval(intervalId);
                 this.asrEngine?.finish(this.sessionId);
               }
               this.asrEngine?.writeAudio(this.sessionId, audioBuf);
             } catch (err) {
               this.asrEngine?.finish(this.sessionId);
               console.error(`Failed to write audio data, ${JSON.stringify(err)}`);
             }
           }, intervalMS);
         },
   ```

完整参考代码如下：

```ts
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { ICallBack, MP4Parser } from '@ohos/mp4parser';
import { speechRecognizer } from '@kit.CoreSpeechKit';
import { util } from '@kit.ArkTS';

const bufSize: number = 1280;
const intervalMS: number = 40;
const wavFileName: string = 'example.wav';
const pcmFileName: string = 'example.pcm';

function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(context, permissions)
    .catch((err: BusinessError) => {
      console.error(`Failed to request permissions from user, code: ${err.code}, message: ${err.message}`);
    });
}

@Entry
@Component
struct WavAudioRecognizeDemo {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private asrEngine?: speechRecognizer.SpeechRecognitionEngine;
  private avRecorder?: media.AVRecorder = undefined;
  private wavFile?: fileIo.File = undefined;
  private pcmFile?: fileIo.File = undefined;
  private sessionId: string = '';

  aboutToAppear(): void {
    const permissions: Permissions[] = ['ohos.permission.MICROPHONE'];
    reqPermissionsFromUser(permissions, this.context);
  }

  async startAudioRecording(context: common.Context): Promise<void> {
    try {
      this.avRecorder = await media.createAVRecorder();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to create avRecorder, error code: ${err.code}, message: ${err.message}`);
      return;
    }

    try {
      this.avRecorder.on('stateChange', (state: media.AVRecorderState, reason: media.StateChangeReason) => {
        console.info(`AVRecorder state is changed to ${state}, reason: ${reason}`);
      });
      this.avRecorder.on('error', (error: BusinessError) => {
        console.error(`Error occurred in avRecorder, error code: ${error.code}, message: ${error.message}`);
      });
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to set avRecorder callback, error code: ${err.code}, message: ${err.message}`);
    }
    let avProfile: media.AVRecorderProfile = {
      audioChannels: 1, // 音频声道数目，单声道
      audioBitrate: 64000, // 音频比特率
      audioSampleRate: 8000, // 音频采样率
      audioCodec: media.CodecMimeType.AUDIO_G711MU, // 音频编码格式
      fileFormat: media.ContainerFormatType.CFT_WAV, // 音频封装格式
    };
    let avConfig: media.AVRecorderConfig = {
      audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
      profile: avProfile,
      url: 'fd://35',
    };

    try {
      let path: string = context.filesDir + `/${wavFileName}`;
      this.wavFile = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to open file, error code: ${err.code}, message: ${err.message}`);
    }
    if (this.wavFile !== undefined) {
      avConfig.url = 'fd://' + this.wavFile.fd;
    }

    try {
      if (this.avRecorder.state === 'idle' || this.avRecorder.state === 'stopped') {
        await this.avRecorder.prepare(avConfig);
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to prepare avRecorder, error code: ${err.code}, message: ${err.message}`);
    }

    try {
      if (this.avRecorder.state === 'prepared') { // 仅在prepared状态下调用start为合理状态切换。
        await this.avRecorder.start();
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to start avRecorder, error code: ${err.code}, message: ${err.message}`);
    }
  }

  async stopAudioRecording() {
    try {
      if (this.avRecorder?.state === 'started' || this.avRecorder?.state === 'paused') {
        await this.avRecorder.stop();
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to stop avRecorder, error code: ${err.code}, message: ${err.message}`);
    }

    try {
      await this.avRecorder?.release();
      this.avRecorder = undefined;
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to release avRecorder, error code: ${err.code}, message: ${err.message}`);
    }

    try {
      if (this.wavFile !== undefined) {
        await fileIo.close(this.wavFile.fd);
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to close fd, error code: ${err.code}, message: ${err.message}`);
    }
  }

  async convert2PCM(wavFilePath: string, pcmFilePath: string) {
    try {
      if (fileIo.accessSync(pcmFilePath)) {
        fileIo.unlinkSync(pcmFilePath);
      }
    } catch (err) {
      console.error(`Failed to unlink ${pcmFilePath}, ${JSON.stringify(err)}`);
      return;
    }

    let callback: ICallBack = {
      callBackResult: (code: number) => {
        if (code === 0) {
          console.info(`Convert succeed`);
        } else {
          console.info(`Convert failed`);
        }
      },
    };
    let cmd = `ffmpeg -i ${wavFilePath} -acodec pcm_s16le -ar 16000 -ac 1 -f s16le ${pcmFilePath}`;
    MP4Parser.ffmpegCmd(cmd, callback);
  }

  async startRecognizer(pcmFilePath: string) {
    if (this.asrEngine) {
      console.error(`Recognizer is running`);
      return;
    }
    this.sessionId = util.generateRandomUUID();

    let createParams: speechRecognizer.CreateEngineParams = {
      online: 1,
      language: 'zh-CN',
    };
    try {
      this.asrEngine = await speechRecognizer.createEngine(createParams);
    } catch (err) {
      console.error(`Failed to invoke createEngine, ${JSON.stringify(err)}`);
      return;
    }

    // 创建回调对象
    let setListener: speechRecognizer.RecognitionListener = {
      // 开始识别成功回调
      onStart: (sessionId: string, eventMessage: string) => {
        console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
        let audioBuf = new Uint8Array(bufSize);
        try {
          this.pcmFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY);
        } catch (err) {
          console.error(`Failed to open pcm file ${pcmFilePath}, ${JSON.stringify(err)}`);
          this.asrEngine?.finish(this.sessionId);
        }
        let intervalId = setInterval(() => {
          try {
            if (this.asrEngine?.isBusy()) {
              return;
            }
            let readLen = fileIo.readSync(this.pcmFile?.fd, audioBuf.buffer.slice(0));
            if (readLen === 0) {
              clearInterval(intervalId);
              this.asrEngine?.finish(this.sessionId);
            }
            this.asrEngine?.writeAudio(this.sessionId, audioBuf);
          } catch (err) {
            this.asrEngine?.finish(this.sessionId);
            console.error(`Failed to write audio data, ${JSON.stringify(err)}`);
          }
        }, intervalMS);
      },
      // 事件回调
      onEvent: (sessionId: string, eventCode: number, eventMessage: string) => {
        console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
      },
      // 识别结果回调，包括中间结果和最终结果
      onResult: (sessionId: string, result: speechRecognizer.SpeechRecognitionResult) => {
        console.info(`onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}`);
      },
      // 识别完成回调
      onComplete: (sessionId: string, eventMessage: string) => {
        console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
        this.asrEngine?.shutdown();
        this.asrEngine = undefined;
        if (this.pcmFile) {
          try {
            fileIo.closeSync(this.pcmFile.fd);
          } catch (err) {
            console.error(`Failed to close file ${this.pcmFile}, ${JSON.stringify(err)}`);
          }
        }
      },
      // 错误回调
      onError: (sessionId: string, errorCode: number, errorMessage: string) => {
        console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
        this.asrEngine?.shutdown();
        this.asrEngine = undefined;
        if (this.pcmFile) {
          try {
            fileIo.closeSync(this.pcmFile.fd);
          } catch (err) {
            console.error(`Failed to close file ${this.pcmFile}, ${JSON.stringify(err)}`);
          }
        }
      },
    };
    // 设置回调
    this.asrEngine.setListener(setListener);

    let audioParam: speechRecognizer.AudioInfo = {
      audioType: 'pcm',
      sampleRate: 16000,
      soundChannel: 1,
      sampleBit: 16,
    };
    let extraParam: Record<string, Object> = {
      'recognitionMode': 1,
      'maxAudioDuration': 60000,
    };

    let recognizerParams: speechRecognizer.StartParams = {
      sessionId: this.sessionId,
      audioInfo: audioParam,
      extraParams: extraParam,
    };
    try {
      this.asrEngine?.startListening(recognizerParams);
    } catch (err) {
      console.error(`Failed to invoke startListening, ${JSON.stringify(err)}`);
      return;
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('Start Recorder')
        .width('100%')
        .onClick(() => {
          this.startAudioRecording(this.context);
        });

      Button('Stop Recorder')
        .width('100%')
        .onClick(() => {
          this.stopAudioRecording();
        });

      Button('Convert to PCM')
        .width('100%')
        .onClick(() => {
          let wavFilePath = this.context.filesDir + `/${wavFileName}`;
          let pcmFilePath = this.context.filesDir + `/${pcmFileName}`;
          console.info(`WAV File Path: ${wavFilePath}, PCM File Path: ${pcmFilePath}`);
          this.convert2PCM(wavFilePath, pcmFilePath);
        });

      Button('Start Recognizer')
        .width('100%')
        .onClick(() => {
          let pcmFilePath = this.context.filesDir + `/${pcmFileName}`;
          this.startRecognizer(pcmFilePath);
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

**Q：怎么判断设备正在录音，麦克风正在被占用？涉及隐私或敏感的业务场景需要此状态提示用户。**

**A**：判断设备是否正在录音的方法如下：

1. 通过AudioStreamManager音频流管理的[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)接口获取当前音频采集器的信息。
2. 遍历获取到的音频采集器的信息，调用[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)接口获取每个采集器音频流的最大电平值，当电平值大于0，说明设备采集到声音，设备正在录音。

示例代码如下：

```ts
import { audio } from '@kit.AudioKit';

const audioManager = audio.getAudioManager();
const audioVolumeManager: audio.AudioVolumeManager = audioManager.getVolumeManager();
const audioStreamManager = audioManager.getStreamManager();

@Entry
@Component
export struct AudioRecordingCheckDemo {
  @State isRecording: boolean = false;
  intervalID = -1;

  aboutToDisappear(): void {
    if (this.intervalID > -1) {
      clearInterval(this.intervalID);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('检查设备是否正在录音')
        .onClick(async () => {
          this.intervalID = setInterval(async () => {
            this.isRecording = await this.checkMicIsRecording();
          }, 500);
        });
      Text(`设备是否正在录音：${this.isRecording}`);
    }
    .justifyContent(FlexAlign.Center)
    .padding(30)
    .height('100%')
    .width('100%');
  }

  //获取麦克风是否在录音
  async checkMicIsRecording(): Promise<boolean> {
    try {
      const audioVolumeGroupManager: audio.AudioVolumeGroupManager =
        await audioVolumeManager.getVolumeGroupManager(audio.DEFAULT_VOLUME_GROUP_ID);
      let array = await audioStreamManager.getCurrentAudioCapturerInfoArray();
      console.info(`checkCapturerChanges size: ${array.length}`); //存在录音流不一定正在录音
      for (let changeInfo of array) {
        for (let deviceDescriptor of changeInfo.deviceDescriptors) {
          let maxAmplitude = await audioVolumeGroupManager.getMaxAmplitudeForInputDevice(deviceDescriptor);
          if (maxAmplitude > 0) { //录音设备电平值大于0，说明录音设备采集到声音
            console.warn(`checkCapturerChanges true maxAmplitude:${maxAmplitude} deviceType:${deviceDescriptor.deviceType}}`);
            return true;
          }
        }
      }
    } catch (err) {
      console.error(`checkCapturerChanges error:${JSON.stringify(err)}`);
      throw new Error(`checkCapturerChanges error:${JSON.stringify(err)}`);
    }
    return false;
  }
}
```

**Q：怎么采集录音数据流，如何避免不断的写入文件，浪费性能？**

**A**：处理方式如下：

1. 定义[Queue](../harmonyos-references/js-apis-queue.md)队列用于缓存音频数据。
2. 通过[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)录音时，在回调函数[on('readData')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#onreaddata11)中不断的将音频数据存入队列。
3. 在需要使用音频数据的时候，从队列中读取数据。

示例代码如下：

```screen
import { audio } from '@kit.AudioKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { Queue } from '@kit.ArkTS';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

@Entry
@Component
export struct AudioCapturerDataDemo {
  atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  capturerDemo = new CapturerDemo(this.context, audioStreamInfo, audioCapturerInfo);

  async aboutToAppear(): Promise<void> {
    await this.atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']); //权限申请
  }

  async aboutToDisappear(): Promise<void> {
    await this.capturerDemo.stop();
    await this.capturerDemo.release();
  }

  build() {
    Column({ space: 20 }) {
      Button('录制start').width('100%')
        .onClick(async () => {
          await this.capturerDemo.init();
          await this.capturerDemo.start();
        });

      Button('录制stop').width('100%')
        .onClick(async () => {
          await this.capturerDemo.stop();
          await this.capturerDemo.release();
        });
    }
    .justifyContent(FlexAlign.Center)
    .padding(30)
    .height('100%')
    .width('100%');
  }
}

class CapturerDemo {
  audioStreamInfo: audio.AudioStreamInfo;
  audioCapturerInfo: audio.AudioCapturerInfo;
  context: common.UIAbilityContext;
  bufferQueue = new Queue<ArrayBuffer>();
  audioCapturer?: audio.AudioCapturer;

  constructor(context: common.UIAbilityContext, audioStreamInfo: audio.AudioStreamInfo,
    audioCapturerInfo: audio.AudioCapturerInfo) {
    this.context = context;
    this.audioStreamInfo = audioStreamInfo;
    this.audioCapturerInfo = audioCapturerInfo;
  }

  // 初始化
  async init() {
    let audioCapturerOptions: audio.AudioCapturerOptions = {
      streamInfo: this.audioStreamInfo,
      capturerInfo: this.audioCapturerInfo
    };
    try {
      this.audioCapturer = await audio.createAudioCapturer(audioCapturerOptions); // 创建AudioCapturer实例。
      console.info(`createAudioCapturer success`);
      this.audioCapturer.on('readData', (buffer: ArrayBuffer) => {
        this.bufferQueue.add(buffer.slice(0)); //录音数据入队列
      });
    } catch (err) {
      console.error(`createAudioCapturer failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  // 开始一次音频采集。
  async start() {
    try {
      this.bufferQueue = new Queue<ArrayBuffer>();
      await this.audioCapturer?.start();
      console.info(`start success`);
    } catch (err) {
      console.error(`Capturer start failed. ${JSON.stringify(err)}`);
    }
  }

  // 停止采集。
  async stop() {
    try {
      await this.audioCapturer?.stop();
      this.handleAudioData(); //根据业务，处理音频数据
      console.info(`stop success`);
    } catch (err) {
      console.error(`Capturer stop failed. ${JSON.stringify(err)}`);
    }
  }

  // 销毁实例，释放资源。
  async release() {
    try {
      await this.audioCapturer?.release();
      console.info(`release success`);
    } catch (err) {
      console.error(`Capturer release failed. ${JSON.stringify(err)}`);
    }
  }

  handleAudioData() {
    // 以下示例将bufferQueue数据保存到文件，根据业务需要调整
    let filePath = this.context.cacheDir + '/StarWars10s-2C-48000-4SW.pcm';
    let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    let offset = 0;
    for (let buff of this.bufferQueue) {
      fs.writeSync(file.fd, buff, {
        offset: offset,
        length: buff.byteLength
      });
      offset += buff.byteLength;
    }
    fs.close(file);
  }
}
```
