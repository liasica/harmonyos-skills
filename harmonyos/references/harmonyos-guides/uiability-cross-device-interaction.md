---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-cross-device-interaction
title: 通过Call调用实现多端协同
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > 通过Call调用实现多端协同
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:42+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:90dd306255e303acdf433c62bbf89d6e7650ee9d8d8ba62466b5180e3c00f00f
---

Call调用是[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)能力的扩展，它为UIAbility提供一种能够被外部调用并与外部进行通信的能力。Call调用支持前台与后台两种启动方式，使UIAbility既能被拉起到前台展示UI，也可以在后台被创建并运行。通过建立跨进程通信（IPC）链路，它在调用方与被调用方间构建起数据通道。当在分布式场景下使用时，Call调用可以跨设备发起，使得一个设备上的应用能够将任务迁移至另一个设备上的UIAbility继续执行，从而完成跨端迁移。

Call调用的核心接口是[startAbilityByCall()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)方法，与[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口的不同之处在于：

* startAbilityByCall支持前台与后台两种启动方式，而startAbility()仅支持前台启动。
* 调用方可使用startAbilityByCall()所返回的[Caller](../harmonyos-references/js-apis-app-ability-uiability.md#caller)对象与被调用方进行通信，而startAbility()不具备通信能力。

## 基本概念

**表1** Call调用相关名词解释

| 名词 | 描述 |
| --- | --- |
| CallerAbility | 进行Call调用的UIAbility（调用方）。 |
| CalleeAbility | 被Call调用的UIAbility（被调用方）。 |
| Caller | 实际对象，由startAbilityByCall接口返回，CallerAbility可使用Caller与CalleeAbility进行通信。 |
| Callee | 实际对象，被CalleeAbility持有，可与Caller进行通信。 |

## 约束限制

* CalleeAbility的启动模式不支持指定实例模式。
* 当前仅分布式迁移场景对第三方应用开放Call调用权限，其余所有Call调用场景均限定为系统内部调用。

## 运行机制

Call调用示意图如下所示。

**图1** Call调用示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/3rwC0Yk7TVy2sq7TqMu0nw/zh-cn_image_0000002583437537.png?HW-CC-KV=V1&HW-CC-Date=20260427T233741Z&HW-CC-Expire=86400&HW-CC-Sign=BA09A4150046A873A88224DACCB8FF67EA9C4896776AE4CACF6AA40EE581734F)

* CallerAbility调用[startAbilityByCall()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口获取[Caller](../harmonyos-references/js-apis-app-ability-uiability.md#caller)，并使用Caller对象的[call](../harmonyos-references/js-apis-app-ability-uiability.md#call)方法向CalleeAbility发送数据。
* CalleeAbility持有一个[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)对象，通过Callee的[on](../harmonyos-references/js-apis-app-ability-uiability.md#on)方法注册回调函数，当接收到Caller发送的数据时将会调用对应的回调函数。

## 接口说明

Call功能主要接口如下表所示。具体的API详见[Caller](../harmonyos-references/js-apis-app-ability-uiability.md#caller)接口说明。

**表2** Call功能主要接口

| 接口名 | 描述 |
| --- | --- |
| startAbilityByCall(want: Want): Promise<Caller> | 启动指定UIAbility并获取其Caller通信接口，默认为后台启动，通过配置want可实现前台启动，详见[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口说明。AbilityContext与ServiceExtensionContext均支持该接口。 |
| on(method: string, callback: CalleeCallBack): void | 通用组件Callee注册method对应的callback方法。 |
| off(method: string): void | 通用组件Callee解注册method的callback方法。 |
| call(method: string, data: rpc.Parcelable): Promise<void> | 向通用组件Callee发送约定序列化数据。 |
| callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence> | 向通用组件Callee发送约定序列化数据，并将Callee返回的约定序列化数据带回。 |
| release(): void | 释放通用组件的Caller通信接口。 |
| on(type: "release", callback: OnReleaseCallback): void | 注册通用组件通信断开监听通知。 |

## 开发步骤

### 创建Callee被调用端

在[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)被调用端，需要实现指定方法的数据接收回调函数、数据的序列化及反序列化方法。在需要接收数据期间，通过[on](../harmonyos-references/js-apis-app-ability-uiability.md#on)接口注册监听，无需接收数据时通过[off](../harmonyos-references/js-apis-app-ability-uiability.md#off)接口解除监听。

1. 需要申请ohos.permission.DISTRIBUTED\_DATASYNC权限，配置方式请参见[声明权限](declare-permissions.md)。
2. 同时需要在应用首次启动时弹窗向用户申请授权，使用方式请参见[向用户申请授权](request-user-authorization.md)。
3. 配置[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的启动模式。

   例如将CalleeAbility配置为单实例模式singleton，配置方式请参见[UIAbility组件启动模式](uiability-launch-type.md)。
4. 定义约定的序列化数据。

   调用端及被调用端发送接收的数据格式需协商一致，如下示例约定数据由number和string组成。

   ```
   1. import { rpc } from '@kit.IPCKit';

   3. class MyParcelable {
   4. num: number = 0;
   5. str: string = '';

   7. constructor(num: number, string: string) {
   8. this.num = num;
   9. this.str = string;
   10. }

   12. mySequenceable(num: number, string: string): void {
   13. this.num = num;
   14. this.str = string;
   15. }

   17. marshalling(messageSequence: rpc.MessageSequence): boolean {
   18. messageSequence.writeInt(this.num);
   19. messageSequence.writeString(this.str);
   20. return true;
   21. }

   23. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
   24. this.num = messageSequence.readInt();
   25. this.str = messageSequence.readString();
   26. return true;
   27. }
   28. }
   ```
5. 实现[Callee.on](../harmonyos-references/js-apis-app-ability-uiability.md#on)监听及[Callee.off](../harmonyos-references/js-apis-app-ability-uiability.md#off)解除监听。

   被调用端[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)的监听函数注册时机，取决于应用开发者。注册监听之前的数据不会被处理，取消监听之后的数据不会被处理。如下示例在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)注册'MSG\_SEND\_METHOD'监听，在[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)取消监听，收到序列化数据后作相应处理并返回，应用开发者根据实际需要做相应处理。具体示例代码如下：

   ```
   1. import { AbilityConstant, UIAbility, Want, Caller } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { rpc } from '@kit.IPCKit';

   5. const TAG: string = '[CalleeAbility]';
   6. const MSG_SEND_METHOD: string = 'CallSendMsg';
   7. const DOMAIN_NUMBER: number = 0xFF00;

   9. class MyParcelable {
   10. num: number = 0;
   11. str: string = '';

   13. constructor(num: number, string: string) {
   14. this.num = num;
   15. this.str = string;
   16. }

   18. mySequenceable(num: number, string: string): void {
   19. this.num = num;
   20. this.str = string;
   21. }

   23. marshalling(messageSequence: rpc.MessageSequence): boolean {
   24. messageSequence.writeInt(this.num);
   25. messageSequence.writeString(this.str);
   26. return true;
   27. }

   29. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
   30. this.num = messageSequence.readInt();
   31. this.str = messageSequence.readString();
   32. return true;
   33. }
   34. }

   36. function sendMsgCallback(data: rpc.MessageSequence): rpc.Parcelable {
   37. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'CalleeSortFunc called');

   39. // 获取Caller发送的序列化数据
   40. let receivedData: MyParcelable = new MyParcelable(0, '');
   41. data.readParcelable(receivedData);
   42. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', `receiveData[${receivedData.num}, ${receivedData.str}]`);
   43. let num: number = receivedData.num;

   45. // 作相应处理
   46. // 返回序列化数据result给Caller
   47. return new MyParcelable(num + 1, `send ${receivedData.str} succeed`) as rpc.Parcelable;
   48. }

   50. export default class CalleeAbility extends UIAbility {
   51. caller: Caller | undefined;

   53. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   54. try {
   55. this.callee.on(MSG_SEND_METHOD, sendMsgCallback);
   56. } catch (error) {
   57. hilog.error(DOMAIN_NUMBER, TAG, '%{public}s', `Failed to register. Error is ${error}`);
   58. }
   59. }

   61. // ...
   62. releaseCall(): void {
   63. try {
   64. if (this.caller) {
   65. this.caller.release();
   66. this.caller = undefined;
   67. }
   68. hilog.info(DOMAIN_NUMBER, TAG, 'caller release succeed');
   69. } catch (error) {
   70. hilog.error(DOMAIN_NUMBER, TAG, `caller release failed with ${error}`);
   71. }
   72. }

   74. // ...
   75. onDestroy(): void {
   76. try {
   77. this.callee.off(MSG_SEND_METHOD);
   78. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Callee OnDestroy');
   79. this.releaseCall();
   80. } catch (error) {
   81. hilog.error(DOMAIN_NUMBER, TAG, '%{public}s', `Failed to register. Error is ${error}`);
   82. }
   83. }
   84. }
   ```

### 访问被调用端UIAbility

1. 导入[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)模块。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   ```
2. 获取Caller通信接口。

   Ability的context属性实现了[startAbilityByCall](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilitybycall)方法，用于获取指定通用组[Caller](../harmonyos-references/js-apis-app-ability-uiability.md#caller)通信接口。如下示例通过this.context获取Ability实例的context属性，使用startAbilityByCall拉起[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)被调用端并获取Caller通信接口，注册Caller的[onRelease](../harmonyos-references/js-apis-app-ability-uiability.md#onrelease)和[onRemoteStateChange](../harmonyos-references/js-apis-app-ability-uiability.md#onremotestatechange10)监听。应用开发者根据实际业务需要做相应处理。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { Caller, common } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   5. import { promptAction } from '@kit.ArkUI';

   7. const TAG: string = '[Page_CollaborateAbility]';
   8. const DOMAIN_NUMBER: number = 0xFF00;
   9. let caller: Caller | undefined;
   10. let dmClass: distributedDeviceManager.DeviceManager;

   12. function getRemoteDeviceId(): string | undefined {
   13. if (typeof dmClass === 'object' && dmClass !== null) {
   14. let list = dmClass.getAvailableDeviceListSync();
   15. hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(dmClass), JSON.stringify(list));
   16. if (typeof (list) === 'undefined' || typeof (list.length) === 'undefined') {
   17. hilog.error(DOMAIN_NUMBER, TAG, 'getRemoteDeviceId err: list is null');
   18. return;
   19. }
   20. if (list.length === 0) {
   21. hilog.error(DOMAIN_NUMBER, TAG, `getRemoteDeviceId err: list is empty`);
   22. return;
   23. }
   24. return list[0].networkId;
   25. } else {
   26. hilog.error(DOMAIN_NUMBER, TAG, 'getRemoteDeviceId err: dmClass is null');
   27. return;
   28. }
   29. }

   31. @Entry
   32. @Component
   33. struct Page_CollaborateAbility {
   34. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   35. build() {
   36. Row() {
   37. Column() {
   38. // ...
   39. List({ initialIndex: 0 }) {
   40. // ...
   41. ListItem() {
   42. Button('test').onClick(() => {
   43. let caller: Caller | undefined;
   44. let context = this.context;

   46. context.startAbilityByCall({
   47. deviceId: getRemoteDeviceId(),
   48. bundleName: 'com.samples.stagemodelabilityinteraction',
   49. abilityName: 'CalleeAbility'
   50. }).then((data) => {
   51. if (data !== null) {
   52. caller = data;
   53. hilog.info(DOMAIN_NUMBER, TAG, 'get remote caller success');
   54. // 注册caller的release监听
   55. caller.onRelease((msg) => {
   56. hilog.info(DOMAIN_NUMBER, TAG, `remote caller onRelease is called ${msg}`);
   57. });
   58. hilog.info(DOMAIN_NUMBER, TAG, 'remote caller register OnRelease succeed');
   59. promptAction.openToast({
   60. message: 'CallerSuccess'
   61. });
   62. // 注册caller的协同场景下跨设备组件状态变化监听通知
   63. try {
   64. caller.onRemoteStateChange((str) => {
   65. hilog.info(DOMAIN_NUMBER, TAG, 'Remote state changed ' + str);
   66. });
   67. } catch (error) {
   68. hilog.error(DOMAIN_NUMBER, TAG, `Caller.onRemoteStateChange catch error, error.code: ${JSON.stringify(error.code)}, error.message: ${JSON.stringify(error.message)}`);
   69. }
   70. }
   71. }).catch((error: BusinessError) => {
   72. hilog.error(DOMAIN_NUMBER, TAG, `get remote caller failed with ${error}`);
   73. });
   74. })
   75. }
   76. // ...
   77. }
   78. // ...
   79. }
   80. // ...
   81. }
   82. }
   83. }
   ```

### 向被调用端UIAbility发送约定序列化数据

1. 向被调用端发送Parcelable数据有两种方式，一种是不带返回值，一种是获取被调用端返回的数据，method以及序列化数据需要与被调用端协商一致。如下示例调用[Call](../harmonyos-references/js-apis-app-ability-uiability.md#call)接口，向[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)被调用端发送数据。

   ```
   1. import { UIAbility, Caller } from '@kit.AbilityKit';
   2. import { rpc } from '@kit.IPCKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[CalleeAbility]';
   6. const DOMAIN_NUMBER: number = 0xFF00;
   7. const MSG_SEND_METHOD: string = 'CallSendMsg';

   9. class MyParcelable {
   10. num: number = 0;
   11. str: string = '';

   13. constructor(num: number, string: string) {
   14. this.num = num;
   15. this.str = string;
   16. }

   18. mySequenceable(num: number, string: string): void {
   19. this.num = num;
   20. this.str = string;
   21. }

   23. marshalling(messageSequence: rpc.MessageSequence): boolean {
   24. messageSequence.writeInt(this.num);
   25. messageSequence.writeString(this.str);
   26. return true;
   27. }

   29. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
   30. this.num = messageSequence.readInt();
   31. this.str = messageSequence.readString();
   32. return true;
   33. }
   34. }

   36. export default class EntryAbility extends UIAbility {
   37. // ...
   38. caller: Caller | undefined;

   40. async onButtonCall(): Promise<void> {
   41. try {
   42. let msg: MyParcelable = new MyParcelable(1, 'origin_Msg');
   43. if (this.caller) {
   44. await this.caller.call(MSG_SEND_METHOD, msg);
   45. }
   46. } catch (error) {
   47. hilog.error(DOMAIN_NUMBER, TAG, `caller call failed with ${error}`);
   48. }
   49. }
   50. // ...
   51. }
   ```
2. 如下示例调用[callWithResult](../harmonyos-references/js-apis-app-ability-uiability.md#callwithresult)接口，向Callee被调用端发送待处理的数据originMsg，并将CallSendMsg方法处理完毕的数据赋值给backMsg。

   ```
   1. import { UIAbility, Caller } from '@kit.AbilityKit';
   2. import { rpc } from '@kit.IPCKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[CalleeAbility]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. const MSG_SEND_METHOD: string = 'CallSendMsg';
   9. let originMsg: string = '';
   10. let backMsg: string = '';

   12. class MyParcelable {
   13. num: number = 0;
   14. str: string = '';

   16. constructor(num: number, string: string) {
   17. this.num = num;
   18. this.str = string;
   19. }

   21. mySequenceable(num: number, string: string): void {
   22. this.num = num;
   23. this.str = string;
   24. }

   26. marshalling(messageSequence: rpc.MessageSequence): boolean {
   27. messageSequence.writeInt(this.num);
   28. messageSequence.writeString(this.str);
   29. return true;
   30. }

   32. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
   33. this.num = messageSequence.readInt();
   34. this.str = messageSequence.readString();
   35. return true;
   36. }
   37. }

   39. export default class EntryAbility extends UIAbility {
   40. // ...
   41. caller: Caller | undefined;

   43. async onButtonCallWithResult(originMsg: string, backMsg: string): Promise<void> {
   44. try {
   45. let msg: MyParcelable = new MyParcelable(1, originMsg);
   46. if (this.caller) {
   47. const data = await this.caller.callWithResult(MSG_SEND_METHOD, msg);
   48. hilog.info(DOMAIN_NUMBER, TAG, 'caller callWithResult succeed');
   49. let result: MyParcelable = new MyParcelable(0, '');
   50. data.readParcelable(result);
   51. backMsg = result.str;
   52. hilog.info(DOMAIN_NUMBER, TAG, `caller result is [${result.num}, ${result.str}]`);
   53. }
   54. } catch (error) {
   55. hilog.error(DOMAIN_NUMBER, TAG, `caller callWithResult failed with ${error}`);
   56. }
   57. }
   58. // ...
   59. }
   ```

### 释放Caller通信接口

[Caller](../harmonyos-references/js-apis-app-ability-uiability.md#caller)不再使用后，应用开发者可以通过[release](../harmonyos-references/js-apis-app-ability-uiability.md#release)接口释放Caller。

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[CalleeAbility]';
5. const DOMAIN_NUMBER: number = 0xFF00;

7. export default class EntryAbility extends UIAbility {
8. caller: Caller | undefined
9. releaseCall(): void {
10. try {
11. if (this.caller) {
12. this.caller.release();
13. this.caller = undefined;
14. }
15. hilog.info(DOMAIN_NUMBER, TAG, 'caller release succeed');
16. } catch (error) {
17. hilog.error(DOMAIN_NUMBER, TAG, `caller release failed with ${error}`);
18. }
19. }
20. }
```
