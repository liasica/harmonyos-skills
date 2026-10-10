---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-compile-build
title: 构建产物说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 概述 > 构建产物说明
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c50a5fe043a481b87af3708c1c1a11fc4a4c2cb0dbab291aa268047ec085b8b3
---

## HAP/HSP构建产物说明

以HAP为例，release模式的构建产物一般包含以下文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/KApSin4tQme2EALTH2nzYg/zh-cn_image_0000002750009926.png)

* resources：构建产物中的资源文件目录，如图片、媒体资源、配置文件等。
* modules.abc：构建产物中通过源码编译出的字节码文件。
* module.json：构建产物中通过模块src目录中的module.json5处理后的运行时配置文件，具体参考[module.json5配置文件](module-configuration-file.md)。
* resources.index：构建产物中的资源索引文件，包含模块中所有的资源ID、资源名称、资源类型以及资源值等信息。
* pack.info：构建产物中的包内容描述文件，在安装升级时提供相关信息。
* pkgContextInfo.json：构建产物中的语境信息表文件，用于运行时查找依赖库信息。

**说明** 

* resources.index文件中可以看到明文信息，为防止泄露，请勿将敏感信息直接明文配置在如string.json等资源文件中。
* 模块的src/main/ets目录，编译时仅处理.ets/.ts/.js文件，其他文件会被当作资源文件打包进产物中，不会进行混淆或加密，因此请勿将敏感信息存放在该目录下。
* 以debug模式构建的HAP/HSP包中的ets目录下存在sourceMaps.map文件，此文件包含源码映射等信息。sourceMaps.map文件格式及解析流程请参考[ArkTS堆栈解析原理](ide-exception-stack-parsing-principle.md)。

## HAR构建产物说明

详情请参考[构建HAR](ide-hmos-hvigor-build-har.md)。

## App构建产物说明

APP构建产物如下，其中包名取决于个人项目中的模块名，与下图可能不同：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/un-EBk70Q5-SdazgVk3Q_w/zh-cn_image_0000002779728989.png)

* entry-default.hap：由字节码、资源、三方库、配置文件等打包生成的entry类型的hap包，是App应用安装和运行的基本单元，application-default.hap是feature类型的hap。
* library1-default.hsp：由字节码、资源、三方库、配置文件等打包生成的动态共享包，可实现代码和资源共享。
* pack.info：应用App构建产物中的包内容描述文件，提供应用市场发布上架所需信息。
* pac.json：应用App构建产物中的隐私清单文件，文件中可配置的字段请参考[pac.json5隐私清单文件](agc-pac.md)，用于提供应用市场发布上架所需信息。
