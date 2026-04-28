---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-particleability
title: @ohos.ability.particleAbility (ParticleAbility模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > FA模型能力的接口 > @ohos.ability.particleAbility (ParticleAbility模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1173b30fa3b8a0487324c6869862b7e321e1ea9ff6668e6008a9c47ec4400ffe
---

particleAbility模块提供了操作Data和Service类型的Ability的能力，包括启动、停止指定的particleAbility，获取dataAbilityHelper，连接、断连指定的ServiceAbility等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

## 使用限制

PhonePC/2in1TabletTVWearable

particleAbility模块用来对Data和Service类型的Ability进行操作。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { particleAbility } from '@kit.AbilityKit';
```

## particleAbility.startAbility

PhonePC/2in1TabletTVWearable

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<void>): void

启动指定的particleAbility。使用callback异步回调。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示启动的ability。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动指定的particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { particleAbility, wantConstant } from '@kit.AbilityKit';

3. particleAbility.startAbility(
4. {
5. want:
6. {
7. action: 'ohos.want.action.home',
8. entities: ['entity.system.home'],
9. type: 'MIMETYPE',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.Data',
13. abilityName: 'com.example.Data.EntryAbility',
14. uri: ''
15. },
16. },
17. (error, data) => {
18. if (error && error.code !== 0) {
19. console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
20. } else {
21. console.info(`startAbility success, data: ${JSON.stringify(data)}`);
22. }
23. },
24. );
```

## particleAbility.startAbility

PhonePC/2in1TabletTVWearable

startAbility(parameter: StartAbilityParameter): Promise<void>

启动指定的particleAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](js-apis-inner-ability-startabilityparameter.md) | 是 | 表示启动的ability。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { particleAbility, wantConstant } from '@kit.AbilityKit';

3. particleAbility.startAbility(
4. {
5. want:
6. {
7. action: 'ohos.want.action.home',
8. entities: ['entity.system.home'],
9. type: 'MIMETYPE',
10. flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
11. deviceId: '',
12. bundleName: 'com.example.Data',
13. abilityName: 'com.example.Data.EntryAbility',
14. uri: ''
15. },
16. },
17. ).then(() => {
18. console.info('particleAbility startAbility');
19. });
```

## particleAbility.terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(callback: AsyncCallback<void>): void

销毁当前particleAbility。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当销毁当前particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { particleAbility } from '@kit.AbilityKit';

3. particleAbility.terminateSelf(
4. (error) => {
5. if (error && error.code !== 0) {
6. console.error(`terminateSelf fail, error: ${JSON.stringify(error)}`);
7. }
8. }
9. );
```

## particleAbility.terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁当前particleAbility。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { particleAbility } from '@kit.AbilityKit';

3. particleAbility.terminateSelf().then(() => {
4. console.info('particleAbility terminateSelf');
5. });
```

## particleAbility.acquireDataAbilityHelper

PhonePC/2in1TabletTVWearable

acquireDataAbilityHelper(uri: string): DataAbilityHelper

获取dataAbilityHelper对象。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

跨应用访问dataAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要打开的文件的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityHelper](js-apis-inner-ability-dataabilityhelper.md) | 用来协助其他Ability访问DataAbility的工具类。 |

**示例：**

```
1. import { particleAbility } from '@kit.AbilityKit';

3. let uri = '';
4. particleAbility.acquireDataAbilityHelper(uri);
```

## particleAbility.startBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void

向系统申请长时任务。使用callback异步回调。

**需要权限**：ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 长时任务通知id号。 |
| request | [NotificationRequest](js-apis-notification.md#notificationrequest) | 是 | 通知参数，用于显示通知栏的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { particleAbility, wantAgent } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import notification from '@ohos.notification';

5. function callback(error: BusinessError, data: void) {
6. if (error && error.code !== 0) {
7. console.error(`Operation failed error: ${JSON.stringify(error)}`);
8. } else {
9. console.info(`Operation succeeded, data: ${data}`);
10. }
11. }

13. let wantAgentInfo: wantAgent.WantAgentInfo = {
14. wants: [
15. {
16. bundleName: 'com.example.myapplication',
17. abilityName: 'EntryAbility'
18. }
19. ],
20. operationType: wantAgent.OperationType.START_ABILITY,
21. requestCode: 0,
22. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
23. };

25. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
26. let id = 1;
27. particleAbility.startBackgroundRunning(id, {
28. content:
29. {
30. contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
31. normal:
32. {
33. title: 'title',
34. text: 'text'
35. }
36. },
37. wantAgent: wantAgentObj
38. }, callback);
39. });
```

## particleAbility.startBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>

向系统申请长时任务。使用Promise异步回调。

**需要权限**：ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning-1)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 长时任务通知id号。 |
| request | [NotificationRequest](js-apis-notification.md#notificationrequest) | 是 | 通知参数，用于显示通知栏的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { particleAbility, wantAgent } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import notification from '@ohos.notification';

5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. }
11. ],
12. operationType: wantAgent.OperationType.START_ABILITY,
13. requestCode: 0,
14. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
15. };

17. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
18. let id = 1;
19. particleAbility.startBackgroundRunning(id, {
20. content:
21. {
22. contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
23. normal:
24. {
25. title: 'title',
26. text: 'text'
27. }
28. },
29. wantAgent: wantAgentObj
30. }).then(() => {
31. console.info('Operation succeeded');
32. }).catch((err: BusinessError) => {
33. console.error(`Operation failed cause: ${JSON.stringify(err)}`);
34. });
35. });
```

## particleAbility.cancelBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

cancelBackgroundRunning(callback: AsyncCallback<void>): void

向系统申请取消长时任务。使用callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请取消长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { particleAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback(error: BusinessError, data: void) {
5. if (error && error.code !== 0) {
6. console.error(`Operation failed error: ${JSON.stringify(error)}`);
7. } else {
8. console.info(`Operation succeeded, data: ${data}`);
9. }
10. }

12. particleAbility.cancelBackgroundRunning(callback);
```

## particleAbility.cancelBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

cancelBackgroundRunning(): Promise<void>

向系统申请取消长时任务。使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning-1)替代。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { particleAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. particleAbility.cancelBackgroundRunning().then(() => {
5. console.info('Operation succeeded');
6. }).catch((err: BusinessError) => {
7. console.error(`Operation failed cause: ${JSON.stringify(err)}`);
8. });
```

## particleAbility.connectAbility

PhonePC/2in1TabletTVWearable

connectAbility(request: Want, options:ConnectOptions): number

将当前ability与指定的ServiceAbility进行连接。

说明

组件启动规则详见：[组件启动规则（FA模型）](../harmonyos-guides/component-startup-rules-fa.md)。

跨应用连接serviceAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Want](js-apis-application-want.md) | 是 | 表示被连接的ServiceAbility。 |
| options | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | 连接回调方法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 连接的ServiceAbility的ID(ID从0开始自增，每连接成功一次ID加1)。 |

**示例**：

```
1. import { particleAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let connId = particleAbility.connectAbility(
6. {
7. bundleName: 'com.ix.ServiceAbility',
8. abilityName: 'ServiceAbilityA',
9. },
10. {
11. onConnect: (element, remote) => {
12. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
13. },
14. onDisconnect: (element) => {
15. console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
16. },
17. onFailed: (code) => {
18. console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
19. },
20. },
21. );

23. particleAbility.disconnectAbility(connId).then((data) => {
24. console.info(`data: ${data}`);
25. }).catch((error: BusinessError) => {
26. console.error(`particleAbilityTest result errCode: ${error.code}`);
27. });
```

## particleAbility.disconnectAbility

PhonePC/2in1TabletTVWearable

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

断开当前ability与指定ServiceAbility的连接。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开当前ability与指定ServiceAbility的连接成功，err为undefined，否则为错误对象。 |

**示例**：

```
1. import { particleAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';

4. let connId = particleAbility.connectAbility(
5. {
6. bundleName: 'com.ix.ServiceAbility',
7. abilityName: 'ServiceAbilityA',
8. },
9. {
10. onConnect: (element, remote) => {
11. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
12. },
13. onDisconnect: (element) => {
14. console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
15. },
16. onFailed: (code) => {
17. console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
18. },
19. },
20. );

22. particleAbility.disconnectAbility(connId, (err) => {
23. console.error(`particleAbilityTest disconnectAbility err: ${JSON.stringify(err)}`);
24. });
```

## particleAbility.disconnectAbility

PhonePC/2in1TabletTVWearable

disconnectAbility(connection: number): Promise<void>

断开当前ability与指定ServiceAbility的连接。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```
1. import { particleAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let connId = particleAbility.connectAbility(
6. {
7. bundleName: 'com.ix.ServiceAbility',
8. abilityName: 'ServiceAbilityA',
9. },
10. {
11. onConnect: (element, remote) => {
12. console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
13. },
14. onDisconnect: (element) => {
15. console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
16. },
17. onFailed: (code) => {
18. console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
19. },
20. },
21. );

23. particleAbility.disconnectAbility(connId).then(() => {
24. console.info('disconnectAbility success');
25. }).catch((error: BusinessError) => {
26. console.error(`particleAbilityTest result errCode : ${error.code}`);
27. });
```

## ErrorCode

PhonePC/2in1TabletTVWearable

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID\_PARAMETER | -1 | 无效的参数。 |
