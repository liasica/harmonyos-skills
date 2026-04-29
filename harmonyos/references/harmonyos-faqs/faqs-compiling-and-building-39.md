---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39
title: 编译报错“Only one default card can be configured in the form_config.json file”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Only one default card can be configured in the form_config.json file”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:28a8e0e1a88cda6129ad5894db0e3617499ca242faf33087ca05223fcc318c8f
---

**问题现象**

DevEco Studio编译失败。提示：Only one default card can be configured in the form\_config.json file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/1vzkXB2mQt6-xdGk6WUN4w/zh-cn_image_0000002229758657.png?HW-CC-KV=V1&HW-CC-Date=20260429T062027Z&HW-CC-Expire=86400&HW-CC-Sign=ED2FC587BCD826B72629C0F02E07B32AD77EA686A26716F5FAC5E19D8034E436 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
