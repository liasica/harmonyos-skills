---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161
title: 编译报错“Duplicate 'routerMap' object names detected.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Duplicate 'routerMap' object names detected.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2e9af17d31f1b9ec6b3c71b840c866d4e20e0b433d4dc0a652f44d4099bd1879
---

**错误描述**

routerMap配置中存在重复名称。

**可能原因**

当前模块的router\_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/iBj_5L0dSF23d5Vlml91jQ/zh-cn_image_0000002624478642.png)

**解决措施**

修改router\_map.json文件中的name字段，确保其值唯一。
