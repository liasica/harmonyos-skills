---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-7
title: BLE蓝牙无法搜索到对端设备
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙无法搜索到对端设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:879bb7907d52b0283c99d58d32f1448cfb5e7d4904ccdb31d35aaf33dd4f5813
---

## 问题现象

1. 使用[低功耗蓝牙（Bluetooth Low Energy，BLE）](../harmonyos-references/js-apis-bluetooth-ble.md)开启扫描，不添加过滤条件时，可以搜索到指定的对端设备，添加自定义过滤条件后，无法搜索到指定的对端设备。
2. 蓝牙搜索过程中，部分蓝牙设备通过[serviceUuid](../harmonyos-references/js-apis-bluetooth-ble.md#servicedata)无法扫描到对应设备。

## 背景知识

通过BLE扫描周边其他设备发出的BLE广播，可以发现或者查找到应用需要的目标设备，适用于查找设备场景。若本机设备扫描到可连接的BLE广播，则可以和该设备进行通用属性协议（Generic Attribute Profile，GATT）的连接和数据传输，此时本机设备角色也被称为GATT客户端。具体操作请参考[连接和传输数据](../harmonyos-guides/gatt-development-guide.md)。

## 问题定位

1. 检查代码中过滤条件使用是否有误或扫描结果返回是否做了特殊处理，存在开发者可能将真实mac地址作为[scanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)过滤条件及BLE设备发现上报事件回调中使用真实mac地址作为判断条件的情况。
2. 存在部分设备厂商可能没有将serviceUuid放入广播包里的情况。

## 分析结论

1. 基于信息安全考虑，BLE蓝牙底层对真实mac地址做了特殊处理，生成的是虚拟mac地址。因此，若代码中使用真实mac地址作为过滤条件，无法筛选出设备。
2. 部分设备厂商没有把serviceUuid放入广播包中，导致搜索异常。

## 修改建议

* 可根据官方API文档中的过滤条件设置其他过滤参数，以实现扫描出指定设备的能力。如：serviceUuid、[manufactureId](../harmonyos-references/js-apis-bluetooth-ble.md#manufacturedata)、name等过滤参数。所有过滤参数只支持完全匹配，不支持模糊匹配。
* 可以不使用过滤条件，查询出所有设备后对全部设备进行代码手动过滤。

## 常见FAQ

Q：使用[BleScanner.startScan](../harmonyos-references/js-apis-bluetooth-ble.md#startscan15)发起扫描时，如果[ScanReportMode](../harmonyos-references/js-apis-bluetooth-ble.md#scanreportmode15)参数设置为ble.ScanReportMode.FENCE\_SENSITIVITY\_HIGH，不添加过滤条件，会报错401。

A：ScanReportMode参数设置为ble.ScanReportMode.FENCE\_SENSITIVITY\_HIGH时，必须添加过滤条件，如果不添加，接口会报错提示401参数错误。
