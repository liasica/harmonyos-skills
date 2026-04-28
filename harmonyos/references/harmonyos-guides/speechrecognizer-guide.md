---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speechrecognizer-guide
title: 语音识别
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > 语音识别
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:efec1ab66ab0e83d2ebe9146b74041d2b48d16e557156f062e10fc5908a9ac44
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

   ```
   1. import { speechRecognizer } from '@kit.CoreSpeechKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[createEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognizercreateengine)方法，对引擎进行初始化，并创建[SpeechRecognitionEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognitionengine)实例。

   createEngine方法提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-speechrecognizer.md)。

   ```
   1. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
   2. // 设置独立的sessionId
   3. let sessionId: string = '123456';
   4. // 创建引擎，通过callback形式返回
   5. // 设置创建引擎参数
   6. let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
   7. let initParamsInfo: speechRecognizer.CreateEngineParams = {
   8. language: 'zh-CN',
   9. online: 1,
   10. extraParams: extraParam
   11. };
   12. // 调用createEngine方法
   13. speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
   14. if (!err) {
   15. console.info('Succeeded in creating engine.');
   16. // 接收创建引擎的实例
   17. asrEngine = speechRecognitionEngine;
   18. } else {
   19. console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
   20. }
   21. });
   ```
3. 得到[SpeechRecognitionEngine](../harmonyos-references/hms-ai-speechrecognizer.md#speechrecognitionengine)实例对象后，实例化[RecognitionListener](../harmonyos-references/hms-ai-speechrecognizer.md#recognitionlistener)对象，调用[setListener](../harmonyos-references/hms-ai-speechrecognizer.md#setlistener)方法设置回调，用来接收语音识别相关的回调信息。

   ```
   1. // 创建回调对象
   2. let setListener: speechRecognizer.RecognitionListener = {
   3. // 开始识别成功回调
   4. onStart(sessionId: string, eventMessage: string) {
   5. console.info(`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
   6. },
   7. // 事件回调
   8. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
   9. console.info(`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
   10. },
   11. // 识别结果回调，包括中间结果和最终结果
   12. onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
   13. console.info(`onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}`);
   14. },
   15. // 识别完成回调
   16. onComplete(sessionId: string, eventMessage: string) {
   17. console.info(`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
   18. },
   19. // 错误回调，错误码通过本方法返回
   20. onError(sessionId: string, errorCode: number, errorMessage: string) {
   21. console.error(`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
   22. },
   23. }
   24. // 设置回调
   25. asrEngine?.setListener(setListener);
   ```
4. 分别为音频文件转文字和麦克风转文字功能设置开始识别的相关参数，调用[startListening](../harmonyos-references/hms-ai-speechrecognizer.md#startlistening)方法，开始识别。

   ```
   1. private startListeningForRecording() {
   2. let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }// audioInfo参数配置请参考AudioInfo
   3. let extraParam: Record<string, Object> = {
   4. "recognitionMode": 0,
   5. "vadBegin": 2000,
   6. "vadEnd": 3000,
   7. "maxAudioDuration": 20000
   8. }
   9. let recognizerParams: speechRecognizer.StartParams = {
   10. sessionId: this.sessionId,
   11. audioInfo: audioParam,
   12. extraParams: extraParam
   13. }
   14. console.info('startListening start');
   15. asrEngine?.startListening(recognizerParams);
   16. }
   ```
5. 传入音频流，调用[writeAudio](../harmonyos-references/hms-ai-speechrecognizer.md#writeaudio)方法，开始写入音频流。读取音频文件时，开发者需预先准备一个pcm格式音频文件。

   ```
   1. let uint8Array: Uint8Array = new Uint8Array();
   2. // 可以通过如下方式获取音频流：1、通过录音获取音频流；2、从音频文件中读取音频流
   3. // 写入音频流，音频流长度仅支持640或1280
   4. asrEngine?.writeAudio(sessionId, uint8Array);
   ```

   说明

   1. 如需通过录音获取音频流，请打开麦克风权限，参考步骤10配置相关权限。
   2. 如需从音频文件中读取音频流，请在项目中的main\resources\resfile路径下存放pcm文件。
6. （可选）当需要查询语音识别服务支持的语种信息，可调用[listLanguages](../harmonyos-references/hms-ai-speechrecognizer.md#listlanguages)方法。

   listLanguages方法提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-speechrecognizer.md)。

   ```
   1. // 设置查询相关的参数
   2. let languageQuery: speechRecognizer.LanguageQuery = {
   3. sessionId: sessionId
   4. };
   5. // 调用listLanguages方法
   6. asrEngine?.listLanguages(languageQuery).then((res: Array<string>) => {
   7. console.info(`Succeeded in listing languages.`);
   8. }).catch((err: BusinessError) => {
   9. console.error(`Failed to list languages. Code: ${err.code}, message: ${err.message}.`);
   10. });
   ```
7. （可选）当需要结束识别时，可调用[finish](../harmonyos-references/hms-ai-speechrecognizer.md#finish)方法。

   ```
   1. // 结束识别
   2. asrEngine?.finish(sessionId);
   ```
8. （可选）当需要取消识别时，可调用[cancel](../harmonyos-references/hms-ai-speechrecognizer.md#cancel)方法。

   ```
   1. // 取消识别
   2. asrEngine?.cancel(sessionId);
   ```
9. （可选）当需要释放语音识别引擎资源时，可调用[shutdown](../harmonyos-references/hms-ai-speechrecognizer.md#shutdown)方法。

   ```
   1. // 释放识别引擎资源
   2. asrEngine?.shutdown();
   ```
10. 需要在[module.json5配置文件](module-configuration-file.md)中添加ohos.permission.MICROPHONE权限，确保麦克风使用正常。详细步骤可查看[声明权限](declare-permissions.md)章节。

```
1. // ...
2. "requestPermissions": [
3. {
4. "name" : "ohos.permission.MICROPHONE",
5. "reason": "$string:reason",
6. "usedScene": {
7. "abilities": [
8. "EntryAbility"
9. ],
10. "when":"inuse"
11. }
12. }
13. ],
14. // ...
```

## 开发实例

点击按钮，将一段音频信息转换为文本。

### Index.ets

```
1. import { speechRecognizer } from '@kit.CoreSpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { PromptAction } from '@kit.ArkUI';
5. import FileCapturer from './FileCapturer';

7. const TAG = 'AsrDemo';

9. let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

11. @Entry
12. @Component
13. struct Index {
14. @State createCount: number = 0;
15. @State result: boolean = false;
16. @State voiceInfo: string = "";
17. // 设置独立的sessionId
18. @State sessionId: string = "123456";
19. @State sessionId2: string = "1234567";
20. @State generatedText: string = "Default Text";
21. @State uiContext: UIContext = this.getUIContext()
22. @State promptAction: PromptAction = this.uiContext.getPromptAction();

24. private mFileCapturer: FileCapturer = new FileCapturer();

26. build() {
27. Column() {
28. Scroll() {
29. Column() {
30. Row() {
31. Column() {
32. Text(this.generatedText)
33. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
34. }
35. .width('100%')
36. .constraintSize({ minHeight: 100 })
37. .border({ width: 1, radius: 5 })
38. .backgroundColor('#d3d3d3')
39. .padding(20)
40. .alignItems(HorizontalAlign.Start)
41. }
42. .width('100%')
43. .padding({ left: 20, right: 20, top: 20, bottom: 20 })

45. Button() {
46. Text("CreateEngineByCallback")
47. .fontColor(Color.White)
48. .fontSize(20)
49. }
50. .type(ButtonType.Capsule)
51. .backgroundColor("#0x317AE7")
52. .width("80%")
53. .height(50)
54. .margin(10)
55. .onClick(() => {
56. this.createByCallback();
57. this.createCount++;
58. console.info(TAG, `CreateAsrEngine: createCount:${this.createCount}`);

60. this.sleep(500).then(() => {
61. this.setListener();
62. try {
63. this.promptAction.showToast({
64. message: 'CreateEngine succeeded!',
65. duration: 2000
66. });
67. }catch (error) {
68. let message = (error as BusinessError).message;
69. let code = (error as BusinessError).code;
70. console.error(`showToast args error code is ${code}, message is ${message}`);
71. };
72. }).catch((err: BusinessError) => {
73. console.error(TAG, `Error in create engine: ${err}`);
74. try {
75. this.promptAction.showToast({
76. message: 'CreateEngine failed!',
77. duration: 2000
78. });
79. }catch (error) {
80. let message = (error as BusinessError).message;
81. let code = (error as BusinessError).code;
82. console.error(`showToast args error code is ${code}, message is ${message}`);
83. };
84. });
85. })

87. Button() {
88. Text("startRecording")
89. .fontColor(Color.White)
90. .fontSize(20)
91. }
92. .type(ButtonType.Capsule)
93. .backgroundColor("#0x317AE7")
94. .width("80%")
95. .height(50)
96. .margin(10)
97. .onClick(() => {
98. this.startRecording();
99. try {
100. this.promptAction.showToast({
101. message: 'start Recording',
102. duration: 2000
103. });
104. }catch (error) {
105. let message = (error as BusinessError).message;
106. let code = (error as BusinessError).code;
107. console.error(`showToast args error code is ${code}, message is ${message}`);
108. };
109. })

111. Button() {
112. Text("audioToText")
113. .fontColor(Color.White)
114. .fontSize(20)
115. }
116. .type(ButtonType.Capsule)
117. .backgroundColor("#0x317AE7")
118. .width("80%")
119. .height(50)
120. .margin(10)
121. .onClick(() => {
122. void this.audioToText();
123. try {
124. this.promptAction.showToast({
125. message: 'start audioToText',
126. duration: 2000
127. });
128. }catch (error) {
129. let message = (error as BusinessError).message;
130. let code = (error as BusinessError).code;
131. console.error(`showToast args error code is ${code}, message is ${message}`);
132. };
133. })

135. Button() {
136. Text("queryLanguagesCallback")
137. .fontColor(Color.White)
138. .fontSize(20)
139. }
140. .type(ButtonType.Capsule)
141. .backgroundColor("#0x317AE7")
142. .width("80%")
143. .height(50)
144. .margin(10)
145. .onClick(() => {
146. try{
147. this.queryLanguagesCallback();
148. try {
149. this.promptAction.showToast({
150. message: 'queryLanguages succeeded!',
151. duration: 2000
152. });
153. }catch (error) {
154. let message = (error as BusinessError).message;
155. let code = (error as BusinessError).code;
156. console.error(`showToast args error code is ${code}, message is ${message}`);
157. };
158. } catch (err) {
159. this.generatedText = `Failed to query language information. message: ${err.message}.`
160. try {
161. this.promptAction.showToast({
162. message: 'queryLanguages failed!',
163. duration: 2000
164. });
165. }catch (error) {
166. let message = (error as BusinessError).message;
167. let code = (error as BusinessError).code;
168. console.error(`showToast args error code is ${code}, message is ${message}`);
169. };
170. }
171. })

173. Button() {
174. Text("shutdown")
175. .fontColor(Color.White)
176. .fontSize(20)
177. }
178. .type(ButtonType.Capsule)
179. .backgroundColor("#0x317AA7")
180. .width("80%")
181. .height(50)
182. .margin(10)
183. .onClick(() => {
184. // 释放引擎
185. try{
186. asrEngine?.shutdown();
187. this.generatedText = `The engine has been released.`
188. try {
189. this.promptAction.showToast({
190. message: 'shutdown succeeded!',
191. duration: 2000
192. });
193. }catch (error) {
194. let message = (error as BusinessError).message;
195. let code = (error as BusinessError).code;
196. console.error(`showToast args error code is ${code}, message is ${message}`);
197. };
198. } catch (err) {
199. this.generatedText = `Failed to release engine. message: ${err.message}.`
200. try {
201. this.promptAction.showToast({
202. message: 'shutdown failed!',
203. duration: 2000
204. });
205. }catch (error) {
206. let message = (error as BusinessError).message;
207. let code = (error as BusinessError).code;
208. console.error(`showToast args error code is ${code}, message is ${message}`);
209. };
210. }
211. })
212. }
213. .layoutWeight(1)
214. }
215. .width('100%')
216. .height('100%')

218. }
219. }

222. // 创建引擎，通过callback形式返回
223. private createByCallback() {
224. // 设置创建引擎参数
225. let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
226. let initParamsInfo: speechRecognizer.CreateEngineParams = {
227. language: 'zh-CN',
228. online: 1,
229. extraParams: extraParam
230. };

232. // 调用createEngine方法
233. speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine:
234. speechRecognizer.SpeechRecognitionEngine) => {
235. if (!err) {
236. console.info(TAG, 'succeeded in creating engine.');
237. // 接收创建引擎的实例
238. asrEngine = speechRecognitionEngine;
239. } else {
240. // 无法创建引擎时返回错误码1002200001，原因：语种不支持、模式不支持、初始化超时、资源不存在等导致创建引擎失败
241. // 无法创建引擎时返回错误码1002200006，原因：引擎正在忙碌中，一般多个应用同时调用语音识别引擎时触发
242. // 无法创建引擎时返回错误码1002200008，原因：引擎已被销毁
243. console.error(TAG, `Failed to create engine. Message: ${err.message}.`);
244. }
245. });
246. }

248. // 查询语种信息，以callback形式返回
249. private queryLanguagesCallback() {
250. // 设置查询相关参数
251. let languageQuery: speechRecognizer.LanguageQuery = {
252. sessionId: this.sessionId
253. };
254. // 调用listLanguages方法
255. asrEngine?.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
256. if (!err) {
257. // 接收目前支持的语种信息
258. console.info(TAG, `succeeded in listing languages, result: ${JSON.stringify(languages)}`);
259. this.generatedText = `languages result: ${JSON.stringify(languages)}`
260. } else {
261. console.error(TAG, `Failed to create engine. Message: ${err.message}.`);
262. this.generatedText = `Failed to create engine. Message: ${err.message}.`
263. }
264. });
265. }

267. private startListeningForRecording() {
268. let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 } // audioInfo参数配置请参考AudioInfo
269. let extraParam: Record<string, Object> = {
270. "recognitionMode": 0,
271. "vadBegin": 2000,
272. "vadEnd": 3000,
273. "maxAudioDuration": 20000
274. }
275. let recognizerParams: speechRecognizer.StartParams = {
276. sessionId: this.sessionId,
277. audioInfo: audioParam,
278. extraParams: extraParam
279. }
280. console.info(TAG, 'startListening start');
281. try {
282. asrEngine?.startListening(recognizerParams);
283. } catch (err) {
284. console.error(`error code: ${err.code}, message: ${err.message}.`)
285. }
286. }

288. // 写音频流
289. private async audioToText() {
290. try {
291. this.setListener();
292. // Set the parameters related to the start of identification.
293. let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }
294. let recognizerParams: speechRecognizer.StartParams = {
295. sessionId: this.sessionId2,
296. audioInfo: audioParam
297. }
298. // Invoke the start recognition method.
299. asrEngine?.startListening(recognizerParams);

301. // Get Audio from File
302. let data: ArrayBuffer | undefined = undefined;
303. let ctx = this.getUIContext().getHostContext() as Context;
304. let filenames: string[] = fileIo.listFileSync(ctx.resourceDir);
305. if (filenames.length <= 0) {
306. console.error('length is null');
307. return;
308. }
309. let filePath: string = ctx.resourceDir + '/' + filenames[0];
310. (this.mFileCapturer as FileCapturer).setFilePath(filePath);
311. this.mFileCapturer.init((dataBuffer: ArrayBuffer) => {
312. data = dataBuffer
313. let uint8Array: Uint8Array = new Uint8Array(data);
314. asrEngine?.writeAudio(this.sessionId2, uint8Array);
315. });
316. await this.mFileCapturer.start();
317. asrEngine?.finish(this.sessionId);
318. this.mFileCapturer.release();
319. } catch (err) {
320. this.generatedText = `Message: ${err.message}.`
321. }
322. }

324. // 麦克风语音转文本
325. private startRecording() {
326. try {
327. this.startListeningForRecording();
328. } catch (err) {
329. this.generatedText = `Message: ${err.message}.`;
330. }
331. }

333. // 睡眠
334. private async sleep(ms: number): Promise<void> {
335. return new Promise(resolve => setTimeout(resolve, ms));
336. }

338. // 设置回调
339. private setListener() {
340. // 创建回调对象
341. let setListener: speechRecognizer.RecognitionListener = {
342. // 开始识别成功回调
343. onStart: (sessionId: string, eventMessage: string) => {
344. this.generatedText = '';
345. console.info(TAG, `onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
346. },
347. // 事件回调
348. onEvent(sessionId: string, eventCode: number, eventMessage: string) {
349. console.info(TAG, `onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}`);
350. },
351. // 识别结果回调，包括中间结果和最终结果
352. onResult: (sessionId: string, result: speechRecognizer.SpeechRecognitionResult) => {
353. console.info(TAG, `onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}`);
354. this.generatedText = result.result;
355. },
356. // 识别完成回调
357. onComplete(sessionId: string, eventMessage: string) {
358. console.info(TAG, `onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}`);
359. },
360. // 错误回调，错误码通过本方法返回
361. onError(sessionId: string, errorCode: number, errorMessage: string) {
362. console.error(TAG, `onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
363. },
364. }
365. // 设置回调
366. asrEngine?.setListener(setListener);
367. }
368. }
```

### FileCapturer.ets

添加FileCapturer.ets文件用于pcm文件音频流。

```
1. import { fileIo } from '@kit.CoreFileKit';

3. const TAG = 'FileCapturer';
4. const SEND_SIZE: number = 1280;

6. /**
7. * File collector tool
8. */
9. export default class FileCapturer {
10. /**
11. * Whether the audio is being written
12. */
13. private mIsWriting: boolean = false;

15. /**
16. * File Path
17. */
18. private mFilePath: string = '';

20. /**
21. * Open File Object
22. */
23. private mFile: fileIo.File | null = null;

25. /**
26. * Indicates whether the file can be read.
27. */
28. private mIsReadFile: boolean = true;

30. /**
31. * Audio Data Callback Method
32. */
33. private mDataCallBack: ((data: ArrayBuffer) => void ) | null = null;

35. /**
36. * Setting the File Path
37. * @param filePath
38. */
39. public setFilePath(filePath: string) {
40. this.mFilePath = filePath;
41. }

43. init(dataCallBack: (data: ArrayBuffer) => void) {
44. if (null != this.mDataCallBack) {
45. return;
46. }
47. this.mDataCallBack = dataCallBack;
48. try {
49. if (!fileIo.accessSync(this.mFilePath)) {
50. return
51. }
52. } catch (err) {
53. console.error(`error code: ${err.code}, message: ${err.message}.`)
54. }
55. console.error(TAG, "init start ");
56. }

58. async start(): Promise<void> {
59. try {
60. if (this.mIsWriting || null == this.mDataCallBack) {
61. return;
62. }
63. this.mIsWriting = true;
64. this.mIsReadFile = true;
65. this.mFile = fileIo.openSync(this.mFilePath, fileIo.OpenMode.READ_ONLY);
66. let buf: ArrayBuffer = new ArrayBuffer(SEND_SIZE);
67. let offset: number = 0;
68. while (SEND_SIZE == fileIo.readSync(this.mFile.fd, buf, {
69. offset: offset
70. }) && this.mIsReadFile) {
71. this.mDataCallBack(buf);
72. await sleep(40);
73. offset = offset + SEND_SIZE;
74. }
75. } catch (e) {
76. console.error(TAG, "read file error " + e);
77. } finally {
78. if (null != this.mFile) {
79. try {
80. fileIo.closeSync(this.mFile);
81. } catch (err) {
82. console.error(`error code: ${err.code}, message: ${err.message}.`)
83. }
84. }
85. this.mIsWriting = false;
86. }
87. }

89. stop() {
90. if (null == this.mDataCallBack) {
91. return;
92. }
93. try {
94. this.mIsReadFile = false;
95. } catch (e) {
96. console.error(TAG, "read file error " + e);
97. }
98. }

100. release() {
101. if (null == this.mDataCallBack) {
102. return;
103. }
104. try {
105. this.mDataCallBack = null;
106. this.mIsReadFile = false;
107. } catch (e) {
108. console.error(TAG, "read file error " + e);
109. }
110. }
111. }

113. async function sleep(ms: number): Promise<void> {
114. return new Promise<void>(resolve => setTimeout(resolve, ms));
115. }
```

### EntryAbility.ets

在EntryAbility.ets文件中添加麦克风权限。

```
1. import { abilityAccessCtrl, UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(): void {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. }

11. onDestroy(): void {
12. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
13. }

15. onWindowStageCreate(windowStage: window.WindowStage): void {
16. // Main window is created, set main page for this ability
17. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

19. let atManager = abilityAccessCtrl.createAtManager();
20. atManager.requestPermissionsFromUser(this.context, ['ohos.permission.MICROPHONE']).then((data) => {
21. hilog.info(0x0000, 'testTag', 'data:' + JSON.stringify(data));
22. hilog.info(0x0000, 'testTag', 'data permissions:' + data.permissions);
23. hilog.info(0x0000, 'testTag', 'data authResults:' + data.authResults);
24. }).catch((err: BusinessError) => {
25. hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
26. });

28. windowStage.loadContent('pages/Index', (err, data) => {
29. if (err.code) {
30. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
31. return;
32. }
33. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
34. });
35. }

37. onWindowStageDestroy(): void {
38. // Main window is destroyed, release UI related resources
39. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
40. }

42. onForeground(): void {
43. // Ability has brought to foreground
44. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
45. }

47. onBackground(): void {
48. // Ability has back to background
49. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
50. }
51. }
```
