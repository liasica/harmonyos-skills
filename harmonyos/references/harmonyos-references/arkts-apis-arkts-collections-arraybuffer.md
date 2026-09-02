---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-arraybuffer
title: Class (ArrayBuffer)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Class (ArrayBuffer)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ce1bc8b56dbb433c0d6445c3c502ee4db244e24f90bf89e3a7ec78717e62386
---

ArkTS TypedArray（[Int8Array](arkts-apis-arkts-collections-int8array.md)、[Uint8Array](arkts-apis-arkts-collections-uint8array.md)、[Int16Array](arkts-apis-arkts-collections-int16array.md)、[Uint16Array](arkts-apis-arkts-collections-uint16array.md)、[Int32Array](arkts-apis-arkts-collections-int32array.md)、[Uint32Array](arkts-apis-arkts-collections-uint32array.md)、[Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md)、[Float32Array](arkts-apis-arkts-collections-float32array.md)）的底层数据结构。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

## 导入模块

```ts
import { collections } from '@kit.ArkTS';
```

## 属性

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| byteLength | number | 是 | 否 | buffer所占的字节数。 |

## constructor

constructor(byteLength: number)

构造函数，用于创建一个指定长度的ArkTS ArrayBuffer对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| byteLength | number | 是 | buffer所占的字节数，取值范围是[0, 2147483647]，否则会抛出异常。0代表构造的ArkTS ArrayBuffer的长度为0，2147483647表示构造的ArkTS ArrayBuffer的长度为2147483647。 |

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200012 | The ArrayBuffer's constructor cannot be directly invoked. |

**示例：**

```ts
let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
console.info("byteLength: " + arrayBuffer.byteLength); // byteLength: 10
```

## slice

slice(begin: number, end?: number): ArrayBuffer

返回一个新的ArkTS ArrayBuffer对象，其包含原ArkTS ArrayBuffer指定范围的内容。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| begin | number | 是 | 开始索引。如果begin < 0，则会从begin + arrayBuffer.byteLength位置开始。如果begin < -arrayBuffer.byteLength，则从0开始。 |
| end | number | 否 | 结束索引（不包括该元素）。如果end < 0，则会到end + arrayBuffer.byteLength位置结束。如果end > arrayBuffer.byteLength，则截取到arrayBuffer.byteLength位置。默认为原ArkTS ArrayBuffer的长度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | collections.ArrayBuffer |

**错误码：**

以下错误码详细介绍请参考[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200011 | The slice method cannot be bound. |
| 10200201 | Concurrent modification error. |

**示例：**

```ts
let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
let slicedBuffer: collections.ArrayBuffer = arrayBuffer.slice(0, 4);
console.info("byteLength: " + slicedBuffer.byteLength); // byteLength: 4
```
