---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photocapturesetting
title: Camera_PhotoCaptureSetting
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_PhotoCaptureSetting
category: harmonyos-references
scraped_at: 2026-04-28T08:12:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:066d149b01dfe8b9eb70475ec01c98c4642d3e1bd493c8b82324529506919fa3
---

```
1. typedef struct Camera_PhotoCaptureSetting {...} Camera_PhotoCaptureSetting
```

## 概述

PhonePC/2in1TabletTVWearable

要设置的拍照捕获选项。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Camera\_QualityLevel](capi-camera-h.md#camera_qualitylevel) quality | 拍照图像质量。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation) rotation | 拍照旋转角度。 |
| [Camera\_Location](capi-oh-camera-camera-location.md)\* location | 拍照位置。 |
| bool mirror | 设置镜像拍照功能开关。  true为打开，false为关闭，默认为false。 |
