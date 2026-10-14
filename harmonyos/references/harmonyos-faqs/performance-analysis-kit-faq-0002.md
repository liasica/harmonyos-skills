---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0002
title: hilog应用日志过滤设置常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > hilog应用日志过滤设置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:34+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:13d1f7d43bc51ac26fb0d20f0c89aaa8febda244072157c8a78b75eda6177b45
---

**Q：hilog日志如何设置为只打印当前应用的日志？**

**A**：使用hilog命令行工具来过滤保留当前应用的日志。

```bash
hilog -T xxx 按tag过滤; 
hilog –D xxx 按domain过滤; 
hilog -e 对日志内容匹配，支持正则表达式。支持tag, domain, pid等多重过滤,组合过滤以及反向过滤;
```
