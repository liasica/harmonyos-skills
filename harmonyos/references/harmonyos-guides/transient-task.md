---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transient-task
title: 短时任务(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 短时任务(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5f7508e73597d148ae82dd9e083d806602b51b84e9bef0f5d2e01747d50a82f4
---

## 概述

应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用需在被挂起前，执行一些耗时不长的任务，如状态保存、消息发送等，可以通过本文申请短时任务，扩展应用在后台的运行时间。

## 约束与限制

* **申请时机**：应用需要在前台或[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)回调内，申请短时任务，否则会申请失败。
* **数量限制**：一个应用同一时刻最多申请3个短时任务。以图1为例，在①②③时间段内的任意时刻，应用申请了2个短时任务；在④时间段内的任意时刻，应用申请了1个短时任务。
* **配额机制**：一个应用会有一定的短时任务配额（根据系统状态和用户习惯调整），单日（24小时内）配额默认为10分钟，低电量（[BatteryCapacityLevel](../harmonyos-references/js-apis-battery-info.md#batterycapacitylevel9)为LEVEL\_LOW）时单次配额默认为1分钟，配额消耗完后不允许再申请短时任务。同时，系统提供获取对应短时任务剩余时间的查询接口[backgroundTaskManager.getRemainingDelayTime](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetremainingdelaytime-1)，用以查询本次短时任务剩余时间，以确认是否继续运行其他业务。
* **配额计算**：仅当应用在后台时，对应用下的短时任务计时；同一个应用下的同一个时间段的短时任务，不重复计时。以下图为例：应用有两个短时任务A和B，在前台时申请短时任务A，应用退至后台后开始计时为①，应用进入前台②后不计时，再次进入后台③后开始计时，短时任务A结束后，由于阶段④仍然有短时任务B，所以该阶段继续计时。因此，在这个过程中，该应用短时任务总耗时为①+③+④。

  **图1** 短时任务配额计算原理图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/c0fbATopSFmLUti7I8ONGQ/zh-cn_image_0000002552798608.png?HW-CC-KV=V1&HW-CC-Date=20260427T234107Z&HW-CC-Expire=86400&HW-CC-Sign=68F1682A5D8A1414F8EACA4C52D03D0946BD0A7755D7D8DB769ADDE2F7E1DC1B)

  说明

  任务完成后，应用需主动取消短时任务，否则会影响应用当日短时任务的剩余配额。
* **超时**：短时任务即将超时时，系统会回调应用，应用需要取消短时任务。如果超时不取消，系统会对应用进行管控，包括进程挂起和进程终止。

## 接口说明

**表1** 主要接口

以下是短时任务开发使用的主要接口，更多接口及使用方式请见[后台任务管理](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerrequestsuspenddelay) | 申请短时任务。 |
| [getRemainingDelayTime(requestId: number): Promise<number>](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagergetremainingdelaytime-1) | 获取对应短时任务的剩余时间。 |
| [cancelSuspendDelay(requestId: number): void](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagercancelsuspenddelay) | 取消短时任务。 |

## 开发步骤

1. 导入模块。

   ```
   1. import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 申请短时任务并实现回调。此处回调在短时任务即将结束时触发，与应用的业务功能不耦合，短时任务申请成功后，正常执行应用本身的任务。

   ```
   1. let id: number;         // 申请短时任务ID
   2. let delayTime: number;  // 本次申请短时任务的剩余时间

   4. // 申请短时任务
   5. function requestSuspendDelay() {
   6. let myReason = 'test requestSuspendDelay';   // 申请原因
   7. try {
   8. let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
   9. // 回调函数。应用申请的短时任务即将超时，通过此函数回调应用，执行一些清理和标注工作，并取消短时任务
   10. console.info('suspend delay task will timeout');
   11. try {
   12. backgroundTaskManager.cancelSuspendDelay(id);
   13. } catch (error) {
   14. console.error(`Operation requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   15. }
   16. })
   17. id = delayInfo.requestId;
   18. delayTime = delayInfo.actualDelayTime;
   19. console.info(`Operation requestSuspendDelay failed. id is ${id} delayTime is ${delayTime}`);
   20. } catch (error) {
   21. console.error(`Operation requestSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   22. }
   23. }
   ```

   [TransientTaskDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/TransientTask/entry/src/main/ets/pages/TransientTaskDialog.ets#L19-L43)
3. 获取短时任务剩余时间。查询本次短时任务的剩余时间，用以判断是否继续运行其他业务，例如应用有两个小任务，在执行完第一个小任务后，可以判断本次短时任务是否还有剩余时间从而决定是否执行第二个小任务。

   ```
   1. async function getRemainingDelayTime() {
   2. backgroundTaskManager.getRemainingDelayTime(id).then((res: number) => {
   3. console.info(`Succeeded in getting remaining delay time. time is ${res}`);
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to get remaining delay time. Code: ${err.code}, message: ${err.message}`);
   6. })
   7. }
   ```

   [TransientTaskDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/TransientTask/entry/src/main/ets/pages/TransientTaskDialog.ets#L45-L53)
4. 取消短时任务。

   ```
   1. function cancelSuspendDelay() {
   2. try {
   3. backgroundTaskManager.cancelSuspendDelay(id);
   4. console.info('Operation cancelSuspendDelay Succeeded.');
   5. } catch (error) {
   6. console.error(`Operation cancelSuspendDelay failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   7. }
   8. }
   ```

   [TransientTaskDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/TransientTask/entry/src/main/ets/pages/TransientTaskDialog.ets#L55-L64)
