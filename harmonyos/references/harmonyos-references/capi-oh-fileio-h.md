---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-fileio-h
title: oh_fileio.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_fileio.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:93618455af4013d317dc4542286183c865f98e1a7fb1377cc9819bfb530d919b
---

## 概述

PhonePC/2in1TabletTVWearable

fileio模块接口定义，提供获取文件存储位置的native接口。

**引用文件：** <filemanagement/fileio/oh\_fileio.h>

**库：** libohfileio.so

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**相关模块：** [FileIO](capi-fileio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileIO\_FileLocation](capi-oh-fileio-h.md#fileio_filelocation) | FileIO\_FileLocation | 文件存储位置枚举值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location)](capi-oh-fileio-h.md#oh_fileio_getfilelocation) | 获取文件存储位置。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### FileIO\_FileLocation

PhonePC/2in1TabletTVWearable

```
1. enum FileIO_FileLocation
```

**描述**

文件存储位置枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| LOCAL = 1 | 文件存储于本地。 |
| CLOUD = 2 | 文件存储于云侧。 |
| LOCAL\_AND\_CLOUD = 3 | 文件存储于本地及云侧。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_FileIO\_GetFileLocation()

PhonePC/2in1TabletTVWearable

```
1. FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location)
```

**描述**

获取文件存储位置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*uri | 指向入参uri的指针。 |
| int uriLength | 入参uri字符串的长度。 |
| [FileIO\_FileLocation](capi-oh-fileio-h.md#fileio_filelocation) \*location | 输出文件存储位置的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode)。 |
