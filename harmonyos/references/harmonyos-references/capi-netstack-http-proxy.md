---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy
title: Http_Proxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Proxy
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:14f3bfe71143c2c946ce7a0cfdf4b5e8f375cd1696bed47d198214899e4ff469
---

```c
typedef struct Http_Proxy {...} Http_Proxy
```

## 概述

代理配置结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Http\_ProxyType](capi-net-http-type-h.md#http_proxytype) proxyType | 代理配置类型，参考[Http\_ProxyType](capi-net-http-type-h.md#http_proxytype)。 |
| [Http\_CustomProxy](capi-netstack-http-customproxy.md) customProxy | 自定义代理配置信息，参考[Http\_CustomProxy](capi-netstack-http-customproxy.md)。 |
