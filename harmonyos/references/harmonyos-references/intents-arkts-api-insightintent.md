---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/intents-arkts-api-insightintent
title: insightIntent
breadcrumb: API参考 > AI > Intents Kit（意图框架服务） > ArkTS API > insightIntent
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aead031246f5a18571a77c098c297e07ce05a9a64e5d2e0e5bbdbbdbc1e8f963
---

insightIntent是Intents Kit的子模块，提供意图开放能力，包括共享和删除InsightIntent。应用/元服务可以通过调用本模块接口，向系统共享数据。意图框架根据共享的数据学习规律，在合适的时机在系统入口将对应的InsightIntent推荐给用户，用户点击后，根据应用/元服务声明的insightIntent API，跳转到对应页面。

举例说明：视频类应用通过insightIntent提供共享数据（如用户每天看视频的时间点、视频信息）和对应的开放API。意图框架将在用户每天看视频的时间点通过卡片推荐视频，用户点击卡片后，意图框架将调用该开放API打开视频。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { insightIntent } from '@kit.IntentsKit';
```

## InsightIntent

InsightIntent，包括意图名称、意图版本号、标识、Action信息、Entity信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intentName | string | 否 | 否 | 表示意图名称，例如：'PlayMusic'。 |
| intentVersion | string | 否 | 否 | 表示意图版本，当前为初始版本'1.0.1'。 |
| identifier | string | 否 | 否 | 表示意图的标识符，开发者按照自身业务需要生成，作为单条共享记录的唯一标识符。该字段的生成方式可参考UUID生成方式，或基于时间戳生成随机字符串。例如：'52dac3b0-6520-4974-81e5-25f0879449b5'。 |
| intentActionInfo | [IntentActionInfo](intents-arkts-api-insightintent.md#intentactioninfo) | 否 | 否 | 表示意图的执行信息，例如：已执行或预测将要执行意图的时间。示例请参考[shareIntent](intents-arkts-api-insightintent.md#shareintent)的示例代码。  **说明：**  - 在5.0.0(12)版本之前，参数类型为{[key: string]: Object}。  - 从5.0.0(12)版本开始，参数类型为IntentActionInfo。该类型定义与5.0.0(12)之前版本兼容。 |
| intentEntityInfo | [IntentEntityInfo](intents-arkts-api-insightintent.md#intententityinfo) | 否 | 否 | 表示意图的实体信息，包含行为和事件。示例请参考[shareIntent](intents-arkts-api-insightintent.md#shareintent)的示例代码。  **说明：**  在5.0.0(12)版本之前，参数类型为{entityId: string; entityName: string; [key: string]: Object}。  从5.0.0(12)版本开始，参数类型为IntentEntityInfo。该类型定义与5.0.0(12)之前版本兼容。 |

## IntentActionInfo

IntentActionInfo，表示意图的执行信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [key: string] | Object | 否 | 否 | 表示值的类型为包含一个或多个键值对的对象。其中键的类型为字符，值的类型为Object，键和值的取值范围因意图名称而异，具体请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |

## IntentEntityInfo

IntentEntityInfo，表示意图的实体信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.AI.InsightIntent

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 否 | 否 | 表示意图实体的标识符，开发者按照自身业务需要生成，作为单条实体的唯一标识符。该字段的生成方式可参考UUID生成方式，或基于时间戳生成随机字符串。例如：'C10194368'。 |
| entityName | string | 否 | 否 | 表示意图实体的名称。取值请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |
| [key: string] | Object | 否 | 否 | 意图实体的其他信息，表示为一个或多个键值对。其中键的类型为字符，值的类型为Object，键和值的取值范围因意图名称而异，具体请参考[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。 |

## shareIntent

shareIntent(context: common.BaseContext, intents: InsightIntent[], callback: AsyncCallback<void>): void

共享已执行或预期的InsightIntent ，使用callback异步回调。

为避免共享能力滥用，默认每个应用每天最多共享20次，超出限制后会返回错误码：1000101104。每次共享的数据条数不限，但是每次最多50KB数据量，单次数据量超出限制后会返回错误码：1000101105。所有接入方每天共享总次数上限为3000次，超出总次数限制会返回错误码：1000101106。建议积攒一定量的数据后一次全部共享并控制共享次数。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intents | [InsightIntent](intents-arkts-api-insightintent.md#insightintent-1)[] | 是 | 表示共享的InsightIntent。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当共享操作成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101102 | HUAWEI Assistant has stopped providing services.  适用版本：4.0.0(10)-5.1.0(18) |
| 1000101103 | The switch of the app in the Data source has been turned off.  适用版本：4.0.0(10)-5.1.0(18) |
| 1000101104 | The number of sharing times exceeds the limit. |
| 1000101105 | The size of a single shared data exceeds the limit. |
| 1000101106 | Exceeded the maximum number of sharing times of all applications. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('shareIntent')
          .onClick(() => {
            let playMusicIntent: insightIntent.InsightIntent = {
              intentName: 'PlayMusic',
              intentVersion: '1.0.1',
              identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
              intentActionInfo: {
                actionMode: 'EXECUTED',
                executedTimeSlots: {
                  executedStartTime: 1637393112000,
                  executedEndTime: 1637393212000
                },
                currentPercentage: 50
              },
              intentEntityInfo: {
                entityName: 'Music',
                entityId: 'C10194368',
                entityGroupId: 'C10194321312',
                displayName: '测试歌曲1',
                description: 'NA',
                logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
                keywords: ['华为音乐', '化妆'],
                rankingHint: 99,
                expirationTime: 1637393212000,
                metadataModificationTime: 1637393212000,
                activityType: ['1', '2', '3'],
                artist: ['测试歌手1', '测试歌手2'],
                lyricist: ['测试词作者1', '测试词作者2'],
                composer: ['测试曲作者1', '测试曲作者2'],
                albumName: '测试专辑',
                duration: 244000,
                playCount: 100000,
                musicalGenre: ['流行', '华语', '金曲', '00后'],
                isPublicData: false
              }
            };
            // 共享数据接口  意图数组可以是更多的实体
            // 根据实际代码上下文自行传入合适的context
            insightIntent.shareIntent(this.getUIContext().getHostContext(), [playMusicIntent], (error) => {
              if (error?.code) {
                // 处理业务逻辑错误
                console.error(`shareIntent failed, Code: ${error?.code}, message: ${error?.message}`);
                return;
              }
              // 执行正常业务
              console.info('shareIntent succeed');
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## shareIntent

shareIntent(context: common.BaseContext, intents: InsightIntent[]): Promise<void>

共享已执行或预期的InsightIntent 。使用Promise异步回调。

为避免共享能力滥用，默认每个应用每天最多共享20次，超出限制后会返回错误码：1000101104。每次共享的数据条数不限，但是每次最多50KB数据量，单次数据量超出限制后会返回错误码：1000101105。所有接入方每天共享总次数上限为3000次，超出总次数限制会返回错误码：1000101106。建议积攒一定量的数据后一次全部共享并控制共享次数。

**模型约束：** 该接口仅可在Stage模型下使用。

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
| 1000101102 | HUAWEI Assistant has stopped providing services.  适用版本：4.0.0(10)-5.1.0(18) |
| 1000101103 | The switch of the app in the Data source has been turned off.  适用版本：4.0.0(10)-5.1.0(18) |
| 1000101104 | The number of sharing times exceeds the limit. |
| 1000101105 | The size of a single shared data exceeds the limit. |
| 1000101106 | Exceeded the maximum number of sharing times of all applications. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('shareIntent')
          .onClick(() => {
            let playMusicIntent: insightIntent.InsightIntent = {
              intentName: 'PlayMusic',
              intentVersion: '1.0.1',
              identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
              intentActionInfo: {
                actionMode: 'EXECUTED',
                currentPercentage: 50,
                executedTimeSlots: {
                  executedStartTime: 1637393112000,
                  executedEndTime: 1637393212000
                }
              },
              intentEntityInfo: {
                entityName: 'Music',
                entityId: 'C10194368',
                entityGroupId: '热门',
                displayName: '歌曲名称',
                description: '歌曲解释',
                logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc_logo.png',
                keywords: ['华为音乐', '化妆'],
                rankingHint: 99,
                expirationTime: 1637393212000,
                metadataModificationTime: 1637393212000,
                activityType: ['1', '2', '3'],
                artist: ['张三', '李四'],
                lyricist: ['李四', '张三'],
                composer: ['张三', '李四'],
                albumName: '专辑名称',
                duration: 123456789,
                playCount: 456213123,
                musicalGenre: ['民族风', '摇滚'],
                isPublicData: false
              }
            }

            // 共享数据
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context
            insightIntent.shareIntent(this.getUIContext().getHostContext(), [playMusicIntent]).then(() => {
              console.info('shareIntent succeed');
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, identifiers: string[], callback: AsyncCallback<void>): void

删除InsightIntent。如果设置了identifiers参数，则删除intent名称下的identifiers对应的记录。否则，删除意图名称下的所有记录。使用callback异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intentName | string | 是 | 表示意图的名称。 |
| identifiers | string[] | 是 | 表示意图的标识符。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除操作成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('deleteIntent')
          .onClick(() => {
            // 删除意图下的某些记录
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context和意图标识符
            insightIntent.deleteIntent(this.getUIContext().getHostContext(), 'PlayMusic', ['52dac3b0-6520-4974-81e5-25f0879449b5'], (error) => {
              if (error?.code) {
                // 处理业务逻辑错误
                console.error(`deleteIntent failed, Code: ${error?.code}, message: ${error?.message}`);
                return;
              }
              // 执行正常业务
              console.info('deleteIntent succeed');
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, callback: AsyncCallback<void>): void

删除InsightIntent。清空指定意图名称下的所有记录。使用callback异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| intentName | string | 是 | 表示意图的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除操作成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('deleteIntent')
          .onClick(() => {
            // 删除指定意图下的所有记录
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context和意图标识符
            insightIntent.deleteIntent(this.getUIContext().getHostContext(), 'PlayMusic', (error) => {
              if (error?.code) {
                // 处理业务逻辑错误
                console.error(`deleteIntent failed, Code: ${error?.code}, message: ${error?.message}`);
                return;
              }
              // 执行正常业务
              console.info('deleteIntent succeed');
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, identifiers?: string[]): Promise<void>

删除InsightIntent。如果设置了identifiers参数，则删除intent名称下的identifiers对应的记录。否则，删除意图名称下的所有记录。使用Promise异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

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

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('deleteIntent')
          .onClick(() => {
            // 删除意图下的某些记录
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context和意图标识符
            insightIntent.deleteIntent(this.getUIContext().getHostContext(), 'PlayMusic', ['52dac3b0-6520-4974-81e5-25f0879449b5']).then(() => {
              console.info('deleteIntent succeed');
            })
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## deleteEntity

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string[], callback: AsyncCallback<void>): void

根据实体ID删除InsightIntent实体。使用callback异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

**元服务API**： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.InsightIntent

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[BaseContext](js-apis-inner-application-basecontext.md) | 是 | 表示应用上下文。 |
| entityName | string | 是 | 表示实体的名称。 |
| entityIds | string[] | 是 | 表示实体的id。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除操作成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](intents-arkts-api-errorcodes-insightintent.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1000101101 | The application has not been registered with the InsightIntent. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('deleteEntity')
          .onClick(() => {
            // 删除Entity数据
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context
            insightIntent.deleteEntity(this.getUIContext().getHostContext(), 'PlayMusic', ['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f'], (error) => {
              if (error?.code) {
                // 处理业务逻辑错误
                console.error(`deleteEntity failed, Code: ${error?.code}, message: ${error?.message}`);
                return;
              }
              // 执行正常业务
              console.info('deleteEntity succeed');
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## deleteEntity

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string[]): Promise<void>

根据实体ID删除InsightIntent实体。使用Promise异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

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

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('deleteEntity')
          .onClick(() => {
            // 删除Entity数据
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context
            insightIntent.deleteEntity(this.getUIContext().getHostContext(), 'PlayMusic', ['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f']).then(() => {
              console.info('deleteEntity succeed');
            })
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

## getSid

getSid(context: common.BaseContext, renew: boolean): Promise<string>

获取Service Open ID。使用Promise异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

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
| 1000101103 | The switch of the app in the Data source has been turned off.  适用版本：5.0.0(12)-5.1.0(18) |
| 1000101107 | Too many Service Open ID renew requests. |
| 1000101201 | The service is abnormal. |

**示例：**

```typescript
import { insightIntent } from '@kit.IntentsKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Button('获取Sid')
          .onClick(() => {
            // 获取SID
            // 此处仅为示例，请根据实际代码上下文自行传入合适的context
            insightIntent.getSid(this.getUIContext().getHostContext(), false).then((sid: string) => {
              console.info(`getSid succeed!, sid: ${sid}`);
            })
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center)
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```
