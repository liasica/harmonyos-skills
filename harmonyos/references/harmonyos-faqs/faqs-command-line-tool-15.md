---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-15
title: 如何重命名本地引用库
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何重命名本地引用库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:660e4977d6c32908267555309da1bdb69a50388b7cb8358b537af02b7715eaf7
---

## 问题现象

DevEco Studio升级到最新的release版本以后，添加本地的依赖重命名报错，有没有对本地引用库进行重命名的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/bPUbAiBZTOSIicMSVQkgIw/zh-cn_image_0000002658928871.png "点击放大")

## 背景知识

升级到DevEco Studio Beta1（5.0.3.800）及以上版本，新建工程的工程级build-profile.json5里[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)下的useNormalizedOHMUrl字段默认为true，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致。

## 解决方案

对本地引用库进行重命名，需确保oh-package.json5中依赖的包使用的别名和依赖包的oh-package.json5的name保持一致，否则编译会报错，具体的适配指导请参考[变更说明](../harmonyos-releases/ide-changelog-500-release.md#section1130320228353)。

错误示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/oDkR_veXSu6ZvAyAERW3oA/zh-cn_image_0000002628409656.png "点击放大")

图左框选内容为oh-package.json5中依赖的包使用的别名，图右框选内容为依赖包的oh-package.json5的name，两者不一致会有报错，若涉及重命名，需同步修改两处并保持名称一致。

正确示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/j5Lt6nKHR_27DznWGuUarA/zh-cn_image_0000002658808919.png "点击放大")

对本地引用库进行重命名时，同步修改oh-package.json5中依赖的包使用的别名和依赖包的oh-package.json5的name，使其保持一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/R4OD6SopRme1ZSAsWYX4bA/zh-cn_image_0000002628569548.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/AqowVVOsRl6_NZykXXFGDg/zh-cn_image_0000002658928873.png "点击放大")

在相关引用处，将导入的库名调整为重命名后的名称。
