---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-rag-api
title: rag（检索增强生成）
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > ArkTS API > rag（检索增强生成）
category: harmonyos-references
scraped_at: 2026-04-29T13:56:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:76c7e932768589ef49d6342c8c5835dbdc5d6c9e13944cc338e111772d3d92ee
---

本模块提供创建和关闭会话（[RagSession](dataaugmentation-rag-api.md#ragsession)）、流式请求大语言模型（[ChatLLM](dataaugmentation-rag-api.md#chatllm)）以及流式问答（[streamRun](dataaugmentation-rag-api.md#streamrun)）的能力。

**起始版本：** 6.0.0(20)

## 导入模块

PC/2in1

```
1. import { rag } from '@kit.DataAugmentationKit';
```

## LLMStreamAnswer

PC/2in1

大模型流式问答的单次结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isFinished | boolean | 否 | 否 | 表示LLM（Large Language Model，大语言模型）流式输出是否已经结束。true表示已结束，false表示后续还有答案输出。 |
| chunk | string | 否 | 否 | 表示LLM流式输出过程中单轮返回的chunk（被拆分后的文本单元）内容。单轮流式返回结果无固定上限，单次问答所有流式返回结果长度上限为8192字节。 |
| err | [BusinessError](js-apis-base.md#businesserror)<string> | 否 | 是 | 表示LLM流式输出过程中出现的错误。[code](js-apis-base.md#businesserror)取值范围为[1021011000, 1021012000)，超过范围则会报错[1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常)。基类必选参数name和message的长度上限为1000字符，超出部分将被截断。不带本参数则认为无错误发生。 |

## LLMRequestStatus

PC/2in1

流式请求大语言模型请求状态的枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LLM\_SUCCESS | 0 | 请求LLM成功。 |
| LLM\_REQUEST\_ERROR | 1 | 请求错误。 |
| LLM\_LOAD\_FAILED | 2 | LLM加载失败。 |
| LLM\_TIMEOUT | 3 | LLM请求超时。 |
| LLM\_BUSY | 4 | LLM繁忙。 |

## LLMRequestInfo

PC/2in1

流式请求大语言模型请求结果的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| chatId | number | 否 | 否 | 表示大模型的请求ID。取值范围：[0, 2147483647]。 |
| status | [LLMRequestStatus](dataaugmentation-rag-api.md#llmrequeststatus) | 否 | 否 | 表示[streamChat](dataaugmentation-rag-api.md#streamchat)请求的状态。 |

## ChatLLM

PC/2in1

用于请求大模型的抽象类。开发者需继承此类并根据业务逻辑实现各接口逻辑。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

### streamChat

PC/2in1

abstract streamChat(query: string, callback: Callback<LLMStreamAnswer>): Promise<LLMRequestInfo>

流式请求大语言模型，用于与大语言模型交互。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 与大模型交互时的请求内容，根据输入问题、问题预处理、检索等结果动态拼接，最大长度为20000字节。  **说明：** 其中已带有需要带给大模型的提示prompt，无需额外附加内容，且提示prompt中的示例数据均只是提示大模型按照预期输出的模拟数据，无其他额外用途。 |
| callback | Callback<[LLMStreamAnswer](dataaugmentation-rag-api.md#llmstreamanswer)> | 是 | 将与大语言模型交互后得到的结果返回给RAG基础框架的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LLMRequestInfo](dataaugmentation-rag-api.md#llmrequestinfo)> | Promise对象，返回LLM请求信息对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { http } from '@kit.NetworkKit';
3. import { rag } from '@kit.DataAugmentationKit';

5. class MyChatLLM extends rag.ChatLLM {
6. httpRequest: http.HttpRequest | null = http.createHttp();
7. cancel(chatId: number) {
8. // 请开发者按需实现chatId与请求之前的映射关系，取消时请取消chatId相应的请求
9. this.httpRequest?.off('dataReceive');
10. }
11. async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
12. let info: rag.LLMRequestInfo = {
13. chatId: 0,
14. status: rag.LLMRequestStatus.LLM_SUCCESS,
15. };
16. try {
17. // 此处开发者可自行选择想要使用的大语言模型以及对应实现
18. // 假设通过httpRequest.on('dataReceive', callback)从大语言模型得到了答案：
19. let err: BusinessError<string> = {
20. code: 1021011000,  // 自定义错误码，取值范围[1021011000, 1021012000)
21. name: 'Fill custom error name here',  // 超出1000字符部分将被截断
22. message: 'Fill custom error message here'  // 超出1000字符部分将被截断
23. }
24. let answer: rag.LLMStreamAnswer = {
25. isFinished: true,  // 可根据大语言模型回复进行判断，如果是最后一条回复则为true，反之则为false
26. chunk: 'This is the last chunk',
27. err: err
28. }
29. callback(answer);
30. } catch (err) {
31. // 此处示例统一返回LLM_REQUEST_ERROR，开发者可根据需要判断err.code并返回相应LLMRequestStatus
32. info.status = rag.LLMRequestStatus.LLM_REQUEST_ERROR;
33. }
34. return info;
35. }
36. }
```

### cancel

PC/2in1

abstract cancel(chatId: number): void

取消流式请求大语言模型，用于暂停与大语言模型交互。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chatId | number | 是 | 需要被取消的请求LLM的ID。与[streamChat](dataaugmentation-rag-api.md#streamchat)返回值[LLMRequestInfo](dataaugmentation-rag-api.md#llmrequestinfo)中填入的chatId保持一致。取值范围：[0, 2147483647]。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { rag } from '@kit.DataAugmentationKit';

4. class MyChatLLM extends rag.ChatLLM {
5. httpRequest: http.HttpRequest | null = http.createHttp();
6. cancel(chatId: number) {
7. // 请开发者按需实现chatId与请求之前的映射关系，取消时请取消chatId相应的请求
8. this.httpRequest?.off('dataReceive');
9. }
10. async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
11. // 省略streamChat实现，其具体使用见streamChat接口说明
12. return {
13. chatId: 0,
14. status: rag.LLMRequestStatus.LLM_SUCCESS,
15. };
16. }
17. }
```

## Config

PC/2in1

RAG会话的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| llm | [ChatLLM](dataaugmentation-rag-api.md#chatllm) | 否 | 否 | 表示[ChatLLM](dataaugmentation-rag-api.md#chatllm)的提供者。 |
| retrievalConfig | [retrieval.RetrievalConfig](dataaugmentation-retrieval-api.md#retrievalconfig) | 否 | 否 | 表示检索使用的配置。 |
| retrievalCondition | [retrieval.RetrievalCondition](dataaugmentation-retrieval-api.md#retrievalcondition) | 否 | 否 | 表示检索的条件。 |

**示例：**

```
1. import { rag, retrieval } from '@kit.DataAugmentationKit';
2. // MyChatLlm对应文件，是自定义实现的rag.ChatLLM类MyChatLLM所在的文件，具体实现见ChatLLM章节示例
3. import MyChatLLM from './MyChatLlm';

5. let retrievalConfig: retrieval.RetrievalConfig = {
6. channelConfigs: [
7. // 假设已经按需配置
8. ]
9. };

11. let retrievalCondition: retrieval.RetrievalCondition = {
12. recallConditions: [
13. // 假设已经按需配置
14. ]
15. };

17. let config: rag.Config = {
18. llm: new MyChatLLM(),
19. retrievalConfig: retrievalConfig,
20. retrievalCondition: retrievalCondition
21. };
```

## Answer

PC/2in1

流式问答的数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| chunk | string | 否 | 否 | 表示问题摘要的答案。长度上限为8192字节。 |
| data | Array<[retrieval.ItemInfo](dataaugmentation-retrieval-api.md#iteminfo)> | 否 | 是 | 表示检索的匹配结果。最多返回600个chunk。 |

## StreamType

PC/2in1

流式问答回答的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| THOUGHT | 0 | 思考过程数据。 |
| REFERENCE | 1 | 检索到的文档或知识的来源。 |
| ANSWER | 2 | 生成的内容的最终结果。 |

## Stream

PC/2in1

流式问答中一次回答的结果信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [StreamType](dataaugmentation-rag-api.md#streamtype) | 否 | 否 | 表示答案的数据类型。 |
| answer | [Answer](dataaugmentation-rag-api.md#answer) | 否 | 否 | 表示答案的数据。 |
| isFinished | boolean | 否 | 否 | 表示流输出是否结束。true表示本轮问答已结束，false表示本轮本轮问答还有后续回答。 |

## RunConfig

PC/2in1

流式问答的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| answerTypes | Array<[StreamType](dataaugmentation-rag-api.md#streamtype)> | 否 | 否 | 用于指定流式输出的数据类型。 |

## FeedbackInfo

PC/2in1

用户反馈信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| runId | number | 否 | 否 | 会话内特定流式问答的唯一标识符。取值范围：[0, 2147483647]。 |
| score | number | 否 | 否 | 用户对返回答案的评分。取值范围：[1, 5]。 |
| source | Record<[StreamType](dataaugmentation-rag-api.md#streamtype), [Answer](dataaugmentation-rag-api.md#answer)> | 否 | 是 | 用户采用的答案信息。 |
| comment | string | 否 | 是 | 用户反馈的文本信息。长度上限为1000字节。 |

## RagSession

PC/2in1

RAG会话，用以提供基于知识库的智能问答能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

### streamRun

PC/2in1

streamRun(question: string, config: RunConfig, callback: AsyncCallback<Stream>): Promise<number>

流式问答，答案是流式传输的，使用Promise异步回调。不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| question | string | 是 | 表示本次提出的问题。长度上限为1000字节。 |
| config | [RunConfig](dataaugmentation-rag-api.md#runconfig) | 是 | 表示本次提问的配置。 |
| callback | AsyncCallback<[Stream](dataaugmentation-rag-api.md#stream)> | 是 | 回调函数。当流式问答成功，err取值为BusinessError，data为获取到的数据內容；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回本次调用的ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[数据增强错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常) | Insufficient system resources or memory access exception. |
| [1021000001](dataaugmentation-error-code.md#section1021000001-调用llm超时) | A timeout occurred when calling the LLM. |
| [1021000002](dataaugmentation-error-code.md#section1021000002-调用llm加载失败) | A loading failure occurred when calling the LLM. |
| [1021000003](dataaugmentation-error-code.md#section1021000003-调用llm时发生请求失败) | A request failure occurred when calling the LLM. |
| [1021000004](dataaugmentation-error-code.md#section1021000004-llm繁忙) | The LLM chat is busy. |
| [1021000005](dataaugmentation-error-code.md#section1021000005-llm输出不符合约束) | The output of LLM chat does not comply with the constraints. |
| [1021000007](dataaugmentation-error-code.md#section1021000007-rag会话繁忙) | The RAG session is busy. |
| [1021000008](dataaugmentation-error-code.md#section1021000008-rag会话已关闭) | The RAG session is Already closed. |
| [1021000009](dataaugmentation-error-code.md#section1021000009-用户已取消streamrun) | User has canceled the stream run. |
| [1021000010](dataaugmentation-error-code.md#section1021000010-会话中发生超时) | A timeout occurred in the session. |
| [1021000011](dataaugmentation-error-code.md#section1021000011-某些参数不满足约束条件) | Some parameter does not meet the constraints. Possible causes:  1. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.  2. The string parameter contains invalid characters. |
| [1021000012](dataaugmentation-error-code.md#section1021000012-知识库不可用) | The knowledge base is not available. |
| [1021000013](dataaugmentation-error-code.md#section1021000013-retrieval-检索过程中发生错误) | Retrieval: An error occurred during the Retrieval. |
| [1021000014](dataaugmentation-error-code.md#section1021000014-retrieval-存在无效的主键) | Retrieval: There are invalid primary keys. |
| [1021000015](dataaugmentation-error-code.md#section1021000015-retrieval-使用了不支持复合主键的重排序算法) | Retrieval: A re-ranking algorithm that does not support composite primary keys was used. |
| [1021000016](dataaugmentation-error-code.md#section1021000016-retrieval-筛选器输入无效) | Retrieval: The filter input is invalid. |
| [1021000017](dataaugmentation-error-code.md#section1021000017-retrieval-recallcondition中存在无效的召回名称) | Retrieval: There are invalid recall names in RecallCondition. |
| [1021000018](dataaugmentation-error-code.md#section1021000018-retrieval-vectorquery中的向量相似度阈值高于vectorrerankparameter中的分层阈值) | Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter. |
| [1021000019](dataaugmentation-error-code.md#section1021000019-retrieval-rerankmethod参数与通道类型不匹配) | Retrieval: RerankMethod parameters do not match the channel type. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { rag } from '@kit.DataAugmentationKit';
4. import { common } from '@kit.AbilityKit';

6. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
7. let session: rag.RagSession | null; // 需要先使用createRagSession接口创建session
8. let runConfig: rag.RunConfig = {
9. answerTypes: [ rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER ]
10. };
11. let output: string = "";

13. if (session != null) {
14. session.streamRun("提出的问题", runConfig, ((err: BusinessError, stream: rag.Stream) => {
15. if (err) {
16. hilog.error(0, 'test', `streamRun inner failed. code is ${err.code}, message is ${err.message}`);
17. } else {
18. hilog.info(0, 'Index', 'StreamType: %{public}d', stream.type);
19. output += stream.answer.chunk;
20. if (stream.isFinished) {
21. output += "回答结束。";
22. }
23. }
24. })).then((data) => {
25. hilog.info(0, 'Index', 'runId: %{public}d', data);
26. }).catch((e: BusinessError) => {
27. hilog.error(0, 'test', `streamRun failed. code is ${e.code}, message is ${e.message}`);
28. });
29. }
```

### cancel

PC/2in1

cancel(runId: number): Promise<void>

取消本次问答，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| runId | number | 是 | 表示需要取消的问答ID。与[streamRun](dataaugmentation-rag-api.md#streamrun)返回值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[数据增强错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常) | Insufficient system resources or memory access exception. |
| [1021000008](dataaugmentation-error-code.md#section1021000008-rag会话已关闭) | The RAG session is Already closed. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { rag } from '@kit.DataAugmentationKit';

5. let session: rag.RagSession | null; // 需要先使用createRagSession接口创建session

7. if (session != null) {
8. let runId: number = 0;  // 请开发者填入streamRun实际返回值
9. session.cancel(runId).then(() => {
10. hilog.info(0, 'test', 'cancel successfully');
11. }).catch((e: BusinessError) => {
12. hilog.error(0, 'test', `cancel failed. code is ${e.code}, message is ${e.message}`);
13. });
14. }
```

### close

PC/2in1

close(): Promise<void>

关闭会话，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[数据增强错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常) | Insufficient system resources or memory access exception. |

**示例：**

```
1. import { rag } from '@kit.DataAugmentationKit';

3. let session: rag.RagSession | null; // 需要先使用createRagSession接口创建session

5. function WindowStageDestroy(): void {
6. // Main window is destroyed, release UI related resources
7. hilog.info(0, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');

9. if (session != null) {
10. session.close();
11. }
12. }
```

## createRagSession

PC/2in1

createRagSession(context: common.Context, config: Config): Promise<RagSession>

获得一个会话，使用Promise异步回调。不支持多线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 表示当前应用上下文。 |
| config | [Config](dataaugmentation-rag-api.md#config) | 是 | 表示与此[RagSession](dataaugmentation-rag-api.md#ragsession)相关的配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RagSession](dataaugmentation-rag-api.md#ragsession)> | Promise对象，返回[RagSession](dataaugmentation-rag-api.md#ragsession)对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[数据增强错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常) | Insufficient system resources or memory access exception. |
| [1021000006](dataaugmentation-error-code.md#section1021000006-rag会话已存在) | The RAG session already exists. |

**示例：**

```
1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want, common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { rag, retrieval } from '@kit.DataAugmentationKit';
4. import { window } from '@kit.ArkUI';
5. // MyChatLlm对应文件，是自定义实现的rag.ChatLLM类MyChatLLM所在的文件，具体实现见ChatLLM章节示例
6. import MyChatLLM from './MyChatLlm';

8. let session: rag.RagSession | null = null;

10. export default class EntryAbility extends UIAbility {
11. onWindowStageCreate(windowStage: window.WindowStage): void {
12. // Main window is created, set main page for this ability
13. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

15. windowStage.loadContent('pages/Index', (err) => {
16. if (err.code) {
17. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
18. return;
19. }
20. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
21. });

23. let retrievalConfig: retrieval.RetrievalConfig = {
24. channelConfigs: [
25. // 假设已经按需配置
26. ]
27. };

29. let retrievalCondition: retrieval.RetrievalCondition = {
30. recallConditions: [
31. // 假设已经按需配置
32. ]
33. };

35. let config: rag.Config = {
36. llm: new MyChatLLM(),
37. retrievalConfig: retrievalConfig,
38. retrievalCondition: retrievalCondition
39. };

41. rag.createRagSession(this.context, config).then((result) => {
42. session = result;
43. }).catch((err: BusinessError) => {
44. hilog.error(0x0000, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
45. })
46. }
47. }
```

## feedback

PC/2in1

feedback(context: common.Context, feedbackInfo: FeedbackInfo): Promise<void>

接受用户反馈的信息。用户使用问答结束之后，可以使用该接口对回答结果进行上报反馈。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.RAG

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 表示当前应用上下文。 |
| feedbackInfo | [FeedbackInfo](dataaugmentation-rag-api.md#feedbackinfo) | 是 | 表示用户反馈的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[数据增强错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021000000](dataaugmentation-error-code.md#section1021000000-系统资源不足或内存访问异常) | Insufficient system resources or memory access exception. |
| [1021000011](dataaugmentation-error-code.md#section1021000011-某些参数不满足约束条件) | Some parameter does not meet the constraints. Possible causes:  1. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.  2. The string parameter contains invalid characters. |

**示例：**

```
1. import { rag, retrieval } from '@kit.DataAugmentationKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { common } from '@kit.AbilityKit';

5. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;

7. async function feedback() {
8. // 定义ValueType类型的变量
9. let valueTypeA: relationalStore.ValueType = 1
10. let valueTypeRecord: Record<string, relationalStore.ValueType> = {
11. "a": valueTypeA,
12. "b": valueTypeA,
13. }
14. // 定义召回分数
15. let recallScoreA: retrieval.RecallScore = {
16. score: 0,
17. isReverseQuery: false
18. }
19. let recallScoreRecord: Record<string, retrieval.RecallScore> = {
20. "a": recallScoreA,
21. "b": recallScoreA,
22. "c": recallScoreA
23. }

25. let channelTypeRecord: Record<number, Record<string, retrieval.RecallScore>> = {
26. 0: recallScoreRecord,
27. 1: recallScoreRecord
28. }
29. // 定义检索项信息
30. let itemInfo: retrieval.ItemInfo = {
31. primaryKey: '',
32. columns: valueTypeRecord,
33. score: 0,
34. recallScores: channelTypeRecord,
35. features: {
36. "111": 1,
37. "222": 2
38. },
39. similarityLevel: retrieval.SimilarityLevel.LOW
40. }
41. // 定义答案信息
42. let answerB: rag.Answer = {
43. chunk: '111',
44. data: [itemInfo]
45. };
46. // 定义来源信息Record，key为StreamType枚举值
47. let sources: Record<number, rag.Answer> = {
48. 0: answerB,
49. 1: answerB,
50. 2: answerB,
51. }
52. let feedbackInfo: rag.FeedbackInfo = {
53. runId: 444,
54. score: 5,
55. comment: "111222333",
56. source: sources
57. }
58. rag.feedback(context, feedbackInfo);
59. }
```
