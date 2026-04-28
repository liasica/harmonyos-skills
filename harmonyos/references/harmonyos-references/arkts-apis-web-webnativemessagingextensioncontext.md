---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext
title: @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:12+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:9d39f52b23625d88a91c90e94f66292392cb6858ccf7751709c54c81757e9199
---

WebNativeMessagingExtensionContext是Web原生消息扩展的上下文，继承自ExtensionContext。它提供了与WebNativeMessagingExtension通信消息的交互能力。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
```

## WebNativeMessagingExtensionContext

PhonePC/2in1TabletTVWearable

WebNativeMessagingExtensionContext是Web原生消息扩展的上下文，包含所需交互能力。

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options?: StartOptions): Promise<void>

使用Promise异步回调启动Ability。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 表示需要启动的Ability的信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动选项。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码:**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

**示例:**

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
2. import { Want } from '@kit.AbilityKit';

4. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
5. onConnectNative(info: ConnectionInfo): void {
6. const abilityWant: Want = {
7. bundleName: 'com.example.mybundle',
8. abilityName: 'MainAbility'
9. };
10. try {
11. const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
12. context.startAbility(abilityWant);
13. console.info('Ability started successfully');
14. } catch (err) {
15. console.error(`Failed to start ability. Code: ${err.code}, Message: ${err.message}`);
16. }
17. }
18. }
```

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁当前Web原生消息扩展。该方法返回一个Promise对象用于异步处理。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码:**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**示例:**

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

3. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
4. onConnectNative(info: ConnectionInfo): void {
5. try {
6. const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
7. context.terminateSelf();
8. console.info('Extension terminated successfully');
9. } catch (err) {
10. console.error(`Failed to terminate extension. Code: ${err.code}, Message: ${err.message}`);
11. }
12. }
13. }
```

### stopNativeConnection

PhonePC/2in1TabletTVWearable

stopNativeConnection(connectionId: number): Promise<void>

停止指定的本地连接。使用Promise进行异步回调。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connectionId | number | 是 | 要停止的连接ID。取值范围为正整数，必须是有效的连接ID。当connectionId值无效时，会对应返回错误码。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码:**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**示例:**

```
1. import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

3. export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
4. onConnectNative(info: ConnectionInfo): void {
5. const CONNECTION_ID = 12345; // 实际的连接 ID
6. try {
7. const context = this.context;// 获取 WebNativeMessagingExtensionContext 实例
8. context.stopNativeConnection(CONNECTION_ID);
9. console.info('Native connection stopped successfully');
10. } catch (err) {
11. console.error(`Failed to stop native connection. Code: ${err.code}, Message: ${err.message}`);
12. }
13. }
14. }
```
