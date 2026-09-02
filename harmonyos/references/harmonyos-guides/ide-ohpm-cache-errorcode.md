---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-cache-errorcode
title: ohpm cache clean错误码
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm cache clean错误码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:59+08:00
doc_updated_at: 2026-07-21
content_hash: sha256:236d37e7e69cc3a3f8f29a1ff02387904ff5677f4f8e55dd7a4a57e4787c2e19
---

## 00601001 缓存子命令为空

**错误信息**

Cache Subcommand Is Empty.

**错误描述**

缓存子命令为空。

**可能原因**

缓存子命令缺失或子命令不正确。

**处理步骤**

检查输入的子命令格式，确保输入正确的缓存子命令 ohpm cache clean。

## 00601002 缓存子命令不支持

**错误信息**

Cache Subcommand Not Support.

**错误描述**

不支持缓存子命令。

**可能原因**

输入的命令不支持配置Cache子命令。

**处理步骤**

确认可配置Cache子命令的命令列表（如 clean 或 -h）。

## 00601003 缓存包无效

**错误信息**

Invalid Cache Package.

**错误描述**

缓存包无效。

**可能原因**

* 缓存包被修改，导致缓存包损坏/不完整。
* 网络问题，使从仓库中下载的包在本地校验失败。

**处理步骤**

1. 执行ohpm cache clean清理缓存，然后执行ohpm install安装依赖。
2. 检查ohpmrc文件中registry配置是否正确。
