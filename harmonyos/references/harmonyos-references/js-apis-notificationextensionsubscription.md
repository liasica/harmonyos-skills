---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationextensionsubscription
title: @ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)
breadcrumb: API参考 > 应用服务 > Notification Kit（用户通知服务） > ArkTS API > @ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:783aa8e09422212a9f5a8c72f737ccf9539102e07e828dbdc99269c52fd3075e
---

本模块提供管理通知扩展的能力，具体包括：打开通知扩展订阅设置界面、订阅和取消订阅通知扩展、获取和设置通知授权状态。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { notificationExtensionSubscription } from '@kit.NotificationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

## notificationExtensionSubscription.openSubscriptionSettings

PhonePC/2in1TabletTVWearable

openSubscriptionSettings(context: UIAbilityContext): Promise<void>

打开应用的通知扩展订阅授权页面，以半模态弹窗形式显示。用户可在该页面授权“允许获取本机通知”开关与“已获取的本机通知”应用开关。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 通知设置页面绑定Ability的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600018 | The notification settings window is already displayed. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';

3. try {
4. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. notificationExtensionSubscription.openSubscriptionSettings(context).then(() => {
7. console.info(`openSubscriberSettings success`);
8. }).catch((e:Error) => {
9. let error = e as BusinessError
10. console.error(`failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
11. });
12. } catch (error) {
13. console.error(`failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
14. }
```

## notificationExtensionSubscription.subscribe

PhonePC/2in1TabletTVWearable

subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>

订阅通知扩展。使用[蓝牙模块](../harmonyos-guides/connectivity-kit-intro.md#蓝牙简介)相关接口获取蓝牙设备的唯一地址后方可订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [NotificationExtensionSubscriptionInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo) | 是 | 订阅的信息列表（数组）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**示例：**

```
1. let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[] = [
2. {
3. addr: '01:23:45:67:89:AB', // 使用动态获取的蓝牙地址
4. type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
5. }
6. ];
7. notificationExtensionSubscription.subscribe(infos).then(() => {
8. console.info("subscribe success");
9. }).catch((err: BusinessError) => {
10. console.error(`subscribe fail: ${JSON.stringify(err)}`);
11. });
```

## notificationExtensionSubscription.unsubscribe

PhonePC/2in1TabletTVWearable

unsubscribe(): Promise<void>

取消通知扩展的订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. notificationExtensionSubscription.unsubscribe().then(() => {
2. console.info("unsubscribe success");
3. }).catch((err: BusinessError) => {
4. console.error(`unsubscribe fail: ${JSON.stringify(err)}`);
5. });
```

## notificationExtensionSubscription.getSubscribeInfo

PhonePC/2in1TabletTVWearable

getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>

获取当前应用的通知扩展订阅信息。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NotificationExtensionSubscriptionInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo)> | Promise对象，返回一个[NotificationExtensionSubscriptionInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo)对象数组，表示应用的订阅信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. notificationExtensionSubscription.getSubscribeInfo().then((data: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[]) => {
2. console.info(`getSubscribeInfo successfully. Data: ${JSON.stringify(data)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`getSubscribeInfo fail: ${JSON.stringify(err)}`);
5. });
```

## notificationExtensionSubscription.isUserGranted

PhonePC/2in1TabletTVWearable

isUserGranted(): Promise<boolean>

查询“允许获取本机通知”的开关状态。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示功能已启用；返回false表示功能未启用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. notificationExtensionSubscription.isUserGranted().then((isOpen: boolean) => {
2. if (isOpen) {
3. console.info('isUserGranted true');
4. } else {
5. console.info('isUserGranted false');
6. }
7. }).catch((err: BusinessError) => {
8. console.error(`isUserGranted fail: ${JSON.stringify(err)}`);
9. });
```

## notificationExtensionSubscription.getUserGrantedEnabledBundles

PhonePC/2in1TabletTVWearable

getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>

获取指定应用中“已获取的本机通知”通知开关开启的应用列表。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE\_NOTIFICATION

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GrantedBundleInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcommondef#grantedbundleinfo22)> | Promise对象，返回获取指定应用中“已获取的本机通知”通知开关开启的应用列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[通知错误码](errorcode-notification.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
1. notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data: notificationExtensionSubscription.GrantedBundleInfo[]) => {
2. console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`getUserGrantedEnabledBundles fail: ${JSON.stringify(err)}`);
5. });
```

## NotificationExtensionSubscriptionInfo

PhonePC/2in1TabletTVWearable

type NotificationExtensionSubscriptionInfo = \_NotificationExtensionSubscriptionInfo

用于描述通知扩展订阅的信息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationExtensionSubscriptionInfo](s-apis-inner-notificationextensionsubscriptioninfo.md) | 用于描述通知扩展订阅的信息。 |

## NotificationInfo

PhonePC/2in1TabletTVWearable

type NotificationInfo = \_NotificationInfo

通知订阅扩展能力中[onReceiveMessage](js-apis-notificationsubscriberextensionability.md#onreceivemessage)回调的通知信息。

**系统能力**：SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_NotificationInfo](js-apis-inner-notification-notificationinfo.md) | 通知订阅扩展能力中[onReceiveMessage](js-apis-notificationsubscriberextensionability.md#onreceivemessage)回调的通知信息。 |

## SubscribeType

PhonePC/2in1TabletTVWearable

表示通知扩展订阅的类型。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLUETOOTH | 0 | 通过蓝牙订阅通知。 |

## BundleOption

PhonePC/2in1TabletTVWearable

type BundleOption = \_BundleOption

指定应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_BundleOption](js-apis-inner-notification-notificationcommondef.md#bundleoption) | 指定应用的包信息。 |

## GrantedBundleInfo

PhonePC/2in1TabletTVWearable

type GrantedBundleInfo = \_GrantedBundleInfo

授权应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

| 类型 | 说明 |
| --- | --- |
| [\_GrantedBundleInfo](js-apis-inner-notification-notificationcommondef.md#grantedbundleinfo22) | 授权应用的包信息。 |
