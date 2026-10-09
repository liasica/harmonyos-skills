---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ohpm-help
title: ohpm help
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm help
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:50387f90379862b88f87a2542d7d851e69137b8e5826f2ac616ee193dc3ea36d
---

获取有关 ohpm 的帮助。

## 命令格式

```screen
ohpm help [command]
ohpm [command] --help
alias: -h
```

**说明** 

command：命令名称。

## 功能描述

如果提供了命令名称，则显示相应命令的帮助信息。

如果提供的命令名称不存在或未提供，则显示所有命令的概要信息。

## 示例

执行以下命令：

```screen
ohpm -h
```

结果示例：

```screen
Usage: ohpm [command] [options]

Options:
  -v, --version  output the ohpm version
  -h, --help     display help for command

Commands:
  config         Manage the ohpm configuration file
  info           Display the information about a package
  init           Create an oh-package.json5 file
  install        Install package(s)
  list           Display the dependency graph
  ping           Test the network connectivity to registry
  prepublish     Pre-verification package content
  publish        Publish a package to the registry
  uninstall      Uninstall package(s)
  unpublish      Unpublish a package from target registry
  update         Update package(s) to their latest version based on the specified range
  root           Print the effective oh_modules folder to standard out
  version        Bump a package version
  cache          Manage the ohpm cache folder
  run            Run user defined package scripts, the optional parameter 'args' is used to append
                 or override script parameters in the form '(-key/--key value), (-key/--key=value), (-key/--key=a=b)'
  clean          Delete all 'oh_modules' directories and the 'oh-package-lock.json5' file in the current project
  dist-tags      Manage version tags of package
  convert        Convert all the packages to the ohpm packages
  help           display help for command
```
