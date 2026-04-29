---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167
title: 编译报错“Duplicate 'Module-Abilities' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'Module-Abilities' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37f492b6068ac87d97a12caa41e6411a65b926b92cdb0f2cdd5f21809d44b389
---

**错误描述**

Module-Abilities对象名称重复。

**可能原因**

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/257vx7CoQYa18-Fl5sUrPA/zh-cn_image_0000002194158504.png?HW-CC-KV=V1&HW-CC-Date=20260429T062059Z&HW-CC-Expire=86400&HW-CC-Sign=5AD17BC595B92CB4810FB7538B91678DC09D9A7118DD144ACBAE1E382C95085C)

**解决措施**

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。
