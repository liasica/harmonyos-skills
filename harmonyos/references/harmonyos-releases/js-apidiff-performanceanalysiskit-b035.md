---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-b035
title: Performance Analysis Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:86c25d5060cc54f314ea7b215dbfd562af6f98817455205b2f6fb6e1c18f7eb3
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace jsLeakWatcher  差异内容： declare namespace jsLeakWatcher | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：function enable(isEnable: boolean): void;  差异内容：function enable(isEnable: boolean): void; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：function watch(obj: object, msg: string): void;  差异内容：function watch(obj: object, msg: string): void; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：function check(): string;  差异内容：function check(): string; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
| 新增API | NA | 类名：jsLeakWatcher；  API声明：function dump(filePath: string): Array<string>;  差异内容：function dump(filePath: string): Array<string>; | api/@ohos.hiviewdfx.jsLeakWatcher.d.ts |
