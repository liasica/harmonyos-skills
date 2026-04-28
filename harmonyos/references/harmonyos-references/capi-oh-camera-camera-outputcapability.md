---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-outputcapability
title: Camera_OutputCapability
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_OutputCapability
category: harmonyos-references
scraped_at: 2026-04-28T08:12:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:151025387fc86daeebf68c5d8510b20a77ebf9b004829f2b5a27e5df6a93f37c
---

```
1. typedef struct Camera_OutputCapability {...} Camera_OutputCapability
```

## 概述

PhonePC/2in1TabletTVWearable

相机输出能力。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_Profile](capi-oh-camera-camera-profile.md)\*\* previewProfiles | 预览配置文件列表。 |
| uint32\_t previewProfilesSize | 预览配置文件列表的大小。 |
| [Camera\_Profile](capi-oh-camera-camera-profile.md)\*\* photoProfiles | 拍照配置文件列表。  配置文件中的size设置的是相机分辨率宽高，非实际出图宽高。 |
| uint32\_t photoProfilesSize | 拍照配置文件列表的大小。 |
| [Camera\_VideoProfile](capi-oh-camera-camera-videoprofile.md)\*\* videoProfiles | 录像配置文件列表。 |
| uint32\_t videoProfilesSize | 录像配置文件列表的大小。 |
| [Camera\_MetadataObjectType](capi-camera-h.md#camera_metadataobjecttype)\*\* supportedMetadataObjectTypes | 元数据对象类型列表。 |
| uint32\_t metadataProfilesSize | 元数据对象类型列表的大小。 |
