---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-queue
title: @ohos.util.Queue (线性容器Queue)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.Queue (线性容器Queue)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:10+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:e60bec51a834a69d81fb53095bfa4e543fb51579da38bebe8b9d1a52adeec0b0
---

Queue的特点是先进先出，在尾部增加元素，在头部删除元素。根据循环队列的数据结构实现。

Queue和[Deque](js-apis-deque.md)相比，Queue在尾部增加元素，在头部删除元素；而Deque支持在两端进行增删操作。

**推荐使用场景：** 一般符合先进先出的场景可以使用Queue。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Queue } from '@kit.ArkTS';
```

## Queue

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | Queue的元素个数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

Queue的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Queue's constructor cannot be directly invoked. |

**示例：**

```
1. let queue = new Queue<number | string | Object>();
```

### add

PhonePC/2in1TabletTVWearable

add(element: T): boolean

在队列尾部插入元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 要插入的元素。 |

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
1. class C1 {
2. name: string = ""
3. age: string = ""
4. }
5. let queue = new Queue<number | string | C1 | number[]>();
6. let result = queue.add("a");
7. let result1 = queue.add(1);
8. let b = [1, 2, 3];
9. let result2 = queue.add(b);
10. let c : C1 = {name : "Dylan", age : "13"};
11. let result3 = queue.add(c);
12. console.info("result:", queue.length);  // result: 4
```

### pop

PhonePC/2in1TabletTVWearable

pop(): T

删除头元素并返回该删除元素。

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
| 10200011 | The pop method cannot be bound. |

**示例：**

```
1. let queue = new Queue<number>();
2. queue.add(2);
3. queue.add(4);
4. queue.add(5);
5. queue.add(2);
6. queue.add(4);
7. let result = queue.pop();
8. console.info("result:", result);  // result: 2
```

### getFirst

PhonePC/2in1TabletTVWearable

getFirst(): T

获取队列的头元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回获取的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |

**示例：**

```
1. let queue = new Queue<number>();
2. queue.add(2);
3. queue.add(4);
4. queue.add(5);
5. queue.add(2);
6. let result = queue.getFirst();
7. console.info("result:", result);  // result: 2
```

### forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void, thisArg?: Object): void

在遍历Queue实例对象中每一个元素的过程中，对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 回调函数。 |
| thisArg | Object | 否 | callbackfn被调用时用作this值，默认值为当前实例对象。 |

callbackfn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值，默认值为0。 |
| Queue | Queue<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```
1. let queue = new Queue<number>();
2. queue.add(2);
3. queue.add(4);
4. queue.add(5);
5. queue.add(4);
6. queue.forEach((value: number, index: number): void => {
7. console.info("value:" + value, "index:" + index);
8. });
9. // value:2 index:0
10. // value:4 index:1
11. // value:5 index:2
12. // value:4 index:3
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
1. let queue = new Queue<number>();
2. queue.add(2);
3. queue.add(4);
4. queue.add(5);
5. queue.add(4);

7. // 使用方法一：
8. for (let value of queue) {
9. console.info("value:", value);
10. }
11. // value: 2
12. // value: 4
13. // value: 5
14. // value: 4

16. // 使用方法二：
17. let iter = queue[Symbol.iterator]();
18. let temp: IteratorResult<number> = iter.next().value;
19. while(temp != undefined) {
20. console.info("value: " + temp);
21. temp = iter.next().value;
22. }
23. // value: 2
24. // value: 4
25. // value: 5
26. // value: 4
```
