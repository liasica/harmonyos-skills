---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-185
title: 升级react-native-openharmony编译出错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 升级react-native-openharmony编译出错
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b4bd6ea7d910abe1e0a78ad6b7a9cb47c520e55ea096fce69f28bf5017b28a14
---

**问题现象**

升级react-native-openharmony编译出错，类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/8yfMX1bJSsmATrXel5jEyQ/zh-cn_image_0000002624638608.png)

**问题原因**

旧版本的react-native-openharmony缓存还在,导致某些链接找不到。

**解决措施**

删除要编译的模块根目录下的.cxx和build目录,然后重新触发编译。
