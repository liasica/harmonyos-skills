---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h
title: hid_ddk_types.h
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 头文件 > hid_ddk_types.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:022beeade139630a58b6e1c7261006c08739f96bdece26356e777e41f20f0b69
---

## 概述

提供HID DDK中的枚举变量与结构体定义，支持开发者在驱动开发中定义和操作HID设备，适用于与鼠标、键盘、触摸屏等输入设备交互的场景，提供了设备特性、事件类型、键值编码、坐标轴等完整定义，帮助开发者快速实现HID设备的驱动开发。

**引用文件：** <hid/hid\_ddk\_types.h>

**库：** libhid.z.so

**系统能力：** SystemCapability.Driver.HID.Extension

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Hid\_EmitItem](capi-hidddk-hid-emititem.md) | Hid\_EmitItem | 表示HID事件信息结构体，包含事件类型、事件编码和事件值，用于描述输入设备的上报事件。在驱动开发场景中，该结构体用于传递和识别各类HID设备产生的事件。 |
| [Hid\_Device](capi-hidddk-hid-device.md) | Hid\_Device | 设备基本信息，用于表示HID设备的名称、厂商ID、产品ID等基本属性，在创建和操作HID设备时作为设备标识使用。 |
| [Hid\_EventTypeArray](capi-hidddk-hid-eventtypearray.md) | Hid\_EventTypeArray | 事件类型编码数组，用于存储HID设备支持的事件类型信息。 |
| [Hid\_KeyCodeArray](capi-hidddk-hid-keycodearray.md) | Hid\_KeyCodeArray | 键值属性编码数组，用于存储HID设备支持的键值编码信息。 |
| [Hid\_AbsAxesArray](capi-hidddk-hid-absaxesarray.md) | Hid\_AbsAxesArray | 绝对坐标属性数组，用于存储HID设备的多个绝对坐标轴的属性信息，支持描述如触摸屏、游戏摇杆等输入设备的坐标特征，适用于需要精确读取和处理多维输入数据的驱动开发场景，例如在手柄、触摸板等输入设备中记录轴位数据。 |
| [Hid\_RelAxesArray](capi-hidddk-hid-relaxesarray.md) | Hid\_RelAxesArray | 相对坐标属性编码数组，用于存储HID设备支持的相对坐标属性信息。 |
| [Hid\_MscEventArray](capi-hidddk-hid-msceventarray.md) | Hid\_MscEventArray | 其他特殊事件属性数组，用于存储HID设备支持的特殊事件信息。 |
| [Hid\_EventProperties](capi-hidddk-hid-eventproperties.md) | Hid\_EventProperties | 设备事件属性，包括事件类型、键值、绝对坐标、相对坐标等各类事件属性编码及取值范围。用于HID设备的属性配置，适用于需要精细化管理输入事件的场景。使用结构体前，需根据HID设备规范初始化所有成员变量。 |
| [Hid\_RawDevInfo](capi-hidddk-hid-rawdevinfo.md) | Hid\_RawDevInfo | HID原始设备信息，包含总线类型、供应商ID、产品ID等关键标识信息。开发者可以通过此结构体识别和区分不同的HID设备，通常用于设备识别、设备匹配、设备过滤等场景。 |
| [Hid\_DeviceHandle](capi-hidddk-hid-devicehandle.md) | Hid\_DeviceHandle | 不透明的USB HID设备结构，用于标识和操作HID设备实例。开发者通过该句柄进行HID设备的打开、关闭、读写等操作。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Hid\_DeviceProp](capi-hid-ddk-types-h.md#hid_deviceprop) | Hid\_DeviceProp | 输入设备特性定义。 |
| [Hid\_EventType](capi-hid-ddk-types-h.md#hid_eventtype) | Hid\_EventType | 事件类型。用于标识HID设备产生的事件类别，在驱动开发中用于事件分类和处理。 |
| [Hid\_SynEvent](capi-hid-ddk-types-h.md#hid_synevent) | Hid\_SynEvent | 同步事件编码。 |
| [Hid\_KeyCode](capi-hid-ddk-types-h.md#hid_keycode) | Hid\_KeyCode | 键值编码。包括键盘、鼠标、触摸屏等输入设备的按键和事件编码。 |
| [Hid\_AbsAxes](capi-hid-ddk-types-h.md#hid_absaxes) | Hid\_AbsAxes | 绝对坐标编码。 |
| [Hid\_RelAxes](capi-hid-ddk-types-h.md#hid_relaxes) | Hid\_RelAxes | 相对坐标编码。 |
| [Hid\_MscEvent](capi-hid-ddk-types-h.md#hid_mscevent) | Hid\_MscEvent | 不适合其他类型的输入事件编码。 |
| [Hid\_DdkErrCode](capi-hid-ddk-types-h.md#hid_ddkerrcode) | Hid\_DdkErrCode | HID DDK错误码定义。 |
| [Hid\_ReportType](capi-hid-ddk-types-h.md#hid_reporttype) | Hid\_ReportType | 报告（HID设备与主机之间交换的数据包）类型定义，用于标识HID设备与主机之间通信的数据包类型，在设备通信和数据交换场景中使用。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| HID\_MAX\_REPORT\_BUFFER\_SIZE (16 \* 1024 - 1) | 最大报告缓冲区大小。 **起始版本：** 18 |

## 枚举类型说明

### Hid\_DeviceProp

```c
enum Hid_DeviceProp
```

**描述**

输入设备特性定义。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_PROP\_POINTER = 0x00 | 指针设备。 |
| HID\_PROP\_DIRECT = 0x01 | 直接输入设备。 |
| HID\_PROP\_BUTTON\_PAD = 0x02 | 底部按键触摸设备。 |
| HID\_PROP\_SEMI\_MT = 0x03 | 半多点触控设备。 |
| HID\_PROP\_TOP\_BUTTON\_PAD = 0x04 | 顶部软按键触摸设备。 |
| HID\_PROP\_POINTING\_STICK = 0x05 | 指点杆设备。 |
| HID\_PROP\_ACCELEROMETER = 0x06 | 加速度传感器设备。 |

### Hid\_EventType

```c
enum Hid_EventType
```

**描述**

事件类型。用于标识HID设备产生的事件类别，在驱动开发中用于事件分类和处理。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_EV\_SYN = 0x00 | 同步事件。 |
| HID\_EV\_KEY = 0x01 | 按键事件。 |
| HID\_EV\_REL = 0x02 | 相对坐标事件。 |
| HID\_EV\_ABS = 0x03 | 绝对坐标事件。 |
| HID\_EV\_MSC = 0x04 | 特殊事件。 |

### Hid\_SynEvent

```c
enum Hid_SynEvent
```

**描述**

同步事件编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_SYN\_REPORT = 0 | 表示一个事件的结束。 |
| HID\_SYN\_CONFIG = 1 | 表示配置同步。 |
| HID\_SYN\_MT\_REPORT = 2 | 表示多点触摸的ABS数据包结束。 |
| HID\_SYN\_DROPPED = 3 | 表示该事件被丢弃。 |

### Hid\_KeyCode

```c
enum Hid_KeyCode
```

**描述**

键值编码。包括键盘、鼠标、触摸屏等输入设备的按键和事件编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_KEY\_A = 30 | 键“A”。 |
| HID\_KEY\_B = 48 | 键“B”。 |
| HID\_KEY\_C = 46 | 键“C”。 |
| HID\_KEY\_D = 32 | 键“D”。 |
| HID\_KEY\_E = 18 | 键“E”。 |
| HID\_KEY\_F = 33 | 键“F”。 |
| HID\_KEY\_G = 34 | 键“G”。 |
| HID\_KEY\_H = 35 | 键“H”。 |
| HID\_KEY\_I = 23 | 键“I”。 |
| HID\_KEY\_J = 36 | 键“J”。 |
| HID\_KEY\_K = 37 | 键“K”。 |
| HID\_KEY\_L = 38 | 键“L”。 |
| HID\_KEY\_M = 50 | 键“M”。 |
| HID\_KEY\_N = 49 | 键“N”。 |
| HID\_KEY\_O = 24 | 键“O”。 |
| HID\_KEY\_P = 25 | 键“P”。 |
| HID\_KEY\_Q = 16 | 键“Q”。 |
| HID\_KEY\_R = 19 | 键“R”。 |
| HID\_KEY\_S = 31 | 键“S”。 |
| HID\_KEY\_T = 20 | 键“T”。 |
| HID\_KEY\_U = 22 | 键“U”。 |
| HID\_KEY\_V = 47 | 键“V”。 |
| HID\_KEY\_W = 17 | 键“W”。 |
| HID\_KEY\_X = 45 | 键“X”。 |
| HID\_KEY\_Y = 21 | 键“Y”。 |
| HID\_KEY\_Z = 44 | 键“Z”。 |
| HID\_KEY\_ESC = 1 | 键ESC。 |
| HID\_KEY\_0 = 11 | 键“0”。 |
| HID\_KEY\_1 = 2 | 键“1”。 |
| HID\_KEY\_2 = 3 | 键“2”。 |
| HID\_KEY\_3 = 4 | 键“3”。 |
| HID\_KEY\_4 = 5 | 键“4”。 |
| HID\_KEY\_5 = 6 | 键“5”。 |
| HID\_KEY\_6 = 7 | 键“6”。 |
| HID\_KEY\_7 = 8 | 键“7”。 |
| HID\_KEY\_8 = 9 | 键“8”。 |
| HID\_KEY\_9 = 10 | 键“9”。 |
| HID\_KEY\_GRAVE = 41 | 键“`”。 |
| HID\_KEY\_MINUS = 12 | 键“-”。 |
| HID\_KEY\_EQUALS = 13 | 键“=”。 |
| HID\_KEY\_BACKSPACE = 14 | 键退格。 |
| HID\_KEY\_LEFT\_BRACKET = 26 | 键“[”。 |
| HID\_KEY\_RIGHT\_BRACKET = 27 | 键“]”。 |
| HID\_KEY\_ENTER = 28 | 键回车。 |
| HID\_KEY\_LEFT\_SHIFT = 42 | 键左shift。 |
| HID\_KEY\_BACKSLASH = 43 | 键“\”。 |
| HID\_KEY\_SEMICOLON = 39 | 键“;”。 |
| HID\_KEY\_APOSTROPHE = 40 | 键“'”。 |
| HID\_KEY\_SPACE = 57 | 键空格。 |
| HID\_KEY\_SLASH = 53 | 键“/”。 |
| HID\_KEY\_COMMA = 51 | 键“,”。 |
| HID\_KEY\_PERIOD = 52 | 键“.”。 |
| HID\_KEY\_RIGHT\_SHIFT = 54 | 键右shift。 |
| HID\_KEY\_NUMPAD\_0 = 82 | 数字小键盘的“0”键。 |
| HID\_KEY\_NUMPAD\_1 = 79 | 数字小键盘的“1”键。 |
| HID\_KEY\_NUMPAD\_2 = 80 | 数字小键盘的“2”键。 |
| HID\_KEY\_NUMPAD\_3 = 81 | 数字小键盘的“3”键。 |
| HID\_KEY\_NUMPAD\_4 = 75 | 数字小键盘的“4”键。 |
| HID\_KEY\_NUMPAD\_5 = 76 | 数字小键盘的“5”键。 |
| HID\_KEY\_NUMPAD\_6 = 77 | 数字小键盘的“6”键。 |
| HID\_KEY\_NUMPAD\_7 = 71 | 数字小键盘的“7”键。 |
| HID\_KEY\_NUMPAD\_8 = 72 | 数字小键盘的“8”键。 |
| HID\_KEY\_NUMPAD\_9 = 73 | 数字小键盘的“9”键。 |
| HID\_KEY\_NUMPAD\_DIVIDE = 70 | 数字小键盘的“/”键。 |
| HID\_KEY\_NUMPAD\_MULTIPLY = 55 | 数字小键盘的“\*”键。 |
| HID\_KEY\_NUMPAD\_SUBTRACT = 74 | 数字小键盘的“-”键。 |
| HID\_KEY\_NUMPAD\_ADD = 78 | 数字小键盘的“+”键。 |
| HID\_KEY\_NUMPAD\_DOT = 83 | 数字小键盘的“.”键。 |
| HID\_KEY\_SYSRQ = 99 | 键打印屏幕。 |
| HID\_KEY\_DELETE = 111 | 键删除。 |
| HID\_KEY\_MUTE = 113 | 键静音。 |
| HID\_KEY\_VOLUME\_DOWN = 114 | 键音量-。 |
| HID\_KEY\_VOLUME\_UP = 115 | 键音量+。 |
| HID\_KEY\_BRIGHTNESS\_DOWN = 224 | 键亮度-。 |
| HID\_KEY\_BRIGHTNESS\_UP = 225 | 键亮度+。 |
| HID\_BTN\_0 = 0x100 | 按钮0。 |
| HID\_BTN\_1 = 0x101 | 按钮1。 |
| HID\_BTN\_2 = 0x102 | 按钮2。 |
| HID\_BTN\_3 = 0x103 | 按钮3。 |
| HID\_BTN\_4 = 0x104 | 按钮4。 |
| HID\_BTN\_5 = 0x105 | 按钮5。 |
| HID\_BTN\_6 = 0x106 | 按钮6。 |
| HID\_BTN\_7 = 0x107 | 按钮7。 |
| HID\_BTN\_8 = 0x108 | 按钮8。 |
| HID\_BTN\_9 = 0x109 | 按钮9。 |
| HID\_BTN\_LEFT = 0x110 | 鼠标按键左键。 |
| HID\_BTN\_RIGHT = 0x111 | 鼠标按键右键。 |
| HID\_BTN\_MIDDLE = 0x112 | 鼠标按键中键。 |
| HID\_BTN\_SIDE = 0x113 | 鼠标侧面按键。 |
| HID\_BTN\_EXTRA = 0x114 | 鼠标附加按键。 |
| HID\_BTN\_FORWARD = 0x115 | 鼠标向前按键。 |
| HID\_BTN\_BACKWARD = 0x116 | 鼠标向后按键。 |
| HID\_BTN\_TASK = 0x117 | 鼠标任务按键。 |
| HID\_BTN\_TOOL\_PEN = 0x140 | 画笔。 |
| HID\_BTN\_TOOL\_RUBBER = 0x141 | 橡皮擦。 |
| HID\_BTN\_TOOL\_BRUSH = 0x142 | 笔刷。 |
| HID\_BTN\_TOOL\_PENCIL = 0x143 | 铅笔。 |
| HID\_BTN\_TOOL\_AIRBRUSH = 0x144 | 喷枪。 |
| HID\_BTN\_TOOL\_FINGER = 0x145 | 手指。 |
| HID\_BTN\_TOOL\_MOUSE = 0x146 | 鼠标。 |
| HID\_BTN\_TOOL\_LENS = 0x147 | 镜头。 |
| HID\_BTN\_TOOL\_QUINT\_TAP = 0x148 | 五指触控。 |
| HID\_BTN\_STYLUS3 = 0x149 | 手写笔3。 |
| HID\_BTN\_TOUCH = 0x14a | 触摸。 |
| HID\_BTN\_STYLUS = 0x14b | 手写笔。 |
| HID\_BTN\_STYLUS2 = 0x14c | 手写笔2。 |
| HID\_BTN\_TOOL\_DOUBLE\_TAP = 0x14d | 二指触控。 |
| HID\_BTN\_TOOL\_TRIPLE\_TAP = 0x14e | 三指触控。 |
| HID\_BTN\_TOOL\_QUAD\_TAP = 0x14f | 四指触控。 |
| HID\_BTN\_WHEEL = 0x150 | 滚轮。 |

### Hid\_AbsAxes

```c
enum Hid_AbsAxes
```

**描述**

绝对坐标编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_ABS\_X = 0x00 | X轴。 |
| HID\_ABS\_Y = 0x01 | Y轴。 |
| HID\_ABS\_Z = 0x02 | Z轴。 |
| HID\_ABS\_RX = 0x03 | 右模拟摇杆的 X 轴。 |
| HID\_ABS\_RY = 0x04 | 右模拟摇杆的 Y 轴。 |
| HID\_ABS\_RZ = 0x05 | 右模拟摇杆的 Z 轴。 |
| HID\_ABS\_THROTTLE = 0x06 | 油门控制。 |
| HID\_ABS\_RUDDER = 0x07 | 方向舵。 |
| HID\_ABS\_WHEEL = 0x08 | 滚轮。 |
| HID\_ABS\_GAS = 0x09 | 油门踏板。 |
| HID\_ABS\_BRAKE = 0x0a | 制动。 |
| HID\_ABS\_HAT0X = 0x10 | HAT0X，游戏手柄或操纵器的方向键X轴，表示水平方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT0Y = 0x11 | HAT0Y，游戏手柄或操纵器的方向键Y轴，表示垂直方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT1X = 0x12 | HAT1X，游戏手柄或操纵器的第二个方向键X轴，表示水平方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT1Y = 0x13 | HAT1Y，游戏手柄或操纵器的第二个方向键Y轴，表示垂直方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT2X = 0x14 | HAT2X，游戏手柄或操纵器的第三个方向键X轴，表示水平方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT2Y = 0x15 | HAT2Y，游戏手柄或操纵器的第三个方向键Y轴，表示垂直方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT3X = 0x16 | HAT3X，游戏手柄或操纵器的第四个方向键X轴，表示水平方向的倾斜或旋转角度。 |
| HID\_ABS\_HAT3Y = 0x17 | HAT3Y，游戏手柄或操纵器的第四个方向键Y轴，表示垂直方向的倾斜或旋转角度。 |
| HID\_ABS\_PRESSURE = 0x18 | 压力。 |
| HID\_ABS\_DISTANCE = 0x19 | 距离。 |
| HID\_ABS\_TILT\_X = 0x1a | X轴倾斜度。 |
| HID\_ABS\_TILT\_Y = 0x1b | Y轴倾斜度。 |
| HID\_ABS\_TOOL\_WIDTH = 0x1c | 触摸工具的宽度。 |
| HID\_ABS\_VOLUME = 0x20 | 音量。 |
| HID\_ABS\_MISC = 0x28 | 其他类型的绝对坐标轴，用于不适合归入上述分类的特殊轴类型。 |

### Hid\_RelAxes

```c
enum Hid_RelAxes
```

**描述**

相对坐标编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_REL\_X = 0x00 | X轴。 |
| HID\_REL\_Y = 0x01 | Y轴。 |
| HID\_REL\_Z = 0x02 | Z轴。 |
| HID\_REL\_RX = 0x03 | 右模拟摇杆的 X 轴。 |
| HID\_REL\_RY = 0x04 | 右模拟摇杆的 Y 轴。 |
| HID\_REL\_RZ = 0x05 | 右模拟摇杆的 Z 轴。 |
| HID\_REL\_HWHEEL = 0x06 | 水平滚轮，表示鼠标水平滚轮的滚动方向和距离，用于水平方向的滚动操作。 |
| HID\_REL\_DIAL = 0x07 | 刻度，表示旋钮或刻度盘的旋转方向和距离，用于调节音量、亮度或其他可调节参数。 |
| HID\_REL\_WHEEL = 0x08 | 垂直滚轮，表示鼠标垂直滚轮的滚动方向和距离，用于垂直方向的滚动操作。 |
| HID\_REL\_MISC = 0x09 | 其他类型的相对坐标事件，用于不适合归入上述分类的特殊相对坐标事件。 |
| HID\_REL\_RESERVED = 0x0a | 预留。 |
| HID\_REL\_WHEEL\_HI\_RES = 0x0b | 高分辨率滚轮，表示鼠标高分辨率滚轮的滚动方向和距离，提供比普通滚轮更高的分辨率和精度。 |
| HID\_REL\_HWHEEL\_HI\_RES = 0x0c | 高分辨率水平滚轮，表示鼠标高分辨率水平滚轮的滚动方向和距离，提供比普通水平滚轮更高的分辨率和精度。 |

### Hid\_MscEvent

```c
enum Hid_MscEvent
```

**描述**

不适合其他类型的输入事件编码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_MSC\_SERIAL = 0x00 | 序列号。 |
| HID\_MSC\_PULSE\_LED = 0x01 | 脉冲。 |
| HID\_MSC\_GESTURE = 0x02 | 手势。 |
| HID\_MSC\_RAW = 0x03 | 原始事件。 |
| HID\_MSC\_SCAN = 0x04 | 扫描。 |
| HID\_MSC\_TIMESTAMP = 0x05 | 时间戳。 |

### Hid\_DdkErrCode

```c
enum Hid_DdkErrCode
```

**描述**

HID DDK错误码定义。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| HID\_DDK\_SUCCESS = 0 | 操作成功。 |
| HID\_DDK\_NO\_PERM = 201 | 没有权限，从API 16起，取值由-6变更为201。请检查应用是否已正确获取所需的权限。 |
| HID\_DDK\_INVALID\_PARAMETER = 401 | 非法参数，从API 16起，取值由-2变更为401。请检查参数取值是否符合要求。 |
| HID\_DDK\_FAILURE = 27300001 | DDK接口执行失败，从API 16起，取值由-1变更为27300001。可能原因：设备状态异常或通信异常。请检查设备状态和参数设置。 |
| HID\_DDK\_NULL\_PTR = 27300002 | 空指针异常，从API 16起，取值由-4变更为27300002。请检查传入参数的有效性。 |
| HID\_DDK\_INVALID\_OPERATION = 27300003 | 非法操作，从API 16起，取值由-3变更为27300003。可能原因：调用API的时机或顺序不正确。请检查调用时机、以及是否初始化DDK。 |
| HID\_DDK\_TIMEOUT = 27300004 | 超时，从API 16起，取值由-5变更为27300004。请检查设备状态和超时时间设置。 |
| HID\_DDK\_INIT\_ERROR = 27300005 | 初始化DDK失败或DDK未初始化。请检查系统服务状态，确保在调用API前先初始化DDK。  **起始版本：** 18 |
| HID\_DDK\_SERVICE\_ERROR = 27300006 | 服务通信过程中错误。可能原因：服务内部错误。请检查当前操作和设备状态。  **起始版本：** 18 |
| HID\_DDK\_MEMORY\_ERROR = 27300007 | 内存相关的错误，包括：内存数据拷贝失败、内存申请失败等。请检查内存使用情况和相关参数。  **起始版本：** 18 |
| HID\_DDK\_IO\_ERROR = 27300008 | I/O操作失败。请检查设备状态和传输参数。  **起始版本：** 18 |
| HID\_DDK\_DEVICE\_NOT\_FOUND = 27300009 | 设备未找到。可能原因：设备未连接或设备ID错误。请检查设备是否连接、设备ID是否正确。  **起始版本：** 18 |

### Hid\_ReportType

```c
enum Hid_ReportType
```

**描述**

报告（HID设备与主机之间交换的数据包）类型定义，用于标识HID设备与主机之间通信的数据包类型，在设备通信和数据交换场景中使用。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| HID\_INPUT\_REPORT = 0 | 输入报告，用于设备向主机上报数据。 |
| HID\_OUTPUT\_REPORT = 1 | 输出报告，用于主机向设备发送数据。 |
| HID\_FEATURE\_REPORT = 2 | 特性报告，用于设备配置和状态查询。 |
