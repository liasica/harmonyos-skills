---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dist-tags
title: ohpm dist-tags
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm dist-tags
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:45+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:47009c523e8e82060c6498bdb47c3e435a07354941cbe5c942261f41b4f8312e
---

tag可标记一个三方库的某个版本，在install时可用tag代替版本号安装包。

## 命令格式

```
1. ohpm dist-tags [subcommand] [<@group>/]<pkg>[@<version>] <tag>
2. alias: dist-tags
```

说明

* subcommand: 包含list、add、update、remove四个子命令。
* @group: 三方库的命名空间，可选。
* pkg: 三方库名称，必选。
* version: 三方库的版本号，在add、update子命令时必选。
* tag: 标签，在add、update、remove子命令时必选。tag必须以大小写字母或数字开头，只允许包含大小写字母、数字、点号(.)、下划线(\_)和中划线(-)，最大长度为60个字符。

## 功能描述

操作tag。分为查看三方库的所有tag，给三方库的某个版本添加tag，修改tag到三方库的另一个版本，删除三方库的某个tag。

说明

"latest"是一个预设的标签，不允许直接通过dist-tags命令来进行修改。该标签自动指向最高的正式版本；若无正式版本，则默认指向最高的先行版本。

以第三方库a为例，假定其版本序列包括"1.0.1-beta"、"1.0.1"和"2.0.1-beta"，在这种情况下，"latest"会自动映射到"1.0.1"，因为它是当前最高的正式版本。

## 子命令

### list

```
1. ohpm dist-tags list [<@group>/]<pkg>
2. alias: ls
```

列出指定三方库的所有标签。输出结果中，`latest`标签始终位于首位，其他标签按照字典序排列显示。

### add

```
1. ohpm dist-tags add [<@group>/]<pkg>[@<version>] <tag>
```

给某个版本的三方库增加一个标签。若该三方库已存在相同标签，则添加操作将会失败。

### update

```
1. ohpm dist-tags update [<@group>/]<pkg>[@<version>] <tag>
2. alias: up
```

更新指定包的某个标签所对应的版本。如果指定的标签不存在，则更新操作将失败。

### remove

```
1. ohpm dist-tags remove [<@group>/]<pkg> <tag>
2. alias: rm
```

删除指定包的一个标签。如果该标签并未存在于包中，则删除操作将会失败。

## Options

### publish\_id

* 默认值：""
* 类型：String

可以在 dist-tags 命令后面配置 --publish\_id <id> 参数，指定发布码。

### key\_path

* 默认值：""
* 类型：String

可以在 dist-tags 命令后面配置 --key\_path <p> 参数，指定ssh私钥路径。

### registry

* 默认值：无
* 类型：URL

可以在 dist-tags 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。

### publish\_registry

* 默认值：""
* 类型：URL

可以在 dist-tags 命令后面配置 --publish\_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型： Number
* 别名：ft

可以在 dist-tags 命令后面配置 --ft <number>或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。

### strict\_ssl

* 默认值：true
* 类型： Boolean

可以在 dist-tags 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验 https 证书。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 dist-tags 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

如果想要通过使用tag，在oh-package.json5文件中引入包@ohos/axios的1.0.0版本，步骤如下：

1. 通过ohpm dist-tags的子命令add，对包@ohos/axios的1.0.0版本添加标签名beta。

```
1. ohpm dist-tags add @ohos/axios@1.0.0 beta
```

2. 在oh-package.json5文件中，使用标签beta引入包@ohos/axios的1.0.0版本。

```
1. {
2. "dependencies": {
3. // tag标签引入，引入标签为"beta"对应的版本号1.0.0
4. "@ohos/axios": "tag:beta"
5. }
6. ...
7. ...
8. }
```
