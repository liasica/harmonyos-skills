---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager
title: @ohos.distributedsched.abilityConnectionManager (应用多端协同管理)
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > ArkTS API > @ohos.distributedsched.abilityConnectionManager (应用多端协同管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8a9ef7cd5bc619f4b4521c463e3edd1b2b7eae1ec97424269365b1901cfc6fa
---

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后，系统应用和三方应用可以跨设备拉起同应用的一个[UIAbility](js-apis-app-ability-uiability.md)，拉起并连接成功后可实现跨设备数据传输（文本信息）。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## abilityConnectionManager.createAbilityConnectionSession

PhonePC/2in1TabletTVWearable

createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo , connectOptions: ConnectOptions): number

创建应用间的协同会话。

**需要权限**：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO、ohos.permission.SET\_NETWORK\_INFO和ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceName | string | 是 | 应用设置的服务名称（两端必须一致），最大长度为256字符。 |
| context | [Context](js-apis-inner-application-context.md) | 是 | 表示应用上下文。 |
| peerInfo | [PeerInfo](js-apis-distributed-abilityconnectionmanager.md#peerinfo) | 是 | 对端的协同信息。 |
| connectOptions | [ConnectOptions](js-apis-distributed-abilityconnectionmanager.md#connectoptions) | 是 | 应用设置的连接选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 成功创建的协同会话ID。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

1. 在设备A上，应用需要主动调用createAbilityConnectionSession()接口创建协同会话并返回sessionId。

   ```
   1. import { abilityConnectionManager, distributedDeviceManager } from '@kit.DistributedServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. let dmClass: distributedDeviceManager.DeviceManager;

   6. function initDmClass(): void {
   7. try {
   8. dmClass = distributedDeviceManager.createDeviceManager('com.example.remotephotodemo');
   9. } catch (err) {
   10. hilog.error(0x0000, 'testTag', 'createDeviceManager err: ' + JSON.stringify(err));
   11. }
   12. }

   14. function getRemoteDeviceId(): string | undefined {
   15. initDmClass();
   16. if (typeof dmClass === 'object' && dmClass !== null) {
   17. hilog.info(0x0000, 'testTag', 'getRemoteDeviceId begin');
   18. let list = dmClass.getAvailableDeviceListSync();
   19. if (typeof (list) === 'undefined' || typeof (list.length) === 'undefined') {
   20. hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is null');
   21. return;
   22. }
   23. if (list.length === 0) {
   24. hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is empty');
   25. return;
   26. }
   27. return list[0].networkId;
   28. } else {
   29. hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: dmClass is null');
   30. return;
   31. }
   32. }

   34. @Entry
   35. @Component
   36. struct Index {
   37. createSession(): void {
   38. // 定义peer信息
   39. const peerInfo: abilityConnectionManager.PeerInfo = {
   40. deviceId: getRemoteDeviceId()!,
   41. bundleName: 'com.example.remotephotodemo',
   42. moduleName: 'entry',
   43. abilityName: 'EntryAbility',
   44. serviceName: 'collabTest'
   45. };
   46. const myRecord: Record<string, string> = {
   47. "newKey1": "value1",
   48. };

   50. // 定义连接选项
   51. const connectOptions: abilityConnectionManager.ConnectOptions = {
   52. needSendData: true,
   53. startOptions: abilityConnectionManager.StartOptionParams.START_IN_FOREGROUND,
   54. parameters: myRecord
   55. };
   56. let context = this.getUIContext().getHostContext();
   57. try {
   58. let sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", context, peerInfo, connectOptions);
   59. hilog.info(0x0000, 'testTag', 'createSession sessionId is', sessionId);
   60. } catch (error) {
   61. hilog.error(0x0000, 'testTag', error);
   62. }
   63. }

   65. build() {
   66. }
   67. }
   ```
2. 在设备B上，对于createAbilityConnectionSession接口的调用，可在应用被拉起后触发协同生命周期函数onCollaborate时，在onCollaborate内进行。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. export default class EntryAbility extends UIAbility {
   6. onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
   7. hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
   8. let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
   9. this.onCollab(param);
   10. return 0;
   11. }

   13. onCollab(collabParam: Record<string, Object>) {
   14. const sessionId = this.createSessionFromWant(collabParam);
   15. if (sessionId == -1) {
   16. hilog.info(0x0000, 'testTag', 'Invalid session ID.');
   17. return;
   18. }
   19. }

   21. createSessionFromWant(collabParam: Record<string, Object>): number {
   22. let sessionId = -1;
   23. const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
   24. if (peerInfo == undefined) {
   25. return sessionId;
   26. }

   28. const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
   29. try {
   30. sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
   31. AppStorage.setOrCreate('sessionId', sessionId);
   32. hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
   33. } catch (error) {
   34. hilog.error(0x0000, 'testTag', error);
   35. }
   36. return sessionId;
   37. }
   38. }
   ```

## abilityConnectionManager.destroyAbilityConnectionSession

PhonePC/2in1TabletTVWearable

destroyAbilityConnectionSession(sessionId: number): void

销毁应用间的协同会话。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 待销毁的协同会话ID。 |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
5. let sessionId = 100;
6. abilityConnectionManager.destroyAbilityConnectionSession(sessionId);
```

## abilityConnectionManager.getPeerInfoById

PhonePC/2in1TabletTVWearable

getPeerInfoById(sessionId: number): PeerInfo | undefined

获取指定会话中对端应用信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 协同会话ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PeerInfo](js-apis-distributed-abilityconnectionmanager.md#peerinfo) | undefined | 若存在对应peerInfo，则返回接收端的协作应用信息。若sessionId未找到，则查询失败，返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. hilog.info(0x0000, 'testTag', 'getPeerInfoById called');
5. let sessionId = 100;
6. const peerInfo = abilityConnectionManager.getPeerInfoById(sessionId);
```

## abilityConnectionManager.connect

PhonePC/2in1TabletTVWearable

connect(sessionId: number): Promise<ConnectResult>

创建协同会话成功并获得会话ID后，设备A上可进行UIAbility的连接。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 已创建的协同会话ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ConnectResult> | 以Promise形式返回[连接结果](js-apis-distributed-abilityconnectionmanager.md#connectresult)。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

设备A上的应用在创建协同会话成功并获得会话ID后，调用connect()方法启动UIAbility连接，并拉起设备B应用。

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.connect(sessionId).then((ConnectResult) => {
6. if (!ConnectResult.isConnected) {
7. hilog.info(0x0000, 'testTag', 'connect failed');
8. return;
9. }
10. }).catch(() => {
11. hilog.error(0x0000, 'testTag', "connect failed");
12. })
```

## abilityConnectionManager.acceptConnect

PhonePC/2in1TabletTVWearable

acceptConnect(sessionId: number, token: string): Promise<void>

设备B上的应用，在创建协同会话成功并获得会话ID后，调用acceptConnect()方法接受连接。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 已创建的协同会话ID。 |
| token | string | 是 | 设备A应用传入的token值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

设备B上的应用，在createAbilityConnectionSession接口调用并获取sessionId成功后，可调用acceptConnect接口来选择接受连接。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
8. }

10. onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
11. hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
12. let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
13. this.onCollab(param);
14. return 0;
15. }

17. onCollab(collabParam: Record<string, Object>) {
18. const sessionId = this.createSessionFromWant(collabParam);
19. if (sessionId == -1) {
20. hilog.info(0x0000, 'testTag', 'Invalid session ID.');
21. return;
22. }
23. const collabToken = collabParam["ohos.dms.collabToken"] as string;
24. abilityConnectionManager.acceptConnect(sessionId, collabToken).then(() => {
25. hilog.info(0x0000, 'testTag', 'acceptConnect success');
26. }).catch(() => {
27. hilog.error(0x0000, 'testTag', 'failed');
28. })
29. }

31. createSessionFromWant(collabParam: Record<string, Object>): number {
32. let sessionId = -1;
33. const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
34. if (peerInfo == undefined) {
35. return sessionId;
36. }

38. const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
39. try {
40. sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
41. AppStorage.setOrCreate('sessionId', sessionId);
42. hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
43. } catch (error) {
44. hilog.error(0x0000, 'testTag', error);
45. }
46. return sessionId;
47. }
48. }
```

## abilityConnectionManager.disconnect

PhonePC/2in1TabletTVWearable

disconnect(sessionId: number): void

当协同业务执行完毕后，协同双端的任意一台设备，应断开UIAbility的连接，结束协同状态。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 协同会话ID |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. hilog.info(0x0000, 'testTag', 'disconnectRemoteAbility begin');
5. let sessionId = 100;
6. abilityConnectionManager.disconnect(sessionId);
```

## abilityConnectionManager.reject

PhonePC/2in1TabletTVWearable

reject(token: string, reason: string): void;

在跨端应用协同过程中，在拒绝对端的连接请求后，向对端发送拒绝原因。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | string | 是 | 用于协作服务管理的令牌。 |
| reason | string | 是 | 连接被拒绝的原因。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want} from '@kit.AbilityKit';
2. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
7. hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
8. let collabParam = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>;
9. const collabToken = collabParam["ohos.dms.collabToken"] as string;
10. const reason = "test";
11. hilog.info(0x0000, 'testTag', 'reject begin');
12. abilityConnectionManager.reject(collabToken, reason);
13. return AbilityConstant.CollaborateResult.REJECT;
14. }
15. }
```

## abilityConnectionManager.on('connect')

PhonePC/2in1TabletTVWearable

on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册connect事件的回调监听。使用callback异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，完成[abilityConnectionManager.connect()](js-apis-distributed-abilityconnectionmanager.md#abilityconnectionmanagerconnect)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.on("connect", sessionId,(callbackInfo) => {
6. hilog.info(0x0000, 'testTag', 'session connect, sessionId is', callbackInfo.sessionId);
7. });
```

## abilityConnectionManager.off('connect')

PhonePC/2in1TabletTVWearable

off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消connect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';

3. let sessionId = 100;
4. abilityConnectionManager.off("connect", sessionId);
```

## abilityConnectionManager.on('disconnect')

PhonePC/2in1TabletTVWearable

on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册disconnect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnect'，完成[abilityConnectionManager.disconnect()](js-apis-distributed-abilityconnectionmanager.md#abilityconnectionmanagerdisconnect)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.on("disconnect", sessionId,(callbackInfo) => {
6. hilog.info(0x0000, 'testTag', 'session disconnect, sessionId is', callbackInfo.sessionId);
7. });
```

## abilityConnectionManager.off('disconnect')

PhonePC/2in1TabletTVWearable

off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消disconnect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnect'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.off("disconnect", sessionId);
```

## abilityConnectionManager.on('receiveMessage')

PhonePC/2in1TabletTVWearable

on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveMessage事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveMessage'，完成[abilityConnectionManager.sendMessage()](js-apis-distributed-abilityconnectionmanager.md#abilityconnectionmanagersendmessage)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.on("receiveMessage", sessionId,(callbackInfo) => {
6. hilog.info(0x0000, 'testTag', 'receiveMessage, sessionId is', callbackInfo.sessionId);
7. });
```

## abilityConnectionManager.off('receiveMessage')

PhonePC/2in1TabletTVWearable

off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveMessage事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveMessage'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.off("receiveMessage", sessionId);
```

## abilityConnectionManager.on('receiveData')

PhonePC/2in1TabletTVWearable

on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveData事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveData'，完成[abilityConnectionManager.sendData()](js-apis-distributed-abilityconnectionmanager.md#abilityconnectionmanagersenddata)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.on("receiveData", sessionId,(callbackInfo) => {
6. hilog.info(0x0000, 'testTag', 'receiveData, sessionId is', callbackInfo.sessionId);
7. });
```

## abilityConnectionManager.off('receiveData')

PhonePC/2in1TabletTVWearable

off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveData事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveData'，完成。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](js-apis-distributed-abilityconnectionmanager.md#eventcallbackinfo)> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.off("receiveData", sessionId);
```

## abilityConnectionManager.sendMessage

PhonePC/2in1TabletTVWearable

sendMessage(sessionId: number, msg: string): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送文本信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 协同会话ID。 |
| msg | string | 是 | 文本信息内容（内容最大限制为1KB）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let sessionId = 100;
5. abilityConnectionManager.sendMessage(sessionId, "message send success").then(() => {
6. hilog.info(0x0000, 'testTag', "sendMessage success");
7. }).catch(() => {
8. hilog.error(0x0000, 'testTag', "connect failed");
9. })
```

## abilityConnectionManager.sendData

PhonePC/2in1TabletTVWearable

sendData(sessionId: number, data: ArrayBuffer): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送[ArrayBuffer](../harmonyos-guides/arraybuffer-object.md)字节流。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | number | 是 | 协同会话ID。 |
| data | [ArrayBuffer](../harmonyos-guides/arraybuffer-object.md) | 是 | 字节流信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { abilityConnectionManager } from '@kit.DistributedServiceKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { util } from '@kit.ArkTS';

5. let textEncoder = util.TextEncoder.create("utf-8");
6. const arrayBuffer  = textEncoder.encodeInto("data send success");

8. let sessionId = 100;
9. abilityConnectionManager.sendData(sessionId, arrayBuffer.buffer).then(() => {
10. hilog.info(0x0000, 'testTag', "sendMessage success");
11. }).catch(() => {
12. hilog.info(0x0000, 'testTag', "sendMessage failed");
13. })
```

## PeerInfo

PhonePC/2in1TabletTVWearable

应用协同信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端设备ID。 |
| bundleName | string | 否 | 否 | 对端应用的包名。 |
| moduleName | string | 否 | 否 | 对端应用的模块名。 |
| abilityName | string | 否 | 否 | 对端应用的组件名。 |
| serviceName | string | 否 | 是 | 应用设置的服务名称。 |

## ConnectOptions

PhonePC/2in1TabletTVWearable

应用连接时所需的连接选项。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| needSendData | boolean | 否 | 是 | true代表需要传输数据，false代表不需要传输数据。 |
| startOptions | [StartOptionParams](js-apis-distributed-abilityconnectionmanager.md#startoptionparams) | 否 | 是 | 配置应用启动选项。 |
| parameters | Record<string, string> | 否 | 是 | 配置连接所需的额外信息。 |

## ConnectResult

PhonePC/2in1TabletTVWearable

连接的结果。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isConnected | boolean | 否 | 否 | true表示连接成功，false表示连接失败。 |
| errorCode | [ConnectErrorCode](js-apis-distributed-abilityconnectionmanager.md#connecterrorcode) | 否 | 是 | 表示连接错误码。 |
| reason | string | 否 | 是 | 表示拒绝连接的原因。 |

## EventCallbackInfo

PhonePC/2in1TabletTVWearable

回调方法的接收信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | number | 否 | 否 | 表示当前事件对应的协同会话ID。 |
| reason | [DisconnectReason](js-apis-distributed-abilityconnectionmanager.md#disconnectreason) | 否 | 是 | 表示断连原因。 |
| msg | string | 否 | 是 | 表示接收的消息。 |
| data | ArrayBuffer | 否 | 是 | 表示接收的字节流。 |

## CollaborateEventInfo

PhonePC/2in1TabletTVWearable

协同事件信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventType | [CollaborateEventType](js-apis-distributed-abilityconnectionmanager.md#collaborateeventtype) | 否 | 否 | 表示协同事件的类型。 |
| eventMsg | string | 否 | 是 | 表示协同事件的消息内容。 |

## ConnectErrorCode

PhonePC/2in1TabletTVWearable

连接的错误码。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTED\_SESSION\_EXISTS | 0 | 表示应用之间存在已连接的会话。 |
| PEER\_APP\_REJECTED | 1 | 表示对端应用拒绝了协作请求。 |
| LOCAL\_WIFI\_NOT\_OPEN | 2 | 表示本端WiFi未开启。 |
| PEER\_WIFI\_NOT\_OPEN | 3 | 表示对端WiFi未开启。 |
| PEER\_ABILITY\_NO\_ONCOLLABORATE | 4 | 表示未实现onCollaborate方法。 |
| SYSTEM\_INTERNAL\_ERROR | 5 | 表示系统内部错误。 |

## StartOptionParams

PhonePC/2in1TabletTVWearable

启动选项参数的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START\_IN\_FOREGROUND | 0 | 表示将对端应用启动至前台。 |

## CollaborateEventType

PhonePC/2in1TabletTVWearable

协同事件类型的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEND\_FAILURE | 0 | 表示任务发送失败。 |
| COLOR\_SPACE\_CONVERSION\_FAILURE | 1 | 表示色彩空间转换失败。 |

## DisconnectReason

PhonePC/2in1TabletTVWearable

当前断连原因的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEER\_APP\_CLOSE\_COLLABORATION | 0 | 表示对端应用主动关闭了协作。 |
| PEER\_APP\_EXIT | 1 | 表示对端应用退出。 |
| NETWORK\_DISCONNECTED | 2 | 表示网络断开。 |

## CollaborationKeys

PhonePC/2in1TabletTVWearable

应用协作键值的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEER\_INFO | ohos.collaboration.key.peerInfo | 表示对端设备信息的键值。 |
| CONNECT\_OPTIONS | ohos.collaboration.key.connectOptions | 表示连接选项的键值。 |
| COLLABORATE\_TYPE | ohos.collaboration.key.abilityCollaborateType | 表示协作类型的键值。 |

## CollaborationValues

PhonePC/2in1TabletTVWearable

**模型约束**：此接口仅可在Stage模型下使用。

应用协作相关值的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ABILITY\_COLLABORATION\_TYPE\_DEFAULT | ohos.collaboration.value.abilityCollab | 表示默认的协作类型。 |
| ABILITY\_COLLABORATION\_TYPE\_CONNECT\_PROXY | ohos.collaboration.value.connectProxy | 表示连接代理的协作类型。 |
