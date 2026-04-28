---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h
title: raw_file.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > raw_file.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:789bb916ff2ff0f2bf3f59618941a38f3472915b508b9b4b8014eb39b8608efa
---

## 概述

PhonePC/2in1TabletTVWearable

提供rawfile文件相关功能，功能包括搜索、读取和关闭。

**引用文件：** <rawfile/raw\_file.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：** [rawfile](capi-rawfile.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) | RawFileDescriptor | 提供rawfile文件描述符信息。RawFileDescriptor是[OH\_ResourceManager\_GetRawFileDescriptor](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。 |
| [RawFileDescriptor64](capi-rawfile-rawfiledescriptor64.md) | RawFileDescriptor64 | 提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH\_ResourceManager\_GetRawFileDescriptor64](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor64)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。 |
| [RawFile](capi-rawfile-rawfile.md) | RawFile | 提供对rawfile的访问功能。 |
| [RawFile64](capi-rawfile-rawfile64.md) | RawFile64 | 提供对较大rawfile的访问功能。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length)](capi-raw-file-h.md#oh_resourcemanager_readrawfile) | 读取rawfile内容，从当前位置读取指定长度的数据。 |
| [int OH\_ResourceManager\_SeekRawFile(const RawFile \*rawFile, long offset, int whence)](capi-raw-file-h.md#oh_resourcemanager_seekrawfile) | 基于指定的偏移量，在rawfile文件内搜索读写数据的位置。 |
| [long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfilesize) | 获取rawfile长度，单位为long。 |
| [long OH\_ResourceManager\_GetRawFileRemainingLength(const RawFile \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfileremaininglength) | 获取rawfile的剩余长度，单位为long。 |
| [void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_closerawfile) | 关闭已打开的[RawFile](capi-rawfile-rawfile.md) 以及释放所有相关联的资源。 |
| [long OH\_ResourceManager\_GetRawFileOffset(const RawFile \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfileoffset) | 获取rawfile当前的偏移量，单位为long。 |
| [bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor)](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor) | 基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。(API12废弃) |
| [bool OH\_ResourceManager\_GetRawFileDescriptorData(const RawFile \*rawFile, RawFileDescriptor \*descriptor)](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptordata) | 基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。 |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptor) | 关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。(API12废弃) |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptorData(const RawFileDescriptor \*descriptor)](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptordata) | 关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。 |
| [int64\_t OH\_ResourceManager\_ReadRawFile64(const RawFile64 \*rawFile, void \*buf, int64\_t length)](capi-raw-file-h.md#oh_resourcemanager_readrawfile64) | 读取较大的rawfile文件内容，从当前位置读取指定长度的数据。 |
| [int OH\_ResourceManager\_SeekRawFile64(const RawFile64 \*rawFile, int64\_t offset, int whence)](capi-raw-file-h.md#oh_resourcemanager_seekrawfile64) | 基于指定的偏移量，在较大的rawfile文件内搜索读写数据的位置。 |
| [int64\_t OH\_ResourceManager\_GetRawFileSize64(RawFile64 \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfilesize64) | 获取较大rawfile文件的长度，单位为int64\_t。 |
| [int64\_t OH\_ResourceManager\_GetRawFileRemainingLength64(const RawFile64 \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfileremaininglength64) | 获取较大rawfile的剩余长度，单位为int64\_t。 |
| [void OH\_ResourceManager\_CloseRawFile64(RawFile64 \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_closerawfile64) | 关闭已打开的[RawFile64](capi-rawfile-rawfile64.md) 以及释放所有相关联的资源。 |
| [int64\_t OH\_ResourceManager\_GetRawFileOffset64(const RawFile64 \*rawFile)](capi-raw-file-h.md#oh_resourcemanager_getrawfileoffset64) | 获取较大rawfile文件的偏移量，单位为int64\_t。 |
| [bool OH\_ResourceManager\_GetRawFileDescriptor64(const RawFile64 \*rawFile, RawFileDescriptor64 \*descriptor)](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptor64) | 基于偏移量（单位为int64\_t）和文件长度（单位为int64\_t）打开较大的rawfile，并获取文件描述符。打开的文件描述符被用于读取rawfile。 |
| [bool OH\_ResourceManager\_ReleaseRawFileDescriptor64(const RawFileDescriptor64 \*descriptor)](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptor64) | 关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ResourceManager\_ReadRawFile()

PhonePC/2in1TabletTVWearable

```
1. int OH_ResourceManager_ReadRawFile(const RawFile *rawFile, void *buf, size_t length)
```

**描述**

读取rawfile内容，从当前位置读取指定长度的数据。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |
| void \*buf | 用于接收读取数据的缓冲区指针。 |
| size\_t length | 读取数据的字节长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回读取的字节数，如果读取长度超过文件末尾长度或者rawfile为空时，则返回0。 |

### OH\_ResourceManager\_SeekRawFile()

PhonePC/2in1TabletTVWearable

```
1. int OH_ResourceManager_SeekRawFile(const RawFile *rawFile, long offset, int whence)
```

**描述**

基于指定的偏移量，在rawfile文件内搜索读写数据的位置。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |
| long offset | 表示指定的偏移量。 |
| int whence | 读写位置，有以下场景:  0: 读写位置为文件起始位置加上offset。  1: 读写位置为当前位置加上offset。  2: 读写位置为文件末尾加上offset。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 如果搜索成功返回0，如果发生错误返回-1。 |

### OH\_ResourceManager\_GetRawFileSize()

PhonePC/2in1TabletTVWearable

```
1. long OH_ResourceManager_GetRawFileSize(RawFile *rawFile)
```

**描述**

获取rawfile长度，单位为long。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| long | 返回rawfile的整体长度，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_GetRawFileRemainingLength()

PhonePC/2in1TabletTVWearable

```
1. long OH_ResourceManager_GetRawFileRemainingLength(const RawFile *rawFile)
```

**描述**

获取rawfile的剩余长度，单位为long。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| long | 返回rawfile的剩余长度，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_CloseRawFile()

PhonePC/2in1TabletTVWearable

```
1. void OH_ResourceManager_CloseRawFile(RawFile *rawFile)
```

**描述**

关闭已打开的[RawFile](capi-rawfile-rawfile.md) 以及释放所有相关联的资源。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |

**参考：**

[OH\_ResourceManager\_OpenRawFile](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile)

### OH\_ResourceManager\_GetRawFileOffset()

PhonePC/2in1TabletTVWearable

```
1. long OH_ResourceManager_GetRawFileOffset(const RawFile *rawFile)
```

**描述**

获取rawfile当前的偏移量，单位为long。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| long | 返回rawfile当前的偏移量，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_GetRawFileDescriptor()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_GetRawFileDescriptor(const RawFile *rawFile, RawFileDescriptor &descriptor)
```

**描述**

基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 8

**废弃版本：** 12

**替代接口：** [OH\_ResourceManager\_GetRawFileDescriptorData](capi-raw-file-h.md#oh_resourcemanager_getrawfiledescriptordata)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |
| RawFileDescriptor &descriptor | 显示rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。 |

### OH\_ResourceManager\_GetRawFileDescriptorData()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_GetRawFileDescriptorData(const RawFile *rawFile, RawFileDescriptor *descriptor)
```

**描述**

基于偏移量（单位为long）和文件长度（单位为long）打开rawfile，并获取rawfile文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile](capi-rawfile-rawfile.md) \*rawFile | 表示指向[RawFile](capi-rawfile-rawfile.md)的指针。 |
| [RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) \*descriptor | 显示rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。 |

### OH\_ResourceManager\_ReleaseRawFileDescriptor()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_ReleaseRawFileDescriptor(const RawFileDescriptor &descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 8

**废弃版本：** 12

**替代接口：** [OH\_ResourceManager\_ReleaseRawFileDescriptorData](capi-raw-file-h.md#oh_resourcemanager_releaserawfiledescriptordata)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) &descriptor | 包含rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。 |

### OH\_ResourceManager\_ReleaseRawFileDescriptorData()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_ReleaseRawFileDescriptorData(const RawFileDescriptor *descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFileDescriptor](capi-rawfile-rawfiledescriptor.md) \*descriptor | 包含rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。 |

### OH\_ResourceManager\_ReadRawFile64()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_ResourceManager_ReadRawFile64(const RawFile64 *rawFile, void *buf, int64_t length)
```

**描述**

读取较大的rawfile文件内容，从当前位置读取指定长度的数据。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |
| void \*buf | 用于接收读取数据的缓冲区指针。 |
| int64\_t length | 读取数据的字节长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回读取的字节数，如果读取长度超过文件末尾长度或者rawfile为空时，则返回0。 |

### OH\_ResourceManager\_SeekRawFile64()

PhonePC/2in1TabletTVWearable

```
1. int OH_ResourceManager_SeekRawFile64(const RawFile64 *rawFile, int64_t offset, int whence)
```

**描述**

基于指定的偏移量，在较大的rawfile文件内搜索读写数据的位置。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |
| int64\_t offset | 表示指定的偏移量。 |
| int whence | 读写位置，有以下场景:  0: 读写位置为文件起始位置加上offset。  1: 读写位置为当前位置加上offset。  2: 读写位置为文件末尾加上offset。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 如果搜索成功返回0，如果发生错误返回-1。 |

### OH\_ResourceManager\_GetRawFileSize64()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_ResourceManager_GetRawFileSize64(RawFile64 *rawFile)
```

**描述**

获取较大rawfile文件的长度，单位为int64\_t。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回rawfile的整体长度，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_GetRawFileRemainingLength64()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_ResourceManager_GetRawFileRemainingLength64(const RawFile64 *rawFile)
```

**描述**

获取较大rawfile的剩余长度，单位为int64\_t。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回rawfile的剩余长度，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_CloseRawFile64()

PhonePC/2in1TabletTVWearable

```
1. void OH_ResourceManager_CloseRawFile64(RawFile64 *rawFile)
```

**描述**

关闭已打开的[RawFile64](capi-rawfile-rawfile64.md) 以及释放所有相关联的资源。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |

**参考：**

[OH\_ResourceManager\_OpenRawFile64](capi-raw-file-manager-h.md#oh_resourcemanager_openrawfile64)

### OH\_ResourceManager\_GetRawFileOffset64()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_ResourceManager_GetRawFileOffset64(const RawFile64 *rawFile)
```

**描述**

获取较大rawfile文件的偏移量，单位为int64\_t。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回rawfile当前的偏移量，如果rawfile为空时返回0。 |

### OH\_ResourceManager\_GetRawFileDescriptor64()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_GetRawFileDescriptor64(const RawFile64 *rawFile, RawFileDescriptor64 *descriptor)
```

**描述**

基于偏移量（单位为int64\_t）和文件长度（单位为int64\_t）打开较大的rawfile，并获取文件描述符。打开的文件描述符被用于读取rawfile。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFile64](capi-rawfile-rawfile64.md) \*rawFile | 表示指向[RawFile64](capi-rawfile-rawfile64.md)的指针。 |
| [RawFileDescriptor64](capi-rawfile-rawfiledescriptor64.md) \*descriptor | 显示rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示打开rawfile文件描述符成功，返回false表示rawfile不允许被访问。 |

### OH\_ResourceManager\_ReleaseRawFileDescriptor64()

PhonePC/2in1TabletTVWearable

```
1. bool OH_ResourceManager_ReleaseRawFileDescriptor64(const RawFileDescriptor64 *descriptor)
```

**描述**

关闭rawfile文件描述符。已打开的文件描述符在使用完以后必须释放，防止文件描述符泄露。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const RawFileDescriptor64](capi-rawfile-rawfiledescriptor64.md) \*descriptor | 包含rawfile文件描述符，以及在HAP包中的起始位置和长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示关闭文件描述符成功，返回false表示关闭文件描述符失败。 |
