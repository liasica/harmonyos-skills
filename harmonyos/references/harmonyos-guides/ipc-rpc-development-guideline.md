---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-rpc-development-guideline
title: IPC与RPC通信开发指导(ArkTS)
breadcrumb: 指南 > 应用框架 > IPC Kit（进程间通信服务） > IPC与RPC通信开发指导(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ed34b6cb9f292c758bcfce308bff5302d198e6fc8242d0310a1897d14a4ca3c
---

## 场景介绍

IPC/RPC的主要工作是跨进程建立对象通信的连接（客户端进程的Proxy和服务端进程的Stub建立一一对应关系），从而通过Proxy的接口可以和Stub进行IPC/RPC通信。

## 开发步骤

说明

* 在进行IPC&RPC跨进程通信前需要通过Ability Kit获取服务端的代理对象。
* 不支持三方应用实现跨进程通信，三方应用仅可通过[connectServiceExtensionAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)连接系统提供的ServiceExtensionAbility，通过返回的代理对[ServiceExtensionAbility](extensionability-overview.md)进行通信从而达到三方应用和系统服务通信的目的。
* 从API version 20开始，在2in1设备上，开发者可使用AppServiceExtensionAbility组件，为应用提供后台服务能力。三方应用可[connectAppServiceExtensionAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接AppServiceExtensionAbility，通过返回的代理对象和[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)进行通信从而达到三方和三方应用通信的目的。详细开发步骤参考[AppServiceExtensionAbility](app-service-extension-ability.md#连接一个后台服务)。
* 三方应用之间也可通过[动态订阅公共事件](common-event-subscription.md)进行进程间通信。
* 完整的IPC&RPC通信开发流程涉及系统ServiceExtensionAbility的实现，故本篇指南仅提供客户端示例代码。

### 客户端实现

1. 创建变量want，指定要连接的Ability所在应用的包名、组件名。
2. 创建变量connect，指定连接成功、连接失败和断开连接时的回调函数。
3. 连接服务，获取服务代理对象Proxy，并注册死亡监听。
4. 客户端发送消息给服务端。
5. 通信结束后，断开连接，移除服务代理对象Proxy的死亡监听。

说明

* 在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

在IPC（同设备的跨进程通信）场景中，客户端的示例如下：

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

连接服务，获取代理对象，发送信息给服务端，通信结束后断开连接。

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

69. // 发送消息
70. async function sendString(promptAction: PromptAction) : Promise <void> {
71. hilog.info(0x00000, 'testTag', 'begin to send String');
72. let option = new rpc.MessageOption();
73. let data = rpc.MessageSequence.create();
74. let reply = rpc.MessageSequence.create();
75. // 在data里写入参数，以传递字符串为例
76. data.writeString('hello world');
77. if (proxy != undefined) {
78. await proxy.sendMessageRequest(1, data, reply, option)
79. .then((result: rpc.RequestResult) => {
80. if (result.errCode != 0) {
81. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode is ' + result.errCode);
82. }
83. // 从result.reply里读取结果
84. let str = result.reply.readString();
85. hilog.info(0x0000, 'testTag', 'sendMessageRequest receive str is ' + str);
86. // ...
87. })
88. .catch((e: Error) => {
89. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error is ' + JSON.stringify(e));
90. // ...
91. })
92. .finally(() => {
93. data.reclaim();
94. reply.reclaim();
95. })
96. } else {
97. hilog.error(0x0000, 'testTag', 'proxy is invalid');
98. // ...
99. }
100. hilog.info(0x0000, 'testTag', 'sendString end');
101. }
```

在RPC（跨设备的跨进程通信）场景中，具体客户端的示例如下：

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

获取[允许多设备协同的权限](permissions-for-all-user.md#ohospermissiondistributed_datasync)，在组网的情况下获取到对端的设备ID（组网场景下对应设备的唯一网络标识符，可以使用distributedDeviceManager获取目标设备的NetworkId）后连接服务，获取代理对象并发送信息给服务端，当代理对象与服务端的通信结束后，进行断连。

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

113. // 发送消息
114. async function sendString(promptAction: PromptAction) : Promise <void> {
115. hilog.info(0x00000, 'testTag', 'begin to send string');
116. let option = new rpc.MessageOption();
117. let data = rpc.MessageSequence.create();
118. let reply = rpc.MessageSequence.create();
119. // 在data里写入参数，以传递字符串为例
120. data.writeString('hello world');

122. if (proxy != undefined) {
123. await proxy.sendMessageRequest(1, data, reply, option)
124. .then((result: rpc.RequestResult) => {
125. if (result.errCode != 0) {
126. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode is ' + result.errCode);
127. }
128. // 从result.reply里读取结果
129. let str = result.reply.readString();
130. hilog.info(0x0000, 'testTag', 'sendMessageRequest receive str is ' + str);
131. // 弹窗显示发送消息成功
132. // ...
133. })
134. .catch((e: Error) => {
135. hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error is ' + JSON.stringify(e));
136. // 弹窗显示发送消息失败
137. // ...
138. })
139. .finally(() => {
140. data.reclaim();
141. reply.reclaim();
142. })
143. } else {
144. hilog.error(0x0000, 'testTag', 'proxy is invalid');
145. // 弹窗显示发送消息失败
146. // ...
147. }
148. }
```

## 完整示例

说明

* 以下完整示例涉及到ServiceExtensionAbility，需要使用full-SDK。参考示例前，请先阅读对应示例的ReadMe进行相应的配置后，再进行编译。

针对IPC与RPC通信开发，端到端的完整示例，请参考：

* [IPC通信完整示例-使用Parcelable/ArrayBuffer通信](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/SystemFeature/IPC/ObjectTransfer)
* [IPC通信完整示例-传递字符串及死亡监听使用](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/IPC/IPC_sendMessage)
* [RPC通信完整示例-传递字符串及死亡监听使用](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/IPC/RPC_sendMessage)
