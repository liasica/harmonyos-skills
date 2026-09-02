---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent
title: AICaptionComponent（AI字幕组件）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS组件 > AICaptionComponent（AI字幕组件）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fa0f1d58ecf9a47b0ae88b153ab55f704d267c7bf34a215daa6245fcaaa01494
---

AI字幕控件使用AI能力将语音实时转化成文本并翻译，提供原文、译文的展示。适用于一些音乐类、视频类等音视频内容App，帮助用户在一些无法直接浏览音频内容或者对音频源语言不熟悉的场景下，通过字幕来高效获取信息。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import {
  AICaptionComponent, AudioInfo, AudioData, AICaptionOptions, AICaptionController, AICaptionFontSize
} from '@kit.SpeechKit';
```

## AICaptionComponent

AI字幕组件，可以作为动态组件加载。

**装饰器类型：** @Component

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| isShown | boolean | 是 | @Link | 字幕显示状态。  true：显示，从5.1.0(18)开始支持自动识别应用音频生成字幕。  false：隐藏。 |
| controller | [AICaptionController](speech-aicaptioncomponent.md#aicaptioncontroller) | 是 | - | 字幕控制器。 |
| options | [AICaptionOptions](speech-aicaptioncomponent.md#aicaptionoptions) | 是 | - | 字幕初始化参数。 |

### build

build(): void

用于创建对象[AICaptionComponent](speech-aicaptioncomponent.md#aicaptioncomponent)的构造函数。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private captionOption?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShow: boolean = false;

  aboutToAppear(): void {
    this.captionOption = {
      initialOpacity: 1,
      onPrepared: () => {
        // ...
      },
      onError: () => {
        // ...
      }
    };
  }

  build() {
    Column() {
      // 调用AICaptionComponent组件初始化字幕
      AICaptionComponent({
        isShown: this.isShow,
        controller: this.controller,
        options: this.captionOption
      })
    }
  }
}
```

组件如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0QfaI6-CSQmv3O2I1f5bcA/zh-cn_image_0000002736316237.png)

## AICaptionController

AI字幕控件的主要功能入口类。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**示例：**

```typescript
import { AICaptionComponent, AICaptionOptions, AICaptionController } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private options?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShown: boolean = false;

  aboutToAppear(): void {
    this.options = {
      initialOpacity: 1,
      onPrepared: () => {
        // ...
      },
      onError: () => {
        // ...
      }
    };
  }

  build() {
    Column() {
      // 调用AICaptionComponent组件初始化字幕
      AICaptionComponent({
        isShown: this.isShown,
        controller: this.controller,
        options: this.options
      })
    }
  }
}
```

### isCapabilitySupported

isCapabilitySupported(): boolean

检测设备是否支持AI字幕功能。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持AI字幕功能特性。true：支持AI字幕功能。false：不支持AI字幕功能。 |

**示例：**

```typescript
import { AICaptionComponent, AICaptionOptions, AICaptionController } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private captionOption?: AICaptionOptions;
  private controller: AICaptionController = new AICaptionController();
  @State isSupport: boolean = false;
  @State isShown: boolean = false;

  aboutToAppear(): void {
    // AI字幕初始化参数，设置字幕的不透明度和回调函数
    this.captionOption = {
      initialOpacity: 1,
      onPrepared: () => {
        console.info('onPrepared')
      },
      onError: (error: BusinessError) => {
        console.error(`AICaption component error. Error code: ${error.code}, message: ${error.message}`);
      }
    };
    this.isSupport = this.controller.isCapabilitySupported();
    this.isShown = true;
  }

  build() {
    Column({ space: 20 }) {
      // 调用AICaptionComponent组件初始化字幕
      if (this.isSupport) {
        AICaptionComponent({
          isShown: this.isShown,
          controller: this.controller,
          options: this.captionOption
        })
      }
    }
  }
}
```

### getAudioInfo

getAudioInfo(): AudioInfo

获取要被识别的音频信息。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioInfo](speech-aicaptioncomponent.md#audioinfo) | 获取当前版本字幕支持的音频信息。 |

**示例：**

```typescript
import { AICaptionController, AudioInfo } from '@kit.SpeechKit';

try {
  let controller = new AICaptionController();
  let audioInfo: AudioInfo = controller.getAudioInfo();
} catch (e) {
  console.error(`GetAudioInfo failed. Code: ${e.code}, message: ${e.message}`);
}
```

### writeAudio

writeAudio(audioData: AudioData): void

写入音频数据。音频流信息格式从[getAudioInfo](speech-aicaptioncomponent.md#getaudioinfo)方法获取（调用此方法会停止自动获取应用音频生成字幕，以写入的音频流为准）。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioData | [AudioData](speech-aicaptioncomponent.md#audiodata) | 是 | 音频数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-speech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1012900012 | Audio recognition failed. |

**示例：**

```typescript
import { AICaptionController, AudioData } from '@kit.SpeechKit';

let audioData: AudioData = {
  data: new Uint8Array()
};
try {
  let controller = new AICaptionController();
  controller.writeAudio(audioData);
} catch (e) {
  console.error(`WriteAudio failed. Code: ${e.code}, message: ${e.message}`);
}
```

## AudioInfo

音频流信息。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioType | string | 否 | 否 | 音频类型。  当前仅支持 "pcm"编码。 |
| sampleRate | audio.[AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8) | 否 | 否 | 音频采样率。  当前仅支持16000采样率。 |
| soundChannel | audio.[AudioChannel](arkts-apis-audio-e.md#audiochannel8) | 否 | 否 | 音频声道。  当前仅支持1个通道。 |
| sampleBit | number | 否 | 否 | 音频采样字节。  当前仅支持16位。 |

## AudioData

音频数据。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 音频数据。  当前仅支持音频数据长度为640字节或1280字节。 建议每次发送音频调用间隔为20ms（传输音频长度为640字节）或40ms（传输音频长度为1280字节）。 |

## AICaptionOptions

字幕初始化选项。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialOpacity | number | 否 | 是 | 字幕精简态下面板背景的不透明度。  - Phone和tablet的取值范围：[0，1]，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位，默认值：0。  - 2in1有全透明：0 、半透明：0.5 、不透明：1三个选项，默认值：全透明：0。 |
| onPrepared | Callback<void> | 否 | 否 | 监听控件初始化完成的回调函数。 |
| onError | ErrorCallback | 否 | 否 | 监听控件错误的回调函数。 |
| sourceLanguage | string | 否 | 是 | 字幕源语言。  取值范围：['zh','en']，'zh'表示中文，'en'表示英文，默认值：'zh'。  **起始版本：** 6.1.1(24) |
| targetLanguage | string | 否 | 是 | 字幕目标语言。  - 当sourceLanguage为英文时，targetLanguage取值范围：['zh','en','zh-en']。  - 当sourceLanguage为中文时，targetLanguage取值范围：['zh']。  'zh'表示中文，'en'表示英文，'zh-en'表示中英双语，默认值：'zh'。  **起始版本：** 6.1.1(24) |
| fontSize | [AICaptionFontSize](speech-aicaptioncomponent.md#aicaptionfontsize) | 否 | 是 | 字幕源语言及目标语言字体大小。  默认值为标准大小。  **起始版本：** 6.1.1(24) |
| fontColor | ResourceColor | 否 | 是 | 字幕源语言及目标语言字体颜色。  默认值为白色。  **起始版本：** 6.1.1(24) |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-speech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012900010 | AI caption service is busy. |
| 1012900011 | AI caption controller initialized failed. |
| 1012900013 | AI caption controller init param failed. |

## AICaptionFontSize

AI字幕字体大小的枚举类。

**系统能力：** SystemCapability.AI.AICaption

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMALL | 1 | 表示字体大小为小号。 |
| NORMAL | 2 | 表示字体大小为标准。 |
| BIG | 3 | 表示字体大小为大号。 |
| LARGE | 4 | 表示字体大小为超大。 |
