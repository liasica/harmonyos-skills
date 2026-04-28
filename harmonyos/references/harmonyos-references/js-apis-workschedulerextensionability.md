---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensionability
title: @ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > @ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:17a313dd25806c4435baab979fbb1aebf2b724ea46f16a488c66d3735967de5b
---

本模块提供延迟任务回调能力。开发者可重写模块接口，在延迟任务触发时，系统可通过本模块接口回调应用，在回调里处理任务逻辑。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';
```

## WorkSchedulerExtensionContext10+

PhonePC/2in1TabletTVWearable

type WorkSchedulerExtensionContext = \_WorkSchedulerExtensionContext

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 类型 | 说明 |
| --- | --- |
| [\_WorkSchedulerExtensionContext](js-apis-workschedulerextensioncontext.md) | WorkSchedulerExtension的上下文环境。 |

## WorkSchedulerExtensionAbility

PhonePC/2in1TabletTVWearable

延迟任务回调，当满足调度条件或调度结束时，系统会回调应用WorkSchedulerExtensionAbility中[onWorkStart()](js-apis-workschedulerextensionability.md#onworkstart)或[onWorkStop()](js-apis-workschedulerextensionability.md#onworkstop)的方法。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context10+ | [WorkSchedulerExtensionContext](js-apis-workschedulerextensioncontext.md) | 否 | 否 | WorkSchedulerExtension的上下文环境，继承自ExtensionContext。 |

### onWorkStart

PhonePC/2in1TabletTVWearable

onWorkStart(work: workScheduler.WorkInfo): void

开始延迟任务调度回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [workScheduler.WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 要添加到执行队列的任务。 |

**示例：**

```
1. import { workScheduler } from '@kit.BackgroundTasksKit';
2. import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

4. export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
5. onWorkStart(workInfo: workScheduler.WorkInfo) {
6. console.info(`MyWorkSchedulerExtensionAbility onWorkStart, workId: ${workInfo.workId},
7. bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
8. }
9. }
```

### onWorkStop

PhonePC/2in1TabletTVWearable

onWorkStop(work: workScheduler.WorkInfo): void

结束延迟任务调度回调。当延迟任务2分钟超时或应用调用[stopWork](js-apis-resourceschedule-workscheduler.md#workschedulerstopwork)接口取消任务时，触发该回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [workScheduler.WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 执行队列中要结束回调的任务。 |

**示例：**

```
1. import { workScheduler } from '@kit.BackgroundTasksKit';
2. import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

4. export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
5. onWorkStop(workInfo: workScheduler.WorkInfo) {
6. console.info(`MyWorkSchedulerExtensionAbility onWorkStop, workId: ${workInfo.workId},
7. bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
8. }
9. }
```
