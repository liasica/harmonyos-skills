---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arraylist
title: @ohos.util.ArrayList (线性容器ArrayList)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.ArrayList (线性容器ArrayList)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5501fb75bba9fa97d195d5c4faf12021d4a1572b50ffa102806687328d831df2
---

ArrayList是一种线性数据结构，底层基于数组实现。ArrayList会根据实际需要动态调整容量，每次扩容增加50%。

ArrayList和[LinkedList](js-apis-linkedlist.md)相比，ArrayList的随机访问效率更高。但由于ArrayList的增删操作可能需要对数组内其他元素进行移动，LinkedList的增加和删除操作效率更高。

**推荐使用场景：** 当需要频繁读取集合中的元素时，推荐使用ArrayList。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ArrayList } from '@kit.ArkTS';
```

## ArrayList

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | ArrayList的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

ArrayList的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The ArrayList's constructor cannot be directly invoked. |

**示例：**

```
1. let arrayList = new ArrayList<string | number>();
```

### add

PhonePC/2in1TabletTVWearable

add(element: T): boolean

在ArrayList尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 待插入的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 插入成功返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. class C1 {
2. name: string = ""
3. age: string = ""
4. }
5. let arrayList = new ArrayList<string | number | boolean | Array<number> | C1>();
6. arrayList.add("a");
7. arrayList.add(1);
8. let b = [1, 2, 3];
9. arrayList.add(b);
10. let c : C1 = {name: "Dylan", age: "13"}
11. let result1 = arrayList.add(c);
12. let result2 = arrayList.add(false);
13. console.info("result1:", result1);  // result1: true
14. console.info("result2:", result2);  // result2: true
15. console.info("length:", arrayList.length);  // length: 5
```

### insert

PhonePC/2in1TabletTVWearable

insert(element: T, index: number): void

在长度范围内指定位置index插入元素element。如果index超出范围，则插入失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 被插入的元素。 |
| index | number | 是 | 被插入的位置索引。需要小于等于int32\_max即2147483647。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The insert method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number | string | boolean>();
2. arrayList.insert("A", 0);
3. arrayList.insert(0, 1);
4. arrayList.insert(true, 2);
5. console.info("length:", arrayList.length);  // length: 3
```

### has

PhonePC/2in1TabletTVWearable

has(element: T): boolean

判断此ArrayList中是否包含该指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示包含指定元素，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<string>();
2. arrayList.add("squirrel");
3. let result: boolean = arrayList.has("squirrel");
4. console.info("result:", result);  // result: true
```

### getIndexOf

PhonePC/2in1TabletTVWearable

getIndexOf(element: T): number

返回指定元素第一次出现的下标，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定元素第一次出现时的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getIndexOf method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(2);
6. arrayList.add(1);
7. arrayList.add(2);
8. arrayList.add(4);
9. let result: number = arrayList.getIndexOf(2);
10. console.info("result = ", result); // result = 0
```

### getLastIndexOf

PhonePC/2in1TabletTVWearable

getLastIndexOf(element: T): number

返回指定元素最后一次出现的下标，查找失败返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定元素最后一次出现时的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLastIndexOf method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(2);
6. arrayList.add(1);
7. arrayList.add(2);
8. arrayList.add(4);
9. let result: number = arrayList.getLastIndexOf(2);
10. console.info("result = ", result); // result = 5
```

### removeByIndex

PhonePC/2in1TabletTVWearable

removeByIndex(index: number): T

根据元素的下标值查找元素，返回元素后将其删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定元素的下标值。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of "index" is out of range. |
| 10200011 | The removeByIndex method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(2);
6. arrayList.add(4);
7. let result: number = arrayList.removeByIndex(2);
8. console.info("result = ", result); // result = 5
```

### remove

PhonePC/2in1TabletTVWearable

remove(element: T): boolean

删除查找到的第一个指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除成功返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: boolean = arrayList.remove(2);
7. console.info("result = ", result); // result =  true
```

### removeByRange

PhonePC/2in1TabletTVWearable

removeByRange(fromIndex: number, toIndex: number): void

删除指定范围内的元素，区间包含fromIndex，但不包含toIndex，即左闭右开区间[fromIndex, toIndex)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromIndex | number | 是 | 起始下标。 |
| toIndex | number | 是 | 终止下标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The removeByRange method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.removeByRange(2, 4);
```

### replaceAllElements

PhonePC/2in1TabletTVWearable

replaceAllElements(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => T, thisArg?: Object): void

用户操作ArrayList中的元素，用操作后的元素替换原元素并返回操作后的元素。

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
| index | number | 否 | 当前遍历到的下标值，默认值为0。 |
| arrlist | ArrayList<T> | 否 | 当前调用replaceAllElements方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The replaceAllElements method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.replaceAllElements((value: number): number => {
7. // 用户操作逻辑根据实际场景进行添加。
8. return value;
9. });
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void, thisArg?: Object): void

在遍历ArrayList实例对象的过程中，对每个元素执行回调函数。

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
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值，默认值为0。 |
| arrlist | ArrayList<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.forEach((value: number, index?: number) => {
7. console.info("value:" + value, "index:" + index);
8. });
9. // value:2 index:0
10. // value:4 index:1
11. // value:5 index:2
12. // value:4 index:3
```

### sort

PhonePC/2in1TabletTVWearable

sort(comparator?: ArrayListComparatorFn<T>): void

根据指定比较器所定义的顺序，对ArrayList中的元素进行排序。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| comparator | [ArrayListComparatorFn<T>](js-apis-arraylist.md#arraylistcomparatorfnt23) | 否 | 回调函数，默认为升序排序的回调函数。  API version23开始发生兼容性变更，在API version22及之前的版本其类型为：(firstValue: T, secondValue: T) => number。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 10200011 | The sort method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.sort((a: number, b: number) => a - b);
7. arrayList.sort((a: number, b: number) => b - a);
8. arrayList.sort();
```

### subArrayList

PhonePC/2in1TabletTVWearable

subArrayList(fromIndex: number, toIndex: number): ArrayList<T>

根据下标截取ArrayList中的一段元素，并返回这一段ArrayList实例，区间包含fromIndex，但不包含toIndex，即左闭右开区间[fromIndex, toIndex)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromIndex | number | 是 | 起始下标。 |
| toIndex | number | 是 | 终止下标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayList<T> | 返回ArrayList对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The subArrayList method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: ArrayList<number> = arrayList.subArrayList(2, 4);
7. console.info("result = ", result.length); // result = 2
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除ArrayList中的所有元素，并把length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.clear();
```

### clone

PhonePC/2in1TabletTVWearable

clone(): ArrayList<T>

克隆一个与ArrayList相同的实例，并返回克隆后的实例。修改克隆后的实例并不会影响原实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayList<T> | 返回ArrayList对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clone method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result:  ArrayList<number> = arrayList.clone();
7. console.info("result = ", result.length); // result = 4
```

### getCapacity

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前实例的容量大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前实例的容量大小。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getCapacity method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: number = arrayList.getCapacity();
7. console.info("result = ", result); // result = 10
```

### convertToArray

PhonePC/2in1TabletTVWearable

convertToArray(): Array<T>

把当前ArrayList实例转换成数组，并返回转换后的数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<T> | 返回数组类型。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The convertToArray method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: Array<number> = arrayList.convertToArray();
7. console.info("result = ", result); // result =  2,4,5,4
```

### isEmpty

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

判断该ArrayList是否为空。

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
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: boolean = arrayList.isEmpty();
7. console.info("result = ", result); // result =  false
```

### [index: number]12+

PhonePC/2in1TabletTVWearable

[index: number]: T

获取指定索引值对应位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 元素的位置索引。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 容器中对应索引值为index的元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200001 | The value of index is out of range. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. let result: number = arrayList[2];
7. console.info("result = ", result); // result =  5
```

### increaseCapacityTo

PhonePC/2in1TabletTVWearable

increaseCapacityTo(newCapacity: number): void

如果传入的新容量大于或等于ArrayList中的元素个数，将容量变更为新容量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newCapacity | number | 是 | 新容量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The increaseCapacityTo method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.increaseCapacityTo(2);
7. arrayList.increaseCapacityTo(8);
8. console.info("result = ", arrayList.length); // result = 4
```

### trimToCurrentLength

PhonePC/2in1TabletTVWearable

trimToCurrentLength(): void

释放ArrayList中预留的空间，把容量调整为当前的元素个数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The trimToCurrentLength method cannot be bound. |

**示例：**

```
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);
6. arrayList.trimToCurrentLength();
7. console.info("result = ", arrayList.length); // result = 4
```

### [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，每一项都是一个JavaScript对象。

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
1. let arrayList = new ArrayList<number>();
2. arrayList.add(2);
3. arrayList.add(4);
4. arrayList.add(5);
5. arrayList.add(4);

7. // 使用方法一：
8. for (let value of arrayList) {
9. console.info("value:", value);
10. }
11. // value: 2
12. // value: 4
13. // value: 5
14. // value: 4

16. // 使用方法二：
17. let iter = arrayList[Symbol.iterator]();
18. let temp: IteratorResult<number> = iter.next();
19. while(!temp.done) {
20. console.info("value:", temp.value);
21. temp = iter.next();
22. }
23. // value: 2
24. // value: 4
25. // value: 5
26. // value: 4
```

### ArrayListComparatorFn<T>23+

PhonePC/2in1TabletTVWearable

type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => number

ArrayList中sort方法的回调函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| firstValue | T | 是 | 需要排序的前一项元素。 |
| secondValue | T | 是 | 需要排序的后一项元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 通过回调函数返回的值，ArrayList能够根据自定义的比较规则维护元素的顺序。 |
