---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-demo
title: 完整示例代码
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > 完整示例代码
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be978d8e6e27cb413d7a4f807d7aea6463038bd21adbfb72c90bb2cc577f041e
---

说明

需要完成网络权限的申请，参见：[开发准备](data-augmentation-rag-development.md#开发准备)。

## EntryAbility.ets

应用的生命周期实现在这个文件中，主要在应用启动时进行RagSession、数据库连接的创建，应用关闭时进行RagSession、数据库连接的释放。

```
1. // src/main/ets/entryability/EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want, common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import SetUp from '../entryability/SetUp';
7. import Config from '../entryability/Config';
8. import { rag } from '@kit.DataAugmentationKit';

10. const DOMAIN = 0x0000;

12. export default class EntryAbility extends UIAbility {
13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
15. }

17. onDestroy(): void {
18. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
19. }

21. onWindowStageCreate(windowStage: window.WindowStage): void {
22. // Main window is created, set main page for this ability
23. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
24. windowStage.loadContent('pages/Index', (err) => {
25. if (err.code) {
26. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
27. return;
28. }
29. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
30. });

32. AppStorage.setOrCreate<common.UIAbilityContext>('Context', this.context);

34. let setUp: SetUp = new SetUp();
35. setUp.initTable().then(() => {
36. setUp.insertData();
37. AppStorage.setOrCreate<SetUp>('SetUpObject', setUp);
38. });

40. let config: Config = new Config();
41. rag.createRagSession(this.context, config.getRAGConfig()).then((data) => {
42. AppStorage.setOrCreate<rag.RagSession>('RagSessionObject', data);
43. }).catch((err: BusinessError) => {
44. hilog.error(DOMAIN, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
45. });
46. }

48. onWindowStageDestroy(): void {
49. // Main window is destroyed, release UI related resources
50. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
51. const session = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
52. session?.close().catch(() => {
53. hilog.error(DOMAIN, 'testTag', 'close rag session failed');
54. });
55. const setup = AppStorage.get<SetUp>('SetUpObject') as SetUp;
56. setup?.closeStore();
57. }

59. onForeground(): void {
60. // Ability has brought to foreground
61. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
62. }

64. onBackground(): void {
65. // Ability has back to background
66. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
67. }
68. }
```

## SetUp.ets

SetUp.ets负责数据源的构造，目前实现是从一个自带的Json文件读取数据，并且插入一个开启知识加工开关的数据库中。数据更新成功后，将会自动触发知识加工，形成知识库。

```
1. // src/main/ets/entryability/SetUp.ets
2. import { UIAbility, common } from '@kit.AbilityKit';
3. import { relationalStore } from '@kit.ArkData';
4. import { buffer } from '@kit.ArkTS';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const TAG = 'SetUp';

9. export default class SetUp extends UIAbility {
10. storeName: string = 'testmail_store.db';  // 与knowledge_schema.json文件中数据库名保持一致
11. storeConfig: relationalStore.StoreConfig = {
12. name: this.storeName,
13. securityLevel: relationalStore.SecurityLevel.S3,
14. enableSemanticIndex: true,  // 源数据库需配置该项为true才会触发知识加工
15. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
16. };
17. store?: relationalStore.RdbStore;

19. async getStore() {
20. try {
21. if (!this.store) {
22. let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // 获取全局context
23. this.store = await relationalStore.getRdbStore(context, this.storeConfig);
24. }
25. } catch (err) {
26. hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
27. }
28. return this.store;
29. }

31. async initTable() {
32. try {
33. const tmpStore = await this.getStore();
34. const createTableSql = 'CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, content text, ' +
35. 'image_text text, attachment_names text, inline_files text, sender text, receivers text, received_date text);';
36. await tmpStore?.execute(createTableSql, 0, undefined);
37. hilog.info(0, TAG, 'InitTable success');
38. } catch (err) {
39. hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
40. }
41. }

43. async insertData() {
44. try {
45. let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // 获取全局context
46. const fileList = context.resourceManager.getRawFileListSync('');
47. let dataIndex = 0;
48. for (let file of fileList) {  // 从json文件中解析数据到数据库中
49. if (!file.startsWith('sourceData') || !file.endsWith('.json')) {
50. hilog.info(0, TAG, `file ${file} skip`);
51. continue;
52. }
53. hilog.info(0, TAG, `file ${file} start`);
54. try {
55. const rawFileData = await context.resourceManager.getRawFileContent(file);
56. const fileData: string = buffer.from(rawFileData).toString();
57. const resultObjArr = JSON.parse(fileData) as Array<object>;
58. let jsonObj: object | undefined;
59. for (let i = 0; i < resultObjArr.length; i++) {
60. try {
61. jsonObj = resultObjArr[i];
62. let sender: string = jsonObj?.['sender_name'];
63. if (!sender || sender.length == 0) {
64. sender = 'undefined';
65. }
66. const receiverStr: string = JSON.stringify(jsonObj['to']);
67. const formattedDateStr: string = jsonObj?.['received_time']?.replace(' ', 'T');
68. let received_date = Date.parse(formattedDateStr);
69. if (!received_date || Number.isNaN(received_date)) {
70. received_date = 0;
71. }
72. let subject: string = jsonObj?.['subject']?.replace(/'/g, '');
73. let doc: string = jsonObj?.['body']?.replace(/'/g, '');
74. let sql = `insert or replace into email VALUES(${dataIndex}, '${subject}', '${doc}', '',` +
75. ` '', '', '${sender}', '${receiverStr}', '${received_date}');`
76. const tmpStore = await this.getStore();
77. await tmpStore?.executeSql(sql);
78. dataIndex++;
79. } catch (e) {
80. hilog.error(0, TAG, `Insert failed, code is ${e.code},message is ${e.message}, jsonObj: ${jsonObj}`);
81. }
82. }
83. } catch (e) {
84. hilog.error(0, TAG, `Load file failed, code is ${e.code},message is ${e.message}`);
85. }
86. hilog.info(0, TAG, `file ${file} end`);
87. }
88. hilog.info(0, TAG, 'insertData end');
89. } catch (err) {
90. hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
91. }
92. }

94. async closeStore() {
95. try {
96. await this.store?.close();
97. } catch (e) {
98. hilog.error(0, TAG, `Close store failed, code is ${e.code},message is ${e.message}.`);
99. }
100. }
101. }
```

## HttpUtils.ets

HttpUtils.ets是与大模型交互的Http工具类，主要负责发往大模型的报文拼装、流式Http消息接收回调的注册等。开发者需根据自身资源，选用合适的大模型。示例代码使用的是[ModelArts](https://console.huaweicloud.com/modelarts)，需要把其中的"\*\*\*\*replace your API key in here\*\*\*\*"替换为真实的API Key。

```
1. // src/main/ets/entryability/HttpUtils.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { http } from '@kit.NetworkKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const TAG = 'HttpUtils';

8. class HttpUtils {
9. httpRequest?: http.HttpRequest;
10. url: string = 'https://api.modelarts-maas.com/v1/chat/completions'; // 开发者需要根据选择的大模型对应修改url以及下面的model
11. isFinished: boolean = false;

13. initOption(question: string) {
14. let option: http.HttpRequestOptions = {
15. // 请求方式
16. method: http.RequestMethod.POST,
17. // 请求头
18. header: {
19. 'Content-Type': 'application/json',
20. // API-KEY from Model
21. 'Authorization': `Bearer ****replace your API key in here****`
22. },
23. // 请求体
24. extraData: {
25. 'stream': true,
26. 'temperature': 0.1,
27. 'max_tokens': 1000,
28. 'frequency_penalty': 1,
29. 'model': 'qwen3-32b',
30. 'top_p': 0.1,
31. 'presence_penalty': -1,
32. 'messages': JSON.parse(question),
33. "chat_template_kwargs": {
34. // 关闭思考中数据
35. "enable_thinking": false
36. }
37. }
38. };
39. return option;
40. }

42. async requestInStream(question: string) { // 拼装流式请求的option并发起流式请求
43. if (!this.httpRequest) {
44. this.httpRequest = http.createHttp();
45. }
46. this.httpRequest?.requestInStream(this.url, this.initOption(question)).catch((err: BusinessError) => {
47. hilog.error(0, TAG, 'Failed to request. Cause: %{public}s', JSON.stringify(err));
48. });
49. this.isFinished = false;
50. }

52. on(callback: Callback<ArrayBuffer>) { // 注册数据接受、数据结束的监听
53. if (!this.httpRequest) {
54. this.httpRequest = http.createHttp();
55. }
56. this.httpRequest.on('dataReceive', callback);
57. }

59. end() { // 取消注册数据接受、数据结束的监听，释放httpRequest
60. this.httpRequest?.off('dataReceive');
61. this.httpRequest?.destroy();
62. this.httpRequest = undefined;
63. }

65. cancel() {
66. this.httpRequest?.off('dataReceive');
67. this.httpRequest?.destroy();
68. this.httpRequest = undefined;
69. }
70. }

72. export default new HttpUtils;
```

## MyChatLlm.ets

应用继承实现ChatLLM类，相当于应用侧实现的大模型客户端，将在创建RagSession的时候把这个大模型客户端作为入参传入RagSession中。

```
1. // src/main/ets/entryability/MyChatLlm.ets
2. import { rag } from '@kit.DataAugmentationKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { JSON, util } from '@kit.ArkTS';
5. import HttpUtils from './HttpUtils';

7. const TAG = "MyChatLLM";

9. function parseLLMResponse(data: ArrayBuffer): rag.LLMStreamAnswer | undefined {
10. try {
11. let decoder = util.TextDecoder.create(`"utf-8"`);
12. let str = decoder.decodeToString(new Uint8Array(data));
13. hilog.info(0, TAG, str);
14. let chunk = '';
15. let isFinished: boolean = (str.length < 20);
16. for (let resultStr of str.split('data:')) {
17. if (resultStr.trim() == ('[DONE]')) {
18. isFinished = true;
19. break;
20. }
21. if (resultStr.trim().length == 0) {
22. continue;
23. }
24. try {
25. let obj = JSON.parse(resultStr.trim());
26. if ((obj as object)?.['choices'].length === 0) {
27. continue;
28. }
29. if ((obj as object)?.['choices'][0]?.['delta']?.['reasoning_content']) {
30. chunk += (obj as object)?.['choices'][0]['delta']['reasoning_content'];
31. } else if ((obj as object)?.['choices'][0]?.['delta']?.['content']) {
32. chunk += (obj as object)?.['choices'][0]['delta']['content'];
33. }
34. } catch (err) {
35. hilog.error(0, TAG, `Parse LLM response failed, resultStr: ${resultStr}`);
36. }
37. }
38. let answer: rag.LLMStreamAnswer = {
39. isFinished: isFinished,
40. chunk: chunk
41. };
42. return answer;
43. } catch (err) {
44. hilog.error(0, TAG, `Parse LLM response failed, error code: ${err.code}, error message: ${err.message}`);
45. }
46. return undefined;
47. }

49. export default class MyChatLLM extends rag.ChatLLM {
50. async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
51. let ret: rag.LLMRequestStatus = rag.LLMRequestStatus.LLM_SUCCESS;
52. try {
53. let dataCallback = async (data: ArrayBuffer) => { // 收到数据时的回调函数，解析数据并组装LLMStreamAnswer，通过callback回调
54. hilog.debug(0, TAG, 'on callback enter. data length: %{public}d', data.byteLength);
55. // 解析大模型返回报文，逻辑因选择模型而异
56. const answer = parseLLMResponse(data);
57. if (!answer) {
58. return;
59. }
60. HttpUtils.isFinished = answer.isFinished;
61. callback(answer);
62. hilog.debug(0, 'MyChatLLM', 'Request LLM success. isFinished: %{public}s, data: %{public}s',
63. Number(answer.isFinished).toString(), answer.chunk);
64. };

66. HttpUtils.on(dataCallback);
67. HttpUtils.requestInStream(query);
68. } catch (err) {
69. hilog.error(0, TAG, `Request LLM failed, error code: ${err.code}, error message: ${err.message}`);
70. ret = rag.LLMRequestStatus.LLM_REQUEST_ERROR; // 开发者可判断错误码从而返回其他LLM错误码
71. }
72. return {
73. chatId: 0,
74. status: ret,
75. };
76. }
77. cancel(chatId: number): void {
78. hilog.info(0, TAG, `The request for the large model has been canceled. chatId: ${chatId}`);
79. HttpUtils.cancel();
80. }
81. }
```

## Config.ets

Config.ets主要负责RagSession创建时入参的组装。详细配置方法及含义可参见[智慧化数据检索](dataaugmentation-retrieval.md)。

```
1. // src/main/ets/entryability/Config.ets
2. import { common, UIAbility } from '@kit.AbilityKit';
3. import { rag, retrieval } from '@kit.DataAugmentationKit';
4. import { relationalStore } from '@kit.ArkData';
5. import MyChatLlm from './MyChatLlm';

7. export default class Config extends UIAbility {
8. getRetrievalConfig() {
9. let storeConfigVector: relationalStore.StoreConfig = {
10. name: 'testmail_store_vector.db', // 知识加工后向量数据库文件名，在原数据库名基础上加_vector后缀
11. securityLevel: relationalStore.SecurityLevel.S3,
12. vector: true  // 向量数据库应设置该项为true
13. };

15. let storeConfigInvIdx: relationalStore.StoreConfig = {
16. name: 'testmail_store.db', // 知识加工后，倒排数据库即原数据库
17. securityLevel: relationalStore.SecurityLevel.S3,
18. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
19. };

21. let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext;
22. let channelConfigVector: retrieval.ChannelConfig = {
23. channelType: retrieval.ChannelType.VECTOR_DATABASE,
24. context: context,
25. dbConfig: storeConfigVector
26. };
27. let channelConfigInvIdx: retrieval.ChannelConfig = {
28. channelType: retrieval.ChannelType.INVERTED_INDEX_DATABASE,
29. context: context,
30. dbConfig: storeConfigInvIdx
31. };
32. let retrievalConfig: retrieval.RetrievalConfig = {
33. channelConfigs: [channelConfigInvIdx, channelConfigVector]
34. };
35. return retrievalConfig;
36. }

38. getRetrivalCondition() {
39. let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
40. ftsTableName: 'email_inverted',
41. fromClause: 'email_inverted',
42. primaryKey: ['chunk_id'],
43. responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'chunk_text'],
44. deepSize: 500,
45. recallName: 'invertedvectorRecall',
46. };
47. let floatArray = new Float32Array(128).fill(0.1);
48. let vectorQuery: retrieval.VectorQuery = {
49. column: 'repr',
50. value: floatArray,
51. similarityThreshold: 0.1
52. };
53. let recallConditionVector: retrieval.VectorRecallCondition = {
54. vectorQuery: vectorQuery,
55. fromClause: 'email_vector',
56. primaryKey: ['id'],
57. responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'repr'],
58. recallName: 'vectorRecall',
59. deepSize: 500
60. };
61. let rerankMethod: retrieval.RerankMethod = {
62. rerankType: retrieval.RerankType.RRF,
63. isSoftmaxNormalized: true,
64. };
65. let retrievalCondition: retrieval.RetrievalCondition = {
66. rerankMethod: rerankMethod,
67. recallConditions: [recallConditionInvIdx, recallConditionVector],
68. resultCount: 5
69. };
70. return retrievalCondition;
71. }

73. getRAGConfig() {
74. let retrievalConfig: retrieval.RetrievalConfig = this.getRetrievalConfig();
75. let retrievalCondition: retrieval.RetrievalCondition = this.getRetrivalCondition();
76. let config: rag.Config = {
77. llm: new MyChatLlm(),
78. retrievalConfig: retrievalConfig,
79. retrievalCondition: retrievalCondition
80. };
81. return config;
82. }
83. }
```

## Index.ets

应用界面功能的实现包含：输入问 入框、开始问答的按钮、答案输出的输出框。

```
1. // src/main/ets/pages/Index.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { rag } from '@kit.DataAugmentationKit';
4. import hilog from '@ohos.hilog';

6. @Entry
7. @Component
8. struct Index {
9. @State inputStr: string = '知识问答开发指南完整示例代码';
10. @State answerStr: string = '';
11. @State thoughtStr: string = '';

13. build() {
14. Column() {
15. Row({ space: 8 }) {
16. TextArea({ text: this.inputStr, placeholder: 'Input question here!' })
17. .margin({ top: 8 })
18. .borderStyle(BorderStyle.Dotted)
19. .onChange((newValue) => {
20. this.inputStr = newValue;
21. })
22. .width('95%')
23. .height('15%')
24. .fontWeight(FontWeight.Bold)
25. }

27. Button('streamRun')
28. .onClick(async () => {
29. // 获取创建的RagSession
30. let session: rag.RagSession = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
31. let config: rag.RunConfig = {
32. // 指定流式输出的输出类型
33. answerTypes: [rag.StreamType.THOUGHT, rag.StreamType.ANSWER]
34. };
35. this.thoughtStr = '';
36. this.answerStr = '';
37. // 发起提问
38. session.streamRun(this.inputStr, config, ((err: BusinessError, stream: rag.Stream) => {
39. // 接收答案的callback回调，处理答案信息
40. if (err) {
41. this.answerStr = `streamRun inner failed. code is ${err.code}, message is ${err.message}`;
42. } else {
43. // 根据不同的数据类型，选择不同的处理方式
44. switch (stream.type) {
45. case rag.StreamType.THOUGHT:
46. this.thoughtStr += stream.answer.chunk;
47. break;
48. case rag.StreamType.ANSWER:
49. this.answerStr += stream.answer.chunk;
50. break;
51. case rag.StreamType.REFERENCE:
52. default:
53. hilog.info(0, 'Index', `streamRun msg: ${JSON.stringify(stream)}`);
54. }
55. }
56. })).catch((e: BusinessError) => {
57. this.answerStr = `streamRun failed. code is ${e.code}, message is ${e.message}`;
58. });
59. })
60. .width('30%')
61. .height('5%')
62. Column({ space: 2 }) {
63. Text(this.thoughtStr)
64. .fontSize(12)
65. .fontColor(Color.Gray)
66. .padding(8)
67. .width('95%')
68. .height('auto')
69. Text(this.answerStr)
70. .padding(8)
71. .width('95%')
72. .height('auto')
73. }
74. .backgroundColor(0xF5DEB3)
75. .width('95%')
76. .height('75%')
77. }
78. .height('100%')
79. .width('100%')
80. }
81. }
```

## knowledge\_schema.json

知识加工的schema文件用来定义知识加工时对于源数据库的处理逻辑。

```
1. // src/main/resources/rawfile/arkdata/knowledge/knowledge_schema.json ------ 实际使用时请删除本行注释
2. {
3. "knowledgeSource": [{
4. "version": 1,
5. "dbName": "testmail_store.db",
6. "tables": [{
7. "tableName": "email",
8. "referenceFields": ["id"],
9. "knowledgeFields": [{
10. "columnName": "subject",
11. "type": ["Text"]
12. },
13. {
14. "columnName": "content",
15. "type": ["Text"]
16. },
17. {
18. "columnName": "image_text",
19. "type": ["Text"]
20. },
21. {
22. "columnName": "attachment_names",
23. "type": ["Text"]
24. },
25. {
26. "columnName": "inline_files",
27. "type": ["Json"],
28. "parser": [
29. {
30. "type": "File",
31. "path": "$[*].uri"
32. }
33. ]
34. },
35. {
36. "columnName": "sender",
37. "type": ["Scalar"],
38. "description": "sender"
39. },
40. {
41. "columnName": "receivers",
42. "type": ["Scalar"],
43. "description": "receivers"
44. },
45. {
46. "columnName": "received_date",
47. "type": ["Scalar"],
48. "description": "received_date"
49. }]
50. }]
51. }]
52. }
```

## sourceData.json

sourceData.json文件中的内容为模拟数据源，作为输入插入应用数据库表。真实情况应用数据输入途径应该是界面输入、服务器获取等。

```
1. // src/main/resources/rawfile/sourceData.json ------ 仅用于测试数据插入，请开发者根据业务需要预置数据库数据
2. [{
3. "subject": "【请阅】手机优惠政策",
4. "sender_name": "test1",
5. "sender_email": "test1@example.com",
6. "received_time": "2025-05-15 15:49:04.135",
7. "recipients": [
8. {
9. "Address": "test2@example.com",
10. "name": "test2",
11. "Type": 1
12. },
13. {
14. "Address": "test3@example.com",
15. "name": "test3",
16. "Type": 2
17. },
18. {
19. "Address": "test4@example.com",
20. "name": "test4",
21. "Type": 3
22. }
23. ],
24. "to": [
25. "lisi"
26. ],
27. "cc": [
28. "wangwu"
29. ],
30. "bcc": [
31. "zhaoliu"
32. ],
33. "attachment": [],
34. "body": "优惠政策：\r\n旗舰系列优惠10%！！ 非旗舰系列优惠20%！！。",
35. "unread": false
36. }]
```
