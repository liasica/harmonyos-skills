---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-220
title: 如何解决编译构建时间过长问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译构建时间过长问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af9392a75dac8b07d6025e68df56e29a824f762f6fa5a7e17ac94ed147cb742d
---

## 问题现象

应用的代码涉及多个common模块和feature模块，clean之后，编译构建需要耗时半小时左右，编译构建时间过长。

场景示例：HAP+20个HSP混合打包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/GGSAIjJxSuy11tqAfNnyfQ/zh-cn_image_0000002658808635.png "点击放大")

## 背景知识

[HSP](../harmonyos-guides/in-app-hsp.md)（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布，而是跟随宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。

[HAR](../harmonyos-guides/har-package.md)（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。

## 问题定位

分析代码，发现应用使用了过多的HSP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/pMJQNaH5TS2rIRg4A2x8vg/zh-cn_image_0000002628569270.png "点击放大")

## 分析结论

应用使用了大量的HSP，在编译构建过程中，应用会将依赖的HSP都安装一遍，会增加编译构建的耗时。

## 修改建议

建议将当前系统架构中大量使用的HSP升级改造为HAR，可有效提升内存收益和性能收益。对于单窗口应用的APP工程而言，其仅包含一个Entry类型的HAP，那么划分的模块如果没有按需加载的需求，则建议业务组件和公共组件采用HAR的打包方式，最终构建应用HAP包时，这些被依赖的HAR，最终都会被编译进HAP包中。

设计成HAR包有如下好处：

1. 全部编译进HAP，无额外的HSP，节省HSP的安装和加载成本。
2. HAR在编译进HAP时，可以利用ArkTS的语言特性和编译器功能，做类型推断和编译优化。

## 常见FAQ

Q：HarmonyOS编译构建时如何指定编译架构信息？

A：HarmonyOS通过–target来设置架构。--target aarch64-linux-ohos和--target arm-linux-ohos分别对应64位和32位的架构。

Q：如何查看编译的详细过程？

A：在hvigor->hvigor-config.json5中"logging": { //"level": "info" }的注释取消，改为debug，改完后的结果为"logging": { "level": "debug" }，在编译时就可以看到编译的详细过程。
