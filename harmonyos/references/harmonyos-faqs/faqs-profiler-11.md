---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-11
title: 如何避免使用AppAnalyzer后使用git提示需要版本化
breadcrumb: FAQ > DevEco Studio > 性能分析 > 如何避免使用AppAnalyzer后使用git提示需要版本化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:446e4772ab05e1a8d3934d5afb104ee2afc1d04d037e7221b26a067e59c4f80c
---

**问题现象**

1. 使用AppAnalyzer进行应用/元服务体检后，使用git提示需要版本化。
2. 提示的文件在工程根目录/.appanalyzer下。

**问题原因**

AppAnalyzer会在体检完成后生成需要展示的数据用于最终报告展示，这类文件会保存在工程根目录/.appanalyzer下。

**解决措施**

在.gitignore文件下配置如下目录：

```
1. /.appanalyzer
```
