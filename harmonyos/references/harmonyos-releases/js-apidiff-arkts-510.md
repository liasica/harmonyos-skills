---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-510
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:504e4ae0fccfca05a57d9bbcc510b39de98b69ff4063f57103e68f3a3aff91df
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Task；  API声明：addDependency(...tasks: Task[]): void;  差异内容：NA | 类名：Task；  API声明：addDependency(...tasks: Task[]): void;  差异内容：10200056 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：Task；  API声明：removeDependency(...tasks: Task[]): void;  差异内容：NA | 类名：Task；  API声明：removeDependency(...tasks: Task[]): void;  差异内容：10200056 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：TaskGroup；  API声明：addTask(task: Task): void;  差异内容：NA | 类名：TaskGroup；  API声明：addTask(task: Task): void;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：NA | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：NA | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：NA | 类名：taskpool；  API声明：function execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>;  差异内容：NA | 类名：taskpool；  API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：NA | 类名：taskpool；  API声明：function executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void;  差异内容：NA | 类名：taskpool；  API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void;  差异内容：NA | 类名：taskpool；  API声明：function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void;  差异内容：10200057 | api/@ohos.taskpool.d.ts |
| 新增错误码 | 类名：taskpool；  API声明：function cancel(task: Task): void;  差异内容：NA | 类名：taskpool；  API声明：function cancel(task: Task): void;  差异内容：10200055 | api/@ohos.taskpool.d.ts |
| 函数变更 | 类名：ASON；  API声明：function stringify(value: ISendable | null | undefined): string;  差异内容：value: ISendable | null | undefined | 类名：ASON；  API声明：function stringify(value: Object | null | undefined): string;  差异内容：value: Object | null | undefined | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：taskpool；  API声明：function cancel(taskId: number): void;  差异内容：function cancel(taskId: number): void; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：export class AsyncRunner  差异内容：export class AsyncRunner | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：AsyncRunner；  API声明：execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：execute(task: Task, priority?: Priority): Promise<Object>; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：collections；  API声明：type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType;  差异内容：type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：collections；  API声明：type ArrayPredicateFn<ElementType, ArrayType> =  (value: ElementType, index: number, array: ArrayType) => boolean;  差异内容：type ArrayPredicateFn<ElementType, ArrayType> =  (value: ElementType, index: number, array: ArrayType) => boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：collections；  API声明：type ArrayReduceCallback<AccType, ElementType, ArrayType> =  (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType;  差异内容：type ArrayReduceCallback<AccType, ElementType, ArrayType> =  (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：locks；  API声明：class ConditionVariable  差异内容：class ConditionVariable | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ConditionVariable；  API声明：static request(name: string): ConditionVariable;  差异内容：static request(name: string): ConditionVariable; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ConditionVariable；  API声明：wait(): Promise<void>;  差异内容：wait(): Promise<void>; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ConditionVariable；  API声明：waitFor(timeout: number): Promise<void>;  差异内容：waitFor(timeout: number): Promise<void>; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ConditionVariable；  API声明：notifyAll(): void;  差异内容：notifyAll(): void; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ConditionVariable；  API声明：notifyOne(): void;  差异内容：notifyOne(): void; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：utils；  API声明：class SendableLruCache  差异内容：class SendableLruCache | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：readonly length: number;  差异内容：readonly length: number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：updateCapacity(newCapacity: number): void;  差异内容：updateCapacity(newCapacity: number): void; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：get(key: K): V | undefined;  差异内容：get(key: K): V | undefined; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：put(key: K, value: V): V;  差异内容：put(key: K, value: V): V; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：remove(key: K): V | undefined;  差异内容：remove(key: K): V | undefined; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：contains(key: K): boolean;  差异内容：contains(key: K): boolean; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getCreateCount(): number;  差异内容：getCreateCount(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getMissCount(): number;  差异内容：getMissCount(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getRemoveCount(): number;  差异内容：getRemoveCount(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getMatchCount(): number;  差异内容：getMatchCount(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getPutCount(): number;  差异内容：getPutCount(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：getCapacity(): number;  差异内容：getCapacity(): number; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：clear(): void;  差异内容：clear(): void; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：isEmpty(): boolean;  差异内容：isEmpty(): boolean; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：values(): V[];  差异内容：values(): V[]; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：keys(): K[];  差异内容：keys(): K[]; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：SendableLruCache；  API声明：entries(): IterableIterator<[K, V]>;  差异内容：entries(): IterableIterator<[K, V]>; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：global；  API声明：export enum ThreadWorkerPriority  差异内容：export enum ThreadWorkerPriority | api/@ohos.worker.d.ts |
| 新增API | NA | 类名：ThreadWorkerPriority；  API声明：HIGH = 0  差异内容：HIGH = 0 | api/@ohos.worker.d.ts |
| 新增API | NA | 类名：ThreadWorkerPriority；  API声明：MEDIUM = 1  差异内容：MEDIUM = 1 | api/@ohos.worker.d.ts |
| 新增API | NA | 类名：ThreadWorkerPriority；  API声明：LOW = 2  差异内容：LOW = 2 | api/@ohos.worker.d.ts |
| 新增API | NA | 类名：ThreadWorkerPriority；  API声明：IDLE = 3  差异内容：IDLE = 3 | api/@ohos.worker.d.ts |
| 新增API | NA | 类名：global；  API声明：type ErrorCallback = (err: ErrorEvent) => void;  差异内容：type ErrorCallback = (err: ErrorEvent) => void; | api/@ohos.worker.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：ThreadWorker；  API声明：onAllErrors?: ErrorCallback;  差异内容：onAllErrors?: ErrorCallback; | api/@ohos.worker.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Task；  API声明：taskId: number;  差异内容：taskId: number; | api/@ohos.taskpool.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：static isArray(value: Object | undefined | null): boolean;  差异内容：static isArray(value: Object | undefined | null): boolean; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：static of<T>(...items: T[]): Array<T>;  差异内容：static of<T>(...items: T[]): Array<T>; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：copyWithin(target: number, start: number, end?: number): Array<T>;  差异内容：copyWithin(target: number, start: number, end?: number): Array<T>; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：reverse(): Array<T>;  差异内容：reverse(): Array<T>; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：lastIndexOf(searchElement: T, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: T, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：every(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：every(predicate: ArrayPredicateFn<T, Array<T>>): boolean; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：some(predicate: ArrayPredicateFn<T, Array<T>>): boolean;  差异内容：some(predicate: ArrayPredicateFn<T, Array<T>>): boolean; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U;  差异内容：reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T;  差异内容：reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int8Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int8Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int8Array；  API声明：static of(...items: number[]): Int8Array;  差异内容：static of(...items: number[]): Int8Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8ClampedArray；  API声明：static of(...items: number[]): Uint8ClampedArray;  差异内容：static of(...items: number[]): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint8Array；  API声明：static of(...items: number[]): Uint8Array;  差异内容：static of(...items: number[]): Uint8Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int16Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int16Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int16Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int16Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int16Array；  API声明：static of(...items: number[]): Int16Array;  差异内容：static of(...items: number[]): Int16Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint16Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint16Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint16Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint16Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint16Array；  API声明：static of(...items: number[]): Uint16Array;  差异内容：static of(...items: number[]): Uint16Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int32Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int32Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Int32Array；  API声明：static of(...items: number[]): Int32Array;  差异内容：static of(...items: number[]): Int32Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint32Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint32Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Uint32Array；  API声明：static of(...items: number[]): Uint32Array;  差异内容：static of(...items: number[]): Uint32Array; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：lastIndexOf(searchElement: number, fromIndex?: number): number;  差异内容：lastIndexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Float32Array>, initialValue: U): U;  差异内容：reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Float32Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Float32Array>): number;  差异内容：reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Float32Array>): number; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：toString(): string;  差异内容：toString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：toLocaleString(): string;  差异内容：toLocaleString(): string; | arkts/@arkts.collections.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Float32Array；  API声明：static of(...items: number[]): Float32Array;  差异内容：static of(...items: number[]): Float32Array; | arkts/@arkts.collections.d.ets |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>;  差异内容：static from<T>(arrayLike: ArrayLike<T> | Iterable<T>, mapFn: ArrayFromMapFn<T, T>): Array<T>; | arkts/@arkts.collections.d.ets |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：global；  API声明：  差异内容：NA | 类名：Array；  API声明：static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>;  差异内容：static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T>; | arkts/@arkts.collections.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：WorkerOptions；  API声明：priority?: ThreadWorkerPriority;  差异内容：priority?: ThreadWorkerPriority; | api/@ohos.worker.d.ts |
