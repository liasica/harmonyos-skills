---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127
title: 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8c6cf4320f0839b0295f39bc49af2ea6052b5ec1e6b62695c6bd6fbb83e9e988
---

**问题现象**

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/rOKrcbkqRG6iGtlPAWP2lw/zh-cn_image_0000002229604153.png?HW-CC-KV=V1&HW-CC-Date=20260429T062048Z&HW-CC-Expire=86400&HW-CC-Sign=4D01186C8F22A4F4AEBAB5F8DB1FB503D5B87ADD7DAE6DC9CBA65E60CE33A306)

**解决方案**

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。
