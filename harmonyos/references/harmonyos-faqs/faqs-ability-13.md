---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-13
title: 部署HAP时上报“Failure[INSTALL_FAILED_SIZE_TOO_LARGE] error while deploying hap”错误
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 部署HAP时上报“Failure[INSTALL_FAILED_SIZE_TOO_LARGE] error while deploying hap”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:810e92bc2908473c7345f311e135e532de70858b54cf6f1da6a61b14f80cd45e
---

**问题现象**

部署HAP时，出现以下错误： Failure[INSTALL\_FAILED\_SIZE\_TOO\_LARGE]。

**可能原因**

这是由于单个HAP包的大小超过限制导致的。

**解决措施**

将内容拆分为多个HAP即可解决问题。
