---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-cartesianposition
title: OH_CartesianPosition
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_CartesianPosition
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3de41034ed383a9b0620712e9a530e9f630eac15e6dad92d77dd01bc579de856
---

```c
typedef struct OH_CartesianPosition {...} OH_CartesianPosition
```

## 概述

表示对象声源在笛卡尔坐标系（Cartesian coordinate system）中的位置。笛卡尔坐标系使用x、y、z轴定义三维空间中的位置。

**起始版本：** 26.0.0

**相关模块：** [Core](capi-core.md)

**所在头文件：** [native\_audio\_vivid.h](capi-native-audio-vivid-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | 对象声源在笛卡尔坐标系中的归一化（Normalization，将数值按比例转换到指定范围内）X坐标，表示左/右维度。  取值范围为[-1.0, 1.0]。 |
| float y | 对象声源在笛卡尔坐标系中的归一化Y坐标，表示前/后维度。  取值范围为[-1.0, 1.0]。 |
| float z | 对象声源在笛卡尔坐标系中的归一化Z坐标，表示上/下维度。  取值范围为[-1.0, 1.0]。 |
