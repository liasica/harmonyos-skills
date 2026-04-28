---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-ping
title: ohpm ping
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm ping
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:44+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:4f92ccaf4a660f1e7f7c5a10e55ae9f1cce47fdc48a1d199b9f8e46d997d1ee4
---

ping ohpm 仓库地址。

## 命令格式

```
1. ohpm ping
```

## 功能描述

对给定的或者是配置中的仓库地址进行身份验证。如果有效，将会输出相关信息，比如以下内容：

```
1. ohpm INFO: PING your_registry
2. ohpm INFO: PONG 255ms
```

否则将会输出错误信息，比如以下内容：

```
1. ohpm INFO: PING your_registry
2. ohpm ERROR: HttpCode 404, API ping in your_registry - Not Found
```

## Options

### registry

* 默认值：""
* 类型：URL

可以在 ping 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型： Number
* 别名：ft

可以在 ping 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。

### strict\_ssl

* 默认值：true
* 类型：Boolean

可以在 ping 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验 https 证书。

### log\_level

* 默认值：无
* 类型： string

从ohpm 6.0.2.636版本开始，可以在 ping 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。
