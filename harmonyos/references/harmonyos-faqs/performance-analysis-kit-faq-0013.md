---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0013
title: 如何通过hdc命令清除手机中应用的缓存
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > 如何通过hdc命令清除手机中应用的缓存
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4de14a74df958d2d061b4686d9454162f190d37102752cd7d199516257219fc4
---

**Q：如何通过hdc命令清除手机中应用的缓存？**

**A**：清除数据：使用hdc shell bm clean -d -n命令，后跟应用包名。

清除缓存：使用hdc shell bm clean -c -n命令，后跟应用包名。
