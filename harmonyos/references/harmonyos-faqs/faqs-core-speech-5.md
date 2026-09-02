---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-5
title: 初始化语音识别引擎报错
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 初始化语音识别引擎报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:d2209be9d1df7371bfd839af0ffb685f4e1042c246312422beb0c7a80e4ddc7a
---

## 问题现象

在开发语音识别功能时，开发者创建SpeechRecognitionEngine实例并初始化引擎时常见报错如下，该如何解决？

* Asr CreateEngineParams is wrong.
* Error message: Cannot read property 'createEngine' of undefined.
* errCode: 1002200001, errMessage: create param is error, language only support zh-CN now.
* errCode: 1002200001, errMessage: asr engine init failed with other process has initialized.

## 背景知识

语音识别能力应用较广泛，例如设备在无网状态下，为听障人士或不方便收听音频场景提供音频转文本能力等。HarmonyOS侧提供[speechRecognizer](../harmonyos-references/hms-ai-speechrecognizer.md)能力，可以将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为pcm音频文件或者实时语音，详情可参考[官网demo](../harmonyos-guides/speechrecognizer-guide.md)。创建实例并初始化引擎对应的API [speechRecognizer.createEngine](../harmonyos-references/hms-ai-speechrecognizer.md#createengineparams)。

## 问题定位

* Asr CreateEngineParams is wrong.测试机中存在多个SpeechRecognitionEngine实例。
* Error message:Cannot read property createEngine of undefined.无法读取undefined的属性createEngine，可能原因为当前调试设备不支持。

通过报错信息以及错误码，可尝试对照[Core Speech Kit错误码](../harmonyos-references/errorcode-corespeech.md)定位报错原因。

* 错误码1002200001：
  + errMessage: create param is error,language only support zh-CN now。创建参数错误，当前仅支持语言zh-CN。
  + errMessage: asr engine init failed with other process has initialized.asr。引擎初始化失败，因为其他进程已初始化。

## 分析结论

* Asr CreateEngineParams is wrong。测试机中存在不止一个SpeechRecognitionEngine实例，可能为创建实例使用完成后未及时释放资源导致的再次创建报错。
* Error message:Cannot read property createEngine of undefined。此报错原因是使用模拟器调试语音识别能力，官网的约束与限制已表明该能力当前不支持模拟器，参考语音识别[约束与限制](../harmonyos-guides/speechrecognizer-guide.md#约束与限制)。
* 错误码1002200001：
  + errMessage: create param is error,language only support zh-CN now。speechRecognizer.createEngine的参数[createEngineParams](../harmonyos-references/hms-ai-speechrecognizer.md#createengineparams)官网已表明language目前只支持“zh-CN”中文。
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

## 常见FAQ

Q：录音转文字识别结束报错，报错信息onError,sessionId:errorCode:1002200009 errorMessage: Capability SendRequest Error.

A：该报错的原因可能为当前测试机版本过低，建议升级版本测试；同时可以先调用shutdown()方法关闭引擎，再通过createEngine()方法重新初始化引擎。

Q：speechRecognizer.createEngine是否支持在穿戴设备上使用？

A：不支持。Core Speech Kit当前支持的设备类型为Phone、Tablet、PC/2in1，不支持穿戴设备，详情可参考[Core Speech Kit支持的设备](../harmonyos-guides/core-speech-introduction.md#支持的设备)。

## 总结

实现语音识别能力，通过speechRecognizer.createEngine创建实例并初始化引擎报错，可通过排查参数CreateEngineParams、当前调试设备、以及当前调试设备中是否存在多实例问题来解决。
