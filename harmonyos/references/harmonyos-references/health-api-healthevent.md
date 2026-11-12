---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthevent
title: healthEvent (场景化健康事件服务)
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > ArkTS API > healthEvent (场景化健康事件服务)
category: harmonyos-references
scraped_at: 2026-11-12T09:57:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4f4c49869a857734708e5874f5cae8ae0526cbac82fe32bd90e94c7de23097b2
---

本模块提供场景化健康事件服务。

**起始版本：** 26.0.1

## 导入模块

```typescript
import { healthService } from '@kit.HealthServiceKit';
```

**说明** 

此模块为healthService子模块，需通过healthService.healthEvent方式使用。

## HealthEvent

健康事件类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 可选 | **说明** |
| --- | --- | --- | --- |
| eventId | number | 否 | 健康事件ID。 |
| eventName | string | 是 | 健康事件名称，若未填写，默认为空。 |

## 常量

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | **只读** | **说明** |
| --- | --- | --- | --- |
| sos | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | SOS事件。 |
| sleep | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | 睡眠状态事件。 |
| heartRate | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | 心率过高/过低提醒事件。 |
| bloodOxygen | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | 血氧偏低提醒事件。 |
| fallDetect | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | 跌倒检测事件。 |
| highlandCare | [HealthEvent](health-api-healthevent.md#healthevent) | 是 | 高原关怀事件。 |

## SubscribeOptions

订阅选项。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 可选 | **说明** |
| --- | --- | --- | --- |
| abilityName | string | 是 | 订阅接收方的abilityName，默认值为"HealthEventAbility"。 |

## EventSource

健康事件来源。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 可选 | **说明** |
| --- | --- | --- | --- |
| deviceName | string | 否 | 健康事件来源的设备名称。 |

## EventData

健康事件数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

| **名称** | **类型** | 可选 | **说明** |
| --- | --- | --- | --- |
| eventType | [HealthEvent](health-api-healthevent.md#healthevent) | 否 | 健康事件类型。 |
| eventSource | [EventSource](health-api-healthevent.md#eventsource) | 否 | 健康事件来源。 |
| eventTime | number | 否 | 健康事件时间，Unix时间戳，单位：ms。 |
| extraData | Map<string, object> | 是 | 健康事件附加数据，若未填写，默认为空。 |

## HealthEventExtensionAbility

健康事件接收器，继承自[DistributedExtensionAbility](../doccenter-references/api/js-apis-distributedextensionability.md)。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

### onHealthEvent

onHealthEvent(eventData: EventData): AbilityConstant.CollaborateResult

接收健康事件数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| eventData | [EventData](health-api-healthevent.md#eventdata) | 是 | 健康事件数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityConstant.CollaborateResult](../doccenter-references/api/js-apis-app-ability-abilityconstant.md#collaborateresult18) | 应用协同状态。 |

## healthEvent.onEvent

onEvent(eventList: HealthEvent[], option?: SubscribeOptions): Promise<void>

订阅健康事件，使用Promise异步回调。

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| eventList | [HealthEvent](health-api-healthevent.md#healthevent)[] | 是 | 健康事件列表。 |
| option | [SubscribeOptions](health-api-healthevent.md#subscribeoptions) | 否 | 订阅选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-healthservice.md#health-service-kit调用失败返回201) | Permission verification failed. |
| [1009100001](errorcode-healthservice.md#section1009100001-不支持的事件类型) | Unsupported event types. |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.healthEvent.onEvent([healthService.healthEvent.sos]);
  hilog.info(0x0000, 'testTag', 'Succeeded in subscribing health event');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to subscribe health event. Code: ${err.code}, message: ${err.message}`);
}
```

## healthEvent.offEvent

offEvent(eventList: HealthEvent[]): Promise<void>

取消订阅健康事件，使用Promise异步回调。

**说明** 

上述接口调用前，需先使用[init](health-api-healthstore.md#healthstoreinit)方法进行初始化。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| eventList | [HealthEvent](health-api-healthevent.md#healthevent)[] | 是 | 健康事件列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](errorcode-healthservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1009104999](errorcode-healthservice.md#section1009104999-通用错误码) | System internal error. |

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.healthEvent.offEvent([healthService.healthEvent.sos]);
  hilog.info(0x0000, 'testTag', 'Succeeded in unsubscribing health event');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to unsubscribe health event. Code: ${err.code}, message: ${err.message}`);
}
```
