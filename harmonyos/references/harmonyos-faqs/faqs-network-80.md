---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-80
title: HarmonyOS中如何使用SSE方式请求大模型流式数据
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HarmonyOS中如何使用SSE方式请求大模型流式数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a7ea598a691eaf491d2ba9b8c1b8acfec683c0495b73a3875715d2e06bf0255
---

## 问题现象

HarmonyOS中如何使用SSE方式请求大模型流式数据？要求如下：

* 使用SSE方式请求。
* 请求类型为POST类型。

## 解决方案

可以使用官方提供的[EventSource](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/eventsource)三方库实现。
