---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-demo
title: 完整示例代码
breadcrumb: 指南 > 应用框架 > Data Augmentation Kit（数据增强服务） > RAG > 完整示例代码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:731c88dc5a510484b0f409a5d03b5323a5dd1fe197579146936745539577e628
---

**说明** 

需要完成网络权限的申请，参见：[开发准备](data-augmentation-rag-development.md#开发准备)。

## EntryAbility.ets

应用的生命周期实现在这个文件中，主要在应用启动时进行RagSession、数据库连接的创建，应用关闭时进行RagSession、数据库连接的释放。

```typescript
// src/main/ets/entryability/EntryAbility.ets
import { AbilityConstant, UIAbility, Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import SetUp from '../entryability/SetUp';
import Config from '../entryability/Config';
import { rag } from '@kit.DataAugmentationKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

    AppStorage.setOrCreate<common.UIAbilityContext>('Context', this.context);

    let setUp: SetUp = new SetUp();
    setUp.initTable().then(() => {
      setUp.insertData();
      AppStorage.setOrCreate<SetUp>('SetUpObject', setUp);
    });

    let config: Config = new Config();
    rag.createRagSession(this.context, config.getRAGConfig()).then((data) => {
      AppStorage.setOrCreate<rag.RagSession>('RagSessionObject', data);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', `createRagSession failed, code is ${err.code},message is ${err.message}.`);
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    const session = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
    session?.close().catch(() => {
      hilog.error(DOMAIN, 'testTag', 'close rag session failed');
    });
    const setup = AppStorage.get<SetUp>('SetUpObject') as SetUp;
    setup?.closeStore();
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

## SetUp.ets

SetUp.ets负责数据源的构造，目前实现是从一个自带的Json文件读取数据，并且插入一个开启知识加工开关的数据库中。数据更新成功后，将会自动触发知识加工，形成知识库。

```typescript
// src/main/ets/entryability/SetUp.ets
import { UIAbility, common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';
import { buffer } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SetUp';

export default class SetUp extends UIAbility {
  storeName: string = 'testmail_store.db';  // 与knowledge_schema.json文件中数据库名保持一致
  storeConfig: relationalStore.StoreConfig = {
    name: this.storeName,
    securityLevel: relationalStore.SecurityLevel.S3,
    enableSemanticIndex: true,  // 源数据库需配置该项为true才会触发知识加工
    tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
  };
  store?: relationalStore.RdbStore;

  async getStore() {
    try {
      if (!this.store) {
        let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // 获取全局context
        this.store = await relationalStore.getRdbStore(context, this.storeConfig);
      }
    } catch (err) {
      hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
    }
    return this.store;
  }

  async initTable() {
    try {
      const tmpStore = await this.getStore();
      const createTableSql = 'CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, content text, ' +
        'image_text text, attachment_names text, inline_files text, sender text, receivers text, received_date text);';
      await tmpStore?.execute(createTableSql, 0, undefined);
      hilog.info(0, TAG, 'InitTable success');
    } catch (err) {
      hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
    }
  }

  async insertData() {
    try {
      let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // 获取全局context
      const fileList = context.resourceManager.getRawFileListSync('');
      let dataIndex = 0;
      for (let file of fileList) {  // 从json文件中解析数据到数据库中
        if (!file.startsWith('sourceData') || !file.endsWith('.json')) {
          hilog.info(0, TAG, `file ${file} skip`);
          continue;
        }
        hilog.info(0, TAG, `file ${file} start`);
        try {
          const rawFileData = await context.resourceManager.getRawFileContent(file);
          const fileData: string = buffer.from(rawFileData).toString();
          const resultObjArr = JSON.parse(fileData) as Array<object>;
          let jsonObj: object | undefined;
          for (let i = 0; i < resultObjArr.length; i++) {
            try {
              jsonObj = resultObjArr[i];
              let sender: string = jsonObj?.['sender_name'];
              if (!sender || sender.length == 0) {
                sender = 'undefined';
              }
              const receiverStr: string = JSON.stringify(jsonObj['to']);
              const formattedDateStr: string = jsonObj?.['received_time']?.replace(' ', 'T');
              let received_date = Date.parse(formattedDateStr);
              if (!received_date || Number.isNaN(received_date)) {
                received_date = 0;
              }
              let subject: string = jsonObj?.['subject']?.replace(/'/g, '');
              let doc: string = jsonObj?.['body']?.replace(/'/g, '');
              let sql = `insert or replace into email VALUES(${dataIndex}, '${subject}', '${doc}', '',` +
                ` '', '', '${sender}', '${receiverStr}', '${received_date}');`
              const tmpStore = await this.getStore();
              await tmpStore?.executeSql(sql);
              dataIndex++;
            } catch (e) {
              hilog.error(0, TAG, `Insert failed, code is ${e.code},message is ${e.message}, jsonObj: ${jsonObj}`);
            }
          }
        } catch (e) {
          hilog.error(0, TAG, `Load file failed, code is ${e.code},message is ${e.message}`);
        }
        hilog.info(0, TAG, `file ${file} end`);
      }
      hilog.info(0, TAG, 'insertData end');
    } catch (err) {
      hilog.error(0, TAG, `Init DB failed, code is ${err.code},message is ${err.message}.`);
    }
  }

  async closeStore() {
    try {
      await this.store?.close();
    } catch (e) {
      hilog.error(0, TAG, `Close store failed, code is ${e.code},message is ${e.message}.`);
    }
  }
}
```

## HttpUtils.ets

HttpUtils.ets是与大模型交互的Http工具类，主要负责发往大模型的报文拼装、流式Http消息接收回调的注册等。开发者需根据自身资源，选用合适的大模型。示例代码使用的是[ModelArts](https://console.huaweicloud.com/modelarts)，需要把其中的"\*\*\*\*replace your API key in here\*\*\*\*"替换为真实的API Key。

```typescript
// src/main/ets/entryability/HttpUtils.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'HttpUtils';

class HttpUtils {
  httpRequest?: http.HttpRequest;
  url: string = 'https://api.modelarts-maas.com/v1/chat/completions'; // 开发者需要根据选择的大模型对应修改url以及下面的model
  isFinished: boolean = false;

  initOption(question: string) {
    let option: http.HttpRequestOptions = {
      // 请求方式
      method: http.RequestMethod.POST,
      // 请求头
      header: {
        'Content-Type': 'application/json',
        // API-KEY from Model
        'Authorization': `Bearer ****replace your API key in here****`
      },
      // 请求体
      extraData: {
        'stream': true,
        'temperature': 0.1,
        'max_tokens': 1000,
        'frequency_penalty': 1,
        'model': 'qwen3-32b',
        'top_p': 0.1,
        'presence_penalty': -1,
        'messages': JSON.parse(question),
        "chat_template_kwargs": {
          // 关闭思考中数据
          "enable_thinking": false
        }
      }
    };
    return option;
  }

  async requestInStream(question: string) { // 拼装流式请求的option并发起流式请求
    if (!this.httpRequest) {
      this.httpRequest = http.createHttp();
    }
    this.httpRequest?.requestInStream(this.url, this.initOption(question)).catch((err: BusinessError) => {
      hilog.error(0, TAG, 'Failed to request. Cause: %{public}s', JSON.stringify(err));
    });
    this.isFinished = false;
  }

  on(callback: Callback<ArrayBuffer>) { // 注册数据接受、数据结束的监听
    if (!this.httpRequest) {
      this.httpRequest = http.createHttp();
    }
    this.httpRequest.on('dataReceive', callback);
  }

  end() { // 取消注册数据接受、数据结束的监听，释放httpRequest
    this.httpRequest?.off('dataReceive');
    this.httpRequest?.destroy();
    this.httpRequest = undefined;
  }

  cancel() {
    this.httpRequest?.off('dataReceive');
    this.httpRequest?.destroy();
    this.httpRequest = undefined;
  }
}

export default new HttpUtils;
```

## MyChatLlm.ets

应用继承实现ChatLLM类，相当于应用侧实现的大模型客户端，将在创建RagSession的时候把这个大模型客户端作为入参传入RagSession中。

```typescript
// src/main/ets/entryability/MyChatLlm.ets
import { rag } from '@kit.DataAugmentationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { JSON, util } from '@kit.ArkTS';
import HttpUtils from './HttpUtils';

const TAG = "MyChatLLM";

function parseLLMResponse(data: ArrayBuffer): rag.LLMStreamAnswer | undefined {
  try {
    let decoder = util.TextDecoder.create(`"utf-8"`);
    let str = decoder.decodeToString(new Uint8Array(data));
    hilog.info(0, TAG, str);
    let chunk = '';
    let isFinished: boolean = (str.length < 20);
    for (let resultStr of str.split('data:')) {
      if (resultStr.trim() == ('[DONE]')) {
        isFinished = true;
        break;
      }
      if (resultStr.trim().length == 0) {
        continue;
      }
      try {
        let obj = JSON.parse(resultStr.trim());
        if ((obj as object)?.['choices'].length === 0) {
          continue;
        }
        if ((obj as object)?.['choices'][0]?.['delta']?.['reasoning_content']) {
          chunk += (obj as object)?.['choices'][0]['delta']['reasoning_content'];
        } else if ((obj as object)?.['choices'][0]?.['delta']?.['content']) {
          chunk += (obj as object)?.['choices'][0]['delta']['content'];
        }
      } catch (err) {
        hilog.error(0, TAG, `Parse LLM response failed, resultStr: ${resultStr}`);
      }
    }
    let answer: rag.LLMStreamAnswer = {
      isFinished: isFinished,
      chunk: chunk
    };
    return answer;
  } catch (err) {
    hilog.error(0, TAG, `Parse LLM response failed, error code: ${err.code}, error message: ${err.message}`);
  }
  return undefined;
}

export default class MyChatLLM extends rag.ChatLLM {
  async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
    let ret: rag.LLMRequestStatus = rag.LLMRequestStatus.LLM_SUCCESS;
    try {
      let dataCallback = async (data: ArrayBuffer) => { // 收到数据时的回调函数，解析数据并组装LLMStreamAnswer，通过callback回调
        hilog.debug(0, TAG, 'on callback enter. data length: %{public}d', data.byteLength);
        // 解析大模型返回报文，逻辑因选择模型而异
        const answer = parseLLMResponse(data);
        if (!answer) {
          return;
        }
        HttpUtils.isFinished = answer.isFinished;
        callback(answer);
        hilog.debug(0, 'MyChatLLM', 'Request LLM success. isFinished: %{public}s, data: %{public}s',
          Number(answer.isFinished).toString(), answer.chunk);
      };

      HttpUtils.on(dataCallback);
      HttpUtils.requestInStream(query);
    } catch (err) {
      hilog.error(0, TAG, `Request LLM failed, error code: ${err.code}, error message: ${err.message}`);
      ret = rag.LLMRequestStatus.LLM_REQUEST_ERROR; // 开发者可判断错误码从而返回其他LLM错误码
    }
    return {
      chatId: 0,
      status: ret,
    };
  }
  cancel(chatId: number): void {
    hilog.info(0, TAG, `The request for the large model has been canceled. chatId: ${chatId}`);
    HttpUtils.cancel();
  }
}
```

## Config.ets

Config.ets主要负责RagSession创建时入参的组装。详细配置方法及含义可参见[智慧化数据检索](dataaugmentation-retrieval.md)。

```typescript
// src/main/ets/entryability/Config.ets
import { common, UIAbility } from '@kit.AbilityKit';
import { rag, retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import MyChatLlm from './MyChatLlm';

export default class Config extends UIAbility {
  getRetrievalConfig() {
    let storeConfigVector: relationalStore.StoreConfig = {
      name: 'testmail_store_vector.db', // 知识加工后向量数据库文件名，在原数据库名基础上加_vector后缀
      securityLevel: relationalStore.SecurityLevel.S3,
      vector: true  // 向量数据库应设置该项为true
    };

    let storeConfigInvIdx: relationalStore.StoreConfig = {
      name: 'testmail_store.db', // 知识加工后，倒排数据库即原数据库
      securityLevel: relationalStore.SecurityLevel.S3,
      tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
    };

    let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext;
    let channelConfigVector: retrieval.ChannelConfig = {
      channelType: retrieval.ChannelType.VECTOR_DATABASE,
      context: context,
      dbConfig: storeConfigVector
    };
    let channelConfigInvIdx: retrieval.ChannelConfig = {
      channelType: retrieval.ChannelType.INVERTED_INDEX_DATABASE,
      context: context,
      dbConfig: storeConfigInvIdx
    };
    let retrievalConfig: retrieval.RetrievalConfig = {
      channelConfigs: [channelConfigInvIdx, channelConfigVector]
    };
    return retrievalConfig;
  }

  getRetrivalCondition() {
    let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
      ftsTableName: 'email_inverted',
      fromClause: 'email_inverted',
      primaryKey: ['chunk_id'],
      responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'chunk_text'],
      deepSize: 500,
      recallName: 'invertedvectorRecall',
    };
    let floatArray = new Float32Array(128).fill(0.1);
    let vectorQuery: retrieval.VectorQuery = {
      column: 'repr',
      value: floatArray,
      similarityThreshold: 0.1
    };
    let recallConditionVector: retrieval.VectorRecallCondition = {
      vectorQuery: vectorQuery,
      fromClause: 'email_vector',
      primaryKey: ['id'],
      responseColumns: ['reference_id', 'chunk_id', 'chunk_source', 'repr'],
      recallName: 'vectorRecall',
      deepSize: 500
    };
    let rerankMethod: retrieval.RerankMethod = {
      rerankType: retrieval.RerankType.RRF,
      isSoftmaxNormalized: true,
    };
    let retrievalCondition: retrieval.RetrievalCondition = {
      rerankMethod: rerankMethod,
      recallConditions: [recallConditionInvIdx, recallConditionVector],
      resultCount: 5
    };
    return retrievalCondition;
  }

  getRAGConfig() {
    let retrievalConfig: retrieval.RetrievalConfig = this.getRetrievalConfig();
    let retrievalCondition: retrieval.RetrievalCondition = this.getRetrivalCondition();
    let config: rag.Config = {
      llm: new MyChatLlm(),
      retrievalConfig: retrievalConfig,
      retrievalCondition: retrievalCondition
    };
    return config;
  }
}
```

## Index.ets

应用界面功能的实现包含：输入问 入框、开始问答的按钮、答案输出的输出框。

```typescript
// src/main/ets/pages/Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';
import hilog from '@ohos.hilog';

@Entry
@Component
struct Index {
  @State inputStr: string = '知识问答开发指南完整示例代码';
  @State answerStr: string = '';
  @State thoughtStr: string = '';

  build() {
    Column() {
      Row({ space: 8 }) {
        TextArea({ text: this.inputStr, placeholder: 'Input question here!' })
          .margin({ top: 8 })
          .borderStyle(BorderStyle.Dotted)
          .onChange((newValue) => {
            this.inputStr = newValue;
          })
          .width('95%')
          .height('15%')
          .fontWeight(FontWeight.Bold)
      }

      Button('streamRun')
        .onClick(async () => {
          // 获取创建的RagSession
          let session: rag.RagSession = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
          let config: rag.RunConfig = {
            // 指定流式输出的输出类型
            answerTypes: [rag.StreamType.THOUGHT, rag.StreamType.ANSWER]
          };
          this.thoughtStr = '';
          this.answerStr = '';
          // 发起提问
          session.streamRun(this.inputStr, config, ((err: BusinessError, stream: rag.Stream) => {
            // 接收答案的callback回调，处理答案信息
            if (err) {
              this.answerStr = `streamRun inner failed. code is ${err.code}, message is ${err.message}`;
            } else {
              // 根据不同的数据类型，选择不同的处理方式
              switch (stream.type) {
                case rag.StreamType.THOUGHT:
                  this.thoughtStr += stream.answer.chunk;
                  break;
                case rag.StreamType.ANSWER:
                  this.answerStr += stream.answer.chunk;
                  break;
                case rag.StreamType.REFERENCE:
                default:
                  hilog.info(0, 'Index', `streamRun msg: ${JSON.stringify(stream)}`);
              }
            }
          })).catch((e: BusinessError) => {
            this.answerStr = `streamRun failed. code is ${e.code}, message is ${e.message}`;
          });
        })
        .width('30%')
        .height('5%')
      Column({ space: 2 }) {
        Text(this.thoughtStr)
          .fontSize(12)
          .fontColor(Color.Gray)
          .padding(8)
          .width('95%')
          .height('auto')
        Text(this.answerStr)
          .padding(8)
          .width('95%')
          .height('auto')
      }
      .backgroundColor(0xF5DEB3)
      .width('95%')
      .height('75%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## knowledge\_schema.json

知识加工的schema文件用来定义知识加工时对于源数据库的处理逻辑。

```text
// src/main/resources/rawfile/arkdata/knowledge/knowledge_schema.json ------ 实际使用时请删除本行注释
{
  "knowledgeSource": [{
    "version": 1,
    "dbName": "testmail_store.db",
    "tables": [{
      "tableName": "email",
      "referenceFields": ["id"],
      "knowledgeFields": [{
        "columnName": "subject",
        "type": ["Text"]
      },
      {
        "columnName": "content",
        "type": ["Text"]
      },
      {
        "columnName": "image_text",
        "type": ["Text"]
      },
      {
        "columnName": "attachment_names",
        "type": ["Text"]
      },
      {
    "columnName": "inline_files",
    "type": ["Json"],
    "parser": [
      {
        "type": "File",
        "path": "$[*].uri"
      }
    ]
      },
      {
        "columnName": "sender",
        "type": ["Scalar"],
        "description": "sender"
      },
      {
        "columnName": "receivers",
        "type": ["Scalar"],
        "description": "receivers"
      },
      {
        "columnName": "received_date",
        "type": ["Scalar"],
        "description": "received_date"
      }]
    }]
  }]
}
```

## sourceData.json

sourceData.json文件中的内容为模拟数据源，作为输入插入应用数据库表。真实情况应用数据输入途径应该是界面输入、服务器获取等。

```text
// src/main/resources/rawfile/sourceData.json ------ 仅用于测试数据插入，请开发者根据业务需要预置数据库数据
[{
  "subject": "【请阅】手机优惠政策",
  "sender_name": "test1",
  "sender_email": "test1@example.com",
  "received_time": "2025-05-15 15:49:04.135",
  "recipients": [
    {
      "Address": "test2@example.com",
      "name": "test2",
      "Type": 1
    },
    {
      "Address": "test3@example.com",
      "name": "test3",
      "Type": 2
    },
    {
      "Address": "test4@example.com",
      "name": "test4",
      "Type": 3
    }
  ],
  "to": [
    "lisi"
  ],
  "cc": [
    "wangwu"
  ],
  "bcc": [
    "zhaoliu"
  ],
  "attachment": [],
  "body": "优惠政策：\r\n旗舰系列优惠10%！！ 非旗舰系列优惠20%！！。",
  "unread": false
}]
```
