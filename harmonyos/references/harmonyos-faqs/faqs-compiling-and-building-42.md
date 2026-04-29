---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-42
title: 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d8616b300e5df3e04f73030d9cb96155939b38d412db6964302a64741c73906b
---

**问题现象**

本地HSP模块对外提供的接口中使用了未在HAP中定义的自定义参数BuildProfileFields。HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/BZychf3jQLK6wKbC8-y0wA/zh-cn_image_0000002194158808.png?HW-CC-KV=V1&HW-CC-Date=20260429T062028Z&HW-CC-Expire=86400&HW-CC-Sign=F5D3CEBA09096F1F95ED24F57B0ACEFCFA9B9168385A7A76764FD38537484523)

**解决措施**

采用以下两种方式解决该问题：

* 在HAP中配置与HSP相同的自定义参数BuildProfileFields。
* 将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中。这种方法会使HSP中的自定义参数在全局生效。
