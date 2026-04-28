---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-2
title: hilog日志如何设置为只打印当前应用的日志
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hilog日志如何设置为只打印当前应用的日志
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4fbfd6231be188e84cbaf2568e2400c221c3a1c5251c16b6585cc5b65b5a7ef9
---

使用hilog命令行工具来过滤保留当前应用的日志。

```
1. hilog -T xxx 按tag过滤;
2. hilog –D xxx 按domain过滤;
3. hilog -e 对日志内容匹配，支持正则表达式。支持tag, domain, pid等多重过滤,组合过滤以及反向过滤;
```
