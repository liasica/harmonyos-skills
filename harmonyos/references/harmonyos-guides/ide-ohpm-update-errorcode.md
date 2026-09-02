---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-update-errorcode
title: ohpm update错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm update错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:64ab147aa1165bfe7dee4c6b4bddbaee17f7712edc546182bdf0c1c469bd1052
---

## 00606001 执行命令时带版本号

**错误信息**

Has Version.

**错误描述**

update时带版本号。

**可能原因**

执行ohpm update library时带版本号，如ohpm update library@2.0.0。

**处理步骤**

更新命令中不应包含版本号，仅指定包名ohpm update library。

## 00606002 执行tag-filter命令时使用非标准的正则

**错误信息**

Tag Filter Non Standard Regex.

**错误描述**

执行tag-filter命令时使用非标准正则。

**可能原因**

执行ohpm update --tag-filter <regex>命令时，使用非标准正则。如ohpm update library --tag-filter [a-z，其中 [a-z表示非法正则表达式，正确正则参数为[a-z]。

**处理步骤**

检查和修改为标准正则。
