---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b105
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9678cd98e634b04d5917af215286aacd109903a34469b7fb39c3f8744a7fe1b8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：taskpool；  API声明：function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>;  差异内容：function execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void;  差异内容：function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明： class GenericsTask  差异内容： class GenericsTask | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：ParseReturnType；  API声明：MAP = 1  差异内容：MAP = 1 | arkts/@arkts.utils.d.ets |
| 删除API | 类名：worker；  API声明： class RestrictedWorker  差异内容： class RestrictedWorker | NA | api/@ohos.worker.d.ts |
