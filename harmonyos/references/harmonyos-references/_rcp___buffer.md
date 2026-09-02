---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer
title: Rcp_Buffer
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Buffer
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:241a10a1b5ada982f4fbd16226ec962829a8e4b5e09f5df806222042741ad512
---

## 概述

文本存储结构。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \* [buffer](_rcp___buffer.md#buffer) | 内容。 |
| uint32\_t [length](_rcp___buffer.md#length) | 内容长度。 |

## 结构体成员变量说明

### buffer

```cpp
const char* Rcp_Buffer::buffer
```

**描述**

文本内容。

### length

```cpp
uint32_t Rcp_Buffer::length
```

**描述**

文本内容长度。
