---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-audioobjectposition
title: OH_AudioObjectPosition
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AudioObjectPosition
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9b695581315b473680332615409a2c959110dcf017cde59d649af3069f349182
---

```c
typedef struct OH_AudioObjectPosition {...} OH_AudioObjectPosition
```

## 概述

表示音频对象声源在三维空间中的位置。该位置可以用笛卡尔坐标或极坐标表示。

**起始版本：** 26.0.0

**相关模块：** [Core](capi-core.md)

**所在头文件：** [native\_audio\_vivid.h](capi-native-audio-vivid-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool isCartesian | 对象声源是否使用笛卡尔坐标表示。  true表示使用笛卡尔坐标，false表示不使用笛卡尔坐标系，使用极坐标系。 |
| union {  [OH\_CartesianPosition](capi-core-oh-cartesianposition.md) cartesian;  [OH\_PolarPosition](capi-core-oh-polarposition.md) polar;  } pos | 包含笛卡尔坐标或极坐标位置数据的联合体。  cartesian：笛卡尔坐标表示的位置。  polar：极坐标表示的位置。 |
