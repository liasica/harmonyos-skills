---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20
title: 多Module应用通过startAbility()启动时报错
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多Module应用通过startAbility()启动时报错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:47+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4f9e3a419a4f626934e8701f595049fe8d4e96fc0f2358803e0d81eafceb9f25
---

**原因**

在同一个工程和设备中存在多个模块，并且这些模块之间存在调用关系，但并非所有HAP包都已安装到设备中。

**解决措施**

单击Run > Edit Configurations，在Deploy Multi Hap/Hsp中，勾选Deploy Multi Hap/Hsp Packaqes，选择多个模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/FchVbTv7TP-aljJWcKjFMA/zh-cn_image_0000002654795245.png "点击放大")

**参考链接**

[设置HAP安装方式](../harmonyos-guides/ide-run-debug-configurations.md#section531811771410)

[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)
