---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager
title: @ohos.resourceschedule.backgroundTaskManager (后台任务管理)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > @ohos.resourceschedule.backgroundTaskManager (后台任务管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e3beae5477f9f48701d6876bb1e2f02c7e244dd52643fe3d52f6961bbf3591b
---

本模块提供申请后台任务的接口。当应用退至后台时，开发者可以通过本模块接口为应用申请短时、长时任务，避免应用进程被终止或挂起。开发指导请参考[长时任务开发指南](../harmonyos-guides/continuous-task.md)、[短时任务开发指南](../harmonyos-guides/transient-task.md)。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## backgroundTaskManager.requestSuspendDelay

PhonePC/2in1TabletTVWearable

requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo

申请短时任务。

说明

短时任务的申请和使用过程中的约束与限制请参考[指南](../harmonyos-guides/transient-task.md#约束与限制)。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 申请短时任务的原因。 |
| callback | Callback<void> | 是 | 短时任务即将超时的回调函数，一般在超时前6秒，通过此回调通知应用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DelaySuspendInfo](js-apis-resourceschedule-backgroundtaskmanager.md#delaysuspendinfo) | 返回短时任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

4. let myReason = 'test requestSuspendDelay';
5. try {
6. let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
7. // 回调函数。应用申请的短时任务即将超时，通过此函数回调应用，执行一些清理和标注工作，并取消短时任务
8. // 此处回调与应用的业务功能不耦合，短时任务申请成功后，正常执行应用本身的业务
9. console.info("Request suspension delay will time out.");
10. })
11. let id = delayInfo.requestId;
12. let time = delayInfo.actualDelayTime;
13. console.info("The requestId is: " + id);
14. console.info("The actualDelayTime is: " + time);
15. } catch (error) {
16. console.error(`requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
17. }
```

## backgroundTaskManager.getRemainingDelayTime

PhonePC/2in1TabletTVWearable

getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void

获取本次短时任务的剩余时间，使用callback异步回调。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务[requestSuspendDelay](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelay)接口获取。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回本次短时任务的剩余时间，单位：ms。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

4. let id = 1;
5. backgroundTaskManager.getRemainingDelayTime(id, (error: BusinessError, res: number) => {
6. if(error) {
7. console.error(`callback => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
8. } else {
9. console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
10. }
11. })
```

## backgroundTaskManager.getRemainingDelayTime

PhonePC/2in1TabletTVWearable

getRemainingDelayTime(requestId: number): Promise<number>

获取本次短时任务的剩余时间，使用Promise异步回调。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务[requestSuspendDelay](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelay)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回本次短时任务的剩余时间，单位：ms。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

4. let id = 1;
5. backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
6. console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
7. }).catch((error: BusinessError) => {
8. console.error(`promise => Operation getRemainingDelayTime failed. code is ${error.code} message is ${error.message}`);
9. })
```

## backgroundTaskManager.cancelSuspendDelay

PhonePC/2in1TabletTVWearable

cancelSuspendDelay(requestId: number): void

取消短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 短时任务的请求ID。通过申请短时任务[requestSuspendDelay](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelay)接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9900001 | Caller information verification failed for a transient task. |
| 9900002 | Transient task verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

4. let id = 1;
5. try {
6. backgroundTaskManager.cancelSuspendDelay(id);
7. } catch (error) {
8. console.error(`cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
9. }
```

## backgroundTaskManager.getTransientTaskInfo20+

PhonePC/2in1TabletTVWearable

getTransientTaskInfo(): Promise<TransientTaskInfo>

获取所有短时任务信息，如当日剩余总配额等，使用Promise异步回调。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TransientTaskInfo](js-apis-resourceschedule-backgroundtaskmanager.md#transienttaskinfo20)> | Promise对象，返回所有短时任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9900001 | Caller information verification failed for a transient task. |
| 9900003 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9900004 | System service operation failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. backgroundTaskManager.getTransientTaskInfo().then((res: backgroundTaskManager.TransientTaskInfo) => {
6. console.info(`Operation getTransientTaskInfo succeeded. data: ` + JSON.stringify(res));
7. }).catch((error : BusinessError) => {
8. console.error(`Operation getTransientTaskInfo failed. code is ${error.code} message is ${error.message}`);
9. });
10. } catch (error) {
11. console.error(`Operation getTransientTaskInfo failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
12. }
```

## backgroundTaskManager.startBackgroundRunning

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void

申请长时任务，支持申请一种类型，使用callback异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| bgMode | [BackgroundMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode) | 是 | 长时任务类型。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |
| callback | AsyncCallback<void> | 是 | 回调函数，申请长时任务成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { wantAgent, WantAgent } from '@kit.AbilityKit';
5. // 在元服务中，请删除WantAgent导入

7. function callback(error: BusinessError, data: void) {
8. if (error) {
9. console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
10. } else {
11. console.info("Operation startBackgroundRunning succeeded");
12. }
13. }

15. export default class EntryAbility extends UIAbility {
16. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
17. let wantAgentInfo: wantAgent.WantAgentInfo = {
18. // 点击通知后，将要执行的动作列表
19. wants: [
20. {
21. bundleName: "com.example.myapplication",
22. abilityName: "EntryAbility"
23. }
24. ],
25. // 点击通知后，动作类型
26. actionType: wantAgent.OperationType.START_ABILITY,
27. // 使用者自定义的一个私有值
28. requestCode: 0,
29. // 点击通知后，动作执行属性
30. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
31. };

33. try {
34. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
35. // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
36. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
37. try {
38. backgroundTaskManager.startBackgroundRunning(this.context,
39. backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj, callback)
40. } catch (error) {
41. console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
42. }
43. });
44. } catch (error) {
45. console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
46. }
47. }
48. };
```

## backgroundTaskManager.startBackgroundRunning

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>

申请长时任务，支持申请一种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| bgMode | [BackgroundMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode) | 是 | 长时任务类型。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { wantAgent, WantAgent } from '@kit.AbilityKit';
5. // 在元服务中，请删除WantAgent导入

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
9. let wantAgentInfo: wantAgent.WantAgentInfo = {
10. // 点击通知后，将要执行的动作列表
11. wants: [
12. {
13. bundleName: "com.example.myapplication",
14. abilityName: "EntryAbility"
15. }
16. ],
17. // 点击通知后，动作类型
18. actionType: wantAgent.OperationType.START_ABILITY,
19. // 使用者自定义的一个私有值
20. requestCode: 0,
21. // 点击通知后，动作执行属性
22. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
23. };

25. try {
26. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
27. // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
28. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
29. try {
30. backgroundTaskManager.startBackgroundRunning(this.context,
31. backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
32. console.info("Operation startBackgroundRunning succeeded");
33. }).catch((error: BusinessError) => {
34. console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
35. });
36. } catch (error) {
37. console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
38. }
39. });
40. } catch (error) {
41. console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
42. }
43. }
44. };
```

## backgroundTaskManager.stopBackgroundRunning

PhonePC/2in1TabletTVWearable

stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void

取消当前UIAbility（FA模型则为ServiceAbility）下所有长时任务，使用callback异步回调。也可以通过[stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning21)接口取消指定Id的长时任务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| callback | AsyncCallback<void> | 是 | 回调函数，取消长时任务成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(error: BusinessError, data: void) {
6. if (error) {
7. console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
8. } else {
9. console.info("Operation stopBackgroundRunning succeeded");
10. }
11. }

13. export default class EntryAbility extends UIAbility {
14. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
15. try {
16. backgroundTaskManager.stopBackgroundRunning(this.context, callback);
17. } catch (error) {
18. console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
19. }
20. }
21. };
```

## backgroundTaskManager.stopBackgroundRunning

PhonePC/2in1TabletTVWearable

stopBackgroundRunning(context: Context): Promise<void>

取消当前UIAbility（FA模型则为ServiceAbility）下所有长时任务，使用Promise异步回调。也可以通过[stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning21)接口取消指定Id的长时任务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. try {
8. backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
9. console.info("Operation stopBackgroundRunning succeeded");
10. }).catch((error: BusinessError) => {
11. console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
12. });
13. } catch (error) {
14. console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
15. }
16. }
17. };
```

## backgroundTaskManager.startBackgroundRunning12+

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>

申请长时任务，支持申请多种类型，使用Promise异步回调。长时任务申请成功后，会有通知栏消息，没有提示音。一个UIAbility（FA模型则为ServiceAbility）同一时刻仅支持通过本接口支持申请一个长时任务，可以通过API version 21新增接口[startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)申请多个长时任务。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| bgModes | string[] | 是 | 长时任务类型，取值范围请参考长时任务类型中的[配置项](../harmonyos-guides/continuous-task.md#使用场景)。  **说明：** 支持传入一个或多个类型。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)> | Promise对象，返回[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)类型对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { notificationManager } from '@kit.NotificationKit';
5. import { wantAgent, WantAgent } from '@kit.AbilityKit';
6. // 在元服务中，请删除WantAgent导入

8. export default class EntryAbility extends UIAbility {
9. id: number = 0; // 保存通知id

11. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
12. let wantAgentInfo: wantAgent.WantAgentInfo = {
13. // 点击通知后，将要执行的动作列表
14. wants: [
15. {
16. bundleName: "com.example.myapplication",
17. abilityName: "EntryAbility"
18. }
19. ],
20. // 点击通知后，动作类型
21. actionType: wantAgent.OperationType.START_ABILITY,
22. // 使用者自定义的一个私有值
23. requestCode: 0,
24. // 点击通知后，动作执行属性
25. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
26. };

28. try {
29. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
30. // 在元服务中，请使用wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {替换下面一行代码
31. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
32. try {
33. let list: Array<string> = ["dataTransfer"];
34. // 在元服务中，let list: Array<string> = ["audioPlayback"];
35. backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
36. console.info("Operation startBackgroundRunning succeeded");
37. // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知
38. this.id = res.notificationId;
39. }).catch((error: BusinessError) => {
40. console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
41. });
42. } catch (error) {
43. console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
44. }
45. });
46. } catch (error) {
47. console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
48. }
49. }

51. // 应用更新进度
52. updateProcess(process: number) {
53. // 定义通知类型，更新进度时的通知类型必须为实况窗
54. let downLoadTemplate: notificationManager.NotificationTemplate = {
55. name: 'downloadTemplate', // 当前只支持downloadTemplate，保持不变
56. data: {
57. title: '文件下载：music.mp4', // 必填
58. fileName: 'senTemplate', // 必填
59. progressValue: process, // 应用更新进度值，自定义
60. }
61. };
62. let request: notificationManager.NotificationRequest = {
63. content: {
64. // 系统实况类型，保持不变
65. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW,
66. systemLiveView: {
67. typeCode: 8, // 上传下载类型需要填写 8，当前仅支持此类型。保持不变
68. title: "test", // 应用自定义
69. text: "test", // 应用自定义
70. }
71. },
72. id: this.id, // 必须是申请长时任务返回的id，否则应用更新通知失败
73. notificationSlotType: notificationManager.SlotType.LIVE_VIEW, // 实况窗类型，保持不变
74. template: downLoadTemplate // 应用需要设置的模版名称
75. };

77. try {
78. notificationManager.publish(request).then(() => {
79. console.info("publish success, id= " + this.id);
80. }).catch((err: BusinessError) => {
81. console.error(`publish fail: ${JSON.stringify(err)}`);
82. });
83. } catch (err) {
84. console.error(`publish fail: ${JSON.stringify(err)}`);
85. }
86. }
87. };
```

## backgroundTaskManager.updateBackgroundRunning12+

PhonePC/2in1TabletTVWearable

updateBackgroundRunning(context: Context, bgModes: string[]): Promise<ContinuousTaskNotification>

更新长时任务类型，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。

更新长时任务前，可以通过[getAllContinuousTasks](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetallcontinuoustasks20)接口获取当前所有长时任务信息，如果当前没有已经存在的长时任务，会更新失败。

该接口仅支持更新如下三个接口申请的长时任务：

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning)

[startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning-1)

[startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning12)

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| bgModes | string[] | 是 | 更新后的长时任务类型，取值范围请参考长时任务类型中的[配置项](../harmonyos-guides/continuous-task.md#使用场景)。  **说明：** 支持传入一个或多个类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)> | Promise对象，返回[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)类型对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 9800001 | Memory operation failed. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800003 | Internal transaction failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. try {
8. // 必须先执行startBackgroundRunning，才能调用updateBackgroundRunning，这里假设已经申请过
9. let list: Array<string> = ["audioPlayback"];
10. backgroundTaskManager.updateBackgroundRunning(this.context, list).then(() => {
11. console.info("Operation updateBackgroundRunning succeeded");
12. }).catch((error: BusinessError) => {
13. console.error(`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
14. });
15. } catch (error) {
16. console.error(`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
17. }
18. }
19. };
```

## backgroundTaskManager.getAllContinuousTasks20+

PhonePC/2in1TabletTVWearable

getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>

获取所有长时任务信息，如长时任务ID、长时任务类型等，使用Promise异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskinfo20)[]> | Promise对象，返回所有长时任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. try {
8. // 如果当前没有申请长时任务，则获取到一个空数组
9. backgroundTaskManager.getAllContinuousTasks(this.context).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
10. console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
11. }).catch((error: BusinessError) => {
12. console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## backgroundTaskManager.getAllContinuousTasks20+

PhonePC/2in1TabletTVWearable

getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>

获取所有长时任务信息，如长时任务ID、长时任务类型等。可选择是否获取暂停的长时任务信息，使用Promise异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| includeSuspended | boolean | 是 | 是否获取暂停的长时任务信息， true表示获取， false表示不获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskinfo20)[]> | Promise对象，返回所有长时任务信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800002 | Failed to write data into parcel. Possible reasons: 1. Invalid parameters; 2. Failed to apply for memory. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. try {
8. // 如果当前没有申请长时任务，则获取到一个空数组
9. backgroundTaskManager.getAllContinuousTasks(this.context, false).then((res: backgroundTaskManager.ContinuousTaskInfo[]) => {
10. console.info(`Operation getAllContinuousTasks succeeded. data: ` + JSON.stringify(res));
11. }).catch((error: BusinessError) => {
12. console.error(`Operation getAllContinuousTasks failed. code is ${error.code} message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`Operation getAllContinuousTasks failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## backgroundTaskManager.on('continuousTaskCancel')15+

PhonePC/2in1TabletTVWearable

on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void

注册长时任务取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskCancel'，表示长时任务取消。 |
| callback | Callback<[ContinuousTaskCancelInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskcancelinfo15)> | 是 | 回调函数，返回长时任务取消原因等信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Register a exist callback type; 3. Parameter verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
6. console.info('continuousTaskCancel callback id ' + info.id);
7. console.info('continuousTaskCancel callback reason ' + info.reason);
8. }

10. export default class EntryAbility extends UIAbility {
11. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
12. try {
13. backgroundTaskManager.on("continuousTaskCancel", callback);
14. } catch (error) {
15. console.error(`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## backgroundTaskManager.off('continuousTaskCancel')15+

PhonePC/2in1TabletTVWearable

off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void

解除长时任务取消的监听，使用callback异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消长时任务，固定取值为'continuousTaskCancel'。 |
| callback | Callback<[ContinuousTaskCancelInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskcancelinfo15)> | 否 | 需要取消监听的回调函数，未传入则取消所有注册回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible cause: 1. Callback parameter error; 2. Unregister type has not register; 3. Parameter verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
6. console.info('continuousTaskCancel callback id ' + info.id);
7. console.info('continuousTaskCancel callback reason ' + info.reason);
8. }

10. export default class EntryAbility extends UIAbility {
11. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
12. try {
13. backgroundTaskManager.off("continuousTaskCancel", callback);
14. } catch (error) {
15. console.error(`Operation onContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## backgroundTaskManager.on('continuousTaskSuspend')20+

PhonePC/2in1TabletTVWearable

on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void

注册长时任务暂停的监听，使用callback异步回调。注册该回调后，如果系统首次检测到应用未执行相应的业务，不会直接取消长时任务，而是将长时任务标记为暂停状态，如果连续检测失败，仍会取消长时任务。

长时任务处于暂停状态时，应用退后台会被挂起，回前台自动激活。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskSuspend'，表示长时任务暂停。 |
| callback | Callback<[ContinuousTaskSuspendInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasksuspendinfo20)> | 是 | 回调函数，返回长时任务暂停原因等信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
6. console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
7. console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
8. console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
9. }

11. export default class EntryAbility extends UIAbility {
12. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
13. try {
14. backgroundTaskManager.on("continuousTaskSuspend", callback);
15. } catch (error) {
16. console.error(`Operation onContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
17. }
18. }
19. };
```

## backgroundTaskManager.off('continuousTaskSuspend')20+

PhonePC/2in1TabletTVWearable

off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void

取消长时任务暂停的监听，使用callback异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskSuspend'，表示长时任务暂停。 |
| callback | Callback<[ContinuousTaskSuspendInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasksuspendinfo20)> | 否 | 需要取消监听的回调函数，未传入则取消所有注册的暂停回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskSuspendInfo) {
6. console.info('continuousTaskSuspend callback continuousTaskId: ' + info.continuousTaskId);
7. console.info('continuousTaskSuspend callback suspendState: ' + info.suspendState);
8. console.info('continuousTaskSuspend callback suspendReason: ' + info.suspendReason);
9. }

11. export default class EntryAbility extends UIAbility {
12. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
13. try {
14. backgroundTaskManager.off("continuousTaskSuspend", callback);
15. } catch (error) {
16. console.error(`Operation offContinuousTaskSuspend failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
17. }
18. }
19. };
```

## backgroundTaskManager.on('continuousTaskActive')20+

PhonePC/2in1TabletTVWearable

on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void

注册长时任务激活的监听，使用callback异步回调。应用回前台激活暂停的长时任务。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskActive'，表示长时任务激活。 |
| callback | Callback<[ContinuousTaskActiveInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskactiveinfo20)> | 是 | 回调函数，返回长时任务激活相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
6. console.info('continuousTaskActive callback id: ' + info.id);
7. }

9. export default class EntryAbility extends UIAbility {
10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
11. try {
12. backgroundTaskManager.on("continuousTaskActive", callback);
13. } catch (error) {
14. console.error(`Operation onContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
15. }
16. }
17. };
```

## backgroundTaskManager.off('continuousTaskActive')20+

PhonePC/2in1TabletTVWearable

off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void

取消长时任务激活的监听，使用callback异步回调。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定取值为'continuousTaskActive'，表示长时任务激活。 |
| callback | Callback<[ContinuousTaskActiveInfo](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskactiveinfo20)> | 否 | 需要取消监听的回调函数，未传入则取消所有注册的激活回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. function callback(info: backgroundTaskManager.ContinuousTaskActiveInfo) {
6. console.info('continuousTaskActive callback id: ' + info.id);
7. }

9. export default class EntryAbility extends UIAbility {
10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
11. try {
12. backgroundTaskManager.off("continuousTaskActive", callback);
13. } catch (error) {
14. console.error(`Operation offContinuousTaskActive failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
15. }
16. }
17. };
```

## backgroundTaskManager.startBackgroundRunning21+

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

申请长时任务，一个UIAbility（FA模型则为ServiceAbility）下支持通过本接口申请多个长时任务，使用Promise异步回调。通过本接口申请长时任务时，支持与已存在的长时任务合并通知，具体请参考[ContinuousTaskRequest](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21)。

同一时间最多可存在10个长时任务，长时任务申请成功后，会有通知栏消息，没有提示音。

如果通过本接口申请的一个长时任务中同时包含多种类型，且包含数据传输类型，则在通知栏会发送2个长时任务通知，一个为数据传输类型，另一个为其他类型的合并通知。任意一个通知被移除时，长时任务取消，且另一个通知也会同步移除。接口返回的长时任务通知Id为数据传输类型的Id，主要用于数据传输的进度更新。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| request | [ContinuousTaskRequest](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21) | 是 | 长时任务请求信息，包括长时任务主类型、子类型等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)> | Promise对象，返回长时任务通知信息，包括长时任务ID等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { wantAgent, WantAgent } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. notificationId: number = 0; // 保存通知id
8. continuousTaskId: number | undefined = -1;
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. let wantAgentInfo: wantAgent.WantAgentInfo = {
11. // 请开发者替换为实际被拉起应用的bundleName和abilityName
12. wants: [
13. {
14. bundleName: "com.example.myapplication",
15. abilityName: "EntryAbility"
16. }
17. ],
18. // 设置点击通知后的动作类型
19. actionType: wantAgent.OperationType.START_ABILITY,
20. // 开发者自定义的请求码，用于标识将被执行的动作
21. requestCode: 0,
22. // 设置点击通知后的动作执行属性
23. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
24. };

26. try {
27. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
28. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
29. try {
30. // 如果要合并通知，主类型和子类型都必须相同，combinedTaskNotification为true，continuousTaskId必须存在且合法
31. // 申请主类型为MODE_LOCATION的长时任务
32. let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_LOCATION];
33. let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_NORMAL_NOTIFICATION];
34. let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
35. continuousTaskRequest.backgroundTaskModes =  modeList;
36. continuousTaskRequest.backgroundTaskSubmodes = subModeList;
37. continuousTaskRequest.wantAgent = wantAgentObj;
38. continuousTaskRequest.combinedTaskNotification = false;
39. continuousTaskRequest.continuousTaskId = this.continuousTaskId;
40. backgroundTaskManager.startBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
41. console.info(`Operation startBackgroundRunning succeeded. notificationId is ${res.notificationId} continuousTaskId is ${res.continuousTaskId}`);
42. this.notificationId = res.notificationId;
43. this.continuousTaskId = res.continuousTaskId;
44. }).catch((error: BusinessError) => {
45. console.error(`Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
46. });
47. } catch (error) {
48. console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
49. }
50. });
51. } catch (error) {
52. console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
53. }
54. }
55. };
```

## backgroundTaskManager.updateBackgroundRunning21+

PhonePC/2in1TabletTVWearable

updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>

更新长时任务，使用Promise异步回调。长时任务更新成功后，会有通知栏消息，没有提示音。

更新长时任务还存在如下约束限制：

1. 本接口仅支持更新如下接口申请的长时任务：[startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)。
2. 已经合并的长时任务，且后台任务主类型和子类型均相同，仅支持更新ContinuousTaskRequest.wantAgent中的wants信息（abilityName等），如果类型不同，更新失败。
3. 如果待更新的长时任务或指定的更新类型中包含数据传输类型，直接返回失败。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| request | [ContinuousTaskRequest](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21) | 是 | 长时任务请求信息，包括待更新的长时任务ID等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContinuousTaskNotification](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasknotification12)> | Promise对象，返回更新后的长时任务通知信息，包括长时任务ID等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { wantAgent, WantAgent } from '@kit.AbilityKit';

6. export default class EntryAbility extends UIAbility {
7. notificationId: number = 0; // 保存通知id
8. continuousTaskId: number | undefined = -1; // 长时任务ID
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. let wantAgentInfo: wantAgent.WantAgentInfo = {
11. // 添加需要被拉起应用的bundleName和abilityName, 请开发者替换为实际的bundleName和abilityName
12. wants: [
13. {
14. bundleName: "com.example.myapplication",
15. abilityName: "EntryAbility"
16. }
17. ],
18. // 设置点击通知后的动作类型
19. actionType: wantAgent.OperationType.START_ABILITY,
20. // 开发者自定义的请求码，用于标识将被执行的动作
21. requestCode: 0,
22. // 设置点击通知后的动作执行属性
23. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
24. };

26. try {
27. // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
28. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
29. try {
30. // 必须先执行startBackgroundRunning，才能调用updateBackgroundRunning，请开发者提前申请长时任务
31. let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_LOCATION];
32. let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_NORMAL_NOTIFICATION];
33. let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
34. continuousTaskRequest.backgroundTaskModes = modeList;
35. continuousTaskRequest.backgroundTaskSubmodes = subModeList;
36. continuousTaskRequest.wantAgent = wantAgentObj;
37. continuousTaskRequest.combinedTaskNotification = false;
38. continuousTaskRequest.continuousTaskId = this.continuousTaskId; // 对于更新接口，长时任务ID必须要传且为存在的ID，否则更新失败
39. backgroundTaskManager.updateBackgroundRunning(this.context, continuousTaskRequest).then((res: backgroundTaskManager.ContinuousTaskNotification) => {
40. console.info("Operation updateBackgroundRunning succeeded");
41. this.notificationId = res.notificationId;
42. }).catch((error: BusinessError) => {
43. console.error(`Operation updateBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
44. });
45. } catch (error) {
46. console.error(`Operation updateBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
47. }
48. });
49. } catch (error) {
50. console.error(`Operation getWantAgent failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
51. }
52. }
53. };
```

## backgroundTaskManager.stopBackgroundRunning21+

PhonePC/2in1TabletTVWearable

stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>

取消指定Id的长时任务，使用Promise异步回调。也可以通过[stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning)取消当前UIAbility下所有长时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| continuousTaskId | number | 是 | 长时任务ID。  **说明：** 可以通过[startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)接口的返回值获取当前申请的长时任务ID，或者通过[getAllContinuousTasks](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetallcontinuoustasks20-1)接口获取所有长时任务信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9800001 | Memory operation failed. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |
| 9800006 | Notification verification failed for a continuous task. |
| 9800007 | Continuous task storage failed. |

**示例**：

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

5. export default class EntryAbility extends UIAbility {
6. continuousTaskId: number = 0;
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. try {
9. backgroundTaskManager.stopBackgroundRunning(this.context, this.continuousTaskId).then(() => {
10. console.info("Operation stopBackgroundRunning succeeded");
11. }).catch((error: BusinessError) => {
12. console.error(`Operation stopBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`Operation stopBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## DelaySuspendInfo

PhonePC/2in1TabletTVWearable

短时任务信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestId | number | 否 | 否 | 短时任务的请求ID。 |
| actualDelayTime | number | 否 | 否 | 应用实际申请的短时任务时间，单位：ms。  **说明：** 申请时间最长为3分钟，低电量（[BatteryCapacityLevel](js-apis-battery-info.md#batterycapacitylevel9)为LEVEL\_LOW）时最长为1分钟。 |

## TransientTaskInfo20+

PhonePC/2in1TabletTVWearable

所有短时任务信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remainingQuota | number | 否 | 否 | 应用当日所剩余总配额，单位：ms。 |
| transientTasks | [DelaySuspendInfo](js-apis-resourceschedule-backgroundtaskmanager.md#delaysuspendinfo)[] | 否 | 否 | 当前已申请的所有短时任务信息。 |

## BackgroundMode

PhonePC/2in1TabletTVWearable

长时任务类型。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_TRANSFER | 1 | 数据传输。  使用场景举例：非托管形式的上传、下载，如在浏览器后台上传或下载数据。  **说明：** 在数据传输时，应用需要更新进度，如果进度长时间（超过10分钟）未更新，数据传输的长时任务会被取消。  更新进度的通知类型必须为实况窗，具体实现可参考[startBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)中的示例。 |
| AUDIO\_PLAYBACK | 2 | 音视频播放。  使用场景举例：音频、视频在后台播放，音视频投播。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **说明：** 从API version 20开始，申请/更新AUDIO\_PLAYBACK类型长时任务但不接入AVSession，申请/更新长时任务成功后会在通知栏显示通知。  接入AVSession后，后台任务模块不会发送通知栏通知，由AVSession发送通知。  对于API version 19及之前的版本，后台任务模块不会在通知栏显示通知。 |
| AUDIO\_RECORDING | 3 | 录制。  使用场景举例：录音、录屏退后台。 |
| LOCATION | 4 | 定位导航。 |
| BLUETOOTH\_INTERACTION | 5 | 蓝牙相关业务。  使用场景举例：通过蓝牙传输文件时退后台。 |
| MULTI\_DEVICE\_CONNECTION | 6 | 多设备互联。  使用场景举例：分布式业务连接、投播。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| VOIP13+ | 8 | 音视频通话。  使用场景举例：某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| TASK\_KEEPING | 9 | 计算任务。  使用场景举例：杀毒软件。  **说明：** 从API version 21开始，对PC/2in1设备、非PC/2in1设备但申请了ACL权限为[ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](../harmonyos-guides/restricted-permissions.md#ohospermissionkeep_background_running_system)的应用开放。 API version 20及之前版本，仅对PC/2in1设备开放。 |

## ContinuousTaskNotification12+

PhonePC/2in1TabletTVWearable

长时任务通知信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotType | [notificationManager.SlotType](js-apis-notificationmanager.md#slottype) | 否 | 否 | 长时任务通知的渠道类型。  **说明：** 长时任务申请或更新成功后不支持提示音。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| contentType | [notificationManager.ContentType](js-apis-notificationmanager.md#contenttype) | 否 | 否 | 长时任务通知的内容类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| notificationId | number | 否 | 否 | 长时任务通知 Id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| continuousTaskId15+ | number | 否 | 是 | 长时任务 Id。 |

## ContinuousTaskCancelInfo15+

PhonePC/2in1TabletTVWearable

长时任务取消信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reason | [ContinuousTaskCancelReason](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskcancelreason15) | 否 | 否 | 长时任务取消原因。 |
| id | number | 否 | 否 | 被取消的长时任务 Id。 |

## ContinuousTaskCancelReason15+

PhonePC/2in1TabletTVWearable

长时任务取消原因。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_CANCEL | 1 | 用户取消。 |
| SYSTEM\_CANCEL | 2 | 系统取消。 |
| USER\_CANCEL\_REMOVE\_NOTIFICATION | 3 | 用户移除通知。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_DATA\_TRANSFER\_LOW\_SPEED | 4 | 申请DATA\_TRANSFER类型长时任务，但是数据传输速率低。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION | 5 | 申请AUDIO\_PLAYBACK类型长时任务，但是未接入[AVSession](../harmonyos-guides/avsession-overview.md)。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_AUDIO\_PLAYBACK\_NOT\_RUNNING | 6 | 申请AUDIO\_PLAYBACK类型长时任务，但是未播放音视频。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_AUDIO\_RECORDING\_NOT\_RUNNING | 7 | 申请AUDIO\_RECORDING类型长时任务，但是未录制。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_NOT\_USE\_LOCATION | 8 | 申请LOCATION类型长时任务，但是未使用定位导航。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_NOT\_USE\_BLUETOOTH | 9 | 申请BLUETOOTH\_INTERACTION类型长时任务，但是未使用蓝牙相关业务。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_NOT\_USE\_MULTI\_DEVICE | 10 | 申请MULTI\_DEVICE\_CONNECTION类型长时任务，但是未使用多设备互联。预留接口，暂未启用。 |
| SYSTEM\_CANCEL\_USE\_ILLEGALLY | 11 | 使用非法类型的长时任务，如申请AUDIO\_PLAYBACK类型长时任务，但是使用音视频播放及定位导航业务。预留接口，暂未启用。 |

## BackgroundSubMode16+

PhonePC/2in1TabletTVWearable

长时任务子类型。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAR\_KEY | 1 | 车钥匙。  **说明：**  1. 只有申请BLUETOOTH\_INTERACTION类型的长时任务，车钥匙子类型才能生效。  2. 不支持通过[updateBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning12)接口更新为此类型长时任务。 |

## BackgroundModeType16+

PhonePC/2in1TabletTVWearable

长时任务类型类别。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUB\_MODE | 'subMode' | 子类型。 |

## ContinuousTaskSuspendInfo20+

PhonePC/2in1TabletTVWearable

长时任务暂停信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| continuousTaskId | number | 否 | 否 | 被暂停的长时任务 Id。 |
| suspendState | boolean | 否 | 否 | 长时任务状态，false表示激活，true表示暂停。 |
| suspendReason | [ContinuousTaskSuspendReason](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustasksuspendreason20) | 否 | 否 | 长时任务暂停原因。 |

## ContinuousTaskSuspendReason20+

PhonePC/2in1TabletTVWearable

长时任务暂停原因。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM\_SUSPEND\_DATA\_TRANSFER\_LOW\_SPEED | 4 | 申请DATA\_TRANSFER类型长时任务，但是数据传输速率低。 |
| SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_USE\_AVSESSION | 5 | 申请AUDIO\_PLAYBACK类型长时任务，但是未接入[AVSession](../harmonyos-guides/avsession-overview.md)。 |
| SYSTEM\_SUSPEND\_AUDIO\_PLAYBACK\_NOT\_RUNNING | 6 | 申请AUDIO\_PLAYBACK类型长时任务，但是未播放音视频。 |
| SYSTEM\_SUSPEND\_AUDIO\_RECORDING\_NOT\_RUNNING | 7 | 申请AUDIO\_RECORDING类型长时任务，但是未录制。 |
| SYSTEM\_SUSPEND\_LOCATION\_NOT\_USED | 8 | 申请LOCATION类型长时任务，但是未使用定位导航。 |
| SYSTEM\_SUSPEND\_BLUETOOTH\_NOT\_USED | 9 | 申请BLUETOOTH\_INTERACTION类型长时任务，但是未使用蓝牙相关业务。 |
| SYSTEM\_SUSPEND\_MULTI\_DEVICE\_NOT\_USED | 10 | 申请MULTI\_DEVICE\_CONNECTION类型长时任务，但是未使用多设备互联。 |
| SYSTEM\_SUSPEND\_USED\_ILLEGALLY | 11 | 使用非法类型的长时任务，如申请AUDIO\_PLAYBACK类型长时任务，但是使用音视频播放及定位导航业务。预留接口，暂未启用。 |
| SYSTEM\_SUSPEND\_SYSTEM\_LOAD\_WARNING | 12 | 系统高负载暂停长时任务。预留接口，暂未启用。 |

## ContinuousTaskActiveInfo20+

PhonePC/2in1TabletTVWearable

长时任务激活信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 被激活的长时任务 Id。 |

## ContinuousTaskInfo20+

PhonePC/2in1TabletTVWearable

长时任务信息。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | UIAbility名称。 |
| uid | number | 否 | 否 | 应用的UID。 |
| pid | number | 否 | 否 | 应用进程的PID。 |
| isFromWebView | boolean | 否 | 否 | 是否通过Webview方式申请，即通过系统代理应用申请长时任务。true表示通过Webview方式申请，false表示不通过Webview方式申请。 |
| backgroundModes | string[] | 否 | 否 | [长时任务类型](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)。 |
| backgroundSubModes | string[] | 否 | 否 | [长时任务子类型](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundsubmode16)。 |
| notificationId | number | 否 | 否 | 通知 Id。 |
| continuousTaskId | number | 否 | 否 | 长时任务ID。 |
| abilityId | number | 否 | 否 | UIAbility Id。 |
| wantAgentBundleName | string | 否 | 否 | [WantAgent](js-apis-app-ability-wantagent.md) 配置的包名。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。 |
| wantAgentAbilityName | string | 否 | 否 | [WantAgent](js-apis-app-ability-wantagent.md) 配置的ability名称。WantAgent为通知参数，用于指定点击长时任务通知后跳转的界面，在申请长时任务时作为参数传入。 |
| suspendState | boolean | 否 | 否 | 申请的长时任务是否处于暂停状态。true表示处于暂停状态，false表示处于激活状态。 |
| bundleName23+ | string | 否 | 是 | 应用包名。 |
| appIndex23+ | number | 否 | 是 | 应用分身ID。 |

## ContinuousTaskRequest21+

PhonePC/2in1TabletTVWearable

通常作为[startBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)和[updateBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)接口的入参，用于指定申请或更新的长时任务信息。其中：

1. 通过[startBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)接口申请长时任务时，如果待申请长时任务与当前应用下已存在长时任务，两者的主类型和子类型均相同，且combinedTaskNotification均取值为true，则会合并通知。否则不会合并通知。
2. 如果长时任务本身没有通知，则不会合并，长时任务类型是否会通知请参考[BackgroundTaskMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)。
3. 如果长时任务类型中包含数据传输类型，则不会合并通知。
4. 通知合并后不能取消合并，已合并的不能更新成不合并。
5. 通知合并后，点击通知栏消息，会跳转到第一个申请的长时任务对应的UIAbility，如果调用了更新接口，则跳转到最后一次更新的长时任务对应的UIAbility。
6. 通过[updateBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)接口更新长时任务时，传入的continuousTaskId必须存在，否则更新失败。
7. 从API version 22开始支持特殊场景类型[MODE\_SPECIAL\_SCENARIO\_PROCESSING](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)的长时任务。必须单独使用且不支持通知合并，即申请或更新长时任务时，长时任务类型只能有特殊场景类型，否则返回错误。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundTaskModes | [BackgroundTaskMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)[] | 否 | 否 | 长时任务主类型。  **说明：** 主类型与子类型必须匹配。 |
| backgroundTaskSubmodes | [BackgroundTaskSubmode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtasksubmode21)[] | 否 | 否 | 长时任务子类型。  **说明：** 主类型与子类型必须匹配。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md#wantagent) | 否 | 否 | 通知参数，用于指定点击长时任务通知后跳转的界面。 |
| combinedTaskNotification | boolean | 否 | 是 | 是否合并通知，true表示合并，false表示不合并，默认为false。  **说明：** 该属性在[updateBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)接口中不生效，如需在已有任务上合并通知，请重新申请该任务，并在申请时设置为支持合并。 |
| continuousTaskId | number | 否 | 是 | 长时任务ID，默认值为-1。  **说明：** 如果combinedTaskNotification取值为true，则该值为必填项，且必须是存在的ID。  作为[updateBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)接口入参时，该属性必填，且必须是存在的ID。  可以通过[getAllContinuousTasks](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetallcontinuoustasks20-1)接口查看当前所有长时任务信息。 |

### isModeSupported21+

PhonePC/2in1TabletTVWearable

isModeSupported(): boolean

查询当前[ContinuousTaskRequest](js-apis-resourceschedule-backgroundtaskmanager.md#continuoustaskrequest21)设置的长时任务主类型，是否支持申请长时任务。是否支持申请长时任务请参考[BackgroundTaskMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)的说明。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回长时任务主类型是否支持。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. let isModeSupported: boolean = false;
8. let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
9. let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_TASK_KEEPING];
10. continuousTaskRequest.backgroundTaskModes = modeList;
11. try {
12. isModeSupported = continuousTaskRequest.isModeSupported();
13. console.info(`Operation isModeSupported succeeded. isModeSupported is ${isModeSupported}`);
14. } catch (error) {
15. console.error(`Operation startBackgroundRunning failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

### requestAuthFromUser22+

PhonePC/2in1TabletTVWearable

requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void

请求用户授权是否能在后台长时间运行，使用callback异步回调。接口调用成功会发送横幅通知，有提示音。仅适用于特殊场景类型[MODE\_SPECIAL\_SCENARIO\_PROCESSING](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)的长时任务。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回9800005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |
| callback | Callback<[UserAuthResult](js-apis-resourceschedule-backgroundtaskmanager.md#userauthresult22)> | 是 | 用户操作后，返回授权结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. function callbackAuth(authResult: backgroundTaskManager.UserAuthResult) {
6. console.info('Operation requestAuthFromUser success. auth result: ' + JSON.stringify(authResult));
7. }

9. export default class EntryAbility extends UIAbility {
10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
11. let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
12. let modeList: Array<number> = [backgroundTaskManager.BackgroundTaskMode.MODE_SPECIAL_SCENARIO_PROCESSING];
13. continuousTaskRequest.backgroundTaskModes = modeList;
14. let subModeList: Array<number> = [backgroundTaskManager.BackgroundTaskSubmode.SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION];
15. continuousTaskRequest.backgroundTaskSubmodes = subModeList;
16. try {
17. continuousTaskRequest.requestAuthFromUser(this.context, callbackAuth);
18. console.info('Operation requestAuthFromUser succeeded.');
19. } catch (error) {
20. console.error(`Operation requestAuthFromUser failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
21. }
22. }
23. };
```

### checkSpecialScenarioAuth22+

PhonePC/2in1TabletTVWearable

checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>

查询用户是否授权能在后台长时间运行。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**设备行为差异：** 该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回9800005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。  **说明：** Stage模型中，仅支持UIAbility申请；FA模型中，仅支持ServiceAbility申请。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UserAuthResult](js-apis-resourceschedule-backgroundtaskmanager.md#userauthresult22)> | Promise对象，返回用户授权结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[backgroundTaskManager错误码](errorcode-backgroundtaskmgr.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 9800004 | System service operation failed. |
| 9800005 | Continuous task verification failed. |

**示例：**

```
1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. try {
8. let continuousTaskRequest = new backgroundTaskManager.ContinuousTaskRequest();
9. continuousTaskRequest.checkSpecialScenarioAuth(this.context).then((res: backgroundTaskManager.UserAuthResult) => {
10. console.info('Operation checkSpecialScenarioAuth succeeded. data: ' + JSON.stringify(res));
11. }).catch((error: BusinessError) => {
12. console.error(`Operation checkSpecialScenarioAuth failed. code is ${error.code} message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`Operation checkSpecialScenarioAuth failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
16. }
17. }
18. };
```

## BackgroundTaskMode21+

PhonePC/2in1TabletTVWearable

长时任务主类型。通常与长时任务子类型[BackgroundTaskSubmode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtasksubmode21)配合使用，对照关系请参考长时任务主类型与子类型对照表，两者共同作为API version 21新增的[申请](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)、[更新](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)长时任务接口入参，用于指定长时任务类型。

仅当主类型为MODE\_SPECIAL\_SCENARIO\_PROCESSING特殊场景类型，或非PC/2in1设备主类型为MODE\_TASK\_KEEPING计算任务时，调用长时任务相关接口时需同时申请ACL权限[ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](../harmonyos-guides/restricted-permissions.md#ohospermissionkeep_background_running_system)，其他场景无需申请该权限。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_DATA\_TRANSFER | 1 | 数据传输。  使用场景举例：非托管形式的上传、下载，如在浏览器后台上传或下载数据。  **说明：**  1. 在数据传输时，应用需要更新进度，如果进度长时间（超过10分钟）未更新，数据传输的长时任务会被取消。  2. 更新进度的通知类型必须为实况窗，具体实现可参考[startBackgroundRunning()](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning12)中的示例。 |
| MODE\_AUDIO\_PLAYBACK | 2 | 音视频播放。  使用场景举例：音频、视频在后台播放，音视频投播。  **说明：** 申请/更新MODE\_AUDIO\_PLAYBACK类型长时任务但不接入AVSession，申请/更新长时任务成功后会在通知栏显示通知。接入AVSession后，后台任务模块不会发送通知栏通知，由AVSession发送通知。 |
| MODE\_AUDIO\_RECORDING | 3 | 录制。  使用场景举例：录音、录屏退后台。 |
| MODE\_LOCATION | 4 | 定位导航。 |
| MODE\_BLUETOOTH\_INTERACTION | 5 | 蓝牙相关业务。  使用场景举例：通过蓝牙传输文件时退后台。 |
| MODE\_MULTI\_DEVICE\_CONNECTION | 6 | 多设备互联。  使用场景举例：分布式业务连接、投播。 |
| MODE\_VOIP | 8 | 音视频通话。  使用场景举例：某些聊天类应用（具有音视频业务）音频、视频通话时退后台。 |
| MODE\_TASK\_KEEPING | 9 | 计算任务。  使用场景举例：杀毒软件。  **说明：** 仅对PC/2in1设备开放，或者非PC/2in1设备但申请了ACL权限为[ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](../harmonyos-guides/restricted-permissions.md#ohospermissionkeep_background_running_system)的应用开放。 |
| MODE\_AV\_PLAYBACK\_AND\_RECORD22+ | 12 | 多媒体相关业务。  使用场景举例：音视频播放、录制、音视频通话场景，场景需与长时任务子类型相匹配。在上述场景下，选择此类型或者对应的长时任务主类型均可。例如：音视频播放场景可以申请MODE\_AUDIO\_PLAYBACK或者MODE\_AV\_PLAYBACK\_AND\_RECORD长时任务主类型。 |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING22+ | 13 | 特殊场景类型（仅对Phone、Tablet、PC/2in1设备开放）。  使用场景举例：应用在后台导出媒体文件、应用使用三方投播组件在后台进行投播，场景需与长时任务子类型相匹配。  **说明：**  1. 如果应用需要在后台长时间运行，可以通过[requestAuthFromUser](js-apis-resourceschedule-backgroundtaskmanager.md#requestauthfromuser22)接口请求用户授权、通过[checkSpecialScenarioAuth](js-apis-resourceschedule-backgroundtaskmanager.md#checkspecialscenarioauth22)接口查询用户授权结果。  2. 仅对申请ACL权限[ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](../harmonyos-guides/restricted-permissions.md#ohospermissionkeep_background_running_system)的应用开放。  3. 必须单独使用且不支持通知合并，即申请或更新长时任务时，长时任务类型只能有特殊场景类型，否则返回错误。 |

## BackgroundTaskSubmode21+

PhonePC/2in1TabletTVWearable

长时任务子类型。通常与长时任务主类型[BackgroundTaskMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21)配合使用，对照关系请参考长时任务主类型与子类型对照表，两者共同作为API version 21新增的申请、更新长时任务接口入参，用于指定长时任务类型。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION | 1 | 车钥匙类型，通知类型为普通文本通知。 |
| SUBMODE\_NORMAL\_NOTIFICATION | 2 | 普通文本通知。 |
| SUBMODE\_LIVE\_VIEW\_NOTIFICATION | 3 | 实况窗通知。 |
| SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION22+ | 4 | 音视频播放，通知类型为普通文本通知。根据实际场景选择是否接入[AVSession](../harmonyos-guides/avsession-overview.md)。 |
| SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK22+ | 5 | 已接入[AVSession](../harmonyos-guides/avsession-overview.md)的音视频播放场景，通知类型为普通文本类型。 |
| SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION22+ | 6 | 录音，通知类型为普通文本通知。 |
| SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION22+ | 7 | 录屏，通知类型为普通文本通知。 |
| SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION22+ | 8 | 通话，通知类型为普通文本通知。 |
| SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION22+ | 9 | 媒体处理，例如：应用在后台导出媒体文件，通知类型为普通文本通知。 |
| SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION22+ | 10 | 视频投播，例如：应用使用三方投播组件在后台进行投播，通知类型为普通文本通知。 |
| SUBMODE\_WORK\_OUT\_NORMAL\_NOTIFICATION23+ | 11 | 运动，例如：应用在后台有室内跑步场景，通知类型为普通文本通知。  **模型约束：** 此接口仅可在Stage模型下使用。 |

**长时任务主类型与子类型对照表：**

| [长时任务主类型](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmode21) | [长时任务子类型](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtasksubmode21) |
| --- | --- |
| MODE\_DATA\_TRANSFER | SUBMODE\_LIVE\_VIEW\_NOTIFICATION |
| MODE\_AUDIO\_PLAYBACK | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_AUDIO\_RECORDING | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_LOCATION | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_BLUETOOTH\_INTERACTION | SUBMODE\_NORMAL\_NOTIFICATION  SUBMODE\_CAR\_KEY\_NORMAL\_NOTIFICATION |
| MODE\_MULTI\_DEVICE\_CONNECTION | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_VOIP | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_TASK\_KEEPING | SUBMODE\_NORMAL\_NOTIFICATION |
| MODE\_AV\_PLAYBACK\_AND\_RECORD22+ | SUBMODE\_AUDIO\_PLAYBACK\_NORMAL\_NOTIFICATION22+  SUBMODE\_AVSESSION\_AUDIO\_PLAYBACK22+  SUBMODE\_AUDIO\_RECORD\_NORMAL\_NOTIFICATION22+  SUBMODE\_SCREEN\_RECORD\_NORMAL\_NOTIFICATION22+  SUBMODE\_VOICE\_CHAT\_NORMAL\_NOTIFICATION22+ |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING22+ | SUBMODE\_MEDIA\_PROCESS\_NORMAL\_NOTIFICATION22+  SUBMODE\_VIDEO\_BROADCAST\_NORMAL\_NOTIFICATION22+  SUBMODE\_WORK\_OUT\_NORMAL\_NOTIFICATION23+ |

## UserAuthResult22+

PhonePC/2in1TabletTVWearable

用户授权结果。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOT\_SUPPORTED | 0 | 不支持。例如：申请的长时任务主类型非MODE\_SPECIAL\_SCENARIO\_PROCESSING时，不支持申请用户授权是否能在后台长时间运行。 |
| NOT\_DETERMINED | 1 | 用户未操作。 |
| DENIED | 2 | 拒绝。 |
| GRANTED\_ONCE | 3 | 本次允许。  **说明：** 在应用退出时该授权记录会被清除。 |
| GRANTED\_ALWAYS | 4 | 始终允许。  **说明：**  当接收到以下公共事件时，相关授权记录将被清除：  [COMMON\_EVENT\_PACKAGE\_ADDED](commoneventmanager-definitions.md#common_event_package_added)、[COMMON\_EVENT\_PACKAGE\_REMOVED](commoneventmanager-definitions.md#common_event_package_removed)、[COMMON\_EVENT\_BUNDLE\_REMOVED](commoneventmanager-definitions.md#common_event_bundle_removed)、[COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED](commoneventmanager-definitions.md#common_event_package_fully_removed)、[COMMON\_EVENT\_PACKAGE\_CHANGED](commoneventmanager-definitions.md#common_event_package_changed)。 |
