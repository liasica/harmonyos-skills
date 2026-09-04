---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-development
title: 知识问答
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > 知识问答
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:13+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5108b1cc78a91b8f8caffa3d19b51307d5e15c82cfc7b93fdc4acd1eae862fcd
---

知识问答是通过检索增强生成（RAG）技术，从数据源中精准提取信息并生成答案的智能交互方式。可用于企业客服、医疗辅助、IT支持等领域。

## 约束限制

1. 知识问答需要先对数据源库进行[知识加工](data-augmentation-knowledge-processing.md)生成知识库，否则无法问答。
2. 用户问答时，RAG可使用的历史记录范围为最近1次问答内容。
3. RAG不提供敏感词风控检测能力，开发者需要自行对用户输入内容和RAG返回内容进行敏感词风控检测。
4. 开发者应选择上下文长度至少应该为30k Tokens的LLM，如Qwen2.5-7B-32K、Mistral-7B-Instruct-v0.2、Llama-3.1-8B等。否则可能会因大模型上下文长度超限而导致知识问答失败。
5. LLM由开发者自行选择，问答支持的语言受选择的LLM影响。

## 接口说明

**说明** 

接口需在页面或自定义组件生命周期内调用。

RAG关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/dataaugmentation-rag-api.md#导入模块)。除接口外，还可以通过配置文件进行深度定制RAG，详见[RAG配置](data-augmentation-config-prompt-template.md)。

| 接口名 | 描述 |
| --- | --- |
| abstract [streamChat](../harmonyos-references/dataaugmentation-rag-api.md#streamchat)(query: string, callback: Callback<[LLMStreamAnswer](../harmonyos-references/dataaugmentation-rag-api.md#llmstreamanswer)>): Promise<[LLMRequestInfo](../harmonyos-references/dataaugmentation-rag-api.md#llmrequestinfo)> | 继承ChatLLM类实现大模型客户端时需要实现的函数。RAG在检索前的问题预处理、检索后的回答生成时，会调用这个函数与大语言模型交互。 |
| [createRagSession](../harmonyos-references/dataaugmentation-rag-api.md#createragsession)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), config: [Config](../harmonyos-references/dataaugmentation-rag-api.md#config)): Promise<[RagSession](../harmonyos-references/dataaugmentation-rag-api.md#ragsession)> | 获得一个会话用于进行知识问答。不支持多线程调用。 |
| [streamRun](../harmonyos-references/dataaugmentation-rag-api.md#streamrun)(question: string, config: [RunConfig](../harmonyos-references/dataaugmentation-rag-api.md#runconfig), callback: AsyncCallback<[Stream](../harmonyos-references/dataaugmentation-rag-api.md#stream)>): Promise<number> | 知识问答接口，传入问题以及问答配置项。当RAG生成问题结果时，触发callback回调函数来流式传递数据。支持的长度为1000个字符内（UTF-8下一个汉字占3个字符）。不支持多线程调用。 |

## 开发准备

1. 申请网络权限。[streamChat](../harmonyos-references/dataaugmentation-rag-api.md#streamchat)中需要开发者实现与LLM交互的功能，因此需要为应用申请网络权限。

   ```json5
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ],
   ```
2. 完成知识加工配置。请参考[知识加工](data-augmentation-knowledge-processing.md)。

## 开发步骤

下面仅对关键步骤关键代码进行片段式说明，省略了很多非核心代码，如果需要查看完整功能示例代码，请参考[示例代码](data-augmentation-rag-demo.md)。应用的一次流式问答过程，和RagSession、ChatLLM、知识库的交互流程，可参考[流式问答调用流程图](data-augmentation-rag-development.md#流式问答调用流程图)。

1. 导入@kit.DataAugmentationKit模块，其余依赖需要开发者按需添加。

   ```typescript
   import { rag } from '@kit.DataAugmentationKit';
   ```
2. 创建http工具类，用以和大模型交互，用户也可选择webSocket（可参考[Network Kit](../harmonyos-references/network-api-arkts.md)）或者其他方式与大模型交互。本示例选用了[ModelArts平台](https://console.huaweicloud.com/modelarts)的qwen3-235b-a22b模型作为示例，开发者使用时需根据实际情况选择合适大模型。示例代码包括如下三个环节：

   * 拼装和大模型交互的请求报文，推荐为流式交互，以获得更好用户体验。
   * 注册大模型的数据接收及输出结束的回调函数，以达到流式访问大模型的效果。
   * 初始化大模型以及向大模型发送请求。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { http } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   class LLMHttpUtils {

     public httpRequest: http.HttpRequest | null = null;
     // url网址：https://api.modelarts-maas.com/v2/chat/completions
     public url: string = 'xxxxxxxxxxxxxx';
     public isFinished: boolean = false;

     initOption(question: string) {
       let option: http.HttpRequestOptions = {
         method: http.RequestMethod.POST,
         header: {
           'Content-Type': 'application/json',
           // 模型API-KEY
           'Authorization': 'Bearer xxxxxxxxx'
         },
         extraData: {
           'stream': true,
           'temperature': 0.1,
           'max_tokens': 10000,
           'frequency_penalty': 1,
           'model': 'qwen3-235b-a22b',
           'top_p': 0.1,
           'presence_penalty': -1,
           'messages': JSON.parse(question)
         }
       };
       return option;
     }

     async requestInStream(question: string) {
       if (this.httpRequest === null) {
         this.httpRequest = http.createHttp();
       }
       this.httpRequest.requestInStream(this.url, this.initOption(question)).catch((err: BusinessError) => {
         hilog.error(0x0000, 'LLMHttpUtils', `requestInStream failed, error code=${err.code}, message=${err.message}`);
       });
       this.isFinished = false;
     }

     on(callback: Callback<ArrayBuffer>, endCallback: Callback<void>) {
       if (this.httpRequest === null) {
         this.httpRequest = http.createHttp();
       }
       this.httpRequest.on('dataReceive', callback);
       this.httpRequest.on('dataEnd', endCallback);
     }

     end() {
       this.httpRequest?.off('dataReceive');
       this.httpRequest?.off('dataEnd');
       this.httpRequest?.destroy();
       this.httpRequest = null;
     }

     cancel() {
       this.httpRequest?.off('dataReceive');
       this.httpRequest?.off('dataEnd');
       this.httpRequest?.destroy();
       this.httpRequest = null;
     }
   }

   export default new LLMHttpUtils;
   ```
3. 继承实现[ChatLLM](../harmonyos-references/dataaugmentation-rag-api.md#chatllm)类，在此函数中与大模型进行交互，并将大模型返回结果通过callback函数返回给RagSession。

   ```typescript
   import rag from '@hms.data.rag'
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { util, JSON } from '@kit.ArkTS';

   import LLMHttpUtils from '../common/utils/LLMHttpUtils'

   export default class MyChatLlm extends rag.ChatLLM {
     public temp: string = '';

     cancel(): void {
       LLMHttpUtils.cancel();
     }

     async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
       let ret = rag.LLMRequestStatus.LLM_SUCCESS;
       try {
         LLMHttpUtils.on(
           (data) => {
             try {
               if (LLMHttpUtils.isFinished) {
                 return;
               }
               let decoder = util.TextDecoder.create(`"utf-8"`);
               let str = decoder.decodeToString(new Uint8Array(data));
               let resultStr: string = str.split('\n')[0];
               if(resultStr.startsWith('{"error_code"')){
                 hilog.error(0, 'MyChatLlm', 'str =' + resultStr);
                 let answer: rag.LLMStreamAnswer = {
                   isFinished: true,
                   chunk: `LLM catch other exception. msg:${resultStr}`,
                   err:{
                     code: 1021011000,
                     name: `LLM catch other exception`,
                     message: `LLM catch other exception. msg:${resultStr}`
                   }
                 }
                 try{
                   let obj = JSON.parse(resultStr) as object;
                   if(obj && obj['error_msg'] && obj['error_code'] && obj['error_msg'] === 'Invalid authorization header.'){
                     answer.chunk = `LLM catch other exception. msg:${obj['error_msg']}`;
                     answer.err!.message = 'Invalid ChatLLM authorization API key';
                   }
                 } catch(err){
                   hilog.error(0, 'MyChatLlm', 'Parse json failed. String: ' + resultStr);
                 }
                 hilog.error(0, 'MyChatLlm', 'LLM catch other exception');
                 LLMHttpUtils.isFinished = true;
                 callback(answer);
                 return;
               }
               let obj = JSON.parse(resultStr.slice(5))
               let chunk = ''
               if ((obj as object)?.['choices'].length === 0) {
                 return;
               }
               if ((obj as object)?.['choices'][0]['delta']['reasoning_content']) {
                 chunk = (obj as object)?.['choices'][0]['delta']['reasoning_content'];
               } else {
                 chunk = (obj as object)?.['choices'][0]['delta']['content'];
               }
               this.temp += chunk;
               let isFinished: boolean = (str.length < 20);
               let answer: rag.LLMStreamAnswer = {
                 isFinished: isFinished,
                 chunk: chunk
               }
               LLMHttpUtils.isFinished = isFinished;
               callback(answer);
             } catch (err) {
               hilog.error(0, 'MyChatLlm', `BusinessError, error code: ${err.code}, error message: ${err.message}`);
             }
           },
           () => {
             if (LLMHttpUtils.isFinished) {
               return;
             }
             let answer: rag.LLMStreamAnswer = {
               isFinished: true,
               chunk: ''
             }
             LLMHttpUtils.isFinished = true;
             callback(answer);
             LLMHttpUtils.end();
             hilog.warn(0, 'MyChatLlm', 'Recv dataEnd callback.');
           }
         );
         LLMHttpUtils.requestInStream(query);
       } catch (err) {
         hilog.error(0, 'MyChatLlm', `Request HuaweiYun failed, error code: ${err.code}, error message: ${err.message}`);
         if (err.code ===2300028) {
           ret = rag.LLMRequestStatus.LLM_TIMEOUT;
         } else if (err.code === 2300007) {
           ret = rag.LLMRequestStatus.LLM_LOAD_FAILED;
         } else if (err.code === 9999999) {
           ret = rag.LLMRequestStatus.LLM_BUSY;
         } else {
           ret = rag.LLMRequestStatus.LLM_REQUEST_ERROR;
         }
       }
       return {
         chatId: 0,
         status: ret,
       };
     }
   }
   ```
4. 创建[Config](../harmonyos-references/dataaugmentation-rag-api.md#config)配置中的属性。下面简要介绍几个主要属性，有关全量配置字段的详细含义，请参见[智慧化数据检索](dataaugmentation-retrieval.md)中的说明。开发者可以根据自身需求进行选择性配置。

   * [RetrievalConfig](../harmonyos-references/dataaugmentation-retrieval-api.md#retrievalconfig)主要配置知识库的数据库配置。[知识加工](data-augmentation-knowledge-processing.md)将会生成向量及倒排两种知识库表。

     ```typescript
     getRetrievalConfig(): retrieval.RetrievalConfig {
       let storeConfigVector: relationalStore.StoreConfig = {
         name: 'testmail_store_vector.db', // VectorBase
         securityLevel: relationalStore.SecurityLevel.S3,
         vector: true
       };

       let storeConfigInvIdx: relationalStore.StoreConfig = {
         name: 'testmail_store.db', // 原始数据库即为倒排索引数据库。
         securityLevel: relationalStore.SecurityLevel.S3,
         tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
       };

       let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext;
       let channelConfigVector: retrieval.ChannelConfig = {
         channelType: retrieval.ChannelType.VECTOR_DATABASE,
         context: context,
         dbConfig: storeConfigVector
       }
       let channelConfigInvIdx: retrieval.ChannelConfig = {
         channelType: retrieval.ChannelType.INVERTED_INDEX_DATABASE,
         context: context,
         dbConfig: storeConfigInvIdx
       }
       let retrievalConfig: retrieval.RetrievalConfig = {
         channelConfigs: [channelConfigInvIdx, channelConfigVector]
       }
       return retrievalConfig;
     }
     ```
   * [RetrievalCondition](../harmonyos-references/dataaugmentation-retrieval-api.md#retrievalcondition)主要配置检索条件及多路召回之后的排序配置。其中fromClause为查询目标索引名，可按照如下示例代码配置为业务数据库表及知识加工产生的数据库表联合形成的虚拟表；responseColumns为召回的字段集合，范围为fromClause配置的数据库表中的列。关于知识库的数据库表结构可参见：[知识加工](data-augmentation-knowledge-processing.md)。

     ```typescript
     getRetrivalCondition(): retrieval.RetrievalCondition {
       let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
         ftsTableName: 'email_inverted',
         fromClause: 'email_inverted',
         primaryKey: ['chunk_id'],
         responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'chunk_text'],
         deepSize: 500,
         recallName: 'invertedvectorRecall',
       }
       let floatArray = new Float32Array(128).fill(0.1);
       let vectorQuery: retrieval.VectorQuery = {
         column: 'repr',
         value: floatArray,
         similarityThreshold: 0.1
       }
       let recallConditionVector: retrieval.VectorRecallCondition = {
         vectorQuery: vectorQuery,
         fromClause: 'email_vector',
         primaryKey: ['id'],
         responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'repr'],
         recallName: 'vectorRecall',
         deepSize: 500
       }
       let rerankMethod: retrieval.RerankMethod = {
         rerankType: retrieval.RerankType.RRF,
         isSoftmaxNormalized: true,
       }
       let retrievalCondition: retrieval.RetrievalCondition = {
         rerankMethod: rerankMethod,
         recallConditions: [recallConditionInvIdx, recallConditionVector],
         resultCount: 5
       }
       return retrievalCondition;
     }
     ```
   * 完成Config数据的构造。[ChatLLM](../harmonyos-references/dataaugmentation-rag-api.md#chatllm)参数则使用步骤3继承实现的ChatLLM的自定义的类的实例。

     ```typescript
     getRAGConfig(): rag.Config {
       let retrievalConfig: retrieval.RetrievalConfig = this.getRetrievalConfig();
       let retrievalCondition: retrieval.RetrievalCondition = this.getRetrivalCondition();
       let config: rag.Config = {
         llm: new MyChatLlm(),
         retrievalConfig: retrievalConfig,
         retrievalCondition: retrievalCondition,
       }
       return config;
     }
     ```
5. 创建RagSession。

   ```typescript
   let config: Config = new GetConfig();
   let sessionCfg: rag.Config = config.getRAGConfig();
   AppStorage.setOrCreate<rag.Config>('config', sessionCfg);
   // 创建 RAG 会话
   rag.createRagSession(this.context, sessionCfg).then((data: rag.RagSession) => {
     AppStorage.setOrCreate<rag.RagSession>('RagSessionObject', data);
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
   })
   ```
6. 使用步骤5创建的RagSession的streamRun()函数进行问答。

   * answerTypes属性用来指定流式输出的数据类型（[StreamType](../harmonyos-references/dataaugmentation-rag-api.md#streamtype)），当前示例代码配置了三种数据类型，所以最终streamRun()函数的callback回调函数将会输出这三种类型的数据。
   * streamRun()函数以增量流式的方式输出数据，所以需要开发者自行对结果进行拼接。

   ```typescript
   const answerTypes: rag.StreamType[] =
     [rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER];
   let option: rag.RunConfig = { answerTypes }
   this.streamRunStartTime = new Date();
   hilog.info(0, TAG, `Before streamRun, time: ${this.streamRunStartTime.getTime()}`);
   let ragSession: rag.RagSession = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
   await ragSession.streamRun(text, option, this.onReceived);
   hilog.info(0, TAG, 'after streamRun, before responseInStream');
   ```

## 流式问答调用流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/SQcVQAO9QsmC01xf5rcFaQ/zh-cn_image_0000002742123293.png)
