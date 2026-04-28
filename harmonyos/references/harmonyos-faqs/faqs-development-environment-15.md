---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15
title: DevEco Studio中如何设置超长日志自动换行
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio中如何设置超长日志自动换行
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67f02f29c6ea3f85d1937705d3cb5de045b0236c635b568107ccd010c3c3d5d6
---

启用Soft-Wrap功能以实现日志消息的自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/sjl3zBbQRAuPBmbwZtI-gg/zh-cn_image_0000002194158840.png?HW-CC-KV=V1&HW-CC-Date=20260428T002854Z&HW-CC-Expire=86400&HW-CC-Sign=3E4C6DD2E7D057A85AC1427BB217F3A858751AF9F41FD4A31BF44A39CC4EC8B4 "点击放大")

日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。
