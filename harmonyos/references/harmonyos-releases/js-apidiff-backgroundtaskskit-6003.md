---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6003
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:72fc7eeaf734b0cb10e2492b7cbbd09559231463edb9f263bb7d2d67140f2ed4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明：export default class WorkSchedulerExtensionAbility  差异内容：stagemodelonly | 类名：global；  API声明：declare class WorkSchedulerExtensionAbility  差异内容：NA | api/@ohos.WorkSchedulerExtensionAbility.d.ts |
| 新增API | NA | 类名：backgroundTaskManager；  API声明：function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>;  差异内容：function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ContinuousTaskInfo；  API声明：suspendState: boolean;  差异内容：suspendState: boolean; | api/@ohos.resourceschedule.backgroundTaskManager.d.ts |
