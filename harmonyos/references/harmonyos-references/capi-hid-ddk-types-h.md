---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h
title: hid_ddk_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > hid_ddk_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6c5d8ebcc46acc88269f21896fa1507f90e80d29a1e10279b64853e330e6dac0
---

## 概述

PC/2in1

提供HID DDK中的枚举变量与结构体定义。

**引用文件：** <hid/hid\_ddk\_types.h>

**库：** libhid.z.so

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Hid\_EmitItem](capi-hidddk-hid-emititem.md) | Hid\_EmitItem | 事件信息。 |
| [Hid\_Device](capi-hidddk-hid-device.md) | Hid\_Device | 设备基本信息。 |
| [Hid\_EventTypeArray](capi-hidddk-hid-eventtypearray.md) | Hid\_EventTypeArray | 事件类型编码数组。 |
| [Hid\_KeyCodeArray](capi-hidddk-hid-keycodearray.md) | Hid\_KeyCodeArray | 键值属性数组。 |
| [Hid\_AbsAxesArray](capi-hidddk-hid-absaxesarray.md) | Hid\_AbsAxesArray | 绝对坐标属性数组。 |
| [Hid\_RelAxesArray](capi-hidddk-hid-relaxesarray.md) | Hid\_RelAxesArray | 相对坐标属性数组。 |
| [Hid\_MscEventArray](capi-hidddk-hid-msceventarray.md) | Hid\_MscEventArray | 其它特殊事件属性数组。 |
| [Hid\_EventProperties](capi-hidddk-hid-eventproperties.md) | Hid\_EventProperties | 设备关注事件属性。 |
| [Hid\_RawDevInfo](capi-hidddk-hid-rawdevinfo.md) | Hid\_RawDevInfo | 原始设备信息定义。 |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) | Hid\_DeviceHandle | 不透明的USB HID设备结构。 |

### 枚举

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Hid\_DeviceProp](capi-hid-ddk-types-h.md#hid_deviceprop) | Hid\_DeviceProp | 输入设备特性定义。 |
| [Hid\_EventType](capi-hid-ddk-types-h.md#hid_eventtype) | Hid\_EventType | 事件类型。 |
| [Hid\_SynEvent](capi-hid-ddk-types-h.md#hid_synevent) | Hid\_SynEvent | 同步事件编码。 |
| [Hid\_KeyCode](capi-hid-ddk-types-h.md#hid_keycode) | Hid\_KeyCode | 键值编码。 |
| [Hid\_AbsAxes](capi-hid-ddk-types-h.md#hid_absaxes) | Hid\_AbsAxes | 绝对坐标编码。 |
| [Hid\_RelAxes](capi-hid-ddk-types-h.md#hid_relaxes) | Hid\_RelAxes | 相对坐标编码。 |
| [Hid\_MscEvent](capi-hid-ddk-types-h.md#hid_mscevent) | Hid\_MscEvent | 不适合其它类型的输入事件编码。 |
| [Hid\_DdkErrCode](capi-hid-ddk-types-h.md#hid_ddkerrcode) | Hid\_DdkErrCode | HID DDK错误码定义。 |
| [Hid\_ReportType](capi-hid-ddk-types-h.md#hid_reporttype) | Hid\_ReportType | 报告（HID设备与主机之间交换的数据包）类型定义。 |

### 宏定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| HID\_MAX\_REPORT\_BUFFER\_SIZE (16 \* 1024 - 1) | 最大报告缓冲区大小。 |

## 枚举类型说明

PC/2in1

### Hid\_DeviceProp

PC/2in1

```
1. enum Hid_DeviceProp
```

**描述**

输入设备特性定义。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_PROP\_POINTER = 0x00 | 指针设备 |
| HID\_PROP\_DIRECT = 0x01 | 直接输入设备 |
| HID\_PROP\_BUTTON\_PAD = 0x02 | 底部按键触摸设备 |
| HID\_PROP\_SEMI\_MT = 0x03 | 全多点触控设备 |
| HID\_PROP\_TOP\_BUTTON\_PAD = 0x04 | 顶部软按键触摸设备 |
| HID\_PROP\_POINTING\_STICK = 0x05 | 指点杆设备 |
| HID\_PROP\_ACCELEROMETER = 0x06 | 加速度传感器设备 |

### Hid\_EventType

PC/2in1

```
1. enum Hid_EventType
```

**描述**

事件类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_EV\_SYN = 0x00 | 同步事件 |
| HID\_EV\_KEY = 0x01 | 按键事件 |
| HID\_EV\_REL = 0x02 | 相对坐标事件 |
| HID\_EV\_ABS = 0x03 | 绝对坐标事件 |
| HID\_EV\_MSC = 0x04 | 特殊事件 |

### Hid\_SynEvent

PC/2in1

```
1. enum Hid_SynEvent
```

**描述**

同步事件编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_SYN\_REPORT = 0 | 表示一个事件的结束 |
| HID\_SYN\_CONFIG = 1 | 表示配置同步 |
| HID\_SYN\_MT\_REPORT = 2 | 表示多点触摸的ABS数据包结束 |
| HID\_SYN\_DROPPED = 3 | 表示该事件被丢弃 |

### Hid\_KeyCode

PC/2in1

```
1. enum Hid_KeyCode
```

**描述**

键值编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_KEY\_A = 30 | 键A |
| HID\_KEY\_B = 48 | 键B |
| HID\_KEY\_C = 46 | 键C |
| HID\_KEY\_D = 32 | 键D |
| HID\_KEY\_E = 18 | 键E |
| HID\_KEY\_F = 33 | 键F |
| HID\_KEY\_G = 34 | 键G |
| HID\_KEY\_H = 35 | 键H |
| HID\_KEY\_I = 23 | 键I |
| HID\_KEY\_J = 36 | 键J |
| HID\_KEY\_K = 37 | 键K |
| HID\_KEY\_L = 38 | 键L |
| HID\_KEY\_M = 50 | 键M |
| HID\_KEY\_N = 49 | 键N |
| HID\_KEY\_O = 24 | 键O |
| HID\_KEY\_P = 25 | 键P |
| HID\_KEY\_Q = 16 | 键Q |
| HID\_KEY\_R = 19 | 键R |
| HID\_KEY\_S = 31 | 键S |
| HID\_KEY\_T = 20 | 键T |
| HID\_KEY\_U = 22 | 键U |
| HID\_KEY\_V = 47 | 键V |
| HID\_KEY\_W = 17 | 键W |
| HID\_KEY\_X = 45 | 键X |
| HID\_KEY\_Y = 21 | 键Y |
| HID\_KEY\_Z = 44 | 键Z |
| HID\_KEY\_ESC = 1 | 键ESC |
| HID\_KEY\_0 = 11 | 键0 |
| HID\_KEY\_1 = 2 | 键1 |
| HID\_KEY\_2 = 3 | 键2 |
| HID\_KEY\_3 = 4 | 键3 |
| HID\_KEY\_4 = 5 | 键4 |
| HID\_KEY\_5 = 6 | 键5 |
| HID\_KEY\_6 = 7 | 键6 |
| HID\_KEY\_7 = 8 | 键7 |
| HID\_KEY\_8 = 9 | 键8 |
| HID\_KEY\_9 = 10 | 键9 |
| HID\_KEY\_GRAVE = 41 | 键` |
| HID\_KEY\_MINUS = 12 | 键- |
| HID\_KEY\_EQUALS = 13 | 键= |
| HID\_KEY\_BACKSPACE = 14 | 键退格 |
| HID\_KEY\_LEFT\_BRACKET = 26 | 键[ |
| HID\_KEY\_RIGHT\_BRACKET = 27 | 键] |
| HID\_KEY\_ENTER = 28 | 键回车 |
| HID\_KEY\_LEFT\_SHIFT = 42 | 键左shift |
| HID\_KEY\_BACKSLASH = 43 | 键\ |
| HID\_KEY\_SEMICOLON = 39 | 键; |
| HID\_KEY\_APOSTROPHE = 40 | 键' |
| HID\_KEY\_SPACE = 57 | 键空格 |
| HID\_KEY\_SLASH = 53 | 键 |
| HID\_KEY\_COMMA = 51 | 键, |
| HID\_KEY\_PERIOD = 52 | 键. |
| HID\_KEY\_RIGHT\_SHIFT = 54 | 键右shift |
| HID\_KEY\_NUMPAD\_0 = 82 | 数字键0 |
| HID\_KEY\_NUMPAD\_1 = 79 | 数字键1 |
| HID\_KEY\_NUMPAD\_2 = 80 | 数字键2 |
| HID\_KEY\_NUMPAD\_3 = 81 | 数字键3 |
| HID\_KEY\_NUMPAD\_4 = 75 | 数字键4 |
| HID\_KEY\_NUMPAD\_5 = 76 | 数字键5 |
| HID\_KEY\_NUMPAD\_6 = 77 | 数字键6 |
| HID\_KEY\_NUMPAD\_7 = 71 | 数字键7 |
| HID\_KEY\_NUMPAD\_8 = 72 | 数字键8 |
| HID\_KEY\_NUMPAD\_9 = 73 | 数字键9 |
| HID\_KEY\_NUMPAD\_DIVIDE = 70 | 数字键 |
| HID\_KEY\_NUMPAD\_MULTIPLY = 55 | 数字键 |
| HID\_KEY\_NUMPAD\_SUBTRACT = 74 | 数字键- |
| HID\_KEY\_NUMPAD\_ADD = 78 | 数字键+ |
| HID\_KEY\_NUMPAD\_DOT = 83 | 数字键. |
| HID\_KEY\_SYSRQ = 99 | 键打印屏幕 |
| HID\_KEY\_DELETE = 111 | 键删除 |
| HID\_KEY\_MUTE = 113 | 键静音 |
| HID\_KEY\_VOLUME\_DOWN = 114 | 键音量- |
| HID\_KEY\_VOLUME\_UP = 115 | 键音量+ |
| HID\_KEY\_BRIGHTNESS\_DOWN = 224 | 键亮度- |
| HID\_KEY\_BRIGHTNESS\_UP = 225 | 键亮度+ |
| HID\_BTN\_0 = 0x100 | 按钮0 |
| HID\_BTN\_1 = 0x101 | 按钮1 |
| HID\_BTN\_2 = 0x102 | 按钮2 |
| HID\_BTN\_3 = 0x103 | 按钮3 |
| HID\_BTN\_4 = 0x104 | 按钮4 |
| HID\_BTN\_5 = 0x105 | 按钮5 |
| HID\_BTN\_6 = 0x106 | 按钮6 |
| HID\_BTN\_7 = 0x107 | 按钮7 |
| HID\_BTN\_8 = 0x108 | 按钮8 |
| HID\_BTN\_9 = 0x109 | 按钮9 |
| HID\_BTN\_LEFT = 0x110 | 鼠标按键左键 |
| HID\_BTN\_RIGHT = 0x111 | 鼠标按键右键 |
| HID\_BTN\_MIDDLE = 0x112 | 鼠标按键中键 |
| HID\_BTN\_SIDE = 0x113 | 鼠标侧面按键 |
| HID\_BTN\_EXTRA = 0x114 | 鼠标附加按键 |
| HID\_BTN\_FORWARD = 0x115 | 鼠标向前按键 |
| HID\_BTN\_BACKWARD = 0x116 | 鼠标向后按键 |
| HID\_BTN\_TASK = 0x117 | 鼠标任务按键 |
| HID\_BTN\_TOOL\_PEN = 0x140 | 画笔 |
| HID\_BTN\_TOOL\_RUBBER = 0x141 | 橡皮擦 |
| HID\_BTN\_TOOL\_BRUSH = 0x142 | 笔刷 |
| HID\_BTN\_TOOL\_PENCIL = 0x143 | 钢笔 |
| HID\_BTN\_TOOL\_AIRBRUSH = 0x144 | 喷枪 |
| HID\_BTN\_TOOL\_FINGER = 0x145 | 手指 |
| HID\_BTN\_TOOL\_MOUSE = 0x146 | 鼠标 |
| HID\_BTN\_TOOL\_LENS = 0x147 | 镜头 |
| HID\_BTN\_TOOL\_QUINT\_TAP = 0x148 | 五指触控 |
| HID\_BTN\_STYLUS3 = 0x149 | 手写笔3 |
| HID\_BTN\_TOUCH = 0x14a | 触摸 |
| HID\_BTN\_STYLUS = 0x14b | 手写笔 |
| HID\_BTN\_STYLUS2 = 0x14c | 手写笔2 |
| HID\_BTN\_TOOL\_DOUBLE\_TAP = 0x14d | 二指触控 |
| HID\_BTN\_TOOL\_TRIPLE\_TAP = 0x14e | 三指触控 |
| HID\_BTN\_TOOL\_QUAD\_TAP = 0x14f | 四指触控 |
| HID\_BTN\_WHEEL = 0x150 | 滚轮 |

### Hid\_AbsAxes

PC/2in1

```
1. enum Hid_AbsAxes
```

**描述**

绝对坐标编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_ABS\_X = 0x00 | X轴 |
| HID\_ABS\_Y = 0x01 | Y轴 |
| HID\_ABS\_Z = 0x02 | Z轴 |
| HID\_ABS\_RX = 0x03 | 右模拟摇杆的 X 轴 |
| HID\_ABS\_RY = 0x04 | 右模拟摇杆的 Y 轴 |
| HID\_ABS\_RZ = 0x05 | 右模拟摇杆的 Z 轴 |
| HID\_ABS\_THROTTLE = 0x06 | 油门 |
| HID\_ABS\_RUDDER = 0x07 | 舵 |
| HID\_ABS\_WHEEL = 0x08 | 滚轮 |
| HID\_ABS\_GAS = 0x09 | 气 |
| HID\_ABS\_BRAKE = 0x0a | 制动 |
| HID\_ABS\_HAT0X = 0x10 | HAT0X |
| HID\_ABS\_HAT0Y = 0x11 | HAT0Y |
| HID\_ABS\_HAT1X = 0x12 | HAT1X |
| HID\_ABS\_HAT1Y = 0x13 | HAT1Y |
| HID\_ABS\_HAT2X = 0x14 | HAT2X |
| HID\_ABS\_HAT2Y = 0x15 | HAT2Y |
| HID\_ABS\_HAT3X = 0x16 | HAT3X |
| HID\_ABS\_HAT3Y = 0x17 | HAT3Y |
| HID\_ABS\_PRESSURE = 0x18 | 压力 |
| HID\_ABS\_DISTANCE = 0x19 | 距离 |
| HID\_ABS\_TILT\_X = 0x1a | X轴倾斜度 |
| HID\_ABS\_TILT\_Y = 0x1b | Y轴倾斜度 |
| HID\_ABS\_TOOL\_WIDTH = 0x1c | 触摸工具的宽度 |
| HID\_ABS\_VOLUME = 0x20 | 音量 |
| HID\_ABS\_MISC = 0x28 | 其它 |

### Hid\_RelAxes

PC/2in1

```
1. enum Hid_RelAxes
```

**描述**

相对坐标编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_REL\_X = 0x00 | X轴 |
| HID\_REL\_Y = 0x01 | Y轴 |
| HID\_REL\_Z = 0x02 | Z轴 |
| HID\_REL\_RX = 0x03 | 右模拟摇杆的 X 轴 |
| HID\_REL\_RY = 0x04 | 右模拟摇杆的 Y 轴 |
| HID\_REL\_RZ = 0x05 | 右模拟摇杆的 Z 轴 |
| HID\_REL\_HWHEEL = 0x06 | 水平滚轮 |
| HID\_REL\_DIAL = 0x07 | 刻度 |
| HID\_REL\_WHEEL = 0x08 | 滚轮 |
| HID\_REL\_MISC = 0x09 | 其它 |
| HID\_REL\_RESERVED = 0x0a | 预留 |
| HID\_REL\_WHEEL\_HI\_RES = 0x0b | 高分辨率滚轮 |
| HID\_REL\_HWHEEL\_HI\_RES = 0x0c | 高分辨率水平滚轮 |

### Hid\_MscEvent

PC/2in1

```
1. enum Hid_MscEvent
```

**描述**

不适合其它类型的输入事件编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_MSC\_SERIAL = 0x00 | 序列号 |
| HID\_MSC\_PULSE\_LED = 0x01 | 脉冲 |
| HID\_MSC\_GESTURE = 0x02 | 手势 |
| HID\_MSC\_RAW = 0x03 | 开始事件 |
| HID\_MSC\_SCAN = 0x04 | 扫描 |
| HID\_MSC\_TIMESTAMP = 0x05 | 时间戳 |

### Hid\_DdkErrCode

PC/2in1

```
1. enum Hid_DdkErrCode
```

**描述**

HID DDK错误码定义。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_DDK\_SUCCESS = 0 | 操作成功。 |
| HID\_DDK\_NO\_PERM = 201 | 没有权限，从API 16起，取值由-6变更为201。 |
| HID\_DDK\_INVALID\_PARAMETER = 401 | 非法参数，从API 16起，取值由-2变更为401。 |
| HID\_DDK\_FAILURE = 27300001 | 操作失败，从API 16起，取值由-1变更为27300001。 |
| HID\_DDK\_NULL\_PTR = 27300002 | 空指针异常，从API 16起，取值由-4变更为27300002。 |
| HID\_DDK\_INVALID\_OPERATION = 27300003 | 非法操作，从API 16起，取值由-3变更为27300003。 |
| HID\_DDK\_TIMEOUT = 27300004 | 超时，从API 16起，取值由-5变更为27300004。 |
| HID\_DDK\_INIT\_ERROR = 27300005 | 初始化DDK失败或DDK未初始化。  **起始版本：** 18 |
| HID\_DDK\_SERVICE\_ERROR = 27300006 | 服务通信过程中错误。  **起始版本：** 18 |
| HID\_DDK\_MEMORY\_ERROR = 27300007 | 内存相关的错误，包括：内存数据拷贝失败、内存申请失败等。  **起始版本：** 18 |
| HID\_DDK\_IO\_ERROR = 27300008 | I/O操作失败。  **起始版本：** 18 |
| HID\_DDK\_DEVICE\_NOT\_FOUND = 27300009 | 设备未找到。  **起始版本：** 18 |

### Hid\_ReportType

PC/2in1

```
1. enum Hid_ReportType
```

**描述**

报告（HID设备与主机之间交换的数据包）类型定义。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| HID\_INPUT\_REPORT = 0 | 输入报告 |
| HID\_OUTPUT\_REPORT = 1 | 输出报告 |
| HID\_FEATURE\_REPORT = 2 | 特性报告 |

### HID\_MAX\_REPORT\_BUFFER\_SIZE

PC/2in1

```
1. HID_MAX_REPORT_BUFFER_SIZE (16 * 1024 - 1)
```

**描述**

最大报告缓冲区大小。

**起始版本：** 18
