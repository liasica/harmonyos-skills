---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensepointdata
title: AREngine_ARSemanticDensePointData
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > C API > 头文件和结构体 > 结构体 > AREngine_ARSemanticDensePointData
category: harmonyos-references
scraped_at: 2026-04-28T08:14:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:660a718bd394f0cbbc0bb5e310dd69bb7da7a5968b652a0c3d68a619dfe7cf1d
---

## 概述

PhoneTabletTV

高精几何重建对象的稠密点云数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquirePointData](arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirepointdata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](arengine-capi-arengine.md)

**所在头文件：** [ar\_engine\_core.h](arengine-header-file.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

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

PhoneTabletTV

### id

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDensePointData::id
```

**描述**

当前点的ID。

### x

PhoneTabletTV

```
1. float AREngine_ARSemanticDensePointData::x
```

**描述**

当前点的X坐标。

### y

PhoneTabletTV

```
1. float AREngine_ARSemanticDensePointData::y
```

**描述**

当前点的Y坐标。

### z

PhoneTabletTV

```
1. float AREngine_ARSemanticDensePointData::z
```

**描述**

当前点的Z坐标。

### r

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDensePointData::r
```

**描述**

当前点的颜色，RGBA表示，这里是R的值。

### g

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDensePointData::g
```

**描述**

当前点的颜色，RGBA表示，这里是G的值。

### b

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDensePointData::b
```

**描述**

当前点的颜色，RGBA表示，这里是B的值。

### a

PhoneTabletTV

```
1. int32_t AREngine_ARSemanticDensePointData::a
```

**描述**

当前点的颜色，RGBA表示，这里是A的值。

### confidence

PhoneTabletTV

```
1. float AREngine_ARSemanticDensePointData::confidence
```

**描述**

当前点的置信度。
