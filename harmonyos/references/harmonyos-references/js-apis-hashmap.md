---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashmap
title: @ohos.util.HashMap (非线性容器HashMap)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.HashMap (非线性容器HashMap)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:08+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:3dad68c117b5acccceebbd6984cdc0e2c005636109cbc64be79a063b5483a751
---

HashMap底层采用数组、链表和红黑树实现，支持高效查询、插入和删除。HashMap存储内容基于key-value的键值对映射，不允许重复的key，且一个key只能对应一个value。

HashMap和[TreeMap](js-apis-treemap.md)相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存储和访问，效率较低。

[HashSet](js-apis-hashset.md)基于HashMap实现。HashMap的输入参数由key、value两个值组成。在HashSet中，只对value对象进行处理。

**推荐使用场景：** 需要快速存取、删除以及插入键值对数据时，推荐使用HashMap。

文档中使用了泛型，包含以下泛型标记符：

* K：Key，键
* V：Value，值

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { HashMap } from '@kit.ArkTS';
```

## HashMap

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | HashMap的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

HashMap的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The HashMap's constructor cannot be directly invoked. |

**示例：**

```
1. let hashMap = new HashMap<string, number>();
```

### isEmpty

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断该HashMap是否为空。

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
1. const hashMap = new HashMap<string, number>();
2. let result = hashMap.isEmpty();
3. console.info("result = ", result) // result = true
```

### hasKey

PhonePC/2in1TabletTVWearable

hasKey(key: K): boolean

判断此HashMap中是否包含指定key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 指定Key。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定Key返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasKey method cannot be bound. |

**示例：**

```
1. const hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. let result = hashMap.hasKey("squirrel");
4. console.info("result:", result);  // result: true
```

### hasValue

PhonePC/2in1TabletTVWearable

hasValue(value: V): boolean

判断此HashMap中是否包含指定value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | V | 是 | 指定value。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定的value返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The hasValue method cannot be bound. |

**示例：**

```
1. const hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. let result = hashMap.hasValue(123);
4. console.info("result:", result);  // result: true
```

### get

PhonePC/2in1TabletTVWearable

get(key: K): V

获取指定key对应的value，不存在返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 查找的指定key。 |

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
1. const hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let result = hashMap.get("sparrow");
5. console.info("result:", result);  // result: 356
```

### setAll

PhonePC/2in1TabletTVWearable

setAll(map: HashMap<K, V>): void

将一个HashMap中的所有元素组添加到另一个HashMap中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | HashMap<K, V> | 是 | 被添加元素的HashMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The setAll method cannot be bound. |

**示例：**

```
1. const hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let newHashMap = new HashMap<string, number>();
5. newHashMap.set("newMap", 99);
6. hashMap.setAll(newHashMap);
7. let result = hashMap.hasKey("newMap");
8. console.info("result:", result);  // result: true
```

### set

PhonePC/2in1TabletTVWearable

set(key: K, value: V): Object

向HashMap中添加或更新一组数据。

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
| Object | 返回添加或更新后的HashMap。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 10200011 | The set method cannot be bound. |

**示例：**

```
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123)
3. console.info("result:", hashMap.get("squirrel"));  // result: 123
```

### remove

PhonePC/2in1TabletTVWearable

remove(key: K): V

删除指定key所对应元素。

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
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let result = hashMap.remove("sparrow");
5. console.info("result:", result);  // result: 356
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除HashMap中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. hashMap.clear();
5. let result = hashMap.isEmpty();
6. console.info("result:", result);  // result: true
```

### keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<K>

返回新迭代器对象，包含此映射中所有的键。

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
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let keys = hashMap.keys();
5. for (let key of keys) {
6. console.info("key:" + key);
7. }
8. // key:squirrel
9. // key:sparrow
```

### values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<V>

返回新迭代器对象，包含此映射中所有键对应的值。

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
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let values = hashMap.values();
5. for (let value of values) {
6. console.info("value:", value)
7. }
8. // value: 123
9. // value: 356
```

### replace

PhonePC/2in1TabletTVWearable

replace(key: K, newValue: V): boolean

用于替换指定键对应的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 依据key指定替换的元素。 |
| newValue | V | 是 | 替换成员数据的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否成功对已有数据进行替换，成功返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The replace method cannot be bound. |

**示例：**

```
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("sparrow", 123);
3. let result = hashMap.replace("sparrow", 357);
4. console.info("result:", result);  // result: true
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void

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
| value | V | 否 | 当前遍历到的元素键值对的值。 |
| key | K | 否 | 当前遍历到的元素键值对的键。 |
| map | HashMap<K, V> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("sparrow", 123);
3. hashMap.set("gull", 357);
4. hashMap.forEach((value: number, key: string) => {
5. console.info("value: " + value, "key: " + key);
6. });
7. // value: 123 key: sparrow
8. // value: 357 key: gull
```

```
1. // 不建议在forEach中使用set、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashMap = new HashMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. hashMap.set("sparrow" + i, 123);
5. }

7. for(let i = 0; i < 10; i++) {
8. hashMap.remove("sparrow" + i);
9. }
```

### entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

返回包含此映射中包含的键值对的新迭代器对象。

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
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);
4. let iter = hashMap.entries();
5. let temp: IteratorResult<Object[]> = iter.next();
6. while(!temp.done) {
7. console.info("key:" + temp.value[0]);
8. console.info("value:" + temp.value[1]);
9. temp = iter.next();
10. }
```

```
1. // 不建议在entries中使用set、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashMap = new HashMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. hashMap.set("sparrow" + i, 123);
5. }

7. for(let i = 0; i < 10; i++) {
8. hashMap.remove("sparrow" + i);
9. }
```

### [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

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
1. let hashMap = new HashMap<string, number>();
2. hashMap.set("squirrel", 123);
3. hashMap.set("sparrow", 356);

5. // 使用方法一：
6. for (let item of hashMap) {
7. console.info("key:", item[0]);
8. console.info("value:", item[1]);
9. }
10. // key: squirrel
11. // value: 123
12. // key: sparrow
13. // value: 356

15. // 使用方法二：
16. let iter = hashMap[Symbol.iterator]();
17. let temp: IteratorResult<Object[]> = iter.next();
18. while(!temp.done) {
19. console.info("key:", temp.value[0]);
20. console.info("value:", temp.value[1]);
21. temp = iter.next();
22. }
23. // key: squirrel
24. // value: 123
25. // key: sparrow
26. // value: 356
```

```
1. // 不建议在Symbol.iterator中使用set、remove方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let hashMap = new HashMap<string, number>();
3. for(let i = 0; i < 10; i++) {
4. hashMap.set("sparrow" + i, 123);
5. }

7. for(let i = 0; i < 10; i++) {
8. hashMap.remove("sparrow" + i);
9. }
```
