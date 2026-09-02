---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-9
title: 如何添加保活应用名单
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > 如何添加保活应用名单
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:5c77eda349ae36ea10affc1385086ddfb1fbe51f0a3470c5ab9d49b2730eb31a
---

## 问题现象

MDM应用中如何添加保活应用名单，添加过程中需要注意些什么事项。

## 解决方案

MDM Kit提供了[applicationManager.addKeepAliveApps14+](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddkeepaliveapps14)接口可以添加保活应用名单，其中bundleNames参数为指定需要添加至保活名单的应用，最大支持5个。使用添加保活应用名单接口过程中，常见注意事项：

* 安装在普通用户下且应用需要参考[应用接入状态栏](../harmonyos-guides/statusbar-extension-guide.md)，通过最小化系统托盘实现应用后台保活。
* 如果将应用添加至应用禁止运行名单[applicationManager.addDisallowedRunningBundlesSync](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)，就不能将应用添加至保活应用名单。
* 保活机制中会检测extensionAbilities中是否有type为statusBarView的类型，需要在module.json5中添加。如果目标应用仅添加了状态栏图标但未实现StatusBarViewExtensionAbility，调用addKeepAliveApps接口会报错Code:9201005，提示“Add keep alive applications failed. Application does not have status bar ability.”。
* addKeepAliveApps接口仅在PC设备上生效（PC设备有状态栏）。如果需要在Phone/Tablet设备上实现类似功能，可以调用[applicationManager.addUserNonStopApps22+](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddusernonstopapps22)或者[applicationManager.addFreezeExemptedApps22+](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddfreezeexemptedapps22)接口。
