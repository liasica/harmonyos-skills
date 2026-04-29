---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-153
title: 编译报错“This project is in the FA model and does not allow for external dependencies.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“This project is in the FA model and does not allow for external dependencies.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7ff08e3f4c60a0eba2a76c795880f03da1105bb656627d72547f5874197b2b80
---

**错误描述**

FA模型项目不得依赖外部项目模块。

**可能原因**

在FA模型项目中，build-profile.json5文件的srcPath字段引用了外部项目模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/yBgu2VlLSaKH8eewo0jmyw/zh-cn_image_0000002194318412.png?HW-CC-KV=V1&HW-CC-Date=20260429T062056Z&HW-CC-Expire=86400&HW-CC-Sign=2EBA8ABDA9748215DA2E8B0BD4F511DE25F2F3EC0DBCAF227686635A29718519)

**解决措施**

在项目根目录的build-profile.json5文件中，移除srcPath字段依赖的外部项目模块。
