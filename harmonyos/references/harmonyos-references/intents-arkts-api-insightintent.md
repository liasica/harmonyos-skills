---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent
title: insightIntent
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > insightIntent
category: harmonyos-references
scraped_at: 2026-04-28T08:18:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93d2d5a08e64e5211d4b2082b075f5763701beb4c12e12aed27df4a7da33c95b
---

insightIntent是Intents Kit的子模块，提供意图开放能力，包括共享和删除InsightIntent。应用/元服务可以通过调用本模块接口，向系统共享数据。意图框架根据共享的数据学习规律，在合适的时机在系统入口将对应的InsightIntent推荐给用户，用户点击后，根据应用/元服务声明的InsightIntent API，跳转到对应页面。

举例说明：视频类应用通过InsightIntent提供共享数据（如用户每天看视频的时间点、视频信息）和对应的开放API。意图框架将在用户每天看视频的时间点通过卡片推荐视频，用户点击卡片后，意图框架将调用该开放API打开视频。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1Tablet

```
1. import { insightIntent } from '@kit.IntentsKit';
```

## InsightIntent

PhonePC/2in1Tablet

InsightIntent，包括意图名称、意图版本号、标识、Action信息、Entity信息。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intentName | string | 否 | 否 | 表示意图名称，例如：'PlayMusic'。 |
| intentVersion | string | 否 | 否 | 表示意图版本，当前为初始版本'1.0'。 |
| identifier | string | 否 | 否 | 表示意图的标识符，开发者按照自身业务需要生成，作为单条共享记录的唯一标识符。该字段的生成方式可参考UUID生成方式，或基于时间戳生成随机字符串。例如：'52dac3b0-6520-4974-81e5-25f0879449b5'。 |
| intentActionInfo | [IntentActionInfo](intents-arkts-api-insightintent.md#intentactioninfo) | 否 | 否 | 表示意图的执行信息，例如：已执行或预测将要执行意图的时间。示例请参考[shareIntent](intents-arkts-api-insightintent.md#insightintentshareintent)的示例代码。  **说明：**  - 在4.0.0(10)版本，参数类型为{[key: string]: Object}。  - 从5.0.0(12)版本开始，参数类型为IntentActionInfo。该类型定义与5.0.0(12)前版本兼容。 |
| intentEntityInfo | [IntentEntityInfo](intents-arkts-api-insightintent.md#intententityinfo) | 否 | 否 | 表示意图的实体信息，包含行为和事件。示例请参考[shareIntent](intents-arkts-api-insightintent.md#insightintentshareintent)的示例代码。  **说明：**  在4.0.0(10)版本，参数类型为{entityId: string; entityName: string; [key: string]: Object}。  从5.0.0(12)版本开始，参数类型为IntentEntityInfo。该类型定义与5.0.0(12)前版本兼容。 |

## IntentActionInfo

PhonePC/2in1Tablet

IntentActionInfo，表示意图的执行信息。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [key: string] | Object | 否 | 否 | 表示值的类型为包含一个或多个键值对的对象。其中键的类型为字符，值的类型为Object，键和值的取值范围因意图名称而异，具体请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |

## IntentEntityInfo

PhonePC/2in1Tablet

IntentEntityInfo，表示意图的实体信息。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 否 | 否 | 表示意图实体的标识符，开发者按照自身业务需要生成，作为单条实体的唯一标识符。该字段的生成方式可参考UUID生成方式，或基于时间戳生成随机字符串。例如：'C10194368'。 |
| entityName | string | 否 | 否 | 表示意图实体的名称。取值请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |
| [key: string] | Object | 否 | 否 | 意图实体的其他信息，表示为一个或多个键值对。其中键的类型为字符，值的类型为Object，键和值的取值范围因意图名称而异，具体请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |

## insightIntent.shareIntent

PhonePC/2in1Tablet

shareIntent(context: common.BaseContext, intents: InsightIntent[], callback: AsyncCallback<void>): void

共享已执行或预期的InsightIntent ，使用callback异步回调。

为避免共享能力滥用，默认每个应用每天最多共享20次，超出限制后会返回错误码：1000101104。每次共享的数据条数不限，但是每次最多50KB数据量，单次数据量超出限制后会返回错误码：1000101105。所有接入方每天共享总次数上限为3000次，超出总次数限制会返回错误码：1000101106。建议积攒一定量的数据后一次全部共享并控制共享次数。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intents | [InsightIntent](intents-arkts-api-insightintent.md#insightintent-1)[] | 是 | 表示共享的InsightIntent。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当具体的操作（视具体接口功能描述）成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101104 | The number of sharing times exceeds the limit. |
| 1000101105 | The size of a single shared data exceeds the limit. |
| 1000101106 | Exceeded the maximum number of sharing times of all applications. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';

4. let playMusicIntent: insightIntent.InsightIntent = {
5. intentName: 'PlayMusic',
6. intentVersion: '1.0',
7. identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
8. intentActionInfo: {
9. actionMode: 'EXECUTED',
10. currentPercentage: 50,
11. executedTimeSlots: {
12. executedEndTime: 1637393112000,
13. executedStartTime: 1637393212000
14. }
15. },
16. intentEntityInfo: {
17. entityName: 'Music',
18. entityId: 'C10194368',
19. entityGroupId: '热门',
20. displayName: '歌曲名称',
21. description: '歌曲解释',
22. logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
23. keywords: ['华为音乐','化妆'],
24. rankingHint: 99,
25. expirationDate: 1637393212000,
26. metadataModificationDate: 1637393212000,
27. activityType: ['1', '2', '3'],
28. artist: ['张三','李四'],
29. lyricist: ['李四','张三'],
30. composer: ['张三','李四'],
31. albumName: '专辑名称',
32. duration: 123456789,
33. playCount: 456213123,
34. musicalGenre: ['民族风','摇滚'],
35. isPublicData: false
36. }
37. }
38. try {
39. // 共享数据
40. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
41. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
42. insightIntent.shareIntent(context, [playMusicIntent], (error) => {
43. if (error?.code) {
44. // 处理业务逻辑错误
45. console.error(`shareIntent failed, error.code: ${error?.code}, error.message: ${error?.message}`);
46. return;
47. }
48. // 执行正常业务
49. console.info('shareIntent succeed');
50. });
51. } catch (error) {
52. // 处理异常
53. console.error(`error.code: ${error?.code}, error.message: ${error?.message}`);
54. }
```

## insightIntent.shareIntent

PhonePC/2in1Tablet

shareIntent(context: common.BaseContext, intents: InsightIntent[]): Promise<void>

共享已执行或预期的InsightIntent 。使用Promise异步回调。

为避免共享能力滥用，默认每个应用每天最多共享20次，超出限制后会返回错误码：1000101104。每次共享的数据条数不限，但是每次最多50KB数据量，单次数据量超出限制后会返回错误码：1000101105。所有接入方每天共享总次数上限为3000次，超出总次数限制会返回错误码：1000101106。建议积攒一定量的数据后一次全部共享并控制共享次数。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intents | [InsightIntent](intents-arkts-api-insightintent.md#insightintent-1)[] | 是 | 表示共享的InsightIntent 。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101104 | The number of sharing times exceeds the limit. |
| 1000101105 | The size of a single shared data exceeds the limit. |
| 1000101106 | Exceeded the maximum number of sharing times of all applications. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from'@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let playMusicIntent: insightIntent.InsightIntent = {
6. intentName: 'PlayMusic',
7. intentVersion: '1.0',
8. identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
9. intentActionInfo: {
10. actionMode: 'EXECUTED',
11. currentPercentage: 50,
12. executedTimeSlots: {
13. executedEndTime: 1637393112000,
14. executedStartTime: 1637393212000
15. }
16. },
17. intentEntityInfo: {
18. entityName: 'Music',
19. entityId: 'C10194368',
20. entityGroupId: '热门',
21. displayName: '歌曲名称',
22. description: '歌曲解释',
23. logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
24. keywords: ['华为音乐','化妆'],
25. rankingHint: 99,
26. expirationDate: 1637393212000,
27. metadataModificationDate: 1637393212000,
28. activityType: ['1', '2', '3'],
29. artist: ['张三','李四'],
30. lyricist: ['李四','张三'],
31. composer: ['张三','李四'],
32. albumName: '专辑名称',
33. duration: 123456789,
34. playCount: 456213123,
35. musicalGenre: ['民族风','摇滚'],
36. isPublicData: false
37. }
38. }

40. // 共享数据
41. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
42. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
43. insightIntent.shareIntent(context, [playMusicIntent]).then(() => {
44. console.info('shareIntent succeed');
45. }).catch((err: BusinessError) => {
46. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
47. });
```

## insightIntent.deleteIntent

PhonePC/2in1Tablet

deleteIntent(context: common.BaseContext, intentName: string, identifiers: string[], callback: AsyncCallback<void>): void

删除InsightIntent。如果设置了identifiers参数，则删除intent名称下的identifiers对应的记录。否则，删除意图名称下的所有记录。结果以Callback的形式返回。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intentName | string | 是 | 表示意图的名称。 |
| identifiers | string[] | 是 | 表示意图的标识符。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回删除InsightIntent接口调用是否成功的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';

4. try {
5. // 删除意图下的某些记录
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.deleteIntent(context, 'PlayMusic', ['52dac3b0-6520-4974-81e5-25f0879449b5'], (error) => {
9. if (error?.code) {
10. // 处理业务逻辑错误
11. console.error(`deleteIntent failed, error.code: ${error?.code}, error.message: ${error?.message}`);
12. return;
13. }
14. // 执行正常业务
15. console.info('deleteIntent succeed');
16. });
17. } catch (error) {
18. // 处理异常
19. console.error(`error.code: ${error?.code}, error.message: ${error?.message}`);
20. }
```

## insightIntent.deleteIntent

PhonePC/2in1Tablet

deleteIntent(context: common.BaseContext, intentName: string, callback: AsyncCallback<void>): void

删除InsightIntent。删除意图名称下的所有记录。结果以Callback的形式返回。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intentName | string | 是 | 表示意图的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回删除InsightIntent接口调用是否成功的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';

4. try {
5. // 删除整个意图的数据
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.deleteIntent(context, 'PlayMusic', (error) => {
9. if (error?.code) {
10. // 处理业务逻辑错误
11. console.error(`deleteIntent failed, error.code: ${error?.code}, error.message: ${error?.message}`);
12. return;
13. }
14. // 执行正常业务
15. console.info('deleteIntent succeed');
16. });
17. } catch (error) {
18. // 处理异常
19. console.error(`error.code: ${error?.code}, error.message: ${error?.message}`);
20. }
```

## insightIntent.deleteIntent

PhonePC/2in1Tablet

deleteIntent(context: common.BaseContext, intentName: string, identifiers?: string[]): Promise<void>

删除InsightIntent。如果设置了identifiers参数，则删除intent名称下的identifiers对应的记录。否则，删除意图名称下的所有记录。结果以Promise的形式返回。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intentName | string | 是 | 表示意图的名称。 |
| identifiers | string[] | 否 | 表示意图的标识符。如果填写该字段，则删除指定标识符的意图；如果未填写该字段，则删除意图名称下的所有记录。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 删除意图下的某些记录
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.deleteIntent(context, 'PlayMusic', ['52dac3b0-6520-4974-81e5-25f0879449b5']).then(() => {
9. console.info('deleteIntent succeed');
10. }).catch((err: BusinessError) => {
11. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
12. });
```

## insightIntent.deleteEntity

PhonePC/2in1Tablet

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string[], callback: AsyncCallback<void>): void

按实体名称下的实体ID删除InsightIntent实体。结果以Callback的形式返回。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| entityName | string | 是 | 表示实体的名称。 |
| entityIds | string[] | 是 | 表示实体的id。 |
| callback | AsyncCallback<void> | 是 | 回调函数，返回删除InsightIntent实体接口调用是否成功的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';

4. try {
5. // 删除Entity数据
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.deleteEntity(context, 'PlayMusic', ['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f'], (error) => {
9. if (error?.code) {
10. // 处理业务逻辑错误
11. console.error(`deleteEntity failed, error.code: ${error?.code}, error.message: ${error?.message}`);
12. return;
13. }
14. // 执行正常业务
15. console.info('deleteEntity succeed');
16. });
17. } catch (error) {
18. // 处理异常
19. console.error(`error.code: ${error?.code}, error.message: ${error?.message}`);
20. }
```

## insightIntent.deleteEntity

PhonePC/2in1Tablet

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string[]): Promise<void>

按实体名称下的实体ID删除InsightIntent实体。使用Promise异步回调。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| entityName | string | 是 | 表示实体的名称。 |
| entityIds | string[] | 是 | 表示实体的id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 删除Entity数据
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.deleteEntity(context, 'PlayMusic', ['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f']).then(() => {
9. console.info('deleteEntity succeed');
10. }).catch((err: BusinessError) => {
11. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
12. });
```

## insightIntent.getSid

PhonePC/2in1Tablet

getSid(context: common.BaseContext, renew: boolean): Promise<string>

获取Service Open ID。使用Promise异步回调。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| renew | boolean | 是 | 是否强制从云端获取新的服务开放ID。如果为true，从云端获取新的服务开放ID；如果为false，则优先获取本地存储的服务开放ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回获取到的Service Open ID。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101102 | HUAWEI Assistant has stopped providing services. |
| 1000101107 | Too many Service Open ID renew requests. |
| 1000101201 | The service is abnormal. |

**示例：**

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import common from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 获取SID
6. // 此处仅为示例，请根据实际代码上下文自行传入合适的context
7. let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
8. insightIntent.getSid(context, false).then((sid: string) => {
9. console.info('getSid succeed!');
10. }).catch((err: BusinessError) => {
11. console.error(`error.code: ${err?.code}, failed because ${err?.message}`);
12. });
```
