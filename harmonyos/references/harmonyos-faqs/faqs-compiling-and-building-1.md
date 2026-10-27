---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1
title: 编译报错“JS heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“JS heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:be3092c6823ba96ae39b34cbbce164cb3601e40be8ee0e476d852db17b7ab18b
---

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/yIl9Hi1LRa6LVoyj0kJJXQ/zh-cn_image_0000002794888789.png "点击放大")

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用DevEco Studio 5.0.0 Release及以上版本时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/QaG8gp3yTf20nByUbgI02w/zh-cn_image_0000002795009023.png "点击放大")

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
