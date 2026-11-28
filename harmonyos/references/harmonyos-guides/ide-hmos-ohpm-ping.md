---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ohpm-ping
title: ohpm ping
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm ping
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:59+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:ad74a1af840e85b31bbc277e4c9445daf5e0a99d949cb05ee676d6265e66c418
---

ping ohpm 仓库地址。

支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

## 命令格式

```screen
ohpm ping
```

## 功能描述

对给定的或者是配置中的仓库地址进行身份验证。如果有效，将会输出相关信息，比如以下内容：

```screen
ohpm INFO: PING your_registry
ohpm INFO: PONG 255ms
```

否则将会输出错误信息，比如以下内容：

```screen
ohpm INFO: PING your_registry
ohpm ERROR: HttpCode 404, API ping in your_registry - Not Found
```

## Options

### registry

* 默认值：""
* 类型：URL

可以在 ping 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型： number
* 别名：ft

可以在 ping 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为 60000 ms。

### strict\_ssl

* 默认值：true
* 类型：boolean

可以在 ping 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验 https 证书。

### log\_level

* 默认值：无
* 类型： string

可以在 ping 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。
