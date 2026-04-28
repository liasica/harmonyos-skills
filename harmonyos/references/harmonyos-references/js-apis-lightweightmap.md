---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightmap
title: @ohos.util.LightWeightMap (非线性容器LightWeightMap)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.LightWeightMap (非线性容器LightWeightMap)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:76c0a181a04a4d6a3ba481c921c47276aa76a15583c9308ba889fd9bca4f501f
---

LightWeightMap可用于存储具有关联关系的key-value键值对集合，存储元素中key值唯一，每个key对应一个value。

LightWeightMap依据泛型定义，采用轻量级结构，初始默认容量大小为8，每次扩容大小为原始容量的两倍。

集合中key值的查找依赖于hash算法，通过一个数组存储hash值，然后映射到其他数组中的key值及value值。

LightWeightMap和[HashMap](js-apis-hashmap.md)都是用来存储键值对的集合，但LightWeightMap占用内存更小。

**推荐使用场景：** 当需要存取key-value键值对时，推荐使用占用内存更小的LightWeightMap。

文档中使用了泛型，涉及以下泛型标记符：

* K：Key，键
* V：Value，值

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 规格限制

PhonePC/2in1TabletTVWearable

当LightWeightMap存入的key为number类型且值大于INT32\_MAX或小于INT32\_MIN时，针对LightWeightMap的操作，其结果可能与预期不一致。

这是因为，当key为number类型且值大于INT32\_MAX或小于INT32\_MIN时，存储结构会发生改变。

例如在以下示例针对key的计算中，1758783600000大于INT32\_MAX，此时会通过TaggedDouble存储；1758783600小于INT32\_MIN，此时会通过TaggedInt存储。由于以上存储方式的差异，当对其进行hash算法即会计算出不同的hash值，从而导致映射结果不同，产生与预期不一致的现象。

```
1. let mp = new LightWeightMap<number, number>();
2. let key = 1758783600000 / 1000;  // 1758783600000 > INT32_MAX
3. mp.set(key, 1001);
4. console.info("result:", mp.hasKey(1758783600));  // result: false
5. console.info("result:", mp.hasKey(key));  // result: true
```

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LightWeightMap } from '@kit.ArkTS';
```

## LightWeightMap

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | LightWeightMap的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

LightWeightMap的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The LightWeightMap's constructor cannot be directly invoked. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
```

### isEmpty

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断LightWeightMap是否为空。

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
1. const lightWeightMap = new LightWeightMap<string, number>();
2. let result = lightWeightMap.isEmpty();
3. console.info("result:", result);  // result: true
```

### hasAll

PhonePC/2in1TabletTVWearable

hasAll(map: LightWeightMap<K, V>): boolean

判断LightWeightMap中是否包含指定map中的所有元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | LightWeightMap<K, V> | 是 | 比较对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含所有元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The hasAll method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let map = new LightWeightMap<string, number>();
5. map.set("sparrow", 356);
6. let result = lightWeightMap.hasAll(map);
7. console.info("result = ", result); // result = true
```

### hasKey

PhonePC/2in1TabletTVWearable

hasKey(key: K): boolean

判断LightWeightMap中是否包含指定key。

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. let result = lightWeightMap.hasKey("squirrel");
4. console.info("result:", result);  // result: true
```

### hasValue

PhonePC/2in1TabletTVWearable

hasValue(value: V): boolean

判断LightWeightMap中是否包含指定value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 是 | 指定元素。 |

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. let result = lightWeightMap.hasValue(123);
4. console.info("result:", result);  // result: true
```

### increaseCapacityTo

PhonePC/2in1TabletTVWearable

increaseCapacityTo(minimumCapacity: number): void

将当前LightWeightMap扩容至指定容量。如果传入的容量值大于或等于当前LightWeightMap中的元素个数，将容量变更为新容量，小于则不会变更。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The increaseCapacityTo method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.increaseCapacityTo(10);
```

### get

PhonePC/2in1TabletTVWearable

get(key: K): V

获取指定key所对应的value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回key映射的value值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The get method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.get("sparrow");
5. console.info("result:", result);  // result: 356
```

### getIndexOfKey

PhonePC/2in1TabletTVWearable

getIndexOfKey(key: K): number

查找key元素首次出现的下标值，如果未找到返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 被查找的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回key元素首次出现的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getIndexOfKey method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.getIndexOfKey("sparrow");
5. console.info("result:", result);  // result: 0
```

### getIndexOfValue

PhonePC/2in1TabletTVWearable

getIndexOfValue(value: V): number

查找value元素首次出现的下标值，如果未找到则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 是 | 被查找的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回value元素首次出现的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getIndexOfValue method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.getIndexOfValue(123);
5. console.info("result:", result);  // result: 1
```

### getKeyAt

PhonePC/2in1TabletTVWearable

getKeyAt(index: number): K

查找指定下标的元素键值对中key值，如果未找到则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 所查找的下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K | 返回该下标对应的元素键值对中key值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The getKeyAt method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.getKeyAt(1);
5. console.info("result:", result);  // result: squirrel
```

### setAll

PhonePC/2in1TabletTVWearable

setAll(map: LightWeightMap<K, V>): void

将一个LightWeightMap中的所有元素组添加到另一个LightWeightMap中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | LightWeightMap<K, V> | 是 | 提供添加元素的LightWeightMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The setAll method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let map = new LightWeightMap<string, number>();
5. map.setAll(lightWeightMap);   // 将lightWeightMap中所有的元素添加到map中
6. let result = map.get("sparrow");
7. console.info("result:", result);  // result: 356
```

### set

PhonePC/2in1TabletTVWearable

set(key: K, value: V): Object

向LightWeightMap中添加或更新一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 添加或更新成员数据的键名。 |
| value | V | 是 | 添加或更新成员数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回添加或更新数据后的LightWeightMap。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The set method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. let result = lightWeightMap.set("squirrel", 123);
3. console.info("result:", result);  // result: squirrel:123
```

### remove

PhonePC/2in1TabletTVWearable

remove(key: K): V

删除指定key映射的元素。

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("sparrow", 356);
3. let result = lightWeightMap.remove("sparrow");
4. console.info("result:", result);  // result: 356
```

### removeAt

PhonePC/2in1TabletTVWearable

removeAt(index: number): boolean

删除指定下标对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功删除元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The removeAt method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.removeAt(1);
5. console.info("result:", result);  // result: true
```

### setValueAt

PhonePC/2in1TabletTVWearable

setValueAt(index: number, newValue: V): boolean

替换指定下标对应键值对中的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于int32\_max即2147483647。 |
| newValue | V | 是 | 替换键值对中的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功替换返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The setValueAt method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. lightWeightMap.setValueAt(1, 3546);
5. console.info("result:", lightWeightMap.get("squirrel"));  // result: 3546
```

### getValueAt

PhonePC/2in1TabletTVWearable

getValueAt(index: number): V

获取指定下标对应键值对中的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回指定下标对应键值对中的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The getValueAt method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.getValueAt(1);
5. console.info("result:", result);  // result: 123
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除LightWeightMap中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. lightWeightMap.clear();
5. let result = lightWeightMap.isEmpty();
6. console.info("result:", result);  // result: true
```

### keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<K>

返回包含此映射中所有的键的新迭代器对象。

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let keys = lightWeightMap.keys();
5. for (let key of keys) {
6. console.info("key:", key);
7. }
8. // key: sparrow
9. // key: squirrel
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<V>

返回包含此映射中所有键值的新迭代器对象。

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let values = lightWeightMap.values();
5. for (let value of values) {
6. console.info("value:", value);
7. }
8. // value: 356
9. // value: 123
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object): void

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
| value | V | 否 | 当前遍历到的元素键值对的值，默认值为首个键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键，默认值为首个键值对的键。 |
| map | LightWeightMap<K, V> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("sparrow", 123);
3. lightWeightMap.set("gull", 357);
4. lightWeightMap.forEach((value: number, key: string) => {
5. console.info("value:" + value, "key:" + key);
6. });
7. // value:123 key:sparrow
8. // value:357 key:gull
```

```
1. // 不建议在forEach中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightMap = new LightWeightMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightMap.remove("sparrow" + i);
8. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

返回包含此映射中所有键值对的新迭代器对象。

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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let iter = lightWeightMap.entries();
5. let temp: IteratorResult<Object[]> = iter.next();
6. while(!temp.done) {
7. console.info("key:" + temp.value[0]);
8. console.info("value:" + temp.value[1]);
9. temp = iter.next();
10. }
```

```
1. // 不建议在entries中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightMap = new LightWeightMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightMap.remove("sparrow" + i);
8. }
```

### toString

PhonePC/2in1TabletTVWearable

toString(): String

将此映射中包含的键值对拼接成字符串并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| String | 返回一个字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The toString method cannot be bound. |

**示例：**

```
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);
4. let result = lightWeightMap.toString();
5. console.info("result:", result);  // result: sparrow:356,squirrel:123
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
1. let lightWeightMap = new LightWeightMap<string, number>();
2. lightWeightMap.set("squirrel", 123);
3. lightWeightMap.set("sparrow", 356);

5. // 使用方法一：
6. for (let item of lightWeightMap) {
7. console.info("key:", item[0]);
8. console.info("value:", item[1]);
9. }
10. // key: sparrow
11. // value: 356
12. // key: squirrel
13. // value: 123

15. // 使用方法二：
16. let iter = lightWeightMap[Symbol.iterator]();
17. let temp: IteratorResult<Object[]> = iter.next();
18. while(!temp.done) {
19. console.info("key:", temp.value[0]);
20. console.info("value:", temp.value[1]);
21. temp = iter.next();
22. }
23. // key: sparrow
24. // value: 356
25. // key: squirrel
26. // value: 123
```

```
1. // 不建议在Symbol.iterator中使用set、setValueAt、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let lightWeightMap = new LightWeightMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. lightWeightMap.set("sparrow" + i, 123);
5. }
6. for(let i = 0; i < 10; i++) {
7. lightWeightMap.remove("sparrow" + i);
8. }
```
