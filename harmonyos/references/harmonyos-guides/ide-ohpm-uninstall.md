---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-uninstall
title: ohpm uninstall
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm uninstall
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2ae75491870b49974d3423ecc15aadb9e46a4a171265e6c5cd4b2529f58a7e2
---

卸载三方库。

## 命令格式

```screen
ohpm uninstall [options] [<@group>/]<pkg> ...
alias: un
```

**说明** 

* @group：三方库的命名空间，可选。
* pkg：三方库名称，必选。

## 功能描述

卸载指定已安装的模块，并将 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息；若没有指定三方库，则不做任何动作。

如无需在 oh-package.json5 文件中 dependencies、devDependencies 属性里移除指定三方库信息，则可配置 --no-save 参数。

## Options

### install\_all

* 默认值：true
* 类型：Boolean
* 别名：all

您可以在uninstall命令后面不配置参数，配置--all或者--install\_all 参数，表示卸载当前模块指定依赖成功后同时安装当前工程下的所有模块的依赖。

从ohpm 26.0.0.630版本开始，如无需卸载，可配置--no-install\_all 参数。

### no-save

* 默认值：true
* 类型：Boolean

可以在uninstall命令后面配置--no-save参数，卸载的三方库信息不会从oh-package.json5文件中删除。不配置参数时，卸载的三方库信息将从 oh-package.json5 文件中删除。

### prefix

* 默认值：""
* 类型：string

可以在 uninstall 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。

### registry

* 默认值：""
* 类型：URL

可以在 uninstall 命令后面配置 --registry <registry> 参数，当检测到oh-package.json5文件存在未安装的三方包时，卸载命令执行后，会自动从registry指定的仓库中下载并安装该三方包；如果没有指定，默认从配置中获取仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型：Number
* 别名：ft

可以在 uninstall 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。

### strict\_ssl

* 默认值：true
* 类型：Boolean

在uninstall命令后面不配置参数、配置--strict\_ssl或--strict\_ssl true参数时，开启校验HTTPS证书。

从ohpm 26.0.0.630版本开始，如需关闭校验，可配置--no-strict\_ssl或--strict\_ssl false参数，推荐使用--no-strict\_ssl参数。

### experimental-concurrently-safe

* 默认值：true
* 类型：Boolean

可以在uninstall命令后面配置--experimental-concurrently-safe参数，并发安全地安装依赖。

从ohpm 26.0.0.630版本开始，如无需并发地安装依赖时，配置--no-experimental-concurrently-safe参数。

### log\_level

* 默认值：无
* 类型：string

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### lockfile\_stable\_order

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后面配置 --lockfile\_stable\_order 参数，会确保在oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。

### odm\_r2\_project\_root

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后面配置 --odm\_r2\_project\_root 参数，当存在overrideDependencyMap配置且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析来查找这些相对路径。详情参见[odm\_r2\_project\_root](ide-ohpmrc.md#section136621053184912)。

### resolve\_conflict\_strict

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后面配置 --resolve\_conflict\_strict 参数，ohpm会按照严格模式处理依赖版本冲突，详情参见[resolve\_conflict\_strict](ide-ohpmrc.md#section1942983310492)。

### resolve\_conflict

* 默认值：true
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后面配置 --resolve\_conflict 参数，ohpm会自动处理依赖版本冲突，详情参见[resolve\_conflict](ide-ohpmrc.md#section368717475562)。

从ohpm 26.0.0.630版本开始，如无需自动处理时，配置 --no-resolve\_conflict 参数。

### cache

* 默认值：无
* 类型：string

从ohpm 6.0.2.636版本开始，可以在 uninstall 命令后面配置 --cache <string> 参数，设置缓存路径。

## 示例

从当前工程下卸载**直接**依赖的某个package。

执行以下命令：

```screen
ohpm uninstall lottie
```

**说明** 

* ohpm 1.0.0~1.3.0
  + 使用 ohpm 卸载时，如果 json 是直接依赖的三方包，则当前工程 oh\_modules 目录下文件夹 lottie 目录被删除，以及 json 对应的间接依赖也可能被删除（若间接依赖的包没有被其他三方包关联引用的情况下）。
  + oh-package.json5 文件中 dependencies 属性删除对应的行（例如："lottie": "2.0.7"）。
* ohpm 1.4.x
  + ohpm 客户端从 1.4.0 版本开始，使用 ohpm 卸载时，项目级 oh\_modules 目录下的文件夹 lottie 目录**不会**被删除，模块级 oh\_modules 目录下的文件夹 lottie 目录会被删除。
  + oh-package.json5 文件中 dependencies 属性删除对应的行（例如："lottie": "2.0.7"）。
