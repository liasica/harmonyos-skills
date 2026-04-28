---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-34
title: 执行sync过程中修改Hvigor及plugin版本导致build init
breadcrumb: FAQ > DevEco Studio > 编译构建 > 执行sync过程中修改Hvigor及plugin版本导致build init
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1309c12cce98814781d2dc1d11f50b93767d842ca0ec24c91e2a76c5d0e0f2ec
---

**问题现象**

在配置Hvigor和hvigor-ohos-plugin的版本号后，点击Sync。如果之后再次修改了版本号，会导致重复下载引发版本冲突，表现为build init报错及日志刷屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/aj3lPDNER_abIxKLdqLeyQ/zh-cn_image_0000002194158832.png?HW-CC-KV=V1&HW-CC-Date=20260428T002913Z&HW-CC-Expire=86400&HW-CC-Sign=F40A9EF6458C392DC4D9EDA15560D0C0C6A8FB38FD927BB87A350B1657D6D8E3)

**解决措施**

该问题源于在执行build init下载Hvigor时修改了Hvigor版本。随后在执行Hvigor.js时，由于依赖发生变化，导致第二次下载新版本，从而引发不兼容问题。建议在执行 Sync 并下载Hvigor时不要修改Hvigor版本。

点击**File > Sync and Refresh Project**，重新执行Sync。
