---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-text-processing-api
title: textProcessing（文本处理）
breadcrumb: API参考 > AI > Natural Language Kit（自然语言理解服务） > ArkTS API > textProcessing（文本处理）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11d1ff17d1b48caca2eaa0ccb18dd52aa227c1ad52f80c76580d28d56143ca83
---

自然语言理解服务提供将输入的普通文本都标注为带词性的文本，标注每个词是名词、动词、形容词或其他词性。

还提供实体抽取功能，通过对用户输入的文本进行实体识别。然后依据Kit中的实体类别来进行分类，其中用户可以根据实体类别列表中的类别来进行选择。输出结果中包含实体的类别、实体在原文本中的位置、实体的原文本以及实体解析后的其他字段。实体字段内容可参考[EntityType](natural-language-text-processing-api.md#entitytype)详情。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
```

## WordSegment

PhonePC/2in1Tablet

分词的输出结果，包含词语和词性。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| word | string | 否 | 否 | 词语。 |
| wordTag | string | 否 | 否 | 词性。词性分类参考[wordTag](natural-language-word-tag-api.md)。 |

## EntityConfig

PhonePC/2in1Tablet

可选配置项，实体的类别。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityTypes | [EntityType](natural-language-text-processing-api.md#entitytype)[] | 否 | 是 | 实体的类别。  默认全选。 |

## EntityType

PhonePC/2in1Tablet

实体类别的枚举类。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATETIME | datetime | 时间实体 |
| EMAIL | email | 邮箱实体 |
| EXPRESS\_NO | expressNo | 快递单号实体 |
| FLIGHT\_NO | flightNo | 航班号实体 |
| LOCATION | location | 地点实体 |
| NAME | name | 姓名实体 |
| PHONE\_NO | phoneNo | 手机号实体 |
| URL | url | url实体 |
| VERIFICATION\_CODE | verificationCode | 验证码实体 |
| ID\_NO | idNo | 身份证号实体 |

## Entity

PhonePC/2in1Tablet

实体抽取的结果。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 实体原文本。 |
| charOffset | number | 否 | 否 | 实体在原文本中的位置。所在位置以字符计算。 |
| type | [EntityType](natural-language-text-processing-api.md#entitytype) | 否 | 否 | 实体类别。 |
| jsonObject | string | 否 | 否 | 实体的其他字段。详情参考[jsonObject](natural-language-json-object-api.md)。 |

## textProcessing.getWordSegment

PhonePC/2in1Tablet

getWordSegment(text: string): Promise<Array<WordSegment>>

创建分词实例，并初始化引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

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

以下错误码的详细介绍请参见[Natural Language Kit错误码](natural-language-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```
1. import { textProcessing } from '@kit.NaturalLanguageKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function testWordSegment(inputText: string) {
5. textProcessing.getWordSegment(inputText)
6. .then(result => {
7. let outputText = formatWordSegmentResult(result);
8. console.info('NLUDemo', `getWordSegment result:${outputText}`);
9. })
10. .catch((err: BusinessError) => {
11. console.error('NLUDemo', `getWordSegment errorCode: ${err.code} errorMessage: ${err.message}`);
12. });
13. }

15. function formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
16. let output = 'Word Segments:\n';
17. segments.forEach((segment, index) => {
18. output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
19. });
20. return output;
21. }

23. @Entry
24. @Component
25. struct Page {

27. build() {
28. Column(){
29. Button('Start').onClick(() => {
30. // 测试文本分词
31. let inputText = 'test for nlp word segment';
32. testWordSegment(inputText);
33. })
34. }
35. }
36. }
```

## textProcessing.getEntity

PhonePC/2in1Tablet

getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>

创建实体抽取实例，并初始化引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

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

以下错误码的详细介绍请参见[Natural Language Kit错误码](natural-language-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```
1. import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function testEntityRecognition(inputText: string) {
5. textProcessing.getEntity(inputText, {
6. entityTypes: [EntityType.NAME]
7. }).then(result => {
8. let outputText = formatEntityResult(result);
9. console.info('NLUDemo', `getEntity result:${outputText}`);
10. }).catch((err: BusinessError) => {
11. console.error('NLUDemo', `getEntity errorCode: ${err.code} errorMessage: ${err.message}`);
12. })
13. }

15. function formatEntityResult(entities: textProcessing.Entity[]): string {
16. if (!entities || !entities.length) {
17. return 'No entities found.';
18. }

20. let output = 'Entities:\n';
21. for (let i = 0; i < entities.length; i++) {
22. let entity = entities[i];
23. output += `Entity[${i}]:\n`;
24. output += `  oriText: ${entity.text}\n`;
25. output += `  charOffset: ${entity.charOffset}\n`;
26. output += `  entityType: ${entity.type}\n`;
27. output += `  jsonObject: ${entity.jsonObject}\n\n`;
28. }
29. return output;
30. }

32. @Entry
33. @Component
34. struct Page {

36. build() {
37. Column(){
38. Button('Start').onClick(() => {
39. // 测试实体识别
40. let inputText = 'test for nlp getEntity. Mary, Bob and Mike.';
41. testEntityRecognition(inputText);
42. })
43. }
44. }
45. }
```

## textProcessing.init

PhonePC/2in1Tablet

init(): Promise<boolean>

初始化自然语言处理的引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，true表示初始化成功，false表示初始化失败。 |

说明

此初始化接口非必须调用。在主动使用时，可以提前初始化该功能，减少首次调用文本处理能力的时延。

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](natural-language-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```
1. import { textProcessing } from '@kit.NaturalLanguageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Page {

8. build() {
9. Column(){
10. Button('init').onClick(() => {
11. textProcessing.init().then(result => {
12. console.info(`textProcess init result: ${result}`)
13. }).catch((err: BusinessError) => {
14. console.error(`textProcess init failed errorCode: ${err.code} errorMessage: ${err.message}`);
15. })
16. })
17. }
18. }
19. }
```

## textProcessing.release

PhonePC/2in1Tablet

release(): Promise<boolean>

释放引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.NaturalLanguage.TextProcessing

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，true表示释放引擎成功，false表示释放引擎失败。 |

**错误码：**

以下错误码的详细介绍请参见[Natural Language Kit错误码](natural-language-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 1011200001 | Failed to run, please try again. |
| 1011200002 | The service is abnormal. |

**示例：**

```
1. import { textProcessing } from '@kit.NaturalLanguageKit';

3. async function runTextProcessing() {
4. await textProcessing.init();
5. console.info('Text processing initialized successfully');

7. try {
8. const result = await textProcessing.release();
9. console.info(`textProcess release result: ${result}`);
10. } catch (err) {
11. console.error(`textProcess release failed errorCode: ${err.code} errorMessage: ${err.message}`);
12. }
13. }

15. @Entry
16. @Component
17. struct Page {

19. build() {
20. Column(){
21. Button('Start').onClick(() => {
22. void runTextProcessing()
23. })
24. }
25. }
26. }
```
