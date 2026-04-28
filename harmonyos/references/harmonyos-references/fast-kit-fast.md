---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast
title: FAST
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 模块 > FAST
category: harmonyos-references
scraped_at: 2026-04-28T08:10:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:35738de5f0818379c1d79103c903e339918c22bd86bbd4a53a7a280a5a03abd8
---

## 概述

PhonePC/2in1Tablet

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。

**起始版本：** 6.0.2(22)

## 汇总

PhonePC/2in1Tablet

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [fast\_ads\_segment\_map.h](fast-kit-fast-ads-segment-map-8h.md) | 线段表相关数据结构及函数定义。 |
| [fast\_common\_def.h](fast-kit-fast-common-def-8h.md) | FAST Kit错误码等类型的公共定义。 |
| [fast\_solver\_rect\_partition.h](fast-kit-fast-solver-rect-partition-8h.md) | 矩形划分求解器相关数据结构及函数定义。 |

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_Rect](fast-kit--fast-rect.md) | 定义矩形的数据结构。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef enum [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype-1) [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype) | 线段表支持的查询操作类型。 |
| typedef enum [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype-1) [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype) | 线段表支持的更新操作类型。 |
| typedef struct [FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) [FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void \* [FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) | 线段表的句柄。 |
| typedef enum [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode) | FAST Kit的错误码。 |
| typedef struct [FAST\_Rect](fast-kit--fast-rect.md) [FAST\_Rect](fast-kit-fast.md#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype-1) { FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM = 0, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN = 1, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX = 2 } | 线段表支持的查询操作类型。 |
| [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype-1) { FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET = 0, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD = 1, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB = 2 } | 线段表支持的更新操作类型。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) {  FAST\_ERROR\_CODE\_SUCCESS = 1023100000, FAST\_ERROR\_CODE\_FAIL = 1023100001, FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002, FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003,  FAST\_ERROR\_CODE\_OOM = 1023199001  } | FAST Kit的错误码。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_CreateConfig](fast-kit-fast.md#hms_fast_segmentmap_createconfig) ([FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) \*\*config) | 创建线段表不透明配置实例。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](fast-kit-fast.md#hms_fast_segmentmap_destroyconfig) ([FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) \*config) | 销毁线段表的不透明配置实例并释放内存。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetQueryType](fast-kit-fast.md#hms_fast_segmentmap_setquerytype) ([FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) \*config, [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype-1) type) | 设置线段表不透明配置中的查询类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetUpdateType](fast-kit-fast.md#hms_fast_segmentmap_setupdatetype) ([FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) \*config, [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype-1) type) | 设置线段表不透明配置中的更新类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Create](fast-kit-fast.md#hms_fast_segmentmap_create) ([FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) \*config) | 创建线段表。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](fast-kit-fast.md#hms_fast_segmentmap_destroy) ([FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) handle) | 销毁线段表实例。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Update](fast-kit-fast.md#hms_fast_segmentmap_update) ([FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t value) | 更新线段表的区间。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Query](fast-kit-fast.md#hms_fast_segmentmap_query) ([FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t \*result) | 查询线段表的区间。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](fast-kit-fast.md#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](fast-kit-fast.md#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](fast-kit-fast.md#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST\_EXPORT [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](fast-kit-fast.md#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](fast-kit--fast-rect.md) \*origin, [FAST\_Rect](fast-kit--fast-rect.md) \*result, size\_t \*resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。  **说明**：  1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。  2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |

## 类型定义说明

PhonePC/2in1Tablet

### FAST\_ErrorCode

PhonePC/2in1Tablet

```
1. typedef enum FAST_ErrorCode FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

### FAST\_Rect

PhonePC/2in1Tablet

```
1. typedef struct FAST_Rect FAST_Rect
```

**描述**

定义矩形的数据结构。

**起始版本：** 6.0.2(22)

### FAST\_RectPartitionConfig

PhonePC/2in1Tablet

```
1. typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig
```

**描述**

矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapConfig

PhonePC/2in1Tablet

```
1. typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig
```

**描述**

线段表的不透明配置（Opaque Configuration）。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapHandle

PhonePC/2in1Tablet

```
1. typedef void* FAST_SegmentMapHandle
```

**描述**

线段表的句柄。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapQueryType

PhonePC/2in1Tablet

```
1. typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType
```

**描述**

线段表数据结构支持的区间查询操作类型。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapUpdateType

PhonePC/2in1Tablet

```
1. typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType
```

**描述**

线段表数据结构支持的区间更新操作类型。

**起始版本：** 6.0.2(22)

## 枚举类型说明

PhonePC/2in1Tablet

### FAST\_ErrorCode

PhonePC/2in1Tablet

```
1. enum FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| FAST\_ERROR\_CODE\_SUCCESS = 1023100000 | 成功。 |
| FAST\_ERROR\_CODE\_FAIL = 1023100001 | 失败。 |
| FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002 | 非法输入。 |
| FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003 | 无效指针（例如 NULL)。 |
| FAST\_ERROR\_CODE\_OOM = 1023199001 | 内存溢出。 |

### FAST\_SegmentMapQueryType

PhonePC/2in1Tablet

```
1. enum FAST_SegmentMapQueryType
```

**描述**

线段表支持的查询操作类型。

该枚举定义了线段表数据结构能够处理的各种区间查询操作。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM | 区间求和查询。 |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN | 区间最小值查询。 |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX | 区间最大值查询。 |

### FAST\_SegmentMapUpdateType

PhonePC/2in1Tablet

```
1. enum FAST_SegmentMapUpdateType
```

**描述**

线段表支持的更新操作类型。

该枚举定义了线段表数据结构能够处理的各种区间更新操作。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET | 赋值更新，区间内的每一个元素赋同一个值。 |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD | 加法更新，区间内的每一个元素加同一个值。 |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB | 减法更新，区间内的每一个元素减同一个值。 |

## 函数说明

PhonePC/2in1Tablet

### HMS\_FAST\_RectPartition\_CreateConfig()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig ** config)
```

**描述**

创建矩形划分求解器的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向矩形划分求解器不透明配置[FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig)的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_RectPartition\_DestroyConfig()

PhonePC/2in1Tablet

```
1. FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig * config)
```

**描述**

销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁的矩形划分求解器的不透明配置[FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig)。 |

### HMS\_FAST\_RectPartition\_SetAlgo()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig * config, const char * name )
```

**描述**

设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为O(N logN)。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待设置的矩形划分求解器的不透明配置[FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig)。 |
| name | 矩形求解器使用的算法名称。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config或name为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当算法不支持时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_RectPartition\_Solve()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig * config, size_t size, const FAST_Rect * origin, FAST_Rect * result, size_t * resultSize )
```

**描述**

在指定不透明配置下求解矩形划分问题。在调用函数之前需要先初始化参数中的结果数组result。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 矩形划分求解器的不透明配置。如果参数config中未设置算法，默认的算法是扫描线算法“SweepLineAlgo”。 |
| size | 待划分的矩形[FAST\_Rect](fast-kit--fast-rect.md)数量。 |
| origin | 待划分的矩形[FAST\_Rect](fast-kit--fast-rect.md)源数组。 |
| result | 由矩形划分求解器得到的[FAST\_Rect](fast-kit--fast-rect.md)结果，在调用函数之前需要初始化该结果数组，大小需要和源数组相等，否则可能导致溢出。 |
| resultSize | 划分之后的[FAST\_Rect](fast-kit--fast-rect.md)数量。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当入参指针为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)，如矩形存在相交。

当算法求解失败时，返回[FAST\_ERROR\_CODE\_FAIL](fast-kit-fast.md#fast_errorcode-1)。

**注解：**

1. 当选择“SweepLineAlgo”时，不应该返回[FAST\_ERROR\_CODE\_FAIL](fast-kit-fast.md#fast_errorcode-1)，此处仅作为预防性设置。

### HMS\_FAST\_SegmentMap\_Create()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle * handle, size_t size, const int32_t * array, FAST_SegmentMapConfig * config )
```

**描述**

创建线段表。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 指向线段表句柄[FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle)的指针。 |
| size | 底层数组的大小（元素数量）。 |
| array | 可选；用于初始化线段表的底层数组。如果为NULL，则线段表中的元素均初始化为0，否则数组大小必须与参数size保持一致。 |
| config | 线段表的不透明配置[FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig)，若该参数为NULL或未配置，默认查询类型为[FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM](fast-kit-fast.md#fast_segmentmapquerytype-1)、更新类型为[FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET](fast-kit-fast.md#fast_segmentmapupdatetype-1)。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config或handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_SegmentMap\_CreateConfig()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig ** config)
```

**描述**

创建线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向线段表不透明配置[FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig)的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_SegmentMap\_Destroy()

PhonePC/2in1Tablet

```
1. FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle)
```

**描述**

销毁线段表实例。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 待销毁线段表句柄[FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle)。 |

### HMS\_FAST\_SegmentMap\_DestroyConfig()

PhonePC/2in1Tablet

```
1. FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig * config)
```

**描述**

销毁线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁线段表不透明配置[FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig)。 |

### HMS\_FAST\_SegmentMap\_Query()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t * result )
```

**描述**

查询线段表的区间。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间左闭右开。 |
| right | 区间右端点 （不包含），区间左闭右开。 |
| result | 根据区间查询的结果。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)，如左端点大于等于右端点。

### HMS\_FAST\_SegmentMap\_SetQueryType()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig * config, FAST_SegmentMapQueryType type )
```

**描述**

设置线段表不透明配置中的查询类型。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 查询类型。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_SegmentMap\_SetUpdateType()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig * config, FAST_SegmentMapUpdateType type )
```

**描述**

设置线段表不透明配置中的更新类型。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待修改的线段表不透明配置。 |
| type | 更新类型。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_SegmentMap\_Update()

PhonePC/2in1Tablet

```
1. FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value )
```

**描述**

更新线段表的区间。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间为左闭右开。 |
| right | 区间右端点 （不包含），区间为左闭右开。 |
| value | 待更新的值。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)，如左端点大于等于右端点。
