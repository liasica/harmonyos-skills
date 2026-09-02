---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata
title: AREngine_ARSemanticDenseCubeData
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ARSemanticDenseCubeData
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:17e01756939dd9243ddbb74e3bff3f95042f1e1c7a43057403e7a140ea07191a
---

## 概述

高精几何重建对象的立方体数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [id](arengine-struct-arsemanticdensecubedata.md#id) | 当前立方体的ID。 |
| int32\_t [vertexSize](arengine-struct-arsemanticdensecubedata.md#vertexsize) | 当前立方体的顶点大小。 |
| float\* [vertexData](arengine-struct-arsemanticdensecubedata.md#vertexdata) | 当前立方体的顶点数据。  对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。 |
| float [confidence](arengine-struct-arsemanticdensecubedata.md#confidence) | 当前立方体的置信度。 |
| AREngine\_ARSemanticPlaneLabel [label](arengine-struct-arsemanticdensecubedata.md#label) | 当前立方体的语义标签。  参见[AREngine\_ARSemanticPlaneLabel](arengine-capi-arengine.md#arengine_arsemanticplanelabel)。 |

## 结构体成员变量说明

### id

```cpp
int32_t AREngine_ARSemanticDenseCubeData::id
```

**描述**

当前立方体的ID。

### vertexSize

```cpp
int32_t AREngine_ARSemanticDenseCubeData::vertexSize
```

**描述**

当前立方体的顶点大小。

### vertexData

```cpp
float* AREngine_ARSemanticDenseCubeData::vertexData
```

**描述**

当前立方体的顶点数据。

### confidence

```cpp
float AREngine_ARSemanticDenseCubeData::confidence
```

**描述**

当前立方体的置信度。

### label

```cpp
AREngine_ARSemanticPlaneLabel AREngine_ARSemanticDenseCubeData::label
```

**描述**

当前立方体的语义标签。
