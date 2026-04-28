---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-servicenotification
title: serviceNotification（服务通知）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > serviceNotification（服务通知）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8afb759bae0cb71a3787ab89d19731cb8eb747a679845a99094f3313c57ad68c
---

本模块提供服务通知的基础能力，包括请求订阅通知授权。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { serviceNotification } from '@kit.PushKit';
```

## serviceNotification.requestSubscribeNotification

PhonePC/2in1TabletTVWearable

requestSubscribeNotification(context: Context, entityIds: Array<string>, callback: AsyncCallback<RequestResult>): void

请求订阅通知授权，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 请求订阅通知授权界面[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  context仅支持传入UIAbilityContext。 |
| entityIds | Array<string> | 是 | 模板ID列表。 |
| callback | AsyncCallback<[RequestResult](push-servicenotification.md#requestresult)> | 是 | 回调函数。当请求订阅成功，err为undefined，data为订阅授权结果；否则为错误对象。 |

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

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { serviceNotification } from '@kit.PushKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. const DOMAIN = 0x0000;
6. export default class EntryAbility extends UIAbility {
7. // 入参want与launchParam并未使用，为初始化项目时自带参数
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
9. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
10. try {
11. // entityIds请替换为待订阅的模板ID
12. const entityIds = ['entityId1', 'entityId2', 'entityId3'];
13. serviceNotification.requestSubscribeNotification(this.context, entityIds, (err, data) => {
14. if (err) {
15. hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
16. err.message);
17. } else {
18. hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
19. JSON.stringify(data.entityResult));
20. }
21. });
22. } catch (err) {
23. let e: BusinessError = err as BusinessError;
24. hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
25. e.message);
26. }
27. }
28. }
```

## serviceNotification.requestSubscribeNotification

PhonePC/2in1TabletTVWearable

requestSubscribeNotification(context: Context, entityIds: Array<string>, type?: SubscribeNotificationType): Promise<RequestResult>

请求订阅通知授权，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 请求订阅通知授权界面[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。  **说明：**  context仅支持传入UIAbilityContext。 |
| entityIds | Array<string> | 是 | 表示待订阅的模板ID列表。  当订阅type为SUBSCRIBE\_WITH\_HUAWEI\_ID时，详情请参见[选用订阅模板](../atomic-guides/push-as-service-noti.md#section880418143379)。 |
| type | [SubscribeNotificationType](push-servicenotification.md#subscribenotificationtype) | 否 | 订阅类型。**默认为SUBSCRIBE\_WITH\_TOKEN。**  **说明：**  起始版本：5.0.0(12)。 |

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

说明

错误码1000900030仅当接口在元服务中使用时才涉及。

错误码1000900011可能是推送服务无网被禁网，请到设置 移动网络 -> 流量管理 -> 应用联网，检查推送服务是否被禁网。

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { serviceNotification } from '@kit.PushKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. const DOMAIN = 0x0000;

7. export default class EntryAbility extends UIAbility {
8. onCreate(): void {
9. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
10. try {
11. // entityIds请替换为待订阅的模板ID
12. const entityIds = ['entityId1', 'entityId2', 'entityId3'];
13. let type: serviceNotification.SubscribeNotificationType =
14. serviceNotification.SubscribeNotificationType.SUBSCRIBE_WITH_HUAWEI_ID;
15. serviceNotification.requestSubscribeNotification(this.context, entityIds, type).then((data) => {
16. hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
17. JSON.stringify(data.entityResult));
18. }).catch((err: BusinessError) => {
19. hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
20. err.message);
21. });
22. } catch (err) {
23. let e: BusinessError = err as BusinessError;
24. hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
25. e.message);
26. }
27. }
28. }
```

## RequestResult

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

表示单次订阅中每一个模板订阅的授权结果。

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

PhonePC/2in1TabletTVWearable

表示授权订阅结果，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCEPTED | 0 | 表示模板被接受。 |
| REJECTED | 1 | 表示模板被拒绝。 |
| FILTERED | 2 | 表示模板被过滤。 |
| BANNED | 3 | 表示模板被禁止。 |
| UNKNOWN | -1 | 表示未知错误。 |

## SubscribeNotificationType

PhonePC/2in1TabletTVWearable

表示订阅类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_WITH\_TOKEN | 0 | 表示通过Push Token订阅，**仅应用支持通过Push Token订阅**。 |
| SUBSCRIBE\_WITH\_HUAWEI\_ID | 1 | 表示通过华为账号订阅，**仅元服务支持通过账号订阅**。详情请参见[推送基于账号的订阅消息](../atomic-guides/push-as-send-sub-noti.md)。 |
