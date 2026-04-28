---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28
title: ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a255995fd2c29efbdfa5c1936e309f26ff010a53ab803a22ff0fc59947966474
---

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/5cIkeIMPTMCg-K5DbTTDjA/zh-cn_image_0000002194158592.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=74B0EC79CA2C14C2966C9C90E4F3C114CAEB568F08F9FA62DA4892DC757A4156)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/OseqEQwISpOpytqIUIrB6g/zh-cn_image_0000002229758465.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=4CFFB59AA57EEB754EE4B673E961646990BDE917099E621FE63EB5BF8905D1F1)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1. 删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2. 在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。

   工程迁移后结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/80-b2tUMSr-SD0ZoggIPHA/zh-cn_image_0000002229758461.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=505B1AF0A08A2755CE0DF47F050A9692F336540AAE4BCEF76A52299132F4691E)
3. 迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/1V026fz7RM-2ufjMXtos_Q/zh-cn_image_0000002229603993.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=5E3052304929C258DB3FFA9664098A771F0430B1FCBD95C81CB46865006CF937)
