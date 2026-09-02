---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-archive-h
title: oh_archive.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_archive.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91a2a301dde32d2f1c7d4c7a6afe338d989292fab66af67b0c3380e0021da857
---

## 概述

压缩解压缩模块接口定义，提供文件压缩解压缩、数据的流式压缩解压缩，缓冲区压缩解压缩的native接口。

**引用文件：** <filemanagement/archive/oh\_archive.h>

**库：** liboharchive.so

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 26.0.0

**相关模块：** [Archive](capi-archive.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Archive\_StreamInfo](capi-archive-oh-archive-streaminfo.md) | OH\_Archive\_StreamInfo | 流式压缩/解压缩信息结构体。 |
| [OH\_Archive\_Stream\_Config](capi-archive-oh-archive-stream-config.md) | OH\_Archive\_Stream\_Config | 流式压缩配置结构体。 |
| [ArchiveWriteCtx\*](capi-archive-archivewritectx.md) | OH\_Archive\_Writer\_Ctx | 文件压缩器的上下文结构体指针。 |
| [ArchiveReadCtx\*](capi-archive-archivereadctx.md) | OH\_Archive\_Reader\_Ctx | 文件解压缩器的上下文结构体指针。 |
| [ArchiveStreamWriteCtx\*](capi-archive-archivestreamwritectx.md) | OH\_Archive\_StreamWrite\_Ctx | 流式压缩器的上下文结构体指针。 |
| [ArchiveStreamReadCtx\*](capi-archive-archivestreamreadctx.md) | OH\_Archive\_StreamRead\_Ctx | 流式解压缩器的上下文结构体指针。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Archive\_Format](capi-oh-archive-h.md#oh_archive_format) | OH\_Archive\_Format | 文件格式枚举。 |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) | OH\_Archive\_CompressMethod | 压缩算法枚举。 |
| [OH\_Archive\_OpenMode](capi-oh-archive-h.md#oh_archive_openmode) | OH\_Archive\_OpenMode | 文件打开模式枚举。 |
| [OH\_Archive\_ProgressType](capi-oh-archive-h.md#oh_archive_progresstype) | OH\_Archive\_ProgressType | 文件进度控制类型枚举。 |
| [OH\_Archive\_StreamChecksumAlg](capi-oh-archive-h.md#oh_archive_streamchecksumalg) | OH\_Archive\_StreamChecksumAlg | 用于计算校验和的哈希算法。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef OH\_Archive\_ProgressType (\*OH\_Archive\_ProgressHandlerWithData)(int32\_t progress, void \*userData)](capi-oh-archive-h.md#oh_archive_progresshandlerwithdata) | OH\_Archive\_ProgressHandlerWithData | 定义进度处理回调函数的类型。 |
| [typedef uint64\_t (\*OH\_Archive\_Stream\_OutputHandler)(const void\* data, uint64\_t size, void\* userData)](capi-oh-archive-h.md#oh_archive_stream_outputhandler) | OH\_Archive\_Stream\_OutputHandler | 用户自定义回调函数指针类型，用于处理压缩后的数据。 |
| [OH\_Archive\_Reader\_Ctx OH\_Archive\_Reader\_OpenFile(const char \*infile)](capi-oh-archive-h.md#oh_archive_reader_openfile) | - | 打开文件进行读取。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Reader\_SetProgressHandlerWithData(OH\_Archive\_Reader\_Ctx arc, OH\_Archive\_ProgressHandlerWithData progressHandler, void \*userData)](capi-oh-archive-h.md#oh_archive_reader_setprogresshandlerwithdata) | - | 设置文件解压缩器的进度回调函数及用户数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Reader\_ExtractAllFile(OH\_Archive\_Reader\_Ctx arc, const char \*outDir)](capi-oh-archive-h.md#oh_archive_reader_extractallfile) | - | 从压缩包中提取所有文件。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Reader\_Close(OH\_Archive\_Reader\_Ctx arc)](capi-oh-archive-h.md#oh_archive_reader_close) | - | 关闭已打开的压缩文件并释放相关资源。 |
| [OH\_Archive\_Writer\_Ctx OH\_Archive\_Writer\_OpenFile(const char \*outfile, OH\_Archive\_OpenMode openMode, OH\_Archive\_Format fmt)](capi-oh-archive-h.md#oh_archive_writer_openfile) | - | 创建并打开压缩文件。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Writer\_SetCompressMethod(OH\_Archive\_Writer\_Ctx arc, OH\_Archive\_CompressMethod method, int32\_t compressLevel)](capi-oh-archive-h.md#oh_archive_writer_setcompressmethod) | - | 设置压缩文件的压缩算法。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Writer\_SetProgressHandlerWithData(OH\_Archive\_Writer\_Ctx arc, OH\_Archive\_ProgressHandlerWithData progressHandler, void \*userData)](capi-oh-archive-h.md#oh_archive_writer_setprogresshandlerwithdata) | - | 设置文件压缩器的进度回调函数及用户数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Writer\_Add(OH\_Archive\_Writer\_Ctx arc, const char \*\*infiles, uint64\_t fileNum)](capi-oh-archive-h.md#oh_archive_writer_add) | - | 向压缩包中添加文件列表。 |
| [OH\_Archive\_ErrCode OH\_Archive\_Writer\_Close(OH\_Archive\_Writer\_Ctx arc)](capi-oh-archive-h.md#oh_archive_writer_close) | - | 关闭文件压缩器。该函数完成压缩包写入过程，将缓冲数据刷新到输出，并释放与文件压缩器的上下文结构体相关的资源。 |
| [uint64\_t OH\_Archive\_BufferWriteCompressBound(OH\_Archive\_CompressMethod method, uint64\_t sourceLen)](capi-oh-archive-h.md#oh_archive_bufferwritecompressbound) | - | 计算给定源数据长度的最大压缩后数据大小。 |
| [OH\_Archive\_ErrCode OH\_Archive\_BufferWrite(uint8\_t \*dstBuffer, uint64\_t \*dstSize, const uint8\_t \*srcBuffer, uint64\_t srcSize, OH\_Archive\_CompressMethod method, int32\_t compressLevel)](capi-oh-archive-h.md#oh_archive_bufferwrite) | - | 向缓冲区写入数据并进行压缩。 |
| [OH\_Archive\_ErrCode OH\_Archive\_BufferRead(uint8\_t \*dstBuffer, uint64\_t \*dstSize, const uint8\_t \*srcBuffer, uint64\_t srcSize, OH\_Archive\_CompressMethod method)](capi-oh-archive-h.md#oh_archive_bufferread) | - | 从缓冲区读取数据并进行解压缩。 |
| [OH\_Archive\_StreamWrite\_Ctx OH\_Archive\_StreamWrite\_Create(OH\_Archive\_Stream\_Config config)](capi-oh-archive-h.md#oh_archive_streamwrite_create) | - | 创建流式压缩的上下文结构体。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamWrite\_Start(OH\_Archive\_StreamWrite\_Ctx ctx, OH\_Archive\_Stream\_OutputHandler outputHandler, void\* userData)](capi-oh-archive-h.md#oh_archive_streamwrite_start) | - | 启动压缩任务，初始化用户回调函数和用户数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamWrite\_SetCompressLevel(OH\_Archive\_StreamWrite\_Ctx ctx, int32\_t compressLevel)](capi-oh-archive-h.md#oh_archive_streamwrite_setcompresslevel) | - | 设置流式压缩的压缩级别。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamWrite\_Cancel(OH\_Archive\_StreamWrite\_Ctx ctx)](capi-oh-archive-h.md#oh_archive_streamwrite_cancel) | - | 强制取消当前压缩操作。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamWrite\_Update(OH\_Archive\_StreamWrite\_Ctx ctx, const uint8\_t\* data, uint64\_t size)](capi-oh-archive-h.md#oh_archive_streamwrite_update) | - | 提交压缩数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamWrite\_End(OH\_Archive\_StreamWrite\_Ctx ctx, OH\_Archive\_StreamInfo \*streamInfo)](capi-oh-archive-h.md#oh_archive_streamwrite_end) | - | 结束压缩，刷新所有剩余数据。 |
| [void OH\_Archive\_StreamWrite\_Destroy(OH\_Archive\_StreamWrite\_Ctx ctx)](capi-oh-archive-h.md#oh_archive_streamwrite_destroy) | - | 销毁压缩实例并释放相关资源。 |
| [OH\_Archive\_StreamRead\_Ctx OH\_Archive\_StreamRead\_Create(OH\_Archive\_Stream\_Config config)](capi-oh-archive-h.md#oh_archive_streamread_create) | - | 创建流式解压缩的上下文结构体。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamRead\_Start(OH\_Archive\_StreamRead\_Ctx ctx, OH\_Archive\_Stream\_OutputHandler outputHandler, void\* userData)](capi-oh-archive-h.md#oh_archive_streamread_start) | - | 启动解压缩任务，初始化用户回调函数和用户数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamRead\_Cancel(OH\_Archive\_StreamRead\_Ctx ctx)](capi-oh-archive-h.md#oh_archive_streamread_cancel) | - | 强制取消当前解压缩操作。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamRead\_Update(OH\_Archive\_StreamRead\_Ctx ctx, const uint8\_t\* data, uint64\_t size)](capi-oh-archive-h.md#oh_archive_streamread_update) | - | 提交解压缩数据。 |
| [OH\_Archive\_ErrCode OH\_Archive\_StreamRead\_End(OH\_Archive\_StreamRead\_Ctx ctx, OH\_Archive\_StreamInfo \*streamInfo)](capi-oh-archive-h.md#oh_archive_streamread_end) | - | 结束解压缩，刷新所有剩余数据并清理内存。 |
| [void OH\_Archive\_StreamRead\_Destroy(OH\_Archive\_StreamRead\_Ctx ctx)](capi-oh-archive-h.md#oh_archive_streamread_destroy) | - | 销毁解压缩实例并释放相关资源。 |

## 枚举类型说明

### OH\_Archive\_Format

```c
enum OH_Archive_Format
```

**描述**

文件格式枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_FMT\_ZIP = 0 | ZIP格式。  **起始版本：** 26.0.0 |

### OH\_Archive\_CompressMethod

```c
enum OH_Archive_CompressMethod
```

**描述**

压缩算法枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_NO\_COMPRESSION = 0 | 不压缩。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_COMPRESS\_DEFLATE = 8 | DEFLATE压缩算法。  **起始版本：** 26.0.0 |

### OH\_Archive\_OpenMode

```c
enum OH_Archive_OpenMode
```

**描述**

文件打开模式枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_OPEN\_MODE\_CREATE = 0 | 创建模式。新建一个文件，如果文件已存在，则覆盖。  **起始版本：** 26.0.0 |

### OH\_Archive\_ProgressType

```c
enum OH_Archive_ProgressType
```

**描述**

文件进度控制类型枚举。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_PROGRESS\_CONTINUE = 0 | 继续压缩/解压缩操作。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_PROGRESS\_CANCEL = 1 | 取消压缩/解压缩操作。  **起始版本：** 26.0.0 |

### OH\_Archive\_StreamChecksumAlg

```c
enum OH_Archive_StreamChecksumAlg
```

**描述**

用于计算校验和的哈希算法。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_NO\_CHECKSUM = 0 | 不额外计算哈希值。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_CRC32 = 1 | 使用CRC32（Cyclic Redundancy Check，循环冗余校验）计算校验和。  **起始版本：** 26.0.0 |

## 函数说明

### OH\_Archive\_ProgressHandlerWithData()

```c
typedef OH_Archive_ProgressType (*OH_Archive_ProgressHandlerWithData)(int32_t progress, void *userData)
```

**描述**

定义进度处理回调函数的类型。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t progress | 处理进度百分比，取值范围为[0, 100]。 |
| void \*userData | 指向用户自定义数据的指针，在调用回调时传入。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ProgressType](capi-oh-archive-h.md#oh_archive_progresstype) | OH\_ARCHIVE\_PROGRESS\_CONTINUE - 继续当前压缩/解压缩操作。  OH\_ARCHIVE\_PROGRESS\_CANCEL - 取消当前压缩/解压缩操作。 |

### OH\_Archive\_Stream\_OutputHandler()

```c
typedef uint64_t (*OH_Archive_Stream_OutputHandler)(const void* data, uint64_t size, void* userData)
```

**描述**

用户自定义回调函数指针类型，用于处理压缩后的数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void\* data | 指向压缩数据的指针。 |
| uint64\_t size | 压缩数据的长度。 |
| void\* userData | 用户自定义上下文，将在回调中传回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 成功处理的字节数。 |

### OH\_Archive\_Reader\_OpenFile()

```c
OH_Archive_Reader_Ctx OH_Archive_Reader_OpenFile(const char *infile)
```

**描述**

打开文件进行读取。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*infile | 源文件的路径，应用需要有读取权限，绝对路径长度需不超过4096bytes。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_Reader\_Ctx](capi-archive-archivereadctx.md) | 返回文件读取器的上下文结构体，操作失败时返回NULL。 |

### OH\_Archive\_Reader\_SetProgressHandlerWithData()

```c
OH_Archive_ErrCode OH_Archive_Reader_SetProgressHandlerWithData(OH_Archive_Reader_Ctx arc, OH_Archive_ProgressHandlerWithData progressHandler, void *userData)
```

**描述**

设置文件解压缩器的进度回调函数及用户数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Reader\_Ctx](capi-archive-archivereadctx.md) arc | 文件解压缩器上下文句柄。 |
| [OH\_Archive\_ProgressHandlerWithData](capi-oh-archive-h.md#oh_archive_progresshandlerwithdata) progressHandler | 用于处理进度更新的回调函数。 |
| void \*userData | 用户处理进度回调时自定义的上下文数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Reader\_ExtractAllFile()

```c
OH_Archive_ErrCode OH_Archive_Reader_ExtractAllFile(OH_Archive_Reader_Ctx arc, const char *outDir)
```

**描述**

从压缩包中提取所有文件。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Reader\_Ctx](capi-archive-archivereadctx.md) arc | 文件解压缩器上下文句柄。 |
| const char \*outDir | 输出目录路径，应用需要有写入权限。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Reader\_Close()

```c
OH_Archive_ErrCode OH_Archive_Reader_Close(OH_Archive_Reader_Ctx arc)
```

**描述**

关闭已打开的压缩文件并释放相关资源。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Reader\_Ctx](capi-archive-archivereadctx.md) arc | 文件解压缩器上下文句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Writer\_OpenFile()

```c
OH_Archive_Writer_Ctx OH_Archive_Writer_OpenFile(const char *outfile, OH_Archive_OpenMode openMode, OH_Archive_Format fmt)
```

**描述**

创建并打开压缩文件。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*outfile | 目标压缩文件的路径，应用需有写入权限，绝对路径长度需不超过4096bytes。 |
| [OH\_Archive\_OpenMode](capi-oh-archive-h.md#oh_archive_openmode) openMode | 文件打开模式。 |
| [OH\_Archive\_Format](capi-oh-archive-h.md#oh_archive_format) fmt | 压缩包格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_Writer\_Ctx](capi-archive-archivewritectx.md) | 返回文件压缩器上下文句柄，操作失败时返回NULL。 |

### OH\_Archive\_Writer\_SetCompressMethod()

```c
OH_Archive_ErrCode OH_Archive_Writer_SetCompressMethod(OH_Archive_Writer_Ctx arc, OH_Archive_CompressMethod method, int32_t compressLevel)
```

**描述**

设置压缩文件的压缩算法。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Writer\_Ctx](capi-archive-archivewritectx.md) arc | 文件压缩器的上下文句柄。 |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) method | 压缩算法。 |
| int32\_t compressLevel | 压缩等级。对于OH\_ARCHIVE\_COMPRESS\_DEFLATE，压缩级别为0到9，默认等级为6。0表示不压缩，压缩等级越高，压缩率越高，速度越慢。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Writer\_SetProgressHandlerWithData()

```c
OH_Archive_ErrCode OH_Archive_Writer_SetProgressHandlerWithData(OH_Archive_Writer_Ctx arc, OH_Archive_ProgressHandlerWithData progressHandler, void *userData)
```

**描述**

设置文件压缩器的进度回调函数及用户数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Writer\_Ctx](capi-archive-archivewritectx.md) arc | 文件压缩器上下文句柄。 |
| [OH\_Archive\_ProgressHandlerWithData](capi-oh-archive-h.md#oh_archive_progresshandlerwithdata) progressHandler | 用于处理进度更新的回调函数。 |
| void \*userData | 用户处理进度回调时自定义的上下文数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Writer\_Add()

```c
OH_Archive_ErrCode OH_Archive_Writer_Add(OH_Archive_Writer_Ctx arc, const char **infiles, uint64_t fileNum)
```

**描述**

向压缩包中添加文件列表。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Writer\_Ctx](capi-archive-archivewritectx.md) arc | 文件压缩器上下文句柄。 |
| const char \*\*infiles | 待压缩的文件。 |
| uint64\_t fileNum | 文件数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_Writer\_Close()

```c
OH_Archive_ErrCode OH_Archive_Writer_Close(OH_Archive_Writer_Ctx arc)
```

**描述**

关闭文件压缩器。该函数完成压缩包写入过程，将缓冲数据刷新到输出，并释放与文件压缩器的上下文结构体相关的资源。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Writer\_Ctx](capi-archive-archivewritectx.md) arc | 文件压缩器上下文句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_BufferWriteCompressBound()

```c
uint64_t OH_Archive_BufferWriteCompressBound(OH_Archive_CompressMethod method, uint64_t sourceLen)
```

**描述**

计算给定源数据长度的最大压缩后数据大小。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) method | 压缩算法类型。当前仅支持OH\_ARCHIVE\_COMPRESS\_DEFLATE。 |
| uint64\_t sourceLen | 待压缩源数据的长度，单位为bytes。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 返回压缩后数据大小的最大值，单位为bytes。 |

### OH\_Archive\_BufferWrite()

```c
OH_Archive_ErrCode OH_Archive_BufferWrite(uint8_t *dstBuffer, uint64_t *dstSize, const uint8_t *srcBuffer, uint64_t srcSize, OH_Archive_CompressMethod method, int32_t compressLevel)
```

**描述**

向缓冲区写入数据并进行压缩。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*dstBuffer | 指向目标缓冲区的指针，用于存储压缩后的数据。 |
| uint64\_t \*dstSize | 指向目标缓冲区大小的指针，传入缓冲区大小，输出实际写入的大小，单位为bytes。 |
| const uint8\_t \*srcBuffer | 指向包含待压缩数据的源缓冲区的指针。 |
| uint64\_t srcSize | 源缓冲区数据的大小，单位为bytes。 |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) method | 压缩算法类型。当前仅支持OH\_ARCHIVE\_COMPRESS\_DEFLATE。 |
| int32\_t compressLevel | 压缩等级。对于OH\_ARCHIVE\_COMPRESS\_DEFLATE，压缩级别为0到9，默认等级为6。0表示不压缩，压缩等级越高，压缩率越高，速度越慢。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_BufferRead()

```c
OH_Archive_ErrCode OH_Archive_BufferRead(uint8_t *dstBuffer, uint64_t *dstSize, const uint8_t *srcBuffer, uint64_t srcSize, OH_Archive_CompressMethod method)
```

**描述**

从缓冲区读取数据并进行解压缩。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint8\_t \*dstBuffer | 指向目标缓冲区的指针，用于存储解压缩后的数据。 |
| uint64\_t \*dstSize | 指向目标缓冲区大小的指针，传入缓冲区大小，输出实际解压缩后的大小，单位为bytes。 |
| const uint8\_t \*srcBuffer | 指向包含待解压缩数据的源缓冲区的指针。 |
| uint64\_t srcSize | 源缓冲区数据的大小，单位为bytes。 |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) method | 解压缩算法类型。当前仅支持OH\_ARCHIVE\_COMPRESS\_DEFLATE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_Create()

```c
OH_Archive_StreamWrite_Ctx OH_Archive_StreamWrite_Create(OH_Archive_Stream_Config config)
```

**描述**

创建流式压缩的上下文结构体。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Stream\_Config](capi-archive-oh-archive-stream-config.md) config | 压缩配置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) | 返回流式压缩的上下文结构体。创建失败时返回NULL。 |

### OH\_Archive\_StreamWrite\_Start()

```c
OH_Archive_ErrCode OH_Archive_StreamWrite_Start(OH_Archive_StreamWrite_Ctx ctx, OH_Archive_Stream_OutputHandler outputHandler, void* userData)
```

**描述**

启动压缩任务，初始化用户回调函数和用户数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |
| [OH\_Archive\_Stream\_OutputHandler](capi-oh-archive-h.md#oh_archive_stream_outputhandler) outputHandler | 用户自定义的压缩数据回调函数。 |
| void\* userData | 用户自定义上下文，将在回调中传回。userData由调用方持有，在[OH\_Archive\_StreamWrite\_End](capi-oh-archive-h.md#oh_archive_streamwrite_end)完成前必须保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_SetCompressLevel()

```c
OH_Archive_ErrCode OH_Archive_StreamWrite_SetCompressLevel(OH_Archive_StreamWrite_Ctx ctx, int32_t compressLevel)
```

**描述**

设置流式压缩的压缩级别。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |
| int32\_t compressLevel | 压缩等级。对于OH\_ARCHIVE\_COMPRESS\_DEFLATE，压缩级别为0到9，默认等级为6。0表示不压缩，压缩等级越高，压缩率越高，速度越慢。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_Cancel()

```c
OH_Archive_ErrCode OH_Archive_StreamWrite_Cancel(OH_Archive_StreamWrite_Ctx ctx)
```

**描述**

强制取消当前压缩操作。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。取消成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_Update()

```c
OH_Archive_ErrCode OH_Archive_StreamWrite_Update(OH_Archive_StreamWrite_Ctx ctx, const uint8_t* data, uint64_t size)
```

**描述**

提交压缩数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |
| const uint8\_t\* data | 待压缩的原始数据。 |
| uint64\_t size | 待压缩数据的大小，单位为bytes。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。压缩成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_End()

```c
OH_Archive_ErrCode OH_Archive_StreamWrite_End(OH_Archive_StreamWrite_Ctx ctx, OH_Archive_StreamInfo *streamInfo)
```

**描述**

结束压缩，刷新所有剩余数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |
| [OH\_Archive\_StreamInfo](capi-archive-oh-archive-streaminfo.md) \*streamInfo | 压缩信息，包括原始数据大小、压缩后数据大小和CRC32值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。压缩成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamWrite\_Destroy()

```c
void OH_Archive_StreamWrite_Destroy(OH_Archive_StreamWrite_Ctx ctx)
```

**描述**

销毁压缩实例并释放相关资源。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamWrite\_Ctx](capi-archive-archivestreamwritectx.md) ctx | 流式压缩的上下文结构体。 |

### OH\_Archive\_StreamRead\_Create()

```c
OH_Archive_StreamRead_Ctx OH_Archive_StreamRead_Create(OH_Archive_Stream_Config config)
```

**描述**

创建流式解压缩的上下文结构体。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_Stream\_Config](capi-archive-oh-archive-stream-config.md) config | 解压缩配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) | 返回流式解压缩的上下文结构体。创建失败时返回NULL。 |

### OH\_Archive\_StreamRead\_Start()

```c
OH_Archive_ErrCode OH_Archive_StreamRead_Start(OH_Archive_StreamRead_Ctx ctx, OH_Archive_Stream_OutputHandler outputHandler, void* userData)
```

**描述**

启动解压缩任务，初始化用户回调函数和用户数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) ctx | 流式解压缩的上下文结构体。 |
| [OH\_Archive\_Stream\_OutputHandler](capi-oh-archive-h.md#oh_archive_stream_outputhandler) outputHandler | 用户自定义的解压缩数据回调函数。 |
| void\* userData | 用户自定义上下文数据，将在回调中传回。userData由调用方拥有，在[OH\_Archive\_StreamRead\_End](capi-oh-archive-h.md#oh_archive_streamread_end)完成前必须保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamRead\_Cancel()

```c
OH_Archive_ErrCode OH_Archive_StreamRead_Cancel(OH_Archive_StreamRead_Ctx ctx)
```

**描述**

强制取消当前解压缩操作。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) ctx | 流式解压缩的上下文结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。取消成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamRead\_Update()

```c
OH_Archive_ErrCode OH_Archive_StreamRead_Update(OH_Archive_StreamRead_Ctx ctx, const uint8_t* data, uint64_t size)
```

**描述**

提交解压缩数据。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) ctx | 流式解压缩的上下文结构体。 |
| const uint8\_t\* data | 待解压缩的数据。 |
| uint64\_t size | 数据大小，单位为bytes。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamRead\_End()

```c
OH_Archive_ErrCode OH_Archive_StreamRead_End(OH_Archive_StreamRead_Ctx ctx, OH_Archive_StreamInfo *streamInfo)
```

**描述**

结束解压缩，刷新所有剩余数据并清理内存。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) ctx | 流式解压缩的上下文结构体。 |
| [OH\_Archive\_StreamInfo](capi-archive-oh-archive-streaminfo.md) \*streamInfo | 解压缩信息，包括原始数据大小、压缩后数据大小和CRC32值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | 返回接口执行的结果。成功返回OH\_ARCHIVE\_OK，失败返回对应错误码。 |

### OH\_Archive\_StreamRead\_Destroy()

```c
void OH_Archive_StreamRead_Destroy(OH_Archive_StreamRead_Ctx ctx)
```

**描述**

销毁解压缩实例并释放相关资源。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Archive\_StreamRead\_Ctx](capi-archive-archivestreamreadctx.md) ctx | 流式解压缩的上下文结构体。 |
