---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-39
title: 跨模块、跨进程时如何保证正常读取首选项中数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 跨模块、跨进程时如何保证正常读取首选项中数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cf93d4e7a1c7e4c94c36e8bba29ea0dd98118b4f992bac8a67a8b04052279449
---

**解决措施**

跨模块：

由于context不同，跨模块、多页面场景下可能无法获取数据。建议在Ability中使用单例类存储全局context，或使用应用级context。

跨进程：

不同进程只有在同沙箱场景下才能访问同一个preference文件。多进程可通过dataGroupId在多个进程间共享同一个preference文件。
