---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deque
title: @ohos.util.Deque (线性容器Deque)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.Deque (线性容器Deque)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7405ce8aa9c4a9200ce36812c5dccf80593523074ee8783aa3057dd6820090ca
---

Deque（double ended queue）基于循环队列的数据结构实现，支持两端元素的插入和删除，同时具备先进先出以及先进后出的特点。Deque会根据实际需要动态调整容量，每次扩容两倍。

Deque和[Queue](js-apis-queue.md)相比，Deque允许在两端执行插入和删除操作，Queue只能在头部删除元素，尾部插入元素。

与[ArrayList](js-apis-arraylist.md)相比，它们都支持在两端插入和删除元素，但Deque不支持中间插入。Deque在头部插入删除元素的效率高于ArrayList，而ArrayList随机访问元素的效率高于Deque。

**推荐使用场景：** 需要在集合两端频繁增删元素时，推荐使用Deque。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Deque } from '@kit.ArkTS';
```

## Deque

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | Deque的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Deque的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Deque's constructor cannot be directly invoked. |

**示例：**

```
1. let deque = new Deque<string | number | boolean | Object>();
```

### insertFront

PhonePC/2in1TabletTVWearable

insertFront(element: T): void

在deque头部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 插入的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The insertFront method cannot be bound. |

**示例：**

```
1. class C1 {
2. name: string = ""
3. age: string = ""
4. }

6. let deque = new Deque<string | number | boolean | Array<number> | C1>();
7. deque.insertFront("a");
8. deque.insertFront(1);
9. let b = [1, 2, 3];
10. deque.insertFront(b);
11. let c: C1 = {name : "Dylan", age : "13"};
12. deque.insertFront(c);
13. deque.insertFront(false);
14. console.info("result:", deque[0]);  // result: false
```

### insertEnd

PhonePC/2in1TabletTVWearable

insertEnd(element: T): void

在deque尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 插入的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The insertEnd method cannot be bound. |

**示例：**

```
1. class C1 {
2. name: string = ""
3. age: string = ""
4. }

6. let deque = new Deque<string | number | boolean | Array<number> | C1>();
7. deque.insertEnd("a");
8. deque.insertEnd(1);
9. let b = [1, 2, 3];
10. deque.insertEnd(b);
11. let c: C1 = {name : "Dylan", age : "13"};
12. deque.insertEnd(c);
13. deque.insertEnd(false);
14. console.info("result:", deque[0]);  // result: a
```

### has

PhonePC/2in1TabletTVWearable

has(element: T): boolean

判断此Deque中是否包含指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 指定的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果包含指定元素返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The has method cannot be bound. |

**示例：**

```
1. let deque = new Deque<string>();
2. deque.insertFront("squirrel");
3. let result = deque.has("squirrel");
4. console.info("result:", result);  // result: true
```

### popFirst

PhonePC/2in1TabletTVWearable

popFirst(): T

删除并返回双端队列的首元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回被删除的首元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The popFirst method cannot be bound. |

**示例：**

```
1. let deque = new Deque<number>();
2. deque.insertFront(2);
3. deque.insertFront(4);
4. deque.insertEnd(5);
5. deque.insertFront(2);
6. deque.insertFront(4);
7. let result = deque.popFirst();
8. console.info("result:", result);  // result: 4
```

### popLast

PhonePC/2in1TabletTVWearable

popLast(): T

删除并返回双端队列的尾元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回被删除的尾元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The popLast method cannot be bound. |

**示例：**

```
1. let deque = new Deque<number>();
2. deque.insertFront(2);
3. deque.insertEnd(6);
4. deque.insertFront(5);
5. deque.insertFront(2);
6. deque.insertFront(4);
7. let result = deque.popLast();
8. console.info("result:", result);  // result: 6
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void

在遍历Deque实例对象中每一个元素的过程中，对每个元素执行回调函数。

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
| deque | Deque<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let deque = new Deque<number>();
2. deque.insertFront(2);
3. deque.insertEnd(3);
4. deque.insertFront(1);
5. deque.insertEnd(4);
6. deque.forEach((value: number, index: number): void => {
7. console.info("value:" + value, "index:" + index);
8. });
9. /*
10. 输出结果：value:1 index:0
11. value:2 index:1
12. value:3 index:2
13. value:4 index:3
14. */
```

### getFirst

PhonePC/2in1TabletTVWearable

getFirst(): T

获取Deque实例的头元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回T类型的头元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |

**示例：**

```
1. let deque = new Deque<number>();
2. deque.insertEnd(2);
3. deque.insertEnd(4);
4. deque.insertFront(5);
5. deque.insertFront(4);
6. let result = deque.getFirst();
7. console.info("result:", result);  // result: 4
```

### getLast

PhonePC/2in1TabletTVWearable

getLast(): T

获取Deque实例的尾元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回T类型的尾元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLast method cannot be bound. |

**示例：**

```
1. let deque = new Deque<number>();
2. deque.insertFront(2);
3. deque.insertFront(4);
4. deque.insertFront(5);
5. deque.insertFront(4);
6. let result = deque.getLast();
7. console.info("result:", result);  // result: 2
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
1. let deque = new Deque<number>();
2. deque.insertFront(2);
3. deque.insertFront(4);
4. deque.insertFront(5);
5. deque.insertFront(4);

7. // 使用方法一：
8. for (let item of deque) {
9. console.info("value:" + item);
10. }
11. /*
12. 输出结果：
13. value:4
14. value:5
15. value:4
16. value:2
17. */

19. // 使用方法二：
20. let iter = deque[Symbol.iterator]();
21. let temp:IteratorResult<number> = iter.next();
22. while(!temp.done) {
23. console.info("value:" + temp.value);
24. temp = iter.next();
25. }
26. /*
27. 输出结果：
28. value:4
29. value:5
30. value:4
31. value:2
32. */
```
