---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0011
title: 通过hdc命令获取设备udid常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > 通过hdc命令获取设备udid常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c48b76ded86b851bf5bf6fce070292b1793466cce69124f9a592322aa02c218f
---

**Q：如何通过hdc命令获取设备的udid？**

A：使用以下命令之一获取设备的udid：

```shell
hdc shell bm get -u 
hdc shell bm get --udid
```
