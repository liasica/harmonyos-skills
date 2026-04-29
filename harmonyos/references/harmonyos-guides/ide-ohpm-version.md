---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-version
title: ohpm version
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm version
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:53+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:0cee9bbc160b47bc8bc738bde34559d94354ed01754eb28cf34073ca647175b4
---

管理模块版本。

## 命令格式

```
1. ohpm version [options] [<newversion> | major | minor | patch]
```

## 功能描述

在模块目录中运行此命令以获取或升级版本号，同时将数据回写入 oh-package.json5 中。

## 参数说明

### 无参数

当无参数使用ohpm version命令时，则会将当前模块的版本号打印至标准输出中。

### newversion

newversion 参数应为一个合法的语义化版本，命令会将当前模块版本改写为 newversion 并打印在标准输出中。

### major

当参数为 major 时，有以下几种情况：

* 若无先行版本号，则将主版本号递增 1，其他位置为 0；
* 若存在先行版本号：
  + 当次版本号、修订号都为 0 时，则主版本号不变，而将先行版本号删掉。即 1.0.0-beta.1 升级为 1.0.0；
  + 当次版本号、修订号任意一个不为 0 时，则将主版本号递增1，其他位置为 0，并删除先行版本号。即 1.0.1-beta.1 升级为 2.0.0。

### minor

当参数为 minor 时，固定主版本号，变化次版本号与修订号，有以下几种情况：

* 若无先行版本号，则将次版本号递增 1，修订号置为 0；
* 若存在先行版本号:
  + 当修订号为 0 时，则次版本号不变，而将先行版本号删除。即 1.1.0-beta.1 升级为 1.1.0;
  + 当修订号不为 0 时，则将次版本号递增 1，修订号置为 0，同时删除先行版本号，即 1.1.1-beta.1 升级为 1.2.0。

### patch

当参数为 patch 时，固定主版本号与次版本号，变化修订号，有以下几种情况：

* 若无先行版本号，则修订号递增 1。即 1.0.0 升级为 1.0.1；
* 若存在先行版本号，则仅删除先行版本号。即 1.0.0-beta.1 升级为 1.0.0。

## Options

### prefix

* 默认值：""
* 类型： string

可以在 version 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。

### parameterFile

* 默认值：无
* 类型： string
* 别名：pf

可以在 version 命令后面配置 --pf <string> 或者 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 version 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

当前模块为 entry，版本号为 1.0.0，在当前模块的根目录执行：

```
1. ohpm version
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/igHp7whlRVauCHdmmIB2dg/zh-cn_image_0000002530752894.png?HW-CC-KV=V1&HW-CC-Date=20260429T054752Z&HW-CC-Expire=86400&HW-CC-Sign=866D1086487931EC9C1CA5511558134B3ADE7D2A17A9E742CD438B0F4F7086DF "点击放大")

接着执行：

```
1. ohpm version 1.0.1-beta.1
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/2rqXZhI_StWi3zS9XOXr0g/zh-cn_image_0000002561832815.png?HW-CC-KV=V1&HW-CC-Date=20260429T054752Z&HW-CC-Expire=86400&HW-CC-Sign=526942C0CC9BD7A3ADF42CFF28028DB4A3FD21F5D28E9069662C2F4B840B0B81 "点击放大")

接着执行：

```
1. ohpm version major
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/7EF6TUTORrqSaH3hJVR24g/zh-cn_image_0000002561832819.png?HW-CC-KV=V1&HW-CC-Date=20260429T054752Z&HW-CC-Expire=86400&HW-CC-Sign=4F53044FAB4968267F9556579F7E9418DD058ECB797C6AAD7D94CF99929A0DF3 "点击放大")
