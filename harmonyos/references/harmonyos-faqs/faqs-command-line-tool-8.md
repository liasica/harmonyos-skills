---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-8
title: 发布ohpm提示错误：The version field: 12.5.0.0-20-dev in the oh-package.json5 file does not satisfy the semver specification
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 发布ohpm提示错误：The version field: 12.5.0.0-20-dev in the oh-package.json5 file does not satisfy the semver specification
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9ae61f55baf4379b24db1e04bda118e2291c1b2034df8839b8c08ff833766e2
---

**问题描述**

在线构建播放器库的HAR包后发布OHPM提示错误：11:29:52 ohpm ERROR: oh-package.json5文件中的版本字段12.5.0.0-20-dev不符合semver规范。

**解决方案**

版本应遵循semver语义化规范，目前仅支持1.0.0-XXXX三段式形式。详情请参阅文档：<https://semver.org/lang/zh-CN/#spec-item-11>。
