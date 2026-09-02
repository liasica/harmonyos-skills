---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-34
title: 如何使用蓝牙订阅事件
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何使用蓝牙订阅事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1848563db731b38e4980f597722dde227b73dfcde7acebc25e45bf06ee5fa16e
---

## 问题现象

如何使用蓝牙订阅事件感知蓝牙开关情况、扫描结果获取和连接状态的变化？对于订阅事件的使用是否有顺序要求？

## 背景知识

* 订阅事件之间没有顺序要求，根据实际情况需要将监听函数放在合适的位置，并且需要在事件触发前进行订阅，比如需要感知蓝牙开关的变化，就要在触发蓝牙开关操作前进行订阅。
* 经典蓝牙物理链路ACL和SCO：
  + ACL（Asynchronous Connectionless）是蓝牙协议中的异步无连接链路，负责设备间数据传输的物理通道。它是经典蓝牙通信的基础链路类型，比如文件传输、音频流等。当ACL链路断开时，所有依赖它的上层协议（如SPP、A2DP、HFP等）的连接状态都会同步断开。
  + SCO（Synchronous Connection Oriented）是同步链路，用于语音等实时性高的场景。

## 解决方案

通过蓝牙订阅事件感知状态变化的实现主要涉及以下三类场景，具体实现方式如下：

* 开关蓝牙场景：调用开启蓝牙[access.enableBluetooth](../harmonyos-references/js-apis-bluetooth-access.md#accessenablebluetooth)时，系统会弹出开启蓝牙的对话框，可以通过以下方式感知用户操作对话框的行为：
  + 同意开启蓝牙：开启蓝牙前通过[access.on('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessonstatechange)订阅本端蓝牙开关状态变化事件，通过回调中的[BluetoothState](../harmonyos-references/js-apis-bluetooth-access.md#bluetoothstate)枚举值确认蓝牙打开。
  + 拒绝开启蓝牙：API20提供了[access.enableBluetoothAsync](../harmonyos-references/js-apis-bluetooth-access.md#accessenablebluetoothasync20)，可以感知弹框拒绝的情况。

    | 错误码ID | 错误信息 | 原因 |
    | --- | --- | --- |
    | 2900013 | The user does not respond. | 弹框后超过一定时间未响应 |
    | 2900014 | User refuse the action. | 弹框后点击拒绝开启蓝牙 |
* 获取蓝牙扫描结果场景：
  + 使用[connection.startBluetoothDiscovery](../harmonyos-references/js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)开启蓝牙扫描，扫描结果可通过API10开始支持的[connection.on('bluetoothDeviceFind')](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)或者API18开始支持的[connection.on('discoveryResult')](../harmonyos-references/js-apis-bluetooth-connection.md#connectionondiscoveryresult18)的回调函数获取。
  + 使用[ble.startBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestartblescan)发起BLE扫描流程，扫描结果可通过[ble.on('BLEDeviceFind')](../harmonyos-references/js-apis-bluetooth-ble.md#bleonbledevicefind)的回调函数获取。
* 监听蓝牙连接状态场景：
  + 经典蓝牙：
    1. 通过API18提供的[socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)、[socket.sppWriteAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwriteasync18)接口可以感知传输过程中经典蓝牙是否已经断连，断开连接时，接口会抛出错误码2901054并返回。
    2. 通过API20提供的[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE](../harmonyos-references/commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_acl_state_change20)的公共事件感知ACL连接状态变化，当ACL链路断开时，所有依赖它的上层协议（如SPP、A2DP、HFP等）的连接状态都会同步断开，因此经典蓝牙连接也会断开。
    3. 通过API22提供的[socket.isConnected](../harmonyos-references/js-apis-bluetooth-socket.md#socketisconnected22)检查当前链路是否已连接。
  + BLE：
    1. client端提供了[on('BLEConnectionStateChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onbleconnectionstatechange)接口，用于监听client端BLE蓝牙的连接状态。server端提供了[on('connectionStateChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onconnectionstatechange)接口，用于监听server端BLE蓝牙的连接状态。通过回调中的[ProfileConnectionState](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)可以确认蓝牙连接状态。

       | 名称 | 值 | 说明 |
       | --- | --- | --- |
       | STATE\_DISCONNECTED | 0 | 表示profile已断连 |
       | STATE\_CONNECTING | 1 | 表示profile正在连接 |
       | STATE\_CONNECTED | 2 | 表示profile已连接 |
       | STATE\_DISCONNECTING | 3 | 表示profile正在断连 |
    2. 通过API22提供的[getConnectedState](../harmonyos-references/js-apis-bluetooth-ble.md#getconnectedstate22-1)获取当前与server端设备的连接状态。
