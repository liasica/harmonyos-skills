---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-api-h
title: ddk_api.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > ddk_api.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:709f6bb0569bdc5f7c697dcdc3dd5bd1bdc5ccba41f89673a3484df9c8a12a90
---

## 概述

声明主机侧访问的Base DDK接口。提供共享内存的创建、映射、销毁等功能，支持开发者在驱动程序中高效管理共享内存资源，适用于需要与驱动侧共享数据的场景，有助于简化内存管理、提升数据传输效率。

**引用文件：** <ddk/ddk\_api.h>

**库：** libddk\_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：** [Ddk](capi-baseddk.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [DDK\_RetCode OH\_DDK\_CreateAshmem(const uint8\_t \*name, uint32\_t size, DDK\_Ashmem \*\*ashmem)](capi-ddk-api-h.md#oh_ddk_createashmem) | 创建共享内存。为了防止资源泄漏，应通过调用[OH\_DDK\_DestroyAshmem](capi-ddk-api-h.md#oh_ddk_destroyashmem)接口来销毁不再需要的共享内存。 |
| [DDK\_RetCode OH\_DDK\_MapAshmem(DDK\_Ashmem \*ashmem, const uint8\_t ashmemMapType)](capi-ddk-api-h.md#oh_ddk_mapashmem) | 映射创建的共享内存到用户空间。需先调用[OH\_DDK\_CreateAshmem](capi-ddk-api-h.md#oh_ddk_createashmem)接口创建共享内存。通过调用[OH\_DDK\_UnmapAshmem](capi-ddk-api-h.md#oh_ddk_unmapashmem)接口取消映射不需要的共享内存。 |
| [DDK\_RetCode OH\_DDK\_UnmapAshmem(DDK\_Ashmem \*ashmem)](capi-ddk-api-h.md#oh_ddk_unmapashmem) | 取消映射共享内存。需先调用[OH\_DDK\_MapAshmem](capi-ddk-api-h.md#oh_ddk_mapashmem)接口映射共享内存。不再访问共享内存时应取消映射，以节省地址空间。 |
| [DDK\_RetCode OH\_DDK\_DestroyAshmem(DDK\_Ashmem \*ashmem)](capi-ddk-api-h.md#oh_ddk_destroyashmem) | 销毁由[OH\_DDK\_CreateAshmem](capi-ddk-api-h.md#oh_ddk_createashmem)创建的共享内存。建议先调用[OH\_DDK\_UnmapAshmem](capi-ddk-api-h.md#oh_ddk_unmapashmem)接口取消映射。共享内存不再使用时应及时销毁以释放系统资源。 |

## 函数说明

### OH\_DDK\_CreateAshmem()

```c
DDK_RetCode OH_DDK_CreateAshmem(const uint8_t *name, uint32_t size, DDK_Ashmem **ashmem)
```

**描述**

创建共享内存。为了防止资源泄漏，应通过调用[OH\_DDK\_DestroyAshmem](capi-ddk-api-h.md#oh_ddk_destroyashmem)接口来销毁不再需要的共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const uint8\_t \*name | 指向共享内存名称字符串的指针，该名称用于标识共享内存。name不能为NULL，建议使用具有唯一性的名称以避免冲突。 |
| uint32\_t size | 共享内存对应的缓冲区大小（单位：字节），必须大于0，过大会导致内存占用过高，影响运行性能。 |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*\*ashmem | 用于输出创建的共享内存对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。共享内存已成功创建并初始化完成。  [DDK\_INVALID\_PARAMETER](capi-ddk-types-h.md#ddk_retcode) 入参name为空指针，size的大小为0或者入参ashmem是空指针。请检查传入的参数值。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 创建共享内存失败或者创建结构体DDK\_Ashmem失败。请检查申请的内存大小和权限。 |

### OH\_DDK\_MapAshmem()

```c
DDK_RetCode OH_DDK_MapAshmem(DDK_Ashmem *ashmem, const uint8_t ashmemMapType)
```

**描述**

映射创建的共享内存到用户空间。需先调用[OH\_DDK\_CreateAshmem](capi-ddk-api-h.md#oh_ddk_createashmem)接口创建共享内存。通过调用[OH\_DDK\_UnmapAshmem](capi-ddk-api-h.md#oh_ddk_unmapashmem)接口取消映射不需要的共享内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要映射的共享内存描述符指针。 |
| const uint8\_t ashmemMapType | 共享内存的保护权限值，取值请参考Ashmem保护权限的通用定义范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。共享内存已映射到用户空间。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。请检查传入的参数值。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效或未先创建共享内存。请检查共享内存是否已被创建、确保文件描述符未被关闭。  [DDK\_INVALID\_OPERATION](capi-ddk-types-h.md#ddk_retcode) 调用接口映射共享内存失败。可能原因包括映射状态异常或权限不足，请检查共享内存的映射状态和权限后重试。 |

### OH\_DDK\_UnmapAshmem()

```c
DDK_RetCode OH_DDK_UnmapAshmem(DDK_Ashmem *ashmem)
```

**描述**

取消映射共享内存。需先调用[OH\_DDK\_MapAshmem](capi-ddk-api-h.md#oh_ddk_mapashmem)接口映射共享内存。不再访问共享内存时应取消映射，以节省地址空间。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要取消映射的共享内存描述符指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。共享内存已成功从用户空间取消映射。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。请检查传入的参数值。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效或未先执行映射。 |

### OH\_DDK\_DestroyAshmem()

```c
DDK_RetCode OH_DDK_DestroyAshmem(DDK_Ashmem *ashmem)
```

**描述**

销毁由[OH\_DDK\_CreateAshmem](capi-ddk-api-h.md#oh_ddk_createashmem)创建的共享内存。建议先调用[OH\_DDK\_UnmapAshmem](capi-ddk-api-h.md#oh_ddk_unmapashmem)接口取消映射。共享内存不再使用时应及时销毁以释放系统资源。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DDK\_Ashmem](capi-baseddk-ddk-ashmem.md) \*ashmem | 要销毁的共享内存描述符指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DDK\_RetCode](capi-ddk-types-h.md#ddk_retcode) | [DDK\_SUCCESS](capi-ddk-types-h.md#ddk_retcode) 调用接口成功。共享内存已成功销毁释放。  [DDK\_NULL\_PTR](capi-ddk-types-h.md#ddk_retcode) 入参ashmem为空指针。请检查传入的参数值。  [DDK\_FAILURE](capi-ddk-types-h.md#ddk_retcode) 共享内存的文件描述符无效。可能原因包括共享内存已被释放或多次销毁，请检查其状态。 |
