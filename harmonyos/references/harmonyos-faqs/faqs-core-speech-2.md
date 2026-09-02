---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-2
title: 文本转语音如何区分是否为手动停止播报
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 文本转语音如何区分是否为手动停止播报
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37ebcbe0ee159f5e1b2da2add1bb3c6cd8e75fe0240ad84134319804c8bdde35
---

## 问题现象

文本转语音播报时如何区分是否手动停止？调用stop方法停止播报后，speak的回调顺序是先onComplete然后onStop。无论是正常结束停止还是手动停止都会执行onComplete，应该如何正确区分是用户手动停止还是已经正常结束停止。

## 背景知识

* [文本转语音](../harmonyos-guides/texttospeech-guide.md)：支持将一篇不超过10000字数的中英文文本（简体中文、繁体中文、数字、英文）合成为语音，并以选定音色进行播报。
* [SpeakListener](../harmonyos-references/hms-ai-texttospeech.md#speaklistener)：合成及播报的回调对象，通过此对象可返回合成及播报过程的相关状态，例如开始合成及播报、合成完成、播报完成、停止播报完成等。
* <'queueMode', number>播报模式：0：排队模式播报；1：抢占模式播报。
* onComplete回调触发有2种情况，回调结果[CompleteResponse](../harmonyos-references/hms-ai-texttospeech.md#completeresponse)中type为0表示合成结束，type为1表示播报结束，两者的回调时序并不固定。而onStop回调必然会在播报结束（type为1）的onComplete回调之后触发，即当调用stop接口时，可能会出现两种回调时序：
  + 调用stop前语音已经合成结束：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OIHBjaYoQXuejiy-NBdJEA/zh-cn_image_0000002658914049.png "点击放大")
  + 调用stop前语音还未合成完毕：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/nrS068aMRqu_FJ0b_Gj8lw/zh-cn_image_0000002658794099.png "点击放大")

## 解决方案

采用排队模式播报，在onComplete回调中判断播报完成（即回调结果[CompleteResponse](../harmonyos-references/hms-ai-texttospeech.md#completeresponse)中type为1）时调用[speak](../harmonyos-references/hms-ai-texttospeech.md#speak)方法加载下一个需要播报的文本。示例代码如下：

```ts
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction } from '@kit.ArkUI';
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  textArr: string[] = [
    '\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t' + '纸上得来终觉浅，绝知此事要躬行。\n\t\t',
    '\n\t\t清明时节雨纷纷，路上行人欲断魂；\n\t\t' + '借问酒家何处有？牧童遥指杏花村。\n\t\t'
  ];
  @State curIndex: number = 0;
  @State isManMadeStopped: boolean = false; // 标识是否为手动停止
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();
  ttsEngine: textToSpeech.TextToSpeechEngine | undefined = undefined;
  engineCreated: boolean = false;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          Text(`${this.textArr[this.curIndex]}`)
            .fontSize(20)
            .fontColor(0x317AE7);

          Button() {
            Text('初始化文本转语音引擎')
              .fontColor(Color.White)
              .fontSize(20);
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0A59F7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            this.engineCreated = true;
            this.createByCallback();
            this.promptAction.showToast({
              message: '初始化文本转语音引擎成功!',
              duration: 2000
            });
          });

          Button() {
            Text('合成播报')
              .fontColor(Color.White)
              .fontSize(20);
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0A59F7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            if (this.engineCreated) {
              try {
                this.speak();
                // 重置手动停止状态
                this.isManMadeStopped = false;
                this.promptAction.showToast({
                  message: '开始合成播报',
                  duration: 2000
                });
              } catch (err) {
                this.promptAction.showToast({
                  message: '合成播报失败',
                  duration: 2000
                });
              }
            } else {
              this.promptAction.showToast({
                message: 'The engine has not been created',
                duration: 2000
              });
            }
          });

          Button() {
            Text('停止播报')
              .fontColor(Color.White)
              .fontSize(20);
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0A59F7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            try {
              let isBusy: boolean = this.ttsEngine?.isBusy() || false;
              if (isBusy) {
                this.isManMadeStopped = true;
                this.ttsEngine?.stop();
              }
              this.promptAction.showToast({
                message: '停止播报!',
                duration: 2000
              });
            } catch (err) {
              this.promptAction.showToast({
                message: '停止播报失败',
                duration: 2000
              });
            }
          });

          Button() {
            Text('关闭引擎')
              .fontColor(Color.White)
              .fontSize(20);
          }
          .type(ButtonType.Capsule)
          .backgroundColor('#0A59F7')
          .width('80%')
          .height(50)
          .margin(10)
          .onClick(() => {
            try {
              this.ttsEngine?.shutdown();
              this.engineCreated = false;
              this.promptAction.showToast({
                message: '关闭引擎成功!',
                duration: 2000
              });
            } catch (err) {
              this.promptAction.showToast({
                message: '关闭引擎失败',
                duration: 2000
              });
            }
          });

        }
        .layoutWeight(1);
      }
      .width('100%')
      .height('100%');

    };
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
      textToSpeech.createEngine(initParamsInfo,
        (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
          if (!err) {
            console.info('createEngine is success');
            // 接收创建引擎的实例
            this.ttsEngine = textToSpeechEngine;
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
    let speakListener: textToSpeech.SpeakListener = {
      // 开始播报回调
      onStart(requestId: string, response: textToSpeech.StartResponse) {
        console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
      },
      // 完成播报回调
      onComplete: (requestId: string, response: textToSpeech.CompleteResponse) => {
        console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
        // 播报完成并且非手动停止则自动播报下一个文本
        if (response.type === 1 && !this.isManMadeStopped) {
          // 语音播放结束，加载下一个需要播报的文本
          let speakParams: textToSpeech.SpeakParams = {
            requestId: '123456' + Date.now(), // requestId在同一实例内仅能用一次，请勿重复设置
            extraParams: extraParam
          };
          this.promptAction.showToast({
            message: '播报下一个',
            duration: 2000
          });
          this.curIndex = this.curIndex == this.textArr.length - 1 ? 0 : this.curIndex + 1;
          this.ttsEngine?.speak(this.textArr[this.curIndex], speakParams);
        }
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
        console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
      }
    };
    // 设置回调
    this.ttsEngine?.setListener(speakListener);
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '123456' + Date.now(), // requestId在同一实例内仅能用一次，请勿重复设置
      extraParams: extraParam
    };
    // 调用speak播报方法
    this.ttsEngine?.speak(this.textArr[this.curIndex], speakParams);
  };
}
```
