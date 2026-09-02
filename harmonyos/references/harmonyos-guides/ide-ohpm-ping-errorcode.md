---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-ping-errorcode
title: ohpm ping错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm ping错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2376f301d5f735a02bbd612193cabba205ffd5df76dd16417fb4c9f15b186679
---

## 00632001 ping仓库失败

**错误信息**

Ping Registries Failed.

**错误描述**

ping仓库地址失败。

**可能原因**

无法成功ping仓库地址，可能是仓库地址与.ohpmrc配置文件中仓库地址不一致，或网络连接问题。

**处理步骤**

检查仓库地址以及网络连接是否可用。

## 00632002 仓库地址为空

**错误信息**

Registry Is Empty.

**错误描述**

仓库地址为空。

**可能原因**

未设置仓库地址。

**处理步骤**

编辑.ohpmrc文件，或使用命令ohpm config set <key> <value>设置仓库地址（如ohpm config set registry https://ohpm.openharmony.cn/ohpm/）。

## 00638001 命令行中使用了无效选项

**错误信息**

Invalid Option.

**错误描述**

命令行中使用了无效的选项。

**可能原因**

在命令行中输入的选项无效，可能是拼写错误、选项不支持或参数格式错误。

**处理步骤**

检查和确认命令支持的选项后再执行。
