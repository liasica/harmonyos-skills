---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-bitvector
title: Class (BitVector)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Class (BitVector)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:56+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:1e5fa448341787235797680d9d8efe3aeff8a3c74439cf55c9ea002cda646c5b
---

BitVector是一种线性数据结构，底层基于数组实现。BitVector中存储元素为bit值，能存储和处理bit级别的操作。

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

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | BitVector的元素个数。 |

## constructor

PhonePC/2in1TabletTVWearable

constructor(length: number)

BitVector的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 | 初始化BitVector的长度。 |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0); // 初始化BitVector的长度为0
```

## push

PhonePC/2in1TabletTVWearable

push(element:number): boolean

在BitVector尾部插入元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待插入的元素，0表示0，其余值表示1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 插入成功返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200011 | The push method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
```

## pop

PhonePC/2in1TabletTVWearable

pop(): number

弹出BitVector尾部的元素。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 弹出BitVector尾部的元素，其值为对应bit值。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The pop method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let res = bitVector.pop(); // bitVector: [0, 1, 0, 1]
8. console.info("bitVector pop:", res); // 0
```

## has

PhonePC/2in1TabletTVWearable

has(element: number, fromIndex: number, toIndex: number): boolean

判断范围内是否包含特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待判断的bit值，0表示0，其余值表示1。 |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 包含特定bit值返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The has method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let res0: boolean = bitVector.has(0, 1, 4);
8. console.info("bitVector has 0:", res0); // true
```

## setBitsByRange

PhonePC/2in1TabletTVWearable

setBitsByRange(element: number, fromIndex: number, toIndex: number): void

将BitVector中指定范围的元素均设为特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待设置的bit值，0表示0，其余表示1。 |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The setBitsByRange method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. bitVector.setBitsByRange(1, 1, 3); // bitVector: [0, 1, 1, 1, 0]
```

## setAllBits

PhonePC/2in1TabletTVWearable

setAllBits(element: number): void

将BitVector中所有元素均设为特定bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待设置的元素，0表示0，其余值表示1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200011 | The setAllBits method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. bitVector.setAllBits(1); // bitVector: [1, 1, 1, 1, 1]
```

## getBitsByRange

PhonePC/2in1TabletTVWearable

getBitsByRange(fromIndex: number, toIndex: number): BitVector

获取指定范围内的bit值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| BitVector | 指定范围内的bit值组成的BitVector。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The getBitsByRange method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let bitVector2 = bitVector.getBitsByRange(1, 3); // bitVector2: [1, 0]
8. console.info("bitVector2 length:", bitVector2.length); // 2
```

## resize

PhonePC/2in1TabletTVWearable

resize(size: number): void

改变BitVector的长度。

若size大于原BitVector的长度，则扩充原BitVector的长度，多出的部分其元素设置为0；

若size小于等于原BitVector的长度，则将原BitVector按size长度大小裁剪。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 需要改变的长度。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200011 | The resize method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. bitVector.resize(10); // bitVector: [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
8. console.info("bitVector get bit vector's length:", bitVector.length); // 10
9. bitVector.resize(3); // bitVector: [0, 1, 0]
10. console.info("bitVector get bit vector's length:", bitVector.length); // 3
```

## getBitCountByRange

PhonePC/2in1TabletTVWearable

getBitCountByRange(element: number, fromIndex: number, toIndex: number): number

统计指定范围内获取指定bit值的数量。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待统计的bit值，0表示0，其余值表示1。 |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 统计指定范围内获取指定bit值的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The getBitCountByRange method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let res: number = bitVector.getBitCountByRange(1, 1, 4);
8. console.info("bitVector getBitCountByRange:", res); // 2
```

## getIndexOf

PhonePC/2in1TabletTVWearable

getIndexOf(element: number, fromIndex: number, toIndex: number): number

返回指定bit值首次出现时的索引值，查找失败返回-1。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待统计的bit值，0表示0，其余值表示1。 |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定bit值首次出现时的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The getIndexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let res: number = bitVector.getIndexOf(0, 1, 4);
8. console.info("bitVector getIndexOf:", res); // 2
```

## getLastIndexOf

PhonePC/2in1TabletTVWearable

getLastIndexOf(element: number, fromIndex: number, toIndex: number): number

返回指定bit值最后一次出现时的下标值，查找失败返回-1。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| element | number | 是 | 待统计的bit值，0表示0，其余值表示1。 |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回指定bit值最后一次出现时的下标值，查找失败返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The getLastIndexOf method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let res: number = bitVector.getLastIndexOf(0, 1, 4);
8. console.info("bitVector getLastIndexOf:", res); // 2
```

## flipBitByIndex

PhonePC/2in1TabletTVWearable

flipBitByIndex(index: number): void

翻转BitVector指定索引处的bit值，0翻转为1，1翻转为0。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定索引。index < 0或者index >= length时，则会抛出错误。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of index is out of range. |
| 10200011 | The flipBitByIndex method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. bitVector.flipBitByIndex(3); // bitVector: [0, 1, 0, 0, 0]
```

## flipBitsByRange

PhonePC/2in1TabletTVWearable

flipBitsByRange(fromIndex: number, toIndex: number): void

翻转BitVector指定范围内的bit值，0翻转为1，1翻转为0。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromIndex | number | 是 | 范围起始索引，包含本索引值。fromIndex < 0或者fromIndex >= toIndex时，则会抛出错误。 |
| toIndex | number | 是 | 范围终止索引，不包含本索引值。toIndex < 0或者toIndex > length时，则会抛出错误。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The flipBitsByRange method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. bitVector.flipBitsByRange(1, 4); // bitVector: [0, 0, 1, 0, 0]
```

## values

PhonePC/2in1TabletTVWearable

values(): IterableIterator<number>

返回一个新的迭代器对象，该对象包含BitVector中每个元素的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<number> | 返回一个BitVector迭代器对象。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The values method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. let iter: IterableIterator<number> = bitVector.values();
8. let temp: IteratorResult<number> = iter.next();
9. while (!temp.done) {
10. console.info(JSON.stringify(temp.value));
11. temp = iter.next();
12. } // 依次输出 0,1,0,1,0
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
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0);

8. for (let item of bitVector) {
9. console.info("value: " + item);
10. }
```

## [index: number]

PhonePC/2in1TabletTVWearable

[index: number]: number

返回BitVector指定索引位置的元素。

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
1. let bitVector: collections.BitVector = new collections.BitVector(0);
2. bitVector.push(0);
3. bitVector.push(1);
4. bitVector.push(0);
5. bitVector.push(1);
6. bitVector.push(0); // bitVector: [0, 1, 0, 1, 0]
7. console.info("BitVector Element Index at 1: " + bitVector[1]);
```
