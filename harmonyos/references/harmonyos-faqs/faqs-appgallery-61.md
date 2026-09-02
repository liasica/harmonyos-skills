---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-61
title: AppGallery Connect测试设备管理无法批量添加已删除的设备
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AppGallery Connect测试设备管理无法批量添加已删除的设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:972bea10f1a23e89dd153cfbb48e7fe4a6a9726a0214ac53ceb2580a5518671a
---

## 问题现象

AppGallery Connect上在设备列表删除了一些设备后，无法通过批量添加再将这些设备添加上来？

## 解决方案

已删除的设备自创建之日起一年后才会过期，批量添加时会与所有未过期的设备的UDID进行匹配然后添加，所以再次批量添加已删除的设备时会提示已存在，如果需要再次添加已删除的设备目前只能通过单个添加设备的方式重新添加，且需要修改设备名称。详细可参考[删除设备](../app/agc-help-delete-device-0000002248111074.md)。
