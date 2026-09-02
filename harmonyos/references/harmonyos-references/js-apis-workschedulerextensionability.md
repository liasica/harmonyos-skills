---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensionability
title: "@ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)"
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > ArkTS API > @ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2715c1d31ee246462edfdc450ab8a669c4252f7ad40b9b2e8cd6fa398c1d9d61
---

本模块提供延迟任务回调能力。开发者可重写模块接口，在延迟任务触发时，系统可通过本模块接口回调应用，在回调里处理任务逻辑。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';
```

## 约束限制

为保障系统安全性和稳定性，防止WorkSchedulerExtensionAbility滥用系统资源，系统对其能力进行管控，不支持以下模块的引用：

[@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)

[@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)

[@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md)

[@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md)

[@ohos.multimedia.media (媒体服务)](arkts-apis-media.md)

## WorkSchedulerExtensionContext10+

type WorkSchedulerExtensionContext = \_WorkSchedulerExtensionContext

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 类型 | 说明 |
| --- | --- |
| [\_WorkSchedulerExtensionContext](js-apis-workschedulerextensioncontext.md) | WorkSchedulerExtension的上下文环境。 |

## WorkSchedulerExtensionAbility

延迟任务回调，当满足调度条件或调度结束时，系统会回调应用WorkSchedulerExtensionAbility中[onWorkStart()](js-apis-workschedulerextensionability.md#onworkstart)或[onWorkStop()](js-apis-workschedulerextensionability.md#onworkstop)的方法。

### 属性

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context10+ | [WorkSchedulerExtensionContext](js-apis-workschedulerextensioncontext.md) | 否 | 否 | WorkSchedulerExtension的上下文环境，继承自ExtensionContext。 |

### onWorkStart

onWorkStart(work: workScheduler.WorkInfo): void

开始延迟任务调度回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [workScheduler.WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 要添加到执行队列的任务。 |

**示例：**

```ts
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStart, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```

### onWorkStop

onWorkStop(work: workScheduler.WorkInfo): void

结束延迟任务调度回调。当延迟任务2分钟超时或应用调用[stopWork](js-apis-resourceschedule-workscheduler.md#workschedulerstopwork)接口取消任务时，触发该回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work | [workScheduler.WorkInfo](js-apis-resourceschedule-workscheduler.md#workinfo) | 是 | 执行队列中要结束回调的任务。 |

**示例：**

```ts
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStop(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStop, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```
