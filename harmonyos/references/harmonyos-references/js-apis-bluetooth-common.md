---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-common
title: "@ohos.bluetooth.common (蓝牙common模块)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.common (蓝牙common模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:529b7068a9cc82425e31839d2c34b5fe27e54e87a094ff02c27aa7e8c07ca833
---

本模块提供了蓝牙公共接口和参数类型。首批接口包括在调用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice21)时用于指定目标设备的MAC地址与地址类型的相关参数。

**说明** 

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { common } from '@kit.ConnectivityKit';
```

## BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 表示蓝牙设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |
| addressType | [BluetoothAddressType](js-apis-bluetooth-common.md#bluetoothaddresstype) | 否 | 否 | 表示地址类型为蓝牙设备的实际MAC地址或虚拟MAC地址。 |
| rawAddressType23+ | [BluetoothRawAddressType](js-apis-bluetooth-common.md#bluetoothrawaddresstype23) | 否 | 是 | 表示地址类型为蓝牙协议定义的Public类型或Random类型。默认值请参见相关接口说明，未传入时使用系统默认地址类型。 |

## BluetoothAddressType

枚举，蓝牙子系统定义的地址类型。蓝牙设备的实际MAC地址属于用户的隐私信息，在发现设备的过程中，蓝牙子系统会给每个蓝牙外设分配一个虚拟MAC地址，并保存该虚拟MAC地址和外设实际MAC地址的映射关系。关于地址类型的详细介绍请参见[蓝牙设备地址类型](../harmonyos-guides/bluetooth-overview.md#蓝牙设备地址类型)。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIRTUAL | 1 | 虚拟MAC地址类型。 |
| REAL | 2 | 实际MAC地址类型。 |

## BluetoothRawAddressType23+

枚举，蓝牙协议定义的蓝牙设备地址类型。关于地址类型的详细介绍请参见[蓝牙设备地址类型](../harmonyos-guides/bluetooth-overview.md#蓝牙设备地址类型)。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PUBLIC | 0 | 公共设备地址类型，该类型地址由IEEE组织分配并保证全球唯一性，永久不变。 |
| RANDOM | 1 | 随机设备地址类型，该类型地址随机生成，包括静态随机地址和私有随机地址等子类型，可能定期变化。 |
