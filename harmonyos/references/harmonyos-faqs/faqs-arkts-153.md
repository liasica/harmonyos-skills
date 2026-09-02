---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-153
title: 应用启动超时问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 应用启动超时问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:83cc4438bfe8eb83551116bad0de55b3e90c74ff97814cada8be60379277510d
---

## 问题现象

应用启动时长时间停留在启动页面，最终显示"Timeout"错误提示。

## 背景知识

在HTTP请求过程中，CURL库返回的错误代码28（CURLcode 28）表示请求超时（Operation timeout）。

## 问题定位

通过分析应用日志，发现关键错误信息：

```shell
E [http_exec.cpp 330] CURLcode result 28   // 请求耗时超时
```

同时观察到完整的请求耗时日志：

```shell
[http_exec.cpp 429] taskid=-2147483648, size:0, dns:0.378, connect:0.000, tls:0.000, firstSend:0.000, firstRecv:0.000, total:60001.334, redirect:0.000
```

## 分析结论

请求总耗时达到60秒（60001ms）后超时，DNS解析耗时378ms，但后续链接未能建立。

## 修改建议

配置服务器，确保服务器能够正常连接。
