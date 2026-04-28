---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-129
title: 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:34+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:212fabd6deec05724049529fa95bb2d9c8ab840f74be887eb6d91f623ca4d97d
---

**问题现象**

编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”。常见于图片中两种错误同时出现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/uTLoXJWeQsiE-lPCoW3sZA/zh-cn_image_0000002581587131.png?HW-CC-KV=V1&HW-CC-Date=20260428T002933Z&HW-CC-Expire=86400&HW-CC-Sign=EE269EA57051D9E78C1106F0DBD6F687D003FE2EFC4FAB730BAF0B3ED679653E "点击放大")

**问题****原因**

大小写敏感导致模块无法找到。

**解决方案**

解决引用中的大小写问题。
