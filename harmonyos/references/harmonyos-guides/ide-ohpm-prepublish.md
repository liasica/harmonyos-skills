---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-prepublish
title: ohpm prepublish
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm prepublish
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:42+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:7d971f0b0026f709dd60c96a31ebea0237fdc827b946c1b892128403bccfa525
---

预发布一个三方库。

## 命令格式

```
1. ohpm prepublish [options] <har_or_tgz_file>
```

说明

* har\_or\_tgz\_file：压缩包路径，可以是 .har 包格式和由 hsp 模块打包出来的 .tgz 包格式，必选参数。
* ohpm v1.8.0 版本开始支持prepublish命令。

## 功能描述

* 拥有publish命令的所有内容校验规则，可以在发布前检测待发布的三方库能否通过ohpm客户端校验。
* 只校验待发布三方库内容，不对publish\_registry、publish\_id、key\_path等做校验。
* 包的格式、结构及具体校验规则可参考[publish命令说明](ide-ohpm-publish.md)。

## Options

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 prepublish 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

预发布工作目录下的三方库，执行以下命令：

```
1. ohpm prepublish publish_test.har
```

结果示例：

```
1. C:\Program Files\Huawei\DevEco Studio\tools\ohpm\bin> ohpm prepublish D:\publish_test.har
2. prepublish publish_test 1.0.0 succeed.
```
