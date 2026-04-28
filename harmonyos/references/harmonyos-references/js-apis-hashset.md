---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashset
title: @ohos.util.HashSet (非线性容器HashSet)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.HashSet (非线性容器HashSet)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:09+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:7b285a033cee02ccb8da55cb117ebba9f39ee5b27d6b75d66fb5fa59110742de
---

HashSet基于[HashMap](js-apis-hashmap.md)实现。在HashSet中，仅处理value对象。

HashSet和[TreeSet](js-apis-treeset.md)相比，HashSet中的数据按Hash值排序，因此元素的插入顺序与遍历时的顺序可能不一致，而TreeSet则是按照元素的自然排序或者自定义比较器进行有序存储。它们集合中的元素都不允许重复，HashSet允许插入null值，TreeSet不建议插入null值，会影响排序结果。

**推荐使用场景：** 可以利用HashSet不重复的特性，当需要不重复的集合或需要去重某个集合的时候使用。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { HashSet } from '@kit.ArkTS';
```

## HashSet

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | HashSet的元素个数。 |

**示例：**

```
1. let hashSet = new HashSet<number>();
2. hashSet.add(1);
3. hashSet.add(2);
4. hashSet.add(3);
5. hashSet.add(4);
6. hashSet.add(5);
7. let res = hashSet.length;
8. console.info("length:", res);  // length: 5
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

HashSet的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The HashSet's constructor cannot be directly invoked. |

**示例：**

```
1. let hashSet = new HashSet<number>();
```

### isEmpty

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断HashSet是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 为空返回true，不为空返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

**示例：**

```
1. const hashSet = new HashSet<number>();
2. let result = hashSet.isEmpty();
3. console.info("result:", result);  // result: true
```

### has

PhonePC/2in1TabletTVWearable

has(value: T): boolean

判断HashSet是否包含指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. let result = hashSet.has("squirrel");
4. console.info("result:", result);  // result: true
```

### add

PhonePC/2in1TabletTVWearable

add(value: T): boolean

向HashSet添加元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 添加成员数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功添加元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. let result = hashSet.add("squirrel");
3. console.info("result:", result);  // result: true
```

### remove

PhonePC/2in1TabletTVWearable

remove(value: T): boolean

从HashSet中删除指定的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 指定删除的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功删除指定元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. hashSet.add("sparrow");
4. let result = hashSet.remove("sparrow");
5. console.info("result:", result);  // result: true
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除HashSet中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. hashSet.add("sparrow");
4. hashSet.clear();
5. let result = hashSet.isEmpty();
6. console.info("result:", result);  // result: true
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<T>

返回包含此映射中所有键值的新迭代器对象。

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
| 10200011 | The values method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. hashSet.add("sparrow");
4. let values = hashSet.values();
5. for (let value of values) {
6. console.info("value:", value);
7. }
8. // value: squirrel
9. // value: sparrow
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: T, key?: T, set?: HashSet<T>) => void, thisArg?: Object): void

在遍历过程中对每个元素调用一次回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值为当前实例对象。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 否 | 当前遍历到的元素键值对的值。 |
| key | T | 否 | 当前遍历到的元素键值对的键（和value相同）。 |
| set | HashSet<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("sparrow");
3. hashSet.add("squirrel");
4. hashSet.forEach((value: string, key: string): void => {
5. console.info("value:" + value, "key:" + key);
6. });
7. // value:squirrel key:squirrel
8. // value:sparrow key:sparrow
```

```
1. // 不建议在forEach中使用add、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashSet = new HashSet<string>();
3. for(let i = 0; i < 10; i++) {
4. hashSet.add("sparrow" + i);
5. }
6. for(let i = 0; i < 10; i++) {
7. hashSet.remove("sparrow" + i);
8. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[T, T]>

返回包含此映射中所有键值对的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[T, T]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The entries method cannot be bound. |

**示例：**

```
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. hashSet.add("sparrow");
4. let iter = hashSet.entries();
5. let temp: IteratorResult<[string, string]> = iter.next();
6. while(!temp.done) {
7. console.info("key:" + temp.value[0]);
8. console.info("value:" + temp.value[1]);
9. temp = iter.next();
10. }
11. // key:squirrel
12. // value:squirrel
13. // key:sparrow
14. // value:sparrow
```

```
1. // 不建议在entries中使用set、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashSet = new HashSet<string>();
3. for(let i = 0; i < 10; i++) {
4. hashSet.add("sparrow" + i);
5. }
6. for(let i = 0; i < 10; i++) {
7. hashSet.remove("sparrow" + i);
8. }
```

### [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。

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
1. let hashSet = new HashSet<string>();
2. hashSet.add("squirrel");
3. hashSet.add("sparrow");

5. // 使用方法一：
6. for (let item of hashSet) {
7. console.info("value: " + item);
8. }
9. // value: squirrel
10. // value: sparrow

12. // 使用方法二：
13. let iter = hashSet[Symbol.iterator]();
14. let temp: IteratorResult<string> = iter.next();
15. while(!temp.done) {
16. console.info("value: " + temp.value);
17. temp = iter.next();
18. }
19. // value: squirrel
20. // value: sparrow
```

```
1. // 不建议在Symbol.iterator中使用set、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashSet = new HashSet<string>();
3. for(let i = 0;i < 10;i++) {
4. hashSet.add("sparrow" + i);
5. }
6. for(let i = 0;i < 10;i++) {
7. hashSet.remove("sparrow" + i);
8. }
```
