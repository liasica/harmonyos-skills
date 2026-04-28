---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-28
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2574fe1bc5ea9e4921c829f6d53e297539eb01b40cebd26522cea0873986b79f
---

**问题现象**

在调试应用代码时，需要判断当前运行的设备是真机还是模拟器，可以通过检查特定的系统属性或环境变量来实现区分。

**解决措施**

在应用中，使用[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CSzDsJB6Q7yN88Tkh1Zk_g/zh-cn_image_0000002229603717.png?HW-CC-KV=V1&HW-CC-Date=20260428T002959Z&HW-CC-Expire=86400&HW-CC-Sign=14296F7C5C2FD049630C0FA3C3BDBCF7081700163B87D5A0265E51A14DE57ECD "点击放大")
