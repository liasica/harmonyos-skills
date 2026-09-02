---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-1
title: 文本转语音引擎使用问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 文本转语音引擎使用问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:375d5bbde94050d675697697ceaa5dac9781589d2e815931018ff97a1e83e7d0
---

## 问题现象

问题步骤如下：

1. 启动程序进入App的主页。点击播报按钮，文本转语音（textToSpeech，以下简称：tts）实例开始播报。
2. 点击进入详情页面按钮，详情页面的tts实例开始播报。
3. 在详情页面点击返回到主页按钮，详情页面的tts实例在aboutToDisappear()方法中被释放。
4. 返回到主页后再次点击主页的播报按钮，主页的tts实例监听器回调错误信息，日志显示引擎未初始化的异常（1002300007）。

两个页面使用的是不同的tts实例对象，为什么详情页面的tts实例释放后会影响到主页tts实例的播报？引擎初始化代码如下：

```ts
private async init() {
  const extraParams: Record<string, Object> = {
    "style": 'interaction-broadcast',
    "locate": 'CN',
    // 可选，设置引擎名称
    "name": 'EngineName'
  };
  const params: textToSpeech.CreateEngineParams = {
    language: 'zh-CN',
    online: 1,
    person: 0,
    extraParams: extraParams
  };
  this._ttsEngine = await textToSpeech.createEngine(params);
  this.registerListener(
    () => { this._listener?.onStart?.(); },
    () => { this._listener?.onStop?.(); },
    () => { this._listener?.onCompleted?.(); },
    (code, message) => { this._listener?.onError?.(code, message); }
  );
}
```

释放引擎代码如下：

```ts
release() {
  // 释放资源
  this.unregisterListener();
  this._ttsEngine?.shutdown();
  this._ttsEngine = null;
}
```

## 背景知识

文本转语音类，用于执行文本转语音过程中的相关操作。在调用[TextToSpeechEngine](../harmonyos-references/hms-ai-texttospeech.md#texttospeechengine)的方法前，需要先通过[createEngine()](../harmonyos-references/hms-ai-texttospeech.md#texttospeechcreateengine)方法创建一个TextToSpeechEngine实例。结束使用后，可以调用[shutdown()](../harmonyos-references/hms-ai-texttospeech.md#shutdown)方法关闭引擎，释放引擎资源。

## 解决方案

该问题是两个页面引擎名称相同导致的，可以在引擎参数的name属性中使用UUID，或是其他命名方式，只需保证引擎名称不重复即可，此时第二个页面使用this.textToSpeech.release()就会只释放当前页面的引擎资源且不影响第一个页面。创建引擎参数修改参考如下：

```ts
// 初始化引擎
async init() {
  // 1. 生成唯一 UUID，确保每个页面的引擎名称不重复
  let uuid = util.generateRandomUUID(true);

  const extraParams: Record<string, Object> = {
    "style": 'interaction-broadcast',
    "locate": 'CN',
    // 【关键点】设置唯一的引擎名称，避免多实例冲突
    "name": `Engine-${this._pageName}-${uuid}`
  };

  const params: textToSpeech.CreateEngineParams = {
    language: 'zh-CN',
    online: 1,
    person: 0,
    extraParams: extraParams
  };

  try {
    // 创建引擎
    this._ttsEngine = await textToSpeech.createEngine(params);
    console.info(`[${this._pageName}] TTS 引擎初始化成功, Name: ${extraParams.name}`);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`[${this._pageName}] TTS 初始化失败: ${error.code}, ${error.message}`);
  }
}
```

完整示例参考如下：

```ts
import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS'; // 用于生成UUID

class TtsWrapper {
  private _ttsEngine: textToSpeech.TextToSpeechEngine | null = null;
  private _pageName: string = '';

  constructor(pageName: string) {
    this._pageName = pageName;
  }

  // 初始化引擎
  async init() {
    // 1. 生成唯一 UUID，确保每个页面的引擎名称不重复
    let uuid = util.generateRandomUUID(true);

    const extraParams: Record<string, Object> = {
      "style": 'interaction-broadcast',
      "locate": 'CN',
      // 【关键点】设置唯一的引擎名称，避免多实例冲突
      "name": `Engine-${this._pageName}-${uuid}`
    };

    const params: textToSpeech.CreateEngineParams = {
      language: 'zh-CN',
      online: 1,
      person: 0,
      extraParams: extraParams
    };

    try {
      // 创建引擎
      this._ttsEngine = await textToSpeech.createEngine(params);
      console.info(`[${this._pageName}] TTS 引擎初始化成功, Name: ${extraParams.name}`);
    } catch (err) {
      let error = err as BusinessError;
      console.error(`[${this._pageName}] TTS 初始化失败: ${error.code}, ${error.message}`);
    }
  }

  // 播报文本
  speak(text: string, ctx: UIContext) {
    if (!this._ttsEngine) {
      console.error(`[${this._pageName}] 引擎为空`);
      return;
    }

    let speakParams: textToSpeech.SpeakParams = {
      requestId: util.generateRandomUUID(true),
      extraParams: {
        "speed": 1.0,
        "volume": 1.0,
        "pitch": 1.0,
        "audioType": 1
      }
    };

    this._ttsEngine.speak(text, speakParams);
    try {
      ctx.getPromptAction().showToast({ message: `[${this._pageName}] 正在播报...` });
    } catch (error) {
      console.error(`显示提示失败: ${error.code}, ${error.message}`);
    }
  }

  // 释放资源
  release() {
    if (this._ttsEngine) {
      this._ttsEngine.shutdown();
      this._ttsEngine = null;
      console.info(`[${this._pageName}] TTS 引擎已释放`);
    }
  }
}

@Entry
@Component
struct Index {
  // 路由栈
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

  // 主页面的 TTS 实例
  private homeTts: TtsWrapper = new TtsWrapper('HomePage');

  async aboutToAppear() {
    // 初始化主页 TTS
    await this.homeTts.init();
  }

  @Builder
  PageMap(name: string) {
    if (name === 'DetailPage') {
      DetailComponent();
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column({ space: 20 }) {
        Text('TTS 多实例冲突解决演示')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 20 })

        // 1. 主页播报测试
        Button('1. 主页播报 (Home Speak)')
          .width('80%')
          .onClick(() => {
            this.homeTts.speak('这是主页的语音播报，引擎正常工作。', this.getUIContext());
          })

        // 2. 跳转到详情页
        Button('2. 进入详情页 (Go to Detail)')
          .width('80%')
          .backgroundColor(Color.Orange)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'DetailPage' });
          })
      }
      .width('100%')
      .height('100%')
    }
    .mode(NavigationMode.Stack)
    .navDestination(this.PageMap)
    .title('Home Page')
  }
}

@Component
struct DetailComponent {
  @Consume('pageInfos') pageInfos: NavPathStack;
  // 详情页的 TTS 实例
  private detailTts: TtsWrapper = new TtsWrapper('DetailPage');

  async aboutToAppear() {
    // 初始化详情页 TTS
    await this.detailTts.init();
  }

  // 【关键】页面销毁时释放资源
  aboutToDisappear() {
    console.info('详情页销毁，释放详情页 TTS 资源');
    this.detailTts.release();
  }

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Text('详情页面')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .margin({ top: 50 })

        Button('3. 详情页播报 (Detail Speak)')
          .width('80%')
          .onClick(() => {
            this.detailTts.speak('这是详情页的播报。返回后，我将被销毁。', this.getUIContext());
          })

        Button('返回主页 (Back)')
          .width('80%')
          .backgroundColor(Color.Gray)
          .onClick(() => {
            this.pageInfos.pop();
          })
      }
      .width('100%')
      .height('100%')
    }
    .title('Detail Page')
  }
}
```

## 常见FAQ

Q：文本转语音组件在文字内容未完全播放完成时，会执行onComplete回调。

A：合成或播报结束后，[onComplete](../harmonyos-references/hms-ai-texttospeech.md#oncomplete)监听都会触发，可以确认此时的[CompleteResponse](../harmonyos-references/hms-ai-texttospeech.md#completeresponse)的type值（0：合成结束，1：播报结束）。

Q：文本转语音引擎在调用speak()方法开始说话时就回调了onComplete，导致回调状态错乱。

A：speak()方法开始会有个合成语音的动作，合成或播报结束后分别回调[onComplete](../harmonyos-references/hms-ai-texttospeech.md#oncomplete)接口，可以根据返回type值（0：合成结束，1：播报结束）的不同进行接下来不同逻辑处理的区分。

Q：文本转语音怎么实现暂停和继续播报？

A：当需要停止合成及停止播报时，可调用ttsEngine.stop()方法，再次开始使用ttsEngine.speak()方法。若要实现暂停后继续播放，有两种方式：

1. speak()获取的是音频流，根据音频流做对应的估算。
2. 可以参考[Speech Kit](../harmonyos-references/speech-api.md)(场景化语音服务)，该服务提供一套基于[Core Speech Kit](../harmonyos-references/core-speech-api.md)(基础语音服务)的播控UI组件，可满足暂停后继续播放的需求。

Q：文本转语音如何实现后台播报？

A：文本转语音当前支持后台播报，在[CreateEngineParams](../harmonyos-references/hms-ai-texttospeech.md#createengineparams)参数中的extraParams字段，设置'isBackStage': true时，tts支持后台播报。

Q：文本转语音时，文本过长时如何顺畅，有序播放？

A：tts是一边播一边合成的，文本过长的情况，可以先分割文本，建议以逗号、句号或者换行符为分隔符，用分割后的文本分次合成。因为onData模式不能保证数据按序到达，需要对收到的数据，根据数据内容进行排序，然后合成。
