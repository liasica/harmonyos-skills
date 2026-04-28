---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-region
title: Region
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > Region
category: harmonyos-references
scraped_at: 2026-04-28T08:15:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba9740ff2a9f06d8543c7b01a56ab9e0d0ce120b63e8e4989f65fa857b1b3ba8
---

```
1. typedef struct {...} Region
```

## 概述

PhonePC/2in1TabletTVWearable

表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。

**起始版本：** 8

**相关模块：** [NativeWindow](capi-nativewindow.md)

**所在头文件：** [external\_window.h](capi-external-window-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| \* rects | 如果rects是空指针nullptr，默认Buffer大小为脏区。 |
| int32\_t rectNumber | 如果rectNumber为0，默认Buffer大小为脏区。 |
