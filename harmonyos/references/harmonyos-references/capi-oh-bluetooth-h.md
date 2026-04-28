---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-bluetooth-h
title: oh_bluetooth.h
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > C API > 头文件 > oh_bluetooth.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3ba47b3fec2a328a23bacae50102d538b3cea133808c155d1e4e3fd28642f67e
---

## 概述

PhonePC/2in1TabletTVWearable

定义查询蓝牙开关状态的接口。

**引用文件：** <ConnectivityKit/bluetooth/oh\_bluetooth.h>

**库：** libbluetooth\_ndk.so

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 13

**相关模块：** [Bluetooth](capi-bluetooth.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Bluetooth\_SwitchState](capi-oh-bluetooth-h.md#bluetooth_switchstate) | Bluetooth\_SwitchState | 定义蓝牙开关状态的枚举值。 |
| [Bluetooth\_ResultCode](capi-oh-bluetooth-h.md#bluetooth_resultcode) | Bluetooth\_ResultCode | 定义蓝牙返回值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Bluetooth\_ResultCode OH\_Bluetooth\_GetBluetoothSwitchState(Bluetooth\_SwitchState \*state)](capi-oh-bluetooth-h.md#oh_bluetooth_getbluetoothswitchstate) | 获取蓝牙开关状态。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Bluetooth\_SwitchState

PhonePC/2in1TabletTVWearable

```
1. enum Bluetooth_SwitchState
```

**描述**

定义蓝牙开关状态的枚举值。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| BLUETOOTH\_STATE\_OFF = 0 | 表示蓝牙关闭。 |
| BLUETOOTH\_STATE\_TURNING\_ON = 1 | 表示蓝牙打开中。 |
| BLUETOOTH\_STATE\_ON = 2 | 表示蓝牙已打开，使用就绪。 |
| BLUETOOTH\_STATE\_TURNING\_OFF = 3 | 表示蓝牙关闭中。 |
| BLUETOOTH\_STATE\_BLE\_TURNING\_ON = 4 | 表示蓝牙LE only模式打开中。 |
| BLUETOOTH\_STATE\_BLE\_ON = 5 | 表示蓝牙处于LE only模式。 |
| BLUETOOTH\_STATE\_BLE\_TURNING\_OFF = 6 | 表示蓝牙LE only模式关闭中。 |

### Bluetooth\_ResultCode

PhonePC/2in1TabletTVWearable

```
1. enum Bluetooth_ResultCode
```

**描述**

定义蓝牙返回值。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| BLUETOOTH\_SUCCESS = 0 | 操作成功。 |
| BLUETOOTH\_INVALID\_PARAM = 401 | 参数错误。可能原因：1. 输入参数为空指针；2. 参数数值超出定义范围。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Bluetooth\_GetBluetoothSwitchState()

PhonePC/2in1TabletTVWearable

```
1. Bluetooth_ResultCode OH_Bluetooth_GetBluetoothSwitchState(Bluetooth_SwitchState *state)
```

**描述**

获取蓝牙开关状态。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Bluetooth\_SwitchState](capi-oh-bluetooth-h.md#bluetooth_switchstate) \*state | - 指向接收蓝牙开关状态的枚举值的指针。需要传入非空指针，否则将返回错误码。详细定义请参考[Bluetooth\_SwitchState](capi-oh-bluetooth-h.md#bluetooth_switchstate)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Bluetooth\_ResultCode](capi-oh-bluetooth-h.md#bluetooth_resultcode) | 蓝牙开关状态函数返回值。  详细定义请参考[Bluetooth\_ResultCode](capi-oh-bluetooth-h.md#bluetooth_resultcode)。  [BLUETOOTH\_SUCCESS](capi-oh-bluetooth-h.md#bluetooth_resultcode) 成功获取蓝牙开关状态。  [BLUETOOTH\_INVALID\_PARAM](capi-oh-bluetooth-h.md#bluetooth_resultcode) 输入参数为空指针。 |
