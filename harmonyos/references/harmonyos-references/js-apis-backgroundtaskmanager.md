---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-backgroundtaskmanager
title: @ohos.backgroundTaskManager (后台任务管理)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > 已停止维护的接口 > @ohos.backgroundTaskManager (后台任务管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b5b0069efde0f39ad01fc8c9d142e5d05a639a1a111a91cb4526292c5f8fcdd7
---

本模块提供后台任务管理能力。

当应用或业务模块处于后台（无可见界面）时，如果有需要继续执行或者后续执行的业务，可基于业务类型，申请短时任务延迟挂起（Suspend）或者长时任务避免进入挂起状态。

应用有不可中断且短时间能完成的任务时（如，用户在文件管理器上点击垃圾文件清理，若清理未完成时退到后台，文件管理器需要申请短时任务完成清理），可以使用短时任务机制。

应用中存在用户能够直观感受到的且需要一直在后台运行的业务时（如，后台播放音乐），可以使用长时任务机制。

说明

* 从API Version 9 开始，该接口不再维护，推荐使用新接口[@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
```

## backgroundTaskManager.requestSuspendDelay(deprecated)

PhonePC/2in1TabletTVWearable

requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo

后台应用申请延迟挂起。

延迟挂起时间一般情况下默认值为3分钟，低电量（依据系统低电量广播）时默认值为1分钟。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.requestSuspendDelay](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelay)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | string | 是 | 延迟挂起申请的原因。 |
| callback | Callback<void> | 是 | 延迟即将超时的回调函数，一般在超时前6秒通过此回调通知应用。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [DelaySuspendInfo](js-apis-backgroundtaskmanager.md#delaysuspendinfodeprecated) | 返回延迟挂起信息。 |

**示例**：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import { BusinessError } from '@ohos.base';

4. // 设置延迟任务挂起的原因
5. let myReason = 'test requestSuspendDelay';
6. // 申请延迟任务
7. let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
8. console.info("Request suspension delay will time out.");
9. })
10. // 打印延迟任务信息
11. let id = delayInfo.requestId;
12. let time = delayInfo.actualDelayTime;
13. console.info("The requestId is: " + id);
14. console.info("The actualDelayTime is: " + time);
```

## backgroundTaskManager.getRemainingDelayTime(deprecated)

PhonePC/2in1TabletTVWearable

getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void

获取应用程序进入挂起状态前的剩余时间，使用callback形式返回。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.getRemainingDelayTime](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetremainingdelaytime)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](js-apis-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。用于返回应用程序进入挂起状态之前的剩余时间，以毫秒为单位。 |

**示例**：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import { BusinessError } from '@ohos.base';

4. let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
5. backgroundTaskManager.getRemainingDelayTime(delayInfo.requestId, (err: BusinessError, res: number) => {
6. if(err) {
7. console.info('callback => Operation getRemainingDelayTime failed. Cause: ' + err.code);
8. } else {
9. console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
10. }
11. })
```

## backgroundTaskManager.getRemainingDelayTime(deprecated)

PhonePC/2in1TabletTVWearable

getRemainingDelayTime(requestId: number): Promise<number>

获取应用程序进入挂起状态前的剩余时间，使用Promise形式返回。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.getRemainingDelayTime](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetremainingdelaytime-1)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](js-apis-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 指定的Promise回调方法。返回应用程序进入挂起状态之前的剩余时间，以毫秒为单位。 |

**示例**：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import { BusinessError } from '@ohos.base';

4. let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
5. backgroundTaskManager.getRemainingDelayTime(delayInfo.requestId).then((res:number) => {
6. console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
7. }).catch((err : BusinessError) => {
8. console.info('promise => Operation getRemainingDelayTime failed. Cause: ' + err.code);
9. })
```

## backgroundTaskManager.cancelSuspendDelay(deprecated)

PhonePC/2in1TabletTVWearable

cancelSuspendDelay(requestId: number): void

取消延迟挂起。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.cancelSuspendDelay](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagercancelsuspenddelay)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](js-apis-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |

**示例**：

```
1. let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
2. backgroundTaskManager.cancelSuspendDelay(delayInfo.requestId);
```

## backgroundTaskManager.startBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void

向系统申请长时任务，使用callback形式返回结果。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning)替代。

**需要权限:** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| bgMode | [BackgroundMode](js-apis-backgroundtaskmanager.md#backgroundmodedeprecated) | 是 | 向系统申请的后台模式。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 通知参数，用于指定长时任务通知点击后跳转的界面。 |
| callback | AsyncCallback<void> | 是 | callback形式返回启动长时任务的结果。 |

**示例**：

FA模型示例：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
4. import { BusinessError } from '@ohos.base';

6. function callback(err: BusinessError, data: void) {
7. if (err) {
8. console.error("Operation startBackgroundRunning failed Cause: " + err);
9. } else {
10. console.info("Operation startBackgroundRunning succeeded");
11. }
12. }

14. let wantAgentInfo : wantAgent.WantAgentInfo = {
15. wants: [
16. {
17. bundleName: "com.example.myapplication",
18. abilityName: "EntryAbility"
19. }
20. ],
21. operationType: wantAgent.OperationType.START_ABILITY,
22. requestCode: 0,
23. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
24. };

26. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
27. backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
28. backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
29. });
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import backgroundTaskManager from '@ohos.backgroundTaskManager';
3. import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
4. import Want from '@ohos.app.ability.Want';
5. import AbilityConstant from '@ohos.app.ability.AbilityConstant';
6. import { BusinessError } from '@ohos.base';

8. function callback(err: BusinessError, data: void) {
9. if (err) {
10. console.error("Operation startBackgroundRunning failed Cause: " + err);
11. } else {
12. console.info("Operation startBackgroundRunning succeeded");
13. }
14. }

16. export default class EntryAbility extends UIAbility {
17. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
18. let wantAgentInfo : wantAgent.WantAgentInfo = {
19. wants: [
20. {
21. bundleName: "com.example.myapplication",
22. abilityName: "EntryAbility"
23. }
24. ],
25. operationType: wantAgent.OperationType.START_ABILITY,
26. requestCode: 0,
27. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
28. };

30. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
31. backgroundTaskManager.startBackgroundRunning(this.context,
32. backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
33. });
34. }
35. };
```

## backgroundTaskManager.startBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>

向系统申请长时任务，使用promise形式返回结果。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.startBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning-1)替代。

**需要权限:** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| bgMode | [BackgroundMode](js-apis-backgroundtaskmanager.md#backgroundmodedeprecated) | 是 | 向系统申请的后台模式。 |
| wantAgent | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 通知参数，用于指定长时任务通知点击跳转的界面。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 使用Promise形式返回结果。 |

**示例**：

FA模型示例（需使用js代码开发）：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
4. import { BusinessError } from '@ohos.base';

6. let wantAgentInfo : wantAgent.WantAgentInfo = {
7. wants: [
8. {
9. bundleName: "com.example.myapplication",
10. abilityName: "EntryAbility"
11. }
12. ],
13. operationType: wantAgent.OperationType.START_ABILITY,
14. requestCode: 0,
15. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
16. };

18. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
19. backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
20. backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
21. console.info("Operation startBackgroundRunning succeeded");
22. }).catch((err: BusinessError) => {
23. console.error("Operation startBackgroundRunning failed Cause: " + err);
24. });
25. });
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import backgroundTaskManager from '@ohos.backgroundTaskManager';
3. import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
4. import Want from '@ohos.app.ability.Want';
5. import AbilityConstant from '@ohos.app.ability.AbilityConstant';
6. import { BusinessError } from '@ohos.base';

8. export default class EntryAbility extends UIAbility {
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. let wantAgentInfo : wantAgent.WantAgentInfo = {
11. wants: [
12. {
13. bundleName: "com.example.myapplication",
14. abilityName: "EntryAbility"
15. }
16. ],
17. // 点击通知后，动作类型
18. operationType: wantAgent.OperationType.START_ABILITY,
19. requestCode: 0,
20. // 点击通知后，动作执行属性
21. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
22. };

24. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
25. backgroundTaskManager.startBackgroundRunning(this.context,
26. backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
27. console.info("Operation startBackgroundRunning succeeded");
28. }).catch((err: BusinessError) => {
29. console.error("Operation startBackgroundRunning failed Cause: " + err);
30. });
31. });
32. }
33. };
```

## backgroundTaskManager.stopBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void

向系统申请取消长时任务，使用callback形式返回结果。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| callback | AsyncCallback<void> | 是 | callback形式返回启动长时任务的结果。 |

**示例**：

FA模型示例（需使用js代码开发）：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import { BusinessError } from '@ohos.base';

5. function callback(err: BusinessError, data: void) {
6. if (err) {
7. console.error("Operation stopBackgroundRunning failed Cause: " + err);
8. } else {
9. console.info("Operation stopBackgroundRunning succeeded");
10. }
11. }

13. backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext(), callback);
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import backgroundTaskManager from '@ohos.backgroundTaskManager';
3. import Want from '@ohos.app.ability.Want';
4. import AbilityConstant from '@ohos.app.ability.AbilityConstant';
5. import { BusinessError } from '@ohos.base';

7. function callback(err: BusinessError, data: void) {
8. if (err) {
9. console.error("Operation stopBackgroundRunning failed Cause: " + err);
10. } else {
11. console.info("Operation stopBackgroundRunning succeeded");
12. }
13. }

15. export default class EntryAbility extends UIAbility {
16. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
17. backgroundTaskManager.stopBackgroundRunning(this.context, callback);
18. }
19. };
```

## backgroundTaskManager.stopBackgroundRunning(deprecated)

PhonePC/2in1TabletTVWearable

stopBackgroundRunning(context: Context): Promise<void>

向系统申请取消长时任务，使用promise形式返回结果。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.stopBackgroundRunning](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning-1)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用运行的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 使用Promise形式返回结果。 |

**示例**：

FA模型示例：

```
1. import backgroundTaskManager from '@ohos.backgroundTaskManager';
2. import featureAbility from '@ohos.ability.featureAbility';
3. import { BusinessError } from '@ohos.base';

5. // 取消长时任务
6. backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext()).then(() => {
7. console.info("Operation stopBackgroundRunning succeeded");
8. }).catch((err: BusinessError) => {
9. console.error("Operation stopBackgroundRunning failed Cause: " + err);
10. });
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import backgroundTaskManager from '@ohos.backgroundTaskManager';
3. import Want from '@ohos.app.ability.Want';
4. import AbilityConstant from '@ohos.app.ability.AbilityConstant';
5. import { BusinessError } from '@ohos.base';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
9. // 取消长时任务
10. backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
11. console.info("Operation stopBackgroundRunning succeeded");
12. }).catch((err: BusinessError) => {
13. console.error("Operation stopBackgroundRunning failed Cause: " + err);
14. });
15. }
16. };
```

## DelaySuspendInfo(deprecated)

PhonePC/2in1TabletTVWearable

延迟挂起信息。

说明

从API version 7开始支持，从API version 9开始废弃。建议使用[DelaySuspendInfo](js-apis-resourceschedule-backgroundtaskmanager.md#delaysuspendinfo)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestId | number | 否 | 否 | 延迟挂起的请求ID。 |
| actualDelayTime | number | 否 | 否 | 应用的实际挂起延迟时间，以毫秒为单位。  一般情况下默认值为180000，低电量（依据系统低电量广播）时默认值为60000。 |

## BackgroundMode(deprecated)

PhonePC/2in1TabletTVWearable

长时任务类型。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[BackgroundMode](js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_TRANSFER | 1 | 数据传输。 |
| AUDIO\_PLAYBACK | 2 | 音频播放。 |
| AUDIO\_RECORDING | 3 | 录音。 |
| LOCATION | 4 | 定位导航。 |
| BLUETOOTH\_INTERACTION | 5 | 蓝牙相关。 |
| MULTI\_DEVICE\_CONNECTION | 6 | 多设备互联。 |
| TASK\_KEEPING | 9 | 计算任务（仅在特定设备生效）。 |
