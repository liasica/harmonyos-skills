---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-43
title: AVRecorder录制WAV封装格式的音频文件并识别为文字
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVRecorder录制WAV封装格式的音频文件并识别为文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8b8f5dbc3aaf35c646aab4ab6e95628c09a1ad09eae92287064ff23348250eb0
---

## 问题现象

使用AVRecorder录制WAV封装格式的音频文件，编码格式只能使用Audio\_G711MU，采样率只能选择8000HZ。语音识别要求输入数据为16000HZ采样率、PCM编码格式的音频数据。使用AVRecorder录制WAV音频后，如何将音频文件识别为文字。

## 背景知识

* 当需要使用麦克风时，需要申请[ohos.permission.MICROPHONE](../harmonyos-guides/permissions-for-all-user.md#ohospermissionmicrophone)麦克风权限。申请方式请参考：[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。
* [AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)用于音视频媒体录制。配置音视频录制参数时，需要使用[支持的格式](../harmonyos-guides/media-kit-intro.md#支持的格式)，具体的录制参数需严格契合既定的录制参数配置，具体可参考：[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)。当录制音频的封装格式为WAV格式时，音频编码格式只能选择AUDIO\_G711MU，采样率必须是8000HZ，单声道，比特率为64000bps。
* [speechRecognizer](../harmonyos-references/hms-ai-speechrecognizer.md)用于将一段中文音频信息转换为文本，音频信息可以为PCM音频文件或实时语音。语音识别当前只支持采样率为16000HZ，采样位数为16位的单声道PCM音频数据。
* [@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)是一个读取、写入操作音视频文件编辑的工具，可以调用ffmpeg命令完成音视频格式转换。

## 解决方案

[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)录制WAV封装格式的音频文件时，目前只支持采样率为8000HZ的G711MU编码格式，不支持录制采样率16000HZ的PCM编码格式的WAV音频文件。可以通过三方库[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令，将AVRecorder录制G711MU编码的音频文件转换为语音识别支持的PCM音频文件，然后通过语音识别将录制的音频文件识别为文字。

1. 使用[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)录制WAV封装格式的音频文件，编码格式为G711MU、采样率8000HZ、单声道、比特率64000bps。

   ```ts
   let avProfile: media.AVRecorderProfile = {
     audioChannels: 1, // 音频声道数目，单声道
     audioBitrate: 64000, // 音频比特率
     audioSampleRate: 8000, // 音频采样率
     audioCodec: media.CodecMimeType.AUDIO_G711MU, // 音频编码格式
     fileFormat: media.ContainerFormatType.CFT_WAV, // 音频封装格式
   };
   ```
2. 使用[@ohos/mp4parser(V2.0.7)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmp4parser)调用ffmpeg命令，生成采样率16000HZ、采样位数16位、单通道的PCM音频文件用于语音识别。

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
3. 启动语音识别，读取PCM音频文件，通过[writeAudio](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)接口持续写入待识别音频数据，并监听识别结果。

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
