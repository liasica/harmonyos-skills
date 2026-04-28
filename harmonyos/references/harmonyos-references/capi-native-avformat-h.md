---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avformat-h
title: native_avformat.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avformat.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49bd6ddebe4562966a67b64112cb031fadf967e85c8404369e6f4634766c7075
---

## 概述

PhonePC/2in1TabletTVWearable

声明了OH\_AVFormat相关的函数和枚举。

**引用文件：** <multimedia/player\_framework/native\_avformat.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：** [Core](capi-core.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) | OH\_AVFormat | 为OH\_AVFormat接口定义native层对象。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVPixelFormat](capi-native-avformat-h.md#oh_avpixelformat) | OH\_AVPixelFormat | 视频像素格式的枚举类。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [struct OH\_AVFormat \*OH\_AVFormat\_Create(void)](capi-native-avformat-h.md#oh_avformat_create) | 创建OH\_AVFormat实例，用于读取数据。 |
| [struct OH\_AVFormat \*OH\_AVFormat\_CreateAudioFormat(const char \*mimeType, int32\_t sampleRate, int32\_t channelCount)](capi-native-avformat-h.md#oh_avformat_createaudioformat) | 创建音频OH\_AVFormat实例指针并预设置指定参数，用于读写数据。 |
| [struct OH\_AVFormat \*OH\_AVFormat\_CreateVideoFormat(const char \*mimeType, int32\_t width, int32\_t height)](capi-native-avformat-h.md#oh_avformat_createvideoformat) | 创建视频OH\_AVFormat实例指针并预设置指定参数，用于读写数据。 |
| [void OH\_AVFormat\_Destroy(struct OH\_AVFormat \*format)](capi-native-avformat-h.md#oh_avformat_destroy) | 销毁OH\_AVFormat实例，不允许重复销毁。 |
| [bool OH\_AVFormat\_Copy(struct OH\_AVFormat \*to, struct OH\_AVFormat \*from)](capi-native-avformat-h.md#oh_avformat_copy) | 复制OH\_AVFormat实例。 |
| [bool OH\_AVFormat\_SetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t value)](capi-native-avformat-h.md#oh_avformat_setintvalue) | 对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋int类型的值。该接口仅能设置int类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetUintValue(struct OH\_AVFormat \*format, const char \*key, uint32\_t value)](capi-native-avformat-h.md#oh_avformat_setuintvalue) | 对OH\_AVFormat的key赋unsigned int类型的值。该接口仅能设置unsigned int类型的参数，具体参数类型定义请参考[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t value)](capi-native-avformat-h.md#oh_avformat_setlongvalue) | 对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋long类型的值。该接口仅能设置long类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetFloatValue(struct OH\_AVFormat \*format, const char \*key, float value)](capi-native-avformat-h.md#oh_avformat_setfloatvalue) | 对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋float类型的值。该接口仅能设置float类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double value)](capi-native-avformat-h.md#oh_avformat_setdoublevalue) | 对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋double类型的值。该接口仅能设置double类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*value)](capi-native-avformat-h.md#oh_avformat_setstringvalue) | 对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋string类型的值。该接口仅能设置string类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_SetBuffer(struct OH\_AVFormat \*format, const char \*key, const uint8\_t \*addr, size\_t size)](capi-native-avformat-h.md#oh_avformat_setbuffer) | 将指定长度的数据块写入OH\_AVFormat。该接口仅能设置buffer类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。 |
| [bool OH\_AVFormat\_GetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t \*out)](capi-native-avformat-h.md#oh_avformat_getintvalue) | 从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取int类型的值。 |
| [bool OH\_AVFormat\_GetUintValue(struct OH\_AVFormat \*format, const char \*key, uint32\_t \*out)](capi-native-avformat-h.md#oh_avformat_getuintvalue) | 使用key从OH\_AVFormat中获取unsigned int类型的值。 |
| [bool OH\_AVFormat\_GetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t \*out)](capi-native-avformat-h.md#oh_avformat_getlongvalue) | 从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取long类型的值。 |
| [bool OH\_AVFormat\_GetFloatValue(struct OH\_AVFormat \*format, const char \*key, float \*out)](capi-native-avformat-h.md#oh_avformat_getfloatvalue) | 从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取float类型的值。 |
| [bool OH\_AVFormat\_GetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double \*out)](capi-native-avformat-h.md#oh_avformat_getdoublevalue) | 从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取double类型的值。 |
| [bool OH\_AVFormat\_GetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*\*out)](capi-native-avformat-h.md#oh_avformat_getstringvalue) | 从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取string类型的值。 |
| [bool OH\_AVFormat\_GetBuffer(struct OH\_AVFormat \*format, const char \*key, uint8\_t \*\*addr, size\_t \*size)](capi-native-avformat-h.md#oh_avformat_getbuffer) | 从OH\_AVFormat中读取指定长度的数据块。 |
| [bool OH\_AVFormat\_GetIntBuffer(struct OH\_AVFormat \*format, const char \*key, int32\_t \*\*addr, size\_t \*size)](capi-native-avformat-h.md#oh_avformat_getintbuffer) | 从OH\_AVFormat中读取一个int32\_t数据的数组。  需要注意的是，获取的buffer生命周期与OH\_AVFormat对象绑定，当format销毁时自动失效。  如果开发者需要长时间保持绑定，应用程序必须将数据显式复制到新分配的内存。 |
| [const char \*OH\_AVFormat\_DumpInfo(struct OH\_AVFormat \*format)](capi-native-avformat-h.md#oh_avformat_dumpinfo) | 返回OH\_AVFormat中包含的key-value组成的字符串。最大可返回1024字节的字符串，销毁format时释放字符串指针。 |
| [bool OH\_AVFormat\_SetIntBuffer(struct OH\_AVFormat \*format, const char \*key, const int32\_t \*addr, size\_t size)](capi-native-avformat-h.md#oh_avformat_setintbuffer) | 将指定长度int32\_t类型的数据块写入OH\_AVFormat。 |
| [uint32\_t OH\_AVFormat\_GetKeyCount(OH\_AVFormat \*format)](capi-native-avformat-h.md#oh_avformat_getkeycount) | 获取OH\_AVFormat中包含的键总数。 |
| [bool OH\_AVFormat\_GetKey(OH\_AVFormat \*format, uint32\_t index, const char \*\*key)](capi-native-avformat-h.md#oh_avformat_getkey) | 通过索引从OH\_AVFormat中获取键名字符串。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVPixelFormat

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVPixelFormat
```

**描述**

视频像素格式的枚举类。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| AV\_PIXEL\_FORMAT\_YUVI420 = 1 | yuv 420 planar。 |
| AV\_PIXEL\_FORMAT\_NV12 = 2 | NV12. yuv 420 semiplanar。 |
| AV\_PIXEL\_FORMAT\_NV21 = 3 | NV21. yvu 420 semiplanar。 |
| AV\_PIXEL\_FORMAT\_SURFACE\_FORMAT = 4 | 像素格式从surface获取。只作用于Surface模式，Buffer模式不生效。 |
| AV\_PIXEL\_FORMAT\_RGBA = 5 | RGBA8888。 |
| AV\_PIXEL\_FORMAT\_RGBA1010102 = 6 | RGBA1010102。  **起始版本：** 20 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVFormat\_Create()

PhonePC/2in1TabletTVWearable

```
1. struct OH_AVFormat *OH_AVFormat_Create(void)
```

**描述**

创建OH\_AVFormat实例，用于读取数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \* | 返回指向OH\_AVFormat实例的指针。系统资源不足时返回NULL。 |

### OH\_AVFormat\_CreateAudioFormat()

PhonePC/2in1TabletTVWearable

```
1. struct OH_AVFormat *OH_AVFormat_CreateAudioFormat(const char *mimeType, int32_t sampleRate, int32_t channelCount)
```

**描述**

创建音频OH\_AVFormat实例指针并预设置指定参数，用于读写数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mimeType | MIME类型描述字符串，请参阅[AVCODEC\_MIMETYPE](capi-native-avcodec-base-h.md#变量)。 |
| int32\_t sampleRate | 采样率，单位Hz。 |
| int32\_t channelCount | 声道个数，如1为单声道，2为双声道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \* | 如果创建成功，返回指向OH\_AVFormat实例的指针，如果失败，则返回NULL。  可能的失败原因：  1. 传入的mimeType为NULL。  2. 系统资源不足。 |

### OH\_AVFormat\_CreateVideoFormat()

PhonePC/2in1TabletTVWearable

```
1. struct OH_AVFormat *OH_AVFormat_CreateVideoFormat(const char *mimeType, int32_t width, int32_t height)
```

**描述**

创建视频OH\_AVFormat实例指针并预设置指定参数，用于读写数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mimeType | MIME类型描述字符串，请参阅[AVCODEC\_MIMETYPE](capi-native-avcodec-base-h.md#变量)。 |
| int32\_t width | 图像的宽度，单位为pixel。 |
| int32\_t height | 图像的高度，单位为pixel。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \* | 如果创建成功，返回指向OH\_AVFormat实例的指针，如果失败，则返回NULL。  可能的失败原因：  1. 传入的mimeType为NULL。  2. 系统资源不足。 |

### OH\_AVFormat\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_AVFormat_Destroy(struct OH_AVFormat *format)
```

**描述**

销毁OH\_AVFormat实例，不允许重复销毁。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |

### OH\_AVFormat\_Copy()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_Copy(struct OH_AVFormat *to, struct OH_AVFormat *from)
```

**描述**

复制OH\_AVFormat实例。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*to | OH\_AVFormat实例，用于接收数据。 |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*from | 指向复制数据的OH\_AVFormat实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入参数为空指针。  2. 输入的OH\_AVFormat参数结构校验失败。 |

### OH\_AVFormat\_SetIntValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetIntValue(struct OH_AVFormat *format, const char *key, int32_t value)
```

**描述**

对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋int类型的值。该接口仅能设置int类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| int32\_t value | 写入数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_SetUintValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetUintValue(struct OH_AVFormat *format, const char *key, uint32_t value)
```

**描述**

对OH\_AVFormat的key赋unsigned int类型的值。该接口仅能设置unsigned int类型的参数，具体参数类型定义请参考[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| uint32\_t value | 写入数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。 |

### OH\_AVFormat\_SetLongValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetLongValue(struct OH_AVFormat *format, const char *key, int64_t value)
```

**描述**

对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋long类型的值。该接口仅能设置long类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| int64\_t value | 写入数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_SetFloatValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetFloatValue(struct OH_AVFormat *format, const char *key, float value)
```

**描述**

对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋float类型的值。该接口仅能设置float类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| float value | 写入数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_SetDoubleValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetDoubleValue(struct OH_AVFormat *format, const char *key, double value)
```

**描述**

对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋double类型的值。该接口仅能设置double类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| double value | 写入数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_SetStringValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetStringValue(struct OH_AVFormat *format, const char *key, const char *value)
```

**描述**

对OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)赋string类型的值。该接口仅能设置string类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| const char \*value | 写入字符串数据（使用建议：设置字符长度不超过256字节）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入value为空指针。  5. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_SetBuffer()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetBuffer(struct OH_AVFormat *format, const char *key, const uint8_t *addr, size_t size)
```

**描述**

将指定长度的数据块写入OH\_AVFormat。该接口仅能设置buffer类型的参数，参数类型定义详见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md#变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| const uint8\_t \*addr | 写入数据的地址，生命周期由开发者管理。 |
| size\_t size | 写入数据的长度，范围为(0, 1]MB。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入addr为空指针。  5. size为0或超过限制1MB。  6. 设置的key对应的value类型错误。 |

### OH\_AVFormat\_GetIntValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetIntValue(struct OH_AVFormat *format, const char *key, int32_t *out)
```

**描述**

从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取int类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| int32\_t \*out | 读取数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。  5. 获取的key不存在或者未设置。 |

### OH\_AVFormat\_GetUintValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetUintValue(struct OH_AVFormat *format, const char *key, uint32_t *out)
```

**描述**

使用key从OH\_AVFormat中获取unsigned int类型的值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| uint32\_t \*out | 读取数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。 |

### OH\_AVFormat\_GetLongValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetLongValue(struct OH_AVFormat *format, const char *key, int64_t *out)
```

**描述**

从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取long类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| int64\_t \*out | 读取数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。  5. 获取的key不存在或者未设置。 |

### OH\_AVFormat\_GetFloatValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetFloatValue(struct OH_AVFormat *format, const char *key, float *out)
```

**描述**

从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取float类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| float \*out | 读取数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。  5. 获取的key不存在或者未设置。 |

### OH\_AVFormat\_GetDoubleValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetDoubleValue(struct OH_AVFormat *format, const char *key, double *out)
```

**描述**

从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取double类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| double \*out | 读取数据的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。  5. 获取的key不存在或者未设置。 |

### OH\_AVFormat\_GetStringValue()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetStringValue(struct OH_AVFormat *format, const char *key, const char **out)
```

**描述**

从OH\_AVFormat的[key](capi-codecbase.md#媒体数据键值对)获取string类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 读取数据的键。 |
| const char \*\*out | 读取string指针，out数据的生命周期与format内string对应，如果开发者需要长时间保持它，必须进行拷贝内存。out最大输出字符串长度为256字节，如果长度超过256字节，会报false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入out为空指针。  5. malloc出的out字符串资源不足。  6. 获取的key不存在或者未设置。  7. 输出out的长度超过256字节。 |

### OH\_AVFormat\_GetBuffer()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetBuffer(struct OH_AVFormat *format, const char *key, uint8_t **addr, size_t *size)
```

**描述**

从OH\_AVFormat中读取指定长度的数据块。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 要读取数据的键。 |
| uint8\_t \*\*addr | 生命周期与format相同，与format一同销毁。如果开发者需要长时间保持它，必须进行内存拷贝。 |
| size\_t \*size | 读到数据的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入addr为空指针。  5. 输入size为空指针。  6. 获取的key不存在或者未设置。 |

### OH\_AVFormat\_GetIntBuffer()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetIntBuffer(struct OH_AVFormat *format, const char *key, int32_t **addr, size_t *size)
```

**描述**

从OH\_AVFormat中读取一个int32\_t数据的数组。

需要注意的是，获取的buffer生命周期与OH\_AVFormat对象绑定，当format销毁时自动失效。

如果开发者需要长时间保持绑定，应用程序必须将数据显式复制到新分配的内存。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 要读取数据的键。 |
| int32\_t \*\*addr | 保存数据内存的指针。 |
| size\_t \*size | 读到数据的元素数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回值为true表示成功，为false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入addr为空指针。  5. 输入size为空指针。 |

### OH\_AVFormat\_DumpInfo()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_AVFormat_DumpInfo(struct OH_AVFormat *format)
```

**描述**

返回OH\_AVFormat中包含的key-value组成的字符串。最大可返回1024字节的字符串，销毁format时释放字符串指针。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 如果创建成功，返回一个由key-value组成的字符串，如果失败，则返回NULL。  可能的失败原因：  1. 传入的format为NULL。  2. 系统资源不足。 |

### OH\_AVFormat\_SetIntBuffer()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_SetIntBuffer(struct OH_AVFormat *format, const char *key, const int32_t *addr, size_t size)
```

**描述**

将指定长度int32\_t类型的数据块写入OH\_AVFormat。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |
| const char \*key | 写入数据的键。 |
| const int32\_t \*addr | 写入数据的地址，生命周期由开发者管理。 |
| size\_t size | 写入数据的长度（以元素为单位，不是字节数）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示成功，返回false表示失败。  可能的失败原因：  1. 输入format为空指针。  2. 输入format参数结构校验失败。  3. 输入key为空指针。  4. 输入addr为空指针。  5. 输入size为0。 |

### OH\_AVFormat\_GetKeyCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_AVFormat_GetKeyCount(OH_AVFormat *format)
```

**描述**

获取OH\_AVFormat中包含的键总数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向一个OH\_AVFormat实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 成功时返回键的数量；失败时返回 0。 |

### OH\_AVFormat\_GetKey()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVFormat_GetKey(OH_AVFormat *format, uint32_t index, const char **key)
```

**描述**

通过索引从OH\_AVFormat中获取键名字符串。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向一个OH\_AVFormat实例的指针。 |
| uint32\_t index | 要查询键的索引值，取值范围为[0, OH\_AVFormat\_GetKeyCount(format))。 |
| const char \*\*key | 用于接收键名字符串的输出指针；该字符串的生命周期与format绑定。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 成功时返回true，失败时返回false。 |
