---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-11
title: 企业MDM应用如何为当前用户添加开机自启动应用名单
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 企业MDM应用如何为当前用户添加开机自启动应用名单
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:390c3584e7786d12d63d463a4f93c9fbe630290a9fd4af7b6f288b0e9d25d42d
---

## 问题现象

企业MDM应用如何实现在手机/PC系统重启后自动启动APP？获取不同空间的accountId参数，作为addAutoStartApps的参数，能否设置不同空间的自动启动APP？

PC上如何设置应用开机自启动？

应用如何实现静默启动，避免开机自启时显示主窗口？

## 解决方案

* PC上可通过系统设置手动配置应用开机自启动：进入设置>应用和元服务>应用启动管理，选择目标应用并开启开机自启动功能。
* 企业MDM应用实现开机自启动可参考：添加开机自启动应用名单，使用[applicationManager.addAutoStartApps](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddautostartapps)添加开机自启动应用名单。
* addAutoStartApps带accountId参数，只在最后调用addAutoStartApps的所属空间生效。
* 从API Version 24开始，[applicationManager.addAutoStartApps](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddautostartapps)新增支持配置应用开机自启时是否隐藏UI界面。设置成功后，应用自启后不显示UI界面，仅在状态栏显示，UI进程存在。隐藏UI界面的能力仅在PC/2in1和Tablet的PC模式中可正常使用。
