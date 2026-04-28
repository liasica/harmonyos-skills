---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h
title: error_code.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e5949dcf7629cb94d3fb20a2753e39c13126b7ffca53e0f6dc8e8670c7c2ef3a
---

## 概述

PhonePC/2in1TabletTVWearable

提供文件管理模块的错误码定义。

**引用文件：** <filemanagement/fileio/error\_code.h>

**库：** NA

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**相关模块：** [FileIO](capi-fileio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [FileManagement\_ErrCode](capi-error-code-h.md#filemanagement_errcode) | FileManagement\_ErrCode | 文件管理模块错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### FileManagement\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum FileManagement_ErrCode
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
