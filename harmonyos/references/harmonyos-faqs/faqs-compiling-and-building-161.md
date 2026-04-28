---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161
title: 编译报错“Duplicate 'routerMap' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'routerMap' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:96290aa06b7e13207841f91579584b86420c6ea0bc372d5a67a85e02adb6ac03
---

**错误描述**

routerMap配置中存在重复名称。

**可能原因**

当前模块的router\_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/MzOAKxNZRz-SRgZphnlB2Q/zh-cn_image_0000002229603813.png?HW-CC-KV=V1&HW-CC-Date=20260428T002942Z&HW-CC-Expire=86400&HW-CC-Sign=5D572D693D76CC8E22086B6AAC1DAF5347E85FF38AE7749DF5B9AEDED6EFC557)

**解决措施**

修改router\_map.json文件中的name字段，确保其值唯一。
