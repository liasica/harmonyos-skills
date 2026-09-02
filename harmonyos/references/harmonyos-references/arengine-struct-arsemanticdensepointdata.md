---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensepointdata
title: AREngine_ARSemanticDensePointData
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ARSemanticDensePointData
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:20e314021c6bb132f547bdda49b01664752a8575eba205556f966e6433950828
---

## 概述

高精几何重建对象的稠密点云数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquirePointData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirepointdata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [id](arengine-struct-arsemanticdensepointdata.md#id) | 当前点的ID。 |
| float [x](arengine-struct-arsemanticdensepointdata.md#x) | 当前点的X坐标。 |
| float [y](arengine-struct-arsemanticdensepointdata.md#y) | 当前点的Y坐标。 |
| float [z](arengine-struct-arsemanticdensepointdata.md#z) | 当前点的Z坐标。 |
| int32\_t [r](arengine-struct-arsemanticdensepointdata.md#r) | 当前点的颜色，RGBA表示，这里是R的值。 |
| int32\_t [g](arengine-struct-arsemanticdensepointdata.md#g) | 当前点的颜色，RGBA表示，这里是G的值。 |
| int32\_t [b](arengine-struct-arsemanticdensepointdata.md#b) | 当前点的颜色，RGBA表示，这里是B的值。 |
| int32\_t [a](arengine-struct-arsemanticdensepointdata.md#a) | 当前点的颜色，RGBA表示，这里是A的值。 |
| float [confidence](arengine-struct-arsemanticdensepointdata.md#confidence) | 当前点的置信度。 |

## 结构体成员变量说明

### id

```cpp
int32_t AREngine_ARSemanticDensePointData::id
```

**描述**

当前点的ID。

### x

```cpp
float AREngine_ARSemanticDensePointData::x
```

**描述**

当前点的X坐标。

### y

```cpp
float AREngine_ARSemanticDensePointData::y
```

**描述**

当前点的Y坐标。

### z

```cpp
float AREngine_ARSemanticDensePointData::z
```

**描述**

当前点的Z坐标。

### r

```cpp
int32_t AREngine_ARSemanticDensePointData::r
```

**描述**

当前点的颜色，RGBA表示，这里是R的值。

### g

```cpp
int32_t AREngine_ARSemanticDensePointData::g
```

**描述**

当前点的颜色，RGBA表示，这里是G的值。

### b

```cpp
int32_t AREngine_ARSemanticDensePointData::b
```

**描述**

当前点的颜色，RGBA表示，这里是B的值。

### a

```cpp
int32_t AREngine_ARSemanticDensePointData::a
```

**描述**

当前点的颜色，RGBA表示，这里是A的值。

### confidence

```cpp
float AREngine_ARSemanticDensePointData::confidence
```

**描述**

当前点的置信度。
