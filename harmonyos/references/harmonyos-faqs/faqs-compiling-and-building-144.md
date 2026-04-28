---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144
title: 编译报错“There are some dependency names that are inconsistent with the actual package names”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“There are some dependency names that are inconsistent with the actual package names”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:47107f76cbbd8cdadf75336f14520b143f8965cd595f201be86c3df7aa336d70
---

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/PobLDKlkTzaxMtlgUZylWg/zh-cn_image_0000002229758445.png?HW-CC-KV=V1&HW-CC-Date=20260428T002938Z&HW-CC-Expire=86400&HW-CC-Sign=3C2A8D68A3C50BF10954FD8D0B7813EC0553E889724A7096FE51F25A23CF2E3E)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
