---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-23
title: 蓝牙BLE无法连接设备问题定位——广播/扫描阶段
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙BLE无法连接设备问题定位——广播/扫描阶段
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c5d7823194fa939fc5cb683871610310c273f672bfc2bed51f8d6bbe0aaca9b8
---

## 问题现象

蓝牙BLE扫描无法获取设备，如何定位是扫描端还是广播端的问题？

## 背景知识

[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)：开始发送BLE广播报文。

[ble.startBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestartblescan)：发起BLE扫描流程。

[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)：扫描BLE广播的过滤条件，只有符合该条件的广播报文才会上报。

[ble.on('BLEDeviceFind')](../harmonyos-references/js-apis-bluetooth-ble.md#bleonbledevicefind)：订阅BLE设备扫描结果上报事件。

## 问题定位

假设当前是手机扫描与车钥匙广播的场景，可以通过以下方式排查：

在车钥匙旁边放一个其他的BLE设备，比如手表、手环或者BLE模组，在蓝牙设置界面能否扫到这个BLE设备和车钥匙。

1.如果设置能扫描到BLE设备，扫描不到车钥匙，可判断为车钥匙广播端问题，需排查是否由于硬件原因未发出广播。

2.如果设置能扫描到，应用扫描不到，可判断为应用的问题，参考以下步骤排查：

* 是否正确设置ScanFilter的过滤条件，例如：参考[BLE扫描流程](../harmonyos-guides/ble-development-guide.md#完整示例)，为什么无法扫描到附近的BLE设备？
* 是否正确设置广播端参数，例如：ble.on('BLEDeviceFind')订阅扫描结果，返回蓝牙名称deviceName为什么是空的？
* 广播端携带的字段与扫描端过滤的字段是否一致，例如：蓝牙扫描ScanFilter过滤参数serviceUuid，无法扫描到目标设备，为什么过滤参数serviceSolicitationUuid就可以扫描到目标设备？

## 分析结论

* **可能原因1：** 硬件原因。

  如果是硬件原因，需要联系硬件提供方分析具体原因。
* **可能原因2：** 应用侧代码设置问题。

  应用侧问题分析结论：

  + 示例中设置了ScanFilter过滤条件，所以扫描不到目标设备，过滤条件需要根据实际情况调整。
  + 对端设备发广播时没有把参数[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)中includeDeviceName设置为true，携带设备名称。由于广播报文数据内容中没有设备名称，扫描到的设备上报就不会有设备名称。
  + serviceUuid一般是外围设备在广播包里携带，表明自己支持哪些服务。serviceSolicitationUuid一般是中央设备在广播包里携带，表明自己希望搜索到哪些服务，但也有设备厂商在外围设备广播包里携带，表明外围设备希望搜索到哪些服务。

## 修改建议

* **场景1：** 硬件原因：

  如果是硬件原因，需要联系硬件提供方分析具体原因后修改。
* **场景2：** 应用侧问题：

  如果需要扫描所有可发现的周边BLE设备，需要把startBLEScan第一个入参改为null，根据实际情况调整过滤条件。
  + 需要把参数AdvertiseData中includeDeviceName设置为true，在广播报文数据内容中携带设备名称，扫描到的设备上报才会有设备名称。
  + 由于当前问题的外围设备在广播报文数据内容中，携带的字段为希望搜索到的UUID服务，因此扫描端需要过滤参数serviceSolicitationUuid，根据广播端携带的字段过滤，两端需要保持一致。

## 总结

蓝牙BLE扫描涉及两端交互，对于扫描端与广播端都需要进行排查，可以通过上述方法进行排查，初步确认问题所在。
