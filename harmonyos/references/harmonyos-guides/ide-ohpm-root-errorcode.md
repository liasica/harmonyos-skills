---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root-errorcode
title: ohpm root错误码
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm root错误码
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:11+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:af31e12ebb0a31de3a555144c53682600389b0f972cc1b32ceddd798b8b8b6ae
---

## 00608001 oh-package.json5文件不存在

**错误信息**

Pkg Not Found.

**错误描述**

找不到三方库。

**可能原因**

工程目录下不存在oh-package.json5文件时，执行ohpm root。

**处理步骤**

请确保工程目录下存在oh-package.json5文件，再执行命令 ohpm root。
