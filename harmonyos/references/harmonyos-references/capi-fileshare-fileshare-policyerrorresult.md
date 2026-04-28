---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyerrorresult
title: FileShare_PolicyErrorResult
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > FileShare_PolicyErrorResult
category: harmonyos-references
scraped_at: 2026-04-28T08:05:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:27e93cde843fa41498129e09df3d38d071934009799dedc6b4b095bac3b88edd
---

```
1. typedef struct FileShare_PolicyErrorResult {...} FileShare_PolicyErrorResult
```

## 概述

PhonePC/2in1Tablet

授予或使能权限失败的URI策略结果。

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

**所在头文件：** [oh\_file\_share.h](capi-oh-file-share-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*uri | 授予或使能策略失败的URI。 |
| [FileShare\_PolicyErrorCode](capi-oh-file-share-h.md#fileshare_policyerrorcode) code | 授予或使能策略失败的URI对应的错误码。 |
| char \*message | 授予或使能策略失败的URI对应的原因。 |
