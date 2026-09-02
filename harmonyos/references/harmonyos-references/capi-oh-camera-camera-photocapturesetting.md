---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photocapturesetting
title: Camera_PhotoCaptureSetting
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_PhotoCaptureSetting
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b665878a8310a879ce5dd6e7dd95455abdc5b36749124b6340b38d2b29c7bc19
---

```c
typedef struct Camera_PhotoCaptureSetting {...} Camera_PhotoCaptureSetting
```

## 概述

要设置的拍照捕获选项。

**起始版本：** 11

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_QualityLevel](capi-camera-h.md#camera_qualitylevel) quality | 拍照图像质量。 |
| [Camera\_ImageRotation](capi-camera-h.md#camera_imagerotation) rotation | 拍照旋转角度。 |
| [Camera\_Location](capi-oh-camera-camera-location.md)\* location | 拍照位置。 |
| bool mirror | 设置镜像拍照功能开关。  true为打开，false为关闭，默认为false。 |
