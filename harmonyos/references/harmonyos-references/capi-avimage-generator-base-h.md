---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimage-generator-base-h
title: avimage_generator_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avimage_generator_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9da31a978feb38fd2ae158b54ead3d0c88fda7252e8983c171b7cb24d1ed2fcf
---

## 概述

定义AVImageGenerator的枚举。

**引用文件：** <multimedia/player\_framework/avimage\_generator\_base.h>

**库：** libavimage\_generator.so

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**相关模块：** [AVImageGenerator](capi-avimagegenerator.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVImageGenerator\_QueryOptions](capi-avimage-generator-base-h.md#oh_avimagegenerator_queryoptions) | OH\_AVImageGenerator\_QueryOptions | 指定查询视频帧时，时间点与帧对应关系选项的枚举类型。 |

## 枚举类型说明

### OH\_AVImageGenerator\_QueryOptions

```c
enum OH_AVImageGenerator_QueryOptions
```

**描述**

指定查询视频帧时，时间点与帧对应关系选项的枚举类型。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_NEXT\_SYNC = 0 | 此选项用于选取传入时间点或之后的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_PREVIOUS\_SYNC = 1 | 此选项用于选取传入时间点或之前的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST\_SYNC = 2 | 此选项用于选取离传入时间点最近的关键帧。 |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST = 3 | 此选项用于选取离传入时间点最近的帧，该帧不一定是关键帧。 |
