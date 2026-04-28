---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightset
title: @ohos.util.LightWeightSet (非线性容器LightWeightSet)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.LightWeightSet (非线性容器LightWeightSet)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:86b79aec434a4b7c9e2fe6a9a9797d41050bfba6f872b576bedc9d5085b8b7cc
---

LightWeightSet可用于存储一系列值的集合，存储元素中value值唯一。

LightWeightSet依据泛型定义，采用轻量级结构，初始默认容量大小为8，每次扩容大小为原始容量的两倍。

集合中value值的查找依赖于hash算法，通过一个数组存储hash值，然后映射到其他数组中的value值。

LightWeightSet和[HashSet](js-apis-hashset.md)都是用来存储元素的集合，但LightWeightSet的占用内存更小。

**推荐使用场景：** 当需要存取某个集合或是对某个集合去重时，推荐使用占用内存更小的LightWeightSet。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 规格限制

PhonePC/2in1TabletTVWearable

当LightWeightSet存入的value为number类型且值大于INT32\_MAX或小于INT32\_MIN时，针对LightWeightSet的操作，其结果可能与预期不一致。

这是因为，当value为number类型且值大于INT32\_MAX或小于INT32\_MIN时，存储结构会发生改变。

例如在以下示例针对value的计算中，1758783600000大于INT32\_MAX，此时会通过TaggedDouble存储；1758783600小于INT32\_MIN，此时会通过TaggedInt存储。由于以上存储方式的差异，当对其进行hash算法即会计算出不同的hash值，从而导致映射结果不同，产生与预期不一致的现象。

```
1. let st = new LightWeightSet<number>();
2. let value = 1758783600000 / 1000;  // 1758783600000 > INT32_MAX
3. st.add(value);
4. console.info("result:", st.has(1758783600));  // result: false
5. console.info("result:", st.has(value));  // result: true
```

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LightWeightSet } from '@kit.ArkTS';
```

## LightWeightSet

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | LightWeightSet的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

LightWeightSet的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The LightWeightSet's constructor cannot be directly invoked. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<number | string>();
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
1. const lightWeightSet = new LightWeightSet<number>();
2. let result = lightWeightSet.isEmpty();
3. console.info("result:", result);  // result: true
```

### add

PhonePC/2in1TabletTVWearable

add(obj: T): boolean

向容器中添加数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | T | 是 | 添加的成员数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功添加元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. let result = lightWeightSet.add("squirrel");
3. console.info("result:", result);  // result: true
```

### addAll

PhonePC/2in1TabletTVWearable

addAll(set: LightWeightSet<T>): boolean

将另一个容器的所有元素组添加到当前容器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | LightWeightSet<T> | 是 | 提供添加元素的LightWeightSet。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功添加元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The addAll method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let set = new LightWeightSet<string>();
5. set.add("gull");
6. lightWeightSet.addAll(set);
7. let result = lightWeightSet.has("gull");
8. console.info("result:", result);  // result: true
```

### hasAll

PhonePC/2in1TabletTVWearable

hasAll(set: LightWeightSet<T>): boolean

判断容器中是否包含指定set中的所有元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| set | LightWeightSet<T> | 是 | 比较对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含所有元素时返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The hasAll method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let set = new LightWeightSet<string>();
5. set.add("sparrow");
6. let result = lightWeightSet.hasAll(set);
7. console.info("result:", result);  // result: true
```

### has

PhonePC/2in1TabletTVWearable

has(key: T): boolean

判断容器中是否包含指定的key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | T | 是 | 指定key |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定key时返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<number>();
2. lightWeightSet.add(123);
3. let result = lightWeightSet.has(123);
4. console.info("result:", result);  // result: true
```

### increaseCapacityTo

PhonePC/2in1TabletTVWearable

increaseCapacityTo(minimumCapacity: number): void

将当前LightWeightSet扩容至指定容量。如果传入的容量值大于或等于当前LightWeightSet中的元素个数，将容量变更为新容量，小于则不会变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minimumCapacity | number | 是 | 需要容纳的元素数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of minimumCapacity is out of range. |
| 10200011 | The increaseCapacityTo method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.increaseCapacityTo(10);
```

### getIndexOf

PhonePC/2in1TabletTVWearable

getIndexOf(key: T): number

获取指定key所对应的下标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | T | 是 | 查找的指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 在lightWeightSet中指定数据的下标。若lightWeightSet中没有要查找的元素，则返回一个负值。表示目标哈希值应该插入的位置，插入位置是从1开始计数的，负号表示这是一个插入位置而不是索引。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getIndexOf method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.getIndexOf("sparrow");
5. console.info("result:", result);  // result: 0
```

### remove

PhonePC/2in1TabletTVWearable

remove(key: T): T

删除并返回指定key对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | T | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除元素的值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.remove("sparrow");
5. console.info("result:", result);  // result: sparrow
```

### removeAt

PhonePC/2in1TabletTVWearable

removeAt(index: number): boolean

删除指定下标所对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于INT32\_MAX即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 确认是否成功删除元素，成功删除元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The removeAt method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.removeAt(1);
5. console.info("result:", result);  // result: true
```

### getValueAt

PhonePC/2in1TabletTVWearable

getValueAt(index: number): T

获取容器中指定下标对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于INT32\_MAX即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回指定下标对应的元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The getValueAt method cannot be bound. |

**参数：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.getValueAt(1);
5. console.info("result:", result);  // result: squirrel
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
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. lightWeightSet.clear();
5. let result = lightWeightSet.isEmpty();
6. console.info("result:", result);  // result: true
```

### toString

PhonePC/2in1TabletTVWearable

toString(): String

获取包含容器中所有键和值的字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| String | 返回对应字符串。 |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.toString();
5. console.info("result:", result);  // result: sparrow,squirrel
```

### toArray

PhonePC/2in1TabletTVWearable

toArray(): Array<T>

获取包含此容器中所有对象的数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<T> | 返回对应数组。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The toArray method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let result = lightWeightSet.toArray();
5. console.info(result.toString());
6. // sparrow,squirrel
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
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let values = lightWeightSet.values();
5. for (let value of values) {
6. console.info("value:", value);
7. }
8. // value: sparrow
9. // value: squirrel
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void

通过回调函数来遍历LightWeightSet实例对象上的元素以及元素对应的下标。

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
| value | T | 否 | 当前遍历到的元素键值对的值，默认值为首个键值对的值。 |
| key | T | 否 | 当前遍历到的元素键值对的键（和value相同），默认值为首个键值对的键。 |
| set | LightWeightSet<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("sparrow");
3. lightWeightSet.add("gull");
4. lightWeightSet.forEach((value: string, key: string) => {
5. console.info("value:" + value, "key:" + key);
6. });
7. // value:gull key:gull
8. // value:sparrow key:sparrow
```

```
1. // 不建议在forEach函数中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightSet = new LightWeightSet<string>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightSet.add(i + "123");
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightSet.remove(i + "123");
8. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[T, T]>

返回包含此映射中包含的键值对的新迭代器对象。

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
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let iter = lightWeightSet.entries();
5. for (let item of iter) {
6. console.info("value:", item[1])
7. }
8. // value: sparrow
9. // value: squirrel
```

```
1. // 不建议在entries中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightSet = new LightWeightSet<string>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightSet.add(i + "123");
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightSet.remove(i + "123");
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
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");

5. // 使用方法一：
6. for (let value of lightWeightSet) {
7. console.info("value:", value);
8. }
9. // value: sparrow
10. // value: squirrel

12. // 使用方法二：
13. let iter = lightWeightSet[Symbol.iterator]();
14. let temp: IteratorResult<string> = iter.next();
15. while(!temp.done) {
16. console.info("value:", temp.value);
17. temp = iter.next();
18. }
19. // value: sparrow
20. // value: squirrel
```

```
1. // 不建议在Symbol.iterator中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightSet = new LightWeightSet<string>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightSet.add(i + "123");
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightSet.remove(i + "123");
8. }
```

### equal(deprecated)

PhonePC/2in1TabletTVWearable

equal(obj: Object): boolean

判断此容器与obj的构成元素是否相同。

说明

此接口从API version 8开始支持，从API version 12开始废弃。无替代接口。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | 是 | 比较对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当obj为仅含string或number的LightWeightSet或数组，且对象内部元素构成相同时，返回true；其他情况返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The equal method cannot be bound. |

**示例：**

```
1. let lightWeightSet = new LightWeightSet<string>();
2. lightWeightSet.add("squirrel");
3. lightWeightSet.add("sparrow");
4. let obj = ["sparrow", "squirrel"];
5. let result = lightWeightSet.equal(obj);
6. console.info("result:", result);  // result: true
```
