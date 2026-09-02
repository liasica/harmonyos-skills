---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyinfo
title: FileShare_PolicyInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > FileShare_PolicyInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ee0175287121038fa392982f2d29b997c9628468bb4111e4e2293ae2babde7b7
---

```c
typedef struct FileShare_PolicyInfo {...} FileShare_PolicyInfo
```

## 概述

需要授予或激活URI访问权限的策略信息，用于描述跨应用文件共享场景中的目标URI和访问模式。

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

**所在头文件：** [oh\_file\_share.h](capi-oh-file-share-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*uri | 需要授予或激活访问权限的URI，需符合系统URI格式规范。 |
| unsigned int length | uri指向字符串的字节长度，不包含字符串结束符'\0'。 |
| unsigned int operationMode | 授予或激活权限的URI访问模式。READ\_MODE表示读取权限，WRITE\_MODE表示写入权限。  示例：FileShare\_OperationMode.READ\_MODE、FileShare\_OperationMode.WRITE\_MODE，  或者 FileShare\_OperationMode.READ\_MODE|FileShare\_OperationMode.WRITE\_MODE。 |
