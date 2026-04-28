---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant
title: @ohos.bluetooth.constant (蓝牙constant模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.constant (蓝牙constant模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f38329ba1d2f1ae201bfde3a2c751097fb52e1730b085fbeb370c2409b975d95
---

本模块提供了蓝牙[Profile](../harmonyos-guides/terminology.md#profile)、设备类型相关的常量定义。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { constant } from '@kit.ConnectivityKit';
```

## ProfileId

PhonePC/2in1TabletTVWearable

枚举，表示蓝牙[Profile](../harmonyos-guides/terminology.md#profile)协议的标识。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE\_A2DP\_SOURCE | 1 | [A2DP Source](../harmonyos-guides/terminology.md#a2dp-source) Profile，负责发送音频数据端使用的协议。 |
| PROFILE\_HANDSFREE\_AUDIO\_GATEWAY | 4 | [HFP Ag](../harmonyos-guides/terminology.md#hfp-ag) Profile，负责通话音频网关使用的协议。 |
| PROFILE\_HID\_HOST | 6 | [HID Host](../harmonyos-guides/terminology.md#hid-host) Profile，负责与[HID Device](../harmonyos-guides/terminology.md#hid-device)建立通信并处理数据交互的协议。 |
| PROFILE\_PAN\_NETWORK | 7 | [NAP](../harmonyos-guides/terminology.md#nap) Profile，负责提供网络共享端使用的协议。 |

## ProfileConnectionState

PhonePC/2in1TabletTVWearable

枚举，本端和对端蓝牙设备间的Profile连接状态。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_DISCONNECTED | 0 | 表示Profile已断开连接。 |
| STATE\_CONNECTING | 1 | 表示Profile正在连接。 |
| STATE\_CONNECTED | 2 | 表示Profile已连接。 |
| STATE\_DISCONNECTING | 3 | 表示Profile正在断开连接。 |

## MajorClass

PhonePC/2in1TabletTVWearable

枚举，蓝牙设备的主要类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAJOR\_MISC | 0x0000 | 表示不属于其他标准类别的杂项设备。 |
| MAJOR\_COMPUTER | 0x0100 | 表示计算机设备。 |
| MAJOR\_PHONE | 0x0200 | 表示手机设备。 |
| MAJOR\_NETWORKING | 0x0300 | 表示局域网/网络接入点设备。 |
| MAJOR\_AUDIO\_VIDEO | 0x0400 | 表示音频/视频设备。 |
| MAJOR\_PERIPHERAL | 0x0500 | 表示外围设备。 |
| MAJOR\_IMAGING | 0x0600 | 表示成像设备。 |
| MAJOR\_WEARABLE | 0x0700 | 表示可穿戴设备。 |
| MAJOR\_TOY | 0x0800 | 表示玩具设备。 |
| MAJOR\_HEALTH | 0x0900 | 表示健康设备。 |
| MAJOR\_UNCATEGORIZED | 0x1F00 | 表示未分类设备。 |

## MajorMinorClass

PhonePC/2in1TabletTVWearable

枚举，蓝牙设备的子类型，在[MajorClass](js-apis-bluetooth-constant.md#majorclass)基础上进一步细分的类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPUTER\_UNCATEGORIZED | 0x0100 | 表示未分类计算机设备。 |
| COMPUTER\_DESKTOP | 0x0104 | 表示台式计算机设备。 |
| COMPUTER\_SERVER | 0x0108 | 表示服务器设备。 |
| COMPUTER\_LAPTOP | 0x010C | 表示便携式计算机设备。 |
| COMPUTER\_HANDHELD\_PC\_PDA | 0x0110 | 表示手持式计算机设备。 |
| COMPUTER\_PALM\_SIZE\_PC\_PDA | 0x0114 | 表示掌上电脑设备。 |
| COMPUTER\_WEARABLE | 0x0118 | 表示可穿戴计算机设备。 |
| COMPUTER\_TABLET | 0x011C | 表示平板电脑设备。 |
| PHONE\_UNCATEGORIZED | 0x0200 | 表示未分类手机设备。 |
| PHONE\_CELLULAR | 0x0204 | 表示便携式手机设备。 |
| PHONE\_CORDLESS | 0x0208 | 表示无线电话设备。 |
| PHONE\_SMART | 0x020C | 表示智能手机设备。 |
| PHONE\_MODEM\_OR\_GATEWAY | 0x0210 | 表示调制解调器或网关手机设备。 |
| PHONE\_ISDN | 0x0214 | 表示ISDN手机设备。 |
| NETWORK\_FULLY\_AVAILABLE | 0x0300 | 表示网络负载占用率0%的网络设备。 |
| NETWORK\_1\_TO\_17\_UTILIZED | 0x0320 | 表示网络负载占用率1%~17%的网络设备。 |
| NETWORK\_17\_TO\_33\_UTILIZED | 0x0340 | 表示网络负载占用率17%~33%的网络设备。 |
| NETWORK\_33\_TO\_50\_UTILIZED | 0x0360 | 表示网络负载占用率33%~50%的网络设备。 |
| NETWORK\_60\_TO\_67\_UTILIZED | 0x0380 | 表示网络负载占用率60%~67%的网络设备。 |
| NETWORK\_67\_TO\_83\_UTILIZED | 0x03A0 | 表示网络负载占用率67%~83%的网络设备。 |
| NETWORK\_83\_TO\_99\_UTILIZED | 0x03C0 | 表示网络负载占用率83%~99%的网络设备。 |
| NETWORK\_NO\_SERVICE | 0x03E0 | 表示网络负载占用率100%的网络设备。 |
| AUDIO\_VIDEO\_UNCATEGORIZED | 0x0400 | 表示未分类音频/视频设备。 |
| AUDIO\_VIDEO\_WEARABLE\_HEADSET | 0x0404 | 表示可穿戴式音频/视频设备。 |
| AUDIO\_VIDEO\_HANDSFREE | 0x0408 | 表示免提音频/视频设备。 |
| AUDIO\_VIDEO\_MICROPHONE | 0x0410 | 表示麦克风音频/视频设备。 |
| AUDIO\_VIDEO\_LOUDSPEAKER | 0x0414 | 表示扬声器音频/视频设备。 |
| AUDIO\_VIDEO\_HEADPHONES | 0x0418 | 表示头戴式音频/视频设备。 |
| AUDIO\_VIDEO\_PORTABLE\_AUDIO | 0x041C | 表示便携式音频/视频设备。 |
| AUDIO\_VIDEO\_CAR\_AUDIO | 0x0420 | 表示汽车音频/视频设备。 |
| AUDIO\_VIDEO\_SET\_TOP\_BOX | 0x0424 | 表示机顶盒音频/视频设备。 |
| AUDIO\_VIDEO\_HIFI\_AUDIO | 0x0428 | 表示高保真音频/视频设备。 |
| AUDIO\_VIDEO\_VCR | 0x042C | 表示录像机音频/视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_CAMERA | 0x0430 | 表示照相机视频设备。 |
| AUDIO\_VIDEO\_CAMCORDER | 0x0434 | 表示摄像机音频/视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_MONITOR | 0x0438 | 表示监视器视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER | 0x043C | 表示具备显示和扬声器的视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_CONFERENCING | 0x0440 | 表示会议视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY | 0x0448 | 表示游戏玩具视频设备。 |
| PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING | 0x0500 | 表示非键盘非指向外围设备。 |
| PERIPHERAL\_KEYBOARD | 0x0540 | 表示外设键盘设备。 |
| PERIPHERAL\_POINTING\_DEVICE | 0x0580 | 表示定点装置外围设备。 |
| PERIPHERAL\_KEYBOARD\_POINTING | 0x05C0 | 表示键盘指向外围设备。 |
| PERIPHERAL\_UNCATEGORIZED | 0x0500 | 表示未分类外围设备。 |
| PERIPHERAL\_JOYSTICK | 0x0504 | 表示周边操纵杆设备。 |
| PERIPHERAL\_GAMEPAD | 0x0508 | 表示周边游戏板设备。 |
| PERIPHERAL\_REMOTE\_CONTROL | 0x05C0 | 表示远程控制外围设备。 |
| PERIPHERAL\_SENSING\_DEVICE | 0x0510 | 表示外围传感设备设备。 |
| PERIPHERAL\_DIGITIZER\_TABLET | 0x0514 | 表示外围数字化仪平板电脑设备。 |
| PERIPHERAL\_CARD\_READER | 0x0518 | 表示外围读卡器设备。 |
| PERIPHERAL\_DIGITAL\_PEN | 0x051C | 表示外设数码笔设备。 |
| PERIPHERAL\_SCANNER\_RFID | 0x0520 | 表示射频识别扫描仪外围设备。 |
| PERIPHERAL\_GESTURAL\_INPUT | 0x0522 | 表示手势输入外围设备。 |
| IMAGING\_UNCATEGORIZED | 0x0600 | 表示未分类的图像设备。 |
| IMAGING\_DISPLAY | 0x0610 | 表示图像显示设备。 |
| IMAGING\_CAMERA | 0x0620 | 表示成像照相机设备。 |
| IMAGING\_SCANNER | 0x0640 | 表示成像扫描仪设备。 |
| IMAGING\_PRINTER | 0x0680 | 表示成像打印机设备。 |
| WEARABLE\_UNCATEGORIZED | 0x0700 | 表示未分类的可穿戴设备。 |
| WEARABLE\_WRIST\_WATCH | 0x0704 | 表示可穿戴腕表设备。 |
| WEARABLE\_PAGER | 0x0708 | 表示可穿戴寻呼机设备。 |
| WEARABLE\_JACKET | 0x070C | 表示可穿戴夹克设备。 |
| WEARABLE\_HELMET | 0x0710 | 表示可穿戴头盔设备。 |
| WEARABLE\_GLASSES | 0x0714 | 表示可穿戴眼镜设备。 |
| TOY\_UNCATEGORIZED | 0x0800 | 表示未分类的玩具设备。 |
| TOY\_ROBOT | 0x0804 | 表示玩具机器人设备。 |
| TOY\_VEHICLE | 0x0808 | 表示玩具车设备。 |
| TOY\_DOLL\_ACTION\_FIGURE | 0x080C | 表示人形娃娃玩具设备。 |
| TOY\_CONTROLLER | 0x0810 | 表示玩具控制器设备。 |
| TOY\_GAME | 0x0814 | 表示玩具游戏设备。 |
| HEALTH\_UNCATEGORIZED | 0x0900 | 表示未分类健康设备。 |
| HEALTH\_BLOOD\_PRESSURE | 0x0904 | 表示血压健康设备。 |
| HEALTH\_THERMOMETER | 0x0908 | 表示温度计健康设备。 |
| HEALTH\_WEIGHING | 0x090C | 表示体重健康设备。 |
| HEALTH\_GLUCOSE | 0x0910 | 表示葡萄糖健康设备。 |
| HEALTH\_PULSE\_OXIMETER | 0x0914 | 表示脉搏血氧仪健康设备。 |
| HEALTH\_PULSE\_RATE | 0x0918 | 表示脉搏率健康设备。 |
| HEALTH\_DATA\_DISPLAY | 0x091C | 表示数据显示健康设备。 |
| HEALTH\_STEP\_COUNTER | 0x0920 | 表示阶梯计数器健康设备。 |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | 表示身体成分分析仪健康设备。 |
| HEALTH\_PEAK\_FLOW\_MONITOR | 0x0928 | 表示湿度计健康设备。 |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | 表示个人移动健康设备。 |

## ProfileUuids12+

PhonePC/2in1TabletTVWearable

枚举，由蓝牙技术联盟（[Bluetooth Special Interest Group](../harmonyos-guides/terminology.md#bluetooth-sig)）定义，使用通用唯一标识（Universally Unique Identifier，[UUID](../harmonyos-guides/terminology.md#uuid)）表示不同的蓝牙协议Profile。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE\_UUID\_HFP\_AG | '0000111F-0000-1000-8000-00805F9B34FB' | 表示Hands-Free Audio Gateway Profile。 |
| PROFILE\_UUID\_HFP\_HF | '0000111E-0000-1000-8000-00805F9B34FB' | 表示Hands-Free Profile。 |
| PROFILE\_UUID\_HSP\_AG | '00001112-0000-1000-8000-00805F9B34FB' | 表示Headset Audio Gateway Profile。 |
| PROFILE\_UUID\_HSP\_HS | '00001108-0000-1000-8000-00805F9B34FB' | 表示Headset Profile。 |
| PROFILE\_UUID\_A2DP\_SRC | '0000110A-0000-1000-8000-00805F9B34FB' | 表示A2DP Source Profile。 |
| PROFILE\_UUID\_A2DP\_SINK | '0000110B-0000-1000-8000-00805F9B34FB' | 表示A2DP Sink Profile。 |
| PROFILE\_UUID\_AVRCP\_CT | '0000110E-0000-1000-8000-00805F9B34FB' | 表示AVRCP Controller Profile。 |
| PROFILE\_UUID\_AVRCP\_TG | '0000110C-0000-1000-8000-00805F9B34FB' | 表示AVRCP Target Profile。 |
| PROFILE\_UUID\_HID | '00001124-0000-1000-8000-00805F9B34FB' | 表示HID Profile。 |
| PROFILE\_UUID\_HOGP | '00001812-0000-1000-8000-00805F9B34FB' | 表示HID over GATT Profile。 |
