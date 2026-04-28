---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-utd-h
title: utd.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > utd.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:34+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:9f0d19a5cb7ee10ba3e2a89cd0055221f03379c44270449a42b8436db98242a1
---

## 概述

PhonePC/2in1TabletTV

提供标准化数据类型描述相关接口和数据结构。当参数类型为char\*时，字符串必须以空字符（'\0'）结尾。

**引用文件：** <database/udmf/utd.h>

**库：** libudmf.so

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 12

**相关模块：** [UDMF](capi-udmf.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md) | OH\_Utd | 统一数据类型描述符。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_Utd\* OH\_Utd\_Create(const char\* typeId)](capi-utd-h.md#oh_utd_create) | 创建统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)指针及实例对象。 |
| [void OH\_Utd\_Destroy(OH\_Utd\* pThis)](capi-utd-h.md#oh_utd_destroy) | 销毁统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)指针指向的实例对象。 |
| [const char\* OH\_Utd\_GetTypeId(OH\_Utd\* pThis)](capi-utd-h.md#oh_utd_gettypeid) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的类型ID。 |
| [const char\* OH\_Utd\_GetDescription(OH\_Utd\* pThis)](capi-utd-h.md#oh_utd_getdescription) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的描述信息。 |
| [const char\* OH\_Utd\_GetReferenceUrl(OH\_Utd\* pThis)](capi-utd-h.md#oh_utd_getreferenceurl) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的URL信息。 |
| [const char\* OH\_Utd\_GetIconFile(OH\_Utd\* pThis)](capi-utd-h.md#oh_utd_geticonfile) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的默认图标文件路径。 |
| [const char\*\* OH\_Utd\_GetBelongingToTypes(OH\_Utd\* pThis, unsigned int\* count)](capi-utd-h.md#oh_utd_getbelongingtotypes) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的归属关系结果集。 |
| [const char\*\* OH\_Utd\_GetFilenameExtensions(OH\_Utd\* pThis, unsigned int\* count)](capi-utd-h.md#oh_utd_getfilenameextensions) | 获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)所关联的文件名后缀结果集。 |
| [const char\*\* OH\_Utd\_GetMimeTypes(OH\_Utd\* pThis, unsigned int\* count)](capi-utd-h.md#oh_utd_getmimetypes) | 获取[OH\_Utd](capi-udmf-oh-utd.md)所关联的MIME类型结果集。 |
| [const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count)](capi-utd-h.md#oh_utd_gettypesbyfilenameextension) | 通过文件名后缀获取关联的统一标准数据描述类型结果集。 |
| [const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count)](capi-utd-h.md#oh_utd_gettypesbymimetype) | 通过MIME类型获取所关联的标准数据类型结果集。 |
| [bool OH\_Utd\_BelongsTo(const char\* srcTypeId, const char\* destTypeId)](capi-utd-h.md#oh_utd_belongsto) | 判断两个标准化数据描述类型是否存在归属关系。 |
| [bool OH\_Utd\_IsLower(const char\* srcTypeId, const char\* destTypeId)](capi-utd-h.md#oh_utd_islower) | 判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE\_SCRIPT为SOURCE\_CODE的低层级类型，TYPE\_SCRIPT和SOURCE\_CODE为PLAIN\_TEXT的低层级类型。 |
| [bool OH\_Utd\_IsHigher(const char\* srcTypeId, const char\* destTypeId)](capi-utd-h.md#oh_utd_ishigher) | 判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE\_CODE为TYPE\_SCRIPT的高层级类型，PLAIN\_TEXT为SOURCE\_CODE和TYPE\_SCRIPT的高层级类型。 |
| [bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2)](capi-utd-h.md#oh_utd_equals) | 判断两个标准化数据描述类型是否相等。 |
| [void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count)](capi-utd-h.md#oh_utd_destroystringlist) | 销毁标准数据描述类型结果集字符串列表。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_Utd\_Create()

PhonePC/2in1TabletTV

```
1. OH_Utd* OH_Utd_Create(const char* typeId)
```

**描述**

创建统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)指针及实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* typeId | 表示统一数据类型ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* | 执行成功则返回一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)实例对象的指针，否则返回nullptr。  当不再需要使用指针时，请使用[OH\_Utd\_Destroy](capi-utd-h.md#oh_utd_destroy)销毁实例对象，否则会导致内存泄漏。 |

### OH\_Utd\_Destroy()

PhonePC/2in1TabletTV

```
1. void OH_Utd_Destroy(OH_Utd* pThis)
```

**描述**

销毁统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)指针指向的实例对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)实例的指针。 |

### OH\_Utd\_GetTypeId()

PhonePC/2in1TabletTV

```
1. const char* OH_Utd_GetTypeId(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的类型ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 当入参有效时返回指向类型ID的字符串指针，否则返回nullptr。 |

### OH\_Utd\_GetDescription()

PhonePC/2in1TabletTV

```
1. const char* OH_Utd_GetDescription(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的描述信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 当入参有效时返回指向描述信息的字符串指针，否则返回nullptr。 |

### OH\_Utd\_GetReferenceUrl()

PhonePC/2in1TabletTV

```
1. const char* OH_Utd_GetReferenceUrl(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的URL信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 当入参有效时返回指向URL信息的字符串指针，否则返回nullptr。 |

### OH\_Utd\_GetIconFile()

PhonePC/2in1TabletTV

```
1. const char* OH_Utd_GetIconFile(OH_Utd* pThis)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的默认图标文件路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 当入参有效时返回指向默认图标文件路径的字符串指针，否则返回nullptr。 |

### OH\_Utd\_GetBelongingToTypes()

PhonePC/2in1TabletTV

```
1. const char** OH_Utd_GetBelongingToTypes(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)中的归属关系结果集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |
| unsigned int\* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\*\* | 当入参有效时返回归属关系结果集的字符串指针列表，否则返回nullptr。 |

### OH\_Utd\_GetFilenameExtensions()

PhonePC/2in1TabletTV

```
1. const char** OH_Utd_GetFilenameExtensions(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)所关联的文件名后缀结果集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |
| unsigned int\* count | 该参数是输出参数，结果集中的文件后缀名数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\*\* | 当入参有效时返回文件名后缀结果集的字符串指针列表，否则返回nullptr。 |

### OH\_Utd\_GetMimeTypes()

PhonePC/2in1TabletTV

```
1. const char** OH_Utd_GetMimeTypes(OH_Utd* pThis, unsigned int* count)
```

**描述**

获取[OH\_Utd](capi-udmf-oh-utd.md)所关联的MIME类型结果集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* pThis | 表示一个指向统一数据类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |
| unsigned int\* count | 该参数是输出参数，结果集中的MIME类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\*\* | 当入参有效时返回MIME类型结果集的字符串指针列表，否则返回nullptr。 |

### OH\_Utd\_GetTypesByFilenameExtension()

PhonePC/2in1TabletTV

```
1. const char** OH_Utd_GetTypesByFilenameExtension(const char* extension, unsigned int* count)
```

**描述**

通过文件名后缀获取关联的统一标准数据描述类型结果集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* extension | 表示文件名后缀。 |
| unsigned int\* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\*\* | 返回标准数据描述类型结果集字符串列表。  当不再需要使用指针时，请及时使用[OH\_Utd\_DestroyStringList](capi-utd-h.md#oh_utd_destroystringlist)销毁对应的实例，否则会导致内存泄漏。 |

### OH\_Utd\_GetTypesByMimeType()

PhonePC/2in1TabletTV

```
1. const char** OH_Utd_GetTypesByMimeType(const char* mimeType, unsigned int* count)
```

**描述**

通过MIME类型获取所关联的标准数据类型结果集。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* mimeType | 表示MIME类型字符串。 |
| unsigned int\* count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\*\* | 返回标准数据描述类型结果集字符串列表。  当不再需要使用指针时，请及时使用[OH\_Utd\_DestroyStringList](capi-utd-h.md#oh_utd_destroystringlist)销毁对应的实例，否则会导致内存泄漏。 |

### OH\_Utd\_BelongsTo()

PhonePC/2in1TabletTV

```
1. bool OH_Utd_BelongsTo(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断两个标准化数据描述类型是否存在归属关系。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* srcTypeId | 表示原标准化数据类型。 |
| const char\* destTypeId | 表示目标标准化数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不属于目标类型，true表示原类型属于目标类型。 |

### OH\_Utd\_IsLower()

PhonePC/2in1TabletTV

```
1. bool OH_Utd_IsLower(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断原标准化数据类型是否是目标标准化数据类型的低层级类型。例如TYPE\_SCRIPT为SOURCE\_CODE的低层级类型，TYPE\_SCRIPT和SOURCE\_CODE为PLAIN\_TEXT的低层级类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* srcTypeId | 表示原标准化数据类型。 |
| const char\* destTypeId | 表示目标标准化数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不低于目标类型；true表示原类型低于目标类型。 |

### OH\_Utd\_IsHigher()

PhonePC/2in1TabletTV

```
1. bool OH_Utd_IsHigher(const char* srcTypeId, const char* destTypeId)
```

**描述**

判断原标准化数据类型是否是目标标准化数据类型的高层级类型。例如SOURCE\_CODE为TYPE\_SCRIPT的高层级类型，PLAIN\_TEXT为SOURCE\_CODE和TYPE\_SCRIPT的高层级类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* srcTypeId | 表示原标准化数据类型。 |
| const char\* destTypeId | 表示目标标准化数据类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | false表示原类型不高于目标类型，true表示原类型高于目标类型。 |

### OH\_Utd\_Equals()

PhonePC/2in1TabletTV

```
1. bool OH_Utd_Equals(OH_Utd* utd1, OH_Utd* utd2)
```

**描述**

判断两个标准化数据描述类型是否相等。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Utd](capi-udmf-oh-utd.md)\* utd1 | 表示一个指向标准化数据描述类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |
| [OH\_Utd](capi-udmf-oh-utd.md)\* utd2 | 表示一个指向标准化数据描述类型[OH\_Utd](capi-udmf-oh-utd.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | false表示两种类型不相等，true表示两种类型相等。 |

### OH\_Utd\_DestroyStringList()

PhonePC/2in1TabletTV

```
1. void OH_Utd_DestroyStringList(const char** list, unsigned int count)
```

**描述**

销毁标准数据描述类型结果集字符串列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\*\* list | 表示字符串列表指针。 |
| unsigned int count | 表示字符串列表list参数中的列表长度。 |
