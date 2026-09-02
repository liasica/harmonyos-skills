---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-glossary
title: Remote Communication Kit术语
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > Remote Communication Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:892a4ad3fe2abb5ceacc0eb689eb226370f942b6642ee0977462ff5fa8e174bc
---

## C

### Cache Interceptor；缓存拦截器

自定义的拦截器，用于介入缓存处理流程，包括缓存数据的预处理、加载逻辑定制等，从而精准匹配复杂业务场景对缓存逻辑的差异化需求。

### Caching Responses；响应缓存

HTTP缓存管理对象，遵循RFC 9111协议，支持独立配置缓存策略与持久化存储路径，实现内存、磁盘双重缓存管理，并提供自定义缓存拦截器能力。

### Certificate Pinning；证书锁定

通过比较证书公钥的SHA256哈希值的BASE64编码，限定可信任的证书范围，增强应用程序的安全性。

## D

### DNS over HTTPS (DOH)；DNS over HTTPS配置

一种通过加密的HTTPS协议进行DNS解析的技术，避免原始DNS协议中用户的DNS解析请求被窃听或修改，保护用户隐私。

### Dynamic DNS Rules；动态DNS规则

可以根据hostname和port直接返回IP地址的函数，如果设置，则优先使用函数中返回的地址进行DNS解析。

## E

### Expiration Policy；过期策略

HTTP缓存的过期策略配置，支持永不过期、绝对时间、相对时间以及滑动时间过期策略，用于灵活调整缓存生命周期。

## I

### Interceptor；拦截器

用于在HTTP请求和响应过程中进行拦截和修改的组件，支持创建拦截器链，按需定制一组拦截器对网络请求/响应进行修改。

## M

### Multi-part Form；多部分表单

用于发送HTTP多部分表单数据的对象，支持指定表单中key的发送顺序，适用于文件上传等场景。

## P

### Pause Policy；暂停策略

用于配置请求暂停行为的策略对象，支持发送暂停和接收暂停，可以基于超时时间或其他条件触发暂停。

## S

### Static DNS Rules；静态DNS规则

手动添加的DNS解析规则，当默认的DNS不能正常解析部分域名时使用，如果hostname匹配，则优先使用指定的地址。

## U

### URPC；统一远程过程调用

Unified Remote Procedure Call的缩写，一种高性能RPC通信库，可实现远程函数调用能力，具有抗弱网传输、多径传输（蜂窝网络和Wi-Fi）等特性。

## W

### Web Proxy；Web代理

自定义代理配置对象，允许开发者设置代理URL、隧道创建策略和排除规则，解决特定网络问题，优化代理路径，提升性能和用户体验。
