---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h
title: native_avbuffer.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avbuffer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8553d61a62fe5eb90df040d438e5d495a0bc783f12309e0455aee5fbafcc1b49
---

## 概述

PhonePC/2in1TabletTVWearable

声明了媒体数据结构AVBuffer的函数接口。

**引用文件：** <multimedia/player\_framework/native\_avbuffer.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**相关模块：** [Core](capi-core.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) | OH\_AVBuffer | 为媒体内存接口定义native层对象。 |
| [OH\_NativeBuffer](capi-oh-nativebuffer.md) | OH\_NativeBuffer | 为图形内存接口定义native层对象。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVBuffer \*OH\_AVBuffer\_Create(int32\_t capacity)](capi-native-avbuffer-h.md#oh_avbuffer_create) | 创建OH\_AVBuffer实例。需要注意的是，返回值指向的创建OH\_AVBuffer的实例需要开发者主动调用接口释放，请参阅[OH\_AVBuffer\_Destroy](capi-native-avbuffer-h.md#oh_avbuffer_destroy)。 |
| [OH\_AVErrCode OH\_AVBuffer\_Destroy(OH\_AVBuffer \*buffer)](capi-native-avbuffer-h.md#oh_avbuffer_destroy) | 释放OH\_AVBuffer实例指针的资源，同一个buffer不允许重复销毁。 |
| [OH\_AVErrCode OH\_AVBuffer\_GetBufferAttr(OH\_AVBuffer \*buffer, OH\_AVCodecBufferAttr \*attr)](capi-native-avbuffer-h.md#oh_avbuffer_getbufferattr) | 获取数据缓冲区的pts、size、offset、flags高频属性参数。 |
| [OH\_AVErrCode OH\_AVBuffer\_SetBufferAttr(OH\_AVBuffer \*buffer, const OH\_AVCodecBufferAttr \*attr)](capi-native-avbuffer-h.md#oh_avbuffer_setbufferattr) | 设置数据缓冲区的pts、size、offset、flags高频属性参数。 |
| [OH\_AVFormat \*OH\_AVBuffer\_GetParameter(OH\_AVBuffer \*buffer)](capi-native-avbuffer-h.md#oh_avbuffer_getparameter) | 获取除基础属性外的其他参数，信息在OH\_AVFormat中承载。需要注意的是，返回值指向的创建OH\_AVFormat的实例需要开发者主动释放，请参阅[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)。 |
| [OH\_AVErrCode OH\_AVBuffer\_SetParameter(OH\_AVBuffer \*buffer, const OH\_AVFormat \*format)](capi-native-avbuffer-h.md#oh_avbuffer_setparameter) | 设置除基础属性外的其他参数，信息在OH\_AVFormat中承载。 |
| [uint8\_t \*OH\_AVBuffer\_GetAddr(OH\_AVBuffer \*buffer)](capi-native-avbuffer-h.md#oh_avbuffer_getaddr) | 获取数据缓冲区的虚拟地址。 |
| [int32\_t OH\_AVBuffer\_GetCapacity(OH\_AVBuffer \*buffer)](capi-native-avbuffer-h.md#oh_avbuffer_getcapacity) | 获取数据缓冲区的容量（字节数）。 |
| [OH\_NativeBuffer \*OH\_AVBuffer\_GetNativeBuffer(OH\_AVBuffer \*buffer)](capi-native-avbuffer-h.md#oh_avbuffer_getnativebuffer) | 获取OH\_NativeBuffer实例的指针。需要注意的是，返回值指向的创建OH\_NativeBuffer的实例需要开发者主动调用接口释放，请参阅[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVBuffer\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVBuffer *OH_AVBuffer_Create(int32_t capacity)
```

**描述**

创建OH\_AVBuffer实例。需要注意的是，返回值指向的创建OH\_AVBuffer的实例需要开发者主动调用接口释放，请参阅[OH\_AVBuffer\_Destroy](capi-native-avbuffer-h.md#oh_avbuffer_destroy)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t capacity | 创建内存的大小，单位字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \* | 如果创建成功，则返回OH\_AVBuffer实例的指针，如果失败，则返回NULL。  可能的失败原因：  1.capacity <= 0。  2.出现内部错误，系统没有资源等。 |

### OH\_AVBuffer\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVBuffer_Destroy(OH_AVBuffer *buffer)
```

**描述**

释放OH\_AVBuffer实例指针的资源，同一个buffer不允许重复销毁。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_INVALID\_VAL：输入的buffer为空指针或者buffer格式校验失败。  AV\_ERR\_OPERATE\_NOT\_PERMIT：输入的buffer不是用户创建的。 |

### OH\_AVBuffer\_GetBufferAttr()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVBuffer_GetBufferAttr(OH_AVBuffer *buffer, OH_AVCodecBufferAttr *attr)
```

**描述**

获取数据缓冲区的pts、size、offset、flags高频属性参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) \*attr | 指向OH\_AVCodecBufferAttr实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_INVALID\_VAL：可能的原因：  1. 输入的buffer或attr为空指针。  2. buffer结构校验失败。 |

### OH\_AVBuffer\_SetBufferAttr()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVBuffer_SetBufferAttr(OH_AVBuffer *buffer, const OH_AVCodecBufferAttr *attr)
```

**描述**

设置数据缓冲区的pts、size、offset、flags高频属性参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |
| [const OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) \*attr | 指向OH\_AVCodecBufferAttr实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_INVALID\_VAL：可能的原因：  1. 输入的buffer或attr为空指针。  2. buffer结构校验失败。  3. 输入buffer中内存的size或offset是无效值。 |

### OH\_AVBuffer\_GetParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVBuffer_GetParameter(OH_AVBuffer *buffer)
```

**描述**

获取除基础属性外的其他参数，信息在OH\_AVFormat中承载。需要注意的是，返回值指向的创建OH\_AVFormat的实例需要开发者主动释放，请参阅[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \* | AV\_ERR\_OK：操作成功。  AV\_ERR\_INVALID\_VAL：可能的原因：  1. 输入的buffer为空指针。  2. 输入buffer的meta为空指针。  3. buffer结构校验失败。 |

### OH\_AVBuffer\_SetParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVBuffer_SetParameter(OH_AVBuffer *buffer, const OH_AVFormat *format)
```

**描述**

设置除基础属性外的其他参数，信息在OH\_AVFormat中承载。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |
| [const OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_INVALID\_VAL：可能的原因：  1. 输入的buffer或format为空指针。  2. 输入buffer的meta为空指针。  3. buffer结构校验失败。 |

### OH\_AVBuffer\_GetAddr()

PhonePC/2in1TabletTVWearable

```
1. uint8_t *OH_AVBuffer_GetAddr(OH_AVBuffer *buffer)
```

**描述**

获取数据缓冲区的虚拟地址。

不同场景下，对是否可以获取虚拟地址的支持情况不同，请见表格：

**编码：**

| 模式 | 填充数据的方式 | 是否可以获取虚拟地址 |
| --- | --- | --- |
| Surface模式 | OnNeedInputBuffer输入 | × |
| Surface模式 | OnNewOutputBuffer输出 | √ |
| Buffer模式 | OnNeedInputBuffer输入 | √ |
| Buffer模式 | OnNewOutputBuffer输出 | √ |

**解码：**

| 模式 | 填充数据的方式 | 是否可以获取虚拟地址 |
| --- | --- | --- |
| Surface模式 | OnNeedInputBuffer输入 | √ |
| Surface模式 | OnNewOutputBuffer输出 | × |
| Buffer模式 | OnNeedInputBuffer输入 | √ |
| Buffer模式 | OnNewOutputBuffer输出 | √ |

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint8\_t \* | 如果成功，则返回数据缓冲区的虚拟地址，如果失败，则返回NULL。  可能的失败原因：  1.输入的buffer为空指针。  2.OH\_AVBuffer结构校验失败。  3.出现内部错误。 |

### OH\_AVBuffer\_GetCapacity()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_AVBuffer_GetCapacity(OH_AVBuffer *buffer)
```

**描述**

获取数据缓冲区的容量（字节数）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果成功，则返回数据缓冲区的容量，如果失败，则返回-1。  可能的失败原因：  1.输入的buffer为空指针。  2.OH\_AVBuffer结构校验失败。  3.出现内部错误。 |

### OH\_AVBuffer\_GetNativeBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_NativeBuffer *OH_AVBuffer_GetNativeBuffer(OH_AVBuffer *buffer)
```

**描述**

获取OH\_NativeBuffer实例的指针。需要注意的是，返回值指向的创建OH\_NativeBuffer的实例需要开发者主动调用接口释放，请参阅[OH\_NativeBuffer\_Unreference](capi-native-buffer-h.md#oh_nativebuffer_unreference)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_NativeBuffer](capi-oh-nativebuffer.md) \* | 如果成功，则返回OH\_NativeBuffer实例的指针，如果失败，则返回NULL。  可能的失败原因：  1.输入的buffer为空指针。  2.OH\_AVBuffer结构校验失败。  3.出现内部错误。 |
