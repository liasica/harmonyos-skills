---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-errorcode-universal
title: ohpm命令公共错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm命令公共错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:50+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:3850a506f5cf557800bfdf103b239d33e964444aac906297bb40c0843cea3e53
---

## 00617101 获取包信息失败

**错误信息**

Fetch Pkg Info Failed.

**错误描述**

获取包信息失败。

**可能原因**

执行ohpm list、ohpm info、ohpm install命令时，包名或版本号不匹配，从中心仓和私仓获取不到相关信息。

**处理步骤**

在中心仓和私仓搜索包名/版本号，确保可以跟仓中匹配。

## 00608001 oh-package.json5文件不存在

**错误信息**

Pkg Not Found.

**错误描述**

找不到三方库。

**可能原因**

工程目录下不存在oh-package.json5文件。

**处理步骤**

确保工程目录下存在oh-package.json5文件，再执行命令。

## 00608002 文件不存在

**错误信息**

File Not Found.

**错误描述**

文件不存在。

**可能原因**

在指定目录下未找到文件。

**处理步骤**

确认目录下存在文件后再执行命令。

## 00608003 读取文件时发生错误

**错误信息**

File Read Error.

**错误描述**

读取文件时发生错误。

**可能原因**

读取配置等文件失败。

**处理步骤**

查看是否被占用后，重新读取。

## 00670002 路径大小写敏感错误

**错误信息**

Path Case Sensitivity Error.

**错误描述**

路径大小写敏感错误。

**可能原因**

工程中文件的配置路径和文件的实际路径大小写不一致。

**处理步骤**

修改工程中配置的文件路径，使其与文件的实际路径一致；或者设置.ohpmrc文件中的case\_sensitive\_check为false，不检测文件路径大小写。更多请参考[case\_sensitive\_check](ide-ohpmrc.md#section2045412394117)。
