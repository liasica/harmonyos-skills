---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-archive-oh-archive-streaminfo
title: OH_Archive_StreamInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_Archive_StreamInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4a8d262111f360f03bf614d2384f8cf70f98e456e1f116c2ff2f62fa0856f75c
---

```c
typedef struct {...} OH_Archive_StreamInfo
```

## 概述

流式压缩/解压缩信息结构体。

**起始版本：** 26.0.0

**相关模块：** [Archive](capi-archive.md)

**所在头文件：** [oh\_archive.h](capi-oh-archive-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t totalInSize | 压缩/解压缩前输入数据大小，单位为bytes。  **起始版本：** 26.0.0 |
| uint64\_t totalOutSize | 压缩/解压缩后输出数据大小，单位为bytes。  **起始版本：** 26.0.0 |
| uint32\_t checksum | 未压缩数据的校验和。当[OH\_Archive\_StreamChecksumAlg](capi-oh-archive-h.md#oh_archive_streamchecksumalg)设置为OH\_ARCHIVE\_NO\_CHECKSUM时，checksum为0。  **起始版本：** 26.0.0 |
