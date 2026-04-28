---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00305
title: 语法错误码
breadcrumb: 指南 > 构建应用 > 构建报错排查 > 编译构建错误码 > 语法错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc562658d1c4c26ea2ac237bc45c42c2ff66eca1a7e438ff018a6d7f67c53282
---

## 00305001 ArkTS语法检查报错

**错误信息**

ArkTS lint errors.

**错误描述**

ArkTS语法检查报错。

**可能原因**

ArkTS语法错误。

**处理步骤**

根据报错信息处理ArkTS语法错误。

## 00305003 hvigorfile.ts或hvigorconfig.ts有类型错误

**错误信息**

There are these type errors in the code.

**错误描述**

解析hvigorfile.ts或hvigorconfig.ts有类型错误。

**可能原因**

hvigorfile.ts或hvigorconfig.ts有类型错误。

**处理步骤**

根据报错信息处理hvigorfile.ts或hvigorconfig.ts文件的类型错误。

## 00305004 json/json5文件存在语法错误

**错误信息**

以实际语法错误为准。

**错误描述**

解析json/json5文件时出现语法错误。

**可能原因**

json/json5文件存在语法错误。

**处理步骤**

根据报错信息处理文件中的语法错误。

## 00305006 JSON/JSON5格式错误

**错误信息**

XXX is not the correct JSON/JSON5 format.

**错误描述**

XXX不是正确的JSON/JSON5格式。

**可能原因**

对应文件不是JSON/JSON5格式。

**处理步骤**

确保对应文件是JSON/JSON5格式。

## 00305008 JSON/JSON5文件语法错误

**错误信息**

XXX at file: YYY:ZZZ".

**错误描述**

XXX在文件位置YYY:ZZZ存在语法错误。

**可能原因**

对应文件中存在JSON/JSON5语法错误。

**处理步骤**

根据报错的文件路径信息修复相关的JSON/JSON5语法错误。

## 00305009 CMake文件API解析失败

**错误信息**

CMake file API parse failed. At file: XXX.

**错误描述**

CMake文件API解析失败。

**可能原因**

在XXX路径下，找不到以“index-”开头的文件。

**处理步骤**

点击菜单栏**Build > Clean Project**后，重新构建。

## 00305010 属性或方法未定义

**错误信息**

以实际错误信息为准。

**错误描述**

属性或方法未定义。

**可能原因**

在hvigorconfig.ts或hvigorfile.ts中使用了未定义的属性或方法。

**处理步骤**

确保hvigorconfig.ts或hvigorfile.ts中使用的属性或方法都已定义。

## 00305011 未定义符号错误

**错误信息**

A 'undefined symbol' error has occurred.

**错误描述**

出现了未定义符号错误。

**可能原因**

源文件没有正确编译或链接，或者因为缺少必要的库文件。

**处理步骤**

参考[CPP编译报错"A 'undefined symbol' error has occurred"](../harmonyos-faqs/faqs-compiling-and-building-116.md)。

## 00305012 CMake任务执行失败

**错误信息**

CMake task execution failed.

**错误描述**

CMake任务执行失败。

**可能原因**

用户手动删除编译后模块的.cxx目录，并且在build-profile.json5中arguments字段下配置“--version”、“

--help”、“--usage”等查询类参数。

**处理步骤**

删除arguments字段下的“--version”、“--help”、“--usage”等查询类参数。

## 00305013 存在无效的tag标签

**错误信息**

Invalid tag XXX at YYY.

**错误描述**

存在无效的tag标签。

**可能原因**

YYY文件中tag标签存在不符合要求的字符。

**处理步骤**

确保tag标签以字母或数字开头，长度不超过60个字符，只能由字母、数字、句点（.）、中划线（-）、下划线（\_）组成，且不能配置为'latest'。

## 00305014 出现了“未知类型”错误

**错误信息**

A 'unknown type name' error has occurred.

**错误描述**

出现了“未知类型”错误。

**可能原因**

代码中存在类型未定义、未包含相关头文件或者头文件路径不正确。

**处理步骤**

根据以下指导排查：[CPP编译报错“A 'unknown type name' error has occurred”](../harmonyos-faqs/faqs-compiling-and-building-117.md)。

## 00305015 解析错误

**错误信息**

以实际错误信息为准。

**错误描述**

以实际错误描述为准。

**可能原因**

通常为源码文件中路径解析错误。

**处理步骤**

根据错误提示信息修改。
