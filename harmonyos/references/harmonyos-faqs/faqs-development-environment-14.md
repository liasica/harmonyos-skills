---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-14
title: 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误
breadcrumb: FAQ > DevEco Studio > 环境准备 > 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:74504e49e7c472b959f7ded5c1238ff7989e90a81fb78a4e47ace14ce7c1712a
---

**问题描述**

自动生成签名失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/6A1mcvQvSxeBXszE8cAVRw/zh-cn_image_0000002229604309.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=3E72C99FDF7353FAF9F787015C8DC8E0A9EB348F42A0C920434FF9F77B09AA63)

**解决方案**

报错原因：本地PC和服务器时间不一致。请将本地PC时间与北京时间进行对比，精确到秒。

DevEco Studio签名提示系统时间不正确，请在设置中选择“时间和语言”>“日期和时间”，开启自动设置时间功能，确保时间精确到1-2秒。
