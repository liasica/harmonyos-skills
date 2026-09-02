---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-colorspaceprimaries
title: ColorSpacePrimaries
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > ColorSpacePrimaries
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:660d5427b1338ebe25b45689055d3c4224c6aef9a564c1fc1a288e772024c695
---

```c
typedef struct {...} ColorSpacePrimaries
```

## 概述

提供色彩原色结构体声明，用于存储色彩空间的红绿蓝三原色和白点的坐标信息。

**起始版本：** 13

**相关模块：** [NativeColorSpaceManager](capi-nativecolorspacemanager.md)

**所在头文件：** [native\_color\_space\_manager.h](capi-native-color-space-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float rX | 红色的x轴坐标值。 |
| float rY | 红色的y轴坐标值。 |
| float gX | 绿色的x轴坐标值。 |
| float gY | 绿色的y轴坐标值。 |
| float bX | 蓝色的x轴坐标值。 |
| float bY | 蓝色的y轴坐标值。 |
| float wX | 白点的x轴坐标值。 |
| float wY | 白点的y轴坐标值。 |
