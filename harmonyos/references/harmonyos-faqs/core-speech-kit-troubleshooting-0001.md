---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-speech-kit-troubleshooting-0001
title: 初始化语音识别引擎报错
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 故障排查 > 初始化语音识别引擎报错
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:55+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:956672508e9b70bc3ffb5f8122e13be5d3d82d7a9e0d833e34fe58324f3e7f59
---

## 问题现象

在开发语音识别功能时，开发者创建SpeechRecognitionEngine实例并初始化引擎时常见报错如下，该如何解决？

* Asr CreateEngineParams is wrong.
* Error message: Cannot read property 'createEngine' of undefined.
* errCode: 1002200001, errMessage: create param is error, language only support zh-CN now.
* errCode: 1002200001, errMessage: asr engine init failed with other process has initialized.

## 定位过程

* Asr CreateEngineParams is wrong.测试机中存在多个SpeechRecognitionEngine实例。
* Error message:Cannot read property createEngine of undefined.无法读取undefined的属性createEngine，可能原因为当前调试设备不支持。

通过报错信息以及错误码，可尝试对照[Core Speech Kit错误码](../harmonyos-references/errorcode-corespeech.md)定位报错原因。

* 错误码1002200001：
  + errMessage: create param is error,language only support zh-CN now。创建参数错误，当前仅支持语言zh-CN。
  + errMessage: asr engine init failed with other process has initialized.asr。引擎初始化失败，因为其他进程已初始化。

## 分析结论

* Asr CreateEngineParams is wrong。测试机中存在不止一个SpeechRecognitionEngine实例，可能为创建实例使用完成后未及时释放资源导致的再次创建报错。
* Error message:Cannot read property createEngine of undefined。此报错原因是使用模拟器调试语音识别能力，官网的约束与限制已表明该能力当前不支持模拟器，参考语音识别[约束与限制](../harmonyos-guides/speechrecognizer-guide.md#section2020122517405)。
* 错误码1002200001：
  + errMessage: create param is error,language only support zh-CN now。speechRecognizer.createEngine的参数[createEngineParams](../harmonyos-references/hms-ai-speechrecognizer.md#section53411946183318)官网已表明language目前只支持“zh-CN”中文。
  + errMessage: asr engine init failed with other process has initialized.此报错意味着在同一时间或同一环境中已经有另一个实例或进程正在使用相同的资源或配置来初始化asr引擎导致的创建引擎失败。

## 修改建议

* 针对Asr CreateEngineParams is wrong报错，为确保当前设备不会存在多个实例，可以在使用完后要及时释放资源，参考如下代码方案：

  ```ts
  import { speechRecognizer } from '@kit.CoreSpeechKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  // 定义引擎对象
  let asrEngine: speechRecognizer.SpeechRecognitionEngine;
  // 定义监听回调对象
  let listener: speechRecognizer.RecognitionListener = {
    onStart() {
    },
    onEvent() {
    },
    onResult() {
    },
    onComplete(sessionId: string, eventMessage: string) {
      asrEngine.shutdown(); // 识别完成时，及时释放资源，保证下一次能再正常创建引擎实例
      console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
    },
    onError() {
    },
  };

  // 设置创建引擎参数
  let extraParams: Record<string, Object> = { "locate": "CN", "recognizerMode": "short" };
  let initParamsInfo: speechRecognizer.CreateEngineParams = {
    language: 'zh-CN',
    online: 1,
    extraParams: extraParams
  };

  // 创建语音识别实例
  function CreateEngine() {
    speechRecognizer.createEngine(initParamsInfo)
      .then((speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
        // 接收引擎实例
        asrEngine = speechRecognitionEngine;
        console.info(`Succeeded in creating engine, result: ${JSON.stringify(asrEngine)}.`);

        // 设置监听
        asrEngine.setListener(listener);

        // 开始监听
        asrEngine.startListening({
          sessionId: 'xxx', // sessionId字符长度需要小于64，而且不能包含特殊字符，如'.'
          audioInfo: {
            audioType: 'pcm',
            sampleRate: 16000,
            soundChannel: 1,
            sampleBit: 16,
          }
        });
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
      });
  }

  @Entry
  @Component
  struct Index {
    private message: string = 'Hello World';

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            CreateEngine();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* speechRecognizer能力不支持模拟器调试，需切换真机调试。
* 通过speechRecognizer.createEngine方法创建实例的参数CreateEngineParams中的language需改成“zh-CN”。
