---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44
title: 编译时DevEco Studio提示Signing material error
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio提示Signing material error
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee1df948a8e48dedca41db1d71e8a6617b4157f204042e886885b1f87454a9f8
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WrD-SmF7TT-8_LuGNg8UAg/zh-cn_image_0000002229604197.png "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
