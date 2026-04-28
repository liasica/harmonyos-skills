---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-40
title: 编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ae1fcb56ffc41d5a8d7375c6d3ecabb8c81138622c966aedc949da0c447af5d3
---

**问题现象**

在form\_config.json文件中，如果updateEnabled字段的值为true，则updateDuration和scheduleUpdateTime字段不能同时为空。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/2ByqwFnTR2uosRU2nTcEdg/zh-cn_image_0000002229758573.png?HW-CC-KV=V1&HW-CC-Date=20260428T002914Z&HW-CC-Expire=86400&HW-CC-Sign=6A68A1C5E8137CB31F3E6E1816A9594BC5FD91E8F9C79A5142C7A468EB9F290B "点击放大")

**问题原因**

从 DevEco Studio NEXT Developer Preview 2 版本开始，新增规则：卡片的配置文件中必须包含updateEnabled，设置为true时，可以选择定时刷新（updateDuration）或定点刷新（scheduledUpdateTime）。如果同时配置了两种刷新方式，定时刷新将优先生效。

**解决措施**

进入 module.json5 文件，根据需求选择配置 updateEnabled 为 false，或配置定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）。
