---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-129
title: 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:94f994bd23369d371bb129dd17401d4a67ee5535cf7cfd6e53bb2f42888f5d14
---

**问题现象**

编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”。常见于图片中两种错误同时出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/iuN-v8b9QyebK2JVicuq6g/zh-cn_image_0000002624638516.png "点击放大")

**问题****原因**

大小写敏感导致模块无法找到。

**解决方案**

解决引用中的大小写问题。
