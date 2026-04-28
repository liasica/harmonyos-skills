---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treeset
title: @ohos.util.TreeSet (非线性容器TreeSet)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.TreeSet (非线性容器TreeSet)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:11+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:8472355f474150daaa2166fd72eb63a20a77f42c42dce8ad86a41d885981cf23
---

TreeSet基于[TreeMap](js-apis-treemap.md)实现，在TreeSet中，只对value对象进行处理。TreeSet可用于存储一系列值的集合，元素中value唯一且有序。

TreeSet和[HashSet](js-apis-hashset.md)中的元素都不允许重复。HashSet中的数据无序存放，而TreeSet是有序存放。HashSet允许插入null值，但TreeSet不建议插入null值，可能会影响排序结果。

**推荐使用场景：** 一般需要存储有序集合的场景，可以使用TreeSet。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TreeSet } from '@kit.ArkTS';
```

## TreeSet

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | TreeSet的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(comparator?: (firstValue: T, secondValue: T) => boolean)

TreeSet的构造函数，支持通过比较函数对元素进行升序或降序排序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| comparator | function | 否 | 用户自定义的比较函数，可通过比较关系对元素进行排序。默认值为null，表示不提供比较函数。 |

comparator的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstValue | T | 是 | 前一项元素。 |
| secondValue | T | 是 | 后一项元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200012 | The TreeSet's constructor cannot be directly invoked. |

**示例：**

```
1. // 默认构造
2. let treeSet = new TreeSet<string | number | boolean | Object>();
```

```
1. // 使用comparator firstValue < secondValue，表示期望结果为升序排序。反之firstValue > secondValue，表示为降序排序。
2. let treeSet: TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string): boolean => {
3. return firstValue < secondValue;
4. });
5. treeSet.add("a");
6. treeSet.add("c");
7. treeSet.add("d");
8. treeSet.add("b");
9. for (let value of treeSet) {
10. console.info("value:", value);
11. }
12. // value: a
13. // value: b
14. // value: c
15. // value: d
```

```
1. // 当插入自定义类型时，则必须要提供比较函数。
2. class TestEntry{
3. public id: number = 0;
4. }
5. let ts1: TreeSet<TestEntry> = new TreeSet<TestEntry>((t1: TestEntry, t2: TestEntry): boolean => {return t1.id > t2.id;});
6. let entry1: TestEntry = {
7. id: 0
8. };
9. let entry2: TestEntry = {
10. id: 1
11. }
12. ts1.add(entry1);
13. ts1.add(entry2);
14. console.info("treeSet: ", ts1.length);
```

### isEmpty

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断容器是否为空。

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
1. let treeSet = new TreeSet<string>();
2. let result = treeSet.isEmpty();
3. console.info("result:", result);  // result: true
```

### has

PhonePC/2in1TabletTVWearable

has(value: T): boolean

判断容器中是否包含指定元素。

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

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let treeSet  = new TreeSet<number>();
2. treeSet.add(123);
3. let result = treeSet.has(123);
4. console.info("result:", result); // result: true
```

### getFirstValue

PhonePC/2in1TabletTVWearable

getFirstValue(): T

获取容器中排序第一的数据，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回排序第一的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirstValue method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let result = treeSet.getFirstValue();
5. console.info("result:", result); // result: sparrow
```

### getLastValue

PhonePC/2in1TabletTVWearable

getLastValue(): T

获取容器中排序最后的数据，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回排序最后的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLastValue method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let result = treeSet.getLastValue();
5. console.info("result:", result); // result: squirrel
```

### add

PhonePC/2in1TabletTVWearable

add(value: T): boolean

向容器中添加一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 添加的成员数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功添加新数据至容器返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. let result = treeSet.add("squirrel");
3. console.info("result:", result); // result: true
```

### remove

PhonePC/2in1TabletTVWearable

remove(value: T): boolean

删除指定的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 指定的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功删除元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let result = treeSet.remove("sparrow");
5. console.info("result:", result); // result: true
```

### getLowerValue

PhonePC/2in1TabletTVWearable

getLowerValue(key: T): T

获取容器中比传入元素排序靠前一位的元素，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | T | 是 | 对比的元素值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回排序中对比元素前一位的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The getLowerValue method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. treeSet.add("gander");
5. let result = treeSet.getLowerValue("sparrow");
6. console.info("result:", result); // result: gander
```

### getHigherValue

PhonePC/2in1TabletTVWearable

getHigherValue(key: T): T

获取容器中比传入元素排序靠后一位的元素，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | T | 是 | 对比的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回排序中传入元素后一位的数据。为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The getHigherValue method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. treeSet.add("gander");
5. let result = treeSet.getHigherValue("sparrow");
6. console.info("result:", result); // result: squirrel
```

### popFirst

PhonePC/2in1TabletTVWearable

popFirst(): T

删除容器中排序最前的数据，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The popFirst method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let result = treeSet.popFirst();
5. console.info("result:", result); // result: sparrow
```

### popLast

PhonePC/2in1TabletTVWearable

popLast(): T

删除容器中排序最后的数据，为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The popLast method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let result = treeSet.popLast();
5. console.info("result:", result); // result: squirrel
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除容器中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. treeSet.clear();
5. let result = treeSet.isEmpty();
6. console.info("result:", result); // result: true
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<T>

返回包含此映射中键值的新迭代器对象。

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
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let values = treeSet.values();
5. for (let value of values) {
6. console.info("value:", value)
7. }
8. // value: sparrow
9. // value: squirrel
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void

通过回调函数来遍历实例对象上的元素及其下标。

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
| value | T | 否 | 当前遍历到的value元素。 |
| key | T | 否 | 当前遍历到的key元素。 |
| set | TreeSet<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let treeSet = new TreeSet<string>();
2. treeSet.add("sparrow");
3. treeSet.add("gull");
4. treeSet.forEach((value: string, key: string): void => {
5. console.info("value:" + value);
6. });
7. // value:gull
8. // value:sparrow
```

```
1. // 不建议在forEach中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeSet = new TreeSet<string>();
3. for(let i = 0; i < 10; i++) {
4. treeSet.add("sparrow" + i);
5. }
6. for(let i = 0; i < 10; i++) {
7. treeSet.remove("sparrow" + i);
8. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[T, T]>

返回包含此映射中键值对的新迭代器对象。

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
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. let it = treeSet.entries();
5. let t: IteratorResult<Object[]> = it.next();
6. while(!t.done) {
7. console.info("TreeSet: " + t.value[1]);
8. t = it.next()
9. }
10. // TreeSet: sparrow
11. // TreeSet: squirrel
```

```
1. // 不建议在entries中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeSet = new TreeSet<string>();
3. for(let i = 0; i < 10; i++) {
4. treeSet.add("sparrow" + i);
5. }
6. for(let i = 0; i < 10; i++) {
7. treeSet.remove("sparrow" + i);
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
1. let treeSet = new TreeSet<string>();
2. treeSet.add("squirrel");
3. treeSet.add("sparrow");
4. // 使用方法一：
5. for (let item of treeSet) {
6. console.info("value:" + item);
7. }
8. // value:sparrow
9. // value:squirrel

11. // 使用方法二：
12. let iter = treeSet[Symbol.iterator]();
13. let temp: IteratorResult<string> = iter.next().value;
14. while(temp != undefined) {
15. console.info("value:" + temp);
16. temp = iter.next().value;
17. }
18. // value:sparrow
19. // value:squirrel
```

```
1. // 不建议在Symbol.iterator中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeSet = new TreeSet<string>();
3. for(let i = 0; i < 10; i++) {
4. treeSet.add("sparrow" + i);
5. }
6. for(let i = 0; i < 10; i++) {
7. treeSet.remove("sparrow" + i);
8. }
```
