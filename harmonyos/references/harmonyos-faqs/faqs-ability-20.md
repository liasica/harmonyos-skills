---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20
title: 多Module应用通过startAbility()启动时报错
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多Module应用通过startAbility()启动时报错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:372c2b77489ce10176a972477c8bd54778c2278a14e5467b6b74797be879ae67
---

**原因**

在同一个工程和设备中存在多个模块，并且这些模块之间存在调用关系，但并非所有HAP包都已安装到设备中。

**解决措施**

单击Run > Edit Configurations，设置指定模块的HAP安装方式，勾选“Keep Application Data”，表示采用覆盖安装方式，保留应用和服务的缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/k_2dzaRfSfyreUHTJ1GYLw/zh-cn_image_0000002194318612.png?HW-CC-KV=V1&HW-CC-Date=20260428T002341Z&HW-CC-Expire=86400&HW-CC-Sign=B5F9779852D8390AEBE4E7D42FB6E29D90E4F7E0F917C3BD5C2D09198C2F005B "点击放大")

**参考链接**

[设置HAP安装方式](../harmonyos-guides/ide-run-debug-configurations.md#section531811771410)

[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)
