---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativebridge-hms-nativebridge-addrinfo
title: HMS_NativeBridge_AddrInfo
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > C API > 结构体 > HMS_NativeBridge_AddrInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:56:12+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:22c767c0c3ad8fb02f649ead909a4d3996b768a63a14ca0bd1d195def021c6e5
---

```c
typedef struct {...} HMS_NativeBridge_AddrInfo
```

## 概述

应用的地址信息结构体。

**起始版本：** 26.0.1

**相关模块：** [NativeBridge](capi-nativebridge.md)

**所在头文件：** [wear\_engine\_slim.h](capi-wear-engine-slim-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t sucCallback | 成功回调函数地址。  **起始版本：** 26.0.1 |
| uint32\_t failCallback | 失败回调函数地址。  **起始版本：** 26.0.1 |
| uint32\_t context | 应用上下文地址。  **起始版本：** 26.0.1 |
| uint32\_t node | 本地节点地址。  **起始版本：** 26.0.1 |
