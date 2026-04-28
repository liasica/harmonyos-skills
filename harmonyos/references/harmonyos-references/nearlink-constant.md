---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-constant
title: constant（星闪公共常量定义）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > constant（星闪公共常量定义）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0c8e521e7ec078ccf7ddeea86571e8e6d0bec6c569f44fd7a857cbb40848981
---

本模块提供了共用的一些常量定义。

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { constant } from '@kit.NearLinkKit';
```

## PairingState

PhonePC/2in1TabletTVWearable

表示和远端设备的配对状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAIRING\_STATE\_NONE | 1 | 表示未配对。 |
| PAIRING\_STATE\_PAIRING | 2 | 表示配对中。 |
| PAIRING\_STATE\_PAIRED | 3 | 表示已配对。 |

## ConnectionState

PhonePC/2in1TabletTVWearable

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_CONNECTING | 0 | 表示正在连接。 |
| STATE\_CONNECTED | 1 | 表示已连接。 |
| STATE\_DISCONNECTING | 2 | 表示正在断连。 |
| STATE\_DISCONNECTED | 3 | 表示已断连。 |

## DeviceClass

PhonePC/2in1TabletTVWearable

表示设备类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_UNCATEGORIZED | 0x000100 | 未分类设备。 |
| DEVICE\_PHONE | 0x000200 | 电话。 |
| DEVICE\_SMARTPHONE | 0x000201 | 智能手机。 |
| DEVICE\_COMPUTER | 0x000300 | 计算机。 |
| DEVICE\_LAPTOP | 0x000301 | 笔记本电脑。 |
| DEVICE\_TABLET | 0x000302 | 平板。 |
| DEVICE\_ALL\_IN\_ONE\_COMPUTER | 0x000303 | 2in1。 |
| DEVICE\_MINI\_PC | 0x000304 | 迷你PC。 |
| DEVICE\_WATCH | 0x000400 | 手表。 |
| DEVICE\_SMART\_WATCH | 0x000401 | 智能手表。 |
| DEVICE\_HUMAN\_INTERFACE | 0x000500 | 人机接口。 |
| DEVICE\_KEYBOARD | 0x000501 | 键盘。 |
| DEVICE\_MOUSE | 0x000502 | 鼠标。 |
| DEVICE\_HANDLE | 0x000503 | 手柄。 |
| DEVICE\_STYLUS | 0x000504 | 手写笔。 |
| DEVICE\_TOUCHPAD | 0x000505 | 触摸板。 |
| DEVICE\_AUDIO\_PLAYBACK | 0x000600 | 音频播放器。 |
| DEVICE\_SMART\_SPEAKER | 0x000601 | 智能扬声器。 |
| DEVICE\_ECHO\_WALL | 0x000602 | 回音设备。 |
| DEVICE\_AUDIO\_CAPTURE | 0x000700 | 录音器。 |
| DEVICE\_KARAOKE\_MICROPHONE | 0x000701 | 卡拉OK麦克风。 |
| DEVICE\_LAPEL\_MICROPHONE | 0x000702 | 佩戴式话筒。 |
| DEVICE\_WEARABLE\_AUDIO | 0x000800 | 穿戴音频设备。 |
| DEVICE\_IN\_EAR\_EARPHONE | 0x000801 | 入耳式耳机。 |
| DEVICE\_HEADSET | 0x000802 | 头戴式受话器。 |
| DEVICE\_OVER\_EAR\_HEADPHONE | 0x000803 | 头戴式耳机。 |
| DEVICE\_NECKBAND\_EARPHONE | 0x000804 | 颈带式耳机。 |
| DEVICE\_PERSONAL\_CARE | 0x000900 | 个人护理。 |
| DEVICE\_INTELLIGENT\_TOOTHBRUSH | 0x000901 | 智能牙刷。 |
| DEVICE\_SMART\_CUP | 0x000902 | 智能杯。 |
| DEVICE\_INTELLIGENT\_SHAVER | 0x000903 | 智能剃刀。 |
| DEVICE\_HVAC | 0x000A00 | 空调HVAC(Ventilating and Air Conditioning)。 |
| DEVICE\_AIR\_PURIFIER | 0x000A01 | 空气净化器。 |
| DEVICE\_HUMIDIFIER | 0x000A02 | 加湿器。 |
| DEVICE\_AIR\_CIRCULATION\_FAN | 0x000A03 | 空气循环风机。 |
| DEVICE\_ELECTRIC\_RIDE | 0x000B00 | 电动骑行工具。 |
| DEVICE\_ELECTRIC\_SCOOTER | 0x000B01 | 电动滑板车。 |
| DEVICE\_ELECTRIC\_BICYCLE | 0x000B02 | 电动自行车。 |
| DEVICE\_LIGHT\_FITTING | 0x000C00 | 灯具配件。 |
| DEVICE\_SMART\_TABLE\_LAMP | 0x000C01 | 智能台灯。 |
| DEVICE\_REMOTE\_CONTROL | 0x000D00 | 远程控制设备。 |
| DEVICE\_TV\_REMOTE\_CONTROL | 0x000D01 | 电视遥控器。 |
| DEVICE\_IMAGING | 0x000E00 | 成像设备。 |
| DEVICE\_SMART\_TV | 0x000E01 | 智能TV。 |
| DEVICE\_IP\_CAMERA | 0x000E02 | 网络摄像机。 |
| DEVICE\_SCREEN\_CASTER | 0x000E03 | 投影仪。 |
| DEVICE\_NETWORKING | 0x000F00 | 网络设备。 |
| DEVICE\_IOT\_GATEWAY | 0x000F01 | 物联网网关。 |
| DEVICE\_ACCESS\_CONTROL | 0x001000 | 门禁设备。 |
| DEVICE\_INTELLIGENT\_LOCK | 0x001001 | 智能锁。 |
| DEVICE\_SMART\_KEY | 0x001002 | 智能钥匙。 |
| DEVICE\_VEHICLE\_KEY | 0x001003 | 车钥匙。  **起始版本：** 5.1.0(18) |
| DEVICE\_VEHICLE\_LOCK | 0x001004 | 车锁。  **起始版本：** 5.1.0(18) |

## AcbState

PhonePC/2in1TabletTVWearable

表示和远端设备的逻辑链路连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 表示已断连。 |
| CONNECTED | 1 | 表示已连接。 |
| ENCRYPTED | 2 | 表示已加密。 |
