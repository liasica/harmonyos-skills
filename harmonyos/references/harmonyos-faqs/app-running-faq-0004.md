---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-running-faq-0004
title: 在应用中如何区分真机和模拟器
breadcrumb: FAQ > DevEco Studio > 应用运行 > 常见问题 > 在应用中如何区分真机和模拟器
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c683083302010bcc4a5e997e611195153e8fd075a42b8ad8d74ea16773276bf6
---

**Q：在调试应用代码时，如何判断当前运行的设备是真机还是模拟器？**

**A**：在应用中，使用[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)模块的productModel属性来区分真机和模拟器。模拟器上，productModel的值为emulator。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/qdPoBBETQjKnnnN_VaGCng/zh-cn_image_0000002802047223.png "点击放大")
