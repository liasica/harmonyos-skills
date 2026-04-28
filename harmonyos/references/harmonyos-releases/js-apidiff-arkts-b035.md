---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-b035
title: ArkTS
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:28+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:bc4d9356737ab229db051f78c32ef47dac302a37774dd6ec03816a0d8f113b7f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：json；  API声明：function parse(text: string, reviver?: Transformer): Object | null;  差异内容：NA | 类名：json；  API声明：function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null;  差异内容：options?: ParseOptions | api/@ohos.util.json.d.ts |
| 函数变更 | 类名：ASON；  API声明：function parse(text: string): ISendable | null;  差异内容：NA | 类名：ASON；  API声明：function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null;  差异内容：reviver?: Transformer, options?: ParseOptions | arkts/@arkts.utils.d.ets |
| 错误码变更 | 类名：util；  API声明：function parseUUID(uuid: string): Uint8Array;  差异内容：401 | 类名：util；  API声明：function parseUUID(uuid: string): Uint8Array;  差异内容：10200002,401 | api/@ohos.util.d.ts |
| 新增API | NA | 类名：json；  API声明： const enum BigIntMode  差异内容： const enum BigIntMode | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：BigIntMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：BigIntMode；  API声明：PARSE\_AS\_BIGINT = 1  差异内容：PARSE\_AS\_BIGINT = 1 | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：BigIntMode；  API声明：ALWAYS\_PARSE\_AS\_BIGINT = 2  差异内容：ALWAYS\_PARSE\_AS\_BIGINT = 2 | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：json；  API声明： interface ParseOptions  差异内容： interface ParseOptions | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：ParseOptions；  API声明：bigIntMode: BigIntMode;  差异内容：bigIntMode: BigIntMode; | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：ASON；  API声明：type Transformer = (this: ISendable, key: string,  value: ISendable | undefined | null) => ISendable | undefined | null  差异内容：type Transformer = (this: ISendable, key: string,  value: ISendable | undefined | null) => ISendable | undefined | null | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ASON；  API声明： const enum BigIntMode  差异内容： const enum BigIntMode | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：BigIntMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：BigIntMode；  API声明：PARSE\_AS\_BIGINT = 1  差异内容：PARSE\_AS\_BIGINT = 1 | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：BigIntMode；  API声明：ALWAYS\_PARSE\_AS\_BIGINT = 2  差异内容：ALWAYS\_PARSE\_AS\_BIGINT = 2 | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ASON；  API声明： const enum ParseReturnType  差异内容： const enum ParseReturnType | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ParseReturnType；  API声明：OBJECT = 0  差异内容：OBJECT = 0 | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ASON；  API声明： interface ParseOptions  差异内容： interface ParseOptions | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ParseOptions；  API声明：bigIntMode: BigIntMode;  差异内容：bigIntMode: BigIntMode; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：ParseOptions；  API声明：parseReturnType: ParseReturnType;  差异内容：parseReturnType: ParseReturnType; | arkts/@arkts.utils.d.ets |
| 新增API | NA | 类名：Array；  API声明：*Symbol.iterator*: IterableIterator<T>;  差异内容：*Symbol.iterator*: IterableIterator<T>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：*Symbol.iterator*: IterableIterator<[K, V]>  差异内容：*Symbol.iterator*: IterableIterator<[K, V]> | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Set；  API声明：*Symbol.iterator*: IterableIterator<T>;  差异内容：*Symbol.iterator*: IterableIterator<T>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Int8Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8ClampedArray；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint8Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Int16Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint16Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Int32Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Uint32Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：static from<T>(iterable: Iterable<T>): Array<T>;  差异内容：static from<T>(iterable: Iterable<T>): Array<T>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：collections；  API声明： class Float32Array  差异内容： class Float32Array | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：static readonly BYTES\_PER\_ELEMENT: number;  差异内容：static readonly BYTES\_PER\_ELEMENT: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：readonly buffer: ArrayBuffer;  差异内容：readonly buffer: ArrayBuffer; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：readonly byteLength: number;  差异内容：readonly byteLength: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：readonly byteOffset: number;  差异内容：readonly byteOffset: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：readonly length: number;  差异内容：readonly length: number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：static from(arrayLike: ArrayLike<number>): Float32Array;  差异内容：static from(arrayLike: ArrayLike<number>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Float32Array;  差异内容：static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Float32Array;  差异内容：static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：copyWithin(target: number, start: number, end?: number): Float32Array;  差异内容：copyWithin(target: number, start: number, end?: number): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：every(predicate: TypedArrayPredicateFn<number, Float32Array>): boolean;  差异内容：every(predicate: TypedArrayPredicateFn<number, Float32Array>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：fill(value: number, start?: number, end?: number): Float32Array;  差异内容：fill(value: number, start?: number, end?: number): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：filter(predicate: TypedArrayPredicateFn<number, Float32Array>): Float32Array;  差异内容：filter(predicate: TypedArrayPredicateFn<number, Float32Array>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：find(predicate: TypedArrayPredicateFn<number, Float32Array>): number | undefined;  差异内容：find(predicate: TypedArrayPredicateFn<number, Float32Array>): number | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：findIndex(predicate: TypedArrayPredicateFn<number, Float32Array>): number;  差异内容：findIndex(predicate: TypedArrayPredicateFn<number, Float32Array>): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：forEach(callbackFn: TypedArrayForEachCallback<number, Float32Array>): void;  差异内容：forEach(callbackFn: TypedArrayForEachCallback<number, Float32Array>): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：indexOf(searchElement: number, fromIndex?: number): number;  差异内容：indexOf(searchElement: number, fromIndex?: number): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：join(separator?: string): string;  差异内容：join(separator?: string): string; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：map(callbackFn: TypedArrayMapCallback<number, Float32Array>): Float32Array;  差异内容：map(callbackFn: TypedArrayMapCallback<number, Float32Array>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：reduce(callbackFn: TypedArrayReduceCallback<number, number, Float32Array>): number;  差异内容：reduce(callbackFn: TypedArrayReduceCallback<number, number, Float32Array>): number; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Float32Array>, initialValue: U): U;  差异内容：reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Float32Array>, initialValue: U): U; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：reverse(): Float32Array;  差异内容：reverse(): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：set(array: ArrayLike<number>, offset?: number): void;  差异内容：set(array: ArrayLike<number>, offset?: number): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：slice(start?: number, end?: number): Float32Array;  差异内容：slice(start?: number, end?: number): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：some(predicate: TypedArrayPredicateFn<number, Float32Array>): boolean;  差异内容：some(predicate: TypedArrayPredicateFn<number, Float32Array>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：sort(compareFn?: TypedArrayCompareFn<number>): Float32Array;  差异内容：sort(compareFn?: TypedArrayCompareFn<number>): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：subarray(begin?: number, end?: number): Float32Array;  差异内容：subarray(begin?: number, end?: number): Float32Array; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：at(index: number): number | undefined;  差异内容：at(index: number): number | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：entries(): IterableIterator<[number, number]>;  差异内容：entries(): IterableIterator<[number, number]>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：keys(): IterableIterator<number>;  差异内容：keys(): IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：values(): IterableIterator<number>;  差异内容：values(): IterableIterator<number>; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Float32Array；  API声明：includes(searchElement: number, fromIndex?: number): boolean;  差异内容：includes(searchElement: number, fromIndex?: number): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：BitVector；  API声明：*Symbol.iterator*: IterableIterator<number>;  差异内容：*Symbol.iterator*: IterableIterator<number>; | arkts/@arkts.collections.d.ets |
