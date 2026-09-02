---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-smpte2086
title: OH_NativeBuffer_Smpte2086
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Smpte2086
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f4a0281adc184ddfa42462ebbb963c130474359e40354a6c3dca901117701b50
---

```c
typedef struct OH_NativeBuffer_Smpte2086 {...} OH_NativeBuffer_Smpte2086
```

## 概述

表示SMPTE 2086静态元数据。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [buffer\_common.h](capi-buffer-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryRed | 红基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryGreen | 绿基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) displayPrimaryBlue | 蓝基色。 |
| [OH\_NativeBuffer\_ColorXY](capi-oh-nativebuffer-oh-nativebuffer-colorxy.md) whitePoint | 白点。 |
| float maxLuminance | 最大的光亮度。 |
| float minLuminance | 最小的光亮度。 |
