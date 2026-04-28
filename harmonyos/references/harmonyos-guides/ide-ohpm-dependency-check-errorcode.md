---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dependency-check-errorcode
title: ohpm dependency-check错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm dependency-check错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:77aca353bcadb8251684d9d4cbb2d8bf20a795cc00067c3d0537d966dcea9437
---

## 00680001 更新信息查询失败

**错误信息**

querying update information from remote repository failed

**错误描述**

更新信息查询失败。

**可能原因**

执行ohpm dependency-check命令时，中心仓或私仓的地址错误。

**处理步骤**

检查中心仓或私仓的地址，确保正确。

## 00680002 指定模块下不存在oh-package.json5文件

**错误信息**

Specified module path or json file not exist

**错误描述**

查询更新信息时，指定的模块路径不存在或指定的模块下没有oh-package.json5文件。

**可能原因**

指定的模块不正确，或者模块下缺少oh-package.json5文件。

**处理步骤**

确认模块名称正确，以及配置oh-package.json5文件。

## 00680003 指定包查询失败

**错误信息**

When no module is specified, querying update information for a specified package is not supported

**错误描述**

当没有指定任何模块时，不支持查询指定包的更新信息。

**可能原因**

仅指定三方库名称，未指定模块或工程。

**处理步骤**

确保填写正确的模块/工程名称、三方库名称。
