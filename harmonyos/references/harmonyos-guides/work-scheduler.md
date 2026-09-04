---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/work-scheduler
title: 延迟任务(ArkTS)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 延迟任务(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:056332023fa3884bae378f73ba2c2379fdb5ccf23e8f6d6166c4adebdae11164
---

## 概述

### 功能介绍

应用退至后台后，需要执行时效性要求不高的任务，例如有网络时不定期主动获取邮件等，可以使用延迟任务。当应用满足设定的触发条件（包括网络类型、充电类型、存储状态、电池状态、定时状态等）时，将任务添加到执行队列，系统会根据内存、功耗、设备温度、用户使用习惯等统一调度拉起应用，执行相应的延迟任务。

### 运行原理

**图1** 延迟任务实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/6e7UWa0kSXq2a0mBbE1fcQ/zh-cn_image_0000002712404312.png)

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
* 针对[WorkSchedulerExtensionAbility](../harmonyos-references/js-apis-workschedulerextensionability.md)接口调用限制，详细请参考API中的[约束限制](../harmonyos-references/js-apis-workschedulerextensionability.md#约束限制)。

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

   在工程entry Module对应的ets目录(./entry/src/main/ets)下，新建目录及ArkTS文件，例如新建一个目录并命名为WorkSchedulerAbility。在WorkSchedulerAbility目录下，新建一个ArkTS文件并命名为WorkSchedulerAbility.ets，用以实现延迟任务回调接口。
2. 导入模块，无需配置权限。

   ```typescript
   import {workScheduler, WorkSchedulerExtensionAbility} from '@kit.BackgroundTasksKit';
   ```
3. 实现WorkSchedulerExtension生命周期接口。

   ```typescript
   export default class WorkSchedulerAbility extends WorkSchedulerExtensionAbility {
     // 延迟任务开始回调
     onWorkStart(workInfo: workScheduler.WorkInfo) {
       // ...
       console.info(`onWorkStart, workInfo = ${JSON.stringify(workInfo)}`);
       // 打印 parameters中的参数，如：参数key1
       console.info(`work info parameters: ${JSON.parse(workInfo.parameters?.toString()).key1}`);
     }

     // 延迟任务结束回调。当延迟任务2分钟超时或应用调用stopWork接口取消任务时，触发该回调。
     onWorkStop(workInfo: workScheduler.WorkInfo) {
       console.info(`onWorkStop, workInfo is ${JSON.stringify(workInfo)}`);
     }
   }
   ```
4. 在[module.json5配置文件](module-configuration-file.md)中注册WorkSchedulerExtensionAbility，并设置如下标签：

   * type标签设置为“workScheduler”。
   * srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。

   ```json5
   {
     "module": {
       // ...
       "extensionAbilities": [
         {
           "name": "WorkSchedulerAbility",
           "srcEntry": "./ets/WorkSchedulerAbility/WorkSchedulerAbility.ets",
           "type": "workScheduler",
           // ...
         }
       ]
     }
   }
   ```

### 实现延迟任务调度

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { workScheduler } from '@kit.BackgroundTasksKit';
   ```
2. 申请延迟任务。

   ```typescript
   let workInfo: workScheduler.WorkInfo = {
     workId: 1,
     networkType: workScheduler.NetworkType.NETWORK_TYPE_ANY,
     bundleName: 'ohos.samples.workschedulerextensionability',
     abilityName: 'WorkSchedulerAbility',
     // ...
   }

   try {
     workScheduler.startWork(workInfo);
     console.info(`startWork success`);
   }
   catch (error) {
     console.error(`startWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   }
   ```
3. 取消延迟任务。

   ```typescript
   // 创建workInfo
   let workInfo: workScheduler.WorkInfo = {
     workId: 1,
     networkType: workScheduler.NetworkType.NETWORK_TYPE_ANY,
     bundleName: 'ohos.samples.workschedulerextensionability',
     abilityName: 'WorkSchedulerAbility',
     // ...
   }
   try {
     workScheduler.stopWork(workInfo);
     console.info(`stopWork success`);
   } catch (error) {
     console.error(`stopWork failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
   }
   ```

### 延迟任务调度功能验证

确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下[hidumper命令](hidumper.md)手动触发延迟任务执行回调。

**说明** 

* -s 1904：指向WorkScheduler系统服务发送命令（1904为该服务ID）。
* -a：携带附加参数，需用引号包裹。
* -t：指定目标应用包名和 ExtensionAbility 名称，示例中的 com.example.application 和 MyWorkSchedulerExtensionAbility 需替换为实际值。

```ts
$ hidumper -s 1904 -a '-t com.example.application MyWorkSchedulerExtensionAbility'

-------------------------------[ability]-------------------------------

----------------------------------WorkSchedule----------------------------------
```
