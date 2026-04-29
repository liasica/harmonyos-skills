---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28
title: ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
breadcrumb: FAQ > DevEco Studio > 编译构建 > ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:64611f51b993e9662005578b28d0dd21d9af7d3f879de989bd442a9e8c37c0fc
---

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/5cIkeIMPTMCg-K5DbTTDjA/zh-cn_image_0000002194158592.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=E8EC6FC3552C61AA55481D7FAD72AD0162B1480A12917775B1B1EF5F452A59C7)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/OseqEQwISpOpytqIUIrB6g/zh-cn_image_0000002229758465.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=493536DBA73E80CB3112FEDF01C87DE78FA06756954D2C4587999D55809DD71A)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1. 删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2. 在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。

   工程迁移后结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/80-b2tUMSr-SD0ZoggIPHA/zh-cn_image_0000002229758461.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=71AB781509B1601D99B32126DF0FC7B14EEAF775A6FE6EF68FFA9B1614104E3E)
3. 迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/1V026fz7RM-2ufjMXtos_Q/zh-cn_image_0000002229603993.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=90EE765ABE3FA03F11FF954F5AC203FF8450925C443DD6BF71466073DD22D886)
