---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowproperties
title: WindowManager_WindowProperties
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_WindowProperties
category: harmonyos-references
scraped_at: 2026-04-28T08:04:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:85d7f86bf5d24f08cc839dc9af53b895b28d298cf23559b146bf96be3e922f52
---

```
1. typedef struct {...} WindowManager_WindowProperties
```

## 概述

PhonePC/2in1TabletTVWearable

窗口属性。

**起始版本：** 15

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [WindowManager\_Rect](capi-windowmanager-rect.md) windowRect | 窗口的位置和尺寸。 |
| [WindowManager\_Rect](capi-windowmanager-rect.md) drawableRect | 窗口内可绘制区域的尺寸。 |
| [WindowManager\_WindowType](capi-oh-window-comm-h.md#windowmanager_windowtype) type | 窗口类型。 |
| bool isFullScreen | 窗口是否全屏模式。默认值为false。true表示窗口是全屏模式，false表示窗口是非全屏模式。 |
| bool isLayoutFullScreen | 窗口布局是否沉浸式。默认值为false。true表示窗口布局是沉浸式，false表示窗口布局是非沉浸式。 |
| bool focusable | 窗口是否能获取焦点。默认值为true。true表示窗口能获取焦点，false表示窗口不能获取焦点。 |
| bool touchable | 窗口是否可触。默认值为true。true表示窗口可触，false表示窗口不可触。 |
| float brightness | 窗口亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示默认亮度。 |
| bool isKeepScreenOn | 是否打开屏幕常亮。默认值为false。true表示屏幕常亮，false表示屏幕不常亮。 |
| bool isPrivacyMode | 窗口是否打开隐私模式。默认值为false。true表示窗口打开隐私模式，false表示窗口关闭隐私模式。 |
| bool isTransparent | 窗口是否透明。默认值为false。true表示窗口透明，false表示窗口非透明。 |
| uint32\_t id | 窗口id。默认值为0，该参数为整数。 |
| uint32\_t displayId | 窗口所在屏幕的id，默认返回主屏幕id，该参数为整数 |
