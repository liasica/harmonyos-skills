---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stack
title: "@ohos.util.Stack (线性容器Stack)"
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.Stack (线性容器Stack)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d50e6624b413807f9125603e87b37252267858e7f23820cae57a53bd0f20ffd
---

Stack基于数组的数据结构实现，特点是先进后出，只能在一端进行数据的插入和删除。

Stack和[Queue](js-apis-queue.md)相比，Queue基于循环队列实现，在尾部增加元素在头部删除元素；而Stack只在一端进行插入和删除操作。

**推荐使用场景：** 一般符合先进后出的场景可以使用Stack，例如撤销/重做操作的历史记录管理、函数调用栈模拟等。

文档中使用了泛型，涉及以下泛型类型参数：

* T：Type，泛型类型参数，可以是任意类型

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了存储位置和属性，不支持自定义属性和方法。

## 导入模块

```ts
import { Stack } from '@kit.ArkTS';
```

## Stack

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | Stack的元素个数。 |

### constructor

constructor()

Stack的构造函数。调用后创建一个空的Stack实例对象，初始length为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Stack's constructor cannot be directly invoked. |

**示例：**

```ts
// 创建Stack实例
let stack = new Stack<number | string | Object>();
console.info("length:", stack.length);  // length: 0
```

### push

push(item: T): T

在栈顶插入元素，并返回该元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| item | T | 是 | 需要在栈顶插入的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回插入栈顶的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The push method cannot be bound. |

**示例：**

```ts
class PersonInfo {
  name: string = "";
  age: string = "";
  constructor(name: string, age: string) {
    this.name = name;
    this.age = age;
  }
}
// 创建支持多种类型的Stack实例
let stack = new Stack<number | string | PersonInfo>();
// 向栈中push字符串元素
console.info("push:", stack.push("a"));  // push: a
// 向栈中push数字元素
console.info("push:", stack.push(1));  //  push: 1
// 创建类实例并push到栈中
let person1: PersonInfo = new PersonInfo("Dylan", "13");
let result = stack.push(person1);
console.info("result instanceof PersonInfo:", result instanceof PersonInfo);  // result instanceof PersonInfo: true
console.info("length:", stack.length);  // length: 3
```

### pop

pop(): T

删除栈顶元素并返回，栈为空时返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回栈顶元素，栈为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The pop method cannot be bound. |

**示例：**

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
stack.push(4);
// 删除栈顶元素并返回该元素
let result = stack.pop();
console.info("result = " + result); // result = 4
```

### peek

peek(): T

返回栈顶元素，栈为空时返回undefined。调用后栈的内容不变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回栈顶元素，栈为空时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The peek method cannot be bound. |

**示例：**

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
// 查看栈顶元素，但不删除
let result = stack.peek();
console.info("result:", result);  // result: 2
```

### locate

locate(element: T): number

查找指定元素首次出现的下标值，查找失败则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 待查找的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 对应元素下标值，查找失败则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The locate method cannot be bound. |

**示例：**

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(2);
// 查找元素5首次出现的下标
let result = stack.locate(5);
console.info("result:", result);  // result: 2
```

### forEach

forEach(callbackFn: (value: T, index?: number, stack?: Stack<T>) => void, thisArg?: Object): void

按照从栈底到栈顶的顺序遍历Stack实例对象中每一个元素，对每个元素执行回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 遍历每个元素时执行的回调函数。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值。不传入时默认值为当前实例对象。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值，从0开始依次递增。默认值为0。 |
| stack | Stack<T> | 否 | 当前调用forEach方法的实例对象，默认值为当前实例对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
// 遍历stack中每个元素并执行回调函数
stack.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3
```

### isEmpty

isEmpty(): boolean

判断栈是否为空。为空返回true，不为空返回false。

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

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);
// 判断栈是否为空
let result = stack.isEmpty();
console.info("result:", result);  // result: false
```

### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，迭代器的每一项为T类型的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个迭代器，用于按栈的存储顺序依次遍历Stack中的所有元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```ts
let stack = new Stack<number>();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(4);

// 使用方法一：
for (let value of stack) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// 使用方法二：
// 创建迭代器
let iter = stack[Symbol.iterator]();
// 获取第一个迭代结果
let currentValue: IteratorResult<number> = iter.next().value;
// 循环遍历迭代器中的元素
while (currentValue != undefined) {
  console.info("value: " + currentValue);
  currentValue = iter.next().value;
}
// value: 2
// value: 4
// value: 5
// value: 4
```
