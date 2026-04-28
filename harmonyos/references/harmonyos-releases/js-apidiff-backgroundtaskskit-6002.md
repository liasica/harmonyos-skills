---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-backgroundtaskskit-6002
title: Background Tasks Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Background Tasks Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:71658ca3ecd29d30c9fa12a4522a3e062a88119dc746fea760a4c4e7ab645a0f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：export enum PowerSaveMode  差异内容：export enum PowerSaveMode | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：PowerSaveMode；  API声明：EFFICIENCY\_MODE = 1  差异内容：EFFICIENCY\_MODE = 1 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：PowerSaveMode；  API声明：DEFAULT\_MODE = 2  差异内容：DEFAULT\_MODE = 2 | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>;  差异内容：function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
| 新增API | NA | 类名：backgroundProcessManager；  API声明：function isPowerSaveMode(pid: number): Promise<boolean>;  差异内容：function isPowerSaveMode(pid: number): Promise<boolean>; | api/@ohos.resourceschedule.backgroundProcessManager.d.ts |
