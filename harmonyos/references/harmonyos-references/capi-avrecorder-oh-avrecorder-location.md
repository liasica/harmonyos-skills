---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-location
title: OH_AVRecorder_Location
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Location
category: harmonyos-references
scraped_at: 2026-09-02T15:02:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fa87427c99cfe2c0f387617818bc0a3c44ad96c7c30a8c550b4fcbb701005fb8
---

```c
typedef struct OH_AVRecorder_Location {...} OH_AVRecorder_Location
```

## 概述

提供媒体资源的地理位置信息，支持在音视频录制过程中标注纬度和经度。该结构体通过AVRecorder的[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口将经纬度信息写入录制文件的元数据中，开发者需在录制前设置该结构体的latitude和longitude参数，录制过程中地理位置信息将自动嵌入到生成的媒体文件中。适用于需要在录制结果中嵌入地理位置的场景，如在视频拍摄时标记拍摄地点、运动记录应用中标记轨迹位置、旅行日记应用中记录行程坐标等，便于后续按位置检索和分类管理媒体资源。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float latitude | 纬度，取值范围[-90, 90]，单位：度（°）。需与longitude配合使用以提供完整的地理位置信息，超出范围时将导致错误。 |
| float longitude | 经度，取值范围[-180, 180]，单位：度（°）。需与latitude配合使用以提供完整的地理位置信息，超出范围时将导致错误。 |
