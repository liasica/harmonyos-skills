---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuptask
title: @ohos.app.appstartup.StartupTask (启动框架任务)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.StartupTask (启动框架任务)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d6bb245af2552b6afbe63d6297cee40b634ed5e438368e002f86fb69bb0af29a
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)任务的相关能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { StartupTask } from '@kit.AbilityKit';
```

## StartupTask

PhonePC/2in1TabletTVWearable

该类提供启动任务的相关能力，使用[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md#sendable装饰器)装饰。

**装饰器类型**：@Sendable

### onDependencyCompleted

PhonePC/2in1TabletTVWearable

onDependencyCompleted?(dependency: string, result: Object): void

当依赖的启动任务执行完成时该方法将会被调用。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dependency | string | 是 | 依赖的启动任务名称。 |
| result | Object | 是 | 依赖的启动任务[init](js-apis-app-appstartup-startuptask.md#init)返回的执行结果。 |

**示例：**

```
1. import { StartupTask, common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Sendable
5. export default class StartupTask_001 extends StartupTask {
6. constructor() {
7. super();
8. }

10. async init(context: common.AbilityStageContext) {
11. // ...
12. }

14. onDependencyCompleted(dependency: string, result: Object): void {
15. hilog.info(0x0000, 'testTag', 'StartupTask_001 onDependencyCompleted, dependency: %{public}s, result: %{public}s',
16. dependency, JSON.stringify(result));
17. // ...
18. }
19. }
```

### init

PhonePC/2in1TabletTVWearable

init(context: AbilityStageContext): Promise<Object | void>

当所有依赖的启动任务都执行完成后，该方法将会被调用。开发者可以在该回调中执行该启动任务的初始化操作。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [AbilityStageContext](js-apis-inner-application-abilitystagecontext.md) | 是 | [AbilityStage](js-apis-app-ability-abilitystage.md)的上下文环境 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object | void> | Promise对象，返回启动任务执行结果对象。 |

**示例：**

```
1. import { StartupTask, common } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Sendable
5. export default class StartupTask_001 extends StartupTask {
6. constructor() {
7. super();
8. }
9. async init(context: common.AbilityStageContext) {
10. hilog.info(0x0000, 'testTag', 'StartupTask_001 init.');
11. // ...

13. return "StartupTask_001";
14. }

16. onDependencyCompleted(dependency: string, result: Object): void {
17. // ...
18. }
19. }
```
