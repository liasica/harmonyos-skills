---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-5051
title: Background Tasks Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5c4b7ea6c4a916c397c41e0a91fc0c59e7c05be62b14ca16f6e179ff7d5de98c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace backgroundProcessManager  差异内容：declare namespace backgroundProcessManager | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：export enum ProcessPriority  差异内容：export enum ProcessPriority | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ProcessPriority；  API声明：PROCESS\_BACKGROUND = 1  差异内容：PROCESS\_BACKGROUND = 1 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：ProcessPriority；  API声明：PROCESS\_INACTIVE = 2  差异内容：PROCESS\_INACTIVE = 2 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：function setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>;  差异内容：function setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：function resetProcessPriority(pid: number): Promise<void>;  差异内容：function resetProcessPriority(pid: number): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.resourceschedule.backgroundProcessManager.d.ts  差异内容：BackgroundTasksKit | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
