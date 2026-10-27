---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-164
title: 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:f7b4153317f143996ae46291bd289e523dc945f80411aceaf135524b04467ee3
---

**错误描述**

FormExtensionAbility中的metadata字段必须非空且不为数组。

**可能原因**

在module.json5文件中，当ExtensionAbility的type为form时，metadata字段可以是空对象或空数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/04l_4732RXyXNmWfK868UQ/zh-cn_image_0000002654837959.png)

**解决措施**

在module.json5中type为form的ExtensionAbility中配置metadata字段，具体配置方式参考[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。
