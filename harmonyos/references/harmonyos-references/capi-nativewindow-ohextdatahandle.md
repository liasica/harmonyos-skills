---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohextdatahandle
title: OHExtDataHandle
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OHExtDataHandle
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b3c8f9cf453d29e0df88739e406e6a6568a8e3acf97ada343c6f11aeb2acaf8
---

```c
typedef struct OHExtDataHandle {...} OHExtDataHandle
```

## 概述

扩展数据句柄结构体定义。

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**相关模块：** [NativeWindow](capi-nativewindow.md)

**所在头文件：** [external\_window.h](capi-external-window-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t fd | 句柄 Fd，-1代表不支持。 |
| uint32\_t reserveInts | Reserve数组的个数。 |
| int32\_t reserve[0] | Reserve数组。 |
