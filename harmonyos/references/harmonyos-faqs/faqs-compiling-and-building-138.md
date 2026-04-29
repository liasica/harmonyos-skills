---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-138
title: 编译报错“The srcPath is not a relative path：xxx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The srcPath is not a relative path：xxx”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:94ec8d5b837d1e26d89cd0d7c6171c8c9d6215890c8b9a5320456c2033518687
---

**错误描述**

srcPath字段配置值必须为相对路径。

**可能原因**

开发者在hvigorconfig.ts文件中使用includeNode方法时，srcPath必须是相对路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/-BN12bSBS4yljLWIgttSmQ/zh-cn_image_0000002229604333.png?HW-CC-KV=V1&HW-CC-Date=20260429T062051Z&HW-CC-Expire=86400&HW-CC-Sign=45515137234EE06D73FC20083E7BEC688143B03CA3AD3574ED82894B8DE6CB1E)

**解决措施**

确保项目的hvigorconfig.ts文件中使用includeNode时的传参srcPath为相对路径。

**参考链接**

[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)
