---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127
title: 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:126a0bfb4b6a3d928bae9f3bc53e9c408d887d8f39a772485f132f40509290aa
---

**问题现象**

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/MiOj5QiZSq6ELhR5PL3vwQ/zh-cn_image_0000002624478606.png)

**解决方案**

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。
