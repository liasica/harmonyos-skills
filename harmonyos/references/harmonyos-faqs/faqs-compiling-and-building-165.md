---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-165
title: 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7181642946e332c519a77717d38a0b62f9e60150f1b40a968852f213f769400
---

**错误描述**

在FormExtensionAbility中，metadata必须包含一个对象，名称设置为“ohos.extension.form”，资源设置为二级资源引用。

**可能原因**

module.json5中type为form的ExtensionAbility中的metadata缺少name为ohos.extension.form的对象值，或者缺少resource字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/-mOvw_i9Qcq6_uwvsfSlWw/zh-cn_image_0000002229758517.png?HW-CC-KV=V1&HW-CC-Date=20260429T062059Z&HW-CC-Expire=86400&HW-CC-Sign=784E1F81B2A3A352AF7E3D7558AABAB813FBDF602C49BD0272EDA4B4E6521337)

**解决措施**

在module.json5中type为form的ExtensionAbility中增加metadata字段，补充一个name为“ohos.extension.form”的对象值，并配置对应的resource值，具体配置方式参考[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。
