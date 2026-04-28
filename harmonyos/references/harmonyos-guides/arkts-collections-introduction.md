---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-collections-introduction
title: 共享容器
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > 共享容器
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0539cd4b936024ae77c84d85f05572c65dfd9b22aba76784dce8ccaf7ad491b
---

## ArkTS容器集

ArkTS共享容器（[@arkts.collections (ArkTS容器集)](../harmonyos-references/arkts-apis-arkts-collections.md)）是一种在并发实例间共享传输的容器类，用于并发场景下的高性能数据传递。它的功能与ECMAScript 262规范定义的容器类似，但存在部分差异，具体可见[共享容器与原生API方法的行为差异对比](arkts-collections-introduction.md#共享容器与原生api方法的行为差异对比)。

ArkTS共享容器在多个并发实例间传递时，默认采用引用传递，允许多个并发实例操作同一容器实例。此外，还支持拷贝传递，即每个并发实例拥有独立的ArkTS容器实例。

ArkTS共享容器不是线程安全的，内部使用了fail-fast（快速失败）机制，即当检测到多个并发实例同时对容器进行结构性修改时，会触发异常。因此，在多线程场景下修改容器内属性时，开发者需要使用ArkTS提供的[异步锁](arkts-async-lock-introduction.md)机制保证ArkTS容器的安全访问。

ArkTS共享容器包含如下几种：[Array](../harmonyos-references/arkts-apis-arkts-collections-array.md)、[Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)、[Set](../harmonyos-references/arkts-apis-arkts-collections-set.md)、TypedArray（[Int8Array](../harmonyos-references/arkts-apis-arkts-collections-int8array.md)、[Uint8Array](../harmonyos-references/arkts-apis-arkts-collections-uint8array.md)、[Int16Array](../harmonyos-references/arkts-apis-arkts-collections-int16array.md)、[Uint16Array](../harmonyos-references/arkts-apis-arkts-collections-uint16array.md)、[Int32Array](../harmonyos-references/arkts-apis-arkts-collections-int32array.md)、[Uint32Array](../harmonyos-references/arkts-apis-arkts-collections-uint32array.md)、[Uint8ClampedArray](../harmonyos-references/arkts-apis-arkts-collections-uint8clampedarray.md)、[Float32Array](../harmonyos-references/arkts-apis-arkts-collections-float32array.md)）、[ArrayBuffer](../harmonyos-references/arkts-apis-arkts-collections-arraybuffer.md)、[BitVector](../harmonyos-references/arkts-apis-arkts-collections-bitvector.md)、[ConcatArray](../harmonyos-references/arkts-apis-arkts-collections-concatarray.md)，具体可见[@arkts.collections (ArkTS容器集)](../harmonyos-references/arkts-apis-arkts-collections.md)。

容器集使用示例如下：

```
1. import { ArkTSUtils, collections, taskpool } from '@kit.ArkTS';

3. @Concurrent
4. async function add(arr: collections.Array<number>, lock: ArkTSUtils.locks.AsyncLock) {
5. await lock.lockAsync(() => {  // 如果不添加异步锁，任务会因为数据竞争冲突，导致抛异常失败
6. arr[0]++;
7. })
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State message: string = 'Hello World';

15. build() {
16. RelativeContainer() {
17. Text(this.message)
18. .id('HelloWorld')
19. .fontSize(50)
20. .fontWeight(FontWeight.Bold)
21. .alignRules({
22. center: { anchor: '__container__', align: VerticalAlign.Center },
23. middle: { anchor: '__container__', align: HorizontalAlign.Center }
24. })
25. .onClick(() => {
26. let taskGroup = new taskpool.TaskGroup();
27. let lock = new ArkTSUtils.locks.AsyncLock();
28. let arr = collections.Array.create<number>(1, 0);
29. let count = 1000;
30. let num = count;
31. while (num--) {
32. taskGroup.addTask(add, arr, lock);
33. }
34. taskpool.execute(taskGroup).then(() => {
35. console.info(`Return success: ${arr[0]} === ${count}`);
36. }).catch((e: Error) => {
37. console.error("Return error.");
38. })
39. })
40. }
41. .height('100%')
42. .width('100%')
43. }
44. }
```

## 共享容器与原生API方法的行为差异对比

ArkTS提供了Sendable数据相关的共享容器集，接口行为与原生API存在部分差异，具体见下文对比。

说明

ArkTS共享容器的类型与ECMAScript 262规范定义的原生容器类型不同，因此使用原生容器Array的isArray()方法判断collections.Array实例对象会返回false。

ArkTS共享容器采用引用传递方式跨线程传递，与原生容器相比效率更高。如果需要跨线程传输大量数据，建议使用ArkTS共享容器。

### Array

支持通过[collections.Array.from](../harmonyos-references/arkts-apis-arkts-collections-array.md#from)方法将原生容器Array转换为ArkTS Array容器；支持通过原生容器Array的from方法将 ArkTS Array容器转换为原生容器Array。

| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| length: number | readonly length: number | 是 | 为了防止undefined扩散，不允许设置length。 |
| new(arrayLength ?: number): any[] | static create(arrayLength: number, initialValue: T): Array | 是 | 为了防止undefined扩散，构造函数中必须提供一个初始值。 |
| new <T>(arrayLength: number): T[] | constructor() | 否 | 构造时传入的数据必须为Sendable类型，否则将导致编译错误。 |
| new <T>(...items: T[]): T[] | constructor(first: T, ...left: T[]) | 是 | 为了防止undefined扩散，构造函数中必须提供一个初始值，继承场景下，无法调用该函数进行对象构造。 |
| from<T>(arrayLike: ArrayLike<T>): T[] | static from<T>(arrayLike: ArrayLike<T>): Array<T> | 否 | / |
| from<T, U>(iterable: Iterable<T> | ArrayLike<T>, mapfn: (v: T, k: number) => U, thisArg?: any): U[] | static from<U, T>(arrayLike: ArrayLike<U> | Iterable<U>, mapFn: ArrayFromMapFn<U, T>): Array<T> | 否 | / |
| pop(): T | undefined | pop(): T | undefined | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| push(...items: T[]): number | push(...items: T[]): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| concat(...items: ConcatArray<T>[]): T[] | concat(...items: ConcatArray<T>[]): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| concat(...items: (T | ConcatArray<T>)[]): T[] | concat(...items: ConcatArray<T>[]): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| join(separator?: string): string | join(separator?: string): string | 否 | / |
| shift(): T | undefined | shift(): T | undefined | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| slice(start?: number, end?: number): T[] | slice(start?: number, end?: number): Array<T> | 否 | / |
| sort(compareFn?: (a: T, b: T) => number): this | sort(compareFn?: (a: T, b: T) => number): Array<T> | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. 继承场景下，无法获得实际类型的返回值。 |
| unshift(...items: T[]): number | unshift(...items: T[]): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| indexOf(searchElement: T, fromIndex?: number): number | indexOf(searchElement: T, fromIndex?: number): number | 否 | / |
| forEach(callbackfn: (value: T, index: number, array: T[]) => void, thisArg?: any): void | forEach(callbackFn: (value: T, index: number, array: Array<T>) => void): void | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| map<U>(callbackfn: (value: T, index: number, array: T[]) => U, thisArg?: any): U[] | map<U>(callbackFn: (value: T, index: number, array: Array<T>) => U): Array<U> | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| filter(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): T[] | filter(predicate: (value: T, index: number, array: Array<T>) => boolean): Array<T> | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| reduce(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T | reduce(callbackFn: (previousValue: T, currentValue: T, currentIndex: number, array: Array<T>) => T): T | 否 | / |
| reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U | reduce<U>(callbackFn: (previousValue: U, currentValue: T, currentIndex: number, array: Array<T>) => U, initialValue: U): U | 否 | / |
| [n: number]: T | [index: number]: T | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| findIndex(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): number | findIndex(predicate: (value: T, index: number, obj: Array<T>) => boolean): number | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| fill(value: T, start?: number, end?: number): this | fill(value: T, start?: number, end?: number): Array<T> | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. 继承场景下，无法获得实际类型的返回值。 |
| entries(): IterableIterator<[number, T]> | entries(): IterableIterator<[number, T]> | 否 | / |
| keys(): IterableIterator<number> | keys(): IterableIterator<number> | 否 | / |
| values(): IterableIterator<T> | values(): IterableIterator<T> | 否 | / |
| includes(searchElement: T, fromIndex?: number): boolean | includes(searchElement: T, fromIndex?: number): boolean | 否 | / |
| at(index: number): T | undefined | at(index: number): T | undefined | 否 | / |
| isArray(arg: any): arg is any[] | static isArray(value: Object | undefined | null): boolean | 是 | 仅判断是否为ArkTS的Array实例，对原生容器Array返回false。 |
| of<T>(...items: T[]): T[] | static of<T>(...items: T[]): Array<T> | 否 | / |
| copyWithin(target: number, start: number, end?: number): this | copyWithin(target: number, start: number, end?: number): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| lastIndexOf(searchElement: T, fromIndex?: number): number | lastIndexOf(searchElement: T, fromIndex?: number): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| some(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean | some(predicate: ArrayPredicateFn<T, Array<T>>): boolean | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2.ArkTS不支持this，因此不支持thisArg参数。 |
| reduceRight(callbackfn: (previousValue: T, currentValue: T, currentIndex: number, array: T[]) => T): T | reduceRight(callbackFn: ArrayReduceCallback<T, T, Array<T>>): T | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| reduceRight<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number, array: T[]) => U, initialValue: U): U | reduceRight<U = T>(callbackFn: ArrayReduceCallback<U, T, Array<T>>, initialValue: U): U | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| reverse(): T[] | reverse(): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| toString(): string | toString(): string | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| find(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): T | undefined | find(predicate: (value: T, index: number, obj: Array<T>) => boolean): T | undefined | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| splice(start: number, deleteCount: number, ...items: T[]): T[] | splice(start: number, deleteCount: number, ...items: T[]): Array<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| every(predicate: (value: T, index: number, array: T[]) => unknown, thisArg?: any): boolean | every(predicate: ArrayPredicateFn<T, Array<T>>): boolean | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| toLocaleString(): string | toLocaleString(): string | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |

### ArrayBuffer

| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly byteLength: number | readonly byteLength: number | 否 | / |
| slice(begin: number, end?: number): ArrayBuffer | slice(begin: number, end?: number): ArrayBuffer | 否 | / |
| new(byteLength: number): ArrayBuffer | constructor(byteLength: number) | 否 | / |

### TypedArray（以Int8Array为例）

支持通过[collections.Int8Array.from](../harmonyos-references/arkts-apis-arkts-collections-int8array.md#from-1)方法将原生容器Int8Array转换为ArkTS Int8Array容器；也支持通过原生容器 Int8Array的from方法将ArkTS Int8Array容器转换为原生容器Int8Array。

| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly buffer: ArrayBufferLike | readonly buffer: ArrayBuffer | 否 | / |
| readonly byteLength: number | readonly byteLength: number | 否 | / |
| readonly byteOffset: number | readonly byteOffset: number | 否 | / |
| readonly length: number | readonly length: number | 否 | / |
| readonly BYTES\_PER\_ELEMENT: number | static readonly BYTES\_PER\_ELEMENT: number | 否 | / |
| copyWithin(target: number, start: number, end?: number): this | copyWithin(target: number, start: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| every(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean | every(predicate: TypedArrayPredicateFn<number, Int8Array>): boolean | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| fill(value: number, start?: number, end?: number): this | fill(value: number, start?: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| filter(predicate: (value: number, index: number, array: Int8Array) => any, thisArg?: any): Int8Array | filter(predicate: TypedArrayPredicateFn<number, Int8Array>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| find(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | undefined | find(predicate: TypedArrayPredicateFn<number, Int8Array>): number | undefined | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| findIndex(predicate: (value: number, index: number, obj: Int8Array) => boolean, thisArg?: any): number | findIndex(predicate: TypedArrayPredicateFn<number, Int8Array>): number | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| forEach(callbackfn: (value: number, index: number, array: Int8Array) => void, thisArg?: any): void | forEach(callbackFn: (value: number, index: number, array: Int8Array) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| indexOf(searchElement: number, fromIndex?: number): number | indexOf(searchElement: number, fromIndex?: number): number | 否 | / |
| join(separator?: string): string | join(separator?: string): string | 否 | / |
| map(callbackfn: (value: number, index: number, array: Int8Array) => number, thisArg?: any): Int8Array | map(callbackFn: TypedArrayForEachCallback<number, Int8Array>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number | reduce(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>): number | 否 | / |
| reduce(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number, initialValue: number): number | reduce(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>, initialValue: number): number | 否 | / |
| reduce<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U | reduce<U>(callbackFn: TypedArrayReduceCallback<U, number, Int8Array>, initialValue: U): U | 否 | / |
| reverse(): Int8Array | reverse(): Int8Array | 否 | / |
| set(array: ArrayLike<number>, offset?: number): void | set(array: ArrayLike<number>, offset?: number): void | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作否则会抛出异常。 |
| slice(start?: number, end?: number): Int8Array | slice(start?: number, end?: number): Int8Array | 否 | / |
| some(predicate: (value: number, index: number, array: Int8Array) => unknown, thisArg?: any): boolean | some(predicate: TypedArrayPredicateFn<number, Int8Array>): boolean | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| sort(compareFn?: (a: number, b: number) => number): this | sort(compareFn?: TypedArrayCompareFn<number>): Int8Array | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. 继承场景下，无法获得实际类型的返回值。 |
| subarray(begin?: number, end?: number): Int8Array | subarray(begin?: number, end?: number): Int8Array | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| [index: number]: number | [index: number]: number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| entries(): IterableIterator<[number, number]> | entries(): IterableIterator<[number, number]> | 否 | / |
| keys(): IterableIterator<number> | keys(): IterableIterator<number> | 否 | / |
| values(): IterableIterator<number> | values(): IterableIterator<number> | 否 | / |
| includes(searchElement: number, fromIndex?: number): boolean | includes(searchElement: number, fromIndex?: number): boolean | 否 | / |
| at(index: number): number | undefined | at(index: number): number | undefined | 否 | / |
| new(length: number): Int8Array | constructor(length: number) | 否 | / |
| new(array: ArrayLike<number> | ArrayBufferLike): Int8Array | constructor(array: ArrayLike<number> | ArrayBuffer) | 否 | / |
| new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array | constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number) | 否 | / |
| from(arrayLike: ArrayLike<number>): Int8Array | static from(arrayLike: ArrayLike<number>): Int8Array | 否 | / |
| from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array | static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Int8Array | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| from(arrayLike: Iterable<number>, mapfn?: (v: number, k: number) => number, thisArg?: any): Int8Array | static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Int8Array | 是 | ArkTS不支持this，因此不支持thisArg参数。 |
| of(...items: number[]): Int8Array | static of(...items: number[]): Int8Array | 否 | / |
| toString(): string | toString(): string | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| toLocaleString(): string | toLocaleString(): string | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| lastIndexOf(searchElement: number, fromIndex?: number): number | lastIndexOf(searchElement: number, fromIndex?: number): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| reduceRight(callbackfn: (previousValue: number, currentValue: number, currentIndex: number, array: Int8Array) => number): number | reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Int8Array>): number | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| reduceRight<U>(callbackfn: (previousValue: U, currentValue: number, currentIndex: number, array: Int8Array) => U, initialValue: U): U | reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Int8Array>, initialValue: U): U | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |

### Map

| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly size: number | readonly size: number | 是 | 不允许在遍历或访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| clear(): void | clear(): void | 是 | 不允许在遍历或访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| delete(key: K): boolean | delete(key: K): boolean | 是 | 不允许在遍历或访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void | forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| get(key: K): V | undefined | get(key: K): V | undefined | 是 | 不允许在遍历或访问过程中对元素进行增、删、改操作，否则将抛出异常。 |
| has(key: K): boolean | has(key: K): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| set(key: K, value: V): this | set(key: K, value: V): Map<K, V> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| entries(): IterableIterator<[K, V]> | entries(): IterableIterator<[K, V]> | 否 | / |
| keys(): IterableIterator<K> | keys(): IterableIterator<K> | 否 | / |
| values(): IterableIterator<V> | values(): IterableIterator<V> | 否 | / |
| new <K, V>(entries?: readonly (readonly [K, V])[] | null): Map<K, V> | constructor(entries?: readonly (readonly [K, V])[] | null) | 是 | 构造时传入的k,v键值不能是非Sendable数据，否则编译会报错。 |

### Set

| 原生API方法 | ArkTS容器集方法 | 是否有行为差异 | 在ArkTS容器中的差异表现 |
| --- | --- | --- | --- |
| readonly size: number | readonly size: number | 是 | Sendable类和接口中不允许使用计算属性名称(arkts-sendable-computed-prop-name)。 |
| add(value: T): this | add(value: T): Set<T> | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| clear(): void | clear(): void | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| delete(value: T): boolean | delete(value: T): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void | forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void | 是 | 1. 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。  2. ArkTS不支持this，因此不支持thisArg参数。 |
| has(value: T): boolean | has(value: T): boolean | 是 | 不允许在遍历、访问过程中进行元素的增、删、改操作，否则会抛出异常。 |
| entries(): IterableIterator<[T, T]> | entries(): IterableIterator<[T, T]> | 否 | / |
| keys(): IterableIterator<T> | keys(): IterableIterator<T> | 否 | / |
| values(): IterableIterator<T> | values(): IterableIterator<T> | 是 | Sendable类和接口中不允许使用计算属性名称(arkts-sendable-computed-prop-name)。 |
| new <T = any>(values?: readonly T[] | null): Set<T> | constructor(values?: readonly T[] | null) | 是 | 构造时传入的数据必须为Sendable类型，否则将导致编译错误。 |
