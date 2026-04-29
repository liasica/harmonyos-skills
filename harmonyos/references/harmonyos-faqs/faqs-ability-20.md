---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20
title: 多Module应用通过startAbility()启动时报错
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 多Module应用通过startAbility()启动时报错
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:79aaf9114b532934f1f8bab13f4f0bb7e396949e8fbb159c0a2ca4af6a6ce2e9
---

**原因**

在同一个工程和设备中存在多个模块，并且这些模块之间存在调用关系，但并非所有HAP包都已安装到设备中。

**解决措施**

单击Run > Edit Configurations，设置指定模块的HAP安装方式，勾选“Keep Application Data”，表示采用覆盖安装方式，保留应用和服务的缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/k_2dzaRfSfyreUHTJ1GYLw/zh-cn_image_0000002194318612.png?HW-CC-KV=V1&HW-CC-Date=20260429T061458Z&HW-CC-Expire=86400&HW-CC-Sign=195985B5AB378CE7E7AC3659F8A73DAC3700338CA0F8D4C9E4951D7A025611D7 "点击放大")

**参考链接**

[设置HAP安装方式](../harmonyos-guides/ide-run-debug-configurations.md#section531811771410)

[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)
