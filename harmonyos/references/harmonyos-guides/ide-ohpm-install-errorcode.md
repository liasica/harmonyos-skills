---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-install-errorcode
title: ohpm install错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm install错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d192492cc9108b0080387046d4095714c8ac1b1c9e08e948b37f4dfe1c9bfe02
---

## 00604001 无匹配版本

**错误信息**

No Match.

**错误描述**

无匹配版本。

**可能原因**

从服务器获取的ohpm版本号和oh-package.json5中配置的版本号不匹配。

**处理步骤**

检查包的可用版本，确保指定的版本存在，修改oh-package.json5中ohpm版本号。

## 00604002 安装HAR包失败

**错误信息**

Install Pkg To Local Failed.

**错误描述**

安装本地包HAR失败。

**可能原因**

* 本地包或依赖的远程包不存在。
* 安装目录权限不足或磁盘空间不足。

**处理步骤**

* 查看本地包的依赖配置是否正确。
* 尝试写入权限的目录下进行操作，或清理磁盘后进行操作。

## 00604003 本地安装HSP包失败

**错误信息**

Install Local Hsp Failed.

**错误描述**

安装本地HSP包失败。

**可能原因**

* 安装本地HSP包失败，路径下缺少.hsp和.har 文件。
* 检查HSP包内的信息是否完整。

**处理步骤**

通过DevEco Studio生成一个新的TGZ包，通过对比，排查本地HSP包缺失的信息。

## 00604004 未找到HSP文件

**错误信息**

Not FoundHsp File By Registry Tgz.

**错误描述**

未找到HSP文件。

**可能原因**

无法从HSP包中找到.hsp文件。

**处理步骤**

检查HSP包，确保包含.hsp 文件。

## 00604005 依赖的包名无效

**错误信息**

Invalid CliInput Pkg .

**错误描述**

依赖的包名无效。

**可能原因**

从中心仓/私仓中未获取的依赖包名。

**处理步骤**

在中心仓或私仓搜索包名，确保输入包名正确。

## 00604006 依赖项中包名与实际包名不一致

**错误信息**

Inconsistent Dep Names.

**错误描述**

依赖名称不一致。

**可能原因**

工程级build-profile.json5文件中[useNormalizedOHMUrl](ide-hvigor-build-profile-app.md#section13181758123312)或 .ohpmrc文件中[enforce\_dependency\_key](ide-ohpmrc.md#section920325116547)设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。

**处理步骤**

检查依赖项列表，确保所有依赖项中包名与实际包名一致。

## 00604007 必选字段为空错误

**错误信息**

Field IS Empty Error.

**错误描述**

Field必选字段为空错误。

**可能原因**

oh-package.json5中必填字段未填。

**处理步骤**

检查oh-package.json5中必填字段，确保其包含有效值。

## 00604008 未找到最大的依赖版本

**错误信息**

Internal Program Error.

**错误描述**

未找到最大版本。

**可能原因**

有多个依赖版本时，未找到最大版本。

**处理步骤**

检查包依赖关系，确保没有依赖包冲突或不兼容的情况。具体请参考[模块内依赖版本冲突](ide-ohpmrc.md#section1623415477574)。

## 00633001 在命令行中指定的路径不存在

**错误信息**

Target Path UnExist Error.

**错误描述**

在命令行中指定的路径不存在。

**可能原因**

当使用--target\_path选项时，指定的target\_path不存在或不正确错误。

**处理步骤**

检查命令行，确保目标路径存在并且正确，更多说明请参考[target\_path](ide-ohpm-install.md#section79331822125611)。

## 00622020 输入的parameterFile文件或地址不存在

**错误信息**

Option Specified Parameter File Not Found.

**错误描述**

parameterFile未找到。

**可能原因**

配置的parameterFile文件或地址不存在错误。

**处理步骤**

检查和确保parameterFile文件路径正确。

## 00638002 包名不规范

**错误信息**

Invalid Group Option.

**错误描述**

包名不规范。

**可能原因**

包名的第一个字符必须是小写字母（a-z），且只能包含小写字母（a-z）、数字（0-9）、中划线（-）和下划线（\_），长度不超过36个字符。

**处理步骤**

检查包名，确保正确。
