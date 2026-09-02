---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-3
title: MDM设置网络白名单功能异常
breadcrumb: FAQ > 系统开发 > 基础功能 > 企业设备管理（MDM） > MDM设置网络白名单功能异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d99e43ef503495cbedca44f4bd218c889929debb3a796b7f22691ff40b27af44
---

## 问题现象

通过[addAllowedWifiList()](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)设置Wi-Fi白名单不生效。

## 背景知识

MDM应用可以通过[addAllowedWifiList](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)添加Wi-Fi白名单，Wi-Fi的ssid+BSSID作为参数传递，添加成功后当前设备仅允许连接该名单下的Wi-Fi。

以下情况下，调用本接口会报策略冲突：

* 已经通过[setDisallowedPolicy](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy24)接口禁用了设备Wi-Fi能力。通过[setDisallowedPolicy](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy24)解除Wi-Fi禁用后，可解除冲突。
* 已经通过[addDisallowedWifiList](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageradddisallowedwifilist19)接口添加了Wi-Fi禁用名单。通过[removeDisallowedWifiList](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanagerremovedisallowedwifilist19)移除Wi-Fi禁用名单后，可解除冲突。

## 问题定位

有问题的操作步骤如下：

1. 确保[restrictions](../harmonyos-references/js-apis-enterprise-restrictions.md)中启用Wi-Fi，wifiManager确保没有[Disallowed](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageradddisallowedwifilist19)和[Allowed](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)的Wi-Fi。
2. 使用[addAllowedWifiList](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)添加一个Wi-Fi白名单，其参数类似[{"ssid":"mate60","BSSID":"92:EF:1C:F1:21:81"}]，BSSID值在此处获取：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/t1J7IdKESjGhTkxlYqA-hA/zh-cn_image_0000002633616294.png "点击放大")
3. 设置后，Wi-Fi白名单未生效。

分析以上操作步骤，发现Wi-Fi白名单未生效的原因是**未正确传递BSSID值**。

BSSID的正确获取方法：

1. 打开“开发者选项”-->"开启wlan详细日志记录"：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/FWKD92X4S66-kK2rpaajxA/zh-cn_image_0000002633456400.png)
2. 查看BSSID：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Z6q8OLa9TveeiP32Rhc7ug/zh-cn_image_0000002663855485.png "点击放大")

## 分析结论

1. BSSID比较隐晦，需要专门的指引，用户才能正确获取BSSID。
2. MAC和BSSID的格式类似，容易误用，导致功能不正常。

## 修改建议

1. 正确获取BSSID。
2. [addAllowedWifiList](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)接口中，传递BSSID。
