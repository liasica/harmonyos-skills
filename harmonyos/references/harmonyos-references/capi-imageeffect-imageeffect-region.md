---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect-imageeffect-region
title: ImageEffect_Region
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageEffect_Region
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2ba0c1304dbbd9f0c37bc29921d9712b7da75d7edd424b18bfd5f4776715242e
---

```c
typedef struct ImageEffect_Region {...} ImageEffect_Region
```

## 概述

图像区域结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](capi-imageeffect.md)

**所在头文件：** [image\_effect\_filter.h](capi-image-effect-filter-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x0 | X轴起始坐标。 |
| int32\_t y0 | Y轴起始坐标。 |
| int32\_t x1 | X轴终止坐标。 |
| int32\_t y1 | Y轴终止坐标。 |
