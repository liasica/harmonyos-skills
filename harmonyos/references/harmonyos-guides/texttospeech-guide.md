---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/texttospeech-guide
title: 文本转语音
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > 文本转语音
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:18a69a74cb6846c49eb21b48c2651966f0649f79524d18a0a2841857c058f4a3
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

   ```
   1. import { textToSpeech } from '@kit.CoreSpeechKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用createEngine接口，创建[TextToSpeechEngine](../harmonyos-references/hms-ai-texttospeech.md#texttospeechengine)实例。

   createEngine接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-texttospeech.md)。

   ```
   1. let ttsEngine: textToSpeech.TextToSpeechEngine;

   3. // 设置创建引擎参数
   4. let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
   5. let initParamsInfo: textToSpeech.CreateEngineParams = {
   6. language: 'zh-CN',
   7. person: 0,
   8. online: 1,
   9. extraParams: extraParam
   10. };

   12. // 调用createEngine方法
   13. textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
   14. if (!err) {
   15. console.info('Succeeded in creating engine');
   16. // 接收创建引擎的实例
   17. ttsEngine = textToSpeechEngine;
   18. } else {
   19. console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
   20. }
   21. });
   ```
3. 得到[TextToSpeechEngine](../harmonyos-references/hms-ai-texttospeech.md#texttospeechengine)实例对象后，实例化[SpeakParams](../harmonyos-references/hms-ai-texttospeech.md#speakparams)对象、[SpeakListener](../harmonyos-references/hms-ai-texttospeech.md#speaklistener)对象，并传入待合成及播报的文本originalText，调用[speak](../harmonyos-references/hms-ai-texttospeech.md#speak)接口进行播报。

   ```
   1. // 设置speak的回调信息
   2. let speakListener: textToSpeech.SpeakListener = {
   3. // 开始播报回调
   4. onStart(requestId: string, response: textToSpeech.StartResponse) {
   5. console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   6. },
   7. // 合成完成及播报完成回调
   8. onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
   9. console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   10. },
   11. // 停止播报回调
   12. onStop(requestId: string, response: textToSpeech.StopResponse) {
   13. console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   14. },
   15. // 返回音频流
   16. onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
   17. console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
   18. },
   19. // 错误回调
   20. onError(requestId: string, errorCode: number, errorMessage: string) {
   21. console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
   22. }
   23. };
   24. // 设置回调
   25. ttsEngine.setListener(speakListener);
   26. // 设置播报内容
   27. let originalText: string = 'Hello HarmonyOS';
   28. // 设置播报相关参数
   29. let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN',
   30. "audioType": "pcm", "soundChannel": 3, "playType": 1 };
   31. let speakParams: textToSpeech.SpeakParams = {
   32. requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
   33. extraParams: extraParam
   34. };
   35. // 调用播报方法
   36. // 开发者可以通过修改speakParams主动设置播报策略
   37. try {
   38. ttsEngine.speak(originalText, speakParams);
   39. } catch (err) {
   40. console.error(`error code: ${err.code}, message: ${err.message}.`)
   41. }
   ```
4. （可选）当需要停止合成及播报时，可调用[stop](../harmonyos-references/hms-ai-texttospeech.md#stop)接口。

   ```
   1. ttsEngine.stop();
   ```
5. （可选）当需要查询文本转语音服务是否处于忙碌状态时，可调用[isBusy](../harmonyos-references/hms-ai-texttospeech.md#isbusy)接口。

   ```
   1. ttsEngine.isBusy();
   ```
6. （可选）当需要查询支持的语种音色信息时，可调用[listVoices](../harmonyos-references/hms-ai-texttospeech.md#listvoices)接口。

   listVoices接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/hms-ai-texttospeech.md)。

   ```
   1. // 在组件中声明并初始化字符串voiceInfo
   2. @State voiceInfo: string = "";

   4. // 设置查询相关参数
   5. let voicesQuery: textToSpeech.VoiceQuery = {
   6. requestId: '12345678', // requestId在同一实例内仅能用一次，请勿重复设置
   7. online: 1
   8. };
   9. // 调用listVoices方法，以callback返回
   10. ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
   11. if (!err) {
   12. // 接收目前支持的语种音色等信息
   13. this.voiceInfo = JSON.stringify(voiceInfo);
   14. console.info(`Succeeded in listing voices, voiceInfo is ${this.voiceInfo}`);
   15. } else {
   16. console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}`);
   17. }
   18. });
   ```

## 设置播报策略

由于不同场景下，模型自动判断所选择的播报策略可能与实际需求不同，此章节提供对于播报策略进行主动设置的方法。

说明

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

```
1. "hello[h1] world"
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

```
1. "[n2]123[n1]456[n0]"
```

其中，123将会按照数值播报，456则会按照号码播报，而后的文本中的数字，均会自动判断。

### 插入静音停顿

格式：[pN]

描述：N为无符号整数，单位为ms。

文本示例：

```
1. "你好[p500]小艺"
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

```
1. "着[=zhuo2]手"
```

“着”字将读作“zhuó”。

## 开发实例

点击按钮，播报一段文本。

### Index.ets

```
1. import { textToSpeech } from '@kit.CoreSpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { PromptAction } from '@kit.ArkUI';
4. import { UIContext } from '@kit.ArkUI';
5. import { TreeMap } from '@kit.ArkTS';
6. import { fileIo } from '@kit.CoreFileKit';
7. import PcmPlayer from './PcmPlayer';
8. import { audio } from '@kit.AudioKit';
9. import { Context } from '@kit.AbilityKit';

11. const TAG: string = 'TtsDemo';
12. let ttsEngine: textToSpeech.TextToSpeechEngine;
13. let bufferLength: number = 0;
14. let engineCreated: boolean = false;

16. // 定义一个函数来拼接ArrayBuffer
17. function concatenateArrayBuffers(buffers: ArrayBuffer[]): ArrayBuffer {
18. const totalLength = buffers.reduce((sum, buffer) => sum + buffer.byteLength, 0);
19. const concatenatedBuffer = new ArrayBuffer(totalLength);
20. let offset = 0;
21. for (const buffer of buffers) {
22. const uint8Array = new Uint8Array(buffer);
23. new Uint8Array(concatenatedBuffer, offset, uint8Array.length).set(uint8Array);
24. offset += uint8Array.length;
25. }
26. return concatenatedBuffer;
27. }

29. @Entry
30. @Component
31. struct Index {
32. @State createCount: number = 0;
33. // 设置播报内容
34. @State originalText: string = "\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t" + "纸上得来终觉浅，绝知此事要躬行。\n\t\t";
35. @State uiContext: UIContext = this.getUIContext()
36. @State promptAction: PromptAction = this.uiContext.getPromptAction();
37. private pcmData: TreeMap<number, Uint8Array> = new TreeMap();
38. private pcmPlayer: PcmPlayer = new PcmPlayer();

40. build() {
41. Column() {
42. Scroll() {
43. Column() {
44. TextArea({ placeholder: 'Please enter tts original text', text: `${this.originalText}` })
45. .margin(20)
46. .focusable(false)
47. .border({ width: 5, color: 0x317AE7, radius: 10, style: BorderStyle.Dotted })
48. .onChange((value: string) => {
49. this.originalText = value;
50. console.info(TAG, "original text: " + this.originalText);
51. })

53. Button() {
54. Text("CreateEngine")
55. .fontColor(Color.White)
56. .fontSize(20)
57. }
58. .type(ButtonType.Capsule)
59. .backgroundColor("#0x317AE7")
60. .width("80%")
61. .height(50)
62. .margin(10)
63. .onClick(() => {
64. engineCreated = true
65. this.createCount++;
66. console.info(`createByCallback: createCount:${this.createCount}`);
67. this.createByCallback();
68. try {
69. this.promptAction.showToast({
70. message: 'CreateEngine success!',
71. duration: 2000
72. });
73. }catch (error) {
74. let message = (error as BusinessError).message;
75. let code = (error as BusinessError).code;
76. console.error(`showToast args error code is ${code}, message is ${message}`);
77. };
78. })

80. Button() {
81. Text("speak")
82. .fontColor(Color.White)
83. .fontSize(20)
84. }
85. .type(ButtonType.Capsule)
86. .backgroundColor("#0x317AE7")
87. .width("80%")
88. .height(50)
89. .margin(10)
90. .onClick(() => {
91. if (engineCreated) {
92. try {
93. this.speak();
94. try {
95. this.promptAction.showToast({
96. message: 'start speaking',
97. duration: 2000
98. });
99. }catch (error) {
100. let message = (error as BusinessError).message;
101. let code = (error as BusinessError).code;
102. console.error(`showToast args error code is ${code}, message is ${message}`);
103. };
104. } catch (err)  {
105. try {
106. this.promptAction.showToast({
107. message: 'start speaking failed',
108. duration: 2000
109. });
110. }catch (error) {
111. let message = (error as BusinessError).message;
112. let code = (error as BusinessError).code;
113. console.error(`showToast args error code is ${code}, message is ${message}`);
114. };
115. }
116. } else {
117. try {
118. this.promptAction.showToast({
119. message: 'The engine has not been created',
120. duration: 2000
121. });
122. }catch (error) {
123. let message = (error as BusinessError).message;
124. let code = (error as BusinessError).code;
125. console.error(`showToast args error code is ${code}, message is ${message}`);
126. };
127. }
128. })

130. Button() {
131. Text("speakOnData")
132. .fontColor(Color.White)
133. .fontSize(20)
134. }
135. .type(ButtonType.Capsule)
136. .backgroundColor("#0x317AE7")
137. .width("80%")
138. .height(50)
139. .margin(10)
140. .onClick(() => {
141. if (engineCreated) {
142. try {
143. void this.speakOnData();
144. try {
145. this.promptAction.showToast({
146. message: 'start speakOnData',
147. duration: 2000
148. });
149. }catch (error) {
150. let message = (error as BusinessError).message;
151. let code = (error as BusinessError).code;
152. console.error(`showToast args error code is ${code}, message is ${message}`);
153. };
154. } catch (err) {
155. try {
156. this.promptAction.showToast({
157. message: 'start speakOnData failed',
158. duration: 2000
159. });
160. }catch (error) {
161. let message = (error as BusinessError).message;
162. let code = (error as BusinessError).code;
163. console.error(`showToast args error code is ${code}, message is ${message}`);
164. };
165. }
166. } else {
167. try {
168. this.promptAction.showToast({
169. message: 'The engine has not been created',
170. duration: 2000
171. });
172. }catch (error) {
173. let message = (error as BusinessError).message;
174. let code = (error as BusinessError).code;
175. console.error(`showToast args error code is ${code}, message is ${message}`);
176. };
177. }
178. })

180. Button() {
181. Text("stop")
182. .fontColor(Color.White)
183. .fontSize(20)
184. }
185. .type(ButtonType.Capsule)
186. .backgroundColor("#0x317AE7")
187. .width("80%")
188. .height(50)
189. .margin(10)
190. .onClick(() => {
191. try {
192. let isBusy: boolean = ttsEngine.isBusy();
193. let isPlaying: boolean = this.pcmPlayer.isPlaying();
194. if (isBusy) {
195. ttsEngine.stop();
196. }
197. if (isPlaying) {
198. this.pcmPlayer.stop()
199. }
200. try {
201. this.promptAction.showToast({
202. message: 'stop!',
203. duration: 2000
204. });
205. }catch (error) {
206. let message = (error as BusinessError).message;
207. let code = (error as BusinessError).code;
208. console.error(`showToast args error code is ${code}, message is ${message}`);
209. };
210. } catch (err) {
211. try {
212. this.promptAction.showToast({
213. message: 'stop failed',
214. duration: 2000
215. });
216. }catch (error) {
217. let message = (error as BusinessError).message;
218. let code = (error as BusinessError).code;
219. console.error(`showToast args error code is ${code}, message is ${message}`);
220. };
221. }
222. })

224. Button() {
225. Text("isBusy")
226. .fontColor(Color.White)
227. .fontSize(20)
228. }
229. .type(ButtonType.Capsule)
230. .backgroundColor("#0x317AE7")
231. .width("80%")
232. .height(50)
233. .margin(10)
234. .onClick(() => {
235. try {
236. let isBusy: boolean = ttsEngine.isBusy();
237. let isPlaying: boolean = this.pcmPlayer.isPlaying();
238. console.info('isBusy :' + isBusy);
239. console.info('isPlaying :' + isPlaying);
240. try {
241. this.promptAction.showToast({
242. message: 'speak isBusy :' + isBusy + '\nspeakOnData isBusy :' + isPlaying,
243. duration: 2000
244. });
245. }catch (error) {
246. let message = (error as BusinessError).message;
247. let code = (error as BusinessError).code;
248. console.error(`showToast args error code is ${code}, message is ${message}`);
249. };
250. } catch (err) {
251. try {
252. this.promptAction.showToast({
253. message: 'isBusy failed',
254. duration: 2000
255. });
256. }catch (error) {
257. let message = (error as BusinessError).message;
258. let code = (error as BusinessError).code;
259. console.error(`showToast args error code is ${code}, message is ${message}`);
260. };
261. }
262. })

264. Button() {
265. Text("shutdown")
266. .fontColor(Color.White)
267. .fontSize(20)
268. }
269. .type(ButtonType.Capsule)
270. .backgroundColor("#0x317AA7")
271. .width("80%")
272. .height(50)
273. .margin(10)
274. .onClick(() => {
275. try {
276. this.pcmPlayer.release()
277. ttsEngine.shutdown();
278. engineCreated = false
279. try {
280. this.promptAction.showToast({
281. message: 'shutdown success!',
282. duration: 2000
283. });
284. }catch (error) {
285. let message = (error as BusinessError).message;
286. let code = (error as BusinessError).code;
287. console.error(`showToast args error code is ${code}, message is ${message}`);
288. };
289. } catch (err) {
290. try {
291. this.promptAction.showToast({
292. message: 'shutdown failed',
293. duration: 2000
294. });
295. }catch (error) {
296. let message = (error as BusinessError).message;
297. let code = (error as BusinessError).code;
298. console.error(`showToast args error code is ${code}, message is ${message}`);
299. };
300. }
301. })

303. }
304. .layoutWeight(1)
305. }
306. .width('100%')
307. .height('100%')

309. }
310. }

312. // 创建引擎，通过callback形式返回
313. // 当引擎不存在、引擎资源不存在、初始化超时，返回错误码1002300005，引擎创建失败
314. private createByCallback() {
315. // 设置创建引擎参数
316. let extraParam: Record<string, Object> = { "style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName' }
317. let initParamsInfo: textToSpeech.CreateEngineParams = {
318. language: 'zh-CN',
319. person: 0,
320. online: 1,
321. extraParams: extraParam
322. };
323. try {
324. // 调用createEngine方法
325. textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
326. if (!err) {
327. console.info('createEngine is success');
328. // 接收创建引擎的实例
329. ttsEngine = textToSpeechEngine;
330. } else {
331. console.error(`error code: ${err.code}, message: ${err.message}.`)
332. }
333. });
334. } catch (error) {
335. let message = (error as BusinessError).message;
336. let code = (error as BusinessError).code;
337. console.error(`createEngine failed, error code: ${code}, message: ${message}.`)
338. }
339. }

341. // 调用speak播报方法
342. private speak() {
343. let speakListener: textToSpeech.SpeakListener = {
344. // 开始播报回调
345. onStart(requestId: string, response: textToSpeech.StartResponse) {
346. console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
347. },
348. // 完成播报回调
349. onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
350. console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
351. },
352. // 停止播报完成回调，调用stop方法并完成时会触发此回调
353. onStop(requestId: string, response: textToSpeech.StopResponse) {
354. console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
355. },
356. // 返回音频流
357. onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
358. console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
359. },
360. // 错误回调，播报过程发生错误时触发此回调
361. onError(requestId: string, errorCode: number, errorMessage: string) {
362. if (errorCode === 1002300007) {
363. engineCreated = false
364. }
365. console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
366. }
367. };
368. // 设置回调
369. ttsEngine.setListener(speakListener);
370. // 设置播报相关参数
371. let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 3, "playType":1}
372. let speakParams: textToSpeech.SpeakParams = {
373. requestId: '123456' + Date.now(), // requestId在同一实例内仅能用一次，请勿重复设置
374. extraParams: extraParam
375. };
376. // 调用speak播报方法
377. try {
378. ttsEngine.speak(this.originalText, speakParams);
379. } catch (err) {
380. console.error(TAG, `error code: ${err.code}, message: ${err.message}.`)
381. }
382. }

384. private onStart = (utteranceId: string, response: textToSpeech.StartResponse) => {
385. bufferLength = 0;
386. // 初始化音频数据映射
387. console.info(TAG, `onStart | utteranceId: ${ utteranceId }, response: ${JSON.stringify(response)}`);
388. }

390. private onData = (utteranceId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) => {
391. // 将ArrayBuffer转换为Uint8Array
392. let uint8Array: Uint8Array = new Uint8Array(audio);
393. this.pcmData.set(response.sequence, uint8Array)
394. bufferLength += 1
395. let str = ""
396. // 或者使用循环打印每个元素
397. for (let i = 0; i < uint8Array.length; i++) {
398. str = str + (","+uint8Array[i]);
399. }
400. console.info(TAG, `onData | utteranceId: ${utteranceId}, sequence: ${JSON.stringify(response.sequence)}, length: ${uint8Array.length}, audio: ${JSON.stringify(str)}`);
401. }

403. private onComplete = (utteranceId: string, response: textToSpeech.CompleteResponse) => {
404. let buffers: ArrayBuffer[] = new Array();

406. console.info(TAG, `pcmData len: ${this.pcmData.length}`)
407. // 遍历Map，将ArrayBuffer添加到数组中
408. try {
409. this.pcmData?.forEach((value: Uint8Array) => {
410. buffers.push(value.buffer.slice(0))
411. })
412. } catch (forEachErr) {
413. console.error(TAG, 'pcmData forEach failed:', forEachErr);
414. }
415. console.info(TAG, `buffers len: ${buffers.length}`)

417. // 按照顺序拼接所有的ArrayBuffer
418. let audioData = concatenateArrayBuffers(buffers);
419. console.info(TAG, `audioData len: ${audioData.byteLength}`)

421. let context = this.uiContext.getHostContext() as Context
422. let path = context.filesDir
423. let filePath: string = `${path}/my.pcm`
424. fileIo.createStream(filePath, "w+")
425. .then(os => os.write(audioData).catch((e: BusinessError) => { throw new Error(`Write failed: ${e}`) }))
426. .then((): Promise<void> => {
427. try {
428. this.pcmPlayer.file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
429. return this.pcmPlayer.prepare(audio.AudioSamplingRate.SAMPLE_RATE_16000);
430. } catch (e) { throw new Error(`Open failed: ${e}`) }
431. })
432. .then(() => this.pcmPlayer.play(audioData))
433. .catch((err: BusinessError) => console.error(TAG, `Error: ${err}`));

435. console.info(TAG, `onComplete | utteranceId: ${utteranceId}, response: ${JSON.stringify(response)}`);
436. }

438. // 调用speakOnData播报方法
439. // 未初始化引擎时调用speak方法，返回错误码1002300007，合成及播报失败
440. private speakOnData() {
441. // 设置播报相关参数
442. let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1.2, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 1, "playType":0}
443. let speakParams: textToSpeech.SpeakParams = {
444. requestId: '1234567' + Date.now(),
445. extraParams: extraParam
446. }

448. try{
449. // 创建回调对象
450. let speakListener: textToSpeech.SpeakListener = {
451. // 开始识别成功回调
452. onStart: this.onStart,
453. // 识别完成回调
454. onComplete: this.onComplete,
455. // 停止播报回调
456. onStop(utteranceId: string, response: textToSpeech.StopResponse) {
457. console.info('speakListener onStop: ' + ' utteranceId: ' + utteranceId + ' response: ' + JSON.stringify(response));
458. },
459. // 返回音频流
460. onData: this.onData,
461. // 错误回调
462. onError(utteranceId: string, errorCode: number, errorMessage: string) {
463. if (errorCode === 1002300007) {
464. engineCreated = false
465. }
466. console.error('speakListener onError: ' + ' utteranceId: ' + utteranceId + ' errorCode: ' + errorCode + ' errorMessage: ' + errorMessage);
467. }
468. };
469. // 设置回调
470. ttsEngine.setListener(speakListener);
471. try{
472. console.info(`speakListener before speak`)
473. // 调用speak播报方法
474. for (let i = 0; i < 1; i++) {
475. ttsEngine?.speak(this.originalText, speakParams);
476. }
477. console.info(`speakListener after speak`)
478. }catch (error) {
479. let message = (error as BusinessError).message;
480. let code = (error as BusinessError).code;
481. console.error(`speakListener speak failed, error code: ${code}, message: ${message}.`)
482. }
483. }catch (error) {
484. let message = (error as BusinessError).message;
485. let code = (error as BusinessError).code;
486. console.error(`speakListener setListener failed, error code: ${code}, message: ${message}.`)
487. }
488. }
489. }
```

### PcmPlayer.ets

```
1. import { audio } from '@kit.AudioKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. const TAG = 'PCM_audio';

6. class Options {
7. offset?: number;
8. length?: number;
9. }

11. export default class PcmPlayer {

13. public file: fileIo.File | undefined;
14. private writeDataCallback = (buffer: ArrayBuffer) => {
15. let options: Options = {
16. offset: this.bufferSize,
17. length: buffer.byteLength
18. };

20. try {
21. fileIo.readSync(this.file?.fd, buffer, options);
22. this.bufferSize += buffer.byteLength;
23. if (this.audioDataSize < this.bufferSize) {
24. this.renderModel?.off('writeData');
25. void this.stop()
26. }
27. console.info(TAG, 'reading file success');
28. // 系统会判定buffer有效，正常播放。
29. return audio.AudioDataCallbackResult.VALID;
30. } catch (error) {
31. console.error(TAG, `Reading file failed, error code: ${error.code}, message: ${error.message}.`)
32. // 系统会判定buffer无效，不播放。
33. return audio.AudioDataCallbackResult.INVALID;
34. }
35. };
36. /**
37. * 缓存大小
38. */
39. private bufferSize: number = 0;
40. /**
41. * 音频总大小
42. */
43. private audioDataSize: number = 0;
44. /**
45. * 播放器
46. */
47. private renderModel: audio.AudioRenderer | null = null;
48. /**
49. * 播放状态
50. */
51. private audioStreamInfo: audio.AudioStreamInfo = {
52. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000, // 采样率
53. channels: audio.AudioChannel.CHANNEL_1, // 通道
54. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
55. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
56. }
57. private audioRendererInfo: audio.AudioRendererInfo = {
58. usage: audio.StreamUsage.STREAM_USAGE_ACCESSIBILITY, // 音频流使用类型
59. rendererFlags: 0 // 音频渲染器标志
60. }
61. private audioRendererOptions: audio.AudioRendererOptions = {
62. streamInfo: this.audioStreamInfo,
63. rendererInfo: this.audioRendererInfo
64. }

66. public async prepare(sampleRate: number) {
67. this.audioRendererOptions.streamInfo.samplingRate = sampleRate;
68. this.audioRendererOptions.rendererInfo.usage = audio.StreamUsage.STREAM_USAGE_MUSIC;
69. if (this.renderModel != null) {
70. await this.renderModel.release();
71. }
72. let renderModel = await audio.createAudioRenderer(this.audioRendererOptions);
73. if (!renderModel) {
74. console.error(TAG, `failed to create audio renderer`);
75. }
76. console.info(TAG, "creating AudioRenderer success");
77. this.renderModel = renderModel;
78. this.bufferSize = await this.renderModel.getBufferSize();
79. }

81. public async play(data: ArrayBuffer): Promise<number> {
82. this.audioDataSize = data.byteLength
83. if (this.renderModel != null) {
84. try {
85. this.renderModel.on('writeData', this.writeDataCallback);
86. } catch (err) {
87. console.error(`error code: ${err.code}, message: ${err.message}.`)
88. }
89. // 启动渲染
90. await this.renderModel.start();
91. console.info(TAG, "start AudioRenderer success");
92. }
93. return -1;
94. }

96. public async stop() {
97. console.info(TAG, 'Renderer begin stop');
98. if (this.renderModel == null) {
99. return;
100. }

102. // 只有渲染器状态为running或paused的时候才可以停止
103. if (this.renderModel.state !== audio.AudioState.STATE_RUNNING
104. && this.renderModel.state !== audio.AudioState.STATE_PAUSED) {
105. console.error(TAG, 'Renderer is not running or paused');
106. return;
107. }
108. await this.renderModel.stop(); // 停止渲染
109. console.info(TAG, 'Renderer stopped');
110. }

112. public async release() {
113. // 渲染器状态不是released状态，才能release
114. if (this.renderModel != null) {
115. if (this.renderModel.state === audio.AudioState.STATE_RELEASED) {
116. console.error(TAG, 'Renderer already released');
117. return;
118. }
119. await this.renderModel.release(); // 释放资源
120. this.renderModel = null;
121. console.info(TAG, 'Renderer released');
122. }
123. }

125. /**
126. * 判断当前渲染状态
127. *
128. * @returns running返回true，否则返回false
129. */
130. public isPlaying() {
131. if (this.renderModel != null) {
132. console.info(TAG, "player.state:" + this.renderModel.state);
133. return this.renderModel.state == audio.AudioState.STATE_RUNNING;
134. } else {
135. return false;
136. }
137. }

139. /**
140. * 获取当前渲染状态
141. *
142. * @returns running返回true，否则返回false
143. */
144. public getRenderState(): number {
145. if (this.renderModel != null) {
146. console.info(TAG, "player.state:" + this.renderModel.state);
147. return this.renderModel.state;
148. } else {
149. return audio.AudioState.STATE_INVALID;
150. }
151. }

153. /**
154. * 获取音频渲染器的最小缓冲区大小
155. */
156. public getBufferSize(): number {
157. return this.bufferSize;
158. }
159. }
```
