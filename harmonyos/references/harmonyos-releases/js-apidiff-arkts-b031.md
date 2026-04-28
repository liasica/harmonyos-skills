---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b031
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:135df3cef6c54ba19ac311c8dc609dee3b2fb53131fdef48028759e6fa94ee22
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：Writable；  API声明：write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean;  差异内容：10200035,10200036,10200037,401 | 类名：Writable；  API声明：write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean;  差异内容：401 | api/@ohos.util.stream.d.ts |
| 错误码变更 | 类名：Writable；  API声明：end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable;  差异内容：10200035,401 | 类名：Writable；  API声明：end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable;  差异内容：401 | api/@ohos.util.stream.d.ts |
| 错误码变更 | 类名：Readable；  API声明：read(size?: number): string | null;  差异内容：10200038,401 | 类名：Readable；  API声明：read(size?: number): string | null;  差异内容：401 | api/@ohos.util.stream.d.ts |
| 错误码变更 | 类名：Duplex；  API声明：write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean;  差异内容：10200036,10200037,10200039,401 | 类名：Duplex；  API声明：write(chunk?: string | Uint8Array, encoding?: string, callback?: Function): boolean;  差异内容：401 | api/@ohos.util.stream.d.ts |
| 错误码变更 | 类名：Duplex；  API声明：end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable;  差异内容：10200039,401 | 类名：Duplex；  API声明：end(chunk?: string | Uint8Array, encoding?: string, callback?: Function): Writable;  差异内容：401 | api/@ohos.util.stream.d.ts |
| 错误码变更 | 类名：Task；  API声明：addDependency(...tasks: Task[]): void;  差异内容：10200026,401 | 类名：Task；  API声明：addDependency(...tasks: Task[]): void;  差异内容：10200026,10200052,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：Task；  API声明：removeDependency(...tasks: Task[]): void;  差异内容：10200027,401 | 类名：Task；  API声明：removeDependency(...tasks: Task[]): void;  差异内容：10200027,10200052,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：TaskGroup；  API声明：addTask(task: Task): void;  差异内容：10200014,401 | 类名：TaskGroup；  API声明：addTask(task: Task): void;  差异内容：10200014,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：10200003,10200006,10200025,401 | 类名：SequenceRunner；  API声明：execute(task: Task): Promise<Object>;  差异内容：10200003,10200006,10200025,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：10200003,10200006,10200014,401 | 类名：taskpool；  API声明：function execute(task: Task, priority?: Priority): Promise<Object>;  差异内容：10200003,10200006,10200014,10200051,401 | api/@ohos.taskpool.d.ts |
| 错误码变更 | 类名：taskpool；  API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>;  差异内容：10200028,401 | 类名：taskpool；  API声明：function executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>;  差异内容：10200028,10200051,401 | api/@ohos.taskpool.d.ts |
| 函数变更 | 类名：Writable；  API声明：off(event: string, callback?: Callback<emitter.EventData>): void;  差异内容：callback?: Callback<emitter.EventData> | 类名：Writable；  API声明：off(event: string): void;  差异内容：NA | api/@ohos.util.stream.d.ts |
| 函数变更 | 类名：Readable；  API声明：off(event: string, callback?: Callback<emitter.EventData>): void;  差异内容：callback?: Callback<emitter.EventData> | 类名：Readable；  API声明：off(event: string): void;  差异内容：NA | api/@ohos.util.stream.d.ts |
| 函数变更 | 类名：Int8Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Int8Array>): Int8Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Int8Array> | 类名：Int8Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Int8Array>): Int8Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Int8Array> | arkts/@arkts.collections.d.ets |
| 函数变更 | 类名：Uint8Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Uint8Array>): Uint8Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Uint8Array> | 类名：Uint8Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Uint8Array>): Uint8Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Uint8Array> | arkts/@arkts.collections.d.ets |
| 函数变更 | 类名：Int16Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Int16Array>): Int16Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Int16Array> | 类名：Int16Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Int16Array>): Int16Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Int16Array> | arkts/@arkts.collections.d.ets |
| 函数变更 | 类名：Uint16Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Uint16Array>): Uint16Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Uint16Array> | 类名：Uint16Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Uint16Array>): Uint16Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Uint16Array> | arkts/@arkts.collections.d.ets |
| 函数变更 | 类名：Int32Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Int32Array>): Int32Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Int32Array> | 类名：Int32Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Int32Array>): Int32Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Int32Array> | arkts/@arkts.collections.d.ets |
| 函数变更 | 类名：Uint32Array；  API声明：map(callbackFn: TypedArrayForEachCallback<number, Uint32Array>): Uint32Array;  差异内容：callbackFn: TypedArrayForEachCallback<number, Uint32Array> | 类名：Uint32Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Uint32Array>): Uint32Array;  差异内容：callbackFn: TypedArrayMapCallback<number, Uint32Array> | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Priority；  API声明：IDLE = 3  差异内容：IDLE = 3 | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：Task；  API声明：isDone(): boolean;  差异内容：isDone(): boolean; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：function executePeriodically(period: number, task: Task, priority?: Priority): void;  差异内容：function executePeriodically(period: number, task: Task, priority?: Priority): void; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：stream；  API声明： interface ReadableOptions  差异内容： interface ReadableOptions | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：ReadableOptions；  API声明：encoding?: string;  差异内容：encoding?: string; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：collections；  API声明：type TypedArrayMapCallback<ElementType, ArrayType> =  (value: ElementType, index: number, array: ArrayType) => ElementType;  差异内容：type TypedArrayMapCallback<ElementType, ArrayType> =  (value: ElementType, index: number, array: ArrayType) => ElementType; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：splice(start: number): Array<T>;  差异内容：splice(start: number): Array<T>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：splice(start: number, deleteCount: number, ...items: T[]): Array<T>;  差异内容：splice(start: number, deleteCount: number, ...items: T[]): Array<T>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：collections；  API声明： class Uint8ClampedArray  差异内容： class Uint8ClampedArray | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：static readonly BYTES\_PER\_ELEMENT: number;  差异内容：static readonly BYTES\_PER\_ELEMENT: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：readonly buffer: ArrayBuffer;  差异内容：readonly buffer: ArrayBuffer; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：readonly byteLength: number;  差异内容：readonly byteLength: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：readonly byteOffset: number;  差异内容：readonly byteOffset: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：readonly length: number;  差异内容：readonly length: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：static from(arrayLike: ArrayLike<number>): Uint8ClampedArray;  差异内容：static from(arrayLike: ArrayLike<number>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray;  差异内容：static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray;  差异内容：static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：copyWithin(target: number, start: number, end?: number): Uint8ClampedArray;  差异内容：copyWithin(target: number, start: number, end?: number): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean;  差异内容：every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：fill(value: number, start?: number, end?: number): Uint8ClampedArray;  差异内容：fill(value: number, start?: number, end?: number): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray;  差异内容：filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined;  差异内容：find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number;  差异内容：findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void;  差异内容：forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：indexOf(searchElement: number, fromIndex?: number): number;  差异内容：indexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：join(separator?: string): string;  差异内容：join(separator?: string): string; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray;  差异内容：map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number;  差异内容：reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U;  差异内容：reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：reverse(): Uint8ClampedArray;  差异内容：reverse(): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：set(array: ArrayLike<number>, offset?: number): void;  差异内容：set(array: ArrayLike<number>, offset?: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：slice(start?: number, end?: number): Uint8ClampedArray;  差异内容：slice(start?: number, end?: number): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean;  差异内容：some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray;  差异内容：sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：subarray(begin?: number, end?: number): Uint8ClampedArray;  差异内容：subarray(begin?: number, end?: number): Uint8ClampedArray; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：at(index: number): number | undefined;  差异内容：at(index: number): number | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：entries(): IterableIterator<[number, number]>;  差异内容：entries(): IterableIterator<[number, number]>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：keys(): IterableIterator<number>;  差异内容：keys(): IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：values(): IterableIterator<number>;  差异内容：values(): IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：includes(searchElement: number, fromIndex?: number): boolean;  差异内容：includes(searchElement: number, fromIndex?: number): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：collections；  API声明： class BitVector  差异内容： class BitVector | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：readonly length: number;  差异内容：readonly length: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：push(element: number): boolean;  差异内容：push(element: number): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：pop(): number;  差异内容：pop(): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：has(element: number, fromIndex: number, toIndex: number): boolean;  差异内容：has(element: number, fromIndex: number, toIndex: number): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：setBitsByRange(element: number, fromIndex: number, toIndex: number): void;  差异内容：setBitsByRange(element: number, fromIndex: number, toIndex: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：setAllBits(element: number): void;  差异内容：setAllBits(element: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：getBitsByRange(fromIndex: number, toIndex: number): BitVector;  差异内容：getBitsByRange(fromIndex: number, toIndex: number): BitVector; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：resize(size: number): void;  差异内容：resize(size: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：getBitCountByRange(element: number, fromIndex: number, toIndex: number): number;  差异内容：getBitCountByRange(element: number, fromIndex: number, toIndex: number): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：getIndexOf(element: number, fromIndex: number, toIndex: number): number;  差异内容：getIndexOf(element: number, fromIndex: number, toIndex: number): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：getLastIndexOf(element: number, fromIndex: number, toIndex: number): number;  差异内容：getLastIndexOf(element: number, fromIndex: number, toIndex: number): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：flipBitByIndex(index: number): void;  差异内容：flipBitByIndex(index: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：flipBitsByRange(fromIndex: number, toIndex: number): void;  差异内容：flipBitsByRange(fromIndex: number, toIndex: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：values(): IterableIterator<number>;  差异内容：values(): IterableIterator<number>; | arkts/@arkts.collections.d.ets |
