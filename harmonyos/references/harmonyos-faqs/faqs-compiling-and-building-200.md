---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-200
title: 编译构建项目无法排除某些目录打包怎么处理
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建项目无法排除某些目录打包怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b250a21981c5a68c0aa6c1f35b1361a2f4828a9782843f914f1967cfb11e62c1
---

## 问题现象

当开启release编译构建，开启从入口文件开始编译，构建闭源HAR时，编译构建指定模块时无法排除该模块中的某些文件。项目结构示例如下，按照以下3项步骤，工程中的test模块中/src/main/ets/com/test/test.ts应该不会被打包进test.har包，但是实际test.ts文件仍然还是会被打包。

1. 首先启用release编译构建；
2. hvigor-config.json5中ohos.compile.lib.entryfile为true，开启从入口文件开始编译；
3. 模块下的build-profile.json5中buildOptionSet.arkOptions.obfuscation.ruleOptions.enable为true，构建闭源HAR。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/ZFLFMaHITu6nyThziuF6NA/zh-cn_image_0000002628409278.png "点击放大")

## 解决方案

当编译构建需要排除某些目录或文件时，需要配置.ohpmignore文件，并且还要明确该目录或文件是否被引用。

**1. 配置.ohpmignore文件：**

若部分工程源文件无需构建到HAR包中，可在module目录下新建.ohpmignore文件，用于配置打包时要忽略的文件，将无需打包进HAR包的文件/文件夹名称写入.ohpmignore文件中。DevEco Studio构建时将过滤掉.ohpmignore文件中所包含的文件目录。

需注意：更改.ohpmignore配置后，需要清空相应模块的build文件夹，或点击DevEco Studio的Build -> clean project后再打包。

**2. 编译构建：**

当开启release编译构建，开启从入口文件开始编译，构建闭源HAR时，存在引用和不引用test.ts两种情况：

a. 如果test文件被其他地方引用了，test.har编译结果如下，发现包含test文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/mOzC_MRdQN2pH6UlsmTk_g/zh-cn_image_0000002658808549.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/B_WB8wY8QNe14IjdEQGevA/zh-cn_image_0000002628569174.png "点击放大")

b. 如果test文件没有被引用，test.har编译结果如下，此时不包含test文件：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/m8fzUitBSbeGxLukNUdjmQ/zh-cn_image_0000002658928499.png "点击放大")

## 总结

当开启release编译构建，开启从入口文件开始编译，构建闭源HAR时，.ohpmignore文件中配置的文件或目录如果被其他地方引用了，则会被打包，如果未被引用，则不会被打包。
