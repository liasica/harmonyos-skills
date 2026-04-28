---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-23
title: 如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:206efbb03925f199fb055d55046fc202a02ad64083b6b6d0734423464be97fad
---

应用所在设备的信息，可以通过@kit.BasicServicesKit的deviceInfo模块获取：

* SDK版本：deviceInfo.sdkApiVersion。
* 产品版本：deviceInfo.displayVersion。
* 设备类型（平板、手机）：deviceInfo.deviceType。
* build版本：deviceInfo.buildVersion。

更多请参见[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)。
