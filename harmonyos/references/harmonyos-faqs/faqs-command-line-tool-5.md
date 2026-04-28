---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-5
title: ohpm ERROR: JSON5: invalid end of input at 1:1
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm ERROR: JSON5: invalid end of input at 1:1
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d4a86a225babc436a0f97ecd7e728c055e36afb433d96674663d965b0e8593d8
---

**问题描述**

电脑无网络，升级到600后出现错误：ohpm ERROR: JSON5: invalid end of input at 1:1。

**解决方案**

删除工程下的oh-package-lock.json5文件后，执行ohpm clean、ohpm cache clean和ohpm install --all。
