---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata
title: AREngine_ARSemanticDenseCubeData
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ARSemanticDenseCubeData
category: harmonyos-references
scraped_at: 2026-04-28T08:14:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:15f2c3d82b25a362de618c61bf178b44a5c8a9c4e2909cf54fcd2a3785f7c78c
---

## 概述

PhoneTabletTV

高精几何重建对象的立方体数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t [id](arengine-struct-arsemanticdensecubedata.md#id) | 当前立方体的ID。 |
| int32\_t [vertexSize](arengine-struct-arsemanticdensecubedata.md#vertexsize) | 当前立方体的顶点大小。 |
| float\* [vertexData](arengine-struct-arsemanticdensecubedata.md#vertexdata) | 当前立方体的顶点数据。  对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。 |
| float [confidence](arengine-struct-arsemanticdensecubedata.md#confidence) | 当前立方体的置信度。 |
| AREngine\_ARSemanticPlaneLabel [label](arengine-struct-arsemanticdensecubedata.md#label) | 当前立方体的语义标签。  参见[AREngine\_ARSemanticPlaneLabel](arengine-capi-arengine.md#arengine_arsemanticplanelabel)。 |

## 结构体成员变量说明

PhoneTabletTV

### id

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDenseCubeData::id
```

**描述**

当前立方体的ID。

### vertexSize

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDenseCubeData::vertexSize
```

**描述**

当前立方体的顶点大小。

### vertexData

PhoneTabletTV

```
1. float* AREngine_ARSemanticDenseCubeData::vertexData
```

**描述**

当前立方体的顶点数据。

### confidence

PhoneTabletTV

```
1. float AREngine_ARSemanticDenseCubeData::confidence
```

**描述**

当前立方体的置信度。

### label

PhoneTabletTV

```
1. AREngine_ARSemanticPlaneLabel AREngine_ARSemanticDenseCubeData::label
```

**描述**

当前立方体的语义标签。
