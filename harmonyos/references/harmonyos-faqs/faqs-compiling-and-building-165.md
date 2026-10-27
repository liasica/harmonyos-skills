---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-165
title: 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e0872fa43b2c550289e275303782451ac0f973cfeb7fd7276335f1cb5cd438d1
---

**错误描述**

在FormExtensionAbility中，metadata必须包含一个对象，名称设置为“ohos.extension.form”，资源设置为二级资源引用。

**可能原因**

module.json5中type为form的ExtensionAbility中的metadata缺少name为ohos.extension.form的对象值，或者缺少resource字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/VWj7kBz2RF6UPh8ZixY2Bg/zh-cn_image_0000002624478648.png)

**解决措施**

在module.json5中type为form的ExtensionAbility中增加metadata字段，补充一个name为“ohos.extension.form”的对象值，并配置对应的resource值，具体配置方式参考[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。
