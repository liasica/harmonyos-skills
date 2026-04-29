---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-185
title: 升级react-native-openharmony编译出错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 升级react-native-openharmony编译出错
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5c2657f197b84cd99504698f17d9b8b8677e992156294e8cc1438d529863a333
---

**问题现象**

升级react-native-openharmony编译出错，类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1tpFiQmBQ4Kl9kpDiQStfw/zh-cn_image_0000002304734606.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=D921EBEB3B2B3B04B9C2263848BDAC7E0BB28041BB966F6781EE88467CDE72BE)

**问题原因**

旧版本的react-native-openharmony缓存还在,导致某些链接找不到。

**解决措施**

删除要编译的模块根目录下的.cxx和build目录,然后重新触发编译。
