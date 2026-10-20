---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0008
title: 系统设备信息获取常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > 系统设备信息获取常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:16+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:f51f8ba158d4dd06098343429685473cfd3db237095fa1c46539fceb05e7cc62
---

**Q：如何获取设备的SDK版本、产品版本、设备类型（平板、手机）、build版本等信息？**

A：应用所在设备的信息，可以通过@kit.BasicServicesKit的deviceInfo模块获取：

* SDK版本：deviceInfo.sdkApiVersion。
* 产品版本：deviceInfo.displayVersion。
* 设备类型（平板、手机）：deviceInfo.deviceType。
* build版本：deviceInfo.buildVersion。

更多请参见[@ohos.deviceInfo (设备信息)](../doccenter-references/api/js-apis-device-info.md)。
