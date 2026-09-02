---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming
title: Http_PerformanceTiming
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_PerformanceTiming
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:28e7846fc7a33ffbc8916733b6a960da4ecfd1f1a68edcb04731a6cb529a3602
---

```c
typedef struct Http_PerformanceTiming {...} Http_PerformanceTiming
```

## 概述

HTTP响应时间信息，会在[Http\_Response](capi-netstack-http-response.md#成员变量)中收集。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double dnsTiming | 从request请求到DNS解析完成的耗时，包含域名解析，TCP连接等流程耗时。单位：ms。 |
| double tcpTiming | 从request请求到TCP连接完成的耗时。单位：ms。 |
| double tlsTiming | 从request请求到TLS连接完成的耗时。单位：ms。 |
| double firstSendTiming | 从request请求到开始发送第一个字节的耗时。单位：ms。 |
| double firstReceiveTiming | 从request请求到接收到第一个字节的耗时。单位：ms。 |
| double totalFinishTiming | 从request请求到完成请求的耗时。单位：ms。 |
| double redirectTiming | 从request请求到完成所有重定向步骤的耗时。单位：ms。 |
