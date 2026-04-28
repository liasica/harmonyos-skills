---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-rect
title: OH_Rect
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_Rect
category: harmonyos-references
scraped_at: 2026-04-28T08:14:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a87eec2d06d9930f5be1e03c2cda3700df201301c2e699853c27f3ebf10fbf54
---

```
1. typedef struct OH_Rect {...} OH_Rect
```

## 概述

PhonePC/2in1TabletTV

定义录屏界面的宽高以及画面信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 录屏界面的X坐标。 |
| int32\_t y | 录屏界面的Y坐标。 |
| int32\_t width | 录屏界面的宽度，单位px。 |
| int32\_t height | 录屏界面的高度，单位px。 |
