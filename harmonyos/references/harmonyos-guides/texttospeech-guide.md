---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/texttospeech-guide
title: 文本转语音
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > 文本转语音
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:0c0a8dbf25bbb0c0103fe841bad31ebe3c8e751003d6cd81138c916c63a1e594
---

Core Speech Kit支持将一篇不超过10000字符数的中英文文本（简体中文、繁体中文、数字、英文）合成为语音，并以选定音色进行播报。

开发者可对播报的策略进行设置，包括单词播报、数字播报、静音停顿、汉字发音策略。

## 场景介绍

手机/平板等设备在无网状态下，系统应用无障碍（屏幕朗读）接入文本转语音能力，为视障人士或不方便阅读场景提供播报能力。

## 约束与限制

| AI能力 | 约束 |
| --- | --- |
| 文本转语音 | - 支持的语种类型：中文、英文。（简体中文、繁体中文、中文语境下的英文）  - 支持的音色类型：聆小珊女声音色、英语（美国）劳拉女声音色、凌飞哲男声音色。  - 文本长度：不超过10000字符数。 |

## 开发步骤

1. 在使用文本转语音时，将实现文本转语音相关的类添加至工程。

   ```typescript
   import { textToSpeech } from '@kit.CoreSpeechKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用createEngine接口，创建[TextToSpeechEngine](../harmonyos-references/hms-ai-texttospeech.md#texttospeechengine)实例。

   createEngine接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-texttospeech.md)。

   ```typescript
   let ttsEngine: textToSpeech.TextToSpeechEngine;

   // 设置创建引擎参数
   let extraParam: Record<string, Object> = {'style': 'interaction-broadcast', 'locate': 'CN', 'name': 'EngineName'};
   let initParamsInfo: textToSpeech.CreateEngineParams = {
     language: 'zh-CN',
     person: 0,
     online: 1,
     extraParams: extraParam
   };

   // 调用createEngine方法
   textToSpeech.createEngine(initParamsInfo, (err: BusinessError,
                                              textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
     if (!err) {
       console.info('Succeeded in creating engine');
       // 接收创建引擎的实例
       ttsEngine = textToSpeechEngine;
     } else {
       console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
     }
   });
   ```
3. 得到[TextToSpeechEngine](../harmonyos-references/hms-ai-texttospeech.md#texttospeechengine)实例对象后，实例化[SpeakParams](../harmonyos-references/hms-ai-texttospeech.md#speakparams)对象、[SpeakListener](../harmonyos-references/hms-ai-texttospeech.md#speaklistener)对象，并传入待合成及播报的文本originalText，调用[speak](../harmonyos-references/hms-ai-texttospeech.md#speak)接口进行播报。

   ```typescript
   // 设置speak的回调信息
   let speakListener: textToSpeech.SpeakListener = {
     // 开始播报回调
     onStart(requestId: string, response: textToSpeech.StartResponse) {
       console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
     },
     // 合成完成及播报完成回调
     onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
       console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
     },
     // 停止播报回调
     onStop(requestId: string, response: textToSpeech.StopResponse) {
       console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
     },
     // 返回音频流
     onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
       console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
     },
     // 错误回调
     onError(requestId: string, errorCode: number, errorMessage: string) {
       console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
     }
   };
   // 设置回调
   ttsEngine.setListener(speakListener);
   // 设置播报内容
   let originalText: string = 'Hello HarmonyOS';
   // 设置播报相关参数
   let extraParam: Record<string, Object> = {
    'queueMode': 0,
    'speed': 1,
    'volume': 2,
    'pitch': 1,
    'languageContext': 'zh-CN',
    'audioType': 'pcm',
    'soundChannel': 3,
    'playType': 1
   };
   let speakParams: textToSpeech.SpeakParams = {
     requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
     extraParams: extraParam
   };
   // 调用播报方法
   // 开发者可以通过修改speakParams主动设置播报策略
   try {
     ttsEngine.speak(originalText, speakParams);
   } catch (err) {
     console.error(`error code: ${err.code}, message: ${err.message}.`);
   }
   ```
4. （可选）当需要停止合成及播报时，可调用[stop](../harmonyos-references/hms-ai-texttospeech.md#stop)接口。

   ```typescript
   ttsEngine.stop();
   ```
5. （可选）当需要查询文本转语音服务是否处于忙碌状态时，可调用[isBusy](../harmonyos-references/hms-ai-texttospeech.md#isbusy)接口。

   ```typescript
   ttsEngine.isBusy();
   ```
6. （可选）当需要查询支持的语种音色信息时，可调用[listVoices](../harmonyos-references/hms-ai-texttospeech.md#listvoices)接口。

   listVoices接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-texttospeech.md)。

   ```typescript
   // 在组件中声明并初始化字符串voiceInfo
   @State voiceInfo: string = '';

   // 设置查询相关参数
   let voicesQuery: textToSpeech.VoiceQuery = {
     requestId: '12345678', // requestId在同一实例内仅能用一次，请勿重复设置
     online: 1
   };
   // 调用listVoices方法，以callback返回
   ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
     if (!err) {
       // 接收目前支持的语种音色等信息
       this.voiceInfo = JSON.stringify(voiceInfo);
       console.info(`Succeeded in listing voices, voiceInfo is ${this.voiceInfo}`);
     } else {
       console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}`);
     }
   });
   ```

## 设置播报策略

由于不同场景下，模型自动判断所选择的播报策略可能与实际需求不同，此章节提供对于播报策略进行主动设置的方法。

**说明** 

以下取值说明均为有效取值，若所使用的数值在有效取值之外则播报结果可能与预期不符，并产生错误的播报结果。

### 设置单词播报方式

文本格式：[hN] (N=0/1/2)

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断单词播放方式。默认值为0。 |
| 1 | 逐个字母进行播报。 |
| 2 | 以单词方式进行播报。 |

文本示例：

```typescript
'hello[h1] world'
```

hello使用单词发音，world及后续单词将会逐个字母进行发音。

### 设置数字播报策略

格式：[nN] (N=0/1/2)

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断数字处理策略。默认值为0。 |
| 1 | 作为号码逐个数字播报。 |
| 2 | 作为数值播报。超过18位数字不支持，自动按逐个数字进行播报。 |

文本示例：

```typescript
'[n2]123[n1]456[n0]'
```

其中，123将会按照数值播报，456则会按照号码播报，而后的文本中的数字，均会自动判断。

### 插入静音停顿

格式：[pN]

描述：N为无符号整数，单位为ms。

文本示例：

```typescript
'你好[p500]小艺'
```

该句播报时，将会在“你好”后插入500ms的静音停顿。

### 指定汉字发音

汉字的声调，通过在拼音后接一位数字1~5分别表示阴平、阳平、上声、去声和轻声5个声调。

格式：[=MN]

描述：M表示拼音，N表示声调。

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 1 | 阴平 |
| 2 | 阳平 |
| 3 | 上声 |
| 4 | 去声 |
| 5 | 轻声 |

文本示例：

```typescript
'着[=zhuo2]手'
```

“着”字将读作“zhuó”。

## 开发实例

点击按钮，播报一段文本。

### Index.ets

```typescript
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction, UIContext } from '@kit.ArkUI';
import { TreeMap } from '@kit.ArkTS';
import { fileIo } from '@kit.CoreFileKit';
import PcmPlayer from './PcmPlayer';
import { audio } from '@kit.AudioKit';
import { Context } from '@kit.AbilityKit';

const TAG: string = 'TtsDemo';
let ttsEngine: textToSpeech.TextToSpeechEngine;
let bufferLength: number = 0;
let engineCreated: boolean = false;

// 定义一个函数来拼接ArrayBuffer
function concatenateArrayBuffers(buffers: ArrayBuffer[]): ArrayBuffer {
  const totalLength = buffers.reduce((sum, buffer) => sum + buffer.byteLength, 0);
  const concatenatedBuffer = new ArrayBuffer(totalLength);
  let offset = 0;
  for (const buffer of buffers) {
    const uint8Array = new Uint8Array(buffer);
    new Uint8Array(concatenatedBuffer, offset, uint8Array.length).set(uint8Array);
    offset += uint8Array.length;
  }
  return concatenatedBuffer;
}

@Entry
@Component
struct Index {
  @State createCount: number = 0;
  // 设置播报内容
  @State originalText: string = '\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t' + '纸上得来终觉浅，绝知此事要躬行。\n\t\t';
  @State uiContext: UIContext = this.getUIContext();
  @State promptAction: PromptAction = this.uiContext.getPromptAction();
  private pcmData: TreeMap<number, Uint8Array> = new TreeMap();
  private pcmPlayer: PcmPlayer = new PcmPlayer();

  build() {
    Column() {
      Scroll() {
        Column() {
          TextArea({ placeholder: 'Please enter tts original text', text: `${this.originalText}` })
            .margin(20)
            .focusable(false)
            .border({ width: 5, color: 0x317AE7, radius: 10, style: BorderStyle.Dotted })
            .onChange((value: string) => {
              this.originalText = value;
              console.info(TAG, 'original text: ' + this.originalText);
            })

          Button() {
            Text('CreateEngine')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            engineCreated = true;
            this.createCount++;
            console.info(`createByCallback: createCount:${this.createCount}`);
            this.createByCallback();
            try {
              this.promptAction.showToast({
                message: 'CreateEngine success!',
                duration: 2000
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`showToast args error code is ${code}, message is ${message}`);
            }
          })

          Button() {
            Text('speak')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            if (engineCreated) {
              try {
                this.speak();
                try {
                  this.promptAction.showToast({
                    message: 'start speaking',
                    duration: 2000
                  });
                } catch (error) {
                  let message = (error as BusinessError).message;
                  let code = (error as BusinessError).code;
                  console.error(`showToast args error code is ${code}, message is ${message}`);
                }
              } catch (err) {
                try {
                  this.promptAction.showToast({
                    message: 'start speaking failed',
                    duration: 2000
                  });
                } catch (error) {
                  let message = (error as BusinessError).message;
                  let code = (error as BusinessError).code;
                  console.error(`showToast args error code is ${code}, message is ${message}`);
                }
              }
            } else {
              try {
                this.promptAction.showToast({
                  message: 'The engine has not been created',
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
            Text('speakOnData')
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0x317AE7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            if (engineCreated) {
              try {
                void this.speakOnData();
                try {
                  this.promptAction.showToast({
                    message: 'start speakOnData',
                    duration: 2000
                  });
                } catch (error) {
                  let message = (error as BusinessError).message;
                  let code = (error as BusinessError).code;
                  console.error(`showToast args error code is ${code}, message is ${message}`);
                }
              } catch (err) {
                try {
                  this.promptAction.showToast({
                    message: 'start speakOnData failed',
                    duration: 2000
                  });
                } catch (error) {
                  let message = (error as BusinessError).message;
                  let code = (error as BusinessError).code;
                  console.error(`showToast args error code is ${code}, message is ${message}`);
                }
              }
            } else {
              try {
                this.promptAction.showToast({
                  message: 'The engine has not been created',
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
            Text('stop')
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
              let isBusy: boolean = ttsEngine.isBusy();
              let isPlaying: boolean = this.pcmPlayer.isPlaying();
              if (isBusy) {
                ttsEngine.stop();
              }
              if (isPlaying) {
                this.pcmPlayer.stop();
              }
              try {
                this.promptAction.showToast({
                  message: 'stop!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            } catch (err) {
              try {
                this.promptAction.showToast({
                  message: 'stop failed',
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
            Text('isBusy')
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
              let isBusy: boolean = ttsEngine.isBusy();
              let isPlaying: boolean = this.pcmPlayer.isPlaying();
              console.info('isBusy :' + isBusy);
              console.info('isPlaying :' + isPlaying);
              try {
                this.promptAction.showToast({
                  message: 'speak isBusy :' + isBusy + '\nspeakOnData isBusy :' + isPlaying,
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            } catch (err) {
              try {
                this.promptAction.showToast({
                  message: 'isBusy failed',
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
            try {
              this.pcmPlayer.release();
              ttsEngine.shutdown();
              engineCreated = false;
              try {
                this.promptAction.showToast({
                  message: 'shutdown success!',
                  duration: 2000
                });
              } catch (error) {
                let message = (error as BusinessError).message;
                let code = (error as BusinessError).code;
                console.error(`showToast args error code is ${code}, message is ${message}`);
              }
            } catch (err) {
              try {
                this.promptAction.showToast({
                  message: 'shutdown failed',
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
  // 当引擎不存在、引擎资源不存在、初始化超时，返回错误码1002300005，引擎创建失败
  private createByCallback() {
    // 设置创建引擎参数
    let extraParam: Record<string, Object> = { 'style': 'interaction-broadcast', 'locate': 'CN', 'name': 'EngineName' };
    let initParamsInfo: textToSpeech.CreateEngineParams = {
      language: 'zh-CN',
      person: 0,
      online: 1,
      extraParams: extraParam
    };
    try {
      // 调用createEngine方法
      textToSpeech.createEngine(initParamsInfo, (err: BusinessError,
                                                 textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
        if (!err) {
          console.info('createEngine is success');
          // 接收创建引擎的实例
          ttsEngine = textToSpeechEngine;
        } else {
          console.error(`error code: ${err.code}, message: ${err.message}.`);
        }
      });
    } catch (error) {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(`createEngine failed, error code: ${code}, message: ${message}.`);
    }
  }

  // 调用speak播报方法
  private speak() {
    let speakListener: textToSpeech.SpeakListener = {
      // 开始播报回调
      onStart(requestId: string, response: textToSpeech.StartResponse) {
        console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
      },
      // 完成播报回调
      onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
        console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
      },
      // 停止播报完成回调，调用stop方法并完成时会触发此回调
      onStop(requestId: string, response: textToSpeech.StopResponse) {
        console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
      },
      // 返回音频流
      onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
        console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
      },
      // 错误回调，播报过程发生错误时触发此回调
      onError(requestId: string, errorCode: number, errorMessage: string) {
        if (errorCode === 1002300007) {
          engineCreated = false;
        }
        console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
      }
    };
    // 设置回调
    ttsEngine.setListener(speakListener);
    // 设置播报相关参数
    let extraParam: Record<string, Object> = {
        'queueMode': 0,
        'speed': 1,
        'volume': 2,
        'pitch': 1,
        'languageContext': 'zh-CN',
        'audioType': 'pcm',
        'soundChannel': 3,
        'playType':1
      };
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '123456' + Date.now(), // requestId在同一实例内仅能用一次，请勿重复设置
      extraParams: extraParam
    };
    // 调用speak播报方法
    try {
      ttsEngine.speak(this.originalText, speakParams);
    } catch (err) {
      console.error(TAG, `error code: ${err.code}, message: ${err.message}.`);
    }
  }

  private onStart = (utteranceId: string, response: textToSpeech.StartResponse) => {
    bufferLength = 0;
    // 初始化音频数据映射
    console.info(TAG, `onStart | utteranceId: ${ utteranceId }, response: ${JSON.stringify(response)}`);
  }

  private onData = (utteranceId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) => {
    // 将ArrayBuffer转换为Uint8Array
    let uint8Array: Uint8Array = new Uint8Array(audio);
    this.pcmData.set(response.sequence, uint8Array);
    bufferLength += 1;
    let str = '';
    // 或者使用循环打印每个元素
    for (let i = 0; i < uint8Array.length; i++) {
      str = str + (',' + uint8Array[i]);
    }
    console.info(TAG, `onData | utteranceId: ${utteranceId}, sequence: ${JSON.stringify(response.sequence)}, length: ${uint8Array.length}, audio: ${JSON.stringify(str)}`);
  }

  private onComplete = (utteranceId: string, response: textToSpeech.CompleteResponse) => {
    let buffers: ArrayBuffer[] = new Array();

    console.info(TAG, `pcmData len: ${this.pcmData.length}`);
    // 遍历Map，将ArrayBuffer添加到数组中
    try {
      this.pcmData?.forEach((value: Uint8Array) => {
        buffers.push(value.buffer.slice(0));
      })
    } catch (forEachErr) {
      console.error(TAG, 'pcmData forEach failed:', forEachErr);
    }
    console.info(TAG, `buffers len: ${buffers.length}`);

    // 按照顺序拼接所有的ArrayBuffer
    let audioData = concatenateArrayBuffers(buffers);
    console.info(TAG, `audioData len: ${audioData.byteLength}`);

    let context = this.uiContext.getHostContext() as Context;
    let path = context.filesDir;
    let filePath: string = `${path}/my.pcm`;
    fileIo.createStream(filePath, 'w+')
      .then(os => os.write(audioData).catch((e: BusinessError) => {
        throw new Error(`Write failed: ${e}`)
      }))
      .then((): Promise<void> => {
        try {
          this.pcmPlayer.file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
          return this.pcmPlayer.prepare(audio.AudioSamplingRate.SAMPLE_RATE_16000);
        } catch (e) {
          throw new Error(`Open failed: ${e}`)
        }
      })
      .then(() => this.pcmPlayer.play(audioData))
      .catch((err: BusinessError) => console.error(TAG, `Error: ${err}`));

    console.info(TAG, `onComplete | utteranceId: ${utteranceId}, response: ${JSON.stringify(response)}`);
  }

  // 调用speakOnData播报方法
  // 未初始化引擎时调用speak方法，返回错误码1002300007，合成及播报失败
  private speakOnData() {
    // 设置播报相关参数
    let extraParam: Record<string, Object> = {
        'queueMode': 0,
        'speed': 1.2,
        'volume': 2,
        'pitch': 1,
        'languageContext': 'zh-CN',
        'audioType': 'pcm',
        'soundChannel': 1,
        'playType':0
      };
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '1234567' + Date.now(),
      extraParams: extraParam
    };

    try {
      // 创建回调对象
      let speakListener: textToSpeech.SpeakListener = {
        // 开始识别成功回调
        onStart: this.onStart,
        // 识别完成回调
        onComplete: this.onComplete,
        // 停止播报回调
        onStop(utteranceId: string, response: textToSpeech.StopResponse) {
          console.info('speakListener onStop: ' + ' utteranceId: ' + utteranceId + ' response: ' + JSON.stringify(response));
        },
        // 返回音频流
        onData: this.onData,
        // 错误回调
        onError(utteranceId: string, errorCode: number, errorMessage: string) {
          if (errorCode === 1002300007) {
            engineCreated = false;
          }
          console.error('speakListener onError: ' + ' utteranceId: ' + utteranceId + ' errorCode: ' + errorCode + ' errorMessage: ' + errorMessage);
        }
      };
      // 设置回调
      ttsEngine.setListener(speakListener);
      try {
        console.info(`speakListener before speak`);
        // 调用speak播报方法
        for (let i = 0; i < 1; i++) {
          ttsEngine?.speak(this.originalText, speakParams);
        }
        console.info(`speakListener after speak`)
      } catch (error) {
        let message = (error as BusinessError).message;
        let code = (error as BusinessError).code;
        console.error(`speakListener speak failed, error code: ${code}, message: ${message}.`);
      }
    } catch (error) {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(`speakListener setListener failed, error code: ${code}, message: ${message}.`);
    }
  }
}
```

### PcmPlayer.ets

```typescript
import { audio } from '@kit.AudioKit';
import { fileIo } from '@kit.CoreFileKit';

const TAG = 'PCM_audio';

class Options {
  offset?: number;
  length?: number;
}

export default class PcmPlayer {

  public file: fileIo.File | undefined;
  private writeDataCallback = (buffer: ArrayBuffer) => {
    let options: Options = {
      offset: this.bufferSize,
      length: buffer.byteLength
    };

    try {
      fileIo.readSync(this.file?.fd, buffer, options);
      this.bufferSize += buffer.byteLength;
      if (this.audioDataSize < this.bufferSize) {
        this.renderModel?.off('writeData');
        void this.stop()
      }
      console.info(TAG, 'reading file success');
      // 系统会判定buffer有效，正常播放。
      return audio.AudioDataCallbackResult.VALID;
    } catch (error) {
      console.error(TAG, `Reading file failed, error code: ${error.code}, message: ${error.message}.`);
      // 系统会判定buffer无效，不播放。
      return audio.AudioDataCallbackResult.INVALID;
    }
  };
  /**
   * 缓存大小
   */
  private bufferSize: number = 0;
  /**
   * 音频总大小
   */
  private audioDataSize: number = 0;
  /**
   * 播放器
   */
  private renderModel: audio.AudioRenderer | null = null;
  /**
   * 播放状态
   */
  private audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000, // 采样率
    channels: audio.AudioChannel.CHANNEL_1, // 通道
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
  };
  private audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_ACCESSIBILITY, // 音频流使用类型
    rendererFlags: 0 // 音频渲染器标志
  };
  private audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: this.audioStreamInfo,
    rendererInfo: this.audioRendererInfo
  };

  public async prepare(sampleRate: number) {
    this.audioRendererOptions.streamInfo.samplingRate = sampleRate;
    this.audioRendererOptions.rendererInfo.usage = audio.StreamUsage.STREAM_USAGE_MUSIC;
    if (this.renderModel != null) {
      await this.renderModel.release();
    }
    let renderModel = await audio.createAudioRenderer(this.audioRendererOptions);
    if (!renderModel) {
      console.error(TAG, `failed to create audio renderer`);
    }
    console.info(TAG, 'creating AudioRenderer success');
    this.renderModel = renderModel;
    this.bufferSize = await this.renderModel.getBufferSize();
  }

  public async play(data: ArrayBuffer): Promise<number> {
    this.audioDataSize = data.byteLength
    if (this.renderModel != null) {
      try {
        this.renderModel.on('writeData', this.writeDataCallback);
      } catch (err) {
        console.error(`error code: ${err.code}, message: ${err.message}.`);
      }
      // 启动渲染
      await this.renderModel.start();
      console.info(TAG, 'start AudioRenderer success');
    }
    return -1;
  }

  public async stop() {
    console.info(TAG, 'Renderer begin stop');
    if (this.renderModel == null) {
      return;
    }

    // 只有渲染器状态为running或paused的时候才可以停止
    if (this.renderModel.state !== audio.AudioState.STATE_RUNNING
      && this.renderModel.state !== audio.AudioState.STATE_PAUSED) {
      console.error(TAG, 'Renderer is not running or paused');
      return;
    }
    await this.renderModel.stop(); // 停止渲染
    console.info(TAG, 'Renderer stopped');
  }

  public async release() {
    // 渲染器状态不是released状态，才能release
    if (this.renderModel != null) {
      if (this.renderModel.state === audio.AudioState.STATE_RELEASED) {
        console.error(TAG, 'Renderer already released');
        return;
      }
      await this.renderModel.release(); // 释放资源
      this.renderModel = null;
      console.info(TAG, 'Renderer released');
    }
  }

  /**
   * 判断当前渲染状态
   *
   * @returns running返回true，否则返回false
   */
  public isPlaying() {
    if (this.renderModel != null) {
      console.info(TAG, 'player.state:' + this.renderModel.state);
      return this.renderModel.state == audio.AudioState.STATE_RUNNING;
    } else {
      return false;
    }
  }

  /**
   * 获取当前渲染状态
   *
   * @returns running返回true，否则返回false
   */
  public getRenderState(): number {
    if (this.renderModel != null) {
      console.info(TAG, 'player.state:' + this.renderModel.state);
      return this.renderModel.state;
    } else {
      return audio.AudioState.STATE_INVALID;
    }
  }

  /**
   * 获取音频渲染器的最小缓冲区大小
   */
  public getBufferSize(): number {
    return this.bufferSize;
  }
}
```
