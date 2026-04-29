---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-28
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:53845ec81fc422475d88c54866cf1519d498bbf84f7fb125f589649118ed7420
---

**问题现象**

在调试应用代码时，需要判断当前运行的设备是真机还是模拟器，可以通过检查特定的系统属性或环境变量来实现区分。

**解决措施**

在应用中，使用[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CSzDsJB6Q7yN88Tkh1Zk_g/zh-cn_image_0000002229603717.png?HW-CC-KV=V1&HW-CC-Date=20260429T062117Z&HW-CC-Expire=86400&HW-CC-Sign=64496D32BC47EF8941C8A5489820F064006507F315D23DD24FBEFFE65D0BC4F4 "点击放大")
