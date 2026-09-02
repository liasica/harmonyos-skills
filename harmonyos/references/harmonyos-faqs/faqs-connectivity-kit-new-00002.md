---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-kit-new-00002
title: 蓝牙BLE广播是否支持自定义广播Type数据
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙BLE广播是否支持自定义广播Type数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:9bb2fc8eba5d2d379b0cb04d4c5a4747a8d5f8d687667c55c60c4693c1585b14
---

## 问题现象

使用BLE广播时，通过nRF Connect工具解析广播包数据，获取的数据类型Type均为0xFF（厂商私有数据），没有0x01（广告标记位）、0x09（设备名称）等其他类型数据。是否可以自定义广播Type数据？

## 解决方案

当前API不支持直接设置任意的AD Type值，不同字段对应不同的AD Type，具体如下：

| 字段 | AD Type |
| --- | --- |
| serviceUuids（服务UUID声明） | 0x02/0x03/0x06/0x07 |
| [serviceData](../harmonyos-references/js-apis-bluetooth-ble.md#servicedata)（服务数据，带UUID的自定义数据） | 0x16 |
| [manufactureData](../harmonyos-references/js-apis-bluetooth-ble.md#manufacturedata)（厂商私有数据） | 0xFF |
| includeDeviceName: true（设备名称） | 0x09 |

可以通过[serviceData](../harmonyos-references/js-apis-bluetooth-ble.md#servicedata)（0x16）、includeDeviceName（0x09）等字段来使用蓝牙规范中定义的其他AD Type，而非所有数据都必须通过[manufactureData](../harmonyos-references/js-apis-bluetooth-ble.md#manufacturedata)（0xFF）发送。

更多BLE广播相关内容可参考[BLE广播流程](../harmonyos-guides/ble-development-guide.md#ble广播流程)。
