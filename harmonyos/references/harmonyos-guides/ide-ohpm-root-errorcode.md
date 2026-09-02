---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root-errorcode
title: ohpm root错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm root错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6ed73fd59c96a850aef9b7767d5979ed3b14282a9529070d347a402277136a5d
---

## 00608001 oh-package.json5文件不存在

**错误信息**

Pkg Not Found.

**错误描述**

找不到三方库。

**可能原因**

工程目录下不存在oh-package.json5文件，执行ohpm root。

**处理步骤**

确保工程目录下存在oh-package.json5文件，再执行命令 ohpm root。
