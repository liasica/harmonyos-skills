---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-config
title: OH_NativeBuffer_Config
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Config
category: harmonyos-references
scraped_at: 2026-04-28T08:15:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:834e09edf3d2ef8b747520a1ac71ebe54d8335ee701795801fbdae6b470eb4ed
---

```
1. typedef struct {...} OH_NativeBuffer_Config
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_NativeBuffer的属性配置，用于申请新的OH\_NativeBuffer实例或查询现有实例的相关属性。

**起始版本：** 9

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [native\_buffer.h](capi-native-buffer-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t width | 宽度（像素）。 |
| int32\_t height | 高度（像素）。 |
| int32\_t format | 像素格式，具体可参见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)枚举。 |
| int32\_t usage | buffer的用途说明，具体可参见[OH\_NativeBuffer\_Usage](capi-native-buffer-h.md#oh_nativebuffer_usage)枚举。 |
| int32\_t stride | 输出参数。本地窗口缓冲区步幅，单位为Byte。  **起始版本：** 10 |
