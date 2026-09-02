---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api
title: knowledgeProcessor（知识加工）
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > ArkTS API > knowledgeProcessor（知识加工）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:48bfd438321e13f4d95204d798fc9af966d0f5349cb02c28e8a5a0b08ac8d2c6
---

本模块提供获取知识加工对象（KnowledgeProcessor）以及获取知识加工状态（ProcessorStatus）的能力。

由于知识加工能力依赖的嵌入模型只支持在PC/2in1部署，因此当前知识加工能力仅支持PC/2in1设备。在其他设备类型中不可用会抛出异常。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
```

## getKnowledgeProcessor

getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>

获取知识加工对象，用于获取知识加工状态等操作。使用promise异步回调。

在schema升级场景下，首次开库或调用getKnowledgeProcessor接口前需调用[cleanKnowledgeData](dataaugmentation-knowledgeprocessor-api.md#cleanknowledgedata)接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.BaseContext](js-apis-inner-application-basecontext.md) | 是 | 知识加工对象的上下文。 |
| config | [KnowledgeProcessorConfig](dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig) | 是 | 知识加工配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KnowledgeProcessor](dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessor)> | Promise对象，返回知识加工对象。该对象可用于获取知识加工状态（getStatus）、启动知识加工（startProcess）和停止知识加工（stopProcess）等操作。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1021400000](errorcode-dataaugmentation.md#section1021400000-内部错误) | Internal error. |
| [1021400001](errorcode-dataaugmentation.md#section1021400001-知识源未配置) | The knowledge source is not configured. |
| [1021400002](errorcode-dataaugmentation.md#section1021400002-知识schema文件不存在) | The knowledge schema file is not found. |
| [1021400003](errorcode-dataaugmentation.md#section1021400003-知识schema内容不合法) | The knowledge schema content is invalid. |
| [1021400004](errorcode-dataaugmentation.md#section1021400004-操作rdb数据源时发生错误) | An error occurred during operations on the RDB source. |

**示例：**

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 获取知识加工器的异步函数
async function getProcessor() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    return processor;
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}
```

## cleanKnowledgeData

cleanKnowledgeData(context: common.Context, config: KnowledgeProcessorConfig): Promise<void>

根据入参中的知识加工配置获取对应知识库信息，将对应知识库进行清空。使用promise异步回调。

在schema升级场景下，首次开库或调用[getKnowledgeProcessor](dataaugmentation-knowledgeprocessor-api.md#getknowledgeprocessor)接口前调用cleanKnowledgeData接口，其他场景调用可能会导致知识库数据丢失或者数据损坏。

**注意** 

在schema升级场景中，为避免数据不一致，强烈建议仅在首次开库或调用getKnowledgeProcessor接口前调用cleanKnowledgeData接口以清理旧数据。非schema升级场景下请勿调用此接口，否则可能导致已有知识库数据永久丢失或损坏，且无法恢复。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | 知识加工对象的上下文。 |
| config | [KnowledgeProcessorConfig](dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessorconfig) | 是 | 知识加工配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1021400001](errorcode-dataaugmentation.md#section1021400001-知识源未配置) | The knowledge source is not configured. |
| [1021400002](errorcode-dataaugmentation.md#section1021400002-知识schema文件不存在)  [1021400003](errorcode-dataaugmentation.md#section1021400003-知识schema内容不合法)  [1021400004](errorcode-dataaugmentation.md#section1021400004-操作rdb数据源时发生错误) | The knowledge schema file is not found.  The knowledge schema content is invalid.  An error occurred during operations on the RDB source. |

**示例：**

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 清理知识库的异步函数
async function cleanKnowledgeData() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 清理知识库
    await knowledgeProcessor.cleanKnowledgeData(context, knowledgeProcessorConfig);
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}
```

## KnowledgeProcessorConfig

管理知识加工对象的配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sourceConfig | [KnowledgeSourceConfig](dataaugmentation-knowledgeprocessor-api.md#knowledgesourceconfig) | 是 | 当前知识加工数据源配置。 |
| llm | [ChatLLM](dataaugmentation-knowledgeprocessor-api.md#chatllm) | 否 | 接口调用方维护的LLM模型指针。为使用邮件分析的任意 handler ，必须配置本参数且不允许为空。  **起始版本：** 26.0.0 |
| properties | string | 否 | 知识加工所需的属性信息，json字符串形如："{\"userName\": \"John\", \"maxCtxLen\": 30000}"，为使用邮件分析的任意handler，必须配置本参数且不允许为空。  - userName：用户本人姓名，长度范围[1,256]，用于排除非本人待办被误提取。为使用邮件分析的任意handler，必须配置本参数。  - maxCtxLen：接口调用方自定义大模型的最大上下文长度，长度[1,INT32\_MAX]。接口调用方应保证[ChatLLM](dataaugmentation-knowledgeprocessor-api.md#chatllm)接口调用的大模型上下文长度大于等于此值，否则可能会因大模型上下文长度超限而导致邮件分析失败。为使用邮件分析的任意handler，必须配置本参数。  **起始版本：** 26.0.0 |

## KnowledgeSourceConfig

管理知识数据源配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rdbSource | relationalStore.StoreConfig | 否 | RDB数据库配置。加工数据源为RDB数据库时配置，当前版本仅支持RDB数据源，若不填该参数，接口返回错误码[1021400001](errorcode-dataaugmentation.md#section1021400001-知识源未配置)。 |

## KnowledgeProcessConfig

知识加工配置。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [KnowledgeProcessMode](dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessmode) | 是 | 知识加工参数。倒排或者倒排+向量两种加工模式. |

## ChatLLM

chat(query: string): Promise<string>

由接口调用方对期望使用的大模型问答过程进行封装的函数类型。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 表示与LLM问答模型问答的问题信息。 |

**返回值：**

| 类型 | 必填 | 说明 |
| --- | --- | --- |
| Promise<string> | 是 | Promise对象，正常情况下返回问答结果，如果出现异常则返回空字符串。 |

## KnowledgeProcessMode

知识加工模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVERTED\_INDEX | 1 | 倒排加工模式。 |
| INVERTED\_INDEX\_VECTORIZATION | 3 | 倒排＋向量加工模式。 |

## KnowledgeProcessor

知识加工对象，用于获取知识加工状态等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

### getStatus

getStatus(): Promise<ProcessorStatus>

获取知识加工状态。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ProcessorStatus](dataaugmentation-knowledgeprocessor-api.md#processorstatus)> | Promise对象，返回知识加工状态。 |

**错误码：**

| **错误码ID** | **错误信息** |
| --- | --- |
| [1021400000](errorcode-dataaugmentation.md#section1021400000-内部错误) | Internal error. |
| [1021400004](errorcode-dataaugmentation.md#section1021400004-操作rdb数据源时发生错误) | An error occurred during operations on the RDB source. |

**示例：**

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 获取知识加工状态的异步函数
async function getStatus() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 获取知识加工状态
    const status: knowledgeProcessor.ProcessorStatus = await processor.getStatus();
    return status;
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}
```

### startProcess

startProcess(config: KnowledgeProcessConfig): Promise<void>

根据入参的配置，启动知识加工。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [KnowledgeProcessConfig](dataaugmentation-knowledgeprocessor-api.md#knowledgeprocessconfig) | 是 | 知识加工配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Device type error. |
| [1021400000](errorcode-dataaugmentation.md#section1021400000-内部错误) | Internal error. |
| [1021400005](errorcode-dataaugmentation.md#section1021400005-重复启动知识加工) | Feature already active. Function called repeatedly. |

**示例：**

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 启动知识加工的异步函数
async function startProcess() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 启动知识加工
    let processMode: knowledgeProcessor.KnowledgeProcessMode = knowledgeProcessor.KnowledgeProcessMode.INVERTED_INDEX;
    let config: knowledgeProcessor.KnowledgeProcessConfig = {
      mode: processMode,
    };
    await processor.startProcess(config);
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
  }
}
```

### stopProcess

stopProcess(): Promise<void>

停止当前知识加工。使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```typescript
import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // 已触发知识加工的数据库名
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// 停止知识加工的异步函数
async function stopProcess() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // 获取知识加工对象
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    // 停止知识加工
    await processor.stopProcess();
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
  }
}
```

## ProcessorStatus

知识加工状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.KnowledgeProcessor

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_REMAINING\_TO\_PROCESS | 0 | 存在待加工的数据。 |
| DATA\_PROCESSING\_IN\_PROGRESS | 1 | 数据正在进行知识加工中。 |
| DATA\_PROCESSING\_COMPLETE | 2 | 所有数据已完成加工。 |
