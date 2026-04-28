---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint8clampedarray
title: Class (Uint8ClampedArray)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Class (Uint8ClampedArray)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1582f522a42f3b4b3fae4da8057dc46d6ffff939e01a59e839f60cede241d8ff
---

一种线性数据结构，底层基于[ArkTS ArrayBuffer](arkts-apis-arkts-collections-arraybuffer.md)实现。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { collections } from '@kit.ArkTS';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 否 | ArkTS Uint8ClampedArray底层使用的buffer。 |
| byteLength | number | 是 | 否 | ArkTS Uint8ClampedArray所占的字节数。 |
| byteOffset | number | 是 | 否 | ArkTS Uint8ClampedArray距离其ArrayBuffer起始位置的偏移。 |
| length | number | 是 | 否 | ArkTS Uint8ClampedArray元素个数。 |
| BYTES\_PER\_ELEMENT | number | 是 | 否 | ArkTS Uint8ClampedArray中每个元素所占用的字节数。 |

## constructor

PhonePC/2in1TabletTVWearable

constructor()

构造函数，用于创建一个空ArkTS Uint8ClampedArray对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The Uint8ClampedArray's constructor cannot be directly invoked. |

**示例：**

```
1. let uint8ClampedArray: collections.Uint8ClampedArray = new collections.Uint8ClampedArray();
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(length: number)

构造函数，用于创建一个指定长度的ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 用于指定ArkTS Uint8ClampedArray的长度。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The Uint8ClampedArray's constructor cannot be directly invoked. |

**示例：**

```
1. // 以长度参数构造对象
2. let uint8ClampedArray: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(12);
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(elements: Iterable<number>)

构造函数，以Iterable创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Iterable<number> | 是 | 可迭代数字集合，用于构造ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The Uint8ClampedArray's constructor cannot be directly invoked. |

**示例：**

```
1. // 从一个Iterable构造对象
2. let set: Set<number> = new Set<number>([1, 2, 3]);
3. let array: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(set);
4. // Uint8ClampedArray [1, 2, 3]
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(array: ArrayLike<number> | ArrayBuffer)

构造函数，以ArrayLike或ArkTS ArrayBuffer创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | ArrayLike<number> | ArrayBuffer | 是 | 用于构造ArkTS Uint8ClampedArray的对象。当参数类型是ArrayBuffer时buffer所占的字节数须是4的整数倍。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The Uint8ClampedArray's constructor cannot be directly invoked. |

**示例：**

```
1. // 例1 从一个ArrayLike构造对象
2. let arrayLike = [1, 3, 5];
3. let array: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(arrayLike);
```

```
1. // 例2 从一个ArrayBuffer构造对象
2. let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(12);
3. let array: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(arrayBuffer);
```

```
1. // 例3 从另一ArkTS Uint8ClampedArray构造对象
2. let arrayLike = [1, 3, 5];
3. // uint8ClampedArray1 [1, 3, 5]
4. let uint8ClampedArray1: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(arrayLike);
5. // uint8ClampedArray2 [1, 3, 5]
6. let uint8ClampedArray2: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(uint8ClampedArray1);
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(buffer: ArrayBuffer, byteOffset?: number, length?: number)

构造函数，以ArrayBuffer创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | 是 | 用于构造ArkTS Uint8ClampedArray的ArrayBuffer对象。buffer所占的字节数须是4的整数倍。 |
| byteOffset | number | 否 | 指定buffer的字节偏移，从0开始，默认为0。 |
| length | number | 否 | 指定ArkTS Uint8ClampedArray的长度，默认为0。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200012 | The Uint8ClampedArray's constructor cannot be directly invoked. |

**示例：**

```
1. let uint8ClampedArray: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5, 6]);
2. console.info("byteLength: " + uint8ClampedArray.buffer.byteLength); // byteLength: 6
3. // 从uint8ClampedArray对应buffer第1个字节开始，长度为5
4. let uint8ClampedArray1: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(uint8ClampedArray.buffer, 1, 5);
5. console.info("[" + uint8ClampedArray1 + "]"); // [2, 3, 4, 5, 6]
```

## from

PhonePC/2in1TabletTVWearable

static from(arrayLike: ArrayLike<number>): Uint8ClampedArray

从一个ArrayLike或者可迭代对象中创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | ArrayLike<number> | 是 | 用于构造ArkTS Uint8ClampedArray的ArrayLike对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新创建的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. let arrayLike = [1, 3, 5];
2. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from(arrayLike); // array [1, 3, 5]
```

## from

PhonePC/2in1TabletTVWearable

static from<T>(arrayLike: ArrayLike<T>, mapFn: TypedArrayFromMapFn<T, number>): Uint8ClampedArray

从一个ArrayLike中创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | ArrayLike<T> | 是 | 用于构造ArrayLike对象。 |
| mapFn | [TypedArrayFromMapFn](arkts-apis-arkts-collections-types.md#typedarrayfrommapfn)<T, number> | 是 | 映射函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新创建的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. // 例1 从一个对象创建
2. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from<number>(
3. { length: 5 }, (v: Object, k: number) => k);
4. // Uint8ClampedArray [0, 1, 2, 3, 4]
```

```
1. // 例2 从一个字符数组创建
2. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from<string>(
3. ["1", "3", "5"], (v: string, k: number) => parseInt(v));
4. // Uint8ClampedArray [1, 3, 5]
```

```
1. // 例3 从一个字符串创建
2. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from<string>(
3. "12345", (v: string, k: number) => parseInt(v));
4. // Uint8ClampedArray [1, 2, 3, 4, 5]
```

## from

PhonePC/2in1TabletTVWearable

static from(arrayLike: Iterable<number>, mapFn?: TypedArrayFromMapFn<number, number>): Uint8ClampedArray

从一个可迭代对象中创建一个ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | Iterable<number> | 是 | 用于构造的可迭代对象。 |
| mapFn | [TypedArrayFromMapFn](arkts-apis-arkts-collections-types.md#typedarrayfrommapfn)<number, number> | 否 | 映射函数。如果省略，则不对元素进行加工处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新创建的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. // 例1 不指定映射函数
2. let set: Set<number> = new Set<number>([1, 2, 3]);
3. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from(set);
4. // Uint8ClampedArray [1, 2, 3]
```

```
1. // 例2 指定映射函数
2. let set: Set<number> = new Set<number>([1, 2, 3]);
3. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from(
4. set, (v: number, k: number) => v + k);
5. // Uint8ClampedArray [1, 3, 5]
```

## of18+

PhonePC/2in1TabletTVWearable

static of(...items: number[]): Uint8ClampedArray

通过可变数量的参数创建一个新的ArkTS Uint8ClampedArray对象，参数个数可以是0个、1个或者多个。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | number[] | 否 | 用于创建数组的元素，参数个数可以是0个、1个或者多个。默认值为空数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新的ArkTS Uint8ClampedArray实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error: Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**示例：**

```
1. let arr: collections.Uint8ClampedArray = collections.Uint8ClampedArray.of(1, 2, 3, 4);
2. console.info(arr.toString()); // 预期输出：1,2,3,4
```

## toString18+

PhonePC/2in1TabletTVWearable

toString(): string

ArkTS Uint8ClampedArray转换为字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 一个包含数组所有元素的字符串。 |

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The toString method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array = new collections.Uint8ClampedArray([1, 2, 3, 4, 5]);
2. let stringArray = array.toString();
3. console.info(stringArray); // 预期输出：1,2,3,4,5
```

## toLocaleString18+

PhonePC/2in1TabletTVWearable

toLocaleString(): string

根据当前应用的系统地区获取符合当前文化习惯的数字表示形式，让每个元素调用自己的toLocaleString方法把数字转换为字符串，然后使用逗号将每个元素的结果字符串按照顺序拼接成字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 一个包含数组所有元素的字符串。 |

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The toLocaleString method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. // 当前应用所在系统为法国地区
2. let array = new collections.Uint8ClampedArray([100, 110, 120]);
3. let stringArray = array.toLocaleString();
4. console.info(stringArray); // 预期输出：100,110,120
```

## copyWithin

PhonePC/2in1TabletTVWearable

copyWithin(target: number, start: number, end?: number): Uint8ClampedArray

从ArkTS Uint8ClampedArray指定范围内的元素依次拷贝到目标位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | number | 是 | 目标起始位置的下标，如果target < 0，则会从target + array.length位置开始。 |
| start | number | 是 | 源起始位置下标，如果start < 0，则会从start + Uint8ClampedArray.length位置开始。 |
| end | number | 否 | 源终止位置下标（不包含end位置的元素），如果end < 0，则会从end + Uint8ClampedArray.length位置终止。默认为ArkTS Uint8ClampedArray的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 修改后的Uint8ClampedArray。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The copyWithin method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5, 6, 7, 8]);
2. let copied: collections.Uint8ClampedArray = array.copyWithin(3, 1, 3);
3. // Uint8ClampedArray [1, 2, 3, 2, 3, 6, 7, 8]
```

## some

PhonePC/2in1TabletTVWearable

some(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean

测试ArkTS Uint8ClampedArray中的是否存在元素满足指定条件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-apis-arkts-collections-types.md#typedarraypredicatefn)<number, Uint8ClampedArray> | 是 | 用于测试的断言函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果存在元素满足指定条件返回true，否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The some method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let arrayLike = [10, 20, 30, 40, 50];
2. let uint8ClampedArray: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(arrayLike);
3. uint8ClampedArray.some((element: number) => element < 1); // false
```

## every

PhonePC/2in1TabletTVWearable

every(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): boolean

测试ArkTS Uint8ClampedArray中的所有元素是否满足指定条件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-apis-arkts-collections-types.md#typedarraypredicatefn)<number, Uint8ClampedArray> | 是 | 用于测试的断言函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果所有元素都满足指定条件则返回true，否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The every method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let arrayLike = [10, 20, 30, 40, 50];
2. let uint8ClampedArray: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(arrayLike);
3. uint8ClampedArray.every((element: number) => element > 10);  // false
```

## fill

PhonePC/2in1TabletTVWearable

fill(value: number, start?: number, end?: number): Uint8ClampedArray

使用特定值填充ArkTS Uint8ClampedArray指定范围的全部元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 待填充的值。 |
| start | number | 否 | 开始填充的索引，如果start < 0，则会从start + Uint8ClampedArray.length位置开始。默认值为0。 |
| end | number | 否 | 结束填充的索引（不包括该元素），如果end < 0，则会到end + Uint8ClampedArray.length位置结束。默认为ArkTS Uint8ClampedArray的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 填充后的Uint8ClampedArray。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The fill method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let arrayLike = [1, 2, 3];
2. new collections.Uint8ClampedArray(arrayLike).fill(4); // Uint8ClampedArray [4, 4, 4]
3. new collections.Uint8ClampedArray(arrayLike).fill(4, 1); // Uint8ClampedArray [1, 4, 4]
4. new collections.Uint8ClampedArray(arrayLike).fill(4, 1, 2); // Uint8ClampedArray [1, 4, 3]
```

## filter

PhonePC/2in1TabletTVWearable

filter(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): Uint8ClampedArray

返回一个新ArkTS Uint8ClampedArray，其包含满足指定条件的所有元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-apis-arkts-collections-types.md#typedarraypredicatefn)<number, Uint8ClampedArray> | 是 | 用于元素过滤的断言函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 过滤后的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The filter method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([0, 1, 2, 3, 4]);
2. let filtered: collections.Uint8ClampedArray = array.filter((element: number) => element % 2 == 0);
3. // Uint8ClampedArray [0, 2, 4]
```

## find

PhonePC/2in1TabletTVWearable

find(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number | undefined

返回ArkTS Uint8ClampedArray中第一个满足指定条件的元素的值，如果所有元素都不满足，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-apis-arkts-collections-types.md#typedarraypredicatefn)<number, Uint8ClampedArray> | 是 | 用于元素查找的断言函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | undefined | 第一个满足条件的元素的值；如果所有元素都不满足条件，则返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The find method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([0, 1, 2, 3, 4]);
2. array.find((element: number) => element > 2); // 3
3. array.find((element: number) => element > 4); // undefined
```

## findIndex

PhonePC/2in1TabletTVWearable

findIndex(predicate: TypedArrayPredicateFn<number, Uint8ClampedArray>): number

返回ArkTS Uint8ClampedArray中第一个满足指定条件的元素索引，如果所有元素都不满足，则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | [TypedArrayPredicateFn](arkts-apis-arkts-collections-types.md#typedarraypredicatefn)<number, Uint8ClampedArray> | 是 | 用于元素查找的断言函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 第一个满足条件的元素索引；如果所有元素都不满足条件，则返回-1。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The findIndex method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. const array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let foundIndex: number = array.findIndex((element: number) => element % 2 === 0); // 1
```

## forEach

PhonePC/2in1TabletTVWearable

forEach(callbackFn: TypedArrayForEachCallback<number, Uint8ClampedArray>): void

对ArkTS Uint8ClampedArray中的每个元素执行提供的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayForEachCallback](arkts-apis-arkts-collections-types.md#typedarrayforeachcallback)<number, Uint8ClampedArray> | 是 | 用于对每个元素执行的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The forEach method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let uint8ClampedArray: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3]);
2. uint8ClampedArray.forEach((value: number, index: number, array: collections.Uint8ClampedArray) => {
3. console.info(`Element ${value} at index ${index}`);
4. });
```

## indexOf

PhonePC/2in1TabletTVWearable

indexOf(searchElement: number, fromIndex?: number): number

返回在ArkTS Uint8ClampedArray中给定元素的第一个索引，如果不存在，则返回-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | number | 是 | 待索引的值。 |
| fromIndex | number | 否 | 搜索的起始下标。默认值为0。如果下标大于等于ArkTS Uint8ClampedArray的长度，则返回-1。如果提供的下标值是负数，则被当做距离数组尾部的偏移，从前到后搜索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 数组中元素的第一个索引；没有找到，则返回-1。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The indexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([3, 5, 9]);
2. array.indexOf(3); // 0
3. array.indexOf(7); // -1
4. array.indexOf(9, 2); // 2
5. array.indexOf(9, -2); // 2
```

## lastIndexOf18+

PhonePC/2in1TabletTVWearable

lastIndexOf(searchElement: number, fromIndex?: number): number

返回ArkTS Uint8ClampedArray实例中最后一次出现searchElement的索引，如果对象不包含，则为-1。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | number | 是 | 待索引的值。 |
| fromIndex | number | 否 | 搜索的起始下标。默认值为0。如果下标大于等于ArkTS Uint8ClampedArray的长度，则返回-1。如果提供的下标值是负数，则被当做距离数组尾部的偏移，从后到前搜索。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 数组中给定元素的最后一个索引；没有找到，则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The lastIndexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([3, 5, 9]);
2. console.info(array.lastIndexOf(3) + ''); // 预期输出：0
3. console.info(array.lastIndexOf(7) + ''); // 预期输出：-1
4. console.info(array.lastIndexOf(9, 2) + ''); // 预期输出：2
5. console.info(array.lastIndexOf(9, -2) + ''); // 预期输出：-1
```

## join

PhonePC/2in1TabletTVWearable

join(separator?: string): string

将ArkTS Uint8ClampedArray的所有元素拼接成一个字符串，元素之间使用指定的分隔符分隔。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 分隔字符串。如果省略，则使用逗号分隔。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 包含所有元素拼接成的字符串。如果ArkTS Uint8ClampedArray为空，则返回空字符串。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The join method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let joined: string = array.join('-'); // "1-2-3-4-5"
```

## map

PhonePC/2in1TabletTVWearable

map(callbackFn: TypedArrayMapCallback<number, Uint8ClampedArray>): Uint8ClampedArray

对ArkTS Uint8ClampedArray中的每个元素应用指定的回调函数，并使用结果创建一个新的ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayMapCallback](arkts-apis-arkts-collections-types.md#typedarraymapcallback)<number, Uint8ClampedArray> | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The map method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([25, 36, 49]);
2. const mapped: collections.Uint8ClampedArray = array.map(Math.sqrt); // Uint8ClampedArray [5, 6 ,7]
```

## reduce

PhonePC/2in1TabletTVWearable

reduce(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number

对ArkTS Uint8ClampedArray中的每个元素执行归约函数，并返回最终的归约结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-apis-arkts-collections-types.md#typedarrayreducecallback)<number, number, Uint8ClampedArray> | 是 | 归约函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 由归约函数返回的结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The reduce method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let reducedValue: number = array.reduce((accumulator: number, value: number) => accumulator + value);
3. // reducedValue == 15
```

## reduceRight18+

PhonePC/2in1TabletTVWearable

reduceRight(callbackFn: TypedArrayReduceCallback<number, number, Uint8ClampedArray>): number

反向遍历ArkTS Uint8ClampedArray，对ArkTS Uint8ClampedArray中的每个元素执行归约函数，并返回最终的归约结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-apis-arkts-collections-types.md#typedarrayreducecallback)<number, number, Uint8ClampedArray> | 是 | 归约函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 由归约函数返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 10200011 | The reduceRight method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let reducedValue: number = array.reduceRight((accumulator: number, value: number) => accumulator + value);
3. console.info(reducedValue + ''); // 预期输出： 15
```

## reduce

PhonePC/2in1TabletTVWearable

reduce<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U

对ArkTS Uint8ClampedArray中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-apis-arkts-collections-types.md#typedarrayreducecallback)<U, number, Uint8ClampedArray> | 是 | 归约函数。 |
| initialValue | U | 是 | 初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 由归约函数返回的结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The reduce method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let reducedValue: number = array.reduce((accumulator: number, value: number) => accumulator + value, 1);
3. // reducedValue == 16
```

## reduceRight18+

PhonePC/2in1TabletTVWearable

reduceRight<U = number>(callbackFn: TypedArrayReduceCallback<U, number, Uint8ClampedArray>, initialValue: U): U

反向遍历ArkTS Uint8ClampedArray，对ArkTS Uint8ClampedArray中的每个元素执行归约函数，且接收一个初始值作为归约函数首次调用的参数，并返回最终的归约结果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackFn | [TypedArrayReduceCallback](arkts-apis-arkts-collections-types.md#typedarrayreducecallback)<U, number, Uint8ClampedArray> | 是 | 归约函数。 |
| initialValue | U | 是 | 初始值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U | 由归约函数返回的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 10200011 | The reduceRight method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let reducedValue: number = array.reduceRight((accumulator: number, value: number) => accumulator + value, 1);
3. console.info(reducedValue + ''); // 预期输出： 16
```

## reverse

PhonePC/2in1TabletTVWearable

reverse(): Uint8ClampedArray

反转ArkTS Uint8ClampedArray。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 反转后的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The reverse method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let reversed: collections.Uint8ClampedArray = array.reverse(); // Uint8ClampedArray [5, 4, 3, 2, 1]
```

## set

PhonePC/2in1TabletTVWearable

set(array: ArrayLike<number>, offset?: number): void

将传入的ArrayLike元素依次写入到指定的起始位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | ArrayLike<number> | 是 | 用于设置的ArrayLike对象。 |
| offset | number | 否 | 写入的起始位置。默认为0。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The set method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let buffer: collections.ArrayBuffer = new collections.ArrayBuffer(8);
2. let array: collections.Uint8ClampedArray = new collections.Uint8ClampedArray(buffer);
3. array.set([1, 2, 3], 3); // Uint8ClampedArray [0, 0, 0, 1, 2, 3, 0, 0]
```

## slice

PhonePC/2in1TabletTVWearable

slice(start?: number, end?: number): Uint8ClampedArray

返回一个新的ArkTS Uint8ClampedArray对象，其包含原ArkTS Uint8ClampedArray指定范围的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 | 开始索引，如果start < 0，则会从start + Uint8ClampedArray.length位置开始。默认为0。 |
| end | number | 否 | 结束索引（不包括该元素），如果end < 0，则会到end + Uint8ClampedArray.length位置结束。默认为ArkTS Uint8ClampedArray的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The slice method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. array.slice(); // Uint8ClampedArray [1, 2, 3, 4, 5]
3. array.slice(1, 3); // Uint8ClampedArray [2, 3]
4. array.slice(-2); // Uint8ClampedArray [4, 5]
```

## sort

PhonePC/2in1TabletTVWearable

sort(compareFn?: TypedArrayCompareFn<number>): Uint8ClampedArray

对ArkTS Uint8ClampedArray进行排序，并返回排序后的ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| compareFn | [TypedArrayCompareFn](arkts-apis-arkts-collections-types.md#typedarraycomparefn)<number> | 否 | 用于确定元素顺序的函数。默认使用升序排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 排序后的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The sort method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 3, 5, 4, 2]);
2. array.sort(); // Uint8ClampedArray [1, 2, 3, 4, 5]
3. array.sort((a: number, b: number) => a - b); // Uint8ClampedArray [1, 2, 3, 4, 5]
4. array.sort((a: number, b: number) => b - a); // Uint8ClampedArray [5, 4, 3, 2, 1]
```

## subarray

PhonePC/2in1TabletTVWearable

subarray(begin?: number, end?: number): Uint8ClampedArray

从指定的位置截取数组，返回一个新的、基于相同ArkTS ArrayBuffer的ArkTS Uint8ClampedArray对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 否 | 开始索引，如果begin < 0，则会从begin + Uint8ClampedArray.length位置开始。默认值为0。 |
| end | number | 否 | 结束索引（不包括该元素），如果end < 0，则会到end + Uint8ClampedArray.length位置结束。默认为ArkTS Uint8ClampedArray的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8ClampedArray | 新的ArkTS Uint8ClampedArray对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The subarray method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let subArray: collections.Uint8ClampedArray = array.subarray(); // Uint8ClampedArray [1, 2, 3, 4, 5]
3. subArray.set([10, 20, 30]); // Uint8ClampedArray [10, 20, 30, 4, 5]
```

## at

PhonePC/2in1TabletTVWearable

at(index: number): number | undefined

返回指定下标的元素，如果不存在，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要返回的Array元素的索引（从零开始），取值为整数。如果index < 0，则会访问index + Uint8ClampedArray.length位置的元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | undefined | 指定下标的元素；如果不存在，则返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The at method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. console.info("element: " + array.at(2));  // element: 3
3. console.info("element: " + array.at(-1)); // element: 5
4. console.info("element: " + array.at(6));  // element: undefined
```

## includes

PhonePC/2in1TabletTVWearable

includes(searchElement: number, fromIndex?: number): boolean

判断ArkTS Uint8ClampedArray是否包含特定元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchElement | number | 是 | 待搜索的元素。 |
| fromIndex | number | 否 | 开始搜索的索引，如果fromIndex < 0，则会从fromIndex + Uint8ClampedArray.length位置开始。默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果ArkTS Uint8ClampedArray包含指定的元素，则返回true；否则返回false。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 10200011 | The includes method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3]);
2. console.info("includes: " + array.includes(2));    // includes: true
3. console.info("includes: " + array.includes(4));    // includes: false
4. console.info("includes: " + array.includes(3, 3)); // includes: false
```

## entries

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[number, number]>

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[number, number]> | 新的迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The entries method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([11, 22, 33]);
2. let iterator: IterableIterator<[number, number]> = array.entries();
3. console.info("value: " + iterator.next().value); // value: 0,11
4. console.info("value: " + iterator.next().value); // value: 1,22
5. console.info("value: " + iterator.next().value); // value: 2,33
```

## keys

PhonePC/2in1TabletTVWearable

keys(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的键（下标）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 新的迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The keys method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let iterator: IterableIterator<number> = array.keys();
3. for (const key of iterator) {
4. console.info("" + key); // 依次输出 0,1,2,3,4
5. }
```

## values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含ArkTS Uint8ClampedArray中每个元素的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 新的迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let array: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5]);
2. let iterator: IterableIterator<number> = array.values();
3. for (const value of iterator) {
4. console.info("" + value); // 依次输出 1,2,3,4,5
5. }
```

## [Symbol.iterator]

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<number>

返回一个迭代器，迭代器的每一项都是一个 JavaScript 对象，并返回该对象。

说明

本接口不支持在.ets文件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 返回一个迭代器。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**示例：**

```
1. let uint8ClampedArray: collections.Uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 3, 4, 5, 6]);

3. for (let item of uint8ClampedArray) {
4. console.info(`value : ${item}`);
5. }
```

## [index: number]

PhonePC/2in1TabletTVWearable

[index: number]: number

返回Uint8ClampedArray指定索引位置的元素。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 所需代码单元的从零开始的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回number数据类型。 |

**示例：**

```
1. let uint8ClampedArray = collections.Uint8ClampedArray.from([1, 2, 4]);
2. console.info("Element at index 1: ", uint8ClampedArray[1]);
```
