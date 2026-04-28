---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-42
title: 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:16+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c8c6c5d410e543c7f313424fe3c7d17c65a02969fb611085343cad58478a1f0d
---

**问题现象**

本地HSP模块对外提供的接口中使用了未在HAP中定义的自定义参数BuildProfileFields。HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/BZychf3jQLK6wKbC8-y0wA/zh-cn_image_0000002194158808.png?HW-CC-KV=V1&HW-CC-Date=20260428T002915Z&HW-CC-Expire=86400&HW-CC-Sign=C8B205527FD4FEE252EE413EAFCF5D222FE1E218AE84B271A5F0BA9D0742B6B2)

**解决措施**

采用以下两种方式解决该问题：

* 在HAP中配置与HSP相同的自定义参数BuildProfileFields。
* 将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中。这种方法会使HSP中的自定义参数在全局生效。
