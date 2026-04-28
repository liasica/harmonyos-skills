---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-164
title: 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7faed3effa6dab67e6d2d9efa19c47de15f2700d70cdfbf1e75fa4e32faa887
---

**错误描述**

FormExtensionAbility中的metadata字段必须非空且不为数组。

**可能原因**

在module.json5文件中，当ExtensionAbility的type为form时，metadata字段可以是空对象或空数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/OV0yZy3zT_anAeSGC6c25A/zh-cn_image_0000002194158712.png?HW-CC-KV=V1&HW-CC-Date=20260428T002943Z&HW-CC-Expire=86400&HW-CC-Sign=A9E7CFFB7ECF4341289CB6B213EA7757399581F2611BD56D454BDBC8AABCB8A1)

**解决措施**

在module.json5中type为form的ExtensionAbility中配置metadata字段，具体配置方式参考[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。
