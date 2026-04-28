---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-8
title: 调用notificationManager.publish发布通知失败
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 调用notificationManager.publish发布通知失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3146650c6ce6f0756a29124965819ade275b24ae8f4e9e2c2241012e42812ca4
---

**问题现象**

发布通知后，未生成错误日志信息，通知栏中未显示通知。

**可能原因**

对应应用的通知开关处于关闭状态。

**解决措施**

在真机端系统设置中，开启对应应用的通知开关后，才能在通知栏中看到发布的通知。

方案一：手动开启步骤：设置 > 通知和状态栏 > 应用名称 > 允许通知。

方案二：可通过`notificationManager.requestEnableNotification()`接口弹窗请求用户授权（仅弹一次）。

**参考链接**

[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)
