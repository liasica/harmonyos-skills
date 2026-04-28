---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-xcomponent-key-event-h
title: native_xcomponent_key_event.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_xcomponent_key_event.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b814a6a41ddea59ae9e76eafffda6bbd7dcd9af304d7739b52e288a67afcbf68
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于访问Native XComponent键盘事件所使用到的枚举类型。

**引用文件：** <ace/xcomponent/native\_xcomponent\_key\_event.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 10

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**相关示例：** [NativeXComponentSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_NativeXComponent\_KeyCode](capi-native-xcomponent-key-event-h.md#oh_nativexcomponent_keycode) | OH\_NativeXComponent\_KeyCode | 按键事件的键码。 |
| [OH\_NativeXComponent\_KeyAction](capi-native-xcomponent-key-event-h.md#oh_nativexcomponent_keyaction) | OH\_NativeXComponent\_KeyAction | 按键事件动作。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_NativeXComponent\_KeyCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_KeyCode
```

**描述：**

按键事件的键码。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| KEY\_UNKNOWN = -1 | 未知按键。 |
| KEY\_FN = 0 | 功能（Fn）键。 |
| KEY\_HOME = 1 | 功能（Home）键。 |
| KEY\_BACK = 2 | 返回键。 |
| KEY\_MEDIA\_PLAY\_PAUSE = 10 | 多媒体键，播放/暂停。 |
| KEY\_MEDIA\_STOP = 11 | 多媒体键，停止。 |
| KEY\_MEDIA\_NEXT = 12 | 多媒体键，下一首。 |
| KEY\_MEDIA\_PREVIOUS = 13 | 多媒体键，上一首。 |
| KEY\_MEDIA\_REWIND = 14 | 多媒体键，快退。 |
| KEY\_MEDIA\_FAST\_FORWARD = 15 | 多媒体键，快进。 |
| KEY\_VOLUME\_UP = 16 | 音量增加键。 |
| KEY\_VOLUME\_DOWN = 17 | 音量减小键。 |
| KEY\_POWER = 18 | 电源键。 |
| KEY\_CAMERA = 19 | 拍照键。 |
| KEY\_VOLUME\_MUTE = 22 | 扬声器静音键。 |
| KEY\_MUTE = 23 | 话筒静音键。 |
| KEY\_BRIGHTNESS\_UP = 40 | 亮度调节按键，调亮。 |
| KEY\_BRIGHTNESS\_DOWN = 41 | 亮度调节按键，调暗。 |
| KEY\_0 = 2000 | 按键'0'。 |
| KEY\_1 = 2001 | 按键'1'。 |
| KEY\_2 = 2002 | 按键'2'。 |
| KEY\_3 = 2003 | 按键'3'。 |
| KEY\_4 = 2004 | 按键'4'。 |
| KEY\_5 = 2005 | 按键'5'。 |
| KEY\_6 = 2006 | 按键'6'。 |
| KEY\_7 = 2007 | 按键'7'。 |
| KEY\_8 = 2008 | 按键'8'。 |
| KEY\_9 = 2009 | 按键'9'。 |
| KEY\_STAR = 2010 | 按键'\*'。 |
| KEY\_POUND = 2011 | 按键'#'。 |
| KEY\_DPAD\_UP = 2012 | 导航键，向上。 |
| KEY\_DPAD\_DOWN = 2013 | 导航键，向下。 |
| KEY\_DPAD\_LEFT = 2014 | 导航键，向左。 |
| KEY\_DPAD\_RIGHT = 2015 | 导航键，向右。 |
| KEY\_DPAD\_CENTER = 2016 | 导航键，确定键。 |
| KEY\_A = 2017 | 按键'A'。 |
| KEY\_B = 2018 | 按键'B'。 |
| KEY\_C = 2019 | 按键'C'。 |
| KEY\_D = 2020 | 按键'D'。 |
| KEY\_E = 2021 | 按键'E'。 |
| KEY\_F = 2022 | 按键'F'。 |
| KEY\_G = 2023 | 按键'G'。 |
| KEY\_H = 2024 | 按键'H'。 |
| KEY\_I = 2025 | 按键'I'。 |
| KEY\_J = 2026 | 按键'J'。 |
| KEY\_K = 2027 | 按键'K'。 |
| KEY\_L = 2028 | 按键'L'。 |
| KEY\_M = 2029 | 按键'M'。 |
| KEY\_N = 2030 | 按键'N'。 |
| KEY\_O = 2031 | 按键'O'。 |
| KEY\_P = 2032 | 按键'P'。 |
| KEY\_Q = 2033 | 按键'Q'。 |
| KEY\_R = 2034 | 按键'R'。 |
| KEY\_S = 2035 | 按键'S'。 |
| KEY\_T = 2036 | 按键'T'。 |
| KEY\_U = 2037 | 按键'U'。 |
| KEY\_V = 2038 | 按键'V'。 |
| KEY\_W = 2039 | 按键'W'。 |
| KEY\_X = 2040 | 按键'X'。 |
| KEY\_Y = 2041 | 按键'Y'。 |
| KEY\_Z = 2042 | 按键'Z'。 |
| KEY\_COMMA = 2043 | 按键','。 |
| KEY\_PERIOD = 2044 | 按键'.'。 |
| KEY\_ALT\_LEFT = 2045 | 左Alt键。 |
| KEY\_ALT\_RIGHT = 2046 | 右Alt键。 |
| KEY\_SHIFT\_LEFT = 2047 | 左Shift键。 |
| KEY\_SHIFT\_RIGHT = 2048 | 右Shift键。 |
| KEY\_TAB = 2049 | Tab键。 |
| KEY\_SPACE = 2050 | 空格键。 |
| KEY\_SYM = 2051 | 符号修改器按键。 |
| KEY\_EXPLORER = 2052 | 浏览器功能键，此键用于启动浏览器应用程序。 |
| KEY\_ENVELOPE = 2053 | 电子邮件功能键，此键用于启动电子邮件应用程序。 |
| KEY\_ENTER = 2054 | 回车键。 |
| KEY\_DEL = 2055 | 退格键。 |
| KEY\_GRAVE = 2056 | 按键'`'。 |
| KEY\_MINUS = 2057 | 按键'-'。 |
| KEY\_EQUALS = 2058 | 按键'='。 |
| KEY\_LEFT\_BRACKET = 2059 | 按键'['。 |
| KEY\_RIGHT\_BRACKET = 2060 | 按键']'。 |
| KEY\_BACKSLASH = 2061 | 按键'\'。 |
| KEY\_SEMICOLON = 2062 | 按键';'。 |
| KEY\_APOSTROPHE = 2063 | 按键''' (单引号)。 |
| KEY\_SLASH = 2064 | 按键'/'。 |
| KEY\_AT = 2065 | 按键'@'。 |
| KEY\_PLUS = 2066 | 按键'+'。 |
| KEY\_MENU = 2067 | 菜单键。 |
| KEY\_PAGE\_UP = 2068 | 向上翻页键。 |
| KEY\_PAGE\_DOWN = 2069 | 向下翻页键。 |
| KEY\_ESCAPE = 2070 | ESC键。 |
| KEY\_FORWARD\_DEL = 2071 | 删除键。 |
| KEY\_CTRL\_LEFT = 2072 | 左Ctrl键。 |
| KEY\_CTRL\_RIGHT = 2073 | 右Ctrl键。 |
| KEY\_CAPS\_LOCK = 2074 | 大写锁定键。 |
| KEY\_SCROLL\_LOCK = 2075 | 滚动锁定键。 |
| KEY\_META\_LEFT = 2076 | 左元修改器键。 |
| KEY\_META\_RIGHT = 2077 | 右元修改器键。 |
| KEY\_FUNCTION = 2078 | 功能键。 |
| KEY\_SYSRQ = 2079 | 系统请求/打印屏幕键。 |
| KEY\_BREAK = 2080 | Break/Pause键。 |
| KEY\_MOVE\_HOME = 2081 | 光标移动到开始键。 |
| KEY\_MOVE\_END = 2082 | 光标移动到末尾键。 |
| KEY\_INSERT = 2083 | 插入键。 |
| KEY\_FORWARD = 2084 | 前进键。 |
| KEY\_MEDIA\_PLAY = 2085 | 多媒体键，播放。 |
| KEY\_MEDIA\_PAUSE = 2086 | 多媒体键，暂停。 |
| KEY\_MEDIA\_CLOSE = 2087 | 多媒体键，关闭。 |
| KEY\_MEDIA\_EJECT = 2088 | 多媒体键，弹出。 |
| KEY\_MEDIA\_RECORD = 2089 | 多媒体键，录音。 |
| KEY\_F1 = 2090 | 按键'F1'。 |
| KEY\_F2 = 2091 | 按键'F2'。 |
| KEY\_F3 = 2092 | 按键'F3'。 |
| KEY\_F4 = 2093 | 按键'F4'。 |
| KEY\_F5 = 2094 | 按键'F5'。 |
| KEY\_F6 = 2095 | 按键'F6'。 |
| KEY\_F7 = 2096 | 按键'F7'。 |
| KEY\_F8 = 2097 | 按键'F8'。 |
| KEY\_F9 = 2098 | 按键'F9'。 |
| KEY\_F10 = 2099 | 按键'F10'。 |
| KEY\_F11 = 2100 | 按键'F11'。 |
| KEY\_F12 = 2101 | 按键'F12'。 |
| KEY\_NUM\_LOCK = 2102 | 小键盘锁。 |
| KEY\_NUMPAD\_0 = 2103 | 小键盘按键'0'。 |
| KEY\_NUMPAD\_1 = 2104 | 小键盘按键'1'。 |
| KEY\_NUMPAD\_2 = 2105 | 小键盘按键'2'。 |
| KEY\_NUMPAD\_3 = 2106 | 小键盘按键'3'。 |
| KEY\_NUMPAD\_4 = 2107 | 小键盘按键'4'。 |
| KEY\_NUMPAD\_5 = 2108 | 小键盘按键'5'。 |
| KEY\_NUMPAD\_6 = 2109 | 小键盘按键'6'。 |
| KEY\_NUMPAD\_7 = 2110 | 小键盘按键'7'。 |
| KEY\_NUMPAD\_8 = 2111 | 小键盘按键'8'。 |
| KEY\_NUMPAD\_9 = 2112 | 小键盘按键'9'。 |
| KEY\_NUMPAD\_DIVIDE = 2113 | 小键盘按键'/'。 |
| KEY\_NUMPAD\_MULTIPLY = 2114 | 小键盘按键'\*'。 |
| KEY\_NUMPAD\_SUBTRACT = 2115 | 小键盘按键'-'。 |
| KEY\_NUMPAD\_ADD = 2116 | 小键盘按键'+'。 |
| KEY\_NUMPAD\_DOT = 2117 | 小键盘按键'.'。 |
| KEY\_NUMPAD\_COMMA = 2118 | 小键盘按键','。 |
| KEY\_NUMPAD\_ENTER = 2119 | 小键盘按键回车。 |
| KEY\_NUMPAD\_EQUALS = 2120 | 小键盘按键'='。 |
| KEY\_NUMPAD\_LEFT\_PAREN = 2121 | 小键盘按键'('。 |
| KEY\_NUMPAD\_RIGHT\_PAREN = 2122 | 小键盘按键')'。 |
| KEY\_VIRTUAL\_MULTITASK = 2210 | 虚拟多任务键。 |
| KEY\_SLEEP = 2600 | 睡眠键。 |
| KEY\_ZENKAKU\_HANKAKU = 2601 | 日文全宽/半宽键。 |
| KEY\_102ND = 2602 | 102nd按键。 |
| KEY\_RO = 2603 | 日文Ro键。 |
| KEY\_KATAKANA = 2604 | 日文片假名键。 |
| KEY\_HIRAGANA = 2605 | 日文平假名键。 |
| KEY\_HENKAN = 2606 | 日文转换键。 |
| KEY\_KATAKANA\_HIRAGANA = 2607 | 日语片假名/平假名键。 |
| KEY\_MUHENKAN = 2608 | 日文非转换键。 |
| KEY\_LINEFEED = 2609 | 换行键。 |
| KEY\_MACRO = 2610 | 宏键。 |
| KEY\_NUMPAD\_PLUSMINUS = 2611 | 数字键盘上的加号/减号键。 |
| KEY\_SCALE = 2612 | 扩展键。 |
| KEY\_HANGUEL = 2613 | 日文韩语键。 |
| KEY\_HANJA = 2614 | 日文汉语键。 |
| KEY\_YEN = 2615 | 日元键。 |
| KEY\_STOP = 2616 | 停止键。 |
| KEY\_AGAIN = 2617 | 重复键。 |
| KEY\_PROPS = 2618 | 道具键。 |
| KEY\_UNDO = 2619 | 撤消键。 |
| KEY\_COPY = 2620 | 复制键。 |
| KEY\_OPEN = 2621 | 打开键。 |
| KEY\_PASTE = 2622 | 粘贴键。 |
| KEY\_FIND = 2623 | 查找键。 |
| KEY\_CUT = 2624 | 剪切键。 |
| KEY\_HELP = 2625 | 帮助键。 |
| KEY\_CALC = 2626 | 计算器特殊功能键，用于启动计算器应用程序。 |
| KEY\_FILE = 2627 | 文件按键。 |
| KEY\_BOOKMARKS = 2628 | 书签键。 |
| KEY\_NEXT = 2629 | 下一个按键。 |
| KEY\_PLAYPAUSE = 2630 | 播放/暂停键。 |
| KEY\_PREVIOUS = 2631 | 上一个按键。 |
| KEY\_STOPCD = 2632 | CD停止键。 |
| KEY\_CONFIG = 2634 | 配置键。 |
| KEY\_REFRESH = 2635 | 刷新键。 |
| KEY\_EXIT = 2636 | 退出键。 |
| KEY\_EDIT = 2637 | 编辑键。 |
| KEY\_SCROLLUP = 2638 | 向上滚动键。 |
| KEY\_SCROLLDOWN = 2639 | 向下滚动键。 |
| KEY\_NEW = 2640 | 新建键。 |
| KEY\_REDO = 2641 | 恢复键。 |
| KEY\_CLOSE = 2642 | 关闭键。 |
| KEY\_PLAY = 2643 | 播放键。 |
| KEY\_BASSBOOST = 2644 | 低音增强键。 |
| KEY\_PRINT = 2645 | 打印键。 |
| KEY\_CHAT = 2646 | 聊天键。 |
| KEY\_FINANCE = 2647 | 金融键。 |
| KEY\_CANCEL = 2648 | 取消键。 |
| KEY\_KBDILLUM\_TOGGLE = 2649 | 键盘灯光切换键。 |
| KEY\_KBDILLUM\_DOWN = 2650 | 键盘灯光调亮键。 |
| KEY\_KBDILLUM\_UP = 2651 | 键盘灯光调暗键。 |
| KEY\_SEND = 2652 | 发送键。 |
| KEY\_REPLY = 2653 | 答复键。 |
| KEY\_FORWARDMAIL = 2654 | 邮件转发键。 |
| KEY\_SAVE = 2655 | 保存键。 |
| KEY\_DOCUMENTS = 2656 | 文件键。 |
| KEY\_VIDEO\_NEXT = 2657 | 下一个视频键。 |
| KEY\_VIDEO\_PREV = 2658 | 上一个视频键。 |
| KEY\_BRIGHTNESS\_CYCLE = 2659 | 背光渐变键。 |
| KEY\_BRIGHTNESS\_ZERO = 2660 | 亮度调节为0键。 |
| KEY\_DISPLAY\_OFF = 2661 | 显示关闭键。 |
| KEY\_BTN\_MISC = 2662 | 游戏手柄上的各种按键。 |
| KEY\_GOTO = 2663 | 进入键。 |
| KEY\_INFO = 2664 | 信息查看键。 |
| KEY\_PROGRAM = 2665 | 程序键。 |
| KEY\_PVR = 2666 | 个人录像机(PVR)键。 |
| KEY\_SUBTITLE = 2667 | 字幕键。 |
| KEY\_FULL\_SCREEN = 2668 | 全屏键。 |
| KEY\_KEYBOARD = 2669 | 键盘。 |
| KEY\_ASPECT\_RATIO = 2670 | 屏幕纵横比调节键。 |
| KEY\_PC = 2671 | 端口控制键。 |
| KEY\_TV = 2672 | TV键。 |
| KEY\_TV2 = 2673 | TV键2。 |
| KEY\_VCR = 2674 | 录像机开启键。 |
| KEY\_VCR2 = 2675 | 录像机开启键2。 |
| KEY\_SAT = 2676 | SIM卡应用工具包（SAT）键。 |
| KEY\_CD = 2677 | CD键。 |
| KEY\_TAPE = 2678 | 磁带键。 |
| KEY\_TUNER = 2679 | 调谐器键。 |
| KEY\_PLAYER = 2680 | 播放器键。 |
| KEY\_DVD = 2681 | DVD键。 |
| KEY\_AUDIO = 2682 | 音频键。 |
| KEY\_VIDEO = 2683 | 视频键。 |
| KEY\_MEMO = 2684 | 备忘录键。 |
| KEY\_CALENDAR = 2685 | 日历键。 |
| KEY\_RED = 2686 | 红色指示器。 |
| KEY\_GREEN = 2687 | 绿色指示器。 |
| KEY\_YELLOW = 2688 | 黄色指示器。 |
| KEY\_BLUE = 2689 | 蓝色指示器。 |
| KEY\_CHANNELUP = 2690 | 频道向上键。 |
| KEY\_CHANNELDOWN = 2691 | 频道向下键。 |
| KEY\_LAST = 2692 | 末尾键。 |
| KEY\_RESTART = 2693 | 重启键。 |
| KEY\_SLOW = 2694 | 慢速键。 |
| KEY\_SHUFFLE = 2695 | 随机播放键。 |
| KEY\_VIDEOPHONE = 2696 | 可视电话键。 |
| KEY\_GAMES = 2697 | 游戏键。 |
| KEY\_ZOOMIN = 2698 | 放大键。 |
| KEY\_ZOOMOUT = 2699 | 缩小键。 |
| KEY\_ZOOMRESET = 2700 | 缩放重置键。 |
| KEY\_WORDPROCESSOR = 2701 | 文字处理键。 |
| KEY\_EDITOR = 2702 | 编辑器键。 |
| KEY\_SPREADSHEET = 2703 | 电子表格键。 |
| KEY\_GRAPHICSEDITOR = 2704 | 图形编辑器键。 |
| KEY\_PRESENTATION = 2705 | 演示文稿键。 |
| KEY\_DATABASE = 2706 | 数据库键标。 |
| KEY\_NEWS = 2707 | 新闻键。 |
| KEY\_VOICEMAIL = 2708 | 语音信箱。 |
| KEY\_ADDRESSBOOK = 2709 | 通讯簿。 |
| KEY\_MESSENGER = 2710 | 通信键。 |
| KEY\_BRIGHTNESS\_TOGGLE = 2711 | 亮度切换键。 |
| KEY\_SPELLCHECK = 2712 | AL拼写检查。 |
| KEY\_COFFEE = 2713 | 终端锁/屏幕保护程序。 |
| KEY\_MEDIA\_REPEAT = 2714 | 媒体循环键。 |
| KEY\_IMAGES = 2715 | 图像键。 |
| KEY\_BUTTONCONFIG = 2716 | 按键配置键。 |
| KEY\_TASKMANAGER = 2717 | 任务管理器。 |
| KEY\_JOURNAL = 2718 | 日志按键。 |
| KEY\_CONTROLPANEL = 2719 | 控制面板键。 |
| KEY\_APPSELECT = 2720 | 应用程序选择键。 |
| KEY\_SCREENSAVER = 2721 | 屏幕保护程序键。 |
| KEY\_ASSISTANT = 2722 | 辅助键。 |
| KEY\_KBD\_LAYOUT\_NEXT = 2723 | 下一个键盘布局键。 |
| KEY\_BRIGHTNESS\_MIN = 2724 | 最小亮度键。 |
| KEY\_BRIGHTNESS\_MAX = 2725 | 最大亮度键。 |
| KEY\_KBDINPUTASSIST\_PREV = 2726 | 键盘输入Assist\_Previous。 |
| KEY\_KBDINPUTASSIST\_NEXT = 2727 | 键盘输入Assist\_Next。 |
| KEY\_KBDINPUTASSIST\_PREVGROUP = 2728 | 键盘输入Assist\_Previous。 |
| KEY\_KBDINPUTASSIST\_NEXTGROUP = 2729 | 键盘输入Assist\_Next。 |
| KEY\_KBDINPUTASSIST\_ACCEPT = 2730 | 键盘输入Assist\_Accept。 |
| KEY\_KBDINPUTASSIST\_CANCEL = 2731 | 键盘输入Assist\_Cancel。 |
| KEY\_FRONT = 2800 | 挡风玻璃除雾器开关。 |
| KEY\_SETUP = 2801 | 设置键。 |
| KEY\_WAKEUP = 2802 | 唤醒键。 |
| KEY\_SENDFILE = 2803 | 发送文件按键。 |
| KEY\_DELETEFILE = 2804 | 删除文件按键。 |
| KEY\_XFER = 2805 | 文件传输(XFER)按键。 |
| KEY\_PROG1 = 2806 | 程序键1。 |
| KEY\_PROG2 = 2807 | 程序键2。 |
| KEY\_MSDOS = 2808 | MS-DOS键（微软磁盘操作系统）。 |
| KEY\_SCREENLOCK = 2809 | 屏幕锁定键。 |
| KEY\_DIRECTION\_ROTATE\_DISPLAY = 2810 | 方向旋转显示键。 |
| KEY\_CYCLEWINDOWS = 2811 | Windows循环键。 |
| KEY\_COMPUTER = 2812 | 按键。 |
| KEY\_EJECTCLOSECD = 2813 | 弹出CD键。 |
| KEY\_ISO = 2814 | ISO键。 |
| KEY\_MOVE = 2815 | 移动键。 |
| KEY\_F13 = 2816 | 按键'F13'。 |
| KEY\_F14 = 2817 | 按键'F14'。 |
| KEY\_F15 = 2818 | 按键'F15'。 |
| KEY\_F16 = 2819 | 按键'F16'。 |
| KEY\_F17 = 2820 | 按键'F17'。 |
| KEY\_F18 = 2821 | 按键'F18'。 |
| KEY\_F19 = 2822 | 按键'F19'。 |
| KEY\_F20 = 2823 | 按键'F20'。 |
| KEY\_F21 = 2824 | 按键'F21'。 |
| KEY\_F22 = 2825 | 按键'F22'。 |
| KEY\_F23 = 2826 | 按键'F23'。 |
| KEY\_F24 = 2827 | 按键'F24'。 |
| KEY\_PROG3 = 2828 | 程序键3。 |
| KEY\_PROG4 = 2829 | 程序键4。 |
| KEY\_DASHBOARD = 2830 | 仪表板。 |
| KEY\_SUSPEND = 2831 | 挂起键。 |
| KEY\_HP = 2832 | 高阶路径键。 |
| KEY\_SOUND = 2833 | 音量键。 |
| KEY\_QUESTION = 2834 | 疑问按键。 |
| KEY\_CONNECT = 2836 | 连接键。 |
| KEY\_SPORT = 2837 | 运动按键。 |
| KEY\_SHOP = 2838 | 商城键。 |
| KEY\_ALTERASE = 2839 | 交替键。 |
| KEY\_SWITCHVIDEOMODE = 2841 | 在可用视频之间循环输出（监视器/LCD/TV输出/等）。 |
| KEY\_BATTERY = 2842 | 电池按键。 |
| KEY\_BLUETOOTH = 2843 | 蓝牙按键。 |
| KEY\_WLAN = 2844 | 无线局域网。 |
| KEY\_UWB = 2845 | 超宽带（UWB）。 |
| KEY\_WWAN\_WIMAX = 2846 | WWAN WiMAX按键。 |
| KEY\_RFKILL = 2847 | 控制所有收音机的键。 |
| KEY\_CHANNEL = 3001 | 向上频道键。 |
| KEY\_BTN\_0 = 3100 | 按键0。 |
| KEY\_BTN\_1 = 3101 | 按键1。 |
| KEY\_BTN\_2 = 3102 | 按键2。 |
| KEY\_BTN\_3 = 3103 | 按键3。 |
| KEY\_BTN\_4 = 3104 | 按键4。 |
| KEY\_BTN\_5 = 3105 | 按键5。 |
| KEY\_BTN\_6 = 3106 | 按键6。 |
| KEY\_BTN\_7 = 3107 | 按键7。 |
| KEY\_BTN\_8 = 3108 | 按键8。 |
| KEY\_BTN\_9 = 3109 | 按键9。 |

### OH\_NativeXComponent\_KeyAction

PhonePC/2in1TabletTVWearable

```
1. enum OH_NativeXComponent_KeyAction
```

**描述：**

按键事件动作。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_UNKNOWN = -1 | 未知的按键动作。 |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_DOWN = 0 | 按键按下动作。 |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_UP = 1 | 按键抬起动作。 |
