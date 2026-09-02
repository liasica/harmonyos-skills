---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer
title: Http_Buffer
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Buffer
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de1e1d0cc677c70f22225a9ca6cf40a44b31946fc50c8ad12e1e29426d570290
---

```c
typedef struct Http_Buffer {...} Http_Buffer
```

## 概述

HTTP缓存结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*buffer | 缓冲区数据。 |
| uint32\_t length | 缓冲区长度。单位：Byte。 |
