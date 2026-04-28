---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/hms-ai-speechrecognizer
title: speechRecognizer（语音识别）
breadcrumb: API参考 > AI > Core Speech Kit（基础语音服务） > ArkTS API > speechRecognizer（语音识别）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f20e28727e605b5f7af3a477d59711d240748ce112c11a9a0b7e2fd2fdfac822
---

语音识别服务提供将音频信息转换为文本的能力，便于用户与设备进行互动，实现实时语音交互、语音识别。

目前本服务支持的语种为中文，支持的模型为离线。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1Tablet

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';
```

## speechRecognizer.createEngine

PhonePC/2in1Tablet

createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<SpeechRecognitionEngine>): void

创建SpeechRecognitionEngine实例，并初始化引擎。使用callback异步回调。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| createEngineParams | [CreateEngineParams](hms-ai-speechrecognizer.md#createengineparams) | 是 | 创建引擎实例的配置项。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[SpeechRecognitionEngine](hms-ai-speechrecognizer.md#speechrecognitionengine)> | 是 | 回调函数。返回创建的引擎实例。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002200001 | Create engine failed. |
| 1002200006 | The engine of SpeechRecognition is busy. |
| 1002200008 | The engine of SpeechRecognition is being destroyed. |
| 1002200009 | Internal Service Error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { speechRecognizer } from '@kit.CoreSpeechKit';

4. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

6. // 设置创建引擎参数
7. let extraParams: Record<string, Object> = { "locate": "CN", "recognizerMode": "short" }
8. let initParamsInfo: speechRecognizer.CreateEngineParams = {
9. language: 'zh-CN',
10. online: 1,
11. extraParams: extraParams
12. };

14. // 调用createEngine方法
15. speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine:
16. speechRecognizer.SpeechRecognitionEngine) => {
17. if (!err) {
18. // 接收创建引擎的实例
19. asrEngine = speechRecognitionEngine;
20. } else {
21. // 无法创建引擎时返回错误码1002200001，原因：语种不支持、模式不支持、初始化超时、资源不存在等导致创建引擎失败
22. // 无法创建引擎时返回错误码1002200006，原因：引擎正在忙碌中，一般多个应用同时调用语音识别引擎时触发
23. // 无法创建引擎时返回错误码1002200008，原因：引擎已被销毁
24. console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
25. }
26. });

28. @Entry
29. @Component
30. struct Page {

32. build() {
33. // ...
34. }
35. }
```

## speechRecognizer.createEngine

PhonePC/2in1Tablet

createEngine(createEngineParams: CreateEngineParams): Promise<SpeechRecognitionEngine>

创建SpeechRecognitionEngine实例，并初始化引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| createEngineParams | [CreateEngineParams](hms-ai-speechrecognizer.md#createengineparams) | 是 | 创建引擎实例的配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SpeechRecognitionEngine](hms-ai-speechrecognizer.md#speechrecognitionengine)> | Promise对象。返回创建的引擎实例。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002200001 | Create engine failed. |
| 1002200006 | The engine of SpeechRecognition is busy. |
| 1002200008 | The engine of SpeechRecognition is being destroyed. |
| 1002200009 | Internal Service Error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { speechRecognizer } from '@kit.CoreSpeechKit';

4. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

6. // 设置创建引擎参数
7. let extraParams: Record<string, Object> = { "locate": "CN", "recognizerMode": "short" }
8. let initParamsInfo: speechRecognizer.CreateEngineParams = {
9. language: 'zh-CN',
10. online: 1,
11. extraParams: extraParams
12. };

14. // 调用createEngine方法
15. speechRecognizer.createEngine(initParamsInfo).then((speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
16. // 接收引擎实例
17. asrEngine = speechRecognitionEngine;
18. console.info(`Succeeded in creating engine.`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
21. });

23. @Entry
24. @Component
25. struct Page {

27. build() {
28. // ...
29. }
30. }
```

## SpeechRecognitionEngine

PhonePC/2in1Tablet

语音识别类，用于执行语音识别过程中的相关操作。在调用SpeechRecognitionEngine的方法前，需要先通过[createEngine](hms-ai-speechrecognizer.md#speechrecognizercreateengine)方法创建一个[SpeechRecognitionEngine](hms-ai-speechrecognizer.md#speechrecognitionengine)实例。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

### listLanguages

PhonePC/2in1Tablet

listLanguages(params: LanguageQuery, callback: AsyncCallback<Array<string>>): void

查询支持的语种信息，使用callback异步回调。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [LanguageQuery](hms-ai-speechrecognizer.md#languagequery) | 是 | 查询语种信息请求参数。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数。返回查询结果。  当前仅支持中文，返回结果为：["zh-CN"]。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200007 | The engine is not initialized. |
| 1002200009 | Internal Service Error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { speechRecognizer } from '@kit.CoreSpeechKit';

4. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

6. @Entry
7. @Component
8. struct Page {
9. // 查询语种信息，以callback形式返回
10. private queryLanguagesCallback() {
11. // 设置查询相关参数
12. let languageQuery: speechRecognizer.LanguageQuery = {
13. sessionId: '123456'
14. };
15. // 调用listLanguages方法
16. asrEngine?.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
17. if (!err) {
18. // 接收目前支持的语种信息
19. console.info(`Succeeded in listing languages, result: ${JSON.stringify(languages)}.`);
20. } else {
21. console.error(`Failed to list languages. Code: ${err.code}, message: ${err.message}.`);
22. }
23. });
24. }

26. build() {
27. // ...
28. }
29. }
```

### listLanguages

PhonePC/2in1Tablet

listLanguages(params: LanguageQuery): Promise<Array<string>>

查询支持的语种信息，使用Promise异步回调。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [LanguageQuery](hms-ai-speechrecognizer.md#languagequery) | 是 | 查询语种信息请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象。返回查询的结果。  当前仅支持中文，返回结果为：["zh-CN"]。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200007 | The engine is not initialized. |
| 1002200009 | Internal Service Error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { speechRecognizer } from '@kit.CoreSpeechKit';

4. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
5. // 设置查询相关的参数
6. let languageQuery: speechRecognizer.LanguageQuery = {
7. sessionId: '123456'
8. };

10. @Entry
11. @Component
12. struct Page {
13. build() {
14. Button()
15. .id('Button')
16. .fontSize(20)
17. .onClick( () => {
18. // 调用listLanguages方法，查询引擎目前支持的语种信息，以Promise返回
19. asrEngine?.listLanguages(languageQuery).then((res: Array<string>) => {
20. console.info(`Succeeded in listing languages, result: ${JSON.stringify(res)}.`);
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to list languages. Code: ${err.code}, message: ${err.message}.`);
23. });
24. })
25. }
26. }
```

### setListener

PhonePC/2in1Tablet

setListener(listener: RecognitionListener): void

设置语音识别回调。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [RecognitionListener](hms-ai-speechrecognizer.md#recognitionlistener) | 是 | 回调对象，识别过程中所有回调信息均通过此对象返回。 |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

### startListening

PhonePC/2in1Tablet

startListening(params: StartParams): void

启动语音识别。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [StartParams](hms-ai-speechrecognizer.md#startparams) | 是 | 启动语音识别的相关参数，用于设置会话ID、音频配置信息等。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200002 | Start listening failed. |
| 1002200007 | The engine is not initialized. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置开始识别相关参数
5. let recognizerParams: speechRecognizer.StartParams = {
6. sessionId: '123456',
7. audioInfo: { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }
8. }

10. @Entry
11. @Component
12. struct Page {
13. build() {
14. Button()
15. .id('Button')
16. .onClick( () => {
17. // 调用开始识别方法
18. asrEngine?.startListening(recognizerParams);
19. })
20. }
21. }
```

### writeAudio

PhonePC/2in1Tablet

writeAudio(sessionId: string, audio: Uint8Array): void

写音频流，最大音频长度为60000ms。为了确保收到识别结果，请优先调用[setListener](hms-ai-speechrecognizer.md#setlistener)和[startListening](hms-ai-speechrecognizer.md#startlistening)。

此接口在调用[speechRecognizer.createEngine](hms-ai-speechrecognizer.md#speechrecognizercreateengine)、[speechRecognizer.createEngine](hms-ai-speechrecognizer.md#speechrecognizercreateengine-1)、[setListener](hms-ai-speechrecognizer.md#setlistener)、[startListening](hms-ai-speechrecognizer.md#startlistening)之后使用。如果是通过录音，不需要显式调用writeAudio；如果是写音频流文件，需要Core File Kit相关接口循环读取文件，详见[开发步骤](../harmonyos-guides/speechrecognizer-guide.md#开发步骤)。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| audio | Uint8Array | 是 | 待识别的音频数据，当前仅支持音频数据长度为640字节或1280字节。每次发送音频调用间隔必须为20ms（传输音频长度为640字节）或40ms（传输音频长度为1280字节）。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200003 | Exceeded the maximum audio length supported. |
| 1002200007 | The engine is not initialized. |
| 1002200010 | Write audio failed because the start listening is failed. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置独立的sessionId
5. let sessionId: string = '123456';
6. let uint8Array: Uint8Array = new Uint8Array();
7. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流

9. @Entry
10. @Component
11. struct Page {
12. build() {
13. Button()
14. .id('Button')
15. .onClick( () => {
16. // 写入音频流，音频流长度仅支持640字节或1280字节
17. asrEngine?.writeAudio(sessionId, uint8Array);
18. })
19. }
20. }
```

### finish

PhonePC/2in1Tablet

finish(sessionId: string): void

结束识别。为了确保事件回调，请优先调用[setListener](hms-ai-speechrecognizer.md#setlistener)。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200004 | Finish recognition failed. |
| 1002200007 | The engine is not initialized. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置独立的sessionId
5. let sessionId: string = '123456';
6. let uint8Array: Uint8Array = new Uint8Array();
7. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流

9. @Entry
10. @Component
11. struct Page {
12. build() {
13. Column(){
14. Button()
15. .id('Button')
16. .onClick( () => {
17. // 写入音频流，音频流长度仅支持640字节或1280字节
18. asrEngine?.writeAudio(sessionId, uint8Array);
19. })

21. Button() {
22. Text("finish")
23. .fontColor(Color.White)
24. .fontSize(20)
25. }
26. .type(ButtonType.Capsule)
27. .backgroundColor("#0x317AE7")
28. .width("80%")
29. .height(50)
30. .margin(10)
31. .onClick(() => {
32. // 结束识别
33. asrEngine?.finish(sessionId);
34. })
35. }
36. }
37. }
```

### cancel

PhonePC/2in1Tablet

cancel(sessionId: string): void

取消识别。为了确保事件回调，请优先调用[setListener](hms-ai-speechrecognizer.md#setlistener)。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1002200005 | Cancel recognition failed. |
| 1002200007 | The engine is not initialized. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置独立的sessionId
5. let sessionId: string = '123456';
6. let uint8Array: Uint8Array = new Uint8Array();
7. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流

9. @Entry
10. @Component
11. struct Page {
12. build() {
13. Column(){
14. Button()
15. .id('Button')
16. .onClick( () => {
17. // 写入音频流，音频流长度仅支持640字节或1280字节
18. asrEngine?.writeAudio(sessionId, uint8Array);
19. })

21. Button() {
22. Text("cancel")
23. .fontColor(Color.White)
24. .fontSize(20)
25. }
26. .type(ButtonType.Capsule)
27. .backgroundColor("#0x317AE7")
28. .width("80%")
29. .height(50)
30. .margin(10)
31. .onClick(() => {
32. // 调用cancel方法
33. asrEngine?.cancel('123456');
34. })
35. }
36. }
37. }
```

### isBusy

PhonePC/2in1Tablet

isBusy(): boolean

判断引擎是否繁忙。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 服务是否处于繁忙状态的返回值。  - true：引擎正处于繁忙状态。  - false：引擎没有处于繁忙状态。 |

**错误码：**

以下错误码的详细介绍请参见[Core Speech Kit错误码](errorcode-corespeech.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1002200007 | The engine is not initialized. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置独立的sessionId
5. let sessionId: string = '123456';
6. let uint8Array: Uint8Array = new Uint8Array();
7. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流

9. @Entry
10. @Component
11. struct Page {
12. build() {
13. Column() {
14. Button()
15. .id('Button')
16. .onClick(() => {
17. // 写入音频流，音频流长度仅支持640字节或1280字节
18. asrEngine?.writeAudio(sessionId, uint8Array);
19. })

21. Button() {
22. Text("cancel")
23. .fontColor(Color.White)
24. .fontSize(20)
25. }
26. .type(ButtonType.Capsule)
27. .backgroundColor("#0x317AE7")
28. .width("80%")
29. .height(50)
30. .margin(10)
31. .onClick(() => {
32. // 调用isBusy方法
33. let isBusy = asrEngine?.isBusy();
34. console.info(`isBusy: ${isBusy}`);
35. })
36. }
37. }
38. }
```

### shutdown

PhonePC/2in1Tablet

shutdown(): void

关闭引擎，释放资源。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 设置独立的sessionId
5. let sessionId: string = '123456';
6. let uint8Array: Uint8Array = new Uint8Array();
7. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流

9. @Entry
10. @Component
11. struct Page {
12. build() {
13. Column() {
14. Button()
15. .id('Button')
16. .onClick(() => {
17. // 写入音频流，音频流长度仅支持640字节或1280字节
18. asrEngine?.writeAudio(sessionId, uint8Array);
19. })

21. Button() {
22. Text("cancel")
23. .fontColor(Color.White)
24. .fontSize(20)
25. }
26. .type(ButtonType.Capsule)
27. .backgroundColor("#0x317AE7")
28. .width("80%")
29. .height(50)
30. .margin(10)
31. .onClick(() => {
32. // 调用shutdown方法
33. asrEngine?.shutdown();
34. })
35. }
36. }
37. }
```

## RecognitionListener

PhonePC/2in1Tablet

语音识别的回调对象，通过此对象可返回识别过程的相关状态，例如识别开始、识别完成、音频开始、音频结束等。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

### onStart

PhonePC/2in1Tablet

onStart(sessionId: string, eventMessage: string): void

开始识别时，回调此方法。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| eventMessage | string | 是 | 开始识别信息描述。  返回值为一个句子，描述开始识别结果的状态信息，开始识别成功则返回：startListening success. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

### onEvent

PhonePC/2in1Tablet

onEvent(sessionId: string, eventCode: number, eventMessage: string): void

识别过程中的事件都通过此方法回调，例如音频开始、音频结束。vadBegin或vadEnd时触发。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| eventCode | number | 是 | 事件标识。  1：音频开始标识。  3：音频结束标识。 |
| eventMessage | string | 是 | 事件信息描述。  返回值为一个句子，描述识别过程的事件信息。  - 音频开始：speech started.  - 音频结束：speech stopped. |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

### onResult

PhonePC/2in1Tablet

onResult(sessionId: string, result: SpeechRecognitionResult): void

识别的中间结果和最终结果都通过此方法返回。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| result | [SpeechRecognitionResult](hms-ai-speechrecognizer.md#speechrecognitionresult) | 是 | 识别结果。 |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

### onComplete

PhonePC/2in1Tablet

onComplete(sessionId: string, eventMessage: string): void

识别结束或者调用[finish](hms-ai-speechrecognizer.md#finish)方法主动结束识别时回调此方法，返回会话ID、识别完成的相关描述信息。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| eventMessage | string | 是 | 识别完成的相关信息。  返回值为一个句子，描述识别结束的状态信息：recognize complete |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

### onError

PhonePC/2in1Tablet

onError(sessionId: string, errorCode: number, errorMessage: string): void

识别过程中，出现错误时回调，返回会话ID、错误码及错误信息描述。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| errorCode | number | 是 | 返回的错误码：  401 参数检查失败  1002200002 开始识别失败  1002200003 超过最大音频  1002200004 结束识别失败  1002200005 取消识别失败  1002200006 服务忙碌  1002200007 引擎未初始化  1002200010 语音识别未启动  1002200011 语音识别异常  1002200012 没有获取麦克风权限  错误码详细信息参见：[Core Speech Kit错误码](errorcode-corespeech.md)。 |
| errorMessage | string | 是 | 错误信息描述。 |

**示例：**

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. // 创建回调对象
5. let setListener: speechRecognizer.RecognitionListener = {
6. // 开始识别成功回调
7. onStart(sessionId: string, eventMessage: string) {
8. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
9. },
10. // 事件回调
11. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
12. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
13. },
14. // 识别结果回调，包括中间结果和最终结果
15. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
16. console.info(`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}`);
17. },
18. // 识别完成回调
19. onComplete(sessionId: string, eventMessage: string) {
20. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
21. },
22. // 错误回调，错误码通过本方法返回
23. onError(sessionId: string, errorCode: number, errorMessage: string) {
24. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
25. },
26. }

28. @Entry
29. @Component
30. struct Page {
31. build() {
32. Button()
33. .id('Button')
34. .onClick( () => {
35. // 设置回调
36. asrEngine?.setListener(setListener);
37. })
38. }
39. }
```

## CreateEngineParams

PhonePC/2in1Tablet

创建引擎实例的相关参数，用于配置语种、模式、区域信息等。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| language | string | 否 | 否 | 语种，当前仅支持“zh-CN”中文。 |
| online | number | 否 | 否 | 模式。  1为离线，当前仅支持离线模式。 |
| extraParams | Record<string, Object> | 否 | 是 | - <'locate', string> 区域信息。  可选，不设置时默认为“CN”，当前仅支持“CN”。  - <'recognizerMode', string> 语言模式。  可选，不设置时默认为“short”，当前支持“short“和“long”。  - <'sysGeneralLexicon, string[]> 系统热词。支持配置热词提高识别率。系统热词针对应用，在整个识别过程中都生效。  可选，不设置时默认为空。热词总数不超过200，每个热词长度范围为[2, 20]。 |

## LanguageQuery

PhonePC/2in1Tablet

查询语种信息时的相关参数，例如查询离线模式下服务支持的语种信息，需将online参数设置为1。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| extraParams | Record<string, Object> | 否 | 是 | - <'online', number> 模式。  可选，1为离线，当前仅支持离线。 |

## StartParams

PhonePC/2in1Tablet

启动语音识别的相关参数，用于设置会话ID、音频配置信息等。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 会话ID，会话的唯一标识。  由字母、数字、下划线和短横线组成，无长度限制。 |
| audioInfo | [AudioInfo](hms-ai-speechrecognizer.md#audioinfo) | 否 | 否 | 音频配置信息。 |
| extraParams | Record<string, Object> | 否 | 是 | - <'recognitionMode', number>实时语音识别模式。  0：实时录音识别（需应用开启录音权限：ohos.permission.MICROPHONE），若需结束录音，则调用[finish](hms-ai-speechrecognizer.md#finish)方法；  1：实时音频转文字识别，开启此模式时需要额外调用[writeAudio](hms-ai-speechrecognizer.md#writeaudio)方法，传入待识别音频流；  可选，不传参时默认为1。  - <'vadBegin', number>  Voice Activity Detection(VAD)前端点设置。长语音模式不支持配置，当前长语音模式下默认存在语音输入。短语音模式中用于检测语音开始，若语音开始时间超出参数范围则认为无语音输入。参数范围是[500,10000]。  可选，不传参时默认为10000ms。  - <'vadEnd', number>  Voice Activity Detection(VAD)后端点设置。长语音模式中用于检测子句是否结束，若语音中断时间超出参数范围则认为子句结束，若需要结束长语音识别需要主动结束。短语音模式中用于检测语音结束，若语音中断时间超出参数范围则认为识别结束。参数范围是[500,10000]。  可选，不传参时，短语音默认为800ms支持配置，长语音默认为500ms不支持配置。  - <'maxAudioDuration', number>最大支持音频时长，不传参时默认20000ms。  短语音模式支持范围[20000-60000]，单位ms。  长语音模式支持范围[20000 - 8 \* 60 \* 60 \* 1000]，单位ms。  - <'recognizerOption', <'enablePartialResult', boolean>>  蹦字模式。  可选，不传参时默认为开启。  开启蹦字模式：  "recognizerOption": recognizerOption = {  "enablePartialResult": true  }  关闭蹦字模式：  "recognizerOption": recognizerOption = {  "enablePartialResult": false  }  - <'sessionGeneralLexicon': string[]>  会话热词。支持配置热词提高识别率。会话热词优先级比系统热词更高，会话结束时释放。  可选，不设置时默认为空。热词总数不超过200，每个热词长度范围为[2, 20]。 |

示例：

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';

3. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
4. interface RecognizerOption {
5. enablePartialResult: boolean
6. }
7. let recognizerOption: RecognizerOption = {"enablePartialResult": false};
8. let extraParam: Record<string, Object> = {
9. "recognitionMode": 0,
10. "vadBegin": 2000,
11. "vadEnd": 3000,
12. "maxAudioDuration": 20000,
13. "srcType": 1,
14. "recognizerOption": recognizerOption
15. }
16. // 设置开始识别相关参数
17. let recognizerParams: speechRecognizer.StartParams = {
18. sessionId: '123456',
19. audioInfo: { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 },
20. extraParams: extraParam
21. }

23. @Entry
24. @Component
25. struct Page {
26. build() {
27. Button()
28. .id('Button')
29. .onClick( () => {
30. // 调用开始识别方法
31. asrEngine?.startListening(recognizerParams);
32. })
33. }
34. }
```

## AudioInfo

PhonePC/2in1Tablet

音频配置信息。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioType | string | 否 | 否 | 音频类型。  当前仅支持“pcm”。 |
| sampleRate | number | 否 | 否 | 音频的采样率。  当前仅支持16000采样率。 |
| sampleBit | number | 否 | 否 | 音频返回的采样位数。  当前仅支持16位。 |
| soundChannel | number | 否 | 否 | 音频返回的通道数信息。  当前仅支持通道1。 |
| extraParams | Record<string, Object> | 否 | 是 | - <'compressRate', number> 音频的压缩率。  可选，pcm格式音频默认为0。预留参数，当前无实际使用。 |

## SpeechRecognitionResult

PhonePC/2in1Tablet

音频识别结果信息。

**系统能力：** SystemCapability.AI.SpeechRecognizer

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isFinal | boolean | 否 | 否 | 是否为本条子句最终结果的判断。  - true：是本条子句的最终结果。  - false：是本条子句的中间结果。 |
| isLast | boolean | 否 | 否 | 是否为最后一条句子的判断。  - true：是最后一条句子。  - false：不是最后一条句子。 |
| result | string | 否 | 否 | 最优识别结果。 |
