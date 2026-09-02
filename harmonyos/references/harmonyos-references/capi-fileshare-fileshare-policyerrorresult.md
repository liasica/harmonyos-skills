---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyerrorresult
title: FileShare_PolicyErrorResult
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > FileShare_PolicyErrorResult
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:53d952655672228e8ab52c46dec13238230912c581484303e9ddfd644918d0a8
---

```c
typedef struct FileShare_PolicyErrorResult {...} FileShare_PolicyErrorResult
```

## 概述

授予或激活权限失败的URI策略结果，用于记录失败URI、错误码和失败原因。

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

**所在头文件：** [oh\_file\_share.h](capi-oh-file-share-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*uri | 授予或激活权限失败的URI。 |
| [FileShare\_PolicyErrorCode](capi-oh-file-share-h.md#fileshare_policyerrorcode) code | 授予或激活权限失败的URI对应的错误码。 |
| char \*message | 授予或激活权限失败的URI对应的原因，由系统管理，无需手动释放。 |
