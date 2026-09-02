---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-types-h
title: media_types.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > media_types.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:72116a98f544b7ee404e3ce01b9523c65141adb73e96225fb6b7218a75ee47ae
---

## 概述

声明了常见媒体类型的定义。

**引用文件：** <multimedia/player\_framework/media\_types.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 18

**相关模块：** [Core](capi-core.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Core\_HdrType](capi-media-types-h.md#oh_core_hdrtype) | OH\_Core\_HdrType | HDR类型枚举。 |

## 枚举类型说明

### OH\_Core\_HdrType

```c
enum OH_Core_HdrType
```

**描述**

HDR类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| OH\_CORE\_HDR\_TYPE\_NONE = 0 | 此选项用于标记非HDR类型。 |
| OH\_CORE\_HDR\_TYPE\_VIVID = 1 | 此选项用于标记HDR Vivid类型。 |
