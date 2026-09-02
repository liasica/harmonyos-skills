---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-79
title: HarmonyOS按需加载实现方法和常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS按需加载实现方法和常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:1200e77603cbf08937e93ffd08dd6848be38842eca39b16f4eb1f4078872fb61
---

## 问题现象

如何通过按需加载能力减少首次安装时耗时和应用的占用空间？

## 背景知识

按需加载模块：用户首次从应用市场安装时，只会下载不包含按需加载模块的内容。当用户需要使用特定功能时，可以选择下载并安装相应的功能模块。

按需加载模块有以下好处：

* 减少包体积：用户从应用市场首次下载的应用不包含按需加载模块，用户看到的包体积减少，从而减少了用户下载和安装时间，减少了用户等待时间。
* 减少系统资源：应用安装之后所占用的空间也变少（节省ROM空间），应用启动时加载的特性少了（节省了RAM空间）。
* 架构演进：定义为按需加载的特性明确，模块间耦合关系清晰，有利于应用架构演进。

## 解决方案

按需加载实现可分为三个步骤：基础包与扩展功能包分包、按需加载下载安装扩展功能包、运行扩展功能包。

**步骤一：基础包与扩展功能包分包。**

如果某个特性做成了按需加载模块，该模块可以设计为Feature类型的HAP或者HSP，HAP和HSP都可以实现按需加载，区别在于Feature类型的HAP可以包含UIAbility组件。

参考[应用程序包开发与使用](../harmonyos-guides/application-package-dev.md)，将APP分为基础功能Entry包和按需加载的动态模块（Feature类型的HAP或者HSP）。

在动态模块的module.json5中设置deliveryWithInstall为false，来标识当前模块在用户主动安装应用的时候不会一起下载安装。

当动态模块为HSP时，基础功能Entry包的oh-package.json5中需要[添加依赖项](../harmonyos-guides/ide-hvigor-dependencies.md)。添加HSP模块的动态依赖方式可参考[如何配置oh-package.json5动态依赖](faqs-compiling-and-building-48.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/yyycaZz8TUGAdRDZ53Oh6w/zh-cn_image_0000002648285864.png "点击放大")

**步骤二：按需加载下载安装扩展功能包。**

调用[moduleInstallManager (产品特性按需分发)](../harmonyos-references/store-moduleinstallmanager.md)实现动态模块的按需加载，可分为以下几步：

1. 使用[getInstalledModule](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagergetinstalledmodule)查询module是否安装。
2. 通过[createModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallprovidercreatemoduleinstallrequest)创建按需加载请求对象。
3. [fetchModules](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagerfetchmodules)按需加载请求下载module功能包。

**步骤三：运行扩展功能包。**

* 对于动态模块为Feature类型的HAP，可以通过UIAbility中的[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法拉起动态模块HAP包中的页面。
* 当动态模块为HSP时，可通过基础功能Entry包HAP[动态import](../harmonyos-guides/arkts-dynamic-import.md) HSP模块名或动态import HSP模块名文件路径的方式调用HSP中的方法或组件。

  **说明** 

  完整按需加载动态HSP可参考：[产品特性按需分发(ArkTS)](../harmonyos-guides/store-moduleinstall_arkts.md)。

## 常见FAQ

Q：按需加载[接入调试功能](../harmonyos-guides/store-moduleinstall_arkts.md#接入调试功能)，如何在沙箱中导入动态模块。

A：Device File Browser可访问的文件夹有五种类型：[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)、一般暂存区目录、日志目录、设备公共目录、媒体库目录。

1. 按下图点击切换Device File Browser沙箱视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/egLRsLs-ReqJha5La9QuqA/zh-cn_image_0000002648286216.png)
2. 在//data/app/el2/base/cache/moduleinstall/下添加对应的动态模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/KEEm5R56SMejvYlaPi3ODw/zh-cn_image_0000002648126326.png "点击放大")

Q：应用未上架如何测试按需加载功能？

A：推荐使用[邀请测试](../app/agc-help-invite-test-0000002270829393.md)。

Q：预装场景下，如果deliveryWithInstall配置为true，代码中是否不能引入@kit.AppGalleryKit？

A：没有这个限制。预装场景下系统会识别需要安装的文件，按需加载特性可以正常使用。
