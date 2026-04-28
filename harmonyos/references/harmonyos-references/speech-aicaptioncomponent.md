---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-aicaptioncomponent
title: AICaptionComponent（AI字幕组件）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS组件 > AICaptionComponent（AI字幕组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ea726263b267779da7025d99ac184a260267b45b1c2e393b8d01160b83ea2b8
---

AI字幕控件使用AI能力将语音实时转化成文本并翻译，提供原文、译文的展示。适用于一些音乐类、视频类等音视频内容App，帮助用户在一些无法直接浏览音频内容或者对音频源语言不熟悉的场景下，通过字幕来高效获取信息。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import {
2. AICaptionComponent, AudioInfo, AudioData, AICaptionOptions, AICaptionController
3. } from "@kit.SpeechKit";
```

## AICaptionComponent

PhonePC/2in1Tablet

AI字幕组件，可以作为动态组件加载。

**装饰器类型：** @Component

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| isShown | boolean | 是 | @Link | 字幕显示状态。  true：显示，从5.1.0(18)开始支持自动识别应用音频生成字幕。  false：隐藏。 |
| controller | [AICaptionController](speech-aicaptioncomponent.md#aicaptioncontroller) | 是 | - | 字幕控制器。 |
| options | [AICaptionOptions](speech-aicaptioncomponent.md#aicaptionoptions) | 是 | - | 字幕初始化参数。 |

### build

PhonePC/2in1Tablet

build(): void

用于创建对象[AICaptionComponent](speech-aicaptioncomponent.md#aicaptioncomponent)的构造函数。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';

3. @Entry
4. @Component
5. struct Index {
6. private captionOption?: AICaptionOptions;
7. private controller = new AICaptionController();
8. @State isShow: boolean = false;

10. aboutToAppear(): void {
11. this.captionOption = {
12. initialOpacity: 1,
13. onPrepared: () => {
14. // ...
15. },
16. onError: () => {
17. // ...
18. }
19. }
20. }

22. build() {
23. Column() {
24. // 调用AICaptionComponent组件初始化字幕
25. AICaptionComponent({
26. isShown: this.isShow,
27. controller: this.controller,
28. options: this.captionOption
29. })
30. }
31. }
32. }
```

## AICaptionController

PhonePC/2in1Tablet

AI字幕控件的主要功能入口类。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { AICaptionComponent, AICaptionOptions, AICaptionController } from '@kit.SpeechKit';

3. @Entry
4. @Component
5. struct Index {
6. private options?: AICaptionOptions;
7. private controller = new AICaptionController();
8. @State isShown: boolean = false;

10. aboutToAppear(): void {
11. this.options = {
12. initialOpacity: 1,
13. onPrepared: () => {
14. // ...
15. },
16. onError: () => {
17. // ...
18. }
19. }
20. }

22. build() {
23. Column() {
24. // 调用AICaptionComponent组件初始化字幕
25. AICaptionComponent({
26. isShown: this.isShown,
27. controller: this.controller,
28. options: this.options
29. })
30. }
31. }
32. }
```

### getAudioInfo

PhonePC/2in1Tablet

getAudioInfo(): AudioInfo

获取要被识别的音频信息。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioInfo](speech-aicaptioncomponent.md#audioinfo) | 获取当前版本字幕支持的音频信息。 |

**示例：**

```
1. import { AICaptionController, AudioInfo } from '@kit.SpeechKit';

3. try {
4. let controller = new AICaptionController();
5. let audioInfo: AudioInfo = controller.getAudioInfo();
6. } catch (e) {
7. console.error(`GetAudioInfo failed. Code: ${e.code}, message: ${e.message}`);
8. }
```

### writeAudio

PhonePC/2in1Tablet

writeAudio(audioData: AudioData): void

写入音频数据。音频流信息格式从[getAudioInfo](speech-aicaptioncomponent.md#getaudioinfo)方法获取（调用此方法会停止自动获取应用音频生成字幕，以写入的音频流为准）。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| audioData | [AudioData](speech-aicaptioncomponent.md#audiodata) | 是 | 音频数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1012900012 | Audio recognition failed. |

**示例：**

```
1. import { AICaptionController } from '@kit.SpeechKit';
2. import { AudioData } from '@kit.SpeechKit';

5. let audioData: AudioData = {
6. data: new Uint8Array()
7. }
8. try {
9. let controller = new AICaptionController();
10. controller.writeAudio(audioData)
11. } catch (e) {
12. console.error(`WriteAudio failed. Code: ${e.code}, message: ${e.message}`);
13. }
```

## AudioInfo

PhonePC/2in1Tablet

音频流信息。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioType | string | 否 | 否 | 音频类型。  当前仅支持 "pcm"编码。 |
| sampleRate | audio.[AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8) | 否 | 否 | 音频采样率。  当前仅支持16000采样率。 |
| soundChannel | audio.[AudioChannel](arkts-apis-audio-e.md#audiochannel8) | 否 | 否 | 音频声道。  当前仅支持1个通道。 |
| sampleBit | number | 否 | 否 | 音频采样字节。  当前仅支持16位。 |

## AudioData

PhonePC/2in1Tablet

音频数据。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 音频数据。  当前仅支持音频数据长度为640字节或1280字节。 建议每次发送音频调用间隔为20ms（传输音频长度为640字节）或40ms（传输音频长度为1280字节）。 |

## AICaptionOptions

PhonePC/2in1Tablet

字幕初始化选项。

**系统能力：** SystemCapability.AI.AICaption

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialOpacity | number | 否 | 是 | 字幕精简态下面板背景的不透明度。  - Phone和tablet的取值范围：[0，1]，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位，默认值：0。  - 2in1有全透明：0 、半透明：0.5 、不透明：1三个选项，默认值：全透明：0。 |
| onPrepared | Callback<void> | 否 | 否 | 监听控件初始化完成的回调函数。 |
| onError | ErrorCallback | 否 | 否 | 监听控件错误的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](speech-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012900010 | AI caption service is busy. |
| 1012900011 | AI caption controller initialized failed. |
