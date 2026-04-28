---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-key-event-h
title: native_key_event.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_key_event.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:789c87501700e2389385f88bd62a18bdd31d202e5864c9a2e723c1c84de8922b
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeKeyEvent相关接口定义。

**引用文件：** <arkui/native\_key\_event.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NdkKeyEvent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NdkKeyEvent)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_KeyCode](capi-native-key-event-h.md#arkui_keycode) | ArkUI\_KeyCode | 按键事件的键码。 |
| [ArkUI\_KeyEventType](capi-native-key-event-h.md#arkui_keyeventtype) | ArkUI\_KeyEventType | 按键的类型。 |
| [ArkUI\_KeySourceType](capi-native-key-event-h.md#arkui_keysourcetype) | ArkUI\_KeySourceType | 触发当前按键的输入设备类型。 |
| [ArkUI\_KeyIntension](capi-native-key-event-h.md#arkui_keyintension) | ArkUI\_KeyIntension | 按键对应的意图。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_KeyEventType OH\_ArkUI\_KeyEvent\_GetType(const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_gettype) | 获取按键的类型。 |
| [int32\_t OH\_ArkUI\_KeyEvent\_GetKeyCode(const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_getkeycode) | 获取按键的键码。 |
| [const char OH\_ArkUI\_KeyEvent\_GetKeyText(const ArkUI\_UIInputEvent event)](capi-native-key-event-h.md#oh_arkui_keyevent_getkeytext) | 获取按键的键值。 |
| [ArkUI\_KeySourceType OH\_ArkUI\_KeyEvent\_GetKeySource(const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_getkeysource) | 获取当前按键的输入设备类型。 |
| [void OH\_ArkUI\_KeyEvent\_StopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](capi-native-key-event-h.md#oh_arkui_keyevent_stoppropagation) | 阻塞事件冒泡传递。 |
| [ArkUI\_KeyIntension OH\_ArkUI\_KeyEvent\_GetKeyIntensionCode(const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_getkeyintensioncode) | 获取按键对应的意图。 |
| [uint32\_t OH\_ArkUI\_KeyEvent\_GetUnicode(const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_getunicode) | 获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。 |
| [void OH\_ArkUI\_KeyEvent\_SetConsumed(const ArkUI\_UIInputEvent\* event, bool isConsumed)](capi-native-key-event-h.md#oh_arkui_keyevent_setconsumed) | 在按键事件回调中，设置事件是否被该回调消费。 |
| [void OH\_ArkUI\_KeyEvent\_Dispatch(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)](capi-native-key-event-h.md#oh_arkui_keyevent_dispatch) | 将按键事件分发到特定组件节点。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsNumLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](capi-native-key-event-h.md#oh_arkui_keyevent_isnumlockon) | 获取按键事件发生时NumLock的状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsCapsLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](capi-native-key-event-h.md#oh_arkui_keyevent_iscapslockon) | 获取按键事件发生时CapsLock的状态。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsScrollLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](capi-native-key-event-h.md#oh_arkui_keyevent_isscrolllockon) | 获取按键事件发生时ScrollLock的状态。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_KeyCode

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyCode
```

**描述：**

按键事件的键码。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEYCODE\_UNKNOWN = -1 | 未知按键。 |
| ARKUI\_KEYCODE\_FN = 0 | 功能（Fn）键。 |
| ARKUI\_KEYCODE\_VOLUME\_UP = 16 | 音量增加键。 |
| ARKUI\_KEYCODE\_VOLUME\_DOWN = 17 | 音量减小键。 |
| ARKUI\_KEYCODE\_POWER = 18 | 电源键。 |
| ARKUI\_KEYCODE\_CAMERA = 19 | 拍照键。 |
| ARKUI\_KEYCODE\_VOLUME\_MUTE = 22 | 扬声器静音键。 |
| ARKUI\_KEYCODE\_MUTE = 23 | 话筒静音键。 |
| ARKUI\_KEYCODE\_BRIGHTNESS\_UP = 40 | 亮度调节按键，调亮。 |
| ARKUI\_KEYCODE\_BRIGHTNESS\_DOWN = 41 | 亮度调节按键，调暗。 |
| ARKUI\_KEYCODE\_0 = 2000 | 按键'0'。 |
| ARKUI\_KEYCODE\_1 = 2001 | 按键'1'。 |
| ARKUI\_KEYCODE\_2 = 2002 | 按键'2'。 |
| ARKUI\_KEYCODE\_3 = 2003 | 按键'3'。 |
| ARKUI\_KEYCODE\_4 = 2004 | 按键'4'。 |
| ARKUI\_KEYCODE\_5 = 2005 | 按键'5'。 |
| ARKUI\_KEYCODE\_6 = 2006 | 按键'6'。 |
| ARKUI\_KEYCODE\_7 = 2007 | 按键'7'。 |
| ARKUI\_KEYCODE\_8 = 2008 | 按键'8'。 |
| ARKUI\_KEYCODE\_9 = 2009 | 按键'9'。 |
| ARKUI\_KEYCODE\_STAR = 2010 | 按键'\*'。 |
| ARKUI\_KEYCODE\_POUND = 2011 | 按键'#'。 |
| ARKUI\_KEYCODE\_DPAD\_UP = 2012 | 导航键，向上。 |
| ARKUI\_KEYCODE\_DPAD\_DOWN = 2013 | 导航键，向下。 |
| ARKUI\_KEYCODE\_DPAD\_LEFT = 2014 | 导航键，向左。 |
| ARKUI\_KEYCODE\_DPAD\_RIGHT = 2015 | 导航键，向右。 |
| ARKUI\_KEYCODE\_DPAD\_CENTER = 2016 | 导航键，确定键。 |
| ARKUI\_KEYCODE\_A = 2017 | 按键'A'。 |
| ARKUI\_KEYCODE\_B = 2018 | 按键'B'。 |
| ARKUI\_KEYCODE\_C = 2019 | 按键'C'。 |
| ARKUI\_KEYCODE\_D = 2020 | 按键'D'。 |
| ARKUI\_KEYCODE\_E = 2021 | 按键'E'。 |
| ARKUI\_KEYCODE\_F = 2022 | 按键'F'。 |
| ARKUI\_KEYCODE\_G = 2023 | 按键'G'。 |
| ARKUI\_KEYCODE\_H = 2024 | 按键'H'。 |
| ARKUI\_KEYCODE\_I = 2025 | 按键'I'。 |
| ARKUI\_KEYCODE\_J = 2026 | 按键'J'。 |
| ARKUI\_KEYCODE\_K = 2027 | 按键'K'。 |
| ARKUI\_KEYCODE\_L = 2028 | 按键'L'。 |
| ARKUI\_KEYCODE\_M = 2029 | 按键'M'。 |
| ARKUI\_KEYCODE\_N = 2030 | 按键'N'。 |
| ARKUI\_KEYCODE\_O = 2031 | 按键'O'。 |
| ARKUI\_KEYCODE\_P = 2032 | 按键'P'。 |
| ARKUI\_KEYCODE\_Q = 2033 | 按键'Q'。 |
| ARKUI\_KEYCODE\_R = 2034 | 按键'R'。 |
| ARKUI\_KEYCODE\_S = 2035 | 按键'S'。 |
| ARKUI\_KEYCODE\_T = 2036 | 按键'T'。 |
| ARKUI\_KEYCODE\_U = 2037 | 按键'U'。 |
| ARKUI\_KEYCODE\_V = 2038 | 按键'V'。 |
| ARKUI\_KEYCODE\_W = 2039 | 按键'W'。 |
| ARKUI\_KEYCODE\_X = 2040 | 按键'X'。 |
| ARKUI\_KEYCODE\_Y = 2041 | 按键'Y'。 |
| ARKUI\_KEYCODE\_Z = 2042 | 按键'Z'。 |
| ARKUI\_KEYCODE\_COMMA = 2043 | 按键','。 |
| ARKUI\_KEYCODE\_PERIOD = 2044 | 按键'.'。 |
| ARKUI\_KEYCODE\_ALT\_LEFT = 2045 | 左Alt键。 |
| ARKUI\_KEYCODE\_ALT\_RIGHT = 2046 | 右Alt键。 |
| ARKUI\_KEYCODE\_SHIFT\_LEFT = 2047 | 左Shift键。 |
| ARKUI\_KEYCODE\_SHIFT\_RIGHT = 2048 | 右Shift键。 |
| ARKUI\_KEYCODE\_TAB = 2049 | Tab键。 |
| ARKUI\_KEYCODE\_SPACE = 2050 | 空格键。 |
| ARKUI\_KEYCODE\_SYM = 2051 | 符号修改器按键。 |
| ARKUI\_KEYCODE\_EXPLORER = 2052 | 浏览器功能键，此键用于启动浏览器应用程序。 |
| ARKUI\_KEYCODE\_ENVELOPE = 2053 | 电子邮件功能键，此键用于启动电子邮件应用程序。 |
| ARKUI\_KEYCODE\_ENTER = 2054 | 回车键。 |
| ARKUI\_KEYCODE\_DEL = 2055 | 退格键。 |
| ARKUI\_KEYCODE\_GRAVE = 2056 | 按键'`'。 |
| ARKUI\_KEYCODE\_MINUS = 2057 | 按键'-'。 |
| ARKUI\_KEYCODE\_EQUALS = 2058 | 按键'='。 |
| ARKUI\_KEYCODE\_LEFT\_BRACKET = 2059 | 按键'['。 |
| ARKUI\_KEYCODE\_RIGHT\_BRACKET = 2060 | 按键']'。 |
| ARKUI\_KEYCODE\_BACKSLASH = 2061 | 按键'\'。 |
| ARKUI\_KEYCODE\_SEMICOLON = 2062 | 按键';'。 |
| ARKUI\_KEYCODE\_APOSTROPHE = 2063 | 按键''' (单引号)。 |
| ARKUI\_KEYCODE\_SLASH = 2064 | 按键'/'。 |
| ARKUI\_KEYCODE\_AT = 2065 | 按键'@'。 |
| ARKUI\_KEYCODE\_PLUS = 2066 | 按键'+'。 |
| ARKUI\_KEYCODE\_MENU = 2067 | 菜单键。 |
| ARKUI\_KEYCODE\_PAGE\_UP = 2068 | 向上翻页键。 |
| ARKUI\_KEYCODE\_PAGE\_DOWN = 2069 | 向下翻页键。 |
| ARKUI\_KEYCODE\_ESCAPE = 2070 | ESC键。 |
| ARKUI\_KEYCODE\_FORWARD\_DEL = 2071 | 删除键。 |
| ARKUI\_KEYCODE\_CTRL\_LEFT = 2072 | 左Ctrl键。 |
| ARKUI\_KEYCODE\_CTRL\_RIGHT = 2073 | 右Ctrl键。 |
| ARKUI\_KEYCODE\_CAPS\_LOCK = 2074 | 大写锁定键。 |
| ARKUI\_KEYCODE\_SCROLL\_LOCK = 2075 | 滚动锁定键。 |
| ARKUI\_KEYCODE\_META\_LEFT = 2076 | 左元修改器键。 |
| ARKUI\_KEYCODE\_META\_RIGHT = 2077 | 右元修改器键。 |
| ARKUI\_KEYCODE\_FUNCTION = 2078 | 功能键。 |
| ARKUI\_KEYCODE\_SYSRQ = 2079 | 系统请求/打印屏幕键。 |
| ARKUI\_KEYCODE\_BREAK = 2080 | Break/Pause键。 |
| ARKUI\_KEYCODE\_MOVE\_HOME = 2081 | 光标移动到开始键。 |
| ARKUI\_KEYCODE\_MOVE\_END = 2082 | 光标移动到末尾键。 |
| ARKUI\_KEYCODE\_INSERT = 2083 | 插入键。 |
| ARKUI\_KEYCODE\_FORWARD = 2084 | 前进键。 |
| ARKUI\_KEYCODE\_MEDIA\_PLAY = 2085 | 多媒体键，播放。 |
| ARKUI\_KEYCODE\_MEDIA\_PAUSE = 2086 | 多媒体键，暂停。 |
| ARKUI\_KEYCODE\_MEDIA\_CLOSE = 2087 | 多媒体键，关闭。 |
| ARKUI\_KEYCODE\_MEDIA\_EJECT = 2088 | 多媒体键，弹出。 |
| ARKUI\_KEYCODE\_MEDIA\_RECORD = 2089 | 多媒体键，录音。 |
| ARKUI\_KEYCODE\_F1 = 2090 | 按键'F1'。 |
| ARKUI\_KEYCODE\_F2 = 2091 | 按键'F2'。 |
| ARKUI\_KEYCODE\_F3 = 2092 | 按键'F3'。 |
| ARKUI\_KEYCODE\_F4 = 2093 | 按键'F4'。 |
| ARKUI\_KEYCODE\_F5 = 2094 | 按键'F5'。 |
| ARKUI\_KEYCODE\_F6 = 2095 | 按键'F6'。 |
| ARKUI\_KEYCODE\_F7 = 2096 | 按键'F7'。 |
| ARKUI\_KEYCODE\_F8 = 2097 | 按键'F8'。 |
| ARKUI\_KEYCODE\_F9 = 2098 | 按键'F9'。 |
| ARKUI\_KEYCODE\_F10 = 2099 | 按键'F10'。 |
| ARKUI\_KEYCODE\_F11 = 2100 | 按键'F11'。 |
| ARKUI\_KEYCODE\_F12 = 2101 | 按键'F12'。 |
| ARKUI\_KEYCODE\_NUM\_LOCK = 2102 | 小键盘锁。 |
| ARKUI\_KEYCODE\_NUMPAD\_0 = 2103 | 小键盘按键'0'。 |
| ARKUI\_KEYCODE\_NUMPAD\_1 = 2104 | 小键盘按键'1'。 |
| ARKUI\_KEYCODE\_NUMPAD\_2 = 2105 | 小键盘按键'2'。 |
| ARKUI\_KEYCODE\_NUMPAD\_3 = 2106 | 小键盘按键'3'。 |
| ARKUI\_KEYCODE\_NUMPAD\_4 = 2107 | 小键盘按键'4'。 |
| ARKUI\_KEYCODE\_NUMPAD\_5 = 2108 | 小键盘按键'5'。 |
| ARKUI\_KEYCODE\_NUMPAD\_6 = 2109 | 小键盘按键'6'。 |
| ARKUI\_KEYCODE\_NUMPAD\_7 = 2110 | 小键盘按键'7'。 |
| ARKUI\_KEYCODE\_NUMPAD\_8 = 2111 | 小键盘按键'8'。 |
| ARKUI\_KEYCODE\_NUMPAD\_9 = 2112 | 小键盘按键'9'。 |
| ARKUI\_KEYCODE\_NUMPAD\_DIVIDE = 2113 | 小键盘按键'/'。 |
| ARKUI\_KEYCODE\_NUMPAD\_MULTIPLY = 2114 | 小键盘按键'\*'。 |
| ARKUI\_KEYCODE\_NUMPAD\_SUBTRACT = 2115 | 小键盘按键'-'。 |
| ARKUI\_KEYCODE\_NUMPAD\_ADD = 2116 | 小键盘按键'+'。 |
| ARKUI\_KEYCODE\_NUMPAD\_DOT = 2117 | 小键盘按键'.'。 |
| ARKUI\_KEYCODE\_NUMPAD\_COMMA = 2118 | 小键盘按键','。 |
| ARKUI\_KEYCODE\_NUMPAD\_ENTER = 2119 | 小键盘按键回车。 |
| ARKUI\_KEYCODE\_NUMPAD\_EQUALS = 2120 | 小键盘按键'='。 |
| ARKUI\_KEYCODE\_NUMPAD\_LEFT\_PAREN = 2121 | 小键盘按键'('。 |
| ARKUI\_KEYCODE\_NUMPAD\_RIGHT\_PAREN = 2122 | 小键盘按键')'。 |
| ARKUI\_KEYCODE\_BUTTON\_A = 2301 | 游戏手柄按键'A'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_B = 2302 | 游戏手柄按键'B'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_X = 2304 | 游戏手柄按键'X'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_Y = 2305 | 游戏手柄按键'Y'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_L1 = 2307 | 游戏手柄按键'L1'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_R1 = 2308 | 游戏手柄按键'R1'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_L2 = 2309 | 游戏手柄按键'L2'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_R2 = 2310 | 游戏手柄按键'R2'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_SELECT = 2311 | 游戏手柄按键'Select'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_START = 2312 | 游戏手柄按键'Start'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_MODE = 2313 | 游戏手柄按键'Mode'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_THUMBL = 2314 | 游戏手柄按键'THUMBL'。  **起始版本：** 15 |
| ARKUI\_KEYCODE\_BUTTON\_THUMBR = 2315 | 游戏手柄按键'THUMBR'。  **起始版本：** 15 |

### ArkUI\_KeyEventType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyEventType
```

**描述：**

按键的类型。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEY\_EVENT\_UNKNOWN = -1 | 未知类型。 |
| ARKUI\_KEY\_EVENT\_DOWN = 0 | 按键按下。 |
| ARKUI\_KEY\_EVENT\_UP = 1 | 按键松开。 |
| ARKUI\_KEY\_EVENT\_LONG\_PRESS = 2 | 按键长按。 |
| ARKUI\_KEY\_EVENT\_CLICK = 3 | 按键点击。 |

### ArkUI\_KeySourceType

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeySourceType
```

**描述：**

触发当前按键的输入设备类型。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEY\_SOURCE\_UNKNOWN = 0 | 未知类型。 |
| ARKUI\_KEY\_SOURCE\_TYPE\_MOUSE = 1 | 鼠标。 |
| ARKUI\_KEY\_SOURCE\_TYPE\_KEYBOARD = 4 | 键盘。 |
| ARKUI\_KEY\_SOURCE\_TYPE\_JOYSTICK = 5 | 游戏手柄。  **起始版本：** 15 |

### ArkUI\_KeyIntension

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_KeyIntension
```

**描述：**

按键对应的意图。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_KEY\_INTENSION\_UNKNOWN = -1 | 未知意图。 |
| ARKUI\_KEY\_INTENSION\_UP = 1 | 向上。 |
| ARKUI\_KEY\_INTENSION\_DOWN = 2 | 向下。 |
| ARKUI\_KEY\_INTENSION\_LEFT = 3 | 向左。 |
| ARKUI\_KEY\_INTENSION\_RIGHT = 4 | 向右。 |
| ARKUI\_KEY\_INTENSION\_SELECT = 5 | 选中。 |
| ARKUI\_KEY\_INTENSION\_ESCAPE = 6 | 返回。 |
| ARKUI\_KEY\_INTENSION\_BACK = 7 | 后退。 |
| ARKUI\_KEY\_INTENSION\_FORWARD = 8 | 前进。 |
| ARKUI\_KEY\_INTENSION\_MENU = 9 | 菜单。 |
| ARKUI\_KEY\_INTENSION\_HOME = 10 | 主页。 |
| ARKUI\_KEY\_INTENSION\_PAGE\_UP = 11 | 上一页。 |
| ARKUI\_KEY\_INTENSION\_PAGE\_DOWN = 12 | 下一页。 |
| ARKUI\_KEY\_INTENSION\_ZOOM\_OUT = 13 | 缩小。 |
| ARKUI\_KEY\_INTENSION\_ZOOM\_IN = 14 | 放大。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_PLAY\_PAUSE = 100 | 播放。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_FAST\_FORWARD = 101 | 快进。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_FAST\_PLAYBACK = 103 | 快速播放。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_NEXT = 104 | 下一首。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_PREVIOUS = 105 | 上一首。 |
| ARKUI\_KEY\_INTENTION\_MEDIA\_MUTE = 106 | 静音。 |
| ARKUI\_KEY\_INTENTION\_VOLUME\_UP = 107 | 音量增加。 |
| ARKUI\_KEY\_INTENTION\_VOLUME\_DOWN = 108 | 音量降低。 |
| ARKUI\_KEY\_INTENTION\_CALL = 200 | 接听电话。 |
| ARKUI\_KEY\_INTENTION\_CAMERA = 300 | 拍照。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_KeyEvent\_GetType()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_KeyEventType OH_ArkUI_KeyEvent_GetType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的类型。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_KeyEventType](capi-native-key-event-h.md#arkui_keyeventtype) | ArkUI\_KeyEventType 按键的类型。 |

### OH\_ArkUI\_KeyEvent\_GetKeyCode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_ArkUI_KeyEvent_GetKeyCode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的键码。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 按键的键码。 |

### OH\_ArkUI\_KeyEvent\_GetKeyText()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_ArkUI_KeyEvent_GetKeyText(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的键值。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 按键的键值。 |

### OH\_ArkUI\_KeyEvent\_GetKeySource()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_KeySourceType OH_ArkUI_KeyEvent_GetKeySource(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前按键的输入设备类型。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_KeySourceType](capi-native-key-event-h.md#arkui_keysourcetype) | ArkUI\_KeySourceType 当前按键的输入设备类型。 |

### OH\_ArkUI\_KeyEvent\_StopPropagation()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_KeyEvent_StopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

阻塞事件冒泡传递。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| bool stopPropagation | 表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。 |

### OH\_ArkUI\_KeyEvent\_GetKeyIntensionCode()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_KeyIntension OH_ArkUI_KeyEvent_GetKeyIntensionCode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键对应的意图。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_KeyIntension](capi-native-key-event-h.md#arkui_keyintension) | ArkUI\_KeyIntension 按键对应的意图。 |

### OH\_ArkUI\_KeyEvent\_GetUnicode()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_ArkUI_KeyEvent_GetUnicode(const ArkUI_UIInputEvent* event)
```

**描述：**

获取按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | Unicode码值。 |

### OH\_ArkUI\_KeyEvent\_SetConsumed()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_KeyEvent_SetConsumed(const ArkUI_UIInputEvent* event, bool isConsumed)
```

**描述：**

在按键事件回调中，设置事件是否被该回调消费。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| bool isConsumed | 事件是否被该回调消费。true表示事件被消费，false表示事件未被消费。 |

### OH\_ArkUI\_KeyEvent\_Dispatch()

PhonePC/2in1TabletTVWearable

```
1. void OH_ArkUI_KeyEvent_Dispatch(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)
```

**描述：**

将按键事件分发到特定组件节点。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md) node | 指定的节点。 |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |

### OH\_ArkUI\_KeyEvent\_IsNumLockOn()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsNumLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时NumLock的状态。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| bool\* state | 输出参数，返回NumLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyEvent\_IsCapsLockOn()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsCapsLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时CapsLock的状态。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| bool\* state | 输出参数，返回CapsLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### OH\_ArkUI\_KeyEvent\_IsScrollLockOn()

PhonePC/2in1TabletTVWearable

```
1. ArkUI_ErrorCode OH_ArkUI_KeyEvent_IsScrollLockOn(const ArkUI_UIInputEvent* event, bool* state)
```

**描述：**

获取按键事件发生时ScrollLock的状态。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ArkUI\_UIInputEvent](capi-arkui-eventmodule-arkui-uiinputevent.md)\* event | ArkUI\_UIInputEvent事件指针。 |
| bool\* state | 输出参数，返回ScrollLock的状态。true表示处于激活状态，false表示处于未激活状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-native-type-h.md#arkui_errorcode) | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
