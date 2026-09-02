---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-polarposition
title: OH_PolarPosition
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_PolarPosition
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cfe8e8cdca5430e36762e5e0d5e45effa34948c5a98f927c2d028c284b2f5a3f
---

```c
typedef struct OH_PolarPosition {...} OH_PolarPosition
```

## 概述

表示极坐标系（polar coordinate system，也叫球坐标系）中的位置。极坐标系使用方位角、俯仰角和距离定义对象声源在三维空间中的位置。

**起始版本：** 26.0.0

**相关模块：** [Core](capi-core.md)

**所在头文件：** [native\_audio\_vivid.h](capi-native-audio-vivid-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float azimuth | 极坐标系下对象声源所在位置的方位角。  取值范围为[-180.0, 180.0]，其中0.0表示正前方，90.0表示左侧，-90.0表示右侧，-180.0或180.0表示正后方。 |
| float elevation | 极坐标系下对象声源所在位置的俯仰角。  取值范围为[-90.0, 90.0]，其中0.0表示水平，90.0表示正上方，-90.0表示正下方。 |
| float distance | 极坐标系下对象声源所在位置的归一化距离。  取值范围为[0.0, 1.0]。 |
