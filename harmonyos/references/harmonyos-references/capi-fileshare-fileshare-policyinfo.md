---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyinfo
title: FileShare_PolicyInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > FileShare_PolicyInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:05:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aa76afbd902806e902e9f728e637288da3f3429982ebb8b7e7d87d7c646254b
---

```
1. typedef struct FileShare_PolicyInfo {...} FileShare_PolicyInfo
```

## 概述

PhonePC/2in1Tablet

需要授予或使能权限URI的策略信息。

**起始版本：** 12

**相关模块：** [fileShare](capi-fileshare.md)

**所在头文件：** [oh\_file\_share.h](capi-oh-file-share-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*uri | 需要授予或使能权限的URI。 |
| unsigned int length | URI的字节长度。 |
| unsigned int operationMode | 授予或使能权限的URI访问模式。  示例：FileShare\_OperationMode.READ\_MODE 、 FileShare\_OperationMode.WRITE\_MODE  或者 FileShare\_OperationMode.READ\_MODE|FileShare\_OperationMode.WRITE\_MODE。 |
