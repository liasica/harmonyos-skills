---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-28
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f6117738fad0233e3c8a2b30e694cb172655c14fd48efbecd9b7daf78c4de18e
---

**问题现象**

在调试应用代码时，需要判断当前运行的设备是真机还是模拟器，可以通过检查特定的系统属性或环境变量来实现区分。

**解决措施**

在应用中，使用[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CSzDsJB6Q7yN88Tkh1Zk_g/zh-cn_image_0000002229603717.png "点击放大")
