---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-service-extension-ability
title: 使用AppServiceExtensionAbility组件实现后台服务
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > ExtensionAbility组件 > 使用AppServiceExtensionAbility组件实现后台服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:925dc20df7377c444575baff9cc6f53f134dd7ef69c7447701c48d2d1f11129d
---

## 概述

从API version 20开始，支持开发者使用[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件，为应用提供后台服务能力，其他三方应用可通过启动或连接该AppServiceExtensionAbility组件获取相应的服务。

例如，企业部署的数据防泄漏 (DLP) 软件需要能够长期无界面运行，持续监听文件操作、网络流量，并拦截违规行为，可以使用AppServiceExtensionAbility组件来实现其核心的后台监控服务。

说明

本文将被启动或被连接的AppServiceExtensionAbility组件称为服务端，将启动或连接AppServiceExtensionAbility组件的应用组件（当前仅支持UIAbility）称为客户端。

## 约束与限制

### 设备限制

AppServiceExtensionAbility组件当前仅支持2in1设备。

### 规格限制

* 应用集成AppServiceExtensionAbility组件需要申请ACL权限（ohos.permission.SUPPORT\_APP\_SERVICE\_EXTENSION）。该ACL权限当前只对企业普通应用开放申请。
* AppServiceExtensionAbility组件内不支持调用[window](../harmonyos-references/arkts-apis-window.md)相关API。

## 运作机制

开发者可以在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)中以[启动](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)或[连接](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)的方式来拉起AppServiceExtensionAbility组件。

* **启动：** 客户端必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用才能调用[startAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)接口。
* **连接：** 如果[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)实例未启动，客户端必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用才能调用[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)接口。如果实例已启动，则没有上述限制。

下表展示了拉起和连接的几种场景：

说明

“客户端是否可信”为是时，表示客户端属于服务端所属应用或已配置在appIdentifierAllowList中。为否时，表示客户端不属于服务端所属应用且未配置在appIdentifierAllowList中。

| 客户端操作 | 服务端状态 | 客户端是否可信 | 结果说明 |
| --- | --- | --- | --- |
| startAppServiceExtensionAbility | 未启动 | 是 | 成功，服务端通过start方式启动，服务端状态变为已启动。 |
| startAppServiceExtensionAbility | 未启动 | 否 | 失败，客户端不在允许列表中，无法调用启动服务。 |
| startAppServiceExtensionAbility | 已启动 | 是 | 成功，服务端已经启动，start操作直接返回成功。 |
| startAppServiceExtensionAbility | 已启动 | 否 | 失败，客户端不在允许列表中，无法调用启动服务。 |
| connectAppServiceExtensionAbility | 未启动 | 是 | 成功，服务端通过connect方式启动，并建立连接。 |
| connectAppServiceExtensionAbility | 未启动 | 否 | 失败，客户端不在允许列表中，无法启动服务端。 |
| connectAppServiceExtensionAbility | 已启动 | 是 | 成功，服务端已启动，直接建立连接。 |
| connectAppServiceExtensionAbility | 已启动 | 否 | 成功，服务端已启动，直接建立连接。 |

## 实现一个后台服务

在DevEco Studio工程中手动新建一个AppServiceExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为myappserviceextability。
2. 在myappserviceextability目录，右键选择“New > ArkTS File”，新建一个文件并命名为MyAppServiceExtAbility.ets。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/9MsWuAPYQdO6uSgY8vN2Tw/zh-cn_image_0000002583437539.png?HW-CC-KV=V1&HW-CC-Date=20260427T233742Z&HW-CC-Expire=86400&HW-CC-Sign=D89533E814F60385E664E2C0951529161ED2DB04BFB5345A705A9C4DD69F8823)

   其目录结构如下所示：

   ```
   1. ├── ets
   2. │ ├── myappserviceextability
   3. │ │   ├── MyAppServiceExtAbility.ets
   4. └
   ```
3. 在MyAppServiceExtAbility.ets文件中，增加导入[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)的依赖包，自定义类继承AppServiceExtensionAbility组件并实现生命周期回调。

   ```
   1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
   2. import { rpc } from '@kit.IPCKit';
   3. // ···
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. const TAG: string = '[MyAppServiceExtAbility]';
   7. const DOMAIN_NUMBER: number = 0xFF00;

   9. class StubTest extends rpc.RemoteObject {
   10. constructor(des: string) {
   11. super(des);
   12. }

   14. onRemoteMessageRequest(code: number,
   15. data: rpc.MessageSequence,
   16. reply: rpc.MessageSequence,
   17. options: rpc.MessageOption): boolean | Promise<boolean> {
   18. // 处理客户端发送的消息
   19. return true;
   20. }
   21. }

   23. export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
   24. onCreate(want: Want): void {
   25. let appServiceExtensionContext = this.context;
   26. hilog.info(DOMAIN_NUMBER, TAG, `onCreate, want: ${want.abilityName}`);
   27. // ···
   28. }

   30. onRequest(want: Want, startId: number): void {
   31. hilog.info(DOMAIN_NUMBER, TAG, `onRequest, want: ${want.abilityName}`);
   32. }

   34. onConnect(want: Want): rpc.RemoteObject {
   35. hilog.info(DOMAIN_NUMBER, TAG, `onConnect, want: ${want.abilityName}`);
   36. return new StubTest('test');
   37. }

   39. onDisconnect(want: Want): void {
   40. hilog.info(DOMAIN_NUMBER, TAG, `onDisconnect, want: ${want.abilityName}`);
   41. }

   43. onDestroy(): void {
   44. hilog.info(DOMAIN_NUMBER, TAG, 'onDestroy');
   45. }
   46. };
   ```

   [MyAppServiceExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/myappserviceextability/MyAppServiceExtAbility.ets#L16-L82)
4. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册AppServiceExtensionAbility组件，type标签需要设置为“appService”，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. // ···
   4. "extensionAbilities": [
   5. // ···
   6. {
   7. "name": "MyAppServiceExtAbility",
   8. "description": "appService",
   9. "type": "appService",
   10. "exported": true,
   11. "srcEntry": "./ets/myappserviceextability/MyAppServiceExtAbility.ets",
   12. "appIdentifierAllowList": [
   13. // 此处填写允许启动该后台服务的客户端应用的appIdentifier列表
   14. ],
   15. }
   16. ]
   17. }
   18. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/module.json5#L15-L111)

## 启动一个后台服务

应用通过[startAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)方法启动一个后台服务，服务的[onRequest()](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md#onrequest)回调就会被调用，并在该回调方法中接收到调用者传递过来的[Want](../harmonyos-references/js-apis-app-ability-want.md)对象。后台服务启动后，其生命周期独立于客户端，即使客户端已经销毁，该后台服务仍可继续运行。因此，后台服务需要在其工作完成时通过调用[AppServiceExtensionContext](../harmonyos-references/-apis-inner-application-appserviceextensioncontext.md)的[terminateSelf()](../harmonyos-references/-apis-inner-application-appserviceextensioncontext.md#terminateself)来自行停止，或者由另一个组件调用[stopAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#stopappserviceextensionability20)来将其停止。

说明

AppServiceExtensionAbility组件以start方式启动，并且没有连接的时候，AppServiceExtensionAbility组件进程可能被挂起（请参考[Background Tasks Kit简介](background-task-overview.md)）。

* 在应用中启动一个新的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. const TAG: string = '[StartAppServiceExt]';
  6. const DOMAIN_NUMBER: number = 0xFF00;

  8. @Entry
  9. @Component
  10. struct StartAppServiceExt {
  11. build() {
  12. Column() {
  13. // ···
  14. List({ initialIndex: 0 }) {
  15. ListItem() {
  16. Row() {
  17. // ···
  18. }
  19. // ···
  20. .onClick(() => {
  21. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
  22. let want: Want = {
  23. deviceId: '',
  24. bundleName: 'com.samples.appserviceextensionability',
  25. abilityName: 'MyAppServiceExtAbility'
  26. };
  27. context.startAppServiceExtensionAbility(want).then(() => {
  28. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting AppServiceExtensionAbility.');
  29. // 成功启动后台服务
  30. this.getUIContext().getPromptAction().showToast({
  31. message: 'SuccessfullyStartBackendService'
  32. });
  33. }).catch((err: BusinessError) => {
  34. hilog.error(DOMAIN_NUMBER, TAG,
  35. `Failed to start AppServiceExtensionAbility. Code is ${err.code}, message is ${err.message}`);
  36. });
  37. })
  38. }

  40. // ···
  41. }
  42. // ···
  43. }

  45. // ···
  46. }
  47. }
  ```

  [StartAppServiceExt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/pages/StartAppServiceExt.ets#L15-L82)
* 在应用中停止一个已启动的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. const TAG: string = '[StopAppServiceExt]';
  6. const DOMAIN_NUMBER: number = 0xFF00;

  8. @Entry
  9. @Component
  10. struct StopAppServiceExt {
  11. build() {
  12. Column() {
  13. // ···
  14. List({ initialIndex: 0 }) {
  15. ListItem() {
  16. Row() {
  17. // ···
  18. }
  19. // ···
  20. .onClick(() => {
  21. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
  22. let want: Want = {
  23. deviceId: '',
  24. bundleName: 'com.samples.appserviceextensionability',
  25. abilityName: 'MyAppServiceExtAbility'
  26. };
  27. context.stopAppServiceExtensionAbility(want).then(() => {
  28. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in stopping AppServiceExtensionAbility.');
  29. this.getUIContext().getPromptAction().showToast({
  30. message: 'SuccessfullyStoppedAStartedBackendService'
  31. });
  32. }).catch((err: BusinessError) => {
  33. hilog.error(DOMAIN_NUMBER, TAG,
  34. `Failed to stop AppServiceExtensionAbility. Code is ${err.code}, message is ${err.message}`);
  35. });
  36. })
  37. }

  39. // ···
  40. }

  42. // ···
  43. }

  45. // ···
  46. }
  47. }
  ```

  [StopAppServiceExt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/pages/StopAppServiceExt.ets#L15-L82)
* 已启动的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件停止自身。

  ```
  1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
  2. // ···
  3. import { BusinessError } from '@kit.BasicServicesKit';
  4. import { hilog } from '@kit.PerformanceAnalysisKit';

  6. const TAG: string = '[MyAppServiceExtAbility]';
  7. // ···

  9. export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
  10. onCreate(want: Want): void {
  11. // ···
  12. // 执行业务逻辑
  13. this.context.terminateSelf().then(() => {
  14. hilog.info(0x0000, TAG, '----------- terminateSelf succeed -----------');
  15. }).catch((error: BusinessError) => {
  16. hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
  17. });
  18. }

  20. // ···
  21. };
  ```

  [MyAppServiceExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/myappserviceextability/MyAppServiceExtAbility.ets#L17-L81)

## 连接一个后台服务

### 客户端连接服务端

客户端可以通过[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接服务端（在Want对象中指定连接的目标服务），服务端的[onConnect()](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md#onconnect)就会被调用，并在该回调方法中接收到客户端传递过来的[Want](../harmonyos-references/js-apis-app-ability-want.md)对象。

服务端的AppServiceExtensionAbility组件会在onConnect()中返回[IRemoteObject](../harmonyos-references/js-apis-rpc.md#iremoteobject)对象给客户端[ConnectOptions](../harmonyos-references/js-apis-inner-ability-connectoptions.md)的[onConnect()](../harmonyos-references/js-apis-inner-ability-connectoptions.md#onconnect)方法。开发者通过该IRemoteObject定义通信接口，实现客户端与服务端的RPC交互。多个客户端可以同时连接到同一个后台服务，客户端完成与服务端的交互后，客户端需要通过调用[disconnectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#disconnectappserviceextensionability20)来断开连接。如果所有连接到某个后台服务的客户端均已断开连接，则系统会销毁该服务。

* 使用[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)建立与后台服务的连接。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. import { rpc } from '@kit.IPCKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';

  5. const TAG: string = '[ConnectAppServiceExt]';
  6. const DOMAIN_NUMBER: number = 0xFF00;

  8. let connectionId: number;
  9. let want: Want = {
  10. deviceId: '',
  11. bundleName: 'com.samples.appserviceextensionability',
  12. abilityName: 'MyAppServiceExtAbility'
  13. };

  15. let options: common.ConnectOptions = {
  16. onConnect(elementName, remote: rpc.IRemoteObject): void {
  17. hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
  18. if (remote === null) {
  19. hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
  20. return;
  21. }
  22. // 通过remote进行通信
  23. },
  24. onDisconnect(elementName): void {
  25. hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
  26. },
  27. onFailed(code: number): void {
  28. hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback', JSON.stringify(code));
  29. }
  30. };

  32. @Entry
  33. @Component
  34. struct ConnectAppServiceExt {
  35. build() {
  36. Column() {
  37. // ···
  38. List({ initialIndex: 0 }) {
  39. ListItem() {
  40. Row() {
  41. // ···
  42. }
  43. // ···
  44. .onClick(() => {
  45. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
  46. // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
  47. connectionId = context.connectAppServiceExtensionAbility(want, options);
  48. // 成功连接后台服务
  49. this.getUIContext().getPromptAction().showToast({
  50. message: 'SuccessfullyConnectBackendService'
  51. });
  52. hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
  53. })
  54. }

  56. // ···
  57. }

  59. // ···
  60. }

  62. // ···
  63. }
  64. }
  ```

  [ConnectAppServiceExt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/pages/ConnectAppServiceExt.ets#L15-L99)
* 使用[disconnectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#disconnectappserviceextensionability20)断开与后台服务的连接。

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. const TAG: string = '[DisConnectAppServiceExt]';
  6. const DOMAIN_NUMBER: number = 0xFF00;

  8. let connectionId: number;

  10. @Entry
  11. @Component
  12. struct DisConnectAppServiceExt {
  13. build() {
  14. Column() {
  15. // ···
  16. List({ initialIndex: 0 }) {
  17. ListItem() {
  18. Row() {
  19. // ···
  20. }
  21. // ···
  22. .onClick(() => {
  23. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
  24. // connectionId为调用connectServiceExtensionAbility接口时的返回值，需开发者自行维护
  25. context.disconnectAppServiceExtensionAbility(connectionId).then(() => {
  26. hilog.info(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility success');
  27. // 成功断连后台服务
  28. this.getUIContext().getPromptAction().showToast({
  29. message: 'SuccessfullyDisconnectBackendService'
  30. });
  31. }).catch((error: BusinessError) => {
  32. hilog.error(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility failed');
  33. });
  34. })
  35. }

  37. // ···
  38. }

  40. // ···
  41. }

  43. // ···
  44. }
  45. }
  ```

  [DisConnectAppServiceExt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/pages/DisConnectAppServiceExt.ets#L15-L80)

### 客户端与服务端通信

客户端在[onConnect()](../harmonyos-references/js-apis-inner-ability-connectoptions.md#onconnect)中获取到[rpc.IRemoteObject](../harmonyos-references/js-apis-rpc.md#iremoteobject)对象后便可与服务端进行通信。

**客户端**：使用[sendMessageRequest](../harmonyos-references/js-apis-rpc.md#sendmessagerequest9)接口向服务端发送消息。

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. const TAG: string = '[ClientServerExt]';
7. const DOMAIN_NUMBER: number = 0xFF00;
8. const REQUEST_CODE = 1;
9. let connectionId: number;
10. let want: Want = {
11. deviceId: '',
12. bundleName: 'com.samples.appserviceextensionability',
13. abilityName: 'MyAppServiceExtAbility'
14. };
15. let options: common.ConnectOptions = {
16. onConnect(elementName, remote): void {
17. hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
18. if (remote === null) {
19. hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
20. return;
21. }
22. let option = new rpc.MessageOption();
23. let data = new rpc.MessageSequence();
24. let reply = new rpc.MessageSequence();

26. // 写入请求数据
27. data.writeInt(1);
28. data.writeInt(2);

30. remote.sendMessageRequest(REQUEST_CODE, data, reply, option).then((ret: rpc.RequestResult) => {
31. if (ret.errCode === 0) {
32. hilog.info(DOMAIN_NUMBER, TAG, `sendRequest got result`);
33. let sum = ret.reply.readInt();
34. hilog.info(DOMAIN_NUMBER, TAG, `sendRequest success, sum:${sum}`);
35. } else {
36. hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed`);
37. }
38. }).catch((error: BusinessError) => {
39. hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed, ${JSON.stringify(error)}`);
40. });
41. },
42. onDisconnect(elementName): void {
43. hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
44. },
45. onFailed(code): void {
46. hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback');
47. }
48. };

50. // 调用connectAppServiceExtensionAbility相关代码

52. @Entry
53. @Component
54. struct ClientServerExt {
55. build() {
56. Column() {
57. // ···
58. List({ initialIndex: 0 }) {
59. ListItem() {
60. Row() {
61. // ···
62. }
63. // ···
64. .onClick(() => {
65. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
66. connectionId = context.connectAppServiceExtensionAbility(want, options);
67. hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
68. })
69. }
70. }
71. // ···
72. }
73. }
74. }
```

[ClientServerExt.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/pages/ClientServerExt.ets#L15-L102)

**服务端**：使用[onRemoteMessageRequest](../harmonyos-references/js-apis-rpc.md#onremotemessagerequest9)接口接收客户端发送的消息。

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[MyAppServiceExtAbility]';
6. const DOMAIN_NUMBER: number = 0xFF00;

8. // 开发者需要在这个类型里对接口进行实现
9. class Stub extends rpc.RemoteObject {
10. onRemoteMessageRequest(code: number,
11. data: rpc.MessageSequence,
12. reply: rpc.MessageSequence,
13. options: rpc.MessageOption): boolean | Promise<boolean> {
14. hilog.info(DOMAIN_NUMBER, TAG, 'onRemoteMessageRequest');
15. let sum = data.readInt() + data.readInt();
16. reply.writeInt(sum);
17. return true;
18. }
19. }

21. // 服务端实现
22. export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
23. onCreate(want: Want): void {
24. hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onCreate');
25. }

27. onDestroy(): void {
28. hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDestroy');
29. }

31. onConnect(want: Want): rpc.RemoteObject {
32. hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onConnect');
33. return new Stub('test');
34. }

36. onDisconnect(): void {
37. hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDisconnect');
38. }
39. }
```

[MyAppServiceExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/myappserviceextabilitytwo/MyAppServiceExtAbility.ets#L15-L55)

### 服务端对客户端身份校验

部分开发者需要使用AppServiceExtensionAbility组件提供一些较为敏感的服务，可以通过如下方式对客户端身份进行校验。

**通过callerTokenId对客户端进行鉴权**

通过调用[getCallingTokenId()](../harmonyos-references/js-apis-rpc.md#getcallingtokenid8)接口获取客户端的tokenID，再调用[verifyAccessTokenSync()](../harmonyos-references/js-apis-abilityaccessctrl.md#verifyaccesstokensync9)接口判断客户端是否有某个具体权限，由于当前不支持自定义权限，因此只能校验当前[系统所定义的权限](app-permissions.md)。示例代码如下：

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { abilityAccessCtrl, bundleManager } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. const TAG: string = '[AppServiceExtImpl]';
8. const DOMAIN_NUMBER: number = 0xFF00;

10. // 开发者需要在这个类里进行实现

12. class Stub extends rpc.RemoteObject {
13. onRemoteMessageRequest(
14. code: number,
15. data: rpc.MessageSequence,
16. reply: rpc.MessageSequence,
17. options: rpc.MessageOption): boolean | Promise<boolean> {
18. // 开发者自行实现业务逻辑
19. hilog.info(DOMAIN_NUMBER, TAG, `onRemoteMessageRequest: ${data}`);
20. let callerUid = rpc.IPCSkeleton.getCallingUid();
21. bundleManager.getBundleNameByUid(callerUid).then((callerBundleName) => {
22. hilog.info(DOMAIN_NUMBER, TAG, 'getBundleNameByUid: ' + callerBundleName);
23. // 对客户端包名进行识别
24. if (callerBundleName !== 'com.samples.stagemodelabilitydevelop') { // 识别不通过
25. hilog.info(DOMAIN_NUMBER, TAG, 'The caller bundle is not in trustlist, reject');
26. return;
27. }
28. // 识别通过，执行正常业务逻辑
29. }).catch((err: BusinessError) => {
30. hilog.error(DOMAIN_NUMBER, TAG, 'getBundleNameByUid failed: ' + err.message);
31. });

33. let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
34. let accessManager = abilityAccessCtrl.createAtManager();
35. // 所校验的具体权限由开发者自行选择，此处ohos.permission.GET_BUNDLE_INFO_PRIVILEGED只作为示例
36. let grantStatus = accessManager.verifyAccessTokenSync(callerTokenId, 'ohos.permission.GET_BUNDLE_INFO_PRIVILEGED');
37. if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_DENIED) {
38. hilog.error(DOMAIN_NUMBER, TAG, 'PERMISSION_DENIED');
39. return false;
40. }
41. hilog.info(DOMAIN_NUMBER, TAG, 'verify access token success.');
42. return true;
43. }
44. }

46. export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
47. onConnect(want: Want): rpc.RemoteObject {
48. return new Stub('test');
49. }
50. // 其他生命周期
51. }
```

[MyAppServiceExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AppServiceExtensionAbility/entry/src/main/ets/myappserviceextabilityfour/MyAppServiceExtAbility.ets#L16-L68)
