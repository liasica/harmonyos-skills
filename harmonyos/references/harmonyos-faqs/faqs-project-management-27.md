---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-27
title: 使用发布证书打release包未成功的解决方案
breadcrumb: FAQ > DevEco Studio > 工程管理 > 使用发布证书打release包未成功的解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e1142139031bf783c9fb80302530d0fbae718663df7e9053fcaf68e6e48771f3
---

## 问题现象

使用发布的证书、profile文件进行打包，build mode选择release，但是打出来的是debug包。

## 背景知识

* 完成HarmonyOS应用开发、调试与测试后，开发者便可以在AGC正式提交应用上架申请。[发布应用](../app/agc-help-releaseharmony-0000001933963166.md)涉及申请发布证书、申请发布profile和正式发布HarmonyOS应用三大步骤。
* build-profile.json5文件中的[buildOption](../harmonyos-guides/ide-hvigor-build-profile-app.md#section14222051575)字段是构建使用的具体配置信息,其中的debuggable字段用于配置当前编译产物是否为可调试模式，如果未配置时使用release的编译模式时默认值为false，使用其他编译模式时默认值为true。app.json5文件中的[debug标签](../harmonyos-guides/app-configuration-file.md#配置文件标签)用于标识应用是否可调试。该标签可缺省，缺省值为false。

## 问题定位

1. 排查工程级的build-profile.json5文件products字段下的buildOption字段的debuggable字段。
2. 排查模块级的build-profile.json5文件buildOption字段的debuggable字段。
3. 排查app.json5文件中的debug字段。
4. 排查是否缓存导致。

## 分析结论

问题根源在于多个配置文件中的debuggable字段或debug字段未被正确设置。这些字段决定了构建模式（即debug模式或release模式）。在某些情况下，即使选择了release模式，如果这些字段仍然设置为true，系统仍然会将应用打包为debug包。

## 修改建议

可以按照以下的步骤进行修改：

1. 修改工程级的build-profile.json5文件products字段下的buildOption字段的debuggable字段为false，或直接把该字段删除。
2. 修改模块级的build-profile.json5文件buildOption字段的debuggable字段为false，或直接把该字段删除。
3. 修改app.json5文件中的debug字段为false，或直接把该字段删除。
4. 清除构建缓存（删除.hvigor文件、IDE中Build -> Clean Project）。
5. 清除IDE缓存（File -> Invalidate Caches... ）。

## 常见FAQ

Q：上架时报错：当前软件包存在有调试信息，不允许上架发布（请删除软件包中module.json文件中包含debug:true字段后重新上传）。

A：通过DevEco Studio界面配置Build Mode选项，点击右上角运行/调试配置旁的圆点图标选择构建模式，检查Build Mode是否设置为release模式，若非release模式请尝试选择release模式后重新编译生成app包。因为Build Mode默认情况下为<Default>选项，选择此项，构建APP包使用release构建模式；构建HAP/HSP/HAR包使用debug构建模式，当应用中存在HAR模块依赖时会导致出现此问题现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/kw225O-eQsCeaebndC-bfw/zh-cn_image_0000002628408060.png "点击放大")
