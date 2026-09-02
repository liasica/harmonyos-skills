---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-styled-string
title: 属性字符串错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > 属性字符串错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:b0e202af88d0596f5a8943fa236cbbf96db553b43846b7a284d41587eee65214
---

属性字符串错误码定义了属性字符串在转换、解码、序列化等操作过程中可能出现的错误信息及对应的处理建议，帮助开发者快速定位和解决属性字符串相关问题。

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 170001 转换错误

**错误信息**

Convert Error.

**错误描述**

fromHtml无法将传入的字符串转换为属性字符串。

**可能原因**

字符串为空或字符串不符合HTML格式。

**处理步骤**

1. 检查传入的字符串是否为空，如果为空，请传入有效的非空字符串。
2. 确认字符串是否符合HTML格式要求，如果不符合，请修改为符合HTML格式的字符串后重新调用。

## 180101 无效的属性字符串

**错误信息**

invalid styled string.

**错误描述**

在属性字符串序列化CAPI中，ArkUI\_StyledString\_Descriptor的属性字符串对象为空。

**可能原因**

参数中传递的属性字符串对象为空。

**处理步骤**

1. 检查ArkUI\_StyledString\_Descriptor中的属性字符串对象是否已正确初始化。
2. 确认在调用相关接口时，属性字符串对象未被设置为空。
