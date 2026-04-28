---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-publish-errorcode
title: ohpm publish错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm publish错误码
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:517b6ff9372191795cc0d7f5a719528f3d7eb65c7fa0c79686580b8ecabf7dea
---

## 00609001 依赖声明缺失

**错误信息**

Dep Statements Missing.

**错误描述**

依赖声明缺失。

**可能原因**

在oh-package.json5的dependencies/dynamicDependencies未声明。

**处理步骤**

确保导入的依赖项在oh-package.json5文件的 "dependencies" 或 "dynamicDependencies" 中声明，具体可参考[ensure\_dependency\_include](ide-ohpmrc.md#section1291814578276)。

## 00609002 私钥路径不存在

**错误信息**

Key Path Is Empty Or NotFound.

**错误描述**

私钥路径为空或未找到。

**可能原因**

在.ohpmrc文件中没有配置私钥路径。

**处理步骤**

在.ohpmrc文件中配置有效的私钥路径。

## 00609003 私钥文件不存在

**错误信息**

Private Key File Not Exist.

**错误描述**

私钥文件不存在。

**可能原因**

.ohpmrc文件中配置的私钥路径不存在或错误。

**处理步骤**

检查.ohpmrc文件中的私钥路径配置，确保私钥文件存在。

## 00609004 私钥文件路径错误

**错误信息**

Key Path Is DirError.

**错误描述**

私钥路径错误。

**可能原因**

私钥路径文件错误。

**处理步骤**

确保.ohpmrc中配置的私钥文件路径指向私钥文件。

## 00609005 发布ID为空

**错误信息**

Publish Id Is Empty.

**错误描述**

发布ID为空。

**可能原因**

未在.ohpmrc文件配置publish\_id字段。

**处理步骤**

在.ohpmrc文件中配置publish\_id。

## 00609006 私钥文件内容为空

**错误信息**

Private Key Content Is Empty.

**错误描述**

私钥文件内容为空。

**可能原因**

私钥文件内容为空。

**处理步骤**

重新生成私钥文件。

## 00609007 不支持的私钥

**错误信息**

Not Support PrivateKey.

**错误描述**

不支持的私钥。

**可能原因**

未配置使用非空密码加密的私钥。

**处理步骤**

在.ohpmrc文件中配置加密的私钥密码。

## 00609009 HSP文件为空

**错误信息**

Hsp File Is Empty.

**错误描述**

HSP文件为空。

**可能原因**

HSP文件内容为空。

**处理步骤**

确保HSP文件包含有效内容。

## 00609010 tgz文件无效

**错误信息**

Invalid Tgz File.

**错误描述**

无效的TGZ文件。

**可能原因**

路径对应的文件中未包含.hsp文件。

**处理步骤**

检查tgz文件路径，确保路径对应的文件中包含.hsp文件。

## 00609011 构建tgz元数据失败

**错误信息**

Build Tgz Metadata Failed.

**错误描述**

构建tgz元数据失败。

**可能原因**

字段信息配置问题。

**处理步骤**

检查包oh-package.json5的配置，确保各字段配置正确。

## 00609012 依赖包被锁定

**错误信息**

Pkg Is Locked.

**错误描述**

依赖包被锁定。

**可能原因**

三次上传失败，依赖包被锁定。

**处理步骤**

等待一段时间后重试，再上传。

## 00609013 超出最大长度限制

**错误信息**

Over Maximum Length Error.

**错误描述**

超出最大长度限制。

**可能原因**

配置的name、email、url值的长度超过了最大限制。

**处理步骤**

检查值的长度，确保其在允许的范围内。name长度范围为[1,128]，email长度范围为[1，64]，url长度范围为[1，256]。

## 00609014 解析源文件失败

**错误信息**

Parse Source File Error.

**错误描述**

解析源文件失败。

**可能原因**

.ohpmrc配置文件格式不正确。

**处理步骤**

检查和确认配置文件的内容和格式，确保正确。

## 00609015 未配置兼容性字段

**错误信息**

Check Compatibility Field Error.

**错误描述**

检查兼容性字段失败。

**可能原因**

oh-package.json5文件中未配置兼容性字段。

**处理步骤**

确保oh-package.json5文件中配置了必要的兼容性检测字段。

## 00640001 系统错误

**错误信息**

System Error.

**错误描述**

系统错误。

**可能原因**

系统错误，例如内存错误等。

**处理步骤**

检查日志文件，寻找错误信息定位根源。
