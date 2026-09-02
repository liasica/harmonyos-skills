---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162
title: 编译报错“Failed to obtain the module type.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Failed to obtain the module type.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c6d08db2c0ee8e42ec7dbfed3e4dcc18ae5f47f9519ffcf4158eb00a94841f7b
---

**错误描述**

未找到指定的模块类型。

**可能原因**

在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/xZrWUTH-QzOZCbSmXs_hww/zh-cn_image_0000002654798001.png)

**解决措施**

确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
