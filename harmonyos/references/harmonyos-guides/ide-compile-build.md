---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compile-build
title: 构建产物说明
breadcrumb: 指南 > 构建应用 > 概述 > 构建产物说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e1fa98335320b751cb3486e227c029459beec7ade7b8505d74b1db498fdf33ce
---

## HAP/HSP构建产物说明

以HAP为例，release模式的构建产物一般包含以下文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/GEyUTOOUQvKITZA9sEdnjQ/zh-cn_image_0000002561832711.png?HW-CC-KV=V1&HW-CC-Date=20260427T235710Z&HW-CC-Expire=86400&HW-CC-Sign=95AE164672C230770FA8F82D70FFBAA90EFB18A60EE407A4DDB92C4B3A1FDE01)

* resources：构建产物中的资源文件目录，如图片、媒体资源、配置文件等。
* modules.abc：构建产物中通过源码编译出的字节码文件。
* module.json：构建产物中通过模块src目录中的module.json5处理后的运行时配置文件，具体参考[module.json5配置文件](module-configuration-file.md)。
* resources.index：构建产物中的资源索引文件, 包含模块中所有的资源ID、资源名称、资源类型以及资源值等信息。
* pack.info：构建产物中的包内容描述文件，在安装升级时提供相关信息。
* pkgContextInfo.json：构建产物中的语境信息表文件，用于运行时查找依赖库信息。

注意

* resources.index文件中可以看到明文信息，为防止泄漏，请勿将敏感信息直接明文配置在如string.json等资源文件中。
* 模块的src/main/ets目录，编译时仅处理.ets/.ts/.js文件，其他文件会被当作资源文件打包进产物中，不会进行混淆或加密，因此请勿将敏感信息存放在该目录下。
* 以debug模式构建的HAP/HSP包中的ets目录下存在sourceMaps.map文件，此文件包含源码映射等信息。sourceMaps.map文件格式及解析流程请参考[ArkTS堆栈解析原理](ide-exception-stack-parsing-principle.md#section5924954297)。
* LiteWearable设备使用标准JS运行时，因此对应的应用开发在release模式下的构建产物中包含JS源码，请注意代码资产保护。

## HAR构建产物说明

详情请参考[构建HAR](ide-hvigor-build-har.md)。

## App构建产物说明

APP构建产物如下，其中包名取决于个人项目中的模块名，与下图可能不同：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AGPukTtoRsa0HtmygLEAGQ/zh-cn_image_0000002530912788.png?HW-CC-KV=V1&HW-CC-Date=20260427T235710Z&HW-CC-Expire=86400&HW-CC-Sign=983515784FE8AB75C67D2E61F35A4E97FD321EE390E67E8D8B16FF27D0EB92A2)

* entry-default.hap：由字节码、资源、三方库、配置文件等打包生成的entry类型的hap包，是App应用安装和运行的基本单元，application-default.hap是feature类型的hap。
* library-default.hsp：由字节码、资源、三方库、配置文件等打包生成的动态共享包，可实现代码和资源共享。
* pack.info：应用App构建产物中的包内容描述文件，提供应用市场发布上架所需信息。
* pac.json：应用App构建产物中的隐私清单文件，文件中可配置的字段请参考[pac.json5隐私清单文件](agc-pac.md)，用于提供应用市场发布上架所需信息。
