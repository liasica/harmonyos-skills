---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/work-scheduler
title: 延迟任务(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 延迟任务(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87dc0b16184a4688559d2c20b7d4d64f5941fe7d3025a9aa176f544262c7eccf
---

## 概述

### 功能介绍

应用退至后台后，需要执行时效性要求不高的任务，例如有网络时不定期主动获取邮件等，可以使用延迟任务。当应用满足设定的触发条件（包括网络类型、充电类型、存储状态、电池状态、定时状态等）时，将任务添加到执行队列，系统会根据内存、功耗、设备温度、用户使用习惯等统一调度拉起应用，执行相应的延迟任务。

### 运行原理

**图1** 延迟任务实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/gO47eFgoSTOsrJ-LKhHB1g/zh-cn_image_0000002558605094.png?HW-CC-KV=V1&HW-CC-Date=20260429T052932Z&HW-CC-Expire=86400&HW-CC-Sign=3340E39A31BDAC2B8C357B85337CFB558F122E90ECF5EDB53F60ACF0302ADA73)

应用调用延迟任务接口添加、删除、查询延迟任务，延迟任务管理模块会根据任务设置的条件（通过[WorkInfo](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workinfo)参数设置，包括网络类型、充电类型、存储状态等）和系统状态（包括内存、功耗、设备温度、用户使用习惯等）统一决策调度时机。

当满足调度条件或调度结束时，系统会回调应用[WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md)中 onWorkStart() 或 onWorkStop() 的方法，同时会为应用单独创建一个Extension扩展进程用以承载[WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md)，并给[WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md)一定的活动周期，开发者可以在对应回调方法中实现自己的任务逻辑。

### 约束与限制

* **数量限制**：一个应用同一时刻最多申请10个延迟任务。
* **执行频率限制**：系统会根据应用的活跃分组，对延迟任务做分级管控，限制延迟任务调度的执行频率。

  **表1** 应用活跃程度分组

  | 应用活跃分组 | 延迟任务执行频率 |
  | --- | --- |
  | 活跃分组 | 最小间隔2小时 |
  | 经常使用分组 | 最小间隔4小时 |
  | 常用分组 | 最小间隔24小时 |
  | 极少使用分组 | 最小间隔48小时 |
  | 受限使用分组 | 禁止 |
  | 从未使用分组 | 禁止 |
* **超时**：WorkSchedulerExtensionAbility单次回调最长运行2分钟。如果超时不取消，系统会终止对应的Extension进程。
* **调度延迟**：系统会根据内存、功耗、设备温度、用户使用习惯等统一调度，如当系统内存资源不足或温度达到一定档位时，系统将延迟调度该任务。
* **WorkSchedulerExtensionAbility接口调用限制**：为保障系统安全性和稳定性，防止延迟任务滥用系统资源，对WorkSchedulerExtensionAbility能力进行管控，在WorkSchedulerExtensionAbility中限制以下接口的调用：

  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md)

  [@ohos.backgroundTaskManager (后台任务管理)](../harmonyos-references/js-apis-backgroundtaskmanager.md)

  [@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)

  [@ohos.multimedia.audio (音频管理)](../harmonyos-references/arkts-apis-audio.md)

  [@ohos.multimedia.media (媒体服务)](../harmonyos-references/arkts-apis-media.md)

## 接口说明

**表2** 延迟任务主要接口

以下是延迟任务开发使用的相关接口，更多接口及使用方式请见[延迟任务调度](../harmonyos-references/js-apis-resourceschedule-workscheduler.md)文档。

| 接口名 | 接口描述 |
| --- | --- |
| [startWork(work: WorkInfo): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerstartwork) | 申请延迟任务。 |
| [stopWork(work: WorkInfo, needCancel?: boolean): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerstopwork) | 取消延迟任务。 |
| [getWorkStatus(workId: number, callback: AsyncCallback<WorkInfo>): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulergetworkstatus) | 获取延迟任务状态（Callback形式）。 |
| [getWorkStatus(workId: number): Promise<WorkInfo>](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulergetworkstatus-1) | 获取延迟任务状态（Promise形式）。 |
| [obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerobtainallworks10) | 获取所有延迟任务（Callback形式）。 |
| [obtainAllWorks(): Promise<Array<WorkInfo>>](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerobtainallworks) | 获取所有延迟任务（Promise形式）。 |
| [stopAndClearWorks(): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerstopandclearworks) | 停止并清除任务。 |
| [isLastWorkTimeOut(workId: number, callback: AsyncCallback<boolean>): void](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerislastworktimeout10) | 获取上次任务是否超时（针对RepeatWork，Callback形式）。 |
| [isLastWorkTimeOut(workId: number): Promise<boolean>](../harmonyos-references/js-apis-resourceschedule-workscheduler.md#workschedulerislastworktimeout) | 获取上次任务是否超时（针对RepeatWork，Promise形式）。 |

**表3** 延迟任务回调接口

以下是延迟任务回调开发使用的相关接口，更多接口及使用方式请见[延迟任务调度回调](../harmonyos-references/js-apis-workschedulerextensionability.md)文档。

| 接口名 | 接口描述 |
| --- | --- |
| [onWorkStart(work: workScheduler.WorkInfo): void](../harmonyos-references/js-apis-workschedulerextensionability.md#onworkstart) | 延迟调度任务开始的回调。 |
| [onWorkStop(work: workScheduler.WorkInfo): void](../harmonyos-references/js-apis-workschedulerextensionability.md#onworkstop) | 延迟调度任务结束的回调。 |

## 开发步骤

延迟任务调度开发步骤分为两步：实现延迟任务调度扩展能力、实现延迟任务调度。

1. **延迟任务调度扩展能力**：实现WorkSchedulerExtensionAbility开始和结束的回调接口。
2. **延迟任务调度**：调用延迟任务接口，实现延迟任务申请、取消等功能。

### 实现延迟任务回调扩展能力

1. 新建工程目录。

   在工程entry Module对应的ets目录(./entry/src/main/ets)下，新建目录及ArkTS文件，例如新建一个目录并命名为WorkSchedulerExtension。在WorkSchedulerExtension目录下，新建一个ArkTS文件并命名为WorkSchedulerExtension.ets，用以实现延迟任务回调接口。
2. 导入模块。

   ```
   1. import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';
   ```
3. 实现WorkSchedulerExtension生命周期接口。

   ```
   1. export default class WorkSchedulerAbility extends WorkSchedulerExtensionAbility {
   2. // 延迟任务开始回调
   3. onWorkStart(workInfo: workScheduler.WorkInfo) {
   4. console.info(`onWorkStart, workInfo = ${JSON.stringify(workInfo)}`);
   5. // 打印 parameters中的参数，如：参数key1
   6. console.info(`work info parameters: ${JSON.parse(workInfo.parameters?.toString()).key1}`);
   7. }

   9. // 延迟任务结束回调。当延迟任务2分钟超时或应用调用stopWork接口取消任务时，触发该回调。
   10. onWorkStop(workInfo: workScheduler.WorkInfo) {
   11. console.info(`onWorkStop, workInfo is ${JSON.stringify(workInfo)}`);
   12. }
   13. }
   ```

   [WorkSchedulerAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/WorkScheduler/entry/src/main/ets/WorkSchedulerAbility/WorkSchedulerAbility.ets#L28-L71)
4. 在[module.json5配置文件](module-configuration-file.md)中注册WorkSchedulerExtensionAbility，并设置如下标签：

   * type标签设置为“workScheduler”。
   * srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. "extensionAbilities": [
   4. {
   5. "name": "MyWorkSchedulerExtensionAbility",
   6. "srcEntry": "./ets/WorkSchedulerExtension/WorkSchedulerExtension.ets",
   7. "type": "workScheduler"
   8. }
   9. ]
   10. }
   11. }
   ```

### 实现延迟任务调度

1. 导入模块。

   ```
   1. import { workScheduler } from '@kit.BackgroundTasksKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 申请延迟任务。

   ```
   1. let workInfo: workScheduler.WorkInfo = {
   2. workId: 1,
   3. networkType: workScheduler.NetworkType.NETWORK_TYPE_ANY,
   4. bundleName: 'ohos.samples.workschedulerextensionability',
   5. abilityName: 'WorkSchedulerAbility',
   6. // ...
   7. }

   9. try {
   10. workScheduler.startWork(workInfo);
   11. console.info(`startWork success`);
   12. }
   13. catch (error) {
   14. console.error(`startWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   15. }
   ```

   [WorkSchedulerSystem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/WorkScheduler/entry/src/main/ets/feature/WorkSchedulerSystem.ets#L124-L149)
3. 取消延迟任务。

   ```
   1. // 创建workinfo
   2. let workInfo: workScheduler.WorkInfo = {
   3. workId: 1,
   4. networkType: workScheduler.NetworkType.NETWORK_TYPE_WIFI,
   5. bundleName: 'ohos.samples.workschedulerextensionability',
   6. abilityName: 'WorkSchedulerAbility',
   7. }

   9. try {
   10. workScheduler.stopWork(workInfo);
   11. console.info(`stopWork success`);
   12. } catch (error) {
   13. console.error(`stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   14. }
   ```

   [WorkSchedulerSystem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/WorkScheduler/entry/src/main/ets/feature/WorkSchedulerSystem.ets#L125-L160)

### 延迟任务调度功能验证

确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下[hidumper命令](hidumper.md)手动触发延迟任务执行回调。

```
1. $ hidumper -s 1904 -a '-t com.example.application MyWorkSchedulerExtensionAbility'

3. -------------------------------[ability]-------------------------------

6. ----------------------------------WorkSchedule----------------------------------
```
