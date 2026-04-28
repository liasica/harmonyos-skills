---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-pushservice
title: pushService（推送服务基础能力）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > pushService（推送服务基础能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c0e99531f5a8c1c811f055c29a579b8e5e16165965758c7f39b734233058f8b
---

本模块提供Push Kit（推送服务）的基础能力，包括获取和删除推送服务Token、绑定和解绑账号、接收场景化消息、注册和解除注册token更新，以及注册和解除注册分布式消息接收事件监听的功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { pushService } from '@kit.PushKit';
```

## pushService.getToken

PhonePC/2in1TabletTVWearable

getToken(callback: AsyncCallback<string>): void

获取推送服务的Token，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。Token获取成功时，字符长度为112，err为undefined；Token获取失败时返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900012 | Push rights are not activated. |
| 1000900013 | Cross-location application is not allowed to obtain the token. |
| 1000900014 | The device does not support getting token. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // data为获取的应用推送服务的Token
7. pushService.getToken((err: BusinessError, data: string) => {
8. if (err) {
9. hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
10. } else {
11. hilog.info(0x0000, 'testTag', 'Succeeded in getting push token');
12. }
13. });
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
17. }
```

## pushService.getToken

PhonePC/2in1TabletTVWearable

getToken(): Promise<string>

获取推送服务的Token，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回Token，字符长度为112。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900012 | Push rights are not activated. |
| 1000900013 | Cross-location application is not allowed to obtain the token. |
| 1000900014 | The device does not support getting token. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // data为获取的应用推送服务的Token
7. pushService.getToken().then((data: string) => {
8. hilog.info(0x0000, 'testTag', 'Succeeded in getting push token.');
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
11. });
12. } catch (err) {
13. let e: BusinessError = err as BusinessError;
14. hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
15. }
```

## pushService.deleteToken

PhonePC/2in1TabletTVWearable

deleteToken(callback: AsyncCallback<void>): void

删除推送服务的Token，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除Token成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. pushService.deleteToken((err: BusinessError) => {
7. if (err) {
8. hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
9. } else {
10. hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
11. }
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
16. }
```

## pushService.deleteToken

PhonePC/2in1TabletTVWearable

deleteToken(): Promise<void>

删除推送服务的Token，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. pushService.deleteToken().then(() => {
7. hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
10. });
11. } catch (err) {
12. let e: BusinessError = err as BusinessError;
13. hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
14. }
```

## pushService.bindAppProfileId

PhonePC/2in1TabletTVWearable

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string, callback: AsyncCallback<void>): void

绑定应用内账号匿名标识，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileType | pushCommon.[AppProfileType](push-pushcommon.md#appprofiletype) | 是 | 绑定账号类型，分为华为账号和应用账号。 |
| appProfileId | string | 是 | 账号匿名标识，不可为空字符串。不建议使用真实的账号id，推荐使用账号id自行生成对应的匿名标识，能与该账号id建立唯一映射关系即可，生成算法无限制。最大长度为64，若长度超限，调用REST API接口会报错。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当绑定应用内账号成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900015 | The number of bound profile-app relationships exceeds the maximum. |
| 1000900016 | The os distributed account is not logged in. |

**示例：**

```
1. import { pushService, pushCommon } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义需要绑定的profileId
6. const profileId: string = '1****9';
7. try {
8. pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE_TYPE_APPLICATION_ACCOUNT, profileId, (err: BusinessError) => {
9. if (err) {
10. hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
11. } else {
12. hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
13. }
14. });
15. } catch (err) {
16. let e: BusinessError = err as BusinessError;
17. hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
18. }
```

## pushService.bindAppProfileId

PhonePC/2in1TabletTVWearable

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string): Promise<void>

绑定应用内账号匿名标识，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、PC/2in1、Tablet、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileType | pushCommon.[AppProfileType](push-pushcommon.md#appprofiletype) | 是 | 绑定账号类型，分为华为账号和应用账号。 |
| appProfileId | string | 是 | 账号匿名标识，不可为空字符串。不建议使用真实的账号id，推荐使用账号id自行生成对应的匿名标识，能与该账号id建立唯一映射关系即可，生成算法无限制。最大长度为64，若长度超限，调用REST API接口会报错。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900015 | The number of bound profile-app relationships exceeds the maximum. |
| 1000900016 | The os distributed account is not logged in. |

**示例：**

```
1. import { pushService, pushCommon } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义需要绑定的profileId
6. const profileId: string = '1****9';
7. try {
8. // 绑定应用账号
9. pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE_TYPE_APPLICATION_ACCOUNT, profileId).then(() => {
10. hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
11. }).catch((err: BusinessError) => {
12. hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
13. });
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
17. }
```

## pushService.unbindAppProfileId

PhonePC/2in1TabletTVWearable

unbindAppProfileId(appProfileId: string, callback: AsyncCallback<void>): void

解绑应用内账号匿名标识，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileId | string | 是 | 账号匿名标识，配置为调用[bindAppProfileId](push-pushservice.md#pushservicebindappprofileid-1)()时设置的appProfileId。最大长度为64，若长度超限，调用REST API接口会报错。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解绑应用内账号成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义需要解绑的profileId
6. const profileId: string = '1****9';
7. try {
8. pushService.unbindAppProfileId(profileId, (err: BusinessError) => {
9. if (err) {
10. hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
11. } else {
12. hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
13. }
14. });
15. } catch (err) {
16. let e: BusinessError = err as BusinessError;
17. hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
18. }
```

## pushService.unbindAppProfileId

PhonePC/2in1TabletTVWearable

unbindAppProfileId(appProfileId: string): Promise<void>

解绑应用内账号匿名标识，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileId | string | 是 | 账号匿名标识，配置为调用[bindAppProfileId](push-pushservice.md#pushservicebindappprofileid-1)()时设置的appProfileId。最大长度为64，若长度超限，调用REST API接口会报错。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |

**示例：**

```
1. import { pushService } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义需要解绑的profileId
6. const profileId: string = '1****9';
7. try {
8. pushService.unbindAppProfileId(profileId).then(() => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
10. }).catch((err: BusinessError) => {
11. hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
16. }
```

## pushService.PushType

PhonePC/2in1TabletTVWearable

type PushType = 'DEFAULT' |'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY'

场景化消息类型，取值类型为下表类型中的并集。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 5.0.2(14)

| 类型 | 说明 |
| --- | --- |
| 'DEFAULT' | 通知消息场景。 |
| 'IM' | 语音播报消息场景。 |
| 'VoIP' | 应用内通话消息场景。 |
| 'BACKGROUND' | 后台消息场景。 |
| 'EMERGENCY' | 紧急事件消息场景。 |

## pushService.receiveMessage

PhonePC/2in1TabletTVWearable

receiveMessage(pushType: PushType, ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void

接收Push场景化消息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pushType | [PushType](push-pushservice.md#pushservicepushtype) | 是 | 场景化消息类型。  **说明：**  · pushService.PushType中EMERGENCY（紧急事件消息场景）起始版本：5.0.0(12)。本场景仅为地震灾害等特殊场景使用。  · pushService.PushType中DEFAULT（通知消息场景）起始版本：5.0.2(14)。调用示例代码请参考[应用在前台时处理通知消息](../harmonyos-guides/push-send-alert.md#应用在前台时处理通知消息)中步骤3。  · IM（语音播报消息场景）调用示例代码请参考[开发步骤](../harmonyos-guides/push-send-extend-noti.md#开发步骤)中步骤3。  · VoIP（应用内通话消息场景）  调用示例代码请参考[开发步骤](../harmonyos-guides/push-voip.md#开发步骤)中步骤2。  · BACKGROUND（后台消息场景）  调用示例代码请参考[开发步骤](../harmonyos-guides/push-background.md#开发步骤)中步骤5。 |
| ability | [Ability](js-apis-app-ability-ability.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)。 |
| onMessage | Callback<pushCommon.[PushPayload](push-pushcommon.md#pushpayload)> | 是 | 回调函数，返回接收场景化消息的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900005 | Messages of the same push type cannot be received repeatedly. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { pushService, pushCommon } from '@kit.PushKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 无需新增UIAbility，在原有UIAbility的onCreate方法中调用即可。以PushMessageAbility为例
7. export default class PushMessageAbility extends UIAbility {
8. // onCreate()为同步接口，不支持异步回调
9. onCreate(): void {
10. try {
11. // receiveMessage()不能放在异步方法之后，否则可能影响消息接收
12. // 注册BACKGROUND场景化消息
13. pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
14. // process message，并建议对Callback进行try-catch
15. try {
16. hilog.info(0x0000, 'testTag', 'Receive background message : %{public}s', JSON.stringify(data));
17. } catch (e) {
18. let errRes: BusinessError = e as BusinessError;
19. hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
20. }
21. });
22. } catch (err) {
23. let e: BusinessError = err as BusinessError;
24. hilog.error(0x0000, 'testTag', 'Failed to receive message: %{public}d %{public}s', e.code, e.message);
25. }
26. }
27. }
```

## pushService.on('tokenUpdate')

PhonePC/2in1TabletTVWearable

on(type: 'tokenUpdate', ability: Ability, callback: Callback<string>): void

注册token更新，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Wearable中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tokenUpdate'，即token更新事件。 |
| ability | [Ability](js-apis-app-ability-ability.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)，包含UI界面的应用组件。 |
| callback | Callback<string> | 是 | 回调函数，返回token更新的数据。Token长度为112。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { pushService } from '@kit.PushKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 无需新增UIAbility，在原有UIAbility的onCreate方法中调用即可。以PushMessageAbility为例
7. export default class PushMessageAbility extends UIAbility {
8. onCreate(): void {
9. const callBack = (data: string) => {
10. try {
11. hilog.info(0x0000, 'testTag', 'update token: %{public}s', data);
12. } catch (e) {
13. let err: BusinessError = e as BusinessError;
14. hilog.error(0x0000, 'testTag', 'Failed to update data: %{public}d %{public}s', err.code, err.message);
15. }
16. }

18. try {
19. // 注册token更新回调场景
20. pushService.on('tokenUpdate', this, callBack);
21. hilog.info(0x0000, 'testTag', 'Register on success');
22. } catch (e) {
23. let err: BusinessError = e as BusinessError;
24. hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', err.code, err.message);
25. }
26. }
27. }
```

## pushService.off('tokenUpdate')

PhonePC/2in1TabletTVWearable

off(type: 'tokenUpdate', callback?: Callback<string>): void

解除注册token更新，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Wearable中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tokenUpdate'，即token更新事件。 |
| callback | Callback<string> | 否 | 回调函数，用于取消注册tokenUpdate监听事件。  注：若取消注册时不传入callback，则会取消注册tokenUpdate事件下所有的callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { pushService } from '@kit.PushKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 无需新增UIAbility，在原有UIAbility的onDestroy方法中调用即可。以PushMessageAbility为例
7. export default class PushMessageAbility extends UIAbility {
8. onDestroy(): void {
9. try {
10. // 解除注册token更新回调场景
11. pushService.off('tokenUpdate');
12. hilog.info(0x0000, 'testTag', 'Register off success');
13. } catch (e) {
14. let err: BusinessError = e as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', err.code, err.message);
16. }
17. }
18. }
```

## pushService.on('distributedMessageReceive')

PhonePC/2in1TabletTVWearable

on(type: 'distributedMessageReceive', callee: Callee, callback: DistributedMessageCallback): void

注册分布式消息接收事件监听，使用callback异步回调。应用需要在UIAbility的onCreate()方法进行注册，每个应用只能注册一次。该UIAbility对应action为**action.ohos.push.distribute.listener**。

说明

若调用接收场景化消息接口（[pushService.receiveMessage](push-pushservice.md#pushservicereceivemessage)）和注册分布式消息事件在同一个UIAbility中，则action.ohos.push.distribute.listener和action.ohos.push.listener定义在同一个actions数组中，否则分别定义在对应UIAbility中的actions中。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'distributedMessageReceive'，即分布式消息接收事件。 |
| callee | [Callee](js-apis-app-ability-uiability.md#callee) | 是 | 通用组件服务端注册和解除客户端[Caller](js-apis-app-ability-uiability.md#caller)通知送信的callback接口，从[UIAbility](js-apis-app-ability-uiability.md)中获取。 |
| callback | [DistributedMessageCallback](push-pushservice.md#distributedmessagecallback) | 是 | 回调函数，注册分布式消息接收事件监听的回调，在收到分布式消息后异步执行。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900031 | The same type of callback can be registered only once. |
| 1000900001 | System internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { pushService, pushCommon } from '@kit.PushKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class PushMessageAbility extends UIAbility {
7. private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
8. let resultCode = pushService.ResultCode.SUCCESS;
9. try {
10. hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
11. // 处理业务逻辑，如将数据内容发布到穿戴设备上等
12. } catch (e) {
13. resultCode = pushService.ResultCode.FAILED;
14. let errRes: BusinessError = e as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
16. }
17. // 处理结束后，返回执行结果
18. return { resultCode };
19. };

21. onCreate(): void {
22. try {
23. // 注册distributeMessageReceive分布式消息接收回调场景
24. pushService.on('distributedMessageReceive', this.callee, this.callback);
25. } catch (err) {
26. let e: BusinessError = err as BusinessError;
27. hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', e.code, e.message);
28. }
29. }
30. }
```

## pushService.off('distributedMessageReceive')

PhonePC/2in1TabletTVWearable

off(type: 'distributedMessageReceive', callback?: DistributedMessageCallback): void

解除注册分布式消息接收事件监听，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'distributedMessageReceive'即分布式消息接收事件。 |
| callback | [DistributedMessageCallback](push-pushservice.md#distributedmessagecallback) | 否 | 回调函数，用于取消注册distributedMessageReceive监听事件。取消注册后，应用无法在该callback方法中接收分布式消息。  注：若取消注册时不传入callback，则会取消注册distributedMessageReceive事件下所有的callback。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { pushCommon, pushService } from '@kit.PushKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class PushMessageAbility extends UIAbility {
7. private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
8. let resultCode = pushService.ResultCode.SUCCESS;
9. try {
10. hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
11. // 处理业务逻辑，如将数据内容发布到穿戴设备上等
12. } catch (e) {
13. resultCode = pushService.ResultCode.FAILED;
14. let errRes: BusinessError = e as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
16. }
17. // 处理结束后，返回执行结果
18. return { resultCode };
19. };

21. onDestroy(): void {
22. try {
23. // 解除注册distributedMessageReceive分布式消息接收回调场景
24. pushService.off('distributedMessageReceive', this.callback);
25. hilog.info(0x0000, 'testTag', 'Register off success');
26. } catch (err) {
27. let e: BusinessError = err as BusinessError;
28. hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', e.code, e.message);
29. }
30. }
31. }
```

## DistributedMessageCallback

PhonePC/2in1TabletTVWearable

type DistributedMessageCallback = (PushPayload: pushCommon.PushPayload) => Promise<DistributedMessageResult>

分布式消息接收事件中使用的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| PushPayload | pushCommon.[PushPayload](push-pushcommon.md#pushpayload) | 是 | 分布式消息数据的参数定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DistributedMessageResult> | Promise对象。返回DistributedMessageResult对象，见[DistributedMessageResult](push-pushservice.md#distributedmessageresult)说明。 |

## DistributedMessageResult

PhonePC/2in1TabletTVWearable

distributedMessageReceive事件中使用的回调类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | [ResultCode](push-pushservice.md#resultcode) | 否 | 否 | 回调函数执行结果，枚举类型，见枚举[ResultCode](push-pushservice.md#resultcode)说明。 |

## ResultCode

PhonePC/2in1TabletTVWearable

表示[DistributedMessageCallback](push-pushservice.md#distributedmessagecallback)回调函数执行结果的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于6.1.0(23)以前版本，该枚举值在Phone、Tablet中可正常使用，在其他设备类型中无效果。对于6.1.0(23)及之后版本，该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAILED | 1 | 执行失败。 |
