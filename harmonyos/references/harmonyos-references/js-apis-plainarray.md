---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plainarray
title: @ohos.util.PlainArray (非线性容器PlainArray)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.PlainArray (非线性容器PlainArray)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:10+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:a10ee11a32dd3a8d9a509a896893dc5bc6b8561bbe774adc6111475280e95d00
---

PlainArray可用于存储具有关联关系的key-value键值对集合，其中key值唯一且类型为number，每个key对应一个value。

PlainArray依据泛型定义，采用轻量级结构，通过二分查找算法在集合中查找 key 值，并映射到其他数组中的value值。

PlainArray和[LightWeightMap](js-apis-lightweightmap.md)都是用来存储键值对，且均采用轻量级结构，但PlainArray的key值类型仅限于number。

**推荐使用场景：** 当需要存储key值为number类型的键值对时，可以使用PlainArray。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { PlainArray } from '@kit.ArkTS';
```

## PlainArray

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | PlainArray的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

PlainArray的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The PlainArray's constructor cannot be directly invoked. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
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
1. const plainArray = new PlainArray<string>();
2. let result = plainArray.isEmpty();
3. console.info("result = ", result); // result =  true
```

### has

PhonePC/2in1TabletTVWearable

has(key: number): boolean

判断容器中是否包含指定key。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 指定key。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含指定key返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. let result = plainArray.has(1);
4. console.info("result = ", result); // result = true
```

### get

PhonePC/2in1TabletTVWearable

get(key: number): T

获取指定key所对应的value。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 查找的指定key。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回key映射的value值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The get method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.get(1);
5. console.info("result:", result);  // result: squirrel
```

### getIndexOfKey

PhonePC/2in1TabletTVWearable

getIndexOfKey(key: number): number

查找指定key对应的下标值，如果未找到则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 指定key。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定key对应的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The getIndexOfKey method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.getIndexOfKey(2);
5. console.info("result = ", result); // result = 1
```

### getIndexOfValue

PhonePC/2in1TabletTVWearable

getIndexOfValue(value: T): number

查找指定value元素第一次出现的下标值，如果未找到则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 指定value元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定value元素第一次出现时的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getIndexOfValue method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.getIndexOfValue("squirrel");
5. console.info("result:", result);  // result: 0
```

### getKeyAt

PhonePC/2in1TabletTVWearable

getKeyAt(index: number): number

查找指定下标元素键值对中的key值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回该下标元素键值对中的key值，失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The getKeyAt method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.getKeyAt(1);
5. console.info("result = ", result); // result = 2
```

### getValueAt

PhonePC/2in1TabletTVWearable

getValueAt(index: number): T

查找指定下标元素键值对中的Value值，失败则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回该下标元素键值对中的value值，失败返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200001 | The value of index is out of range. |
| 10200011 | The getValueAt method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.getValueAt(1);
5. console.info("result:", result);  // result: sparrow
```

### clone

PhonePC/2in1TabletTVWearable

clone(): PlainArray<T>

克隆一个实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PlainArray<T> | 返回新的对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clone method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let newPlainArray = plainArray.clone();
5. console.info("result:", newPlainArray.get(1));  // result: squirrel
```

### add

PhonePC/2in1TabletTVWearable

add(key: number, value: T): void

向容器中添加一组数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 添加成员数据的键名。需要小于等于int32\_max即2147483647。 |
| value | T | 是 | 添加成员数据的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. console.info("result:", plainArray.get(1));  // result: squirrel
```

### remove

PhonePC/2in1TabletTVWearable

remove(key: number): T

删除指定key对应的键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | number | 是 | 指定key。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回所删除的键值对中的Value值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.remove(2);
5. console.info("result:", result);  // result: sparrow
```

### removeAt

PhonePC/2in1TabletTVWearable

removeAt(index: number): T

删除指定下标对应的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定元素下标。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The removeAt method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.removeAt(1);
5. console.info("result:", result);  // result: sparrow
```

### removeRangeFrom

PhonePC/2in1TabletTVWearable

removeRangeFrom(index: number, size: number): number

删除指定范围内的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 删除元素的起始下标。需要小于等于int32\_max即2147483647。 |
| size | number | 是 | 期望删除元素个数。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 实际删除元素个数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200001 | The value of index is out of range. |
| 10200011 | The removeRangeFrom method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.removeRangeFrom(1, 3);
5. console.info("result:", result);  // result: 1
```

### setValueAt

PhonePC/2in1TabletTVWearable

setValueAt(index: number, value: T): void

替换容器中指定下标对应键值对中的键值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定替换数据下标。需要小于等于int32\_max即2147483647。 |
| value | T | 是 | 替换键值对中的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200001 | The value of index is out of range. |
| 10200011 | The setValueAt method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string | number>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. plainArray.setValueAt(1, 3546);
5. let result = plainArray.getValueAt(1);
6. console.info("result:", result);  // result: 3546
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

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The toString method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. let result = plainArray.toString();
5. console.info("result:", result);  // result: 1:squirrel,2:sparrow
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
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. plainArray.clear();
5. let result = plainArray.isEmpty();
6. console.info("result:", result);  // result: true
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray<T>) => void, thisArg?: Object): void

在遍历PlainArray实例对象中每一个元素的过程中，对每个元素执行回调函数。

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
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值。 |
| PlainArray | PlainArray<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");
4. plainArray.forEach((value: string, index: number) => {
5. console.info("value:" + value, "index:" + index);
6. });
7. // value:squirrel index:1
8. // value:sparrow index:2
```

```
1. // 不建议在forEach中使用add、remove、removeAt方法，因其可能导致迭代过程中的状态异常，建议使用for循环来进行安全的插入与删除操作。
2. let plainArray = new PlainArray<string>();
3. for(let i = 0; i < 10; i++) {
4. plainArray.add(i,"123");
5. }

7. for(let i = 0; i < 10; i++) {
8. plainArray.remove(i);
9. }
```

### [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[number, T]>

返回一个包含key-value键值对的迭代器对象，其中key是number类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[number, T]> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```
1. let plainArray = new PlainArray<string>();
2. plainArray.add(1, "squirrel");
3. plainArray.add(2, "sparrow");

5. for (let item of plainArray) {
6. console.info("value:" + item[1], "index:" + item[0]);
7. }
8. // value:squirrel index:1
9. // value:sparrow index:2
```

```
1. // 不建议在Symbol.iterator中使用add、remove、removeAt方法，会导致死循环等不可预知的风险，可使用for循环来进行插入和删除。
2. let plainArray = new PlainArray<string>();
3. for(let i = 0; i < 10; i++) {
4. plainArray.add(i,"123");
5. }

7. for(let i = 0; i < 10; i++) {
8. plainArray.remove(i);
9. }
```
