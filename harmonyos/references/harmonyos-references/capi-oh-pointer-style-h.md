---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pointer-style-h
title: oh_pointer_style.h
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 头文件 > oh_pointer_style.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca0cd34ed19b92b96ef2a9c0c85cda9b8e5cbdfb3e27804ee11c4ba4aaaa25dd
---

## 概述

PhonePC/2in1TabletTVWearable

鼠标光标的样式。

**引用文件：** <multimodalinput/oh\_pointer\_style.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 22

**相关模块：** [input](capi-input.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Input\_PointerStyle](capi-oh-pointer-style-h.md#input_pointerstyle) | Input\_PointerStyle | 鼠标光标样式。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Input\_PointerStyle

PhonePC/2in1TabletTVWearable

```
1. enum Input_PointerStyle
```

**描述**

鼠标光标样式。

**起始版本：** 22

| 枚举项 | 描述 | 图示 |
| --- | --- | --- |
| DEFAULT = 0 | 默认 |  |
| EAST = 1 | 向东箭头 |  |
| WEST = 2 | 向西箭头 |  |
| SOUTH = 3 | 向南箭头 |  |
| NORTH = 4 | 向北箭头 |  |
| WEST\_EAST = 5 | 向西东箭头 |  |
| NORTH\_SOUTH = 6 | 向北南箭头 |  |
| NORTH\_EAST = 7 | 向东北箭头 |  |
| NORTH\_WEST = 8 | 向西北箭头 |  |
| SOUTH\_EAST = 9 | 向东南箭头 |  |
| SOUTH\_WEST = 10 | 向西南箭头 |  |
| NORTH\_EAST\_SOUTH\_WEST = 11 | 东北西南调整 |  |
| NORTH\_WEST\_SOUTH\_EAST = 12 | 西北东南调整 |  |
| CROSS = 13 | 准确选择 |  |
| CURSOR\_COPY = 14 | 拷贝 |  |
| CURSOR\_FORBID = 15 | 不可用 |  |
| COLOR\_SUCKER = 16 | 取色器 |  |
| HAND\_GRABBING = 17 | 并拢的手 |  |
| HAND\_OPEN = 18 | 张开的手 |  |
| HAND\_POINTING = 19 | 手形指针 |  |
| HELP = 20 | 帮助选择 |  |
| MOVE = 21 | 移动 |  |
| RESIZE\_LEFT\_RIGHT = 22 | 内部左右调整 |  |
| RESIZE\_UP\_DOWN = 23 | 内部上下调整 |  |
| SCREENSHOT\_CHOOSE = 24 | 截图十字准星 |  |
| SCREENSHOT\_CURSOR = 25 | 截图 |  |
| TEXT\_CURSOR = 26 | 文本选择 |  |
| ZOOM\_IN = 27 | 放大 |  |
| ZOOM\_OUT = 28 | 缩小 |  |
| MIDDLE\_BTN\_EAST = 29 | 向东滚动 |  |
| MIDDLE\_BTN\_WEST = 30 | 向西滚动 |  |
| MIDDLE\_BTN\_SOUTH = 31 | 向南滚动 |  |
| MIDDLE\_BTN\_NORTH = 32 | 向北滚动 |  |
| MIDDLE\_BTN\_NORTH\_SOUTH = 33 | 向南北滚动 |  |
| MIDDLE\_BTN\_NORTH\_EAST = 34 | 向东北滚动 |  |
| MIDDLE\_BTN\_NORTH\_WEST = 35 | 向西北滚动 |  |
| MIDDLE\_BTN\_SOUTH\_EAST = 36 | 向东南滚动 |  |
| MIDDLE\_BTN\_SOUTH\_WEST = 37 | 向西南滚动 |  |
| MIDDLE\_BTN\_NORTH\_SOUTH\_WEST\_EAST = 38 | 四向锥形移动 |  |
| HORIZONTAL\_TEXT\_CURSOR = 39 | 垂直文本选择 |  |
| CURSOR\_CROSS = 40 | 十字光标 |  |
| CURSOR\_CIRCLE = 41 | 圆形光标 |  |
| LOADING = 42 | 正在载入动画光标 |  |
| RUNNING = 43 | 后台运行中动画光标 |  |
| MIDDLE\_BTN\_EAST\_WEST = 44 | 向东西滚动 |  |
| RUNNING\_LEFT = 45 | 后台运行中动画光标(拓展1) |  |
| RUNNING\_RIGHT = 46 | 后台运行中动画光标(拓展2) |  |
| AECH\_DEVELOPER\_DEFINED\_ICON = 47 | 圆形自定义光标 |  |
| SCREENRECORDER\_CURSOR = 48 | 录屏光标 |  |
| LASER\_CURSOR = 49 | 悬浮光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| LASER\_CURSOR\_DOT = 50 | 点击光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| LASER\_CURSOR\_DOT\_RED = 51 | 激光笔光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| DEVELOPER\_DEFINED\_ICON = -100 | 自定义光标，开发者可使用[OH\_Input\_SetCustomCursor](capi-oh-input-manager-h.md#oh_input_setcustomcursor)设置自定义光标，不支持使用[OH\_Input\_SetPointerStyle](capi-oh-input-manager-h.md#oh_input_setpointerstyle)直接设置。 | 自定义光标样式，通过接口设置。 |
