---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-clean
title: ohpm clean
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm clean
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:44+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:261952b25f01e900e231ecbdf8dd59d19af6a3fd750275599f86d908daf2cedd
---

清理工程下所有模块的ohpm安装产物。

## 命令格式

```
1. ohpm clean|cls
```

## 功能描述

清理工程下所有模块的oh\_modules目录、oh-package-lock.json5文件和oh-package-targetName-lock.json5文件（指定选项--target\_path安装时生成）()，清理完成后会在控制台打印耗时信息。

## Options

### keep-lockfile

* 默认值：false
* 类型： Boolean
* 别名：kl

可以在 clean 命令后面配置--kl或者--keep-lockfile参数，执行清理时会保留oh-package-lock.json5文件和oh-package-targetName-lock.json5文件（指定选项--target\_path安装时生成）。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 clean 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 注意事项

* clean命令只会清理工程根目录和在build-profile.json5文件中modules节点下配置的模块。
* 当build-profile.json5文件不存在时，当前oh-package.json5文件所在目录即为工程根目录。

## 示例

当前工程为 test，子模块为testModule1，工程结构如下：

```
1. test
2. |————testModule1
3. |————libs
4. |————oh-package.json5
5. |————build-profile.json5
6. |————oh-package.json5
```

在当前工程的任意子目录执行（以libs目录下执行为例）：

```
1. ohpm clean
```

结果示例：

```
1. D:\test\testModule1\libs>ohpm clean
2. ohpm DEBUG: startClean.
3. ohpm DEBUG: clean all modules under: D:\test
4. ohpm DEBUG: begin to clean module: D:\test\testModule1
5. ohpm DEBUG: begin to clean module: D:\test
6. ohpm DEBUG: clean module: D:\test\testModule1 succeed.
7. ohpm DEBUG: clean module: D:\test succeed.
8. clean completed in 0s 67ms
```
