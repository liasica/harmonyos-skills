---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-linkedlist
title: @ohos.util.LinkedList (线性容器LinkedList)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.LinkedList (线性容器LinkedList)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4980de490c68ded3a20afe8eeabe90e4abc32984814f0eecac386f2f337cdbde
---

LinkedList底层通过双向链表实现，每个节点都包含对前一个元素和后一个元素的引用。查询元素时，可以从头或从尾部遍历，插入和删除效率高，查询效率低。LinkedList允许元素为null。

LinkedList和[List](js-apis-list.md)相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。

LinkedList和[ArrayList](js-apis-arraylist.md)相比，LinkedList插入数据效率高于ArrayList，而ArrayList查询效率高于LinkedList。

注意

在LinkedList中使用[index]的方式获取元素可能导致未定义结果，推荐使用get()方法。

**推荐使用场景：** 当需要频繁的插入删除元素且需要使用双向链表时，推荐使用LinkedList。

文档中使用了泛型，涉及以下泛型标记符：

* T： Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LinkedList } from '@kit.ArkTS';
```

## LinkedList

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | LinkedList的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

LinkedList的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The LinkedList's constructor cannot be directly invoked. |

**示例：**

```
1. let linkedList = new LinkedList<string | number | boolean | object>();
```

### add

PhonePC/2in1TabletTVWearable

add(element: T): boolean

在LinkedList尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 待插入的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 插入成功返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The add method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<string | number | boolean | object>();
2. let result = linkedList.add("a");
3. let result1 = linkedList.add(1);
4. let b = [1, 2, 3];
5. let result2 = linkedList.add(b);
6. class C {
7. name: string = ''
8. age: string = ''
9. }
10. let c: C = {name : "Dylan", age : "13"};
11. let result3 = linkedList.add(c);
12. let result4 = linkedList.add(false);
13. console.info("result = ", result4) // result =  true
```

### addFirst

PhonePC/2in1TabletTVWearable

addFirst(element: T): void

在LinkedList头部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 待插入的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The addFirst method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<string | number | boolean | object>();
2. linkedList.addFirst("a");
3. linkedList.addFirst(1);
4. let b = [1, 2, 3];
5. linkedList.addFirst(b);
6. class C {
7. name: string = ''
8. age: string = ''
9. }
10. let c: C = {name : "Dylan", age : "13"};
11. linkedList.addFirst(c);
12. linkedList.addFirst(false);
13. let result = linkedList.get(2);
14. console.info("result:", result);  // result: 1,2,3
```

### insert

PhonePC/2in1TabletTVWearable

insert(index: number, element: T): void

在长度范围内任意位置插入指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 插入位置索引。需要小于等于int32\_max即2147483647。 |
| element | T | 是 | 插入元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The insert method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<string | number | boolean | object>();
2. linkedList.insert(0, "A");
3. linkedList.insert(1, 0);
4. linkedList.insert(2, true);
5. let result = linkedList.get(1);
6. console.info("result:", result);  // result: 0
```

### has

PhonePC/2in1TabletTVWearable

has(element: T): boolean

判断LinkedList中是否包含指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

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
1. let linkedList = new LinkedList<string>();
2. linkedList.add("squirrel");
3. let result = linkedList.has("squirrel");
4. console.info("result:", result);  // result: true
```

### get

PhonePC/2in1TabletTVWearable

get(index: number): T

根据下标获取LinkedList中的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定的下标值。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 根据下标查找到的元素，元素不存在返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The get method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(1);
7. linkedList.add(2);
8. linkedList.add(4);
9. let result = linkedList.get(2);
10. console.info("result:", result);  // result: 5
```

### getLastIndexOf

PhonePC/2in1TabletTVWearable

getLastIndexOf(element: T): number

查找指定元素最后一次出现时的下标值，查找失败返回-1。

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
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(1);
7. linkedList.add(2);
8. linkedList.add(4);
9. let result = linkedList.getLastIndexOf(2);
10. console.info("result:", result);  // result: 5
```

### getIndexOf

PhonePC/2in1TabletTVWearable

getIndexOf(element: T): number

查找指定元素第一次出现时的下标值，查找失败返回-1。

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
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(1);
7. linkedList.add(2);
8. linkedList.add(4);
9. let result = linkedList.getIndexOf(2);
10. console.info("result:", result);  // result: 0
```

### removeByIndex

PhonePC/2in1TabletTVWearable

removeByIndex(index: number): T

根据元素的下标值查找元素，并将其删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定元素的下标值。需要小于等于int32\_max即2147483647。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素，如果元素为空返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The removeByIndex method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(4);
7. let result = linkedList.removeByIndex(2);
8. console.info("result:", result);  // result: 5
```

### removeFirst

PhonePC/2in1TabletTVWearable

removeFirst(): T

删除并返回LinkedList的第一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200010 | Container is empty. |
| 10200011 | The removeFirst method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(4);
7. let result = linkedList.removeFirst();
8. console.info("result:", result);  // result: 2
```

### removeLast

PhonePC/2in1TabletTVWearable

removeLast(): T

删除并返回LinkedList的最后一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200010 | Container is empty. |
| 10200011 | The removeLast method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(2);
6. linkedList.add(4);
7. let result = linkedList.removeLast();
8. console.info("result:", result);  // result: 4
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
| boolean | 删除成功返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The remove method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.remove(2);
7. console.info("result:", result);  // result: true
```

### removeFirstFound

PhonePC/2in1TabletTVWearable

removeFirstFound(element: T): boolean

删除第一次出现的指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除成功返回true，删除失败或不存在该元素时返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200010 | Container is empty. |
| 10200011 | The removeFirstFound method cannot be bound. |
| 10200017 | The element does not exist in this container. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.removeFirstFound(4);
7. console.info("result:", result);  // result: true
```

### removeLastFound

PhonePC/2in1TabletTVWearable

removeLastFound(element: T): boolean

删除最后一次出现的指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除成功返回true，删除失败或不存在该元素时返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200010 | Container is empty. |
| 10200011 | The removeLastFound method cannot be bound. |
| 10200017 | The element does not exist in this container. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.removeLastFound(4);
7. console.info("result:", result);  // result: true
```

### clone

PhonePC/2in1TabletTVWearable

clone(): LinkedList<T>

克隆一个与LinkedList相同的实例并返回。修改克隆后的实例并不会影响原实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| LinkedList<T> | 返回LinkedList对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clone method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.clone();
7. console.info("result:", result.has(4));  // result: true
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, index?: number, LinkedList?: LinkedList<T>) => void, thisArg?: Object): void

通过回调函数来遍历LinkedList实例对象上的元素以及其下标。

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
| LinkedList | LinkedList<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. linkedList.forEach((value: number, index: number) => {
7. console.info("value:" + value, "index:" + index);
8. });
9. // value:2 index:0
10. // value:4 index:1
11. // value:5 index:2
12. // value:4 index:3
```

### clear

PhonePC/2in1TabletTVWearable

clear(): void

清除LinkedList中的所有元素，并将length置为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The clear method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. linkedList.clear();
7. let result = linkedList.has(2);
8. console.info("result:", result);  // result: false
```

### set

PhonePC/2in1TabletTVWearable

set(index: number, element: T): T

替换LinkedList指定位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 查找的下标值。需要小于等于int32\_max即2147483647。 |
| element | T | 是 | 用来替换的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回替换后的元素，如果元素为空则返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The set method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number | string>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.set(2, "b");
7. console.info("result:", result);  // result: b
```

### convertToArray

PhonePC/2in1TabletTVWearable

convertToArray(): Array<T>

将当前LinkedList实例转换成数组并返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<T> | 返回转换后的数组。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The convertToArray method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.convertToArray();
7. console.info("result:", result);  // result: 2,4,5,4
```

### getFirst

PhonePC/2in1TabletTVWearable

getFirst(): T

获取LinkedList实例中的第一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回对应元素，若元素为空则返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.getFirst();
7. console.info("result:", result);  // result: 2
```

### getLast

PhonePC/2in1TabletTVWearable

getLast(): T

获取LinkedList实例中的最后一个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回对应元素，若元素为空则返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLast method cannot be bound. |

**示例：**

```
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);
6. let result = linkedList.getLast();
7. console.info("result:", result);  // result: 4
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
1. let linkedList = new LinkedList<number>();
2. linkedList.add(2);
3. linkedList.add(4);
4. linkedList.add(5);
5. linkedList.add(4);

7. // 使用方法一：
8. for (let item of linkedList) {
9. console.info("value:", item);
10. }
11. // value: 2
12. // value: 4
13. // value: 5
14. // value: 4

16. // 使用方法二：
17. let iter = linkedList[Symbol.iterator]();
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
