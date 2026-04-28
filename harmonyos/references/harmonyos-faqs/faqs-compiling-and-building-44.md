---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44
title: 编译时DevEco Studio提示Signing material error
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio提示Signing material error
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2911cdf5d6fd8a2a89414a26e5baf76b72b4c36a5037465a4dcde70875ef1857
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WrD-SmF7TT-8_LuGNg8UAg/zh-cn_image_0000002229604197.png?HW-CC-KV=V1&HW-CC-Date=20260428T002916Z&HW-CC-Expire=86400&HW-CC-Sign=2199763DC26954B010F1F81CC93A7193F58F9E1AF92C23D59B495B2DDDC3CDA0 "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
