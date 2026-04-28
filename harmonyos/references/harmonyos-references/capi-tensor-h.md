---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-tensor-h
title: tensor.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > tensor.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d53b8282221b1e24d8888145e042495d9e2076bf14f358e1a0c4273c3edb0007
---

## 概述

PhonePC/2in1TabletTVWearable

提供了张量相关的接口，可用于创建和修改张量信息，该接口是非线程安全的。

**引用文件：** <mindspore/tensor.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| void \* | [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) | 指向张量对象句柄。 |
| void \* | [OH\_AI\_AllocatorHandle](capi-mindspore-oh-ai-allocatorhandle.md) | 指向内存分配器对象句柄。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorCreate(const char \*name, OH\_AI\_DataType type, const int64\_t \*shape,size\_t shape\_num, const void \*data, size\_t data\_len)](capi-tensor-h.md#oh_ai_tensorcreate) | 创建一个张量对象。 |
| [OH\_AI\_API void OH\_AI\_TensorDestroy(OH\_AI\_TensorHandle \*tensor)](capi-tensor-h.md#oh_ai_tensordestroy) | 释放张量对象。 |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorClone(OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorclone) | 深拷贝一个张量。 |
| [OH\_AI\_API void OH\_AI\_TensorSetName(OH\_AI\_TensorHandle tensor, const char \*name)](capi-tensor-h.md#oh_ai_tensorsetname) | 设置张量的名称。 |
| [OH\_AI\_API const char \*OH\_AI\_TensorGetName(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetname) | 获取张量的名称。 |
| [OH\_AI\_API void OH\_AI\_TensorSetDataType(OH\_AI\_TensorHandle tensor, OH\_AI\_DataType type)](capi-tensor-h.md#oh_ai_tensorsetdatatype) | 设置张量的数据类型。 |
| [OH\_AI\_API OH\_AI\_DataType OH\_AI\_TensorGetDataType(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetdatatype) | 获取张量类型。 |
| [OH\_AI\_API void OH\_AI\_TensorSetShape(OH\_AI\_TensorHandle tensor, const int64\_t \*shape, size\_t shape\_num)](capi-tensor-h.md#oh_ai_tensorsetshape) | 设置张量的形状。 |
| [OH\_AI\_API const int64\_t \*OH\_AI\_TensorGetShape(const OH\_AI\_TensorHandle tensor, size\_t \*shape\_num)](capi-tensor-h.md#oh_ai_tensorgetshape) | 获取张量的形状。 |
| [OH\_AI\_API void OH\_AI\_TensorSetFormat(OH\_AI\_TensorHandle tensor, OH\_AI\_Format format)](capi-tensor-h.md#oh_ai_tensorsetformat) | 设置张量数据的排列方式。 |
| [OH\_AI\_API OH\_AI\_Format OH\_AI\_TensorGetFormat(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetformat) | 获取张量数据的排列方式。 |
| [OH\_AI\_API void OH\_AI\_TensorSetData(OH\_AI\_TensorHandle tensor, void \*data)](capi-tensor-h.md#oh_ai_tensorsetdata) | 设置张量的数据。 |
| [OH\_AI\_API const void \*OH\_AI\_TensorGetData(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetdata) | 获取张量数据的指针。 |
| [OH\_AI\_API void \*OH\_AI\_TensorGetMutableData(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetmutabledata) | 获取可变的张量数据指针。如果数据为空则会开辟内存。 |
| [OH\_AI\_API int64\_t OH\_AI\_TensorGetElementNum(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetelementnum) | 获取张量元素数量。 |
| [OH\_AI\_API size\_t OH\_AI\_TensorGetDataSize(const OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetdatasize) | 获取张量中的数据的字节数大小。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetUserData(OH\_AI\_TensorHandle tensor, void \*data, size\_t data\_size)](capi-tensor-h.md#oh_ai_tensorsetuserdata) | 设置张量为用户自行管理的数据。此接口常用于复用用户数据作为模型输入，可减少一次数据拷贝。  注意：此数据对于张量来说是外部数据，张量销毁时不会主动释放，由调用者负责释放。另外，在此张量使用过程中，调用者须确保此数据有效。 |
| [OH\_AI\_API OH\_AI\_AllocatorHandle OH\_AI\_TensorGetAllocator(OH\_AI\_TensorHandle tensor)](capi-tensor-h.md#oh_ai_tensorgetallocator) | 获取内存分配器。此接口主要是提供一种获取张量的内存分配器的方法。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetAllocator(OH\_AI\_TensorHandle tensor, OH\_AI\_AllocatorHandle allocator)](capi-tensor-h.md#oh_ai_tensorsetallocator) | 设置内存分配器。此接口主要是提供一种设置内存分配器的方法，tensor的内存将由这个分配器分配。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_TensorCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandle OH_AI_TensorCreate(const char *name, OH_AI_DataType type, const int64_t *shape,size_t shape_num, const void *data, size_t data_len)
```

**描述**

创建一个张量对象。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 张量名称。字符串长度跟随系统限制。 |
| [OH\_AI\_DataType](capi-data-type-h.md#oh_ai_datatype) type | 张量的数据类型。 |
| const int64\_t \*shape | 张量的维度数组。 |
| size\_t shape\_num | 张量维度数组长度。 |
| const void \*data | 指向数据的指针。 |
| size\_t data\_len | 数据的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) | 指向张量对象句柄。 |

### OH\_AI\_TensorDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorDestroy(OH_AI_TensorHandle *tensor)
```

**描述**

释放张量对象。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) \*tensor | 指向张量句柄的二级指针。 |

### OH\_AI\_TensorClone()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandle OH_AI_TensorClone(OH_AI_TensorHandle tensor)
```

**描述**

深拷贝一个张量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) | 指向新张量对象句柄。 |

### OH\_AI\_TensorSetName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorSetName(OH_AI_TensorHandle tensor, const char *name)
```

**描述**

设置张量的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| const char \*name | 张量名称。字符串长度跟随系统限制。 |

### OH\_AI\_TensorGetName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const char *OH_AI_TensorGetName(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量的名称。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const char \* | 张量的名称。 |

### OH\_AI\_TensorSetDataType()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorSetDataType(OH_AI_TensorHandle tensor, OH_AI_DataType type)
```

**描述**

设置张量的数据类型。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| [OH\_AI\_DataType](capi-data-type-h.md#oh_ai_datatype) type | 数据类型，具体见[OH\_AI\_DataType](capi-data-type-h.md#oh_ai_datatype)。 |

### OH\_AI\_TensorGetDataType()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_DataType OH_AI_TensorGetDataType(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量类型。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_DataType](capi-data-type-h.md#oh_ai_datatype) | 张量的数据类型。 |

### OH\_AI\_TensorSetShape()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorSetShape(OH_AI_TensorHandle tensor, const int64_t *shape, size_t shape_num)
```

**描述**

设置张量的形状。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| const int64\_t \*shape | 形状数组。 |
| size\_t shape\_num | 张量形状数组长度。 |

### OH\_AI\_TensorGetShape()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const int64_t *OH_AI_TensorGetShape(const OH_AI_TensorHandle tensor, size_t *shape_num)
```

**描述**

获取张量的形状。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| size\_t \*shape\_num | 该参数是输出参数，形状数组的长度会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const int64\_t \* | 形状数组。 |

### OH\_AI\_TensorSetFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorSetFormat(OH_AI_TensorHandle tensor, OH_AI_Format format)
```

**描述**

设置张量数据的排列方式。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| [OH\_AI\_Format](capi-format-h.md#oh_ai_format) format | 张量数据排列方式。 |

### OH\_AI\_TensorGetFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Format OH_AI_TensorGetFormat(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量数据的排列方式。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Format](capi-format-h.md#oh_ai_format) | 张量数据的排列方式。 |

### OH\_AI\_TensorSetData()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TensorSetData(OH_AI_TensorHandle tensor, void *data)
```

**描述**

设置张量的数据。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| void \*data | 指向数据的指针。 |

### OH\_AI\_TensorGetData()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API const void *OH_AI_TensorGetData(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量数据的指针。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API const void \* | 张量数据的指针。 |

### OH\_AI\_TensorGetMutableData()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void *OH_AI_TensorGetMutableData(const OH_AI_TensorHandle tensor)
```

**描述**

获取可变的张量数据指针。如果数据为空则会开辟内存。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API void \* | 张量数据的指针。 |

### OH\_AI\_TensorGetElementNum()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API int64_t OH_AI_TensorGetElementNum(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量元素数量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API int64\_t | 张量的元素数量。 |

### OH\_AI\_TensorGetDataSize()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API size_t OH_AI_TensorGetDataSize(const OH_AI_TensorHandle tensor)
```

**描述**

获取张量中的数据的字节数大小。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API size\_t | 张量数据的字节数大小。 |

### OH\_AI\_TensorSetUserData()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_TensorSetUserData(OH_AI_TensorHandle tensor, void *data, size_t data_size)
```

**描述**

设置张量为用户自行管理的数据。此接口常用于复用用户数据作为模型输入，可减少一次数据拷贝。

注意：此数据对于张量来说是外部数据，张量销毁时不会主动释放，由调用者负责释放。另外，在此张量使用过程中，调用者须确保此数据有效。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| void \*data | 用户数据首地址。 |
| size\_t data\_size | 用户数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 执行状态码。若成功返回OH\_AI\_STATUS\_SUCCESS，否则返回具体错误码。 |

### OH\_AI\_TensorGetAllocator()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_AllocatorHandle OH_AI_TensorGetAllocator(OH_AI_TensorHandle tensor)
```

**描述**

获取内存分配器。此接口主要是提供一种获取张量的内存分配器的方法。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_AllocatorHandle](capi-mindspore-oh-ai-allocatorhandle.md) | 内存分配器的句柄。 |

### OH\_AI\_TensorSetAllocator()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_TensorSetAllocator(OH_AI_TensorHandle tensor, OH_AI_AllocatorHandle allocator)
```

**描述**

设置内存分配器。此接口主要是提供一种设置内存分配器的方法，tensor的内存将由这个分配器分配。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) tensor | 张量对象句柄。 |
| [OH\_AI\_AllocatorHandle](capi-mindspore-oh-ai-allocatorhandle.md) allocator | 内存分配器对象句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 执行状态码。若成功返回OH\_AI\_STATUS\_SUCCESS，否则返回具体错误码。 |
