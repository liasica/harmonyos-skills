---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-6
title: requestEnableNotification接口申请通知权限的机制是怎样的
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > requestEnableNotification接口申请通知权限的机制是怎样的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f10f4db5c2473ed65cfe859d34b0f8b9b140432bef7c21cefb0810ac88628a46
---

* 首次执行requestEnableNotification时，会弹出通知权限申请弹窗，该接口的回调与用户授权状态无关。
* 当requestEnableNotification非首次执行时，不会弹出通知权限申请弹窗，并且无论是否拥有通知权限，都会直接返回 success。
