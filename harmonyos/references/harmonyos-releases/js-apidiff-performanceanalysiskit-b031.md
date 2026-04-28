---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-performanceanalysiskit-b031
title: Performance Analysis Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Performance Analysis Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a7bc9ae7b7c30d4c3b576612145ab8c8c7dcf90f923e8e1106f9bc76b59dc812
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MemoryLimit；  API声明：vmTotalHeapSize: bigint;  差异内容：vmTotalHeapSize: bigint; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：type GcStats = Record<string, number>;  差异内容：type GcStats = Record<string, number>; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getVMRuntimeStats(): GcStats;  差异内容：function getVMRuntimeStats(): GcStats; | api/@ohos.hidebug.d.ts |
| 新增API | NA | 类名：hidebug；  API声明：function getVMRuntimeStat(item: string): number;  差异内容：function getVMRuntimeStat(item: string): number; | api/@ohos.hidebug.d.ts |
