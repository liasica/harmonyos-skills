---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadata
title: OH_AVRecorder_Metadata
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Metadata
category: harmonyos-references
scraped_at: 2026-04-28T08:13:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:291c83a87b5d2811c01942fa513ee5ff2e5b8980dec9a38eea45b3dd152da516
---

```
1. typedef struct OH_AVRecorder_Metadata {...} OH_AVRecorder_Metadata
```

## 概述

PhonePC/2in1TabletTVWearable

元数据信息数据结构。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* genre | 媒体资源的类型或体裁。 |
| char\* videoOrientation | 视频的旋转方向，单位为度。 |
| [OH\_AVRecorder\_Location](capi-avrecorder-oh-avrecorder-location.md) location | 视频的地理位置信息。 |
| [OH\_AVRecorder\_MetadataTemplate](capi-avrecorder-oh-avrecorder-metadatatemplate.md) customInfo | 从 moov.meta.list 读取的自定义参数键值映射。 |
