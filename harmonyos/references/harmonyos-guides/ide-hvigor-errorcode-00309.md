---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00309
title: ArkTS编译错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > ArkTS编译错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:29+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:945256ebb4d95c9d1c9854e68c86eb90c250f1b6020de3907417c32940df3b6d
---

## 00309001 禁止使用相对路径导入模块以外的文件

**错误信息**

Cannot import files outside of the current module using relative paths. Import statement: XXX. At file: YYY.

**错误描述**

禁止使用相对路径方式导入当前模块以外的文件。

**可能原因**

在当前模块中使用相对路径方式导入了模块外的文件YYY。

**处理步骤**

检查当前模块，确保没有使用相对路径方式导入模块外文件YYY。

## 00309002 在import语句中避免使用绝对路径

**错误信息**

Avoid absolute paths in imports. Import statement: XXX. At file: YYY.

**错误描述**

在import语句中避免使用绝对路径。

**可能原因**

在文件YYY的import语句XXX中使用了绝对路径。

**处理步骤**

检查import语句XXX，确保没有使用绝对路径方式导入文件。

## 00309003 无法解析import语句

**错误信息**

Cannot resolve import statement XXX.

**错误描述**

无法解析import语句XXX。

**可能原因**

* 在开启大小写敏感时（即工程级build-profile.json5的caseSensitiveCheck设置为true），import的文件夹中只包含Index.ets或Index.ts（大写I），当前import文件夹仅支持index.ets或index.ts（小写i）。
* 在开启大小写敏感时，import的文件和实际的文件名大小写不一致。

**处理步骤**

* 将import文件夹改为import具体的文件，如果要import文件夹，确保文件夹中存在index.ets或index.ts（小写i）。
* 确保import的文件和实际的文件名大小写一致。
