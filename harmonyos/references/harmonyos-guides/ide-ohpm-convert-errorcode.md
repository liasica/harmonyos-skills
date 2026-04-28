---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-convert-errorcode
title: ohpm convert错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm convert错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90a552587e77ef4bcfa849c41052e1aa8df7bf7f2189f9332206939b7c896a2d
---

## 00636001 无子目录

**错误信息**

No Subdirectories.

**错误描述**

无子目录。

**可能原因**

本地node\_modules目录下无子目录。

**处理步骤**

检查node\_modules目录，确保存在有效的子目录。

## 00636002 未找到artifactType属性

**错误信息**

Not Found Attribute Name.

**错误描述**

未找到属性名称。

**可能原因**

在package.json配置文件中未找到artifactType属性。

**处理步骤**

检查属性名称，确保其存在。

## 00636003 RuleType无效

**错误信息**

Invalid Rule Type.

**错误描述**

无效的规则类型。

**可能原因**

在验证配置时，未找到 attrName属性对应的ruleType规则。

**处理步骤**

检查规则类型，确保其存在验证配置中。

## 00636004 未找到package.json文件

**错误信息**

Not Found Constants.PackageJson.

**错误描述**

未找到package.json文件。

**可能原因**

指定的规则类型在验证配置中不存在。

**处理步骤**

检查目录路径，确保npm包中package.json文件存在。

## 00636005 包转换失败

**错误信息**

Convert Package Failed.

**错误描述**

包转换失败。

**可能原因**

npm包中package.json配置文件字段缺失。

**处理步骤**

检查npm包中package.json配置文件字段存在，且取值符合要求。具体字段说明请参考[oh-package.json5](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)。

## 00636006 Node\_modules目录配置错误

**错误信息**

Configure Node Modules Error.

**错误描述**

node\_modules配置错误。

**可能原因**

使用本地模式转换时，node\_modules目录配置错误。

**处理步骤**

配置正确的node\_modules目录，确保转换顺利进行。
