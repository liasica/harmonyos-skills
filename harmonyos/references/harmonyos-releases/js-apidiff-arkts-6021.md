---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6021
title: ArkTS
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:11ee783f4cda02482e83126d24e02890f1f577008eb43b99c71fc95176b0eed6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：taskpool；  API声明：function getTask(taskId: number, taskName?: string): Task | undefined;  差异内容：function getTask(taskId: number, taskName?: string): Task | undefined; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：util；  API声明：interface AutoFinalizer  差异内容：interface AutoFinalizer | api/@ohos.util.d.ts |
| 新增API | NA | 类名：AutoFinalizer；  API声明：onFinalization(heldValue: T): void;  差异内容：onFinalization(heldValue: T): void; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util；  API声明：class AutoFinalizerCleaner  差异内容：class AutoFinalizerCleaner | api/@ohos.util.d.ts |
| 新增API | NA | 类名：AutoFinalizerCleaner；  API声明：static register<T>(obj: AutoFinalizer<T>, heldValue: T): void;  差异内容：static register<T>(obj: AutoFinalizer<T>, heldValue: T): void; | api/@ohos.util.d.ts |
