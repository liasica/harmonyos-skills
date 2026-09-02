---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39
title: 编译报错“Only one default card can be configured in the form_config.json file”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Only one default card can be configured in the form_config.json file”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:18b1c8d31cb774dfaeccf7770ff7d65d5e2d13bf8972251f1111be538317ef41
---

**问题现象**

DevEco Studio编译失败。提示：Only one default card can be configured in the form\_config.json file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_j8fUP4cTZ6CvvGL3Ritdw/zh-cn_image_0000002624638410.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
