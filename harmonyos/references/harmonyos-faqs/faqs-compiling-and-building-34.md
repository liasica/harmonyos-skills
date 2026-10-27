---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-34
title: 执行sync过程中修改Hvigor及plugin版本导致build init
breadcrumb: FAQ > DevEco Studio > 编译构建 > 执行sync过程中修改Hvigor及plugin版本导致build init
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:14617f8cfc7598fc64bfd6293523ed90fb34e959372b1624254c6dbd86618d19
---

**问题现象**

在配置Hvigor和hvigor-ohos-plugin的版本号后，点击Sync。如果之后再次修改了版本号，会导致重复下载引发版本冲突，表现为build init报错及日志刷屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/-_HU1iH4QXesz9121-2kSQ/zh-cn_image_0000002654797863.png)

**解决措施**

该问题源于在执行build init下载Hvigor时修改了Hvigor版本。随后在执行Hvigor.js时，由于依赖发生变化，导致第二次下载新版本，从而引发不兼容问题。建议在执行 Sync 并下载Hvigor时不要修改Hvigor版本。

点击**File > Sync and Refresh Project**，重新执行Sync。
