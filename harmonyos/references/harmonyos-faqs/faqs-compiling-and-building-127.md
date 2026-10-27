---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127
title: 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7d8ee700412980536d15d292a10a9776031fdaa2a4a8a5f8497ddfda6cf99762
---

**问题现象**

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/G9m5Oq25QFG_fyEkX1Rsfw/zh-cn_image_0000002624478606.png)

**解决方案**

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。
