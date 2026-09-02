---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h
title: error_code.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cdc858e5fc47bce8239d088450d6eea6ad36b5f0a0074f22f0c9d2b031813f32
---

## 概述

提供文件管理模块的错误码定义。

**引用文件：** <filemanagement/fileio/error\_code.h>

**库：** NA

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**相关模块：** [FileIO](capi-fileio.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | FileManagement\_ErrCode | 文件管理模块错误码。 |

## 枚举类型说明

### FileManagement\_ErrCode

```c
enum FileManagement_ErrCode
```

**描述**

文件管理模块错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ERR\_OK = 0 | 接口调用成功。 |
| ERR\_PERMISSION\_ERROR = 201 | 接口权限校验失败。 |
| ERR\_INVALID\_PARAMETER = 401 | 无效入参。 |
| ERR\_DEVICE\_NOT\_SUPPORTED = 801 | 当前设备不支持此接口。 |
| ERR\_EPERM = 13900001 | 操作不被允许。 |
| ERR\_ENOENT = 13900002 | 不存在此文件或文件夹。 |
| ERR\_ENOMEM = 13900011 | 内存溢出。 |
| ERR\_UNKNOWN = 13900042 | 内部未知错误。 |
