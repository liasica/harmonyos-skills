---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-localchatmodel-api
title: localChatModel（端侧问答模型）
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > ArkTS API > localChatModel（端侧问答模型）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e2601b2c2c0207f493d9ef9c35dc4f70f280405a15895e7e344c7557fc1b6113
---

## 模块概述

localChatModel模块是Data Augmentation Kit中的端侧问答组件，提供接入端侧问答模型的方法，适用于需要在设备本地进行智能问答的应用场景，实现数据本地化处理。

开发者可通过localChatModel模块提供的方法[init](dataaugmentation-localchatmodel-api.md#init)、[chat](dataaugmentation-localchatmodel-api.md#chat)实现上述能力。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';
```

## Config

是否支持流式问答的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isStream | boolean | 否 | 否 | 表示是否支持流式问答。  设置为true时，支持流式返回结果，适用于需要实时响应的场景；  设置为false时，一次性返回完整结果，适用于对结果完整性要求较高且可接受延迟的场景。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let localConfig: localChatModel.Config = {
  isStream: true
}
```

## QuestionInfo

与端侧问答模型交互的问题信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| questionId | number | 否 | 否 | 表示与端侧问答模型交互的问题ID，ID取值范围为[0,65535]，若超过范围，则上报某些参数不符合指定约束条件的错误码[1021900005](errorcode-dataaugmentation.md#section1021900005-某些参数不满足指定的约束条件)。在同一应用运行时，questionId应保持唯一性。建议使用递增序列生成唯一ID，以防止在并发请求中出现重复ID导致的问题。 |
| content | string | 否 | 否 | 表示与端侧问答模型交互的问题内容，由于受到端侧性能的限制，为保证模型处理效率，建议控制问题内容在4500字节以内，并尽量精简表达，避免冗余信息。若问题过长，部分设备可能面临性能下降，甚至导致模型异常。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let questionInfo: localChatModel.QuestionInfo = {
  questionId: 1,
  content: "问题内容"
}
```

## Answer

与端侧问答模型交互的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| questionId | number | 否 | 否 | 表示问答模型返回结果对应的问题ID，与请求中的questionId保持一致。 |
| content | string | 否 | 否 | 表示问答模型对于questionId对应的问题的问答结果。 |
| isFinished | boolean | 否 | 否 | 表示问答结果是否完整，true表示所有结果已完整返回，本轮问答结束；false表示还有后续结果，当前回调返回的是增量内容。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

let answer: localChatModel.Answer = {
  questionId: 1,
  content: "回答内容",
  isFinished: true
}
```

## init

init(): Promise<boolean>

初始化端侧问答模型，负责拉起模型管理应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回模型初始化结果，true表示初始化成功，模型已就绪；false表示初始化失败，模型不可用。 |

**示例：**

```typescript
import { localChatModel } from '@kit.DataAugmentationKit';

async function init() {
  try {
    const result = await localChatModel.init();
    console.info('init result: ', result);
  } catch (err) {
    console.error('init err: ', err);
  }
}
```

## chat

chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>

chat方法用于向端侧问答模型发送问题并获取回答，适用于本地智能问答场景，使用Promise异步回调。

**说明** 

在调用chat方法前，必须先调用[init](dataaugmentation-localchatmodel-api.md#init)方法完成模型初始化，以确保端侧问答模型处于可用状态。若未初始化模型，则chat方法将因模型未就绪而抛出端侧问答模型加载失败错误码[1021900002](errorcode-dataaugmentation.md#section1021900002-端侧问答模型加载失败)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [QuestionInfo](dataaugmentation-localchatmodel-api.md#questioninfo) | 是 | 表示与端侧问答模型问答的问题信息。 |
| config | [Config](dataaugmentation-localchatmodel-api.md#config) | 是 | 表示问题的配置选项。 |
| callback | AsyncCallback<[Answer](dataaugmentation-localchatmodel-api.md#answer)> | 是 | 回调函数，返回问答的结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-dataaugmentation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021900001](errorcode-dataaugmentation.md#section1021900001-调用端侧问答模型超时) | A timeout occurs when the local chat model is called. |
| [1021900002](errorcode-dataaugmentation.md#section1021900002-端侧问答模型加载失败) | A loading failure occurs when the local chat model is called. |
| [1021900003](errorcode-dataaugmentation.md#section1021900003-端侧问答模型请求失败) | A request failure occurs when the local chat model is called. |
| [1021900004](errorcode-dataaugmentation.md#section1021900004-端侧问答模型繁忙) | The local chat model is busy. |
| [1021900005](errorcode-dataaugmentation.md#section1021900005-某些参数不满足指定的约束条件) | Some parameters do not meet the specified constraints. |

**示例：**

```typescript
import { BusinessError } from "@kit.BasicServicesKit";
import { localChatModel } from '@kit.DataAugmentationKit';

async function chat() {
  // `questionId`用于标识问题ID，`content`用于设置问题内容。
  let questionInfo: localChatModel.QuestionInfo = {
    questionId: 1,
    content: "你是一个翻译助手，可以翻译多国语言，请将以下内容翻译成36国语言：PC模型管家"
  }
  // `isStream: true`表示启用流式返回结果，适用于实时响应场景。
  let localConfig: localChatModel.Config = {
    isStream: true
  }
  let localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
    if (err) {
      // 模型运行相关错误码
      console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      return;
    }
    if (!ans) {
      console.error('Received null or undefined answer. Skipping processing.');
      return;
    }
    // `questionId`用于标识问题ID，`content`问题回答内容，`isFinished`表示问答结果是否完整，true表示所有结果已完整返回。
    console.info('questionId: ' + ans.questionId + ', content: ' + ans.content + ', isFinished: ' + ans.isFinished);
  };
  try {
    await localChatModel.chat(questionInfo, localConfig, localChatCallback);
  } catch (err) {
    // 入参相关错误码
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  }
}
```
