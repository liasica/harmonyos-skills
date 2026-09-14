---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadatatemplate
title: OH_AVRecorder_MetadataTemplate
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_MetadataTemplate
category: harmonyos-references
scraped_at: 2026-09-15T07:08:14+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:3dd531a4750694dc1730e71182ec73f78a93716056811c1fe8544f838a159a5c
---

```c
typedef struct OH_AVRecorder_MetadataTemplate {...} OH_AVRecorder_MetadataTemplate
```

## 概述

定义音视频录制过程中元数据的基本模板，通过键值对（key-value）形式组织元数据，适用于需要在录制输出中附加自定义元数据（如标题、作者、描述等）的场景，便于对录制文件进行分类、检索和管理。开发者可通过AVRecorder的[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口将该结构体中的元数据设置到录制输出文件中。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*key | 元数据的键。 |
| char \*value | 元数据的值。 |
