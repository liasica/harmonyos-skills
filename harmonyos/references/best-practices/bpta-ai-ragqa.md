---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ai-ragqa
title: 基于RAG框架实现邮件智能问答
breadcrumb: 最佳实践 > AI使能 > 基于RAG框架实现邮件智能问答
category: best-practices
scraped_at: 2026-04-29T14:13:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9dbdfb4e9eb23714670d2a35704ef359e1897b568d4a5a111696636ca09262be
---

## 概述

RAG（检索增强生成）是一种结合了信息检索与文本生成技术的混合型自然语言处理方法。其核心思想是通过引入外部知识库，动态检索与输入问题相关的信息，并基于这些信息生成更准确、可靠的回答，被广泛用于问答系统、对话助手、文档摘要等任务，尤其在需要结合外部知识的场景（如医疗、法律、学术研究）中表现突出。

当RAG作用于私人信息领域，就可结合私人信息形成定制化的问答系统、检索助手，本文将从以下关键步骤介绍如何基于RAG框架实现邮件系统的智能问答。

* [知识库构建](bpta-ai-ragqa.md#section147555014915)：将用户邮件信息写入数据库中，便于后续查找。
* [LLM部署与调用](bpta-ai-ragqa.md#section29233013420)：部署大模型和配置request请求。
* [RAG会话](bpta-ai-ragqa.md#section1939152912915)：配置并开启RAG会话，包括配置知识加工schema、检索配置retrieval.RetrievalConfig、检索条件retrieval.RetrievalCondition和LLM会话。

## 用户体验

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/97joQ8OSSCiuWnHnlteNQQ/zh-cn_image_0000002368829345.png?HW-CC-KV=V1&HW-CC-Date=20260429T061312Z&HW-CC-Expire=86400&HW-CC-Sign=A016A4BD92A5E366AA31930B2BEB46825975D9239313D283CD00FCB3228510BE "点击放大")

本文案例依托用户自定义的邮件数据库进行智能问答，准确识别语义并提供精确答案，并有以下基本功能：

1. 自由增加数据： 系统能接收、存储新的数据源。
2. 精准问答： 构建一个基于上述数据和模型的、能够提供准确答案的问答系统。

## 实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/BuWvJ9mzRKyxr8U6TAXjyQ/zh-cn_image_0000002368709477.png?HW-CC-KV=V1&HW-CC-Date=20260429T061312Z&HW-CC-Expire=86400&HW-CC-Sign=4079EBBEBD38EC042BBECC22A1812AE77BFA361A99B575C41A19C7B56099B790 "点击放大")

RAG提供用于进行流式问答的接口，整体问答流程分为两个阶段：

* **检索阶段**：根据用户输入的问题或指令，利用稠密向量检索、关键词匹配等技术，从数据库或文档库中筛选出最相关的文本片段。
* **生成阶段**：将检索结果与原始输入拼接，输入大语言模型（如千问等），生成结合上下文知识的最终回答。

## 知识库构建

本章节介绍如何将原始的邮件数据存储到数据库中，以便后续问答使用。

### 原始数据准备

将邮件数据进行提取和清理，存储为如下例所示的结构，包含包括发件人、收件人、时间、邮件文本等基本信息，便于后续的搜索查找。

```
1. {
2. "subject": "【请阅】Mate系列手机优惠政策",
3. "sender_name": "zhangsan",
4. "sender_email": "zhangsan@xxx.com",
5. "received_time": "2025-05-15 15:49:04.135",
6. "recipients": [
7. {
8. "Address": "lisi@xxx.com",
9. "name": "lisi",
10. "Type": 1
11. },
12. {
13. "Address": "wangwu@xxx.com",
14. "name": "wangwu",
15. "Type": 2
16. },
17. {
18. "Address": "zhaoliu@xxx.com",
19. "name": "zhaoliu",
20. "Type": 3
21. }
22. ],
23. "to": [
24. "lisi"
25. ],
26. "cc": [
27. "wangwu"
28. ],
29. "bcc": [
30. "zhaoliu"
31. ],
32. "attachment": [],
33. "body": "优惠政策：\r\n\r\nMate60系列优惠xxx！！ Mate70系列优惠xxx！！。",
34. "unread": false
35. }
```

### 初始化数据库

首先需要构建一个数据库，获取一个RdbStore，其中包括建库、建表、插入数据的操作步骤。

1、通过[relationalStore.getRdbStore()](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore)接口创建或打开已有关系型数据库。

2、通过[execute()](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#execute12)接口执行建表操作，包含id、subject text、content text、image\_text text、attachment\_names text等字段。

说明

数据库创建时StoreConfig的enableSemanticIndex需要为true才能触发知识加工。

```
1. storeName: string = "testmail_store.db";
2. // keep same with the db name in knowledge_schema.json
3. storeConfig: relationalStore.StoreConfig = {
4. name: this.storeName,
5. securityLevel: relationalStore.SecurityLevel.S3,
6. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
7. enableSemanticIndex: true
8. };
9. store: relationalStore.RdbStore | null = null;
10. dataIndexNow = 0;

12. async InitTable() {
13. try {
14. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
15. if (!this.store) {
16. this.store = await relationalStore.getRdbStore(context, this.storeConfig);
17. }
18. if (this.store != undefined) {
19. const createTableSql =
20. "CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, content text, image_text text," +
21. " attachment_names text, inlineFiles text, sender text, toReceivers text, ccReceivers text, " +
22. "bccReceivers text, received_date text);";
23. await this.store.execute(createTableSql, 0, undefined);
24. await this.InsertData(context);
25. }
26. } catch (e) {
27. hilog.error(0, TAG, `Init DB failed, code is ${e.code},message is ${e.message}.`);
28. }
29. }
```

[SetUp.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/SetUp.ets#L26-L55)

依次读取原始数据文件，将读出的数据使用[execute()](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#execute12)接口插入到新建的数据库中。

```
1. async InsertData(context: common.UIAbilityContext) {
2. // ...
3. let fileList: string[] = [];
4. try {
5. fileList = context.resourceManager.getRawFileListSync('');
6. } catch (error) {
7. let err = error as BusinessError;
8. hilog.error(0x0000, TAG, `getRawFileListSync failed, error code=${err.code}, message=${err.message}`);
9. }
10. let dataIndex = this.dataIndexNow;
11. for (let file of fileList) {
12. // ...
13. try {
14. const rawFileData = await context.resourceManager.getRawFileContent(file);
15. const fileData: string = buffer.from(rawFileData).toString();
16. const resultObjArr = JSON.parse(fileData) as Array<object>;
17. let jsonObj: object | undefined;
18. for (let i = 0; i < resultObjArr.length; i++) {
19. jsonObj = resultObjArr[i];
20. dataIndex = await this.InsertSingleDataJson(jsonObj, this.store, dataIndex)
21. }
22. } catch (e) {
23. hilog.error(0, TAG, `Load file failed, code is ${e.code},message is ${e.message}`);
24. }
25. }
26. this.dataIndexNow = dataIndex;
27. }
```

[SetUp.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/SetUp.ets#L59-L104)

## LLM部署与调用

本章节介绍LLM模型的部署和调用，在实际开发过程中可根据业务诉求自行选择LLM大模型进行配置，这里以华为云部署的大模型接入作为参考。

### 模型部署

1. 进入并登录网址[ModelArts - Console](https://console.huaweicloud.com/modelarts/?locale=zh-cn&region=cn-southwest-2#/model-studio/authmanage)，在左侧菜单中选择API Key管理，点击右上角创建API key，生成Key。

   说明

   生成的key值只在弹窗中出现一次，请立刻保存后再关闭弹窗。
2. 在左侧菜单中选择在线推理，在商用服务列表中开通商用服务Qwen3-235B-A22B-32K。
3. 在[费用中心](https://account.huaweicloud.com/usercenter/?agencyId=4a4d3a21c84e4c94b7995314981bf802&region=cn-southwest-2&locale=zh-cn#/userindex/allview)管理页面进行服务充值。

### 模型调用

1、初始化请求，配置请求参数，在header中需要配置生成的API生成的key，extraData中需要传入相关的提问和模型参数，参考[请求参数说明](https://support.huaweicloud.com/usermanual-maas-modelarts/maas-modelarts-0011.html)设置frequency\_penalty频率奖惩、presence\_penalty新词语奖惩、top\_p浮点数累计概率控制确保大模型回答偏向简短精准，提升系统的回答速度和准确度。

```
1. httpRequest: http.HttpRequest | null = null;
2. url: string = "https://api.modelarts-maas.com/v1/chat/completions";
3. isFinished: boolean = false;

5. //initialize the llm option
6. initOption(question: string) {
7. let option: http.HttpRequestOptions = {
8. // request
9. method: http.RequestMethod.POST,
10. header: {
11. "Content-Type": "application/json",
12. // API-KEY from Model
13. "Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
14. },
15. extraData: {
16. "stream": true,
17. "temperature": 0.1,
18. "max_tokens": 10000,
19. "frequency_penalty": 1,
20. "model": "qwen3-235b-a22b",
21. "top_p": 0.1,
22. "presence_penalty": -1,
23. "messages": JSON.parse(question)
24. }
25. };
26. return option;
27. }
```

[LLMHttpUtils.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/common/utils/LLMHttpUtils.ets#L23-L49)

2、使用[requestInStream()](../harmonyos-references/js-apis-http.md#requestinstream10-1)根据URL地址和相关配置项，发起HTTP网络请求并返回流式响应。

```
1. async requestInStream(question: string) {
2. if (this.httpRequest === null) {
3. this.httpRequest = http.createHttp();
4. }
5. this.httpRequest.requestInStream(this.url, this.initOption(question)).catch((err: BusinessError) => {
6. hilog.error(0x0000, 'LLMHttpUtils', `requestInStream failed, error code=${err.code}, message=${err.message}`);
7. });
8. this.isFinished = false;
9. }
```

[LLMHttpUtils.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/common/utils/LLMHttpUtils.ets#L53-L61)

3、设置监听，订阅HTTP流式响应数据接收事件和HTTP流式响应数据接收完毕事件。

```
1. on(callback: Callback<ArrayBuffer>, endCallback: Callback<void>) {
2. if (this.httpRequest === null) {
3. this.httpRequest = http.createHttp();
4. }
5. this.httpRequest.on("dataReceive", callback);
6. this.httpRequest.on('dataEnd', endCallback);
7. }
```

[LLMHttpUtils.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/common/utils/LLMHttpUtils.ets#L65-L71)

## RAG会话

### 配置会话

1、配置知识库加工，如下所示配置resources/rawfile/arkdata/knowledge/knowledge\_schema.json文件，倒排表、向量库、向量表将会根据schema配置自动生成。

```
1. {
2. "knowledgeSource": [{
3. "version": 1,
4. "dbName": "testmail_store.db",
5. "tables": [{
6. "tableName": "email",
7. "referenceFields": ["id"],
8. "knowledgeFields": [{
9. "columnName": "subject",
10. "type": ["Text"]
11. },
12. {
13. "columnName": "content",
14. "type": ["Text"]
15. },
16. {
17. "columnName": "image_text",
18. "type": ["Text"]
19. },
20. {
21. "columnName": "attachment_names",
22. "type": ["Text"]
23. },
24. {
25. "columnName": "sender",
26. "type": ["Scalar"],
27. "description": "sender"
28. },
29. {
30. "columnName": "receivers",
31. "type": ["Scalar"],
32. "description": "receivers"
33. },
34. {
35. "columnName": "received_date",
36. "type": ["Scalar"],
37. "description": "received_date"
38. }]
39. }]
40. }]
41. }
```

2、构建检索配置[retrieval.RetrievalConfig](../harmonyos-references/dataaugmentation-retrieval-api.md#section95236010016)，配置向量数据库和倒排索引数据库的参数，并将这些配置绑定到相应的检索通道中，构建了一个用于多数据源检索的配置对象retrievalConfig。这个配置对象可以被后续的检索操作使用，以从指定的数据库中检索数据。

```
1. getRetrievalConfig(): retrieval.RetrievalConfig {
2. let storeConfigVector: relationalStore.StoreConfig = {
3. name: "testmail_store_vector.db", // VectorBase
4. securityLevel: relationalStore.SecurityLevel.S3,
5. vector: true
6. };

8. let storeConfigInvIdx: relationalStore.StoreConfig = {
9. name: "testmail_store.db", // original db is the inverted index db
10. securityLevel: relationalStore.SecurityLevel.S3,
11. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
12. };

14. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
15. let channelConfigVector: retrieval.ChannelConfig = {
16. channelType: retrieval.ChannelType.VECTOR_DATABASE,
17. context: context,
18. dbConfig: storeConfigVector
19. }
20. let channelConfigInvIdx: retrieval.ChannelConfig = {
21. channelType: retrieval.ChannelType.INVERTED_INDEX_DATABASE,
22. context: context,
23. dbConfig: storeConfigInvIdx
24. }
25. let retrievalConfig: retrieval.RetrievalConfig = {
26. channelConfigs: [channelConfigInvIdx, channelConfigVector]
27. }
28. return retrievalConfig;
29. }
```

[Config.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/Config.ets#L23-L51)

3、配置检索条件[retrieval.RetrievalCondition](../harmonyos-references/dataaugmentation-retrieval-api.md#section4881955192413)，从多个数据源（基于逆向索引和向量相似度）召回相关数据，并通过RRF方法对召回结果进行重排，最终返回5条最相关的记录，在信息检索系统中提升召回率和精确率。

```
1. getRetrivalCondition(): retrieval.RetrievalCondition {
2. let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
3. ftsTableName: "email_inverted",
4. fromClause: "select email_inverted.reference_id as rowid, * from email INNER JOIN email_inverted ON email.id = email_inverted.reference_id",
5. primaryKey: ["chunk_id"],
6. responseColumns: ["reference_id", "chunk_id", "chunk_source", "chunk_text", "subject", "image_text",
7. "attachment_names"],
8. deepSize: 500,
9. recallName: 'invertedvectorRecall',
10. }
11. let floatArray = new Float32Array(128).fill(0.1);
12. let vectorQuery: retrieval.VectorQuery = {
13. column: "repr",
14. value: floatArray,
15. similarityThreshold: 0.1
16. }
17. let recallConditionVector: retrieval.VectorRecallCondition = {
18. vectorQuery: vectorQuery,
19. fromClause: "email_vector",
20. primaryKey: ["id"],
21. responseColumns: ["reference_id", "chunk_id", "chunk_source", "repr"],
22. recallName: "vectorRecall",
23. deepSize: 500
24. }
25. let rerankMethod: retrieval.RerankMethod = {
26. rerankType: retrieval.RerankType.RRF,
27. isSoftmaxNormalized: true,
28. }
29. let retrievalCondition: retrieval.RetrievalCondition = {
30. rerankMethod: rerankMethod,
31. recallConditions: [recallConditionInvIdx, recallConditionVector],
32. resultCount: 5
33. }
34. return retrievalCondition;
35. }
```

[Config.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/Config.ets#L55-L89)

4、配置[LLM会话](../harmonyos-references/dataaugmentation-rag-api.md#section1400115191116)，在HTTP流式响应数据接收事件中进行数据解析，将问题的答案和是否结束封装在answer中传入回调。此步骤会因大模型的选型受到影响，开发中根据实际选择的大模型进行调整。

```
1. export default class MyChatLlm extends rag.ChatLLM {
2. temp: string = '';

4. cancel(): void {
5. LLMHttpUtils.cancel();
6. }

8. async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
9. let ret = rag.LLMRequestStatus.LLM_SUCCESS;
10. try {
11. LLMHttpUtils.on(
12. // data received callback function
13. (data) => {
14. try {
15. if (LLMHttpUtils.isFinished) {
16. return;
17. }
18. let decoder = util.TextDecoder.create(`"utf-8"`);
19. let str = decoder.decodeToString(new Uint8Array(data));
20. let resultStr: string = str.split('\n')[0];
21. if(resultStr.startsWith('{"error_code"')){
22. hilog.error(0, 'MyChatLlm', 'str =' + resultStr);
23. let answer: rag.LLMStreamAnswer = {
24. isFinished: true,
25. chunk: `LLM catch other exception. msg:${resultStr}`,
26. err:{
27. code: 1021011000,
28. name: `LLM catch other exception`,
29. message: `LLM catch other exception. msg:${resultStr}`
30. }
31. }
32. try{
33. let obj = JSON.parse(resultStr) as object;
34. if(obj && obj['error_msg'] && obj['error_code'] && obj['error_msg'] === 'Invalid authorization header.'){
35. answer.chunk = `LLM catch other exception. msg:${obj['error_msg']}`;
36. answer.err!.message = 'Invalid ChatLLM authorization API key';
37. }
38. }
39. catch(err){
40. hilog.error(0, 'MyChatLlm', 'Parse json failed. String: ' + resultStr);
41. }
42. hilog.error(0, 'MyChatLlm', 'LLM catch other exception');
43. LLMHttpUtils.isFinished = true;
44. callback(answer);
45. return;
46. }
47. let obj = JSON.parse(resultStr.slice(5))
48. let chunk = ''
49. if ((obj as object)?.["choices"].length === 0) {
50. return;
51. }
52. if ((obj as object)?.["choices"][0]["delta"]["reasoning_content"]) {
53. chunk = (obj as object)?.["choices"][0]["delta"]["reasoning_content"];
54. } else {
55. chunk = (obj as object)?.["choices"][0]["delta"]["content"];
56. }
57. this.temp += chunk;
58. let isFinished: boolean = (str.length < 20);
59. let answer: rag.LLMStreamAnswer = {
60. isFinished: isFinished,
61. chunk: chunk
62. }
63. LLMHttpUtils.isFinished = isFinished;
64. callback(answer);
65. } catch (err) {
66. hilog.error(0, 'MyChatLlm', `BusinessError, error code: ${err.code}, error message: ${err.message}`);
67. }
68. },
69. // data end callback function
70. () => {
71. if (LLMHttpUtils.isFinished) {
72. return;
73. }
74. let answer: rag.LLMStreamAnswer = {
75. isFinished: true,
76. chunk: ''
77. }
78. LLMHttpUtils.isFinished = true;
79. callback(answer);
80. LLMHttpUtils.end();
81. hilog.warn(0, 'MyChatLlm', 'Recv dataEnd callback.');
82. }
83. );
84. LLMHttpUtils.requestInStream(query);
85. } catch (err) {
86. hilog.error(0, 'MyChatLlm', `Request HuaweiYun failed, error code: ${err.code}, error message: ${err.message}`);
87. if (err.code ===2300028) {
88. ret = rag.LLMRequestStatus.LLM_TIMEOUT;
89. } else if (err.code === 2300007) {
90. ret = rag.LLMRequestStatus.LLM_LOAD_FAILED;
91. } else if (err.code === 9999999) {
92. ret = rag.LLMRequestStatus.LLM_BUSY;
93. } else {
94. ret = rag.LLMRequestStatus.LLM_REQUEST_ERROR;
95. }
96. }
97. return {
98. chatId: 0,
99. status: ret,
100. };
101. }
102. }
```

[MyChatLlm.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/MyChatLlm.ets#L23-L124)

5、在完成检索条件、检索配置、LLM会话的配置后，即可配置[rag.Config](../harmonyos-references/dataaugmentation-rag-api.md#section1033315317182)。

```
1. getRAGConfig(): rag.Config {
2. let retrievalConfig: retrieval.RetrievalConfig = this.getRetrievalConfig();
3. let retrievalCondition: retrieval.RetrievalCondition = this.getRetrivalCondition();
4. let config: rag.Config = {
5. llm: new MyChatLlm(),
6. retrievalConfig: retrievalConfig,
7. retrievalCondition: retrievalCondition,
8. }
9. return config;
10. }
```

[Config.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/viewmodel/Config.ets#L93-L102)

### 开启会话

1、使用[rag.createRagSession()](../harmonyos-references/dataaugmentation-rag-api.md#section14201103320529)接口创建会话，需要传入应用上下文context和[rag.Config](../harmonyos-references/dataaugmentation-rag-api.md#section1033315317182)。

```
1. let config: Config = new GetConfig();
2. let sessionCfg: rag.Config = config.getRAGConfig();
3. // create the rag session
4. rag.createRagSession(this.context, sessionCfg).then((data: rag.RagSession) => {
5. AppStorage.setOrCreate<rag.RagSession>("RagSessionObject", data);
6. }).catch((err: BusinessError) => {
7. hilog.error(DOMAIN, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
8. })
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L62-L69)

2、使用[streamRun()](../harmonyos-references/dataaugmentation-rag-api.md#section178721756950)接口开始会话，需要传入提问的问题、提问选项和处理的动作，接收返回的字符串进行拼接形成答案。

```
1. const answerTypes: Array<rag.StreamType> =
2. [rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER];
3. let option: rag.RunConfig = { answerTypes }
4. this.streamRunStartTime = new Date();
5. hilog.info(0, TAG, `Before streamRun, time: ${this.streamRunStartTime.getTime()}`);
6. let ragSession: rag.RagSession = AppStorage.get<rag.RagSession>("RagSessionObject") as rag.RagSession;
7. await ragSession.streamRun(text, option, this.onReceived);
8. hilog.info(0, TAG, "after streamRun, before responseInStream");
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/RAG_QA/blob/master/entry/src/main/ets/pages/Index.ets#L273-L280)

## 总结

本文介绍了如何使用RAG架构构建问答系统，以提高问答的准确性。在接入RAG架构时，首先需要完成知识库的构建，将原始数据写入数据库中，然后进行LLM的接入，可自由选择大模型，但需要调参以确保回答的准确性和精炼简短，最后按照步骤完成RAG会话的配置与开启。

## 示例代码

* [基于RAG实现智能问答系统](https://gitcode.com/harmonyos_samples/RAG_QA)
