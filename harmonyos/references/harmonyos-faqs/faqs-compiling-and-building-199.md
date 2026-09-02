---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-199
title: 如何解决编译本地依赖包失败的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译本地依赖包失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2385c883ca072af993f731afb2d6a3b191d02ea62903c6b348c9f364ad3334f6
---

## 问题现象

编译本地依赖包失败，一直报错：

```txt
dependent module does not exist.
```

## 背景知识

HSP（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布上架，而是跟随宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* [集成态HSP](../harmonyos-guides/integrated-hsp.md)：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于宿主应用HAP的应用内HSP。

## 问题定位

* 检查依赖的共享包模块是否安装。
* 检查Deploy Multi Hap Packages配置。
* 检查Auto Dependencies配置。
* 检查是否配置签名。

## 分析结论

* 依赖的共享包模块未安装。
* Deploy Multi Hap Packages配置错误。
* Auto Dependencies配置错误。
* 依赖的共享包模块未签名。

## 修改建议

1. [安装引用共享包](../harmonyos-guides/ide-har-import.md)参考官方文档。
2. 在运行配置页，选择[Deploy Multi Hap](../harmonyos-guides/ide-run-debug-configurations.md#section711735724014)标签页，勾选Deploy Multi Hap Packages，选择依赖的模块，点击OK保存配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Zox4qrW4RY-uuSm53sw0PQ/zh-cn_image_0000002628569172.png "点击放大")
3. 在运行配置页，选择General标签页中配置[Auto Dependencies](../harmonyos-guides/ide-run-debug-configurations.md#section18910152417412)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/EP2t7BItRlmU62CiE-JPlQ/zh-cn_image_0000002658928497.png "点击放大")
4. [配置签名](../harmonyos-guides/ide-signing.md#section18815157237)，DevEco Studio在打包时会对HSP模块重签名，只有重签名才会进行部署entry时自动部署HSP依赖。

## 总结

entry通过tgz的方式引用HSP模块（即远程仓的方式），需要配置2个选项：

1. 在运行配置页配置Auto Dependencies。
2. 项目配置签名。

配置后在真机上即可正常安装、调试。如果使用模拟器，需要注意安装模拟器PC的CPU架构。由于模拟器的限制，推荐使用真机运行。
