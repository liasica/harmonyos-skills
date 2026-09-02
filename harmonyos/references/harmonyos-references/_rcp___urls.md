---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls
title: Rcp_Urls
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Urls
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cb85562ff89e87667e13cba7e5552eb60d51b0550c0aca1eb8e66648eacd487f
---

## 概述

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___urls.md#url) | 匹配的URL。 |
| struct [Rcp\_Urls](_rcp___urls.md) \* [next](_rcp___urls.md#next) | 链式存储。指向下一个[Rcp\_Urls](_rcp___urls.md)的指针。 |

## 结构体成员变量说明

### next

```cpp
struct Rcp_Urls* Rcp_Urls::next
```

**描述**

链式存储。指向下一个[Rcp\_Urls](_rcp___urls.md)的指针。

### url

```cpp
const char* Rcp_Urls::url
```

**描述**

匹配的URL。
