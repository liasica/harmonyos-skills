---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy
title: Http_Proxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Proxy
category: harmonyos-references
scraped_at: 2026-04-28T08:08:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c7b8f157f71030c0c2f8f625582a72c2da6d407c0fc8403a4228adb06c71af90
---

```
1. typedef struct Http_Proxy {...} Http_Proxy
```

## 概述

PhonePC/2in1TabletTVWearable

代理配置结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Http\_ProxyType](capi-net-http-type-h.md#http_proxytype) proxyType | 代理配置类型，参考[Http\_ProxyType](capi-net-http-type-h.md#http_proxytype)。 |
| [Http\_CustomProxy](capi-netstack-http-customproxy.md) customProxy | 自定义代理配置信息，参考[Http\_CustomProxy](capi-netstack-http-customproxy.md)。 |
