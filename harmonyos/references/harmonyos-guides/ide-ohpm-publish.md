---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-publish
title: ohpm publish
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm publish
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:52+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:67696221db76a363a7d0b4dd233b3d04e09e6f88631dee322f8904a49a9369bc
---

发布一个三方库。

## 命令格式

```
1. ohpm publish [options] <har_or_tgz_file>
```

说明

* har\_or\_tgz\_file：压缩包路径，可以是 .har 包格式和由 hsp 模块打包出来的 .tgz 包格式，必选参数。
* ohpm 命令行 1.3.0 之前版本仅支持发布 .har 包，从 1.3.0 版本开始支持发布 .tgz 包。
* ohpm命令行 5.0.1 版本开始支持发布与下载最大300M的.har/.tgz包。

## 功能描述

* 将三方库发布到 OpenHarmony 三方库中心仓，以便可按名称安装它。 发布前，需要完成公钥私钥生成，把公钥上传服务端，并在ohpmrc 文件中配置公仓的发布码和私钥路径。
* 默认情况下，ohpm 将发布到 [OpenHarmony 三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)，但仍可以通过指定不同的 publish\_registry 值（详情可查阅 [ohpmrc](ide-ohpmrc.md) 章节 中 publish\_registry 描述信息），发布到指定的仓库。
* 如果指定的仓库中已存在三方库名称和版本组合，则发布失败。
* 一旦三方库以给定的名称和版本发布并审核通过后，该特定名称及对应的版本号将被占用，无法再次使用，即使它已被 [ohpm unpublish](ide-ohpm-unpublish.md) 下架。

注意

* 为了保证.har 和 .tgz 包的编译与运行正常，包中的 oh-package.json5 必须包含该包的所有直接依赖，若有依赖通过项目级别的 oh-package.json5 引入，则相应的依赖也必须写入包中对应的 oh-package.json5 中。
* 请注意debug模式构建的HAR包中含有源码，便于本地调试，请注意代码安全，详细请参考[构建HAR](ide-hvigor-build-har.md)。
* 发布包前请务必检查待发布包 oh-package.json5 的配置是否满足要求，具体要求请参考：[oh-package.json5 字段说明](ide-oh-package-json5.md#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)

## 发布校验规则

### 三方库校验规则

1. ohpm打包的三方库须以.har和.tgz作为其扩展名；
2. 三方库所有内容须放置在package目录内，且package目录内需包含oh-package.json5配置文件、README.md文件、LICENSE文件和CHANGELOG.md文件，其中oh-package.json5配置文件须包含必选字段（请参阅[oh-package.json5](ide-oh-package-json5.md)文件字段说明）；

   说明

   README.md文件、LICENSE文件和CHANGELOG.md三个文件在该HAR包发布至[OpenHarmony 三方库中心仓](https://ohpm.openharmony.cn/#/cn/help/publishrequirefile)时必须包含，且不能为空。
3. 将package目录压缩为tgz包，并将后缀名改为.har，即可获得三方库的HAR包。

### 开闭源规则

1. 开源

   不进行 ArkTS 代码相关编译的，只进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块的部分原始配置文件会被打包。其 oh-package.json5 文件中的 "artifactType" 字段值为 original。
2. 闭源

   ArkTS 代码会被编译成混淆的 js 和 d.ets 和 d.ts 等声明文件，进行 cpp 代码编译和 OpenHarmony 资源处理，还有模块的部分原始配置文件会被打包。其 oh-package.json5 文件中 "artifactType" 属性值为 obfuscation。此时则检查 oh-package.json5 文件中 "types" 属性中定义的声明文件是否带有扩展名 ".d.ts/.d.ets"，且对应路径下存在该文件。若无则进行报错，且不会发布。

## Options

### publish\_id

* 默认值：""
* 类型：String

可以在 publish 命令后面配置 --publish\_id <id> 参数，指定发布码。

### key\_path

* 默认值：""
* 类型：String

可以在 publish 命令后面配置 --key\_path <p> 参数，指定ssh私钥路径。

### tag

* 默认值：无
* 类型：String
* 别名：t

可以在 publish 命令后面配置 -t <tag\_name>或者 --tag <tag\_name> 参数，给将要发布的三方库打上标签。

### publish\_registry

* 默认值：""
* 类型：URL

可以在 publish 命令后面配置 --publish\_registry <r> 参数，指定发布仓库地址。如果未指定，默认从配置中获取发布仓库地址。

### source\_type

* 默认值：无
* 类型： String

从ohpm 6.1.1.816版本开始，可以在 publish 命令后配置--source\_type <string>参数，指定将要发布的三方库的开闭源类型。如果值为closed，则不校验发布的三方包是否包含 LICENSE 文件，发布的三方库是闭源类型；如果值为open，则校验发布的三方包必须包含 LICENSE 文件，发布的三方库是开源类型。

### fetch\_timeout

* 默认值：60000
* 类型： Number
* 别名：ft

可以在 publish 命令后面配置 --ft <number>或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。

### strict\_ssl

* 默认值：true
* 类型： Boolean

可以在 publish 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验 https 证书。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 publish 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### use\_stream\_threshold\_size

* 默认值：无
* 类型： Number

从ohpm 6.0.2.636版本开始，可以在 publish 命令后配置--use\_stream\_threshold\_size <number>参数，指定流式上传阈值，取值范围：[0, 300]，单位mb。当publish三方库的文件体积超过阈值时，将使用流式方式上传；如果仓库不存在流式上传接口，则转为Base64方式上传。

### compability\_log\_level

* 默认值：无
* 类型：String

从ohpm 6.0.2.636版本开始，可以在 publish 命令后配置 --compability\_log\_level <string> 参数，在publish命令时，ohpm会检测oh-package.json5文件中是否配置了兼容性检测需要的所有字段（'compatibleSdkVersion', 'compatibleSdkType', 'obfuscated', 'nativeComponents'）。如果未配置，则会根据compability\_log\_level设置的日志等级（info、debug、warn、error）打印提示或报错。详情请见[compability\_log\_level](ide-ohpmrc.md#section96369529419)。

### disallow\_nested\_package

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 publish 命令后配置 --disallow\_nested\_package 参数。在执行publish命令时，会扫描包内是否存在'./'形式配置，且后缀为.har/.tgz格式的依赖。如果存在，则命令执行失败并提示报错信息，详情请见[disallow\_nested\_package](ide-ohpmrc.md#section1237023983514)。

### ensure\_dependency\_include

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 publish 命令后配置 --ensure\_dependency\_include 参数，会开启依赖扫描功能，详情请见[ensure\_dependency\_include](ide-ohpmrc.md#section1291814578276)。

### cache

* 默认值：无
* 类型：string

从ohpm 6.0.2.636版本开始，可以在 publish 命令后面配置 --cache <string> 参数，设置缓存路径。

## 示例

发布工作目录下的三方库，执行以下命令：

```
1. ohpm publish publish_test.har
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/vYjkEj5wTLeWt5dMAA5eMw/zh-cn_image_0000002561832663.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=33902AC7D1B97F0C59993865FDA43BFE55FA32C6B082A6E534C2B58CC52456E5)
