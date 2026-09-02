---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-archive-errcode-h
title: oh_archive_errcode.h
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 头文件 > oh_archive_errcode.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5cfb9654cc42e704af505f0288073d2b9b58f0ba4824b059205a993301d93743
---

## 概述

提供压缩解压模块错误码的声明。

**引用文件：** <filemanagement/archive/oh\_archive\_errcode.h>

**库：** liboharchive.so

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 26.0.0

**相关模块：** [Archive](capi-archive.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Archive\_ErrCode](capi-oh-archive-errcode-h.md#oh_archive_errcode) | OH\_Archive\_ErrCode | 压缩解压模块错误码。 |

## 枚举类型说明

### OH\_Archive\_ErrCode

```c
enum OH_Archive_ErrCode
```

**描述**

压缩解压模块错误码。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ARCHIVE\_OK = 0 | 操作成功。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_PARAM\_ERROR = 401 | 无效入参。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_UNKNOWN\_ERROR = 13900100 | 未知错误。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_CANCEL\_ERROR = 13900101 | 用户取消操作。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_UNSUPPORTED\_ERROR = 13900102 | 不支持当前压缩算法。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_MEM\_ERROR = 13900103 | 内存分配失败。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_OPEN\_ERROR = 13900104 | 打开压缩包文件失败。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_WRITE\_ERROR = 13900105 | 写操作失败。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_READ\_ERROR = 13900106 | 读操作失败。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_STREAM\_OUTPUT\_ERROR = 13900107 | 流输出错误。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_INSUFFICIENT\_OUTBUF\_ERROR = 13900108 | 输出缓冲区空间不足。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_NO\_SPACE\_ERROR = 13900200 | 磁盘空间不足。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_PATH\_NOT\_EXIST\_ERROR = 13900201 | 路径不存在。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_PATH\_EXISTS\_ERROR = 13900202 | 路径已存在。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_PATH\_ACCESS\_ERROR = 13900203 | 路径访问错误。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_NAME\_TOO\_LONG\_ERROR = 13900204 | 文件名过长。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_FULL\_PATH\_TOO\_LONG\_ERROR = 13900205 | 完整路径过长。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_DATA\_ERROR = 13900300 | 数据完整性错误。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_CRC\_ERROR = 13900301 | CRC校验错误。  **起始版本：** 26.0.0 |
| OH\_ARCHIVE\_DEFLATE\_ERROR = 13900302 | DEFLATE算法错误。  **起始版本：** 26.0.0 |
