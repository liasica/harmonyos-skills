---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-11
title: 如何解决ohpm上传har包异常，报错：The publishId is invalid!
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何解决ohpm上传har包异常，报错：The publishId is invalid!
category: harmonyos-faqs
scraped_at: 2026-11-21T09:19:33+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:cf3998a7d4b5f6074aef0dd80072f4ecfb92bca38cd1fa82a4a812e270d71bb8
---

1. 请登录ohpm-repo私仓管理页面，重新复制下最新的发布码。获取发布码操作请参考以下文档：[使用命令行工具发布](../doccenter-deveco-studio/ide-ohpm-repo-quickstart.md#section182904013257)
2. 重新执行命令“ohpm config set publish\_id发布码”，执行后请检查下.ohpmrc文件中的publish\_id是否同步更新。
3. 重新上传har包。
