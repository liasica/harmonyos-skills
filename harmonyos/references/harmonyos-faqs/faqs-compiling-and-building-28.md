---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28
title: ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a0b16cc36a45be29762038e81afcae33bfe2c7d5cbad4c9bdd1875f56996aef0
---

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/WUjWJXn-R_2-H9KLIuXhcQ/zh-cn_image_0000002654837807.png)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/qUBhvCQMSRuGlCJD2y6OZQ/zh-cn_image_0000002624478496.png)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1. 删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2. 在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。

   工程迁移后结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/SnaUOC36Q_2O0WzdGO7XXw/zh-cn_image_0000002654797855.png)
3. 迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/nsYPy1u4RNeABtBhqktaUg/zh-cn_image_0000002624638400.png)
