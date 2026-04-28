---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-faq-4
title: 应用市场更新功能抛出不在前台异常
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 应用市场更新功能抛出不在前台异常
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0ff674998362003fa85dccaa0f0c682e03a8d4c064801cd78443951acb303b4a
---

**问题现象**

调用应用市场更新功能相关API时，提示应用不在前台异常。

**解决措施**

应用市场更新功能API要求应用必须在前台时进行调用，请在应用处于前台时调用相关接口。
