---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-errorcode-universal
title: ohpm命令公共错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm命令公共错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:adba6041da5ec9a64a0ab4b950c076d35942149a49122046e32308f360958c13
---

## 00617101 获取包信息失败

**错误信息**

Fetch Pkg Info Failed.

**错误描述**

获取包信息失败。

**可能原因**

未配置仓库地址。

**处理步骤**

在.ohpmrc文件中配置registry字段，或执行命令"ohpm config set registry https://ohpm.openharmony.cn/ohpm/"配置仓库地址。

## 00617102 检查仓库失败

**错误信息**

Check Registry Failed.

**错误描述**

检查仓库失败。

**可能原因**

执行ohpm info、ohpm install命令时，配置的registry参数错误。

**处理步骤**

检查和确保仓库地址为中心仓地址或私仓地址。

## 00608003 读取文件时发生错误

**错误信息**

File Read Error.

**错误描述**

读取文件时发生错误。

**可能原因**

读取配置等文件失败。

**处理步骤**

查看是否被占用后，重新读取。

## 00625003 文件不存在

**错误信息**

File Not Exist.

**错误描述**

文件不存在。

**可能原因**

读取文件不存在。

**处理步骤**

查看文件是否存在，重新读取。

## 00631002 仓库请求失败

**错误信息**

Registry Request Error.

**错误描述**

仓库请求失败。

**可能原因**

执行ohpm publish、ohpm dist-tags命令时，配置的publish\_registry参数错误。

**处理步骤**

检查和确保仓库地址为中心仓地址或私仓地址。

## 00640001 系统错误

**错误信息**

System Error.

**错误描述**

系统错误。

**可能原因**

系统错误，例如内存错误等。

**处理步骤**

检查日志文件，寻找错误信息定位根源。

## 00670002 路径大小写敏感错误

**错误信息**

Path Case Sensitivity Error.

**错误描述**

路径大小写敏感错误。

**可能原因**

工程中文件的配置路径和文件的实际路径大小写不一致。

**处理步骤**

修改工程中配置的文件路径，使其与文件的实际路径一致；或者设置.ohpmrc文件中的case\_sensitive\_check为false，不检测文件路径大小写。更多请参考[case\_sensitive\_check](ide-ohpmrc.md#section2045412394117)。
