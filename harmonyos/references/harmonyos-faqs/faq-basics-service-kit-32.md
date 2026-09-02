---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-32
title: 如何监听到用户是否卸载了App
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何监听到用户是否卸载了App
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:12f5e59cb314c8231563b21260e4af998fdb422eca43315f96c87d96ead36b7e
---

## 问题现象

HarmonyOS中是否有API能够监听到用户卸载了APP。

## 解决方案

监听用户安装与卸载分为两种情况：

1. 监听其他应用：

   可以参考[动态订阅公共事件](../harmonyos-guides/common-event-subscription.md)：

   * [usual.event.PACKAGE\_ADDED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_added)：表示设备上已安装新应用包的公共事件的动作。在设备上指定用户下安装了新的应用程序，将会触发事件通知服务发布该系统公共事件。需注意，三方应用只能监听自身应用的安装事件。
   * [usual.event.PACKAGE\_REMOVED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_removed)：表示已从设备卸载已安装的应用程序，但应用程序数据保留的公共事件的动作。在设备指定用户下卸载指定的应用程序包，将会触发事件通知服务发布该系统公共事件。
2. 监听应用自身：
   * 应用内无法通过代码监听自身是否被卸载，因为卸载会直接终止进程，不会触发生命周期回调函数或者其他函数，也就无法在应用内监听卸载。
   * 可以通过[“下载安装”](../app/agc-help-anaiyze-app-usage-0000002236492392.md#section14231122115416)报表获取安装和卸载量。
