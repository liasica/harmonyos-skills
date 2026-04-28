---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167
title: 编译报错“Duplicate 'Module-Abilities' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'Module-Abilities' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dc48258917bc421d41e4968a067a7581ee2c4c400786128467e6211db7e62e98
---

**错误描述**

Module-Abilities对象名称重复。

**可能原因**

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/257vx7CoQYa18-Fl5sUrPA/zh-cn_image_0000002194158504.png?HW-CC-KV=V1&HW-CC-Date=20260428T002944Z&HW-CC-Expire=86400&HW-CC-Sign=1BB6AE70EF0673DC0953ECDDB6E50ADFB2C968A90419B5672D015427B10DCB26)

**解决措施**

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。
