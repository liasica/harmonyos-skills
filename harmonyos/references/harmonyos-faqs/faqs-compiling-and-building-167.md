---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167
title: 编译报错“Duplicate 'Module-Abilities' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'Module-Abilities' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2060dd864d370034cbcad855295e7a2da867bf901eb4a2903d96bc41d2de5903
---

**错误描述**

Module-Abilities对象名称重复。

**可能原因**

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/nfyP39WrT7WjT53LPAxyHg/zh-cn_image_0000002654837963.png)

**解决措施**

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。
