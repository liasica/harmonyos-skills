---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15
title: DevEco Studio中如何设置超长日志自动换行
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio中如何设置超长日志自动换行
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ac1195f7d39ed4862b8bcf9684f25a97ea6e4b2539f147b46e0ce652426689e
---

启用Soft-Wrap功能以实现日志消息的自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/sjl3zBbQRAuPBmbwZtI-gg/zh-cn_image_0000002194158840.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=1E460CF0C31EEE222A3347DF748A506DE7D5AD068910B964D937008EAA98CD17 "点击放大")

日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。
