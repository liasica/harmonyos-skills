---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-153
title: 编译报错“This project is in the FA model and does not allow for external dependencies.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“This project is in the FA model and does not allow for external dependencies.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0d72c88fee67f42b83b93f31ed7539acde5215471c5ce0e252dca35178fffc8c
---

**错误描述**

FA模型项目不得依赖外部项目模块。

**可能原因**

在FA模型项目中，build-profile.json5文件的srcPath字段引用了外部项目模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/bH6FJ2t8RPqkglJPNXdJZw/zh-cn_image_0000002654837947.png)

**解决措施**

在项目根目录的build-profile.json5文件中，移除srcPath字段依赖的外部项目模块。
