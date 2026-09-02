---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-queue
title: "@ohos.util.Queue (线性容器Queue)"
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.Queue (线性容器Queue)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:db6c7e7192020a095920d45733e60e79b1decc87c5a2c219826a41331f2d7cb6
---

Queue遵循先进先出原则：在尾部增加元素，在头部删除元素。Queue基于循环队列的数据结构实现。

Queue和[Deque](js-apis-deque.md)相比，Queue在尾部增加元素，在头部删除元素；而Deque支持在两端进行增删操作。

**推荐使用场景：** 一般符合先进先出的场景可以使用Queue。

文档中使用了泛型，涉及以下泛型类型参数：

* T：Type，泛型类型参数，可以是任意类型

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

```ts
import { Queue } from '@kit.ArkTS';
```

## Queue

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | Queue的元素个数。 |

### constructor

constructor()

Queue的构造函数，创建一个新的Queue实例，初始长度为0。Queue容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Queue's constructor cannot be directly invoked. |

**示例：**

```ts
// 创建Queue实例
let queue = new Queue<number | string | Object>();
console.info("queue length:", queue.length);  // queue length: 0
```

### add

add(element: T): boolean

在队列尾部插入元素，插入成功则返回true，队列长度增加，否则返回false。

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

```ts
class PersonInfo {
  name: string = "";
  age: string = "";
}
// 创建支持多种类型的Queue实例
let queue = new Queue<number | string | PersonInfo | number[]>();
// 向队列尾部添加元素
queue.add("a");
queue.add(1);
let b = [1, 2, 3];
queue.add(b);
let c : PersonInfo = {name : "Dylan", age : "13"};
queue.add(c);
console.info("result:", queue.length);  // result: 4
```

### pop

pop(): T

删除队列头部元素，并返回被删除元素。当Queue为空时，返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回删除的元素。当Queue为空时，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The pop method cannot be bound. |

**示例：**

```ts
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
queue.add(4);
// 删除队列头部元素，并返回被删除元素
let result = queue.pop();
console.info("result:", result);  // result: 2
```

### getFirst

getFirst(): T

获取队列的头元素（不会删除队列的头元素）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回队列的头元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |

**示例：**

```ts
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(2);
// 获取队列的头元素
let result = queue.getFirst();
console.info("result:", result);  // result: 2
```

### forEach

forEach(callbackFn: (value: T, index?: number, Queue?: Queue<T>) => void, thisArg?: Object): void

在遍历Queue实例中的每个元素，并对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 对每个元素执行的回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值，默认值为当前实例对象。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值，未指定时默认从0开始遍历。 |
| Queue | Queue<T> | 否 | 当前调用forEach方法的实例对象，未指定时取当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```ts
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);
// 遍历Queue中的每个元素，对每个元素执行回调函数
queue.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，每一项为T类型的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个迭代器，用于遍历Queue中的所有元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```ts
let queue = new Queue<number>();
queue.add(2);
queue.add(4);
queue.add(5);
queue.add(4);

// 使用方法一：
for (let value of queue) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
// 获取Queue的迭代器
let iter = queue[Symbol.iterator]();
// 通过迭代器的next方法遍历元素
let temp: IteratorResult<number> = iter.next().value;
while(temp != undefined) {
  console.info("value: " + temp);
  temp = iter.next().value;
}
// value: 2
// value: 4
// value: 5
// value: 4
```
