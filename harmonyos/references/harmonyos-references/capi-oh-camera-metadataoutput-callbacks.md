---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks
title: MetadataOutput_Callbacks
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > MetadataOutput_Callbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:da4daf5c2a3064ea295e0e90bfbe206423c98b90da6f61ac24344932b568687b
---

```c
typedef struct MetadataOutput_Callbacks {...} MetadataOutput_Callbacks
```

## 概述

元数据输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [metadata\_output.h](capi-metadata-output-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_MetadataOutput\_OnMetadataObjectAvailable](capi-metadata-output-h.md#oh_metadataoutput_onmetadataobjectavailable) onMetadataObjectAvailable | 此回调将调用元数据输出结果数据。 |
| [OH\_MetadataOutput\_OnError](capi-metadata-output-h.md#oh_metadataoutput_onerror) onError | 元数据输出错误事件。 |
