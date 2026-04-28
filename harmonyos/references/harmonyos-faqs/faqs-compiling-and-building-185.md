---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-185
title: 升级react-native-openharmony编译出错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 升级react-native-openharmony编译出错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:48cf1473b0db287ba0ad226b2e7afd3d95eea1b1ba36d6dbe42e0aa35bdeede6
---

**问题现象**

升级react-native-openharmony编译出错，类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1tpFiQmBQ4Kl9kpDiQStfw/zh-cn_image_0000002304734606.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=9E3CC312F6CFB83D99DF4D1791A588ED798FEBDD3FED1B238CDD2A1E50994E87)

**问题原因**

旧版本的react-native-openharmony缓存还在,导致某些链接找不到。

**解决措施**

删除要编译的模块根目录下的.cxx和build目录,然后重新触发编译。
