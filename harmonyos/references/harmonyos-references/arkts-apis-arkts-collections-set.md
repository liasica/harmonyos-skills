---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-set
title: Class (Set)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Class (Set)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:51+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:e0421ef8c1a9a3f9cc51f52937ff17168ac6c6db1323206871cf9df95e1a8a44
---

一种存储唯一值的非线性数据结构，能够高效地进行元素存在性检测和去重操作。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

* T：Type，支持[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)。

**装饰器类型：**@Sendable

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { collections } from '@kit.ArkTS';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | number | 是 | 否 | Set的元素个数。 |

## constructor

PhonePC/2in1TabletTVWearable

constructor(values?: readonly T[] | null)

构造函数，用于创建ArkTS Set对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | readonly T[] | null | 否 | 数组或其它可迭代对象。默认值为null，创建一个空Set对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

**示例：**

```
1. // 正例1：
2. const mySet = new collections.Set<number>();
```

```
1. // 正例2：
2. const mySet = new collections.Set<number>([1, 2, 3, 4, 5]);
```

```
1. // 反例：
2. @Sendable
3. class SharedClass {
4. constructor() {
5. }
6. }

8. let sObj = new SharedClass();
9. const mySet1: collections.Set<number|SharedClass> = new collections.Set<number|SharedClass>([1, sObj]);
10. // Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
11. let obj = new Object();
12. const mySet2: collections.Set<number|SharedClass> = new collections.Set<number|Object>([1, obj]);
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(iterable: Iterable<T>)

创建ArkTS Set对象的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | Iterable<T> | 是 | 用于构造ArkTS Set的对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

**示例：**

```
1. const mapper = new Map([
2. ['1', 'a'],
3. ['2', 'b'],
4. ]);
5. let newSet = new collections.Set<string>(mapper.values());
6. console.info(newSet.has('a').toString()); // 预期输出： true
7. console.info(newSet.has('b').toString()); // 预期输出： true
```

## entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[T, T]>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[T, T]> | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的键值对。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const mySet = new collections.Set<number>([0, 1, 2, 3]);

3. const iterator = mySet.entries();
4. // Expected output: [0, 0]
5. console.info(iterator.next().value);
6. // Expected output: [1, 1]
7. console.info(iterator.next().value);
```

## keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<T>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的键。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const mySet = new collections.Set<number>([0, 1, 2, 3]);

3. const iterator = mySet.keys();
4. // Expected output: 0
5. console.info(iterator.next().value);
6. // Expected output: 1
7. console.info(iterator.next().value);
```

## values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<T>

返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个Set迭代器对象，该对象包含了此Set中每个元素的值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 例1：
2. const mySet = new collections.Set<number>([0, 1, 2, 3]);

4. const iterator = mySet.values();
5. // Expected output: 0
6. console.info(iterator.next().value);
7. // Expected output: 1
8. console.info(iterator.next().value);
```

```
1. // 例2：
2. const mySet = new collections.Set<number>([0, 1, 2, 3]);

4. const valueIter = mySet.values();
5. for (let value of valueIter) {
6. if (value % 2 == 0) {
7. mySet.delete(value);
8. }
9. }

11. // Expected output: 2
12. console.info("size:" + mySet.size);
```

## clear

PhonePC/2in1TabletTVWearable

clear(): void

删除该Set中的所有元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const mySet = new collections.Set<number>([0, 1]);
2. // Expected output: 2
3. console.info("size:" + mySet.size);
4. mySet.clear();
5. // Expected output: 0
6. console.info("size:" + mySet.size);
```

## delete

PhonePC/2in1TabletTVWearable

delete(value: T): boolean

删除该Set中指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 待删除元素的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功删除返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const mySet = new collections.Set<string>(["hello", "world"]);
2. // Expected result: true
3. console.info("result:" + mySet.delete("hello"));
4. // Expected result: false
5. console.info("result:" + mySet.has("hello"));
6. // Expected result: false
7. console.info("result:" + mySet.delete("hello"));
```

## forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void

按插入顺序对该Set中的每个键/值对执行一次回调函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | (value: T, value2: T, set: Set<T>) => void | 是 | 回调函数。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 否 | 当前遍历到的元素键值对的值。 |
| value2 | T | 否 | 当前遍历到的元素键值对的键。 |
| set | Set<T> | 否 | 当前set实例对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The forEach method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 正例：
2. new collections.Set<string>(['foo', 'bar', 'baz']).forEach((value1, value2, set) => {
3. console.info(`s[${value1}] = ${value2}`);
4. });
```

```
1. // 反例：
2. new collections.Set<string>(['foo', 'bar', 'baz']).forEach((value1, value2, set) => {
3. // Throw exception `Concurrent modification error.`
4. set.delete(value1);
5. });
```

## has

PhonePC/2in1TabletTVWearable

has(value: T): boolean

判断该Set中是否存在指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 待查找元素的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果存在指定元素，则返回true；否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const mySet = new collections.Set<string>(["hello", "world"]);
2. // Expected output: true
3. console.info("result:" + mySet.has("hello"));
4. // Expected output: true
5. console.info("result:" + mySet.has("world"));
```

## add

PhonePC/2in1TabletTVWearable

add(value: T): Set<T>

如果没有相同元素，则在该Set中插入一个新元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 待插入元素的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Set<T> | Set对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The add method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 正例：
2. const mySet: collections.Set<string> = new collections.Set<string>();
3. mySet.add("foo");
```

```
1. // 反例：
2. let obj = new Object();
3. const mySet: collections.Set<Object> = new collections.Set<Object>();
4. // Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
5. mySet.add(obj);
```

## [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象，并返回该对象。

说明

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```
1. let set = new collections.Set<number>([1, 2, 3, 4, 5]);

3. let val: Array<number> = Array.from(set.values());
4. for (let item of val) {
5. console.info("value: " + item);
6. }
```
