---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-types
title: Types
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.collections (ArkTS容器集) > Types
category: harmonyos-references
scraped_at: 2026-04-28T07:59:56+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:2390182c60227f1f507c0db53f06e112b17be494702c440d1109ceba7d775f5d
---

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## ISendable

PhonePC/2in1TabletTVWearable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](js-apis-arkts-lang.md#langisendable) | 所有Sendable类型的父类型。 |

## ArrayFromMapFn18+

PhonePC/2in1TabletTVWearable

type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType

ArkTS Array归约函数类型，被Array类的[from](arkts-apis-arkts-collections-array.md#from18)接口使用。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | FromElementType | 是 | 当前正在处理的元素。 |
| index | number | 是 | 当前遍历的ArkTS Array元素索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToElementType | 归约函数的结果，该结果会作为数组的新元素。 |

## ArrayPredicateFn18+

PhonePC/2in1TabletTVWearable

type ArrayPredicateFn<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => boolean

ArkTS Array归约函数类型，被Array类的'some'和'every'接口使用，用来判断数组元素是否满足测试条件。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ElementType | 是 | 当前正在处理的元素。 |
| index | number | 是 | 当前遍历的ArkTS Array元素索引。 |
| array | ArrayType | 是 | 当前遍历的ArkTS Array本身。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 归约函数的结果，该结果作为判断当前元素是否通过测试条件。为true时表示当前或之前的某个元素已满足条件，为false时表示尚未找到符合条件的元素。 |

## ArrayReduceCallback18+

PhonePC/2in1TabletTVWearable

type ArrayReduceCallback<AccType, ElementType, ArrayType> = (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType

ArkTS Array归约函数类型，被Array类的'reduceRight'接口使用。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| previousValue | AccType | 是 | 当前遍历所累积的值。 |
| currentValue | ElementType | 是 | 当前遍历的ArkTS Array元素。 |
| currentIndex | number | 是 | 当前遍历的ArkTS Array元素索引。 |
| array | ArrayType | 是 | 当前遍历的ArkTS Array实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AccType | 归约函数的结果，该结果会作为下一次调用ArrayReduceCallback时的previousValue参数。 |

## TypedArrayFromMapFn

PhonePC/2in1TabletTVWearable

type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType

ArkTS TypedArray映射函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | FromElementType | 是 | 当前遍历的用于构造ArkTS TypedArray的元素。 |
| index | number | 是 | 当前遍历的用于构造ArkTS TypedArray的元素索引，从0开始。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ToElementType | 转换后的元素值。 |

## TypedArrayPredicateFn

PhonePC/2in1TabletTVWearable

type TypedArrayPredicateFn<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => boolean

ArkTS TypedArray断言测试函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ElementType | 是 | 当前遍历的ArkTS TypedArray元素。 |
| index | number | 是 | 当前遍历的ArkTS TypedArray元素索引，从0开始。 |
| array | ArrayType | 是 | 当前遍历的ArkTS TypedArray实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果值符合条件，则为true，否则为false。 |

## TypedArrayForEachCallback

PhonePC/2in1TabletTVWearable

type TypedArrayForEachCallback<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => void

ArkTS TypedArray遍历函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ElementType | 否 | 当前遍历的ArkTS TypedArray元素。 |
| index | number | 否 | 当前遍历的ArkTS TypedArray元素索引，从0开始。 |
| array | ArrayType | 否 | 当前遍历的ArkTS TypedArray实例。 |

## TypedArrayMapCallback

PhonePC/2in1TabletTVWearable

type TypedArrayMapCallback<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => ElementType

ArkTS TypedArray转换映射函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ElementType | 是 | 当前映射的ArkTS TypedArray元素。 |
| index | number | 是 | 当前映射的ArkTS TypedArray元素索引，从0开始。 |
| array | ArrayType | 是 | 当前映射的ArkTS TypedArray实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ElementType | 转换后的元素值。 |

## TypedArrayReduceCallback

PhonePC/2in1TabletTVWearable

type TypedArrayReduceCallback<AccType, ElementType, ArrayType> = (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType

ArkTS TypedArray归约函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| previousValue | AccType | 是 | 当前遍历所累积的值。 |
| currentValue | ElementType | 是 | 当前遍历的ArkTS TypedArray元素。 |
| currentIndex | number | 是 | 当前遍历的ArkTS TypedArray元素索引，从0开始。 |
| array | ArrayType | 是 | 当前遍历的ArkTS TypedArray实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AccType | 归约函数的结果。该结果会作为下一次调用TypedArrayReduceCallback时的previousValue参数。 |

## TypedArrayCompareFn

PhonePC/2in1TabletTVWearable

type TypedArrayCompareFn<ElementType> = (first: ElementType, second: ElementType) => number

ArkTS TypedArray排序函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | ElementType | 是 | 当前待比较的第一个元素。 |
| second | ElementType | 是 | 当前待比较的第二个元素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 元素比较的结果。如果first小于second，返回值为负数；如果first大于second，返回值为正数；如果两个值相等，返回值为0。 |
