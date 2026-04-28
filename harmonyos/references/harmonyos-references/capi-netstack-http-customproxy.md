---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy
title: Http_CustomProxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_CustomProxy
category: harmonyos-references
scraped_at: 2026-04-28T08:08:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1e22fbbce96e9f0db4e1c164d5ea1db273da341158bda266fd378594448b0d45
---

```
1. typedef struct Http_CustomProxy {...} Http_CustomProxy
```

## 概述

PhonePC/2in1TabletTVWearable

用户自定义代理配置。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \*host | 代理服务器主机名， 如果没有显式设置端口，端口将默认为1080。 |
| int32\_t port | 主机端口。取值范围[0, 65535]。 |
| const char \*exclusionLists | 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式。 |
