---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1
title: 编译报错“JS heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“JS heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:63031c14b9f38a1b3f2ab12cd2febc955d3782c675dd757d25d7abffaabdaf0f
---

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/IjcCn1x0SFGeo80EmjER2w/zh-cn_image_0000002794888789.png "点击放大")

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用DevEco Studio 5.0.0 Release及以上版本时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/55CgEjOBTIKuwR4wmTy6qw/zh-cn_image_0000002795009023.png "点击放大")

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
