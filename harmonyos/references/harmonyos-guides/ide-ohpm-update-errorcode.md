---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-update-errorcode
title: ohpm update错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm update错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4594ab73619ed4220951524c9e8ecdfbd9ad93fced710075d5ac75baa03256f6
---

## 00606001 执行命令时带版本号

**错误信息**

Has Version.

**错误描述**

update时带版本号。

**可能原因**

执行ohpm update时带版本号。

**处理步骤**

更新命令中不应包含版本号，仅指定包名。

## 00606002 执行tag-filter命令时使用非标准的正则

**错误信息**

Tag Filter Non Standard Regex.

**错误描述**

tag-filter命令使用非标准正则。

**可能原因**

执行ohpm update --tag-filter <regex>命令时，使用非标准正则。

**处理步骤**

检查和修改为标准正则。
