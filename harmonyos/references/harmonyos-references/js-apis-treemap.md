---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treemap
title: @ohos.util.TreeMap (非线性容器TreeMap)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.TreeMap (非线性容器TreeMap)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e716f0d97f2caab1c43930264849001953ee30ce8eb5d5cddeddd8f204c7fb5d
---

TreeMap可用于存储具有关联关系的key-value键值对集合，存储元素中key值唯一，每个key对应一个value。

TreeMap底层使用红黑树实现，可以利用二叉树特性快速查找键值对。key值有序存储，可以实现快速的插入和删除。

TreeMap和[HashMap](js-apis-hashmap.md)相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。

**推荐使用场景：** 一般需要存储有序键值对的场景，可以使用TreeMap。

文档使用了泛型，涉及以下泛型标记符：

* K：Key，键
* V：Value，值

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { TreeMap } from '@kit.ArkTS';
```

## TreeMap

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | TreeMap的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(comparator?:(firstValue: K, secondValue: K) => boolean)

TreeMap的构造函数，支持通过比较函数使元素按照自定义规则排序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| comparator | function | 否 | 用户自定义的比较函数，可通过比较关系对元素进行排序。默认值为null，表示不提供比较函数。 |

comparator的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstValue | K | 是 | 前一项元素。 |
| secondValue | K | 是 | 后一项元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200012 | The TreeMap's constructor cannot be directly invoked. |

**示例：**

```
1. // 默认构造
2. let treeMap = new TreeMap<number, number>();
```

```
1. //使用comparator firstValue < secondValue，表示期望结果为升序排序。反之firstValue > secondValue，表示为降序排序。
2. let treeMap: TreeMap<string,string> = new TreeMap<string,string>((firstValue: string, secondValue: string): boolean => {
3. return firstValue > secondValue;
4. });
5. treeMap.set("aa","3");
6. treeMap.set("dd","1");
7. treeMap.set("cc","2");
8. treeMap.set("bb","4");
9. for (let item of treeMap) {
10. console.info("key: " + item[0], "value: " + item[1]);
11. }
12. // 输出结果：
13. // key: dd value: 1
14. // key: cc value: 2
15. // key: bb value: 4
16. // key: aa value: 3
```

```
1. // 当插入自定义类型时，则必须要提供比较函数。
2. class TestEntry{
3. public id: number = 0;
4. }

6. let ts1: TreeMap<TestEntry, string> = new TreeMap<TestEntry, string>((t1: TestEntry, t2: TestEntry): boolean => {
7. return t1.id < t2.id;
8. });
9. let entry1: TestEntry = {
10. id: 0
11. };
12. let entry2: TestEntry = {
13. id: 1
14. }
15. ts1.set(entry1, "0");
16. ts1.set(entry2, "1");
17. console.info("length:", ts1.length); // length: 2
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
| boolean | 为空返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The isEmpty method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<number, number>();
2. let result = treeMap.isEmpty();
3. console.info("result:", result);  // result: true
```

### hasKey

PhonePC/2in1TabletTVWearable

hasKey(key: K): boolean

判断容器中是否包含指定key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定key返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasKey method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. let result = treeMap.hasKey("squirrel");
4. console.info("result:", result);  // result: true
```

### hasValue

PhonePC/2in1TabletTVWearable

hasValue(value: V): boolean

判断容器中是否包含该指定value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 是 | 指定value。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. let result = treeMap.hasValue(123);
4. console.info("result:", result);  // result: true
```

### get

PhonePC/2in1TabletTVWearable

get(key: K): V

获取指定key所对应的value，若为空则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回key映射的value值，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The get method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let result = treeMap.get("sparrow");
5. console.info("result:", result); // result: 356
```

### getFirstKey

PhonePC/2in1TabletTVWearable

getFirstKey(): K

获取容器中排序第一的key，若为空则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K | 返回排序第一的key，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirstKey method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let result = treeMap.getFirstKey();
5. console.info("result:", result); // result: sparrow
```

### getLastKey

PhonePC/2in1TabletTVWearable

getLastKey(): K

获取容器中排序最后的key，若为空则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K | 返回排序最后的key，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLastKey method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let result = treeMap.getLastKey();
5. console.info("result:", result); // result: squirrel
```

### setAll

PhonePC/2in1TabletTVWearable

setAll(map: TreeMap<K, V>): void

将一个TreeMap中的所有元素组添加到另一个TreeMap中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | TreeMap<K, V> | 是 | 该map会添加到其调用setAll接口的map对象中。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The setAll method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let map : TreeMap<string, number> = new TreeMap();
5. map.set("demo", 12);
6. map.setAll(treeMap); // 将treeMap中的所有元素添加到map中
7. map.forEach((value ?: number, key ?: string) : void => {
8. console.info("value: " + value, "key: " + key);
9. })
10. // 输出结果:
11. // value: 12 key: demo
12. // value: 356 key: sparrow
13. // value: 123 key: squirrel
```

### set

PhonePC/2in1TabletTVWearable

set(key: K, value: V): Object

向容器中添加或更新一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 添加成员数据的键名。 |
| value | V | 是 | 添加成员数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回添加后的TreeMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The set method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. console.info("squirrel:", treeMap.get("squirrel")); // squirrel: 123
```

### remove

PhonePC/2in1TabletTVWearable

remove(key: K): V

删除指定key对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回删除元素的值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let result = treeMap.remove("sparrow"); // 删除数据
5. console.info("result = " + result); // result = 356
```

### getLowerKey

PhonePC/2in1TabletTVWearable

getLowerKey(key: K): K

获取容器中小于对比key值的最大键，如果不存在小于对比key值的键值，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 对比的key值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K | 返回排序中key前一位的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLowerKey method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<number, string>();
2. treeMap.set(1, 'one');
3. treeMap.set(2, 'two');
4. treeMap.set(3, 'three');
5. treeMap.set(4, 'four');
6. let result = treeMap.getLowerKey(3);
7. console.info("result:", result); // result: 2
```

### getHigherKey

PhonePC/2in1TabletTVWearable

getHigherKey(key: K): K

获取容器中大于对比key值的最小键，如果不存在大于对比key值的键值，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 对比的key值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K | 返回排序中key后一位的数据，为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getHigherKey method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<number, string>();
2. treeMap.set(1, 'one');
3. treeMap.set(2, 'two');
4. treeMap.set(3, 'three');
5. treeMap.set(4, 'four');
6. let result = treeMap.getHigherKey(3);
7. console.info("result:", result); // result: 4
```

### replace

PhonePC/2in1TabletTVWearable

replace(key: K, newValue: V): boolean

对容器中一组数据进行更新（替换）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |
| newValue | V | 是 | 替换的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 对指定key对应的元素替换成功返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The replace method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("sparrow", 123);
3. let result = treeMap.replace("sparrow", 357);
4. console.info("sparrow:", treeMap.get("sparrow")); // sparrow: 357
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
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. treeMap.clear();
5. let result = treeMap.isEmpty();
6. console.info("result:", result); // result: true
```

### keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<K>

返回包含此映射中所有键的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<K> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The keys method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let keys = treeMap.keys();
5. for (let key of keys) {
6. console.info("key:", key);
7. }
8. // 输出结果：
9. // key: sparrow
10. // key: squirrel
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<V>

返回包含此映射中键值的新迭代器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<V> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let values = treeMap.values();
5. for (let value of values) {
6. console.info("value:", value);
7. }
8. // value: 356
9. // value: 123
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object): void

通过回调函数来遍历实例对象上的元素及其下标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值为undefined。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 否 | 当前遍历到的元素键值对的值，默认值为首个键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键，默认值为首个键值对的键。 |
| map | TreeMap<K, V> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("sparrow", 123);
3. treeMap.set("gull", 357);
4. treeMap.forEach((value: number, key: string): void => {
5. console.info("value: " + value, "key: " + key);
6. });
7. // 输出结果：
8. // value: 357 key: gull
9. // value: 123 key: sparrow
```

```
1. // 不建议在forEach中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeMap = new TreeMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. treeMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0;i < 10; i++) {
7. treeMap.remove("sparrow" + i);
8. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

返回包含此映射中键值对的新迭代器对象。

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
| 10200011 | The entries method cannot be bound. |

**示例：**

```
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);
4. let it = treeMap.entries();
5. let t: IteratorResult<Object[]> = it.next();
6. while(!t.done) {
7. console.info("TreeMap:", t.value);
8. t = it.next()
9. }
10. // 输出结果：
11. // TreeMap: sparrow,356
12. // TreeMap: squirrel,123
```

```
1. // 不建议在entries中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeMap = new TreeMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. treeMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0;i < 10; i++) {
7. treeMap.remove("sparrow" + i);
8. }
```

### [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个JavaScript对象。

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
1. let treeMap = new TreeMap<string, number>();
2. treeMap.set("squirrel", 123);
3. treeMap.set("sparrow", 356);

5. // 使用方法一：
6. for (let item of treeMap) {
7. console.info("TreeMap:", item[0], item[1]);
8. }
9. // 输出结果：
10. // TreeMap: sparrow,356
11. // TreeMap: squirrel,123

13. // 使用方法二：
14. let iter = treeMap[Symbol.iterator]();
15. let temp: IteratorResult<Object[]> = iter.next();
16. while(!temp.done) {
17. console.info("key:", temp.value[0]);
18. console.info("value:", temp.value[1]);
19. temp = iter.next();
20. }
21. // 输出结果：
22. // key: sparrow
23. // value: 356
24. // key: squirrel
25. // value: 123
```

```
1. // 不建议在Symbol.iterator中使用set、remove方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let treeMap = new TreeMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. treeMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0;i < 10; i++) {
7. treeMap.remove("sparrow" + i);
8. }
```
