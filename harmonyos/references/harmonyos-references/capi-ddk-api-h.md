---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-api-h
title: ddk_api.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > ddk_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:327d313f56a2c1a8610c99d5702fd3da58222fde4a814ed0d59918d25bcb4777
---

## 概述

PC/2in1

声明主机侧访问的Base DDK接口。

**引用文件：** <ddk/ddk\_api.h>

**库：** libddk\_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：** [Ddk](capi-baseddk.md)

## 汇总

PC/2in1

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [DDK\_RetCode OH\_DDK\_CreateAshmem(const uint8\_t \*name, uint32\_t size, DDK\_Ashmem \*\*ashmem)](capi-ddk-api-h.md#oh_ddk_createashmem) | 创建共享内存。为了防止资源泄漏，通过调用**OH\_DDK\_DestroyAshmem**接口来销毁不再需要的共享内存。 |
| [DDK\_RetCode OH\_DDK\_MapAshmem(DDK\_Ashmem \*ashmem, const uint8\_t ashmemMapType)](capi-ddk-api-h.md#oh_ddk_mapashmem) | 映射创建的共享内存到用户空间。通过调用**OH\_DDK\_UnmapAshmem**接口取消映射不需要的共享内存。 |
| [DDK\_RetCode OH\_DDK\_UnmapAshmem(DDK\_Ashmem \*ashmem)](capi-ddk-api-h.md#oh_ddk_unmapashmem) | 取消映射共享内存。 |
| [DDK\_RetCode OH\_DDK\_DestroyAshmem(DDK\_Ashmem \*ashmem)](capi-ddk-api-h.md#oh_ddk_destroyashmem) | 销毁共享内存。 |

## 函数说明

PC/2in1

### OH\_DDK\_CreateAshmem()

PC/2in1

```
1. DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)
```

**描述**

创建共享内存。为了防止资源泄漏，通过调用**OH\_DDK\_DestroyAshmem**接口来销毁不再需要的共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const uint8\_t \*name | 指向要创建的共享内存的指针。 |
| uint32\_t size | 共享内存对应的缓冲区大小。 |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*\*ashmem | 指向创建的共享内存的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。  [DDK\_INVALID\_PARAMETER](capi-ddk-types-h.md#ddk_retcode) 入参name为空指针，size的大小为0或者入参ashmem是空指针。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 创建共享内存失败或者创建结构体DDK\_Ashmem失败。 |

### OH\_DDK\_MapAshmem()

PC/2in1

```
1. DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)
```

**描述**

映射创建的共享内存到用户空间。通过调用**OH\_DDK\_UnmapAshmem**接口取消映射不需要的共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要映射的共享内存指针。 |
| const uint8\_t ashmemMapType | 共享内存的保护权限值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效。  [DDK\_INVALID\_OPERATION](capi-ddk-types-h.md#ddk_retcode) 调用接口MapAshmem失败. |

### OH\_DDK\_UnmapAshmem()

PC/2in1

```
1. DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)
```

**描述**

取消映射共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要取消映射的共享内存指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效。 |

### OH\_DDK\_DestroyAshmem()

PC/2in1

```
1. DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)
```

**描述**

销毁共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要销毁的共享内存指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效。 |
