---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44
title: 编译时DevEco Studio提示Signing material error
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio提示Signing material error
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7d5cf6f2870e16f729edb4fb7ded6b9f07a428dd5480de5d38af03fc11e9c42f
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WrD-SmF7TT-8_LuGNg8UAg/zh-cn_image_0000002229604197.png?HW-CC-KV=V1&HW-CC-Date=20260429T062029Z&HW-CC-Expire=86400&HW-CC-Sign=E26428C3F547062965085670551C808478CA6CD8944748982538CCAE52266421 "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
