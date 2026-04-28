---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-map
title: Class (Map)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Class (Map)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:51+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:7726dd3fea2ade1498ca9cb60988fec43035dee7e6947738ecc7b20c6490fcf9
---

一种基于键值对存储的非线性数据结构。能够高效地通过唯一键来存取对应的值。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

文档中存在泛型的使用，涉及以下泛型标记符：

* K：Key，键
* V：Value，值

K和V类型都需为[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)。

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
| size | number | 是 | 否 | Map的元素个数。 |

## constructor

PhonePC/2in1TabletTVWearable

constructor(entries?: readonly (readonly [K, V])[] | null)

构造函数，用于创建ArkTS Map对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | readonly (readonly [K, V])[] | null | 否 | 键值对数组或其它可迭代对象。默认值为null，创建一个空Map对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

**示例：**

```
1. // 正例1：
2. const myMap = new collections.Map<number, number>();
```

```
1. // 正例2：
2. const myMap = new collections.Map<number, string>([
3. [1, "one"],
4. [2, "two"],
5. [3, "three"]
6. ]);
```

```
1. // 反例：
2. @Sendable
3. class SharedClass {
4. constructor() {
5. }
6. }
7. let sObj = new SharedClass();
8. const myMap1: collections.Map<number, SharedClass> = new collections.Map<number, SharedClass>([[1, sObj]]);
9. // Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
10. let obj = new Object();
11. const myMap2: collections.Map<number, Object> = new collections.Map<number, Object>([[1, obj]]);
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(iterable: Iterable<readonly [K, V]>)

创建ArkTS Map对象的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iterable | Iterable<readonly [K, V]> | 是 | 用于构造ArkTS Map的对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Map's constructor cannot be directly invoked. |

**示例：**

```
1. const mapper = new Map([
2. ['1', 'a'],
3. ['2', 'b'],
4. ]);
5. let newMap = new collections.Map<string, string>(mapper.entries());
6. console.info(newMap.get('1')); // 预期输出： a
7. console.info(newMap.get('2')); // 预期输出： b
```

## entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

返回一个Map迭代器对象，该对象包含了此Map中的每个元素的[key, value]对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 例1：
2. const myMap = new collections.Map<number, string>([
3. [0, "foo"],
4. [1, "bar"]
5. ]);

7. const iterator = myMap.entries();
8. // Expected output: 0, foo
9. console.info(iterator.next().value);
10. // Expected output: 1, bar
11. console.info(iterator.next().value);
```

```
1. // 例2：
2. const myMap: collections.Map<number, string> = new collections.Map<number, string>([
3. [0, "one"],
4. [1, "two"],
5. [2, "three"],
6. [3, "four"]
7. ]);
8. // 返回一个myMap迭代器对象，该对象包含了此myMap中的每个元素的[number, string]键值对。
9. const entriesIter: IterableIterator<[number, string]> = myMap.entries();
10. // 遍历entriesIter迭代器对象。
11. for (const entry of entriesIter) {
12. if (entry[1].startsWith('t')) {
13. myMap.delete(entry[0]);
14. }
15. }
16. // Expected output: 2
17. console.info("size:" + myMap.size);
```

## keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<K>

返回一个Map迭代器对象，该对象包含了此Map中每个元素的键。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<K> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const myMap = new collections.Map<number, string>([
2. [0, "foo"],
3. [1, "bar"]
4. ]);

6. const iterator = myMap.keys();
7. // Expected output: 0
8. console.info(iterator.next().value);
9. // Expected output: 1
10. console.info(iterator.next().value);
```

## values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<V>

返回一个Map迭代器对象，该对象包含此Map中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<V> | 返回一个Map迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const myMap = new collections.Map<number, string>([
2. [0, "foo"],
3. [1, "bar"]
4. ]);

6. const iterator = myMap.values();
7. // Expected output: "foo"
8. console.info(iterator.next().value);
9. // Expected output: "bar"
10. console.info(iterator.next().value);
```

## clear

PhonePC/2in1TabletTVWearable

clear(): void

删除该Map中的所有元素。

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
1. const myMap = new collections.Map<number, string>([
2. [0, "foo"],
3. [1, "bar"]
4. ]);
5. // Expected output: 2
6. console.info("size:" + myMap.size);
7. myMap.clear();
8. // Expected output: 0
9. console.info("size:" + myMap.size);
```

## delete

PhonePC/2in1TabletTVWearable

delete(key: K): boolean

删除该Map中指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待删除元素的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果元素存在并已被删除，则为true；否则该元素不存在，返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const myMap = new collections.Map<string, string>([
2. ["hello", "world"],
3. ]);
4. // Expected result: true
5. console.info("result:" + myMap.delete("hello"));
6. // Expected result: false
7. console.info("result:" + myMap.has("hello"));
8. // Expected result: false
9. console.info("result:" + myMap.delete("hello"));
```

## forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: V, key: K, map: Map<K, V>) => void): void

按插入顺序对该Map中的每个键/值对执行一次回调函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | (value: V, key: K, map: Map<K, V>) => void | 是 | 回调函数。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 否 | 当前遍历到的元素键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键。 |
| map | Map<K, V> | 否 | 当前map实例对象。 |

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
2. new collections.Map<string, number>([
3. ['foo', 0],
4. ['bar', 1],
5. ['baz', 2],
6. ]).forEach((value, key, map) => {
7. console.info(`m[${key}] = ${value}`);
8. });
```

```
1. // 反例：
2. new collections.Map<string, number>([
3. ['foo', 0],
4. ['bar', 1],
5. ['baz', 2],
6. ]).forEach((value, key, map) => {
7. // Throw exception `Concurrent modification error.`
8. map.delete(key);
9. });
```

## get

PhonePC/2in1TabletTVWearable

get(key: K): V | undefined

返回该Map中的指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 与指定键相关联的元素，如果键在Map对象中找不到，则返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The get method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const myMap = new collections.Map<string, string>([
2. ["hello", "world"],
3. ]);
4. // Expected output: "world"
5. console.info(myMap.get("hello"));
6. // Expected output: undefined
7. console.info(myMap.get("hel"));
```

## has

PhonePC/2in1TabletTVWearable

has(key: K): boolean

判断该Map中是否存在指定元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 待查找元素的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果存在指定元素，则返回true，否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const myMap = new collections.Map<string, string>([
2. ["hello", "world"],
3. ]);
4. // Expected output: true
5. console.info("result:" + myMap.has("hello"));
6. // Expected output: false
7. console.info("result:" + myMap.has("world"));
```

## set

PhonePC/2in1TabletTVWearable

set(key: K, value: V): Map<K, V>

向该Map添加或更新一个指定的键值对。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 添加或更新指定元素的键。 |
| value | V | 是 | 添加或更新指定元素的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Map<K, V> | Map对象 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The set method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 正例：
2. const myMap = new collections.Map<string, string>();
3. myMap.set("foo", "bar");
```

```
1. // 反例：
2. let obj = new Object();
3. const myMap: collections.Map<string, Object> = new collections.Map<string, Object>();
4. // Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
5. myMap.set("foo", obj);
```

## [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象，并返回该对象。

说明

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```
1. let map = new collections.Map<number, string>([
2. [0, "one"],
3. [1, "two"],
4. [2, "three"],
5. [3, "four"]
6. ]);

8. let keys = Array.from(map.keys());
9. for (let key of keys) {
10. console.info("key:" + key);
11. console.info("value:" + map.get(key));
12. }
```
