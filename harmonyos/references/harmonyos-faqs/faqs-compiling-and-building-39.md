---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39
title: 编译报错“Only one default card can be configured in the form_config.json file”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Only one default card can be configured in the form_config.json file”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ca630ebf8c25b205d080ca5e60b2652700de5537e1386b70547b3b6d384b93d9
---

**问题现象**

DevEco Studio编译失败。提示：Only one default card can be configured in the form\_config.json file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/_zs_86DARXyHFUI03I5crA/zh-cn_image_0000002624638410.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
