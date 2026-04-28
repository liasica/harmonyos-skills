---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-localchatmodel-api
title: localChatModel（端侧问答模型）
breadcrumb: API参考 > 应用框架 > Data Augmentation Kit（数据增强服务） > ArkTS API > localChatModel（端侧问答模型）
category: harmonyos-references
scraped_at: 2026-04-28T08:05:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75354da2741bf68996a641f53742b3921de7a8880fc9a81d0e92f0236991f13c
---

本模块提供接入端侧问答模型问答的方法，实现数据不出端的智能问答能力。

**起始版本：** 6.0.0(20)

## 导入模块

PC/2in1

```
1. import { localChatModel } from '@kit.DataAugmentationKit';
```

## Config

PC/2in1

是否支持流式问答的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isStream | boolean | 否 | 否 | 表示是否支持流式问答。true表示支持，false表示不支持。 |

**示例：**

```
1. import { localChatModel } from '@kit.DataAugmentationKit';

3. let localConfig: localChatModel.Config = {
4. isStream: true
5. }
```

## QuestionInfo

PC/2in1

与端侧问答模型交互的问题信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| questionId | number | 否 | 否 | 表示与端侧问答模型交互的问题ID，ID取值范围为[0,65535]，在同一应用运行时，questionId应保持唯一性。 |
| content | string | 否 | 否 | 表示与端侧问答模型交互的问题内容，由于受到端侧性能的限制，建议content长度不超过4500字节。 |

**示例：**

```
1. import { localChatModel } from '@kit.DataAugmentationKit';

3. let questionInfo: localChatModel.QuestionInfo = {
4. questionId: 1,
5. content: "问题内容"
6. }
```

## Answer

PC/2in1

与端侧问答模型交互的返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| questionId | number | 否 | 否 | 表示问答模型返回结果对应的问题ID，与请求的questionId一致。 |
| content | string | 否 | 否 | 表示问答模型对于questionId对应的问题的问答结果。 |
| isFinished | boolean | 否 | 否 | 表示问答结果是否完整，true表示所有结果已完整返回，false表示结果未完整返回。 |

**示例：**

```
1. import { localChatModel } from '@kit.DataAugmentationKit';

3. let answer: localChatModel.Answer = {
4. questionId: 1,
5. content: "回答内容",
6. isFinished: true
7. }
```

## init

PC/2in1

init(): Promise<boolean>

初始化端侧问答模型，使用promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回模型初始化结果，true表示成功，false表示失败。 |

**示例：**

```
1. import { localChatModel } from '@kit.DataAugmentationKit';

3. async function init() {
4. try {
5. const result = await localChatModel.init();
6. console.info('init result: ', result);
7. } catch (err) {
8. console.error('init err: ', err);
9. }
10. }
```

## chat

PC/2in1

chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>

对端侧问答模型进行问答，使用Promise异步回调。

说明

调用chat方法前需要先调用init方法初始化端侧问答模型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DataAugmentation.LocalChatModel

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [QuestionInfo](dataaugmentation-localchatmodel-api.md#questioninfo) | 是 | 表示与端侧问答模型问答的问题信息。 |
| config | [Config](dataaugmentation-localchatmodel-api.md#config) | 是 | 表示问题的配置选项。 |
| callback | AsyncCallback<[Answer](dataaugmentation-localchatmodel-api.md#answer)> | 是 | 表示将问答的结果返回给调用方的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](dataaugmentation-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1021900001](dataaugmentation-error-code.md#section1021900001-调用端侧问答模型超时) | A timeout occurs when the local chat model is called. |
| [1021900002](dataaugmentation-error-code.md#section1021900002-端侧问答模型加载失败) | A loading failure occurs when the local chat model is called. |
| [1021900003](dataaugmentation-error-code.md#section1021900003-端侧问答模型请求失败) | A request failure occurs when the local chat model is called. |
| [1021900004](dataaugmentation-error-code.md#section1021900004-端侧问答模型繁忙) | The local chat model is busy. |
| [1021900005](dataaugmentation-error-code.md#section1021900005-某些参数不满足指定的约束条件) | Some parameters do not meet the specified constraints. |

**示例：**

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { localChatModel } from '@kit.DataAugmentationKit';

4. async function chat() {
5. let questionInfo: localChatModel.QuestionInfo = {
6. questionId: 100,
7. content: "你是一个翻译助手，可以翻译多国语言，请将以下内容翻译成36国语言：PC模型管家"
8. }
9. let localConfig: localChatModel.Config = {
10. isStream: true
11. }
12. let localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
13. if (err) {
14. // 模型运行相关错误码
15. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
16. return;
17. }
18. console.info('questionId: ' + ans.questionId + ', content: ' + ans.content + ', isFinished: ' + ans.isFinished);
19. };
20. try {
21. await localChatModel.chat(questionInfo, localConfig, localChatCallback);
22. } catch (err) {
23. // 入参相关错误码
24. console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
25. }
26. }
```
