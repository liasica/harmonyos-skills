---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-unpublish-errorcode
title: ohpm unpublish错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm unpublish错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e16d02b6aa194d44f087c1bc23c86495721c42dd17bdcb2ea35543d1430c9440
---

## 00610001 执行下架命令时未指定版本号

**错误信息**

Delete All Version Pkg Not Force.

**错误描述**

未强制下架不同版本的包。

**可能原因**

下架时未指定版本号，且未使用强制下架。

**处理步骤**

如果未指定版本，默认下架三方库的所有版本，并且需要加上 -f 配置参数。
