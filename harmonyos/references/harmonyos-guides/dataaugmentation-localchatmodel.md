---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataaugmentation-localchatmodel
title: 端侧问答模型
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > 端侧问答模型
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ff7858466848b07400f8809f90b5f507520d1a6602362b226ba558283a3d0ce
---

## 概述

当应用通过RAG接口进行知识问答时，系统会经过以下处理流程：问题分解、查询改写、知识检索和检索生成，该流程需要与大语言模型（LLM）进行多次交互。应用可选择两种部署方案：

* 使用自建的云端大模型。
* 采用Kit提供的端侧问答模型能力。

选择端侧问答模型方案具有以下优势：

* 免除云端大模型的运维成本。
* 增强用户数据安全性（数据在端侧处理）。

## 约束与限制

开发者需要申请接口调用。

## 接口说明

端侧问答模型关键接口如下表所示，具体API说明详见API参考。

| 接口名 | 描述 |
| --- | --- |
| init(): Promise<boolean> | 初始化端侧问答模型，负责拉起模型管理应用。 |
| chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void> | 与端侧模型进行交互，实现端侧模型的问答功能。 |

注意

模型资源来自[Matrix](https://matrix.openharmony.cn/#/model/main)模型库，chat接口默认调用模型为Qwen25-7B-Instruct。

## 白名单申请

打开华为开发者联盟的“[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)”页面，填写“概述”，端侧模型问答接口调用申请，问题分类选择“HarmonyOS NEXT > 系统 > Data Augmentation Kit”，描述问题详情并单击“提交问题”。提交问题后，有时需要您进一步澄清问题，请及时关注进展并予以回复，以便更好地解决问题。

注意

1.当前端侧模型问答仅支持PC/2in1设备类型，其它设备类型（Phone、Tablet等）无法使用此能力。

2.为了提供优质的开发体验，当前端侧模型问答接口需要申请，优先处理华为开放生态团队对接的企业方应用。

说明

申请接口调用信息模板：

1. 应用名称：xxx。
2. bundleName：xxx。
3. AppID：xxx。
4. 支持PC/2in1设备类型：是或否。
5. 华为开放生态团队对接的企业方应用：是或否。
6. 当前鸿蒙化进展：xxx。
7. 当前已经支持的AI能力：xxx。
8. 当前行业与用户影响力：xxx。
9. 应用内容信息介绍：xxx。

## 开发步骤

1. 问答过程中，端侧模型与LLM通过http请求交互，因此需要为应用申请网络权限。

   ```
   1. // module.json5中配置"requestPermissions"字段
   2. "requestPermissions": [
   3. {
   4. "name": "ohos.permission.INTERNET"
   5. }
   6. ],
   ```
2. 调用init接口，拉起本地AI模型管理。
3. 本地AI模型管理首次拉起，弹出隐私声明界面，同意后下载默认模型。
4. 本地AI模型管理非首次拉起，打开设置>系统>本地AI模型管理，下载默认模型。
5. 等待模型下载完成后，调用chat接口，开始进行端侧问答。

## 完整示例代码

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { localChatModel } from '@kit.DataAugmentationKit'

4. type MessageRole = 'system' | 'user' | 'assistant';

6. interface ChatMessage {
7. role: MessageRole;
8. content: string;
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State title: string = '端侧大模型问答助手';
15. @State isStreamMode: boolean = true;
16. @State messages: ChatMessage[] = [];
17. @State inputText: string = '';
18. @State initFlag: boolean = false;
19. @State isProcessing: boolean = false;
20. @State assistantContent: string = '';
21. @State chatCounter: number = 0;

23. // 页面加载时，拉起模型管理应用
24. onPageShow() {
25. console.info('modelChat onPageShow');
26. this.initModel();
27. }

29. private scroller: Scroller = new Scroller();

31. private scrollToBottom() {
32. setTimeout(() => {
33. this.scroller.scrollEdge(Edge.Bottom);
34. }, 50);
35. }

37. private addMessage(role: MessageRole, content: string): void {
38. const newMessage: ChatMessage = {
39. role: role,
40. content: content,
41. };
42. this.messages = [...this.messages, newMessage];
43. }

45. private async initModel(): Promise<void> {
46. try {
47. await localChatModel.init();
48. this.initFlag = true;
49. this.addMessage('system', '模型初始化完成！');
50. } catch (err) {
51. const error = err as BusinessError;
52. this.initFlag = false;
53. this.addMessage('system', `模型初始化出错: ${error.message}`);
54. }
55. }

57. private async DoChat(questionId: number): Promise<void> {
58. if (!this.inputText.trim() || this.isProcessing) {
59. return;
60. }
61. const userQuestion = this.inputText.trim();
62. if (!userQuestion) {
63. return;
64. }
65. this.inputText = '';
66. this.addMessage('user', userQuestion);
67. this.assistantContent = "思考中...";
68. this.isProcessing = true;

70. const questionInfo: localChatModel.QuestionInfo = {
71. questionId: questionId,
72. content: userQuestion
73. };

75. const localConfig: localChatModel.Config = {
76. isStream: this.isStreamMode
77. };

79. const localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
80. this.scrollToBottom();
81. if (err) {
82. if (this.assistantContent == "思考中...") {
83. this.assistantContent = "";
84. this.isProcessing = false;
85. }
86. // 模型运行相关错误码
87. console.error('modelChat Callback failed:', err.message);
88. this.addMessage('system', `localChatCallback: error code is ${err.code},  ${err.message}`);
89. this.scrollToBottom();
90. }
91. if (ans.content && ans.content.trim() !== '') {
92. if (this.assistantContent == "思考中...") {
93. this.assistantContent = "";
94. }
95. this.assistantContent += ans.content;
96. this.scrollToBottom();
97. }
98. this.scrollToBottom();
99. if (ans.isFinished) {
100. console.log('modelChat finished');
101. this.addMessage('assistant', this.assistantContent);
102. this.isProcessing = false;
103. }

105. };
106. try {
107. console.log('modelChat Starting chat...');
108. localChatModel.chat(questionInfo, localConfig, localChatCallback);
109. } catch (err) {
110. // 入参相关错误码
111. const error = err as BusinessError;
112. console.error('modelChat Chat failed:', error.message);
113. this.addMessage('system', `chat: error code is ${error.code},  ${error.message}`);
114. this.isProcessing = false;
115. }
116. }

118. private clearChat(): void {
119. this.messages = [];
120. }

122. build() {
123. Stack({ alignContent: Alignment.Top }) {
124. Column() {
125. Row() {
126. Text(this.title)
127. .fontSize(20)
128. .fontWeight(FontWeight.Bold)
129. .fontColor('#1a73e8')
130. .margin({ left: 12 })

132. Circle()
133. .width(10)
134. .height(10)
135. .margin({ left: 12 })
136. .fill(this.initFlag ? '#0f0' : '#f00')
137. .opacity(0.8)

139. Text(this.initFlag ? '已就绪' : '未就绪')
140. .margin({ left: 6 })
141. .fontSize(12)
142. .fontColor('#666')

144. Blank()

146. Row() {
147. Button(this.isStreamMode ? '流式' : '非流式')
148. .width(70)
149. .height(25)
150. .fontSize(12)
151. .margin({ right: 20 })
152. .backgroundColor(Color.Gray)
153. .fontColor(Color.White)
154. .borderRadius(12.5)
155. .onClick(() => {
156. this.isStreamMode = !this.isStreamMode;
157. this.addMessage('system', `已切换至 ${this.isStreamMode ? '流式问答' : '非流式问答'} 模式`);
158. })
159. }
160. .margin({ right: 12 })
161. }
162. .width('100%')
163. .height(50)
164. .backgroundColor(Color.White)
165. .borderRadius(16)
166. .shadow({
167. radius: 4,
168. color: '#1a73e888',
169. offsetX: 0,
170. offsetY: 2
171. })
172. .margin({ bottom: 12 })

174. // 聊天区域
175. Scroll(this.scroller) {
176. Column() {
177. ForEach(this.messages, (msg: ChatMessage, index: number) => {
178. if (msg.role === 'system') {
179. Row() {
180. Text(msg.content)
181. .fontSize(14)
182. .fontColor('#666')
183. .textAlign(TextAlign.Center)
184. .padding(8)
185. }
186. .width('100%')
187. .justifyContent(FlexAlign.Center)
188. .margin({ top: index === 0 ? 0 : 12 })
189. } else if (msg.role === 'user') {
190. Row() {
191. Blank()
192. Text(msg.content)
193. .fontSize(16)
194. .fontColor(Color.White)
195. .padding(10)
196. .backgroundColor('#1a73e8')
197. .borderRadius(12)
198. }
199. .width('100%')
200. .margin({ top: 12 })
201. .justifyContent(FlexAlign.End)
202. } else if (msg.role === 'assistant') {
203. Row() {
204. Column() {
205. Text(msg.content)
206. .fontSize(16)
207. .fontColor('#333')
208. .lineHeight(20)
209. .padding(10)
210. .backgroundColor(Color.White)
211. .borderRadius(12)
212. }
213. .borderRadius(12)
214. .margin({ left: 8 })

216. Blank()
217. }
218. .width('100%')
219. .margin({ top: 12 })
220. .justifyContent(FlexAlign.Start)
221. }
222. }, (msg: ChatMessage) => msg.toString())

224. // 加载指示器
225. if (this.isProcessing) {
226. Row() {
227. Column() {
228. Text(this.assistantContent)
229. .fontSize(16)
230. .fontColor('#333')
231. .lineHeight(20)
232. .padding(10)
233. .backgroundColor(Color.White)
234. .borderRadius(12)
235. }
236. .borderRadius(12)
237. .margin({ left: 8 })

239. Blank()
240. }
241. .width('100%')
242. .margin({ top: 12 })
243. }
244. }
245. .padding(12)
246. .width('100%')
247. }
248. .width('100%')
249. .layoutWeight(1)
250. .margin({ bottom: 12 })

252. // 输入区域
253. Column() {
254. Row() {
255. TextInput({ text: this.inputText, placeholder: '请输入您的问题...' })
256. .flexGrow(1)
257. .height(42)
258. .fontSize(16)
259. .padding(8)
260. .backgroundColor(Color.White)
261. .borderRadius(21)
262. .width('85%')
263. .onChange((value: string) => {
264. this.inputText = value;
265. })
266. .onSubmit(() => {
267. if (!this.isProcessing && this.inputText.trim() !== '') {
268. const chatId = this.chatCounter++;
269. this.DoChat(chatId);
270. }
271. })

273. Button('发送')
274. .width(72)
275. .height(42)
276. .fontSize(16)
277. .margin({ left: 8 })
278. .backgroundColor('#1a73e8')
279. .fontColor(Color.White)
280. .borderRadius(21)
281. .onClick(() => {
282. if (!this.isProcessing && this.inputText.trim() !== '') {
283. const chatId = this.chatCounter++;
284. this.DoChat(chatId);
285. }
286. })
287. .opacity(this.isProcessing || this.inputText.trim() === '' ? 0.6 : 1)

289. Button("清空")
290. .width(72)
291. .height(42)
292. .fontSize(16)
293. .margin({ left: 8 })
294. .fontColor('#fff')
295. .backgroundColor('#ea4335')
296. .borderRadius(18)
297. .onClick(() => {
298. this.clearChat();
299. })
300. }
301. .width('100%')
302. .justifyContent(FlexAlign.SpaceBetween)
303. .alignItems(VerticalAlign.Center)
304. }
305. .width('100%')
306. .padding(8)
307. .backgroundColor(Color.White)
308. .borderRadius(16)
309. .shadow({
310. radius: 4,
311. color: '#1a73e888',
312. offsetX: 0,
313. offsetY: 2
314. })
315. }
316. .width('100%')
317. .height('100%')
318. .padding(12)
319. .backgroundColor('#f0f5ff')
320. }
321. .width('100%')
322. .height('100%')
323. }
324. }
```
