---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vobject
title: OH_VObject
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > OH_VObject
category: harmonyos-references
scraped_at: 2026-04-28T07:59:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:311e6a658f2f6217e39675a1a22d5d817adfbf5e741f77444acfea6066e4b05b
---

```
1. typedef struct {...} OH_VObject
```

## 概述

PhonePC/2in1TabletTVWearable

表示允许的数据字段类型。

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [oh\_value\_object.h](capi-oh-value-object-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int64\_t id | OH\_VObject结构体的唯一标识符。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int (\*putInt64)(OH\_VObject \*valueObject, int64\_t \*value, uint32\_t count)](capi-rdb-oh-vobject.md#putint64) | 将int64类型的单个参数或者数组转换为OH\_VObject类型的值。 |
| [int (\*putDouble)(OH\_VObject \*valueObject, double \*value, uint32\_t count)](capi-rdb-oh-vobject.md#putdouble) | 将double类型的单个参数或者数组转换为OH\_VObject类型的值。 |
| [int (\*putText)(OH\_VObject \*valueObject, const char \*value)](capi-rdb-oh-vobject.md#puttext) | 将char \*类型的字符数组转换为OH\_VObject类型的值。 |
| [int (\*putTexts)(OH\_VObject \*valueObject, const char \*\*value, uint32\_t count)](capi-rdb-oh-vobject.md#puttexts) | 将char \*类型的字符串数组转换为OH\_VObject类型的值。 |
| [int (\*destroy)(OH\_VObject \*valueObject)](capi-rdb-oh-vobject.md#destroy) | 销毁OH\_VObject对象，并回收该对象占用的内存。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### putInt64()

PhonePC/2in1TabletTVWearable

```
1. int (*putInt64)(OH_VObject *valueObject, int64_t *value, uint32_t count)
```

**描述**

将int64类型的单个参数或者数组转换为OH\_VObject类型的值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VObject \*valueObject | 表示指向OH\_VObject实例的指针。 |
| int64\_t \*value | 表示指向int64\_t类型的单个参数或者数组的指针。 |
| uint32\_t count | 如果value是指向单个数值的指针，则count = 1；如果value是指向数组的指针，则count是数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putDouble()

PhonePC/2in1TabletTVWearable

```
1. int (*putDouble)(OH_VObject *valueObject, double *value, uint32_t count)
```

**描述**

将double类型的单个参数或者数组转换为OH\_VObject类型的值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VObject \*valueObject | 表示指向OH\_VObject实例的指针。 |
| double \*value | 表示指向double类型的单个参数或者数组的指针。 |
| uint32\_t count | 如果value是指向单个数值的指针，则count = 1；如果value是指向数组的指针，则count是数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putText()

PhonePC/2in1TabletTVWearable

```
1. int (*putText)(OH_VObject *valueObject, const char *value)
```

**描述**

将char \*类型的字符数组转换为OH\_VObject类型的值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VObject \*valueObject | 表示指向OH\_VObject实例的指针。 |
| const char \*value | 表示字符数组参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### putTexts()

PhonePC/2in1TabletTVWearable

```
1. int (*putTexts)(OH_VObject *valueObject, const char **value, uint32_t count)
```

**描述**

将char \*类型的字符串数组转换为OH\_VObject类型的值。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VObject \*valueObject | 表示指向OH\_VObject实例的指针。 |
| const char \*\*value | 表示字符串数组参数。 |
| uint32\_t count | 表示字符串数组参数value的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

### destroy()

PhonePC/2in1TabletTVWearable

```
1. int (*destroy)(OH_VObject *valueObject)
```

**描述**

销毁OH\_VObject对象，并回收该对象占用的内存。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_VObject \*valueObject | 表示指向OH\_VObject实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |
