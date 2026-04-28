---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-info-errorcode
title: ohpm info错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm info错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:75cfaafea5d30bb581030c86deba479579116ec49d14c7857886fa993652d63d
---

## 00639001 获取包失败

**错误信息**

Package Not Found Error.

**错误描述**

包未找到错误。

**可能原因**

在中心仓或私仓未找到相应的包。

**处理步骤**

检查包名称，确保在中心仓或私仓中存在。

## 00639002 包名称为空

**错误信息**

Package Name Is Empty Error.

**错误描述**

包名称为空错误。

**可能原因**

执行命令时未配置包名。

**处理步骤**

填写有效的包名称。

## 00639003 配置Field不支持的字段

**错误信息**

UnSupport Field Error.

**错误描述**

不支持的字段错误。

**可能原因**

命令中配置field不支持的字段。

**处理步骤**

检查和输入field支持的字段，如“keywords”、“dependencies”、"latest"等。

## 00639004 PageNum页码错误

**错误信息**

Invalid PageNum Error.

**错误描述**

无效的页码错误。

**可能原因**

配置的PageNum值超出有效范围。

**处理步骤**

检查页码范围，确保其在[1, 10000]有效范围内。

## 00639005 PageSize无效错误

**错误信息**

Invalid PageSize Error.

**错误描述**

无效的页面大小错误。

**可能原因**

配置的PageSize值超出有效范围。

**处理步骤**

检查PageSize值，确保其在[1, 500]有效范围内。
