---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-remote-state
title: 远端状态订阅开发实例
breadcrumb: 指南 > 应用框架 > IPC Kit（进程间通信服务） > 远端状态订阅开发实例
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:332b83c31c87d374a04f9f145bc20d2fa6789d85736fa4c999d2a0849215e089
---

IPC/RPC提供了订阅远端Stub对象状态的机制。当远端Stub对象死亡时，可以自动触发本端Proxy注册的死亡通知。这种死亡通知订阅需要调用指定接口[registerDeathRecipient](../harmonyos-references/js-apis-rpc.md#registerdeathrecipient9-1)完成。不再需要订阅时，也需要调用指定接口[unregisterDeathRecipient](../harmonyos-references/js-apis-rpc.md#unregisterdeathrecipient9-1)取消订阅。

使用这种订阅机制的用户需要继承死亡通知类[DeathRecipient](../harmonyos-references/js-apis-rpc.md#deathrecipient)，并实现[onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied)方法清理资源。该方法会在远端Stub对象所在进程退出或当前RPC通信依赖的软总线连接断开时被回调。

注意

* 首先，Proxy订阅Stub死亡通知，若在订阅期间Stub状态正常，则在不再需要时取消订阅。
* 其次，若在订阅期间，Stub所在进程退出或当前RPC通信依赖的软总线连接断开，则会自动触发执行业务已向Proxy注册的自定义的[onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied)方法。

## 使用场景

IPC/RPC的订阅机制适用于以下场景：

1. IPC通信，Proxy对象需要感知远端Stub对象所在进程的状态。
2. RPC通信，Proxy对象需要感知远端Stub对象所在进程的状态，或者RPC通信依赖的软总线连接断开。

当Proxy感知到Stub端死亡后，应该清理本地Proxy对象以及相关资源。

注意

RPC不支持匿名Stub对象（没有向SAMgr注册）的死亡通知，IPC支持匿名Stub对象的死亡通知。

## ArkTS侧接口

说明

* 此文档中的示例代码描述的是系统应用跨进程通信。
* 使用场景约束：客户端是第三方/系统应用，服务端是系统应用/服务

| 接口名 | 返回值类型 | 功能描述 |
| --- | --- | --- |
| [registerDeathRecipient](../harmonyos-references/js-apis-rpc.md#registerdeathrecipient9-1) | void | 注册用于接收远程对象死亡通知的回调，该方法应该在proxy侧调用。 |
| [unregisterDeathRecipient](../harmonyos-references/js-apis-rpc.md#unregisterdeathrecipient9-1) | void | 注销用于接收远程对象死亡通知的回调。 |
| [onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied) | void | Proxy侧注册死亡通知成功后，当远端Stub对象所在进程死亡时，将自动回调本方法。 |

### 参考代码

在IPC（同设备的跨进程通信）场景中，示例代码如下：

导入相关依赖，并定义所需的变量；

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { Want, common } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { PromptAction  } from '@kit.ArkUI';
6. import { JSON } from '@kit.ArkTS';

8. let proxy: rpc.IRemoteObject | undefined;
9. let connectId: number | undefined;

11. // 死亡通知
12. class MyDeathRecipient implements rpc.DeathRecipient {
13. onRemoteDied() {
14. hilog.info(0x0000, 'testTag', 'server is dead');
15. }
16. }
17. let deathRecipient = new MyDeathRecipient();
```

连接服务，获取代理对象，然后注册死亡监听。在断开连接时，移除死亡监听。

```
1. // 连接服务
2. function connectAbility(context:common.UIAbilityContext, promptAction: PromptAction) {
3. hilog.info(0x00000, 'testTag', 'begin to connect Ability');
4. let want: Want = {
5. bundleName: 'com.example.ipc_stub',
6. abilityName: 'ServiceAbility',
7. };
8. let connect: common.ConnectOptions = {
9. onConnect: (elementName, remoteProxy) => {
10. hilog.info(0x00000, 'testTag', 'onConnect. elementName is :' + JSON.stringify(elementName));
11. proxy = remoteProxy;
12. // 客户端注册死亡监听
13. try {
14. proxy.registerDeathRecipient(deathRecipient, 0);
15. hilog.info(0x00000, 'testTag', 'registerDeathRecipient success');
16. } catch (err) {
17. let code = (err as BusinessError).code;
18. let message = (err as BusinessError).message;
19. hilog.error(0x0000, 'testTag', 'register failed, code is ' + code + ', message is ' + message);
20. }
21. // ...
22. },

24. onDisconnect: (elementName) => {
25. hilog.info(0x0000, 'testTag', 'onDisconnect. elementName is ' + JSON.stringify(elementName));
26. // 客户端移除死亡监听
27. try {
28. proxy?.unregisterDeathRecipient(deathRecipient, 0);
29. hilog.info(0x00000, 'testTag', 'unregisterDeathRecipient success');
30. } catch (err) {
31. let code = (err as BusinessError).code;
32. let message = (err as BusinessError).message;
33. hilog.error(0x0000, 'testTag', 'unregister failed, code is ' + code + ', message is ' + message);
34. }
35. proxy = undefined;
36. // ...
37. },

39. onFailed: (code: number) => {
40. hilog.info(0x0000, 'testTag', 'onFailed. code is ' + code);
41. // ...
42. },
43. }

45. try {
46. connectId = context.connectServiceExtensionAbility(want, connect);
47. hilog.info(0x00000, 'testTag', 'begin to connect Ability end');
48. } catch (err) {
49. let code = (err as BusinessError).code;
50. let message = (err as BusinessError).message;
51. hilog.error(0x0000, 'testTag', 'connectAbility failed, code is ' + code + ', message is ' + message);
52. }
53. }

55. // 断开连接
56. function disconnectAbility(context: common.UIAbilityContext) {
57. hilog.info(0x00000, 'testTag', 'begin to disconnect Ability. connectId is ' + connectId);
58. if (connectId != undefined) {
59. try {
60. context.disconnectServiceExtensionAbility(connectId);
61. } catch (err) {
62. let code = (err as BusinessError).code;
63. let message = (err as BusinessError).message;
64. hilog.error(0x0000, 'testTag', 'disconnect failed, code is ' + code + ', message is ' + message);
65. }
66. }
67. }
```

在RPC（跨设备的跨进程通信）场景中，示例代码如下：

导入相关依赖，并定义所需的变量；

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
5. import { abilityAccessCtrl, PermissionRequestResult, common, Want} from '@kit.AbilityKit';
6. import { JSON } from '@kit.ArkTS';
7. import { PromptAction  } from '@kit.ArkUI';

9. let proxy: rpc.IRemoteObject | undefined;
10. let connectId: number | undefined;
11. let dmInstance: distributedDeviceManager.DeviceManager;
12. let deviceList: Array<distributedDeviceManager.DeviceBasicInfo> | undefined;
13. let deviceId: string| undefined;

15. // 死亡通知
16. class MyDeathRecipient implements rpc.DeathRecipient {
17. onRemoteDied() {
18. hilog.info(0x0000, 'testTag', 'server is dead');
19. }
20. };
21. let deathRecipient = new MyDeathRecipient();
```

获取[允许多设备协同的权限](permissions-for-all-user.md#ohospermissiondistributed_datasync)，在组网的情况下获取到对端的设备ID（组网场景下对应设备的唯一网络标识符，可以使用distributedDeviceManager获取目标设备的NetworkId）后连接服务，获取代理对象并注册死亡监听。当代理对象与服务端的通信结束后，在断开连接时，移除死亡监听。

```
1. // 获取权限
2. function getPermission(context:common.UIAbilityContext) {
3. hilog.info(0x00000, 'testTag', 'begin to requestPermissions');
4. try {
5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
6. atManager.requestPermissionsFromUser(context, ['ohos.permission.DISTRIBUTED_DATASYNC'],
7. (err: BusinessError, data: PermissionRequestResult) => {
8. if (err) {
9. hilog.error(0x0000, 'testTag', 'requestPermissions failed, code is ' + err.code);
10. hilog.error(0x0000, 'testTag', 'requestPermissions failed, message is ' + err.message);
11. } else {
12. hilog.info(0x0000, 'testTag', 'requestPermissions success, result is ' + JSON.stringify(data));
13. hilog.info(0x0000, 'testTag', 'data permissions is ' + data.permissions);
14. hilog.info(0x0000, 'testTag', 'data authResults is ' + data.authResults);
15. hilog.info(0x0000, 'testTag', 'data dialogShownResults is ' + data.dialogShownResults);
16. }
17. });
18. } catch (err) {
19. let code = (err as BusinessError).code;
20. let message = (err as BusinessError).message;
21. hilog.error(0x0000, 'testTag', 'getPermission failed, code is ' + code + ', message is ' + message);
22. }
23. }

25. // 获取对端设备信息
26. function getDeviceId(promptAction: PromptAction) {
27. hilog.info(0x00000, 'testTag', 'begin to getDeviceId');
28. try {
29. dmInstance = distributedDeviceManager.createDeviceManager('com.example.rpc_client');
30. hilog.info(0x0000, 'testTag', 'createDeviceManager success');
31. deviceList = dmInstance.getAvailableDeviceListSync();
32. hilog.info(0x0000, 'testTag', 'deviceList is ' + JSON.stringify(deviceList));
33. if (deviceList.length !== 0) {
34. deviceId = deviceList[0].networkId;
35. hilog.info(0x0000, 'testTag', 'networkId is ' + deviceId);
36. // ...
37. }
38. } catch (err) {
39. let code = (err as BusinessError).code;
40. let message = (err as BusinessError).message;
41. hilog.error(0x0000, 'testTag', 'getDeviceId failed, code is ' + code + ', message is ' + message);
42. // ...
43. }
44. }

46. // 连接服务
47. function connectAbility(context:common.UIAbilityContext, promptAction: PromptAction) {
48. hilog.info(0x00000, 'testTag', 'begin to connect Ability');
49. let want: Want = {
50. bundleName: 'com.example.rpc_stub',
51. abilityName: 'ServiceAbility',
52. deviceId: deviceId,
53. }

55. let connect: common.ConnectOptions = {
56. onConnect: (elementName, remoteProxy) => {
57. hilog.info(0x00000, 'testTag', 'onConnect. elementName is ' + JSON.stringify(elementName));
58. proxy = remoteProxy;
59. // 客户端注册死亡监听
60. try {
61. proxy.registerDeathRecipient(deathRecipient, 0);
62. hilog.info(0x00000, 'testTag', 'registerDeathRecipient success');
63. } catch (err) {
64. let code = (err as BusinessError).code;
65. let message = (err as BusinessError).message;
66. hilog.error(0x0000, 'testTag', 'register failed, code is ' + code + ', message is ' + message);
67. };
68. // ...
69. },
70. onDisconnect: (elementName) => {
71. hilog.info(0x0000, 'testTag', 'onDisconnect. elementName is ' + JSON.stringify(elementName));
72. // 客户端移除死亡监听
73. try {
74. proxy?.unregisterDeathRecipient(deathRecipient, 0);
75. hilog.info(0x00000, 'testTag', 'unregisterDeathRecipient success');
76. } catch (err) {
77. let code = (err as BusinessError).code;
78. let message = (err as BusinessError).message;
79. hilog.error(0x0000, 'testTag', 'unregister failed, code is ' + code + ', message is ' + message);
80. }
81. proxy = undefined;
82. // ...
83. },
84. onFailed: (code: number) => {
85. hilog.info(0x0000, 'testTag', 'onFailed. code is ' + code);
86. // ...
87. },
88. }

90. try {
91. connectId = context.connectServiceExtensionAbility(want, connect);
92. } catch (err) {
93. let code = (err as BusinessError).code;
94. let message = (err as BusinessError).message;
95. hilog.error(0x0000, 'testTag', 'connectService failed, code is ' + code + ', message is ' + message);
96. }
97. }

99. // 断开连接
100. function disconnectAbility(context: common.UIAbilityContext) {
101. hilog.info(0x00000, 'testTag', 'begin to disconnect Ability');
102. if (connectId != undefined) {
103. try {
104. context.disconnectServiceExtensionAbility(connectId);
105. } catch (err) {
106. let code = (err as BusinessError).code;
107. let message = (err as BusinessError).message;
108. hilog.error(0x0000, 'testTag', 'disconnectService failed, code is ' + code + ', message is ' + message);
109. }
110. }
111. }
```

## Stub反向感知Proxy死亡状态（匿名Stub的特殊用法）

正向的死亡通知是Proxy感知Stub的状态，要实现反向的死亡通知（即Stub感知Proxy的状态），可以利用反向死亡通知。例如，进程A（原Stub所在进程）和进程B（原Proxy所在进程），进程B获取到进程A的原Proxy对象后，在B进程新建一个匿名Stub对象（未向SAMgr注册），称为回调Stub，通过[sendMessageRequest](../harmonyos-references/js-apis-rpc.md#sendmessagerequest9-2)接口将回调Stub传给进程A的原Stub，进程A就可以获取到进程B的回调Proxy。只要向回调Proxy注册了死亡通知，当进程B（回调Stub）死亡或者RPC通信依赖的软总线连接断开时，回调Proxy会感知并通知进程A（原Stub），从而实现反向死亡通知。

注意

* 反向死亡通知仅限设备内跨进程通信使用，不可用于跨设备。
* 当匿名Stub对象没有被任何一个Proxy引用时，对象会被自动释放。
