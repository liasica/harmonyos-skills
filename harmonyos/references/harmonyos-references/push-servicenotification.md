---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-servicenotification
title: serviceNotification（服务通知）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > serviceNotification（服务通知）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:56b47fc706494b886fbfd16d7b723fce669664f174c24bf2ca36f4575916275b
---

为了向用户提供更好的服务和更优的体验，Push Kit为开发者提供了消息订阅能力，支持通过Push Token订阅和通过账号订阅两种类型。通过Push Token订阅可通过申请开通订阅通知消息自分类权益，发送对应的订阅消息。HarmonyOS元服务支持[通过账号订阅](../atomic-guides/push-as-subscription.md)。

开发者在选用订阅模板后，基于该模板向用户发起订阅请求，Push Kit将向用户弹出授权弹窗。仅当用户同意订阅后，开发者方可向用户推送该订阅模板对应的消息，从而实现完整的服务闭环。

本模块为开发者提供消息订阅管理能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { serviceNotification } from '@kit.PushKit';
```

## serviceNotification.requestSubscribeNotification

requestSubscribeNotification(context: Context, entityIds: Array<string>, callback: AsyncCallback<RequestResult>): void

向用户请求订阅消息授权，使用callback异步回调。接口调用间隔需大于1秒。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回错误码1000900017。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 请求订阅消息授权上下文，仅支持传入[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| entityIds | Array<string> | 是 | 待订阅的消息模板ID列表，列表数量最多传入3个。 |
| callback | AsyncCallback<[RequestResult](push-servicenotification.md#requestresult)> | 是 | 接口调用结束的回调函数。当请求订阅成功，err为undefined，data为订阅授权结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900017 | The device does not support current operation. |
| 1000900018 | Number of calls exceeded. |
| 1000900019 | Illegal entity id. |
| 1000900020 | App token is empty. |
| 1000900021 | App is not available or not registered. |
| 1000900022 | Notification switch off. |
| 1000900023 | Number of entity ids exceed the upper limit. |
| 1000900024 | Failed to display subscription UI. |
| 1000900025 | No rights to access entity id. |
| 1000900026 | Illegal entity type. |

**示例：**

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  async onForeground(): Promise<void> {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'onForeground');

    try {
      await this.requestSubscribe();
    } catch (err) {
      const e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'requestSubscribe failed, code=%{public}d, message=%{public}s', e.code, e.message);
    }
  }

  private async requestSubscribe(): Promise<void> {
    // entityIds请替换为待订阅的模板ID
    const entityIds = ['entityId1', 'entityId2', 'entityId3'];
    serviceNotification.requestSubscribeNotification(this.context, entityIds, (err, data) => {
      if (err) {
        const e: BusinessError = err as BusinessError;
        hilog.error(LOG_DOMAIN, LOG_TAG, 'requestSubscribeNotification failed, code=%{public}d, message=%{public}s', e.code, e.message);
      } else {
        hilog.info(LOG_DOMAIN, LOG_TAG, 'requestSubscribeNotification succeeded, result=%{public}s', JSON.stringify(data.entityResult));
      }
    });
  }
}
```

## serviceNotification.requestSubscribeNotification

requestSubscribeNotification(context: Context, entityIds: Array<string>, type?: SubscribeNotificationType): Promise<RequestResult>

向用户请求订阅消息授权，使用Promise异步回调。接口调用间隔需大于1秒。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 请求订阅消息授权上下文，仅支持传入[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |
| entityIds | Array<string> | 是 | 待订阅的消息模板ID列表，列表数量最多传入3个。  当订阅type为SUBSCRIBE\_WITH\_HUAWEI\_ID时，详情请参见[选用订阅模板](../atomic-guides/push-as-service-noti.md#section880418143379)。 |
| type | [SubscribeNotificationType](push-servicenotification.md#subscribenotificationtype) | 否 | 订阅类型。默认为SUBSCRIBE\_WITH\_TOKEN。起始版本：5.0.0(12)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RequestResult](push-servicenotification.md#requestresult)> | Promise对象，返回订阅授权结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900017 | The device does not support current operation. |
| 1000900018 | Number of calls exceeded. |
| 1000900019 | Illegal entity id. |
| 1000900020 | App token is empty. |
| 1000900021 | App is not available or not registered. |
| 1000900022 | Notification switch off. |
| 1000900023 | Number of entity ids exceed the upper limit. |
| 1000900024 | Failed to display subscription UI. |
| 1000900025 | No rights to access entity id. |
| 1000900026 | Illegal entity type. |
| 1000900030 | The user has not logged in with HUAWEI ID. |

**说明** 

错误码1000900030仅当接口在元服务中使用时才涉及。

错误码1000900011可能是推送服务无网被禁网，请到设置 移动网络 -> 流量管理 -> 应用联网，检查推送服务是否被禁网。

**示例：**

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  async onForeground(): Promise<void> {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'onForeground');

    try {
      await this.requestSubscribe();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'requestSubscribe failed, %{public}d %{public}s', e.code, e.message);
    }
  }

  private async requestSubscribe(): Promise<void> {
    // entityIds请替换为待订阅的模板ID
    const entityIds = ['entityId1', 'entityId2', 'entityId3'];
    let type: serviceNotification.SubscribeNotificationType =
      serviceNotification.SubscribeNotificationType.SUBSCRIBE_WITH_HUAWEI_ID;
    serviceNotification.requestSubscribeNotification(this.context, entityIds, type).then((data) => {
      hilog.info(LOG_DOMAIN, LOG_TAG, 'requestSubscribeNotification succeeded, result=%{public}s', JSON.stringify(data.entityResult));
    }).catch((err: BusinessError) => {
      hilog.error(LOG_DOMAIN, LOG_TAG, 'requestSubscribeNotification failed, %{public}d %{public}s', err.code, err.message);
    });
  }
}
```

## serviceNotification.querySubscribeNotificationSetting

querySubscribeNotificationSetting(): Promise<SubscribeNotificationSetting>

查询元服务服务通知配置详情。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SubscribeNotificationSetting](push-servicenotification.md#subscribenotificationsetting)> | Promise对象，返回元服务服务通知配置信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900017 | The device does not support current operation. |
| 1000900021 | App is not available or not registered. |
| 1000900030 | The user has not logged in with HUAWEI ID. |
| 1000900032 | The service notification setting does not exist. |

**示例：**

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';

const LOG_DOMAIN = 0x0000;
const LOG_TAG = 'EntryAbility';

export default class EntryAbility extends UIAbility {
  async onForeground(): Promise<void> {
    hilog.info(LOG_DOMAIN, LOG_TAG, 'onForeground');

    try {
      await this.querySubscribe();
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(LOG_DOMAIN, LOG_TAG, 'querySubscribe failed, %{public}d %{public}s', e.code, e.message);
    }
  }

  /**
   * 查询元服务服务通知配置详情
   */
  private async querySubscribe(): Promise<void> {
    serviceNotification.querySubscribeNotificationSetting().then((data) => {
      hilog.info(LOG_DOMAIN, LOG_TAG,
        `querySubscribeNotificationSetting succeeded, bundle: ${JSON.stringify(data.bundleName)},` +
          ` enable: ${JSON.stringify(data.enable)}, entitySettings: ${JSON.stringify(data.entitySettings)}`);
    }).catch((err: BusinessError) => {
      hilog.error(LOG_DOMAIN, LOG_TAG, 'querySubscribeNotificationSetting failed, %{public}d %{public}s', err.code, err.message);
    });
  }
}
```

## RequestResult

表示单次订阅的授权结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityResult | Array<[EntityResult](push-servicenotification.md#entityresult)> | 是 | 否 | 授权订阅结果。 |

## EntityResult

表示单次订阅中每一个消息模板订阅的授权结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 是 | 否 | 模板ID。 |
| resultCode | [ResultCode](push-servicenotification.md#resultcode) | 是 | 否 | 授权订阅结果码。 |

## ResultCode

表示授权订阅结果，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCEPTED | 0 | 表示用户同意订阅该模板对应的消息。 |
| REJECTED | 1 | 表示用户拒绝订阅该模板对应的消息。 |
| FILTERED | 2 | 表示该模板因标题重复被过滤。 |
| BANNED | 3 | 表示该模板已被下架或禁用。 |
| UNKNOWN | -1 | 表示未知错误。 |

## SubscribeNotificationType

表示订阅类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_WITH\_TOKEN | 0 | 表示通过Push Token订阅，当应用使用通过Push Token订阅能力时，使用该值。 |
| SUBSCRIBE\_WITH\_HUAWEI\_ID | 1 | 表示通过华为账号订阅，当元服务使用通过账号订阅能力时，使用该值。详情请参见[推送基于账号的订阅消息](../atomic-guides/push-as-send-sub-noti.md)。 |

## SubscribeNotificationSetting

表示元服务服务通知配置信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 元服务包名。 |
| enable | boolean | 否 | 是 | 元服务通知总开关，true表示打开元服务通知，false表示关闭元服务通知。 |
| entitySettings | Array<[EntitySetting](push-servicenotification.md#entitysetting)> | 否 | 是 | 服务通知模板信息。 |

## EntitySetting

表示服务通知模板信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 否 | 否 | 模板ID。 |
| entityName | string | 否 | 否 | 模板名称。 |
| enable | boolean | 否 | 是 | 模板开关，true表示打开该模板通知，false表示关闭该模板通知。 |
| entityType | [EntityType](push-servicenotification.md#entitytype) | 否 | 否 | 模板类型。 |

## EntityType

表示订阅消息模板类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ONCE | 0 | 一次性订阅消息模板。 |
| PERIOD | 1 | 长期订阅消息模板。 |
