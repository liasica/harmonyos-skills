---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127
title: 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d80b1f57c2cff3271515915371672f234b14d87de1515e5e037c9f96f5cafdac
---

**问题现象**

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/rOKrcbkqRG6iGtlPAWP2lw/zh-cn_image_0000002229604153.png?HW-CC-KV=V1&HW-CC-Date=20260428T002933Z&HW-CC-Expire=86400&HW-CC-Sign=9EB0E90E8B0780100ED9256DEE922BE7A27AB8202F2CF94F734FCF2FF1FA1A43)

**解决方案**

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。
