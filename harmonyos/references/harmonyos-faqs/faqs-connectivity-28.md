---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-28
title: 如何在多个无名称ble设备中确定目标设备
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何在多个无名称ble设备中确定目标设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5308ed4a17ceda6bfab77863214a2a385ee018a157d776ef41459e1e0ebe9b6d
---

## 问题现象

当前有部分蓝牙设备无设备名称，在对这些无设备名称的蓝牙设备进行BLE扫描时，如何获取到想要连接的目标设备？

## 背景知识

* BLE广播报文数据[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)中包含设备服务UUID、制造商数据、服务数据等数据。
* HarmonyOS官方指南中提供了BLE扫描及[广播包数据解析](../harmonyos-guides/ble-development-guide.md#完整示例)的代码样例。

## 解决方案

通常蓝牙设备在发送广播时，会携带设备名称、设备服务UUID、特定的制造商标识等一系列标志信息，可根据设备说明书，或联系设备厂家提前获取这类标志信息，然后将HarmonyOS手机扫描获取到的广播包数据进行解析，获取同样的标志部分进行信息匹配，借此确定目标BLE设备。
