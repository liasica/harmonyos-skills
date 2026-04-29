---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162
title: 编译报错“Failed to obtain the module type.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to obtain the module type.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:00d69fc67b9a44a60c09ac07e26c66d12e82c1a73cb6d7f35faf448a08314924
---

**错误描述**

未找到指定的模块类型。

**可能原因**

在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zd7I9Wb-QzyfDrQSSXIhLw/zh-cn_image_0000002229604177.png?HW-CC-KV=V1&HW-CC-Date=20260429T062058Z&HW-CC-Expire=86400&HW-CC-Sign=CE665FF19163D605AAA68A25E6F528D7D3306BA43071D47E16CE2E5C482BB8B5)

**解决措施**

确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
