---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144
title: 编译报错“There are some dependency names that are inconsistent with the actual package names”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“There are some dependency names that are inconsistent with the actual package names”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:12740f37f91541c0ea76b7ed85f4ca1e4d12fda99ba9c09483e7fdcca3d2c021
---

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/PobLDKlkTzaxMtlgUZylWg/zh-cn_image_0000002229758445.png)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
