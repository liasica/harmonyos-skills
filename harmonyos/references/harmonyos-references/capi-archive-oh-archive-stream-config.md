---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive-oh-archive-stream-config
title: OH_Archive_Stream_Config
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_Archive_Stream_Config
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b5aaba945e02325394bcd67da474bc7b1fa7d1c2cc88bb8015c326bf5b6291ef
---

```c
typedef struct {...} OH_Archive_Stream_Config
```

## 概述

流式压缩配置结构体。

**起始版本：** 26.0.0

**相关模块：** [Archive](capi-archive.md)

**所在头文件：** [oh\_archive.h](capi-oh-archive-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t blockSize | 内存块大小，单位为bytes。当[OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod)设置为OH\_ARCHIVE\_COMPRESS\_DEFLATE时，blockSize需不小于32768bytes。  **起始版本：** 26.0.0 |
| int32\_t threadNum | 线程数，取值为正整数，如果大于设备核数，则使用设备核数。  **起始版本：** 26.0.0 |
| [OH\_Archive\_StreamChecksumAlg](capi-oh-archive-h.md#oh_archive_streamchecksumalg) checksum | 用于计算校验和的哈希算法。  **起始版本：** 26.0.0 |
| [OH\_Archive\_CompressMethod](capi-oh-archive-h.md#oh_archive_compressmethod) method | 压缩算法。流式压缩和流式解压缩只支持OH\_ARCHIVE\_COMPRESS\_DEFLATE。  **起始版本：** 26.0.0 |
