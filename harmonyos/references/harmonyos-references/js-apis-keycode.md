---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode
title: @ohos.multimodalInput.keyCode (键值)
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.keyCode (键值)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c3cd43d4c29ac33358f1300eb1f3c81029a43b1e5c7b724f8ee99e65e68edd24
---

按键设备的键值，按键设备包括键盘、光盘、游戏手柄等。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { KeyCode } from '@kit.InputKit';
```

## KeyCode

PhonePC/2in1TabletTVWearable

键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KEYCODE\_FN | 0 | 功能（Fn）键。 |
| KEYCODE\_UNKNOWN | -1 | 未知按键。 |
| KEYCODE\_HOME | 1 | 功能（Home）键。 |
| KEYCODE\_BACK | 2 | 返回键。 |
| KEYCODE\_SEARCH13+ | 9 | 搜索键。 |
| KEYCODE\_MEDIA\_PLAY\_PAUSE | 10 | 多媒体键：播放/暂停。  与KEYCODE\_PLAYPAUSE的区别为：  KEYCODE\_PLAYPAUSE是较早的定义，KEYCODE\_MEDIA\_PLAY\_PAUSE为现代媒体键设备设计，常见于较新的媒体键设备。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_STOP | 11 | 光盘停止键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_NEXT | 12 | 多媒体键：下一首。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_PREVIOUS | 13 | 多媒体键：上一首。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_REWIND | 14 | 多媒体键：快退。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_FAST\_FORWARD | 15 | 多媒体键：快进。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_VOLUME\_UP | 16 | 音量增加键。 |
| KEYCODE\_VOLUME\_DOWN | 17 | 音量减小键。 |
| KEYCODE\_POWER | 18 | 电源键。 |
| KEYCODE\_CAMERA | 19 | 拍照键。 |
| KEYCODE\_VOLUME\_MUTE | 22 | 扬声器静音键。 |
| KEYCODE\_MUTE | 23 | 话筒静音键。 |
| KEYCODE\_BRIGHTNESS\_UP | 40 | 亮度调节按键：调亮。 |
| KEYCODE\_BRIGHTNESS\_DOWN | 41 | 亮度调节按键：调暗。 |
| KEYCODE\_0 | 2000 | 按键'0'。 |
| KEYCODE\_1 | 2001 | 按键'1'。 |
| KEYCODE\_2 | 2002 | 按键'2'。 |
| KEYCODE\_3 | 2003 | 按键'3'。 |
| KEYCODE\_4 | 2004 | 按键'4'。 |
| KEYCODE\_5 | 2005 | 按键'5'。 |
| KEYCODE\_6 | 2006 | 按键'6'。 |
| KEYCODE\_7 | 2007 | 按键'7'。 |
| KEYCODE\_8 | 2008 | 按键'8'。 |
| KEYCODE\_9 | 2009 | 按键'9'。 |
| KEYCODE\_STAR | 2010 | 按键'\*'。 |
| KEYCODE\_POUND | 2011 | 按键'#'。 |
| KEYCODE\_DPAD\_UP | 2012 | 导航键：向上。 |
| KEYCODE\_DPAD\_DOWN | 2013 | 导航键：向下。 |
| KEYCODE\_DPAD\_LEFT | 2014 | 导航键：向左。 |
| KEYCODE\_DPAD\_RIGHT | 2015 | 导航键：向右。 |
| KEYCODE\_DPAD\_CENTER | 2016 | 导航键：确定键。 |
| KEYCODE\_A | 2017 | 按键'A'。 |
| KEYCODE\_B | 2018 | 按键'B'。 |
| KEYCODE\_C | 2019 | 按键'C'。 |
| KEYCODE\_D | 2020 | 按键'D'。 |
| KEYCODE\_E | 2021 | 按键'E'。 |
| KEYCODE\_F | 2022 | 按键'F'。 |
| KEYCODE\_G | 2023 | 按键'G'。 |
| KEYCODE\_H | 2024 | 按键'H'。 |
| KEYCODE\_I | 2025 | 按键'I'。 |
| KEYCODE\_J | 2026 | 按键'J'。 |
| KEYCODE\_K | 2027 | 按键'K'。 |
| KEYCODE\_L | 2028 | 按键'L'。 |
| KEYCODE\_M | 2029 | 按键'M'。 |
| KEYCODE\_N | 2030 | 按键'N'。 |
| KEYCODE\_O | 2031 | 按键'O'。 |
| KEYCODE\_P | 2032 | 按键'P'。 |
| KEYCODE\_Q | 2033 | 按键'Q'。 |
| KEYCODE\_R | 2034 | 按键'R'。 |
| KEYCODE\_S | 2035 | 按键'S'。 |
| KEYCODE\_T | 2036 | 按键'T'。 |
| KEYCODE\_U | 2037 | 按键'U'。 |
| KEYCODE\_V | 2038 | 按键'V'。 |
| KEYCODE\_W | 2039 | 按键'W'。 |
| KEYCODE\_X | 2040 | 按键'X'。 |
| KEYCODE\_Y | 2041 | 按键'Y'。 |
| KEYCODE\_Z | 2042 | 按键'Z'。 |
| KEYCODE\_COMMA | 2043 | 按键','。 |
| KEYCODE\_PERIOD | 2044 | 按键'.'。 |
| KEYCODE\_ALT\_LEFT | 2045 | 左Alt键。 |
| KEYCODE\_ALT\_RIGHT | 2046 | 右Alt键。 |
| KEYCODE\_SHIFT\_LEFT | 2047 | 左Shift键。 |
| KEYCODE\_SHIFT\_RIGHT | 2048 | 右Shift键。 |
| KEYCODE\_TAB | 2049 | Tab键。 |
| KEYCODE\_SPACE | 2050 | 空格键。 |
| KEYCODE\_SYM | 2051 | 符号修改器按键。 |
| KEYCODE\_EXPLORER | 2052 | 浏览器功能键，此键用于启动浏览器应用程序。 |
| KEYCODE\_ENVELOPE | 2053 | 电子邮件功能键，此键用于启动电子邮件应用程序。 |
| KEYCODE\_ENTER | 2054 | 回车键。 |
| KEYCODE\_DEL | 2055 | 退格键。 |
| KEYCODE\_GRAVE | 2056 | 按键'`'。 |
| KEYCODE\_MINUS | 2057 | 按键'-'。 |
| KEYCODE\_EQUALS | 2058 | 按键'='。 |
| KEYCODE\_LEFT\_BRACKET | 2059 | 按键'['。 |
| KEYCODE\_RIGHT\_BRACKET | 2060 | 按键']'。 |
| KEYCODE\_BACKSLASH | 2061 | 按键'\'。 |
| KEYCODE\_SEMICOLON | 2062 | 按键';'。 |
| KEYCODE\_APOSTROPHE | 2063 | 按键''' (单引号)。 |
| KEYCODE\_SLASH | 2064 | 按键'/'。 |
| KEYCODE\_AT | 2065 | 按键'@'。 |
| KEYCODE\_PLUS | 2066 | 按键'+'。 |
| KEYCODE\_MENU | 2067 | 菜单键。 |
| KEYCODE\_PAGE\_UP | 2068 | 向上翻页键。 |
| KEYCODE\_PAGE\_DOWN | 2069 | 向下翻页键。 |
| KEYCODE\_ESCAPE | 2070 | Esc键。 |
| KEYCODE\_FORWARD\_DEL | 2071 | 删除键。 |
| KEYCODE\_CTRL\_LEFT | 2072 | 左Ctrl键。 |
| KEYCODE\_CTRL\_RIGHT | 2073 | 右Ctrl键。 |
| KEYCODE\_CAPS\_LOCK | 2074 | 大写锁定键。 |
| KEYCODE\_SCROLL\_LOCK | 2075 | 滚动锁定键。 |
| KEYCODE\_META\_LEFT | 2076 | 左Meta键。 |
| KEYCODE\_META\_RIGHT | 2077 | 右Meta键。 |
| KEYCODE\_FUNCTION | 2078 | 功能键。 |
| KEYCODE\_SYSRQ | 2079 | 系统请求/打印屏幕键。 |
| KEYCODE\_BREAK | 2080 | Break/Pause键。 |
| KEYCODE\_MOVE\_HOME | 2081 | 光标移动到开始键。 |
| KEYCODE\_MOVE\_END | 2082 | 光标移动到末尾键。 |
| KEYCODE\_INSERT | 2083 | 插入键。 |
| KEYCODE\_FORWARD | 2084 | 前进键。 |
| KEYCODE\_MEDIA\_PLAY | 2085 | 多媒体键：播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_PAUSE | 2086 | 光盘暂停键。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| KEYCODE\_MEDIA\_CLOSE | 2087 | 光盘关闭键。 |
| KEYCODE\_MEDIA\_EJECT | 2088 | 光盘弹出键。 |
| KEYCODE\_MEDIA\_RECORD | 2089 | 多媒体键：录音。 |
| KEYCODE\_F1 | 2090 | 按键'F1'。 |
| KEYCODE\_F2 | 2091 | 按键'F2'。 |
| KEYCODE\_F3 | 2092 | 按键'F3'。 |
| KEYCODE\_F4 | 2093 | 按键'F4'。 |
| KEYCODE\_F5 | 2094 | 按键'F5'。 |
| KEYCODE\_F6 | 2095 | 按键'F6'。 |
| KEYCODE\_F7 | 2096 | 按键'F7'。 |
| KEYCODE\_F8 | 2097 | 按键'F8'。 |
| KEYCODE\_F9 | 2098 | 按键'F9'。 |
| KEYCODE\_F10 | 2099 | 按键'F10'。 |
| KEYCODE\_F11 | 2100 | 按键'F11'。 |
| KEYCODE\_F12 | 2101 | 按键'F12'。 |
| KEYCODE\_NUM\_LOCK | 2102 | 小键盘锁。 |
| KEYCODE\_NUMPAD\_0 | 2103 | 小键盘按键'0'。 |
| KEYCODE\_NUMPAD\_1 | 2104 | 小键盘按键'1'。 |
| KEYCODE\_NUMPAD\_2 | 2105 | 小键盘按键'2'。 |
| KEYCODE\_NUMPAD\_3 | 2106 | 小键盘按键'3'。 |
| KEYCODE\_NUMPAD\_4 | 2107 | 小键盘按键'4'。 |
| KEYCODE\_NUMPAD\_5 | 2108 | 小键盘按键'5'。 |
| KEYCODE\_NUMPAD\_6 | 2109 | 小键盘按键'6'。 |
| KEYCODE\_NUMPAD\_7 | 2110 | 小键盘按键'7'。 |
| KEYCODE\_NUMPAD\_8 | 2111 | 小键盘按键'8'。 |
| KEYCODE\_NUMPAD\_9 | 2112 | 小键盘按键'9'。 |
| KEYCODE\_NUMPAD\_DIVIDE | 2113 | 小键盘按键'/'。 |
| KEYCODE\_NUMPAD\_MULTIPLY | 2114 | 小键盘按键'\*'。 |
| KEYCODE\_NUMPAD\_SUBTRACT | 2115 | 小键盘按键'-'。 |
| KEYCODE\_NUMPAD\_ADD | 2116 | 小键盘按键'+'。 |
| KEYCODE\_NUMPAD\_DOT | 2117 | 小键盘按键'.'。 |
| KEYCODE\_NUMPAD\_COMMA | 2118 | 小键盘按键','。 |
| KEYCODE\_NUMPAD\_ENTER | 2119 | 小键盘按键回车。 |
| KEYCODE\_NUMPAD\_EQUALS | 2120 | 小键盘按键'='。 |
| KEYCODE\_NUMPAD\_LEFT\_PAREN | 2121 | 小键盘按键'('。 |
| KEYCODE\_NUMPAD\_RIGHT\_PAREN | 2122 | 小键盘按键')'。 |
| KEYCODE\_VIRTUAL\_MULTITASK | 2210 | 虚拟多任务键。 |
| KEYCODE\_BUTTON\_A15+ | 2301 | 游戏手柄按键'A'。 |
| KEYCODE\_BUTTON\_B15+ | 2302 | 游戏手柄按键'B'。 |
| KEYCODE\_BUTTON\_X15+ | 2304 | 游戏手柄按键'X'。 |
| KEYCODE\_BUTTON\_Y15+ | 2305 | 游戏手柄按键'Y'。 |
| KEYCODE\_BUTTON\_L115+ | 2307 | 游戏手柄按键'L1'。 |
| KEYCODE\_BUTTON\_R115+ | 2308 | 游戏手柄按键'R1'。 |
| KEYCODE\_BUTTON\_L215+ | 2309 | 游戏手柄按键'L2'。 |
| KEYCODE\_BUTTON\_R215+ | 2310 | 游戏手柄按键'R2'。 |
| KEYCODE\_BUTTON\_SELECT15+ | 2311 | 游戏手柄按键'Select'。 |
| KEYCODE\_BUTTON\_START15+ | 2312 | 游戏手柄按键'Start'。 |
| KEYCODE\_BUTTON\_MODE15+ | 2313 | 游戏手柄按键'Mode'。 |
| KEYCODE\_BUTTON\_THUMBL15+ | 2314 | 游戏手柄按键'THUMBL'。 |
| KEYCODE\_BUTTON\_THUMBR15+ | 2315 | 游戏手柄按键'THUMBR'。 |
| KEYCODE\_SLEEP | 2600 | 睡眠键。 |
| KEYCODE\_ZENKAKU\_HANKAKU | 2601 | 日文全宽/半宽键。 |
| KEYCODE\_102ND | 2602 | 国际键盘扩展键。 |
| KEYCODE\_RO | 2603 | 日文Ro键。 |
| KEYCODE\_KATAKANA | 2604 | 日文片假名键。 |
| KEYCODE\_HIRAGANA | 2605 | 日文平假名键。 |
| KEYCODE\_HENKAN | 2606 | 日文转换键。 |
| KEYCODE\_KATAKANA\_HIRAGANA | 2607 | 日语片假名/平假名键。 |
| KEYCODE\_MUHENKAN | 2608 | 日文非转换键。 |
| KEYCODE\_LINEFEED | 2609 | 换行键。 |
| KEYCODE\_MACRO | 2610 | 宏键。 |
| KEYCODE\_NUMPAD\_PLUSMINUS | 2611 | 数字键盘上的加号/减号键。 |
| KEYCODE\_SCALE | 2612 | 扩展键。 |
| KEYCODE\_HANGUEL | 2613 | 日文韩语键。 |
| KEYCODE\_HANJA | 2614 | 日文汉语键。 |
| KEYCODE\_YEN | 2615 | 日元键。 |
| KEYCODE\_STOP | 2616 | 停止键。 |
| KEYCODE\_AGAIN | 2617 | 重复键。 |
| KEYCODE\_PROPS | 2618 | 道具键。 |
| KEYCODE\_UNDO | 2619 | 撤消键。 |
| KEYCODE\_COPY | 2620 | 复制键。 |
| KEYCODE\_OPEN | 2621 | 打开键。 |
| KEYCODE\_PASTE | 2622 | 粘贴键。 |
| KEYCODE\_FIND | 2623 | 查找键。 |
| KEYCODE\_CUT | 2624 | 剪切键。 |
| KEYCODE\_HELP | 2625 | 帮助键。 |
| KEYCODE\_CALC | 2626 | 计算器特殊功能键，用于启动计算器应用程序。 |
| KEYCODE\_FILE | 2627 | 文件按键。 |
| KEYCODE\_BOOKMARKS | 2628 | 书签键。 |
| KEYCODE\_NEXT | 2629 | Page Down键。 |
| KEYCODE\_PLAYPAUSE | 2630 | 多媒体键：播放/暂停。  与KEYCODE\_MEDIA\_PLAY\_PAUSE的区别为：  KEYCODE\_PLAYPAUSE是较早的定义，KEYCODE\_MEDIA\_PLAY\_PAUSE为现代媒体键设备设计，常见于较新的媒体键设备。 |
| KEYCODE\_PREVIOUS | 2631 | Page Up键。 |
| KEYCODE\_STOPCD | 2632 | CD停止键。 |
| KEYCODE\_CONFIG | 2634 | 配置键。 |
| KEYCODE\_REFRESH | 2635 | 刷新键。 |
| KEYCODE\_EXIT | 2636 | 退出键。 |
| KEYCODE\_EDIT | 2637 | 编辑键。 |
| KEYCODE\_SCROLLUP | 2638 | 向上滚动键。 |
| KEYCODE\_SCROLLDOWN | 2639 | 向下滚动键。 |
| KEYCODE\_NEW | 2640 | 新建键。 |
| KEYCODE\_REDO | 2641 | 恢复键。 |
| KEYCODE\_CLOSE | 2642 | 关闭键。 |
| KEYCODE\_PLAY | 2643 | 播放键。 |
| KEYCODE\_BASSBOOST | 2644 | 低音增强键。 |
| KEYCODE\_PRINT | 2645 | 打印键。 |
| KEYCODE\_CHAT | 2646 | 聊天键。 |
| KEYCODE\_FINANCE | 2647 | 金融键。 |
| KEYCODE\_CANCEL | 2648 | 取消键。 |
| KEYCODE\_KBDILLUM\_TOGGLE | 2649 | 键盘灯光切换键。 |
| KEYCODE\_KBDILLUM\_DOWN | 2650 | 键盘灯光调暗键。 |
| KEYCODE\_KBDILLUM\_UP | 2651 | 键盘灯光调亮键。 |
| KEYCODE\_SEND | 2652 | 发送键。 |
| KEYCODE\_REPLY | 2653 | 答复键。 |
| KEYCODE\_FORWARDMAIL | 2654 | 邮件转发键。 |
| KEYCODE\_SAVE | 2655 | 保存键。 |
| KEYCODE\_DOCUMENTS | 2656 | 文件键。 |
| KEYCODE\_VIDEO\_NEXT | 2657 | 下一个视频键。 |
| KEYCODE\_VIDEO\_PREV | 2658 | 上一个视频键。 |
| KEYCODE\_BRIGHTNESS\_CYCLE | 2659 | 背光渐变键。 |
| KEYCODE\_BRIGHTNESS\_ZERO | 2660 | 亮度调节为0键。 |
| KEYCODE\_DISPLAY\_OFF | 2661 | 显示关闭键。 |
| KEYCODE\_BTN\_MISC | 2662 | 游戏手柄上的各种按键。 |
| KEYCODE\_GOTO | 2663 | 进入键。 |
| KEYCODE\_INFO | 2664 | 信息查看键。 |
| KEYCODE\_PROGRAM | 2665 | 程序键。 |
| KEYCODE\_PVR | 2666 | 个人录像机（PVR）键。 |
| KEYCODE\_SUBTITLE | 2667 | 字幕键。 |
| KEYCODE\_FULL\_SCREEN | 2668 | 全屏键。 |
| KEYCODE\_KEYBOARD | 2669 | 键盘。 |
| KEYCODE\_ASPECT\_RATIO | 2670 | 屏幕纵横比调节键。 |
| KEYCODE\_PC | 2671 | 端口控制键。 |
| KEYCODE\_TV | 2672 | TV键。 |
| KEYCODE\_TV2 | 2673 | TV键2。 |
| KEYCODE\_VCR | 2674 | 录像机开启键。 |
| KEYCODE\_VCR2 | 2675 | 录像机开启键2。 |
| KEYCODE\_SAT | 2676 | SIM卡应用工具包（SAT）键。 |
| KEYCODE\_CD | 2677 | CD键。 |
| KEYCODE\_TAPE | 2678 | 磁带键。 |
| KEYCODE\_TUNER | 2679 | 调谐器键。 |
| KEYCODE\_PLAYER | 2680 | 播放器键。 |
| KEYCODE\_DVD | 2681 | DVD键。 |
| KEYCODE\_AUDIO | 2682 | 音频键。 |
| KEYCODE\_VIDEO | 2683 | 视频键。 |
| KEYCODE\_MEMO | 2684 | 备忘录键。 |
| KEYCODE\_CALENDAR | 2685 | 日历键。 |
| KEYCODE\_RED | 2686 | 红色指示器。 |
| KEYCODE\_GREEN | 2687 | 绿色指示器。 |
| KEYCODE\_YELLOW | 2688 | 黄色指示器。 |
| KEYCODE\_BLUE | 2689 | 蓝色指示器。 |
| KEYCODE\_CHANNELUP | 2690 | 频道向上键。 |
| KEYCODE\_CHANNELDOWN | 2691 | 频道向下键。 |
| KEYCODE\_LAST | 2692 | 末尾键。 |
| KEYCODE\_RESTART | 2693 | 重启键。 |
| KEYCODE\_SLOW | 2694 | 慢速键。 |
| KEYCODE\_SHUFFLE | 2695 | 随机播放键。 |
| KEYCODE\_VIDEOPHONE | 2696 | 可视电话键。 |
| KEYCODE\_GAMES | 2697 | 游戏键。 |
| KEYCODE\_ZOOMIN | 2698 | 放大键。 |
| KEYCODE\_ZOOMOUT | 2699 | 缩小键。 |
| KEYCODE\_ZOOMRESET | 2700 | 缩放重置键。 |
| KEYCODE\_WORDPROCESSOR | 2701 | 文字处理键。 |
| KEYCODE\_EDITOR | 2702 | 编辑器键。 |
| KEYCODE\_SPREADSHEET | 2703 | 电子表格键。 |
| KEYCODE\_GRAPHICSEDITOR | 2704 | 图形编辑器键。 |
| KEYCODE\_PRESENTATION | 2705 | 演示文稿键。 |
| KEYCODE\_DATABASE | 2706 | 数据库键标。 |
| KEYCODE\_NEWS | 2707 | 新闻键。 |
| KEYCODE\_VOICEMAIL | 2708 | 语音信箱。 |
| KEYCODE\_ADDRESSBOOK | 2709 | 通讯簿。 |
| KEYCODE\_MESSENGER | 2710 | 通信键。 |
| KEYCODE\_BRIGHTNESS\_TOGGLE | 2711 | 亮度切换键。 |
| KEYCODE\_SPELLCHECK | 2712 | 拼写检查键。 |
| KEYCODE\_COFFEE | 2713 | 终端锁/屏幕保护程序。 |
| KEYCODE\_MEDIA\_REPEAT | 2714 | 媒体循环键。 |
| KEYCODE\_IMAGES | 2715 | 图像键。 |
| KEYCODE\_BUTTONCONFIG | 2716 | 按键配置键。 |
| KEYCODE\_TASKMANAGER | 2717 | 任务管理器。 |
| KEYCODE\_JOURNAL | 2718 | 日志按键。 |
| KEYCODE\_CONTROLPANEL | 2719 | 控制面板键。 |
| KEYCODE\_APPSELECT | 2720 | 应用程序选择键。 |
| KEYCODE\_SCREENSAVER | 2721 | 屏幕保护程序键。 |
| KEYCODE\_ASSISTANT | 2722 | 智慧键。 |
| KEYCODE\_KBD\_LAYOUT\_NEXT | 2723 | 下一个键盘布局键。 |
| KEYCODE\_BRIGHTNESS\_MIN | 2724 | 最小亮度键。 |
| KEYCODE\_BRIGHTNESS\_MAX | 2725 | 最大亮度键。 |
| KEYCODE\_KBDINPUTASSIST\_PREV | 2726 | 键盘输入Assist\_Previous，查看输入法输入记录。 |
| KEYCODE\_KBDINPUTASSIST\_NEXT | 2727 | 键盘输入Assist\_Next，查看输入法输入拓展。 |
| KEYCODE\_KBDINPUTASSIST\_PREVGROUP | 2728 | 键盘输入Assist\_Previous，切换输入组中上一个输入法。 |
| KEYCODE\_KBDINPUTASSIST\_NEXTGROUP | 2729 | 键盘输入Assist\_Next，切换输入组中下一个输入法。 |
| KEYCODE\_KBDINPUTASSIST\_ACCEPT | 2730 | 键盘输入Assist\_Accept。 |
| KEYCODE\_KBDINPUTASSIST\_CANCEL | 2731 | 键盘输入Assist\_Cancel。 |
| KEYCODE\_FRONT | 2800 | 挡风玻璃除雾器开关。 |
| KEYCODE\_SETUP | 2801 | 设置键。 |
| KEYCODE\_WAKEUP | 2802 | 唤醒键。 |
| KEYCODE\_SENDFILE | 2803 | 发送文件按键。 |
| KEYCODE\_DELETEFILE | 2804 | 删除文件按键。 |
| KEYCODE\_XFER | 2805 | 文件传输（XFER）按键。 |
| KEYCODE\_PROG1 | 2806 | 程序键1。 |
| KEYCODE\_PROG2 | 2807 | 程序键2。 |
| KEYCODE\_MSDOS | 2808 | DOS面板键。 |
| KEYCODE\_SCREENLOCK | 2809 | 屏幕锁定键。 |
| KEYCODE\_DIRECTION\_ROTATE\_DISPLAY | 2810 | 方向旋转显示键。 |
| KEYCODE\_CYCLEWINDOWS | 2811 | 窗口切换键。 |
| KEYCODE\_COMPUTER | 2812 | 按键。 |
| KEYCODE\_EJECTCLOSECD | 2813 | 弹出CD键。 |
| KEYCODE\_ISO | 2814 | ISO键。 |
| KEYCODE\_MOVE | 2815 | 移动键。 |
| KEYCODE\_F13 | 2816 | 按键'F13'。 |
| KEYCODE\_F14 | 2817 | 按键'F14'。 |
| KEYCODE\_F15 | 2818 | 按键'F15'。 |
| KEYCODE\_F16 | 2819 | 按键'F16'。 |
| KEYCODE\_F17 | 2820 | 按键'F17'。 |
| KEYCODE\_F18 | 2821 | 按键'F18'。 |
| KEYCODE\_F19 | 2822 | 按键'F19'。 |
| KEYCODE\_F20 | 2823 | 按键'F20'。 |
| KEYCODE\_F21 | 2824 | 按键'F21'。 |
| KEYCODE\_F22 | 2825 | 按键'F22'。 |
| KEYCODE\_F23 | 2826 | 按键'F23'。 |
| KEYCODE\_F24 | 2827 | 按键'F24'。 |
| KEYCODE\_PROG3 | 2828 | 程序键3。 |
| KEYCODE\_PROG4 | 2829 | 程序键4。 |
| KEYCODE\_DASHBOARD | 2830 | 仪表板。 |
| KEYCODE\_SUSPEND | 2831 | 挂起键。 |
| KEYCODE\_HP | 2832 | 高阶路径键。 |
| KEYCODE\_SOUND | 2833 | 音量键。 |
| KEYCODE\_QUESTION | 2834 | 疑问按键。 |
| KEYCODE\_CONNECT | 2836 | 连接键。 |
| KEYCODE\_SPORT | 2837 | 运动按键。 |
| KEYCODE\_SHOP | 2838 | 商城键。 |
| KEYCODE\_ALTERASE | 2839 | 交替键。 |
| KEYCODE\_SWITCHVIDEOMODE | 2841 | 在可用视频之间循环输出（监视器/LCD/TV输出/等）。 |
| KEYCODE\_BATTERY | 2842 | 电池按键。 |
| KEYCODE\_BLUETOOTH | 2843 | 蓝牙按键。 |
| KEYCODE\_WLAN | 2844 | 无线局域网。 |
| KEYCODE\_UWB | 2845 | 超宽带控制键。 |
| KEYCODE\_WWAN\_WIMAX | 2846 | 移动网络控制键。 |
| KEYCODE\_RFKILL | 2847 | 控制所有收音机的键。 |
| KEYCODE\_CHANNEL | 3001 | 向上频道键。 |
| KEYCODE\_BTN\_0 | 3100 | 按键0。 |
| KEYCODE\_BTN\_1 | 3101 | 按键1。 |
| KEYCODE\_BTN\_2 | 3102 | 按键2。 |
| KEYCODE\_BTN\_3 | 3103 | 按键3。 |
| KEYCODE\_BTN\_4 | 3104 | 按键4。 |
| KEYCODE\_BTN\_5 | 3105 | 按键5。 |
| KEYCODE\_BTN\_6 | 3106 | 按键6。 |
| KEYCODE\_BTN\_7 | 3107 | 按键7。 |
| KEYCODE\_BTN\_8 | 3108 | 按键8。 |
| KEYCODE\_BTN\_9 | 3109 | 按键9。 |
| KEYCODE\_DAGGER\_CLICK18+ | 3211 | 智能手表智感窗按键单击。 |
| KEYCODE\_DAGGER\_DOUBLE\_CLICK18+ | 3212 | 智能手表智感窗按键双击。 |
| KEYCODE\_DAGGER\_LONG\_PRESS18+ | 3213 | 智能手表智感窗按键长按。 |
| KEYCODE\_DIV20+ | 3220 | 智能手表左按键。 |
