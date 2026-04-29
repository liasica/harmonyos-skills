---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-40
title: 编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e3c9f4a3b2adbe51a2eed7f4db0e2dc2b130eb9bfa72debfa2fdb8855780be5
---

**问题现象**

在form\_config.json文件中，如果updateEnabled字段的值为true，则updateDuration和scheduleUpdateTime字段不能同时为空。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/2ByqwFnTR2uosRU2nTcEdg/zh-cn_image_0000002229758573.png?HW-CC-KV=V1&HW-CC-Date=20260429T062028Z&HW-CC-Expire=86400&HW-CC-Sign=6304E655E65E2767E15E35C72A6F31E4765B02E4B80A848CCD5A797CE6875110 "点击放大")

**问题原因**

从 DevEco Studio NEXT Developer Preview 2 版本开始，新增规则：卡片的配置文件中必须包含updateEnabled，设置为true时，可以选择定时刷新（updateDuration）或定点刷新（scheduledUpdateTime）。如果同时配置了两种刷新方式，定时刷新将优先生效。

**解决措施**

进入 module.json5 文件，根据需求选择配置 updateEnabled 为 false，或配置定时刷新（updateDuration）和定点刷新（scheduledUpdateTime）。
