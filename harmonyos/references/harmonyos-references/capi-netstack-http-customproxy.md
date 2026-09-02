---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy
title: Http_CustomProxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_CustomProxy
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:22bae28996d2a83fa5074d8fb7bb1d14320bfb9597580900157a435ff47b9bd5
---

```c
typedef struct Http_CustomProxy {...} Http_CustomProxy
```

## 概述

用户自定义代理配置。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*host | 代理服务器主机名，如果没有显式设置端口，端口将默认为1080。 |
| int32\_t port | 主机端口。取值范围[0, 65535]。 |
| const char \*exclusionLists | 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式。 |
