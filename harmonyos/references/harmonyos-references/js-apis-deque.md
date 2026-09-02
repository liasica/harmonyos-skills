---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deque
title: "@ohos.util.Deque (线性容器Deque)"
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.Deque (线性容器Deque)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7fd3bb282ae48a4fc72b751b77a23778d33502b09f34bb977a85c2e0c471727
---

Deque（double-ended queue）基于循环队列的数据结构实现，支持两端元素的插入和删除。Deque同时具备先进先出以及先进后出的特点，可根据操作端的不同同时作为队列和栈使用。当现有容量不足以容纳新插入的元素时，Deque会动态调整容量，每次扩容两倍，无需手动预设容量。

Deque和[Queue](js-apis-queue.md)相比，Deque允许在两端执行插入和删除操作，Queue只能在头部删除元素，尾部插入元素。

与[ArrayList](js-apis-arraylist.md)相比，它们都支持在两端插入和删除元素，但Deque不支持中间插入。Deque在头部插入删除元素的效率高于ArrayList，而ArrayList随机访问元素的效率高于Deque。

**推荐使用场景：** 需要在集合两端频繁增删元素时，推荐使用Deque。

文档中使用了泛型，涉及以下泛型标记符：

* T：Type，类型

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

容器类使用静态语言实现，限制了内部存储方式和所支持的属性，不支持自定义属性和方法。

## 导入模块

```ts
import { Deque } from '@kit.ArkTS';
```

## Deque

### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | Deque的元素个数。 |

### constructor

constructor()

Deque的构造函数，用于创建一个基于循环队列数据结构的空Deque实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Deque's constructor cannot be directly invoked. |

**示例：**

```ts
// 创建Deque实例
let deque = new Deque<string | number | boolean | Object>();
```

### insertFront

insertFront(element: T): void

在Deque头部插入元素。插入成功后Deque的元素个数增加1。Deque在头部插入元素的效率高于ArrayList。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 在头部插入的元素，类型需与Deque实例化时指定的泛型类型T一致。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The insertFront method cannot be bound. |

**示例：**

```ts
class PersonInfo {
  name: string = "";
  age: string = "";
}

// 创建支持多种类型的Deque实例
let deque = new Deque<string | number | boolean | Array<number> | PersonInfo>();
// 在头部插入字符串元素
deque.insertFront("a");
// 在头部插入数字元素
deque.insertFront(1);
let numArray = [1, 2, 3];
deque.insertFront(numArray);
let person: PersonInfo = {name : "Dylan", age : "13"};
deque.insertFront(person);
deque.insertFront(false);
console.info("result:", deque[0]);  // result: false
```

### insertEnd

insertEnd(element: T): void

在Deque尾部插入元素。插入成功后Deque的元素个数增加1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 在尾部插入的元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The insertEnd method cannot be bound. |

**示例：**

```ts
class PersonInfo {
  name: string = "";
  age: string = "";
}

// 创建支持多种类型的Deque实例
let deque = new Deque<string | number | boolean | Array<number> | PersonInfo>();
// 在尾部插入字符串元素
deque.insertEnd("a");
// 在尾部插入数字元素
deque.insertEnd(1);
let numArray = [1, 2, 3];
deque.insertEnd(numArray);
let person: PersonInfo = {name : "Dylan", age : "13"};
deque.insertEnd(person);
deque.insertEnd(false);
console.info("result:", deque[0]);  // result: a
```

### has

has(element: T): boolean

判断此Deque中是否包含指定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | T | 是 | 要在Deque中查找的指定元素，用于判断Deque是否包含该元素。类型需与Deque实例化时指定的泛型类型T一致。 |

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

```ts
// 创建Deque实例
let deque = new Deque<string>();
// 在头部插入元素
deque.insertFront("squirrel");
// 判断Deque中是否包含指定元素
let result = deque.has("squirrel");
console.info("result:", result);  // result: true
```

### popFirst

popFirst(): T

删除并返回Deque的首元素。删除成功后Deque的元素个数减少1。Deque在头部删除元素的效率高于ArrayList。

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

```ts
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertEnd(5);
deque.insertFront(2);
deque.insertFront(4);
// 删除并返回双端队列的首元素
let result = deque.popFirst();
console.info("result:", result);  // result: 4
```

### popLast

popLast(): T

删除并返回Deque的尾元素。删除成功后Deque的元素个数减少1。

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

```ts
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(6);
deque.insertFront(5);
deque.insertFront(2);
deque.insertFront(4);
// 删除并返回双端队列的尾元素
let result = deque.popLast();
console.info("result:", result);  // result: 6
```

### forEach

forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void

通过回调函数遍历Deque实例中的每个元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | function | 是 | 遍历每个元素时执行的回调函数，执行时的this值可通过thisArg参数指定。在回调函数执行过程中，不建议修改Deque（如插入或删除元素），否则可能导致遍历行为异常。 |
| thisArg | Object | 否 | callbackFn被调用时用作this值。当需要改变回调函数中的this指向时传入此参数；不传入时默认值为当前实例对象。 |

callbackFn的参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 当前遍历到的元素。 |
| index | number | 否 | 当前遍历到的下标值，从0开始递增。 |
| deque | [Deque](js-apis-deque.md#deque)<T> | 否 | 当前调用forEach方法的实例对象，即正在遍历的Deque实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The forEach method cannot be bound. |

**示例：**

```ts
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(3);
deque.insertFront(1);
deque.insertEnd(4);
// 使用forEach遍历Deque中每个元素并执行回调函数
deque.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
/*
输出结果：value:1 index:0
         value:2 index:1
         value:3 index:2
         value:4 index:3
 */
```

### getFirst

getFirst(): T

获取Deque实例的头元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回首元素，请使用popFirst。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回Deque实例的头元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getFirst method cannot be bound. |

**示例：**

```ts
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertEnd(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertFront(4);
// 获取Deque的头元素
let result = deque.getFirst();
console.info("result:", result);  // result: 4
```

### getLast

getLast(): T

获取Deque实例的尾元素，不删除该元素。调用后，Deque的内容和长度不变。如需删除并返回尾元素，请使用popLast。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回Deque实例的尾元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The getLast method cannot be bound. |

**示例：**

```ts
// 创建Deque实例并插入元素
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);
// 获取Deque的尾元素
let result = deque.getLast();
console.info("result:", result);  // result: 2
```

### [Symbol.iterator]

[Symbol.iterator](): IterableIterator<T>

返回一个迭代器，按插入顺序遍历Deque中的元素，迭代器每项为T类型的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<T> | 返回一个迭代器，用于遍历Deque实例中的所有元素。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```ts
let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);

// 使用方法一：
for (let item of deque) {
  console.info("value:" + item);
}
/*
输出结果：
value:4
value:5
value:4
value:2
 */

// 使用方法二：
let iter = deque[Symbol.iterator]();
let iterResult: IteratorResult<number> = iter.next();
while (!iterResult.done) {
  console.info("value:" + iterResult.value);
  iterResult = iter.next();
}
/*
输出结果：
value:4
value:5
value:4
value:2
 */
```
