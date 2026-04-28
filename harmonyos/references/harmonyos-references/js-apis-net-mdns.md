---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns
title: @ohos.net.mdns (MDNS管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.mdns (MDNS管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8df6d96e8a0ed7e5d9cd86031ab27c64faf3766e1daad4d59dede07fc612c75
---

MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、移除、发现、解析等能力。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { mdns } from '@kit.NetworkKit';
```

## mdns.addLocalService

PhonePC/2in1TabletTVWearable

addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

添加一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | mDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 是 | 回调函数。成功添加时error为undefined，data为添加到本地的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let localServiceInfo: mdns.LocalServiceInfo = {
9. serviceType: "_print._tcp",
10. serviceName: "servicename",
11. port: 5555,
12. host: {
13. address: "10.14.**.***",
14. },
15. serviceAttribute: [{key: "111", value: [1]}]
16. }

18. mdns.addLocalService(context, localServiceInfo, (error:BusinessError, data:mdns.LocalServiceInfo) =>  {
19. console.error(JSON.stringify(error));
20. console.info(JSON.stringify(data));
21. });
```

## mdns.addLocalService

PhonePC/2in1TabletTVWearable

addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

添加一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 以Promise形式返回添加的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let localServiceInfo: mdns.LocalServiceInfo = {
9. serviceType: "_print._tcp",
10. serviceName: "servicename",
11. port: 5555,
12. host: {
13. address: "10.14.**.***",
14. },
15. serviceAttribute: [{key: "111", value: [1]}]
16. }

18. mdns.addLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
19. console.info(JSON.stringify(data));
20. });
```

## mdns.removeLocalService

PhonePC/2in1TabletTVWearable

removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

移除一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | MDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 是 | 回调函数。成功移除error为undefined，data为移除本地的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let localServiceInfo: mdns.LocalServiceInfo = {
9. serviceType: "_print._tcp",
10. serviceName: "servicename",
11. port: 5555,
12. host: {
13. address: "10.14.**.***",
14. },
15. serviceAttribute: [{key: "111", value: [1]}]
16. }

18. mdns.removeLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
19. console.error(JSON.stringify(error));
20. console.info(JSON.stringify(data));
21. });
```

## mdns.removeLocalService

PhonePC/2in1TabletTVWearable

removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

移除一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 以Promise形式返回移除的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

7. let localServiceInfo: mdns.LocalServiceInfo = {
8. serviceType: "_print._tcp",
9. serviceName: "servicename",
10. port: 5555,
11. host: {
12. address: "10.14.**.***",
13. },
14. serviceAttribute: [{key: "111", value: [1]}]
15. }

17. mdns.removeLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
18. console.info(JSON.stringify(data));
19. });
```

## mdns.createDiscoveryService

PhonePC/2in1TabletTVWearable

createDiscoveryService(context: Context, serviceType: string): DiscoveryService

返回一个DiscoveryService对象，该对象用于发现指定服务类型（serviceType）的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceType | string | 是 | 需要发现的MDNS服务类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DiscoveryService | 基于指定服务类型（serviceType）和Context的发现服务对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let serviceType = "_print._tcp";
9. let discoveryService : Object = mdns.createDiscoveryService(context, serviceType);
```

## mdns.resolveLocalService

PhonePC/2in1TabletTVWearable

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

解析一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | MDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 是 | 回调函数。成功移除error为undefined，data为解析的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let localServiceInfo: mdns.LocalServiceInfo = {
9. serviceType: "_print._tcp",
10. serviceName: "servicename",
11. port: 5555,
12. host: {
13. address: "10.14.**.***",
14. },
15. serviceAttribute: [{key: "111", value: [1]}]
16. }

18. mdns.resolveLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
19. console.error(JSON.stringify(error));
20. console.info(JSON.stringify(data));
21. });
```

## mdns.resolveLocalService

PhonePC/2in1TabletTVWearable

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

解析一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| serviceInfo | [LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 以Promise形式返回解析的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](errorcode-net-mdns.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

8. let localServiceInfo: mdns.LocalServiceInfo = {
9. serviceType: "_print._tcp",
10. serviceName: "servicename",
11. port: 5555,
12. host: {
13. address: "10.14.**.***",
14. },
15. serviceAttribute: [{key: "111", value: [1]}]
16. }

18. mdns.resolveLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
19. console.info(JSON.stringify(data));
20. });
```

## DiscoveryService

PhonePC/2in1TabletTVWearable

指定服务类型的发现服务对象。

### startSearchingMDNS

PhonePC/2in1TabletTVWearable

startSearchingMDNS(): void

开始搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();
```

### stopSearchingMDNS

PhonePC/2in1TabletTVWearable

stopSearchingMDNS(): void

停止搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

Stage模型示例：

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 获取context。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.stopSearchingMDNS();
```

### on('discoveryStart')

PhonePC/2in1TabletTVWearable

on(type: 'discoveryStart', callback: Callback<DiscoveryEventInfo>): void

订阅开启监听mDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'discoveryStart'。  discoveryStart：开始搜索局域网内的MDNS服务事件。 |
| callback | Callback<[DiscoveryEventInfo](js-apis-net-mdns.md#discoveryeventinfo11)> | 是 | MDNS服务的信息和事件错误信息。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();
```

### off('discoveryStart')

PhonePC/2in1TabletTVWearable

off(type: 'discoveryStart', callback?: Callback<DiscoveryEventInfo>): void

取消开启监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件，固定为'discoveryStart'。  discoveryStart：开始搜索局域网内的MDNS服务事件。 |
| callback | Callback<[DiscoveryEventInfo](js-apis-net-mdns.md#discoveryeventinfo11)> | 否 | MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();

17. discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
18. console.info(JSON.stringify(data));
19. });
```

### on('discoveryStop')

PhonePC/2in1TabletTVWearable

on(type: 'discoveryStop', callback: Callback<DiscoveryEventInfo>): void

订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'discoveryStop'。  discoveryStop：停止搜索局域网内的MDNS服务事件。 |
| callback | Callback<[DiscoveryEventInfo](js-apis-net-mdns.md#discoveryeventinfo11)> | 是 | MDNS服务的信息和事件错误信息。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();
```

### off('discoveryStop')

PhonePC/2in1TabletTVWearable

off(type: 'discoveryStop', callback?: Callback<[DiscoveryEventInfo](js-apis-net-mdns.md#discoveryeventinfo11)>): void

取消订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件'discoveryStop'。  discoveryStop：停止搜索局域网内的MDNS服务事件。 |
| callback | Callback<[DiscoveryEventInfo](js-apis-net-mdns.md#discoveryeventinfo11)> | 否 | MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();

17. discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
18. console.info(JSON.stringify(data));
19. });
```

### on('serviceFound')

PhonePC/2in1TabletTVWearable

on(type: 'serviceFound', callback: Callback<LocalServiceInfo>): void

订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'serviceFound'。  serviceFound：发现MDNS服务事件。 |
| callback | Callback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 是 | MDNS服务的信息，需调用resolveLocalService解析这个MDNS服务信息。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
12. console.info('serviceFound', JSON.stringify(data));
13. mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
14. console.info('serviceFound', JSON.stringify(resolveData));
15. });
16. });

18. discoveryService.stopSearchingMDNS();
```

### off('serviceFound')

PhonePC/2in1TabletTVWearable

off(type: 'serviceFound', callback?: Callback<LocalServiceInfo>): void

取消订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件，固定为'serviceFound'。  serviceFound：发现MDNS服务事件。 |
| callback | Callback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 否 | MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
12. console.info('serviceFound', JSON.stringify(data));
13. mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
14. console.info('serviceFound', JSON.stringify(resolveData));
15. });
16. });

18. discoveryService.stopSearchingMDNS();

20. discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
21. console.info(JSON.stringify(data));
22. });
```

### on('serviceLost')

PhonePC/2in1TabletTVWearable

on(type: 'serviceLost', callback: Callback<LocalServiceInfo>): void

订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅事件，固定为'serviceLost'。  serviceLost：移除MDNS服务事件。 |
| callback | Callback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 是 | MDNS服务的信息。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();
```

### off('serviceLost')

PhonePC/2in1TabletTVWearable

off(type: 'serviceLost', callback?: Callback<LocalServiceInfo>): void

取消订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件，固定为'serviceLost'。  serviceLost：移除MDNS服务事件。 |
| callback | Callback<[LocalServiceInfo](js-apis-net-mdns.md#localserviceinfo)> | 否 | MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { mdns } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. // 参考mdns.createDiscoveryService。
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let serviceType = "_print._tcp";
8. let discoveryService = mdns.createDiscoveryService(context, serviceType);
9. discoveryService.startSearchingMDNS();

11. discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
12. console.info(JSON.stringify(data));
13. });

15. discoveryService.stopSearchingMDNS();

17. discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
18. console.info(JSON.stringify(data));
19. });
```

## LocalServiceInfo

PhonePC/2in1TabletTVWearable

MDNS服务信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceType | string | 否 | 否 | MDNS服务的类型。格式：\_<name>.<\_tcp/\_udp>，name长度小于63字符并且不能包含字符'.'。 |
| serviceName | string | 否 | 否 | MDNS服务的名字。 |
| port | number | 否 | 是 | MDNS服务的端口号。取值范围[0，65535]。 |
| host | [NetAddress](js-apis-net-connection.md#netaddress) | 否 | 是 | MDNS服务设备的IP地址。采用设备的IP，添加服务和移除服务时候不生效。 |
| serviceAttribute | Array<[ServiceAttribute](js-apis-net-mdns.md#serviceattribute)> | 否 | 是 | MDNS服务属性信息。 |

## ServiceAttribute

PhonePC/2in1TabletTVWearable

MDNS服务属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | MDNS服务属性键值，键值长度应该小于9个字符。 |
| value | Array<number> | 否 | 否 | MDNS服务属性值。 |

## DiscoveryEventInfo11+

PhonePC/2in1TabletTVWearable

监听到的MDNS服务事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceInfo | LocalServiceInfo | 否 | 否 | MDNS服务信息。 |
| errorCode | MdnsError | 否 | 是 | MDNS错误信息。 |

## MdnsError

PhonePC/2in1TabletTVWearable

MDNS错误信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL\_ERROR | 0 | 内部错误导致操作失败。 |
| ALREADY\_ACTIVE | 1 | 服务已经存在导致操作失败。 |
| MAX\_LIMIT | 2 | 请求超过最大限制导致操作失败。 |

## NetAddress

PhonePC/2in1TabletTVWearable

type NetAddress = connection.NetAddress

获取网络地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.NetAddress | 定义网络地址。 |
