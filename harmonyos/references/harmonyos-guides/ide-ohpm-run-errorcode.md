---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-run-errorcode
title: ohpm run错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm run错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:13a69cebc576e3f0eba8b59a41661cb41615bc94e52549a87bcf47b21d4cb1ae
---

## 00611001 脚本执行失败

**错误信息**

Script Fail.

**错误描述**

脚本执行失败。

**可能原因**

在目标路径未找到执行脚本。

**处理步骤**

确保脚本文件在目标路径存在。

## 00611003 script\_name开头位置使用非法字符

**错误信息**

Invalid Command Error.

**错误描述**

非法字符命令行错误。

**可能原因**

脚本别名开头位置使用非法字符，包括(、[、{，如oh-package.json5配置："scripts": { "build": "(echo hello)" }

**处理步骤**

检查脚本别名，确保脚本名称开头位置不使用(、[、{。

## 00611004 脚本别名首字母未小写

**错误信息**

Invalid Key.

**错误描述**

脚本别名出现的无效键错误。

**可能原因**

当脚本别名的首字母不是小写时，系统认为该键无效。

**处理步骤**

检查脚本别名的首字母，确保其为小写字母。

## 00611005 脚本别名长度无效

**错误信息**

Invalid KeyLen.

**错误描述**

脚本别名长度无效。

**可能原因**

脚本别名长度不在规定区间时，系统认为该键的长度无效。

**处理步骤**

检查脚本别名的长度，确保在[1,128]范围之内。

## 00611006 args参数长度无效

**错误信息**

Invalid ParamLen.

**错误描述**

参数长度无效。

**可能原因**

args参数长度超出范围。如在oh-package.json5配置"scripts": { "build": "echo test" }，执行ohpm run build -- -a ([string]::new("a", 3000))命令。

**处理步骤**

检查args参数长度，确保在[1,2048]范围内。

## 00611007 脚本别名不符合规范

**错误信息**

Invalid Key Regex.

**错误描述**

无效密钥正则表达式。

**可能原因**

script\_name不符合规范

**处理步骤**

检查脚本别名的字符，只能包含：大写字母、小写字母、 数字、下划线\_ 、中划线-。

## 00611008 脚本中用连接的ohpm命令

**错误信息**

Command Error.

**错误描述**

命令错误。

**可能原因**

合法的scriptContent不能引用除ohpm run以外的其它ohpm命令（如ohpm install、ohpm add等）。如在oh-package.json5配置"scripts": { "build": "ohpm install pkg" }，执行ohpm run build命令。

**处理步骤**

直接在终端执行ohpm命令（如ohpm install），不可放在scripts中使用ohpm run命令执行。

## 00611009 包解析失败

**错误信息**

Parse Pkg Error.

**错误描述**

解析包失败。

**可能原因**

oh-package-lock.json5文件格式不正确。

**处理步骤**

检查oh-package-lock.json5文件是否符合规定的格式，具体请参考[oh-package.json5](ide-oh-package-json5.md)。

## 00611010 prefix命令执行失败

**错误信息**

Prefix Invalid Error.

**错误描述**

--prefix选项错误。

**可能原因**

指定路径下未包含oh-package.json5文件，如执行ohpm run build -- --prefix D:\新建目录命令，D:\新建目录下未包含oh-package.json5文件。

**处理步骤**

确认指定路径下包含oh-package.json5文件。

## 00611011 未能找到指定的包管理配置文件

**错误信息**

Pkg UnExist Error.

**错误描述**

未能找到指定的包管理配置文件。

**可能原因**

在当前目录中执行ohpm run build，当前目录下不包含oh-package.json5文件。

**处理步骤**

确保当前目录中存在oh-package.json5文件。

## 00611012 脚本别名不存在

**错误信息**

Script UnExist Error.

**错误描述**

脚本别名不存在。

**可能原因**

执行脚本别名未在oh-package.json5文件中声明。

**处理步骤**

检查oh-package.json5文件，确保脚本别名已正确声明并且格式正确。

## 00611013 脚本内容为空

**错误信息**

Script Empty Error.

**错误描述**

执行脚本为空错误。

**可能原因**

脚本内容为空。

**处理步骤**

检查脚本内容，确保其包含有效命令。

## 00611014 脚本内容无效

**错误信息**

Script Invalid Error.

**错误描述**

脚本无效错误。

**可能原因**

脚本内容无效。如oh-package.json5配置为"scripts": { "build": "ohpm" }，执行ohpm run build。

**处理步骤**

检查脚本内容，确保已正确配置。

## 00611015 脚本内容错误

**错误信息**

Script Content Error.

**错误描述**

脚本内容错误。

**可能原因**

当同时满足以下三个条件时返回该错误码：

1. 脚本内容包含ohpm run

2. 脚本内容包含 --（参数分隔符）

3. 脚本内容包含 && 或 ||（命令连接符 ）

如oh-package.json5 配置为"scripts": { "bad": "ohpm run build -- --prefix D:\\test && ohpm run test" }，执行ohpm run bad。

**处理步骤**

检查脚本别名的配置，确保ohpm run、参数分隔符、 命令连接符未同时使用。

## 00611016 循环调用

**错误信息**

Directed Cycle Error.

**错误描述**

循环调用无法正常执行脚本。

**可能原因**

脚本包含循环调用，如"scriptName1": "ohpm run scriptName2","scriptName2": "ohpm run scriptName2"。

**处理步骤**

检查脚本配置，确保脚本调用关系无循环。

## 00611017 脚本参数不正确

**错误信息**

Invalid Header Param Error.

**错误描述**

脚本参数不正确。

**可能原因**

脚本参数以-或--开头，如ohpm run scriptName1 -- arg1=1 --arg2=2。

**处理步骤**

检查脚本参数，确保-或--开头，如--debug。

## 00611018 无效参数

**错误信息**

Invalid Param Error.

**错误描述**

无效参数。

**可能原因**

执行ohpm run build-- --key value命令时，key和value未成对使用，如ohpm run build -- --name value1 value2。

**处理步骤**

检查脚本参数格式，参数以短横线-或双短横线--开头，后跟参数名称和对应的值，确保其符合要求，如：--key value（如script --name Alice）、--key=value（如script --age=25）、--key=a=b（如script --config=a=b,c=d）。

## 00611019 传递参数配置无效

**错误信息**

Invalid Param Config Error.

**错误描述**

配置无效参数。

**可能原因**

配置传递参数命令时，未以--开头。如oh-package.json5配置："scripts": { "build": "ohpm run compile -name John" }，compile 后面缺少 ' -- '，执行ohpm run build。

**处理步骤**

传递参数配置时，确保以--开头，以指示需要添加或覆盖的参数。具体请参考[传递参数](ide-ohpm-run.md#zh-cn_topic_0000001792216413_传递参数)。
