---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162
title: 编译报错“Failed to obtain the module type.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to obtain the module type.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:40b5b6b0a5267874b1da07aaa0af3e23a8ec389a8758726894b50fb2834e119c
---

**错误描述**

未找到指定的模块类型。

**可能原因**

在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zd7I9Wb-QzyfDrQSSXIhLw/zh-cn_image_0000002229604177.png?HW-CC-KV=V1&HW-CC-Date=20260428T002942Z&HW-CC-Expire=86400&HW-CC-Sign=880698ADECDD5B049EC892F900FD6797DC55B5D816BC0E524F45066677DFB854)

**解决措施**

确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
