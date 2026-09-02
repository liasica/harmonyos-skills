---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-2
title: hilog日志如何设置为只打印当前应用的日
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hilog日志如何设置为只打印当前应用的日
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f6c068c30ff23966f97e8ee9dce3622e8cddf2ee8b308dc02ac148f15904d4f5
---

使用hilog命令行工具来过滤保留当前应用的日志。

```text
hilog -T xxx 按tag过滤; 
hilog –D xxx 按domain过滤; 
hilog -e 对日志内容匹配，支持正则表达式。支持tag, domain, pid等多重过滤,组合过滤以及反向过滤;
```
