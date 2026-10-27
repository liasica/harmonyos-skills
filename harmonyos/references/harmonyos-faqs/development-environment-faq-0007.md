---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0007
title: DevEco Studio自动签名时间过期问题排查
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > DevEco Studio自动签名时间过期问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:1845cafe51dcc2b3e9fdee1225c9cf17c37b5af3ae36175c00f2c0ad54616c0c
---

**Q：自动签名时提示“The signature does not take effect or has expired. It May be the current system time is inaccurate, please calibrate the system time and sign again”错误，自动生成签名失败。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/TIXo8UkzSt-7zuj-yv9_0Q/zh-cn_image_0000002773151448.png "点击放大")

**A**：报错原因：本地PC和服务器时间不一致。请将本地PC时间与北京时间进行对比，精确到秒。

DevEco Studio签名提示系统时间不正确，请在设置中选择“时间和语言”>“日期和时间”，开启自动设置时间功能，确保时间精确到1-2秒。
