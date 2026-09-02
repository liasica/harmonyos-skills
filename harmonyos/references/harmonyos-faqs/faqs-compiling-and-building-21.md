---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-21
title: 编译报错“Failed to generate test project build system”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to generate test project build system”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5cc6d11c364e2543b7474fbbf92598b13decd22b7ca5aa7d6608ced1d9f21b1b
---

**问题现象**

执行多模块Native模块构建时，出现“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/8oAmR2BOSsKGY2Abi4i8wQ/zh-cn_image_0000002194158584.png)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行Make Module {moduleName}完成单独构建。注意：此方案需避免多模块并行构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/GXgnlimyTeCX_ekvB_19RA/zh-cn_image_0000002229758457.png)
