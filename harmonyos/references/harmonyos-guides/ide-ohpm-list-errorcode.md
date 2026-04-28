---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-list-errorcode
title: ohpm list错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm list错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:71ea734b57027373397110454a6959cb0f17354cdb853cb46e28ac0abe4e8f30
---

## 00622014 parameterFile配置问题

**错误信息**

Parameter File Not Config Error.

**错误描述**

参数文件未配置。

**可能原因**

parameterFile配置问题。

**处理步骤**

检查和确保parameterFile配置正确，具体修改可参考[parameterFile](ide-oh-package-json5.md#section122411462820)。

## 00608001 包未找到

**错误信息**

Pkg Not Found.

**错误描述**

包未找到。

**可能原因**

目录中不存在oh-package.json5文件。

**处理步骤**

确保当前目录下存在oh-package.json5文件。

## 00618005 存在循环依赖

**错误信息**

Invalid Dependency.

**错误描述**

无效依赖。

**可能原因**

存在循环依赖，如ma@1.0.0 -> mb@1.0.0 -> mc@1.0.0 -> ma@1.0.0。

**处理步骤**

检查依赖配置，确保无循环依赖。
