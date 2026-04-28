---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-spatialrecon-hms-spatialrecon-dataframe
title: HMS_SpatialRecon_DataFrame
breadcrumb: API参考 > 图形 > Spatial Recon Kit（空间建模服务） > C API > 结构体 > HMS_SpatialRecon_DataFrame
category: harmonyos-references
scraped_at: 2026-04-28T08:15:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68cca6849473f7f9ba181698d455fee4f2c4eca4ac2f7aeb56b682d3b3fd7a06
---

```
1. typedef struct HMS_SpatialRecon_DataFrame {...} HMS_SpatialRecon_DataFrame
```

## 概述

定义HMS（Huawei Mobile Services）空间重建数据帧的结构体，包含用于空间重建的相机内参、姿态信息、时间戳和图像数据。

**起始版本：** 6.1.0(23)

**相关模块：** [SpatialRecon](capi-spatialrecon.md)

**所在头文件：** [spatial\_recon\_interface.h](capi-spatial-recon-interface-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float focalX = 0.0f | X轴方向的焦距，单位：px。 |
| float focalY = 0.0f | Y轴方向的焦距，单位：px。 |
| float principalX = 0.0f | 主点X坐标（光心），单位：px。 |
| float principalY = 0.0f | 主点Y坐标（光心），单位：px。 |
| float distortionCoef[8] | 失真参数 [k1, k2, p1, p2, k3, k4, k5, k6]。 |
| int32\_t imageWidth = 0.0f | 图像的宽度，单位：px。 |
| int32\_t imageHeight = 0.0f | 图像的高度，单位：px。 |
| float position[3] | 相机在3D空间中的位置 [x, y, z]。 |
| float rotation[4] | 相机旋转，表示为四元数 [x, y, z, w]。 |
| int64\_t timestamp = 0 | 帧捕获的时间戳，单位：ns。 |
| uint8\_t \*imageData = 0 | 指向原始图像像素数据的指针。 |
| HMS\_SpatialReconImageDataFormat format = SPATIAL\_RECON\_IMAGEDATA\_FORMAT\_RGB | 图像数据的格式/编码。 |
