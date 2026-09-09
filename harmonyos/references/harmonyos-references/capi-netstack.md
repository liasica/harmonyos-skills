---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack
title: Netstack
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 模块 > Netstack
category: harmonyos-references
scraped_at: 2026-09-10T06:27:10+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f1c42896a0d39ff365b95acb5c891aca3e1c3099853a1a73d647997fcb4171b1
---

## 概述

提供网络相关模块的C接口，包括SSL/TLS证书链校验、WebSocket客户端、HTTP请求和HTTP全局拦截器等功能。

调用范式：以HTTP请求为例，典型调用流程为：创建请求实例→设置请求参数→发起请求→获取响应→销毁实例；WebSocket客户端需按创建实例→连接服务器→收发数据→关闭连接的顺序调用；SSL/TLS证书链校验需在发起网络请求前先加载并校验证书链；HTTP全局拦截器需先注册后使用，并在不再需要时注销。

**起始版本：** 11

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [net\_ssl\_c.h](capi-net-ssl-c-h.md) | 定义SSL/TLS证书链校验模块C接口数据结构。 |
| [net\_ssl\_c\_type.h](capi-net-ssl-c-type-h.md) | 定义SSL/TLS证书链校验模块的C接口需要的数据结构。 |
| [net\_websocket.h](capi-net-websocket-h.md) | 定义WebSocket客户端模块的接口。 |
| [net\_websocket\_type.h](capi-net-websocket-type-h.md) | 定义WebSocket客户端模块的C接口需要的数据结构。 |
| [net\_http.h](capi-net-http-h.md) | 定义HTTP请求模块的接口。 |
| [net\_http\_type.h](capi-net-http-type-h.md) | 定义HTTP请求模块的C接口需要的数据结构。 |
| [http\_interceptor.h](capi-net-http-interceptor-h.md) | 定义HTTP全局拦截器模块的接口。 |
| [http\_interceptor\_type.h](capi-net-http-interceptor-type-h.md) | 定义HTTP全局拦截器模块的C接口需要的数据结构。 |
