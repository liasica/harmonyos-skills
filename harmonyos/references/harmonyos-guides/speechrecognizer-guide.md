---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speechrecognizer-guide
title: 语音识别
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > 语音识别
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:ff8365566781d886870a618d72f1135eb260d3d4b90ca41747351b8dba2eb0da
---

将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为PCM音频文件或者实时语音。

## 场景介绍

手机/平板等设备在无网状态下，为听障人士或不方便收听音频场景提供音频转文本能力。

## 约束与限制

| AI能力 | 约束 |
| --- | --- |
| 语音识别 | - 支持的语种类型：中文普通话。  - 支持的模型类型：离线。  - 语音时长：短语音模式不超过60s，长语音模式不超过8h。 |

## 开发步骤

1. 在使用语音识别时，将实现语音识别相关的类添加至工程。

   ```typescript
   import { speechRecognizer } from '@kit.CoreSpeechKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[createEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognizercreateengine)方法，对引擎进行初始化，并创建[SpeechRecognitionEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognitionengine)实例。

   createEngine方法提供了两种调用形式，当前以其中一种作为示例，其他方式可参见[speechRecognizer.createEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognizercreateengine)。

   ```typescript
   let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
   // 设置独立的sessionId
   let sessionId: string = '123456';
   // 创建引擎，通过callback形式返回
   // 设置创建引擎参数
   let extraParam: Record<string, Object> = {'locate': 'CN', 'recognizerMode': 'short'};
   let initParamsInfo: speechRecognizer.CreateEngineParams = {
     language: 'zh-CN',
     online: 1,
     extraParams: extraParam
   };
   // 调用createEngine方法
   speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
     if (!err) {
       console.info('Succeeded in creating engine.');
       // 接收创建引擎的实例
       asrEngine = speechRecognitionEngine;
     } else {
       console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
     }
   });
   ```
3. 得到[SpeechRecognitionEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognitionengine)实例对象后，实例化[RecognitionListener](../harmonyos-references/hms-ai-speechrecognizer.md#recognitionlistener)对象，然后调用[setListener](../harmonyos-references/hms-ai-speechrecognizer.md#setlistener)方法设置回调，用来接收语音识别相关的回调信息。

   ```typescript
   // 创建回调对象
   let setListener: speechRecognizer.RecognitionListener = {
     // 开始识别成功回调
     onStart(sessionId: string, eventMessage: string) {
       console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
     },
     // 事件回调
     onEvent(sessionId: string, eventCode: number, eventMessage: string) {
       console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
     },
     // 识别结果回调，包括中间结果和最终结果
     onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
       console.info(`onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}`);
     },
     // 识别完成回调
     onComplete(sessionId: string, eventMessage: string) {
       console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
     },
     // 错误回调，错误码通过本方法返回
     onError(sessionId: string, errorCode: number, errorMessage: string) {
       console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
     }
   };
   // 设置回调
   asrEngine?.setListener(setListener);
   ```
4. 分别为音频文件转文字和麦克风转文字功能设置开始识别的相关参数，调用[startListening](../harmonyos-references/hms-ai-speechrecognizer.md#startlistening)方法，开始识别。

   ```typescript
   private startListeningForRecording() {
     let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 };// audioInfo参数配置请参考AudioInfo
     let extraParam: Record<string, Object> = {
       'recognitionMode': 0,
       'vadBegin': 2000,
       'vadEnd': 3000,
       'maxAudioDuration': 20000
     };
     let recognizerParams: speechRecognizer.StartParams = {
       sessionId: this.sessionId,
       audioInfo: audioParam,
       extraParams: extraParam
     };
     console.info('startListening start');
     asrEngine?.startListening(recognizerParams);
   }
   ```
5. 传入音频流，调用[writeAudio](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)方法，开始写入音频流。读取音频文件时，开发者需预先准备一个pcm格式音频文件。

   ```typescript
   let uint8Array: Uint8Array = new Uint8Array();
   // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流
   // 写入音频流，音频流长度仅支持640或1280
   asrEngine?.writeAudio(sessionId, uint8Array);
   ```

   **说明** 

   1. 如需通过录音获取音频流，请打开麦克风权限，参考步骤10配置相关权限。
   2. 如需从音频文件中读取音频流，请在项目中的main\resources\resfile路径下存放pcm文件。
6. （可选）当需要查询语音识别服务支持的语种信息，可调用[listLanguages](../harmonyos-references/hms-ai-speechrecognizer.md#listlanguages)方法。

   listLanguages方法提供了两种调用形式，当前以其中一种作为示例，其他方式可参见[listLanguages](../harmonyos-references/hms-ai-speechrecognizer.md#listlanguages)。

   ```typescript
   // 设置查询相关的参数
   let languageQuery: speechRecognizer.LanguageQuery = {
     sessionId: sessionId
   };
   // 调用listLanguages方法
   asrEngine?.listLanguages(languageQuery).then((res: Array<string>) => {
     console.info(`Succeeded in listing languages.`);
   }).catch((err: BusinessError) => {
     console.error(`Failed to list languages. Code: ${err.code}, message: ${err.message}.`);
   });
   ```
7. （可选）当需要结束识别时，可调用[finish](../harmonyos-references/hms-ai-speechrecognizer.md#finish)方法。

   ```typescript
   // 结束识别
   asrEngine?.finish(sessionId);
   ```
8. （可选）当需要取消识别时，可调用[cancel](../harmonyos-references/hms-ai-speechrecognizer.md#cancel)方法。

   ```typescript
   // 取消识别
   asrEngine?.cancel(sessionId);
   ```
9. （可选）当需要释放语音识别引擎资源时，可调用[shutdown](../harmonyos-references/hms-ai-speechrecognizer.md#shutdown)方法。

   ```typescript
   // 释放识别引擎资源
   asrEngine?.shutdown();
   ```
10. 需要在[module.json5配置文件](module-configuration-file.md)中添加ohos.permission.MICROPHONE权限，确保麦克风使用正常。详细步骤可查看[声明权限](declare-permissions.md)章节。

```typescript
// ...
'requestPermissions': [
  {
    'name' : 'ohos.permission.MICROPHONE',
    'reason': '$string:reason',
    'usedScene': {
      'abilities': [
        'EntryAbility'
      ],
      'when':'inuse'
    }
  }
],
// ...
```

## 开发实例

点击按钮，将一段音频信息转换为文本。

### Index.ets

```typescript
import { speechRecognizer } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { PromptAction } from '@kit.ArkUI';
import FileCapturer from './FileCapturer';

const TAG = 'AsrDemo';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

@Entry
@Component
struct Index {
  @State createCount: number = 0;
  @State result: boolean = false;
  @State voiceInfo: string = '';
  // 设置独立的sessionId
  @State sessionId: string = '123456';
  @State sessionId2: string = '1234567';
  @State generatedText: string = 'Default Text';
  @State uiContext: UIContext = this.getUIContext();
  @State promptAction: PromptAction = this.uiContext.getPromptAction();

  private mFileCapturer: FileCapturer = new FileCapturer();

  build() {
    Column() {
      Scroll() {
        Column() {
          Row() {
            Column() {
              Text(this.generatedText)
                .fontColor($r('sys.color.ohos_id_color_text_secondary'))
            }
            .width('100%')
            .constraintSize({ minHeight: 100 })
            .border({ width: 1, radius: 5 })
            .backgroundColor('#d3d3d3')
            .padding(20)
            .alignItems(HorizontalAlign.Start)
          }
          .width('100%')
          .padding({ left: 20, right: 20, top: 20, bottom: 20 })

          Button() {
            Text('CreateEngineByCallback')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            this.createByCallback();
            this.createCount++;
            console.info(TAG, `CreateAsrEngine: createCount:${this.createCount}`);

            this.sleep(500).then(() => {
              this.setListener();
              try {
                this.promptAction.showToast({
                  message: 'CreateEngine succeeded!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            }).catch((err: BusinessError) => {
              console.error(TAG, `Error in create engine: ${err}`);
              try {
                this.promptAction.showToast({
                  message: 'CreateEngine failed!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            });
          })

          Button() {
            Text('startRecording')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            this.startRecording();
            try {
              this.promptAction.showToast({
                message: 'start Recording',
                duration: 2000
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`showToast args error code is ${code}, message is ${message}`);
            }
          })

          Button() {
            Text('audioToText')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            void this.audioToText();
            try {
              this.promptAction.showToast({
                message: 'start audioToText',
                duration: 2000
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`showToast args error code is ${code}, message is ${message}`);
            }
          })

          Button() {
            Text('queryLanguagesCallback')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            try {
              this.queryLanguagesCallback();
              try {
                this.promptAction.showToast({
                  message: 'queryLanguages succeeded!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            } catch (err) {
              this.generatedText = `Failed to query language information. message: ${err.message}.`;
              try {
                this.promptAction.showToast({
                  message: 'queryLanguages failed!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            }
          })

          Button() {
            Text('shutdown')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AA7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            // 释放引擎
            try {
              asrEngine?.shutdown();
              this.generatedText = `The engine has been released.`;
              try {
                this.promptAction.showToast({
                  message: 'shutdown succeeded!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            } catch (err) {
              this.generatedText = `Failed to release engine. message: ${err.message}.`;
              try {
                this.promptAction.showToast({
                  message: 'shutdown failed!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            }
          })
        }
        .layoutWeight(1)
      }
      .width('100%')
      .height('100%')

    }
  }

  // 创建引擎，通过callback形式返回
  private createByCallback() {
    // 设置创建引擎参数
    let extraParam: Record<string, Object> = {'locate': 'CN', 'recognizerMode': 'short'};
    let initParamsInfo: speechRecognizer.CreateEngineParams = {
      language: 'zh-CN',
      online: 1,
      extraParams: extraParam
    };

    // 调用createEngine方法
    speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine:
      speechRecognizer.SpeechRecognitionEngine) => {
      if (!err) {
        console.info(TAG, 'succeeded in creating engine.');
        // 接收创建引擎的实例
        asrEngine = speechRecognitionEngine;
      } else {
        // 无法创建引擎时返回错误码1002200001，原因：语种不支持、模式不支持、初始化超时、资源不存在等导致创建引擎失败
        // 无法创建引擎时返回错误码1002200006，原因：引擎正在忙碌中，一般多个应用同时调用语音识别引擎时触发
        // 无法创建引擎时返回错误码1002200008，原因：引擎已被销毁
        console.error(TAG, `Failed to create engine. Message: ${err.message}.`);
      }
    });
  }

  // 查询语种信息，以callback形式返回
  private queryLanguagesCallback() {
    // 设置查询相关参数
    let languageQuery: speechRecognizer.LanguageQuery = {
      sessionId: this.sessionId
    };
    // 调用listLanguages方法
    asrEngine?.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
      if (!err) {
        // 接收目前支持的语种信息
        console.info(TAG, `succeeded in listing languages, result: ${JSON.stringify(languages)}`);
        this.generatedText = `languages result: ${JSON.stringify(languages)}`;
      } else {
        console.error(TAG, `Failed to create engine. Message: ${err.message}.`);
        this.generatedText = `Failed to create engine. Message: ${err.message}.`;
      }
    });
  }

  private startListeningForRecording() {
    let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }; // audioInfo参数配置请参考AudioInfo
    let extraParam: Record<string, Object> = {
      'recognitionMode': 0,
      'vadBegin': 2000,
      'vadEnd': 3000,
      'maxAudioDuration': 20000
    };
    let recognizerParams: speechRecognizer.StartParams = {
      sessionId: this.sessionId,
      audioInfo: audioParam,
      extraParams: extraParam
    };
    console.info(TAG, 'startListening start');
    try {
      asrEngine?.startListening(recognizerParams);
    } catch (err) {
      console.error(`error code: ${err.code}, message: ${err.message}.`);
    }
  }

  // 写音频流
  private async audioToText() {
    try {
      this.setListener();
      // Set the parameters related to the start of identification.
      let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 };
      let recognizerParams: speechRecognizer.StartParams = {
        sessionId: this.sessionId2,
        audioInfo: audioParam
      };
      // Invoke the start recognition method.
      asrEngine?.startListening(recognizerParams);

      // Get Audio from File
      let data: ArrayBuffer | undefined = undefined;
      let ctx = this.getUIContext().getHostContext() as Context;
      let filenames: string[] = fileIo.listFileSync(ctx.resourceDir);
      if (filenames.length <= 0) {
        console.error('length is null');
        return;
      }
      let filePath: string = ctx.resourceDir + '/' + filenames[0];
      (this.mFileCapturer as FileCapturer).setFilePath(filePath);
      this.mFileCapturer.init((dataBuffer: ArrayBuffer) => {
        data = dataBuffer;
        let uint8Array: Uint8Array = new Uint8Array(data);
        asrEngine?.writeAudio(this.sessionId2, uint8Array);
      });
      await this.mFileCapturer.start();
      asrEngine?.finish(this.sessionId);
      this.mFileCapturer.release();
    } catch (err) {
      this.generatedText = `Message: ${err.message}.`;
    }
  }

  // 麦克风语音转文本
  private startRecording() {
    try {
      this.startListeningForRecording();
    } catch (err) {
      this.generatedText = `Message: ${err.message}.`;
    }
  }

  // 睡眠
  private async sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // 设置回调
  private setListener() {
    // 创建回调对象
    let setListener: speechRecognizer.RecognitionListener = {
      // 开始识别成功回调
      onStart: (sessionId: string, eventMessage: string) => {
        this.generatedText = '';
        console.info(TAG, `onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
      },
      // 事件回调
      onEvent(sessionId: string, eventCode: number, eventMessage: string) {
        console.info(TAG, `onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
      },
      // 识别结果回调，包括中间结果和最终结果
      onResult: (sessionId: string, result: speechRecognizer.SpeechRecognitionResult) => {
        console.info(TAG, `onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}`);
        this.generatedText = result.result;
      },
      // 识别完成回调
      onComplete(sessionId: string, eventMessage: string) {
        console.info(TAG, `onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
      },
      // 错误回调，错误码通过本方法返回
      onError(sessionId: string, errorCode: number, errorMessage: string) {
        console.error(TAG, `onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
      }
    };
    // 设置回调
    asrEngine?.setListener(setListener);
  }
}
```

### FileCapturer.ets

添加FileCapturer.ets文件用于pcm文件音频流。

```typescript
import { fileIo } from '@kit.CoreFileKit';

const TAG = 'FileCapturer';
const SEND_SIZE: number = 1280;

/**
 * File collector tool
 */
export default class FileCapturer {
  /**
   * Whether the audio is being written
   */
  private mIsWriting: boolean = false;

  /**
   * File Path
   */
  private mFilePath: string = '';

  /**
   * Open File Object
   */
  private mFile: fileIo.File | null = null;

  /**
   * Indicates whether the file can be read.
   */
  private mIsReadFile: boolean = true;

  /**
   * Audio Data Callback Method
   */
  private mDataCallBack: ((data: ArrayBuffer) => void ) | null = null;

  /**
   * Setting the File Path
   * @param filePath
   */
  public setFilePath(filePath: string) {
    this.mFilePath = filePath;
  }

  init(dataCallBack: (data: ArrayBuffer) => void) {
    if (null != this.mDataCallBack) {
      return;
    }
    this.mDataCallBack = dataCallBack;
    try {
      if (!fileIo.accessSync(this.mFilePath)) {
        return
      }
    } catch (err) {
      console.error(`error code: ${err.code}, message: ${err.message}.`);
    }
    console.info(TAG, 'init start ');
  }

  async start(): Promise<void> {
    try {
      if (this.mIsWriting || null == this.mDataCallBack) {
        return;
      }
      this.mIsWriting = true;
      this.mIsReadFile = true;
      this.mFile = fileIo.openSync(this.mFilePath, fileIo.OpenMode.READ_ONLY);
      let buf: ArrayBuffer = new ArrayBuffer(SEND_SIZE);
      let offset: number = 0;
      while (SEND_SIZE == fileIo.readSync(this.mFile.fd, buf, {
        offset: offset
      }) && this.mIsReadFile) {
        this.mDataCallBack(buf);
        await sleep(40);
        offset = offset + SEND_SIZE;
      }
    } catch (e) {
      console.error(TAG, 'read file error ' + e);
    } finally {
      if (null != this.mFile) {
        try {
          fileIo.closeSync(this.mFile);
        } catch (err) {
          console.error(`error code: ${err.code}, message: ${err.message}.`)
        }
      }
      this.mIsWriting = false;
    }
  }

  stop() {
    if (null == this.mDataCallBack) {
      return;
    }
    try {
      this.mIsReadFile = false;
    } catch (e) {
      console.error(TAG, 'read file error ' + e);
    }
  }

  release() {
    if (null == this.mDataCallBack) {
      return;
    }
    try {
      this.mDataCallBack = null;
      this.mIsReadFile = false;
    } catch (e) {
      console.error(TAG, 'read file error ' + e);
    }
  }
}

async function sleep(ms: number): Promise<void> {
  return new Promise<void>(resolve => setTimeout(resolve, ms));
}
```

### EntryAbility.ets

在EntryAbility.ets文件中添加麦克风权限。

```typescript
import { abilityAccessCtrl, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']).then((data) => {
      hilog.info(0x0000, 'testTag', 'data:' + JSON.stringify(data));
      hilog.info(0x0000, 'testTag', 'data permissions:' + data.permissions);
      hilog.info(0x0000, 'testTag', 'data authResults:' + data.authResults);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
    });

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```
