---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request
title: Http_Request
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Request
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:421773e6419f873152efd6963ebf48c265b7919facce1ad65b1a44dce6804737
---

```c
typedef struct Http_Request {...} Http_Request
```

## 概述

HTTP请求结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t requestId | HTTP请求的ID。 |
| char \*url | HTTP请求的URL。 |
| [Http\_RequestOptions](capi-netstack-http-requestoptions.md) \*options | HTTP请求配置，指向Http\_RequestOptions的指针，参考[Http\_RequestOptions](capi-netstack-http-requestoptions.md)。 |
