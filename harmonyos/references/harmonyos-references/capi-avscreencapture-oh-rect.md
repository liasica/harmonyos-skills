---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-rect
title: OH_Rect
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_Rect
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea8969a618bbd22eaec451925ecca8d9b65fcc249087a07c49a15d15300bab9d
---

```c
typedef struct OH_Rect {...} OH_Rect
```

## 概述

定义录屏界面的位置和尺寸。包含位置坐标和尺寸信息。可用于精确控制录屏范围，支持自定义区域录制、局部录制等场景。

适用于教学/演示录制中只录制重点操作区域、会议录制中只录制演示文稿区域和游戏录制中只录制游戏画面区域等场景。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 录屏界面的X坐标，相对于屏幕左上角。取值需大于等于0，单位为像素（px）。 |
| int32\_t y | 录屏界面的Y坐标，相对于屏幕左上角。取值需大于等于0，单位为像素（px）。 |
| int32\_t width | 录屏区域的宽度，取值需大于0，单位为像素（px）。传入0或负数时录屏不生效。 |
| int32\_t height | 录屏区域的高度，取值需大于0，单位为像素（px）。传入0或负数时录屏不生效。 |
