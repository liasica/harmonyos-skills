---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144
title: 编译报错“There are some dependency names that are inconsistent with the actual package names”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“There are some dependency names that are inconsistent with the actual package names”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:525d4ffe1c69f474c401e5c40d7b893f150bfbbc90d2e7c77c3e40bcfe3f569f
---

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/PobLDKlkTzaxMtlgUZylWg/zh-cn_image_0000002229758445.png?HW-CC-KV=V1&HW-CC-Date=20260429T062053Z&HW-CC-Expire=86400&HW-CC-Sign=E44A6D7923782B5E46539A3946716958609BA5A103691AA9119279E1EC3BB0F3)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
