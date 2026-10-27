---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144
title: 编译报错“There are some dependency names that are inconsistent with the actual package names”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“There are some dependency names that are inconsistent with the actual package names”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b10ea4e6833a32546cc7fef1a88b6da8c7df2e64fcd3b7b22a0840cd0439cedd
---

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/6aTS5YrnQbKzTXR8SOnxqQ/zh-cn_image_0000002654797987.png)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
