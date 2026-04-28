---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-11
title: 如何解决ohpm上传har包异常，报错：The publishId is invalid!
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何解决ohpm上传har包异常，报错：The publishId is invalid!
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5d532c09ce8ee95678f4b299384c99777fc5900e4fc110b4cd9e4b7736fcc0ea
---

1. 请登录ohpm-repo私仓管理页面，重新复制下最新的发布码。获取发布码操作请参考以下文档：[使用命令行工具发布](../harmonyos-guides/ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_使用命令行工具发布)
2. 重新执行命令“ohpm config set publish\_id发布码”，执行后请检查下.ohpmrc文件中的publish\_id是否同步更新。
3. 重新上传har包。
