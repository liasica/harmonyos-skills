---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-165
title: 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e119486d30ce6c03af5a5c3cac14f40607ecac71869506cd69ee9513febb350d
---

**错误描述**

在FormExtensionAbility中，metadata必须包含一个对象，名称设置为“ohos.extension.form”，资源设置为二级资源引用。

**可能原因**

module.json5中type为form的ExtensionAbility中的metadata缺少name为ohos.extension.form的对象值，或者缺少resource字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/-mOvw_i9Qcq6_uwvsfSlWw/zh-cn_image_0000002229758517.png?HW-CC-KV=V1&HW-CC-Date=20260428T002943Z&HW-CC-Expire=86400&HW-CC-Sign=F472EBAE7C8C42B9FCFF84B45AB56515AD3AAF9FED1C8C310129E998FBD770DD)

**解决措施**

在module.json5中type为form的ExtensionAbility中增加metadata字段，补充一个name为“ohos.extension.form”的对象值，并配置对应的resource值，具体配置方式参考[配置ArkTS卡片的配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md)。
