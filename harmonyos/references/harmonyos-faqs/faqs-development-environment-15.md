---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15
title: DevEco Studio中如何设置超长日志自动换行
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio中如何设置超长日志自动换行
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a79aefad60c7e129281a08355e1f9986720dcf377efab711f0635af92db6f616
---

启用Soft-Wrap功能以实现日志消息的自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/sXJ2emwiTFOQIBXtVta8nw/zh-cn_image_0000002624638320.png "点击放大")

日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。
