---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager
title: @ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:13+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:8d63f933b5f8edf1d848fa9820b37a058a4a1e53eef0e3b852068663244a7b50
---

webNativeMessagingExtensionManager模块提供基于Web标准的消息扩展管理能力。

说明

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
```

## ConnectionNativeInfo

PhonePC/2in1TabletTVWearable

表示Web原生消息连接的连接信息。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectionId | number | 否 | 否 | 连接ID。 |
| bundleName | string | 否 | 否 | Web原生消息扩展应用的包名。 |
| extensionOrigin | string | 否 | 否 | 浏览器扩展的源URL。 |
| extensionPid | number | 否 | 否 | Web原生消息扩展的进程ID。 |

## NmErrorCode

PhonePC/2in1TabletTVWearable

Native Messaging的错误列表。

**系统能力**：SystemCapability.Web.Webview.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERMISSION\_DENY | 17100203 | Permission denied due to missing ohos.permission.WEB\_NATIVE\_MESSAGING. |
| WANT\_CONTENT\_ERROR | 17100202 | The want content is invalid. |
| INNER\_ERROR | 17100201 | Inner error for native messaging. |

## WebExtensionConnectionCallback

PhonePC/2in1TabletTVWearable

### onConnect

PhonePC/2in1TabletTVWearable

onConnect(connection: ConnectionNativeInfo): void

建立连接时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-apis-web-webnativemessagingextensionmanager.md#connectionnativeinfo) | 是 | 连接信息。 |

**示例:**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
4. import { common } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onForeground() {
8. try {
9. let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
10. let want:Want = {
11. bundleName: 'com.example.app',
12. abilityName: 'MyWebNativeMessageExtAbility',
13. parameters: {
14. 'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
15. 'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
16. 'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' // 此处需要插件URI
17. },
18. };

20. let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
21. onConnect(connection) {
22. console.info('onConnect, connectionId:' + connection.connectionId);
23. },
24. onDisconnect(connection) {
25. console.info('onDisconnect');
26. },
27. onFailed(code, errMsg) {
28. console.info(`onFailed, code:${code} errMsg:${errMsg}`);
29. }
30. };

32. let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
33. } catch (err) {
34. // 处理入参错误异常
35. let code = (err as BusinessError).code;
36. let message = (err as BusinessError).message;
37. console.error(`connectNative failed, code is ${code}, message is ${message}`);
38. }
39. }
40. }
```

### onDisconnect

PhonePC/2in1TabletTVWearable

onDisconnect(connection: ConnectionNativeInfo): void

断开连接时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-apis-web-webnativemessagingextensionmanager.md#connectionnativeinfo) | 是 | 连接信息。 |

**示例:**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
4. import { common } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onForeground() {
8. try {
9. let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
10. let want:Want = {
11. bundleName: 'com.example.app',
12. abilityName: 'MyWebNativeMessageExtAbility',
13. parameters: {
14. 'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
15. 'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
16. 'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' // 此处需要插件URI
17. },
18. };

20. let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
21. onConnect(connection) {
22. console.info('onConnect, connectionId:' + connection.connectionId);
23. },
24. onDisconnect(connection) {
25. console.info('onDisconnect');
26. },
27. onFailed(code, errMsg) {
28. console.info(`onFailed, code:${code} errMsg:${errMsg}`);
29. }
30. };

32. let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
33. } catch (err) {
34. // 处理入参错误异常
35. let code = (err as BusinessError).code;
36. let message = (err as BusinessError).message;
37. console.error(`connectNative failed, code is ${code}, message is ${message}`);
38. }
39. }
40. }
```

### onFailed

PhonePC/2in1TabletTVWearable

onFailed(code: NmErrorCode, errMsg: string): void

连接失败时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | [NmErrorCode](arkts-apis-web-webnativemessagingextensionmanager.md#nmerrorcode) | 是 | 错误码。 |
| errMsg | string | 是 | 错误码对应信息。 |

**示例:**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
4. import { common } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onForeground() {
8. try {
9. let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
10. let want:Want = {
11. bundleName: 'com.example.app',
12. abilityName: 'MyWebNativeMessageExtAbility',
13. parameters: {
14. 'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
15. 'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
16. 'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' // 此处需要插件URI
17. },
18. };

20. let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
21. onConnect(connection) {
22. console.info('onConnect, connectionId:' + connection.connectionId);
23. },
24. onDisconnect(connection) {
25. console.info('onDisconnect');
26. },
27. onFailed(code, errMsg) {
28. console.info(`onFailed, code:${code} errMsg:${errMsg}`);
29. }
30. };

32. let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
33. } catch (err) {
34. // 处理入参错误异常
35. let code = (err as BusinessError).code;
36. let message = (err as BusinessError).message;
37. console.error(`connectNative failed, code is ${code}, message is ${message}`);
38. }
39. }
40. }
```

## webNativeMessagingExtensionManager.connectNative

PhonePC/2in1TabletTVWearable

connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): number

将当前Ability连接到指定的Web原生消息扩展Ability。

**需要权限**：ohos.permission.WEB\_NATIVE\_MESSAGING

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | Web原生消息扩展的上下文。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability的want信息。 |
| callback | [WebExtensionConnectionCallback](arkts-apis-web-webnativemessagingextensionmanager.md#webextensionconnectioncallback) | 是 | WebExtensionConnection状态的回调对象。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| number | 连接标识ID。 |

**错误码:**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例:**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
4. import { common } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. onForeground() {
8. try {
9. let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
10. let want:Want = {
11. bundleName: 'com.example.app',
12. abilityName: 'MyWebNativeMessageExtAbility',
13. parameters: {
14. 'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
15. 'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
16. 'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' // 此处需要插件URI
17. },
18. };

20. let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
21. onConnect(connection) {
22. console.info('onConnect, connectionId:' + connection.connectionId);
23. },
24. onDisconnect(connection) {
25. console.info('onDisconnect');
26. },
27. onFailed(code, errMsg) {
28. console.info(`onFailed, code:${code} errMsg:${errMsg}`);
29. }
30. };

32. let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
33. } catch (err) {
34. // 处理入参错误异常
35. let code = (err as BusinessError).code;
36. let message = (err as BusinessError).message;
37. console.error(`connectNative failed, code is ${code}, message is ${message}`);
38. }
39. }
40. }
```

## webNativeMessagingExtensionManager.disconnectNative

PhonePC/2in1TabletTVWearable

disconnectNative(connectionId: number): Promise<void>

断开指定Web原生消息扩展连接。

**需要权限**：ohos.permission.WEB\_NATIVE\_MESSAGING

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connectionId | number | 是 | 连接的标识ID，用于标识一次Web原生消息扩展连接，由[connectNative](arkts-apis-web-webnativemessagingextensionmanager.md#webnativemessagingextensionmanagerconnectnative)方法返回。建立连接后需要通过disconnectNative释放。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码:**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |

**示例:**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';

5. export default class EntryAbility extends UIAbility {
6. async disconnect() {
7. try {
8. let connectionId = 1;
9. // 假设之前已连接并获得connectionId
10. await webNativeMessagingExtensionManager.disconnectNative(connectionId).then(() => {
11. console.info('disconnectNative success');
12. })
13. } catch (err) {
14. // 处理入参错误异常
15. let code = (err as BusinessError).code;
16. let message = (err as BusinessError).message;
17. console.error(`disconnectNative failed, code is ${code}, message is ${message}`);
18. }
19. }
20. onForeground() {
21. this.disconnect();
22. }
23. }
```
