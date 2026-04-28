---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming
title: Http_PerformanceTiming
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_PerformanceTiming
category: harmonyos-references
scraped_at: 2026-04-28T08:08:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:224e46ab12b4219a3f03d148076a57f1da94be3a19df7a16eb173dbcd43e525f
---

```
1. typedef struct Http_PerformanceTiming {...} Http_PerformanceTiming
```

## 概述

PhonePC/2in1TabletTVWearable

HTTP响应时间信息，会在[Http\_Response](capi-netstack-http-response.md#成员变量)中收集。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| double dnsTiming | 从request请求到DNS解析完成的耗时，包含域名解析，TCP连接等流程耗时。 |
| double tcpTiming | 从request请求到TCP连接完成的耗时。 |
| double tlsTiming | 从request请求到TLS连接完成的耗时。 |
| double firstSendTiming | 从request请求到开始发送第一个字节的耗时。 |
| double firstReceiveTiming | 从request请求到接收到第一个字节的耗时。 |
| double totalFinishTiming | 从request请求到完成请求的耗时。 |
| double redirectTiming | 从request请求到完成所有重定向步骤的耗时。 |
