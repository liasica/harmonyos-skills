---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-bluetooth
title: @system.bluetooth (蓝牙)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 已停止维护的接口 > @system.bluetooth (蓝牙)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4fbd73d765ecdfa62929b1af790e287111481e62f75d4b3510f61fcb6bb54d8
---

说明

* 从API Version 7 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](js-apis-bluetooth-ble.md)等相关profile接口。
* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

WearableLite Wearable

```
1. import bluetooth from '@system.bluetooth';
```

## bluetooth.startBLEScan(OBJECT)

WearableLite Wearable

开始搜寻附近的低功耗蓝牙外围设备。此操作比较耗费系统资源，请在搜索并连接到设备后调用[bluetooth.stopBLEScan](js-apis-system-bluetooth.md#bluetoothstopblescanobject)方法停止搜索。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表1** StartBLEScanOptions

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| interval | number | 否 | 上报设备的间隔，单位毫秒，默认值为0。0表示找到新设备立即上报，其他数值根据传入的间隔上报。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**示例：**

```
1. bluetooth.startBLEScan({
2. interval:0,
3. success() {
4. console.log('call bluetooth.startBLEScan success.');
5. },
6. fail(code, data) {
7. console.log('call bluetooth.startBLEScan failed, code:' + code + ', data:' + data);
8. },
9. complete() {
10. console.log('call bluetooth.startBLEScan complete.');
11. }
12. });
```

## bluetooth.stopBLEScan(OBJECT)

WearableLite Wearable

停止搜寻附近的低功耗蓝牙外围设备。与[bluetooth.startBLEScan(OBJECT)](js-apis-system-bluetooth.md#bluetoothstartblescanobject)接口配套使用。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表2** StopBLEScanOptions

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**示例：**

```
1. bluetooth.stopBLEScan({
2. success() {
3. console.log('call bluetooth.stopBLEScan success.');
4. },
5. fail(data, code) {
6. console.log('call bluetooth.stopBLEScan fail, code:' + code + ', data:' + data);
7. },
8. complete() {
9. console.log('call bluetooth.stopBLEScan complete.');
10. }
11. });
```

## bluetooth.subscribeBLEFound(OBJECT)

WearableLite Wearable

订阅寻找到新设备。再次调用时，会覆盖前一次调用效果，即仅最后一次调用生效。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

**表3** SubscribeBLEFoundOptions

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | Function | 是 | 寻找到新设备上报时调用的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |

**表4** success返回值

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| devices | Array<BluetoothDevice> | 新搜索到的设备列表。 |

**表5** BluetoothDevice

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| addrType | string | 设备地址类型，可能值有：  - public: 公共地址  - random: 随机地址 |
| addr | string | 设备MAC地址。 |
| rssi | number | 设备蓝牙的信号强弱指标。 |
| txpower | string | 广播数据中的txpower字段。 |
| data | hex string | 广播数据（包含广播数据和扫描响应数据），十六进制字符串。 |

**示例：**

```
1. bluetooth.subscribeBLEFound({
2. success(data) {
3. console.log('call bluetooth.subscribeBLEFound success, data: ${data}.');
4. },
5. fail(data, code) {
6. console.log('call bluetooth.startBLEScan failed, code:' + code + ', data:' + data);
7. }
8. });
```

## bluetooth.unsubscribeBLEFound()

WearableLite Wearable

解除订阅寻找到新设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**示例：**

```
1. bluetooth.unsubscribeBLEFound();
```

## 常见错误码

WearableLite Wearable

| 错误码 | 说明 |
| --- | --- |
| 1100 | 是否处于已连接状态。 |
| 1101 | 当前蓝牙适配器不可用。 |
| 1102 | 没有找到指定设备。 |
| 1103 | 连接失败。 |
| 1104 | 没有找到指定服务。 |
| 1105 | 没有找到指定特征值。 |
| 1106 | 当前连接已断开。 |
| 1107 | 当前特征值不支持此操作。 |
| 1108 | 其余所有系统上报的异常。 |
| 1109 | 系统版本不支持 BLE。 |
