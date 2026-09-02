---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-7002
title: ArkTS
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:84c3bb5fb58229777829d853ef6516279348b189d135d790e2741ba7346f46b5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：ArkTSVM；  API声明：static setMultithreadingDetectionEnabled(enabled: boolean): void;  差异内容：NA | 类名：ArkTSVM；  API声明：static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions): void;  差异内容：options?: MultithreadingDetectionOptions | api/@ohos.util.d.ts |
| 新增API | NA | 类名：util；  API声明：interface MultithreadingDetectionOptions  差异内容：interface MultithreadingDetectionOptions | api/@ohos.util.d.ts |
| 新增API | NA | 类名：MultithreadingDetectionOptions；  API声明：abort?: boolean;  差异内容：abort?: boolean; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：MultithreadingDetectionOptions；  API声明：frequency?: number;  差异内容：frequency?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：MultithreadingDetectionOptions；  API声明：interval?: number;  差异内容：interval?: number; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM；  API声明：static setTrackGlobalRef(enable: boolean): void;  差异内容：static setTrackGlobalRef(enable: boolean): void; | api/@ohos.util.d.ts |
| 修改导出符号 | 类名：global；  API声明：export enum Priority  差异内容：export enum Priority | 类名：global；  API声明：export { ArrayList, convertxml, DedicatedWorkerGlobalScope, Deque, ErrorEvent, Event, EventListener, EventTarget, HashMap, HashSet, LightWeightMap, LightWeightSet, LinkedList, List, MessageEvent, MessageEvents, PlainArray, PostMessageOptions, Queue, Stack, ThreadWorkerGlobalScope, TreeMap, TreeSet, Vector, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, buffer, process, taskpool, uri, url, util, worker, xml, JSON, lang, Retention, RetentionPolicy, ArkTSUtils, collections, stream, Decimal, fastbuffer, ArrayListComparatorFn, ListComparatorFn, Priority };  差异内容：export { ArrayList, convertxml, DedicatedWorkerGlobalScope, Deque, ErrorEvent, Event, EventListener, EventTarget, HashMap, HashSet, LightWeightMap, LightWeightSet, LinkedList, List, MessageEvent, MessageEvents, PlainArray, PostMessageOptions, Queue, Stack, ThreadWorkerGlobalScope, TreeMap, TreeSet, Vector, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, buffer, process, taskpool, uri, url, util, worker, xml, JSON, lang, Retention, RetentionPolicy, ArkTSUtils, collections, stream, Decimal, fastbuffer, ArrayListComparatorFn, ListComparatorFn, Priority }; | kits/@kit.ArkTS.d.ts |
