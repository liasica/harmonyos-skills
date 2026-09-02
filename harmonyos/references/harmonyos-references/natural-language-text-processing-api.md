---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-text-processing-api
title: textProcessing（文本处理）
breadcrumb: API参考 > AI > Natural Language Kit（自然语言理解服务） > ArkTS API > textProcessing（文本处理）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c2d8bec22aff1d1d535a177fa5c1bc9ee97660ab520a2d76b9306ea4f63f9049
---

自然语言理解服务，该模块基于自然语言处理技术，能够将输入的普通文本进行分词并标注词性，标注每个词是名词、动词、形容词或其他词性。

还提供实体抽取功能，通过对用户输入的文本进行实体识别。然后依据Kit中的实体类别来进行分类，其中用户可以根据实体类别列表中的类别来进行选择。输出结果中包含实体的类别、实体在原文本中的位置、实体的原文本以及实体解析后的其他字段。实体字段内容可参考[EntityType](natural-language-entity-type-api.md)详情。适用于智能客服、内容分析、信息提取等需要对文本进行深度解析的业务场景。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
```

## WordSegment

分词的输出结果，包含词语和词性。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| word | string | 否 | 否 | 词语。从getWordSegment方法中获取到的结果中的词语。 |
| wordTag | string | 否 | 否 | 词性。从getWordSegment方法中获取到的结果中的词性，词性分类参考[wordTag](natural-language-word-tag-api.md)。 |

## EntityConfig

可选配置项，实体的类别。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityTypes | [EntityType](natural-language-entity-type-api.md)[] | 否 | 是 | 实体的类别。若未指定，则默认识别所有支持的实体类型。 |
| timestamp | number | 否 | 是 | 参考时间戳，用于指定实体识别的时间上下文。取值为从1970年1月1日开始的毫秒数（整数）。若未指定，则使用当前系统时间。  **起始版本：** 26.0.0 |

## Entity

实体抽取的结果。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 实体原文本。 |
| charOffset | number | 否 | 否 | 实体在原文本中的位置。所在位置以字符计算。 |
| type | [EntityType](natural-language-entity-type-api.md) | 否 | 否 | 实体类别。 |
| jsonObject | string | 否 | 否 | Entity返回参数说明。详情参考[jsonObject](natural-language-json-object-api.md)。 |

## textProcessing.getWordSegment

getWordSegment(text: string): Promise<Array<WordSegment>>

创建分词实例，并初始化引擎。使用Promise异步回调。适用于文本分词、关键词提取、文本相似度计算等场景。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入待分析的文本内容。相关规格参考[约束与限制](../harmonyos-guides/natural-language-introduction.md#约束与限制)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WordSegment](natural-language-text-processing-api.md#wordsegment)>> | Promise对象，返回分词结果的集合。 |

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](errorcode-natural-language.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 分词结果格式化函数
// 功能：对分词结果数组进行格式化，包含每个词的词语和词性
function formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
  let output = 'Word Segments:\n';
  segments.forEach((segment, index) => {
    output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
  });
  return output;
}

// 分词功能测试函数
// 功能：对输入文本进行分词处理，识别文本中的词语及其词性
function testWordSegment(inputText: string) {
  textProcessing.getWordSegment(inputText)
    .then(result => {
      // 处理分词成功结果，格式化并输出
      let outputText = formatWordSegmentResult(result);
      console.info('NLUDemo', `getWordSegment result:${outputText}`);
    })
    .catch((err: BusinessError) => {
      console.error('NLUDemo', `getWordSegment errorCode: ${err.code} errorMessage: ${err.message}`);
    });
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        // 输入待分词文本，调用分词功能
        let inputText = 'test for nlp word segment';
        testWordSegment(inputText);
      })
    }
  }
}
```

## textProcessing.getEntity

getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>

创建实体抽取实例，并初始化引擎。使用Promise异步回调。适用于用户输入的敏感信息识别，内容审核等场景。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的字符串。相关规格参考[约束与限制](../harmonyos-guides/natural-language-introduction.md#约束与限制)。 |
| entityConfig | [EntityConfig](natural-language-text-processing-api.md#entityconfig) | 否 | 实体配置项：实体类别。  默认全选。推荐按需加载实体类别，以提高应用性能。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Entity](natural-language-text-processing-api.md#entity)>> | Promise对象，返回实体的结果集合。 |

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](errorcode-natural-language.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```typescript
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 实体识别结果格式化函数
// 功能：对实体识别结果数组进行格式化，包含实体的原文、位置、类型和详细参数

function formatEntityResult(entities: textProcessing.Entity[]): string {
  if (!entities || !entities.length) {
    return 'No entities found.';
  }

  let output = 'Entities:\n';
  for (let i = 0; i < entities.length; i++) {
    let entity = entities[i];
    output += `Entity[${i}]:\n`;
    output += `  oriText: ${entity.text}\n`;         // 实体原文
    output += `  charOffset: ${entity.charOffset}\n`; // 实体在原文中的字符偏移
    output += `  entityType: ${entity.type}\n`;      // 实体类型
    output += `  jsonObject: ${entity.jsonObject}\n\n`; // 实体的详细参数
  }
  return output;
}

// 实体识别功能测试函数
// 功能：对输入文本进行实体识别，抽取文本中的特定类型实体
function testEntityRecognition(inputText: string) {
  // 指定只识别姓名实体类型，以提高处理效率和准确性
  textProcessing.getEntity(inputText, {
    entityTypes: [EntityType.NAME]
  }).then(result => {
    // 处理识别成功结果，格式化并输出
    let outputText = formatEntityResult(result);
    console.info('NLUDemo', `getEntity result:${outputText}`);
  }).catch((err: BusinessError) => {
    console.error('NLUDemo', `getEntity errorCode: ${err.code} errorMessage: ${err.message}`);
  });
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        // 输入待识别文本，调用实体识别功能（识别人名）
        let inputText = 'test for nlp getEntity. Mary, Bob and Mike.';
        testEntityRecognition(inputText);
      })
    }
  }
}
```

## textProcessing.init

init(): Promise<boolean>

初始化自然语言处理的引擎。使用Promise异步回调。

**说明** 

当开发者需要提前初始化自然语言处理引擎，以减少首次调用文本处理能力（如分词、实体识别）的时延时，可以主动调用此方法。在实际使用中，如果对性能没有特殊要求，可以不调用此接口，系统会在首次使用时自动初始化。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，true表示初始化成功，false表示初始化失败。 |

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](errorcode-natural-language.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('init').onClick(() => {
        textProcessing.init().then(result => {
          console.info(`textProcess init result: ${result}`);
        }).catch((err: BusinessError) => {
          console.error(`textProcess init failed errorCode: ${err.code} errorMessage: ${err.message}`);
        });
      })
    }
  }
}
```

## textProcessing.release

release(): Promise<boolean>

释放引擎。使用Promise异步回调。当开发者不再需要使用自然语言处理功能时，应主动调用此方法释放引擎资源。建议在页面退出或不再需要文本处理能力时调用，以释放内存资源。调用 release() 后，再次调用getWordSegment 或 getEntity 会触发重新初始化引擎，可能会增加调用耗时。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，true表示释放引擎成功，false表示释放引擎失败。 |

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](errorcode-natural-language.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';

async function runTextProcessing() {
  // 初始化引擎
  await textProcessing.init();
  console.info('Text processing initialized successfully');

  // 使用完成后释放引擎资源
  try {
    const result = await textProcessing.release();
    console.info(`textProcess release result: ${result}`);
  } catch (err) {
    console.error(`textProcess release failed errorCode: ${err.code} errorMessage: ${err.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        void runTextProcessing();
      })
    }
  }
}
```
