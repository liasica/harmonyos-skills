---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-28
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9cda85159be7a386c03d78a19358630841f86ca171ab41f3520f37bd6814ac21
---

**问题现象**

在调试应用代码时，需要判断当前运行的设备是真机还是模拟器，可以通过检查特定的系统属性或环境变量来实现区分。

**解决措施**

在应用中，使用[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/2HYajBXDTLajwln0IbBuCg/zh-cn_image_0000002624478762.png "点击放大")
