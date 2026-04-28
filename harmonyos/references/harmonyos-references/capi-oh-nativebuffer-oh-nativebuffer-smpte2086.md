---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-smpte2086
title: OH_NativeBuffer_Smpte2086
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Smpte2086
category: harmonyos-references
scraped_at: 2026-04-28T08:15:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6af7bb5c8c55cc38a8bb6abd71cc3e5715f2b1e67ba1b7518e21b18576f12427
---

```
1. typedef struct OH_NativeBuffer_Smpte2086 {...} OH_NativeBuffer_Smpte2086
```

## 概述

PhonePC/2in1TabletTVWearable

表示smpte2086静态元数据。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [buffer\_common.h](capi-buffer-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryRed | 红基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryGreen | 绿基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryBlue | 蓝基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) whitePoint | 白点。 |
| float maxLuminance | 最大的光亮度。 |
| float minLuminance | 最小的光亮度。 |
