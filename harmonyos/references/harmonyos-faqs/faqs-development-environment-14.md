---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-14
title: 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b01b47f85b63224ca61df610ee485664831c1e0357449dd5186bb29bbe46b699
---

**问题描述**

自动生成签名失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/6A1mcvQvSxeBXszE8cAVRw/zh-cn_image_0000002229604309.png)

**解决方案**

报错原因：本地PC和服务器时间不一致。请将本地PC时间与北京时间进行对比，精确到秒。

DevEco Studio签名提示系统时间不正确，请在设置中选择“时间和语言”>“日期和时间”，开启自动设置时间功能，确保时间精确到1-2秒。
