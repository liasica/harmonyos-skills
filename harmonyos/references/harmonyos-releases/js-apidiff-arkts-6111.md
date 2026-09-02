---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6111
title: ArkTS
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:4760f7ccbb1d3001e80f35f74cfcbd979e13afa89eff3e78d12b10e19ca98d77
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：taskpool；  API声明：function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>;  差异内容：10200006,401 | 类名：taskpool；  API声明：function execute(group: TaskGroup, priority?: Priority): Promise<Object[]>;  差异内容：10200006,10200059 | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：interface Configs  差异内容：interface Configs | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：Configs；  API声明：priority?: Priority;  差异内容：priority?: Priority; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：Configs；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：ArkTSVM；  API声明：static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>;  差异内容：static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM；  API声明：static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean;  差异内容：static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM；  API声明：static offVMHeapMemoryPressure(): void;  差异内容：static offVMHeapMemoryPressure(): void; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util；  API声明：interface HeapMemoryThreshold  差异内容：interface HeapMemoryThreshold | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold；  API声明：localHeapThreshold?: number;  差异内容：localHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold；  API声明：sharedHeapThreshold?: number;  差异内容：sharedHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryThreshold；  API声明：processHeapThreshold?: number;  差异内容：processHeapThreshold?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util；  API声明：interface HeapMemoryInfo  差异内容：interface HeapMemoryInfo | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo；  API声明：threadId?: number;  差异内容：threadId?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo；  API声明：threadName?: string;  差异内容：threadName?: string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo；  API声明：heapType: string;  差异内容：heapType: string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：HeapMemoryInfo；  API声明：heapObjectSize: number;  差异内容：heapObjectSize: number; | api/@ohos.util.d.ts |
