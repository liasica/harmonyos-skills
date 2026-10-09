---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ohpm-root
title: ohpm root
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm root
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:21856827e405743c4566f7c431ff29878a7b80057ec71362b6c2c992219e2f43
---

在标准输出中打印有效的 oh\_modules 目录路径信息。

支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

## 命令格式

```screen
ohpm root
```

## 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh\_modules 目录路径信息。

## Options

### prefix

* 默认值：""
* 类型： string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh\_modules 目录路径信息。

### log\_level

* 默认值：无
* 类型： String

可以在 root 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

在entry模块的src目录下执行：

```screen
ohpm root
```

结果示例：

```screen
pwd
/storage/Users/currentUser/Documents/DevEcoStudioProjects/MyApplication01/entry/src
ohpm root
/storage/Users/currentUser/Documents/DevEcostudioProjects/MyApplication01/entry/oh_modules
```
