---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-5111
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d3b591992554953f28f9b8d24b1918b0ae2b29d6f37c015d2f3ece5f9ab7aefd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：taskpool；  API声明：function cancel(task: Task): void;  差异内容：401 | 类名：taskpool；  API声明：function cancel(task: Task): void;  差异内容：NA | api/@ohos.taskpool.d.ts |
| 删除错误码 | 类名：taskpool；  API声明：function cancel(taskId: number): void;  差异内容：401 | 类名：taskpool；  API声明：function cancel(taskId: number): void;  差异内容：NA | api/@ohos.taskpool.d.ts |
| 删除错误码 | 类名：AsyncRunner；  API声明：execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：401 | 类名：AsyncRunner；  API声明：execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：NA | api/@ohos.taskpool.d.ts |
| 删除错误码 | 类名：Array；  API声明：lastIndexOf(searchElement: T, fromIndex?: number): number;  差异内容：401 | 类名：Array；  API声明：lastIndexOf(searchElement: T, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Array；  API声明：every(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：401 | 类名：Array；  API声明：every(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Array；  API声明：some(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：401 | 类名：Array；  API声明：some(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Int8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Int8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Uint8ClampedArray；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Uint8ClampedArray；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Uint8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Uint8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Int16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Int16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Uint16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Uint16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Int32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Int32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Uint32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Uint32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：Float32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：401 | 类名：Float32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：BitVector；  API声明：has(element: number, fromIndex: number, toIndex: number): boolean;  差异内容：401 | 类名：BitVector；  API声明：has(element: number, fromIndex: number, toIndex: number): boolean;  差异内容：NA | arkts/@arkts.collections.d.ets |
| 删除错误码 | 类名：ConditionVariable；  API声明：static request(name: string): ConditionVariable;  差异内容：401 | 类名：ConditionVariable；  API声明：static request(name: string): ConditionVariable;  差异内容：NA | arkts/@arkts.utils.d.ets |
| 删除错误码 | 类名：ConditionVariable；  API声明：waitFor(timeout: number): Promise<void>;  差异内容：401 | 类名：ConditionVariable；  API声明：waitFor(timeout: number): Promise<void>;  差异内容：NA | arkts/@arkts.utils.d.ets |
| 删除错误码 | 类名：SendableLruCache；  API声明：get(key: K): V | undefined;  差异内容：401 | 类名：SendableLruCache；  API声明：get(key: K): V | undefined;  差异内容：NA | arkts/@arkts.utils.d.ets |
| 删除错误码 | 类名：SendableLruCache；  API声明：put(key: K, value: V): V;  差异内容：401 | 类名：SendableLruCache；  API声明：put(key: K, value: V): V;  差异内容：NA | arkts/@arkts.utils.d.ets |
| 删除错误码 | 类名：SendableLruCache；  API声明：remove(key: K): V | undefined;  差异内容：401 | 类名：SendableLruCache；  API声明：remove(key: K): V | undefined;  差异内容：NA | arkts/@arkts.utils.d.ets |
| 删除错误码 | 类名：SendableLruCache；  API声明：contains(key: K): boolean;  差异内容：401 | 类名：SendableLruCache；  API声明：contains(key: K): boolean;  差异内容：NA | arkts/@arkts.utils.d.ets |
