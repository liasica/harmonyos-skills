---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast
title: FAST
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 模块 > FAST
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ecf6480e65b9e93b5541badfa2c7bfc46260bad7bb6f9fb232a21b62fb691330
---

## 概述

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。

**起始版本：** 6.0.2(22)

## 汇总

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。

### 文件

| 名称 | 描述 |
| --- | --- |
| [fast\_ads\_segment\_map.h](fast-kit-fast-ads-segment-map-8h.md) | 线段表相关数据结构及函数定义。 |
| [fast\_ads\_concurrent\_hashmap.h](fast-kit-fast-ads-concurrent-hashmap-8h.md) | 并发哈希表相关数据结构及函数定义。 |
| [fast\_common\_def.h](fast-kit-fast-common-def-8h.md) | FAST Kit错误码等类型的公共定义。 |
| [fast\_dsp\_common.h](fast-kit-fast-dsp-common-8h.md) | 数字信号处理（DSP）通用数据结构和工具函数定义。 |
| [fast\_dsp\_transform.h](fast-kit-fast-dsp-transform-8h.md) | 数字信号处理（DSP）变换函数定义，包括FFT、IFFT等。 |
| [fast\_solver\_rect\_partition.h](fast-kit-fast-solver-rect-partition-8h.md) | 矩形划分求解器相关数据结构及函数定义。 |
| [fast\_solver\_polynomial.h](fast-kit-fast-solver-polynomial-8h.md) | 多项式零点求解器相关数据结构及函数定义。 |
| [fast\_collections\_hashmap.h](fast-kit-fast-collections-hashmap-8h.md) | 适用于单线程场景的哈希表相关数据结构及函数定义。 |
| [fast\_utils\_algorithm.h](fast-kit-fast-utils-algorithm-8h.md) | 通用算法实现，目前提供排序相关的数据结构和函数定义。 |
| [scheduling\_optimization.h](fast-kit-scheduling-optimization-8h.md) | 系统性能优化相关数据结构及函数定义。 |

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_Rect](fast-kit--fast-rect.md) | 定义矩形的数据结构。 |
| struct [FAST\_Poly](fast-kit--fast-poly.md) | 定义稀疏格式多项式的数据结构。 |
| struct [FAST\_SplitComplex](fast-kit--fast-splitcomplex.md) | 定义单精度浮点复数信号的数据结构（分离格式）。 |
| struct [FAST\_SplitComplexD](fast-kit--fast-splitcomplexd.md) | 定义双精度浮点复数信号的数据结构（分离格式）。 |
| struct [FAST\_BiquadCoefficients](fast-kit--fast-biquadcoefficients.md) | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadCoefficientsD](fast-kit--fast-biquadcoefficientsd.md) | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadState](fast-kit--fast-biquadstate.md) | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_BiquadStateD](fast-kit--fast-biquadstated.md) | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_Biquadm](fast-kit--fast-biquadm.md) | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct [FAST\_BiquadmD](fast-kit--fast-biquadmd.md) | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct [HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) | 定义待排序的连续数据块的数据结构。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype-1) [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype) | 线段表支持的查询操作类型。 |
| typedef enum [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype-1) [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype) | 线段表支持的更新操作类型。 |
| typedef struct [FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) [FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig) | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void \* [FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle) | 线段表的句柄。 |
| typedef enum [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode) | FAST Kit的错误码。 |
| typedef enum [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1) [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype) | 汉宁窗类型枚举。 |
| typedef struct [FAST\_Rect](fast-kit--fast-rect.md) [FAST\_Rect](fast-kit-fast.md#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST\_Poly](fast-kit--fast-poly.md) [FAST\_Poly](fast-kit-fast.md#fast_poly) | 定义稀疏格式多项式的数据结构。 |
| typedef struct [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) [FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |
| typedef struct [FAST\_SplitComplex](fast-kit--fast-splitcomplex.md) [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) | 单精度浮点复数信号结构体。 |
| typedef struct [FAST\_SplitComplexD](fast-kit--fast-splitcomplexd.md) [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) | 双精度浮点复数信号结构体。 |
| typedef struct [FAST\_BiquadCoefficients](fast-kit--fast-biquadcoefficients.md) [FAST\_BiquadCoefficients](fast-kit-fast.md#fast_biquadcoefficients) | 单精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadCoefficientsD](fast-kit--fast-biquadcoefficientsd.md) [FAST\_BiquadCoefficientsD](fast-kit-fast.md#fast_biquadcoefficientsd) | 双精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadState](fast-kit--fast-biquadstate.md) [FAST\_BiquadState](fast-kit-fast.md#fast_biquadstate) | 单精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_BiquadStateD](fast-kit--fast-biquadstated.md) [FAST\_BiquadStateD](fast-kit-fast.md#fast_biquadstated) | 双精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_Biquadm](fast-kit--fast-biquadm.md) [FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) | 单精度多通道多节IIR滤波器组。 |
| typedef struct [FAST\_BiquadmD](fast-kit--fast-biquadmd.md) [FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) | 双精度多通道多节IIR滤波器组。 |
| typedef struct [FAST\_FFTConfig](fast-kit-fast-dsp-transform-8h.md) [FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig) | 快速傅里叶变换的不透明配置。 |
| typedef void\* [FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) | 哈希表的句柄。 |
| typedef void\* [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) | 哈希表键指针。 |
| typedef void\* [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) | 哈希表的值指针。 |
| typedef uint64\_t(\* [HMS\_FAST\_Hashmap\_HashFunc](fast-kit-fast.md#hms_fast_hashmap_hashfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key) | 自定义的哈希值计算函数。 |
| typedef int32\_t(\* [HMS\_FAST\_Hashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_hashmap_keyequalfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) leftKey, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) rightKey) | 自定义的键比较函数。 |
| typedef int32\_t(\* [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc)) (const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value, void\* context) | 自定义的通用回调函数形式。 |
| typedef void\* [FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) | 并发哈希表的句柄。 |
| typedef void\* [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) | 并发哈希表键指针。 |
| typedef void\* [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr) | 并发哈希表的值指针。 |
| typedef uint64\_t ([\*HMS\_FAST\_ConcurrentHashmap\_HashFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key) | 开发者自定义的哈希值计算函数。 |
| typedef int32\_t ([\*HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) leftKey, const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) rightKey) | 开发者自定义的键比较函数。 |
| typedef int32\_t ([\*HMS\_FAST\_ConcurrentHashmap\_HookFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr) value, void\* context) | 开发者自定义的通用回调函数形式。 |
| typedef struct [HMS\_FAST\_SortData](fast-kit--hms-fast-sortdata.md) [HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) | 定义待排序的连续数据块的数据结构。 |
| typedef void\* [HMS\_FAST\_SortElementPtr](fast-kit-fast.md#hms_fast_sortelementptr) | 表示通用容器中单个元素的opaque pointer类型。 |
| typedef const void\* [HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) | 表示通用容器中单个元素的const opaque pointer类型。 |
| typedef int32\_t(\* [HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc)) ([HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) first, [HMS\_FAST\_SortElementConstPtr](fast-kit-fast.md#hms_fast_sortelementconstptr) second) | 用户自定义比较函数的回调函数指针类型。 |
| typedef struct HMS\_FAST\_PerfHintConfigBuilder [HMS\_FAST\_PerfHintConfigBuilder](fast-kit-fast.md#hms_fast_perfhintconfigbuilder) | 系统性能优化配置参数构建器。 |
| typedef struct HMS\_FAST\_PerfHintConfig [HMS\_FAST\_PerfHintConfig](fast-kit-fast.md#hms_fast_perfhintconfig) | 系统性能优化配置参数。 |

### 常量

| 名称 | 描述 |
| --- | --- |
| const uint32\_t [FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n) = 16 | FFT支持的最大点数对应的以2为底的对数值。值为16，即最大点数为65536。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [FAST\_SegmentMapQueryType](fast-kit-fast.md#fast_segmentmapquerytype-1) { FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM = 0, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN = 1, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX = 2 } | 线段表支持的查询操作类型。 |
| [FAST\_SegmentMapUpdateType](fast-kit-fast.md#fast_segmentmapupdatetype-1) { FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET = 0, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD = 1, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB = 2 } | 线段表支持的更新操作类型。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) {  FAST\_ERROR\_CODE\_SUCCESS = 1023100000, FAST\_ERROR\_CODE\_FAIL = 1023100001, FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002, FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003,  FAST\_ERROR\_CODE\_KEY\_EXISTS = 1023110000, FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS = 1023110001,  FAST\_ERROR\_CODE\_OOM = 1023199001  } | FAST Kit的错误码。 |
| [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1) {  HMS\_FAST\_HANN\_DENORMALIZE\_FULL = 0x00,  HMS\_FAST\_HANN\_NORMALIZE\_FULL = 0x01,  HMS\_FAST\_HANN\_DENORMALIZE\_HALF = 0x10,  HMS\_FAST\_HANN\_NORMALIZE\_HALF = 0x11  } | 汉宁窗类型枚举。 |
| [HMS\_FAST\_SchedulingOptimization\_SceneType](fast-kit-fast.md#hms_fast_schedulingoptimization_scenetype) {  HMS\_FAST\_APP\_LAUNCH = 1,  HMS\_FAST\_PAGE\_TRANSITION = 2,  HMS\_FAST\_PAGE\_LOAD = 3,  HMS\_FAST\_NETWORK\_FILE\_PROCESSING = 4,  HMS\_FAST\_LOCAL\_FILE\_PROCESSING = 5,  HMS\_FAST\_PAGE\_DRAWING = 6,  HMS\_FAST\_ANIMATION = 7,  HMS\_FAST\_MEDIA\_PLAYBACK = 8,  HMS\_FAST\_MEDIA\_ENCODING\_AND\_DECODING = 9  } | 需要系统性能优化的场景类型。 |
| [HMS\_FAST\_SchedulingOptimization\_SceneState](fast-kit-fast.md#hms_fast_schedulingoptimization_scenestate) {  HMS\_FAST\_END = 0,  HMS\_FAST\_BEGIN = 1  } | 需要系统性能优化的场景状态。 |
| [HMS\_FAST\_SchedulingOptimization\_DurationType](fast-kit-fast.md#hms_fast_schedulingoptimization_durationtype) {  HMS\_FAST\_SHORT = 1,  HMS\_FAST\_MEDIUM = 2,  HMS\_FAST\_LONG = 3  } | 需要系统性能优化的持续时间选项。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) {  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS = 0,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_HIGH\_SYSTEM\_LOAD = 1027700001,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_POWER\_SAVING\_MODE = 1027700002,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_LOW\_POWER\_MODE = 1027700003,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NON\_FRONTEND = 1027700004,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INTERVAL = 1027700005,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_EXECUTE\_ERROR = 1027700006,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM = 1027700007,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NO\_MEMORY = 1027700008  } | 系统性能优化的错误码。 |

### 函数

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
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeRoots](fast-kit-fast.md#hms_fast_polyroot_computeroots) (const [FAST\_Poly](fast-kit-fast.md#fast_poly) \*poly, const size\_t maxRootCount, double \*root, size\_t \*rootCount) | 计算多项式的给定数量的实数根。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeSingle](fast-kit-fast.md#hms_fast_polyroot_computesingle) (const [FAST\_Poly](fast-kit-fast.md#fast_poly) \*poly, double \*root) | 计算多项式的绝对值最大的实根。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_PolyRoot\_ComputeRootIntervals](fast-kit-fast.md#hms_fast_polyroot_computerootintervals) (const [FAST\_Poly](fast-kit-fast.md#fast_poly) \*poly, const size\_t maxRootCount, double \*leftBoundary, double \*rightBoundary, size\_t \*rootCount) | 计算多项式给定数量的实根的隔离区间，输出每个实根的左右边界。 |
| float [HMS\_FAST\_DSP\_Maxmgv](fast-kit-fast.md#hms_fast_dsp_maxmgv) (const float \*input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（单精度）。 |
| double [HMS\_FAST\_DSP\_MaxmgvD](fast-kit-fast.md#hms_fast_dsp_maxmgvd) (const double \*input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Maxvi](fast-kit-fast.md#hms_fast_dsp_maxvi) (const float \*input, size\_t stride, size\_t length, float \*value, size\_t \*index) | 查找步长实数向量中的最大值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MaxviD](fast-kit-fast.md#hms_fast_dsp_maxvid) (const double \*input, size\_t stride, size\_t length, double \*value, size\_t \*index) | 查找步长实数向量中的最大值及其索引（双精度）。 |
| float [HMS\_FAST\_DSP\_Sve](fast-kit-fast.md#hms_fast_dsp_sve) (const float \*input, size\_t stride, size\_t length) | 计算步长实数向量的和（单精度）。 |
| double [HMS\_FAST\_DSP\_SveD](fast-kit-fast.md#hms_fast_dsp_sved) (const double \*input, size\_t stride, size\_t length) | 计算步长实数向量的和（双精度）。 |
| float [HMS\_FAST\_DSP\_Svemg](fast-kit-fast.md#hms_fast_dsp_svemg) (const float \*input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS\_FAST\_DSP\_SvemgD](fast-kit-fast.md#hms_fast_dsp_svemgd) (const double \*input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS\_FAST\_DSP\_Meamgv](fast-kit-fast.md#hms_fast_dsp_meamgv) (const float \*input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（单精度）。 |
| double [HMS\_FAST\_DSP\_MeamgvD](fast-kit-fast.md#hms_fast_dsp_meamgvd) (const double \*input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（双精度）。 |
| float [HMS\_FAST\_DSP\_Dotpr](fast-kit-fast.md#hms_fast_dsp_dotpr) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（单精度）。 |
| double [HMS\_FAST\_DSP\_DotprD](fast-kit-fast.md#hms_fast_dsp_dotprd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsbsm](fast-kit-fast.md#hms_fast_dsp_vsbsm) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float scalar, float \*outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（单精度）。 |
| void [HMS\_FAST\_DSP\_VsbsmD](fast-kit-fast.md#hms_fast_dsp_vsbsmd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double scalar, double \*outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（双精度）。 |
| void [HMS\_FAST\_DSP\_Ctoz](fast-kit-fast.md#hms_fast_dsp_ctoz) (const float \*input, size\_t strideInput, [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) \*output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS\_FAST\_DSP\_CtozD](fast-kit-fast.md#hms_fast_dsp_ctozd) (const double \*input, size\_t strideInput, [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) \*output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Ztoc](fast-kit-fast.md#hms_fast_dsp_ztoc) (const [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS\_FAST\_DSP\_ZtocD](fast-kit-fast.md#hms_fast_dsp_ztocd) (const [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvabs](fast-kit-fast.md#hms_fast_dsp_zvabs) (const [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvabsD](fast-kit-fast.md#hms_fast_dsp_zvabsd) (const [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvmags](fast-kit-fast.md#hms_fast_dsp_zvmags) (const [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvmagsD](fast-kit-fast.md#hms_fast_dsp_zvmagsd) (const [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvphas](fast-kit-fast.md#hms_fast_dsp_zvphas) (const [FAST\_SplitComplex](fast-kit-fast.md#fast_splitcomplex) \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvphasD](fast-kit-fast.md#hms_fast_dsp_zvphasd) (const [FAST\_SplitComplexD](fast-kit-fast.md#fast_splitcomplexd) \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsmul](fast-kit-fast.md#hms_fast_dsp_vsmul) (const float \*input, size\_t strideInput, const float scalar, float \*output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsmulD](fast-kit-fast.md#hms_fast_dsp_vsmuld) (const double \*input, size\_t strideInput, const double scalar, double \*output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsdiv](fast-kit-fast.md#hms_fast_dsp_vsdiv) (const float \*input, size\_t strideInput, const float scalar, float \*output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsdivD](fast-kit-fast.md#hms_fast_dsp_vsdivd) (const double \*input, size\_t strideInput, const double scalar, double \*output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Svdiv](fast-kit-fast.md#hms_fast_dsp_svdiv) (const float scalar, const float \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_SvdivD](fast-kit-fast.md#hms_fast_dsp_svdivd) (const double scalar, const double \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsadd](fast-kit-fast.md#hms_fast_dsp_vsadd) (const float \*input, size\_t strideInput, const float scalar, float \*output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_VsaddD](fast-kit-fast.md#hms_fast_dsp_vsaddd) (const double \*input, size\_t strideInput, const double scalar, double \*output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（双精度）。 |
| void [HMS\_FAST\_DSP\_Vadd](fast-kit-fast.md#hms_fast_dsp_vadd) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（单精度）。 |
| void [HMS\_FAST\_DSP\_VaddD](fast-kit-fast.md#hms_fast_dsp_vaddd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsub](fast-kit-fast.md#hms_fast_dsp_vsub) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（单精度）。 |
| void [HMS\_FAST\_DSP\_VsubD](fast-kit-fast.md#hms_fast_dsp_vsubd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vmul](fast-kit-fast.md#hms_fast_dsp_vmul) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（单精度）。 |
| void [HMS\_FAST\_DSP\_VmulD](fast-kit-fast.md#hms_fast_dsp_vmuld) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdiv](fast-kit-fast.md#hms_fast_dsp_vdiv) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（单精度）。 |
| void [HMS\_FAST\_DSP\_VdivD](fast-kit-fast.md#hms_fast_dsp_vdivd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double \*outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdist](fast-kit-fast.md#hms_fast_dsp_vdist) (const float \*inputA, size\_t strideA, const float \*inputB, size\_t strideB, float \*outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数（单精度）。 |
| void [HMS\_FAST\_DSP\_VdistD](fast-kit-fast.md#hms_fast_dsp_vdistd) (const double \*inputA, size\_t strideA, const double \*inputB, size\_t strideB, double \*outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数（双精度）。 |
| float [HMS\_FAST\_DSP\_Svesq](fast-kit-fast.md#hms_fast_dsp_svesq) (const float \*input, size\_t stride, size\_t length) | 计算向量元素的平方和（单精度）。 |
| double [HMS\_FAST\_DSP\_SvesqD](fast-kit-fast.md#hms_fast_dsp_svesqd) (const double \*input, size\_t stride, size\_t length) | 计算向量元素的平方和（双精度）。 |
| void [HMS\_FAST\_DSP\_Minvi](fast-kit-fast.md#hms_fast_dsp_minvi) (const float \*input, size\_t stride, size\_t length, float \*value, size\_t \*index) | 查找步长实数向量中的最小值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MinviD](fast-kit-fast.md#hms_fast_dsp_minvid) (const double \*input, size\_t stride, size\_t length, double \*value, size\_t \*index) | 查找步长实数向量中的最小值及其索引（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsq](fast-kit-fast.md#hms_fast_dsp_vsq) (const float \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（单精度）。 |
| void [HMS\_FAST\_DSP\_VsqD](fast-kit-fast.md#hms_fast_dsp_vsqd) (const double \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Vabs](fast-kit-fast.md#hms_fast_dsp_vabs) (const float \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（单精度）。 |
| void [HMS\_FAST\_DSP\_VabsD](fast-kit-fast.md#hms_fast_dsp_vabsd) (const double \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（双精度）。 |
| void [HMS\_FAST\_DSP\_Vthr](fast-kit-fast.md#hms_fast_dsp_vthr) (const float \*input, size\_t strideInput, const float threshold, float \*output, size\_t strideOutput, size\_t length) | 对向量应用阈值（单精度）。 |
| void [HMS\_FAST\_DSP\_VthrD](fast-kit-fast.md#hms_fast_dsp_vthrd) (const double \*input, size\_t strideInput, const double threshold, double \*output, size\_t strideOutput, size\_t length) | 对向量应用阈值（双精度）。 |
| void [HMS\_FAST\_DSP\_Vrvrs](fast-kit-fast.md#hms_fast_dsp_vrvrs) (float \*vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（单精度）。 |
| void [HMS\_FAST\_DSP\_VrvrsD](fast-kit-fast.md#hms_fast_dsp_vrvrsd) (double \*vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（双精度）。 |
| void [HMS\_FAST\_DSP\_Vspdp](fast-kit-fast.md#hms_fast_dsp_vspdp) (const float \*input, size\_t strideInput, double \*output, size\_t strideOutput, size\_t length) | 将单精度向量转换为双精度向量。 |
| void [HMS\_FAST\_DSP\_Vdpsp](fast-kit-fast.md#hms_fast_dsp_vdpsp) (const double \*input, size\_t strideInput, float \*output, size\_t strideOutput, size\_t length) | 将双精度向量转换为单精度向量。 |
| void [HMS\_FAST\_DSP\_Vfill](fast-kit-fast.md#hms_fast_dsp_vfill) (float \*vector, size\_t stride, size\_t length, const float scalar) | 使用指定标量值填充向量（单精度）。 |
| void [HMS\_FAST\_DSP\_VfillD](fast-kit-fast.md#hms_fast_dsp_vfilld) (double \*vector, size\_t stride, size\_t length, const double scalar) | 使用指定标量值填充向量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vclr](fast-kit-fast.md#hms_fast_dsp_vclr) (float \*vector, size\_t stride, size\_t length) | 将向量所有元素清零（单精度）。 |
| void [HMS\_FAST\_DSP\_VclrD](fast-kit-fast.md#hms_fast_dsp_vclrd) (double \*vector, size\_t stride, size\_t length) | 将向量所有元素清零（双精度）。 |
| void [HMS\_FAST\_DSP\_Conv](fast-kit-fast.md#hms_fast_dsp_conv) (const float \*input, size\_t strideInput, const float \*filter, size\_t strideFilter, float \*output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（单精度）。 |
| void [HMS\_FAST\_DSP\_ConvD](fast-kit-fast.md#hms_fast_dsp_convd) (const double \*input, size\_t strideInput, const double \*filter, size\_t strideFilter, double \*output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（双精度）。 |
| void [HMS\_FAST\_DSP\_HannWindow](fast-kit-fast.md#hms_fast_dsp_hannwindow) (float \*output, size\_t length, [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1) type) | 生成汉宁窗序列（单精度）。 |
| void [HMS\_FAST\_DSP\_HannWindowD](fast-kit-fast.md#hms_fast_dsp_hannwindowd) (double \*output, size\_t length, [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1) type) | 生成汉宁窗序列（双精度）。 |
| void [HMS\_FAST\_DSP\_Mmul](fast-kit-fast.md#hms_fast_dsp_mmul) (const float \*matrixA, size\_t strideA, const float \*matrixB, size\_t strideB, float \*matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法：C = A \* B（单精度）。 |
| void [HMS\_FAST\_DSP\_MmulD](fast-kit-fast.md#hms_fast_dsp_mmuld) (const double \*matrixA, size\_t strideA, const double \*matrixB, size\_t strideB, double \*matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法：C = A \* B（双精度）。 |
| void [HMS\_FAST\_DSP\_Vvpow](fast-kit-fast.md#hms_fast_dsp_vvpow) (const float \*inputA, const float \*inputB, float \*outputC, size\_t length) | 执行向量逐元素幂运算（单精度）。 |
| void [HMS\_FAST\_DSP\_VvpowD](fast-kit-fast.md#hms_fast_dsp_vvpowd) (const double \*inputA, const double \*inputB, double \*outputC, size\_t length) | 执行向量逐元素幂运算（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsort](fast-kit-fast.md#hms_fast_dsp_vsort) (float \*vector, size\_t length, int order) | 对向量进行原地排序（单精度）。 |
| void [HMS\_FAST\_DSP\_VsortD](fast-kit-fast.md#hms_fast_dsp_vsortd) (double \*vector, size\_t length, int order) | 对向量进行原地排序（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFilters](fast-kit-fast.md#hms_fast_biquadm_setactivefilters) ([FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*filter, const uint8\_t \*activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFiltersD](fast-kit-fast.md#hms_fast_biquadm_setactivefiltersd) ([FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*filter, const uint8\_t \*activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingle](fast-kit-fast.md#hms_fast_biquadm_setcoeffsingle) ([FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*filter, const float \*coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDouble](fast-kit-fast.md#hms_fast_biquadm_setcoeffdouble) ([FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*filter, const double \*coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingleD](fast-kit-fast.md#hms_fast_biquadm_setcoeffsingled) ([FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*filter, const float \*coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDoubleD](fast-kit-fast.md#hms_fast_biquadm_setcoeffdoubled) ([FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*filter, const double \*coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_Create](fast-kit-fast.md#hms_fast_biquadm_create) (size\_t numChannels, size\_t numSections, size\_t maxFrames, [FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*\*filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_CreateD](fast-kit-fast.md#hms_fast_biquadm_created) (size\_t numChannels, size\_t numSections, size\_t maxFrames, [FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*\*filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS\_FAST\_Biquadm\_Destroy](fast-kit-fast.md#hms_fast_biquadm_destroy) ([FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS\_FAST\_Biquadm\_DestroyD](fast-kit-fast.md#hms_fast_biquadm_destroyd) ([FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm](fast-kit-fast.md#hms_fast_biquadm) ([FAST\_Biquadm](fast-kit-fast.md#fast_biquadm) \*filter, const float \*\*input, const size\_t strideInput, float \*\*output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_BiquadmD](fast-kit-fast.md#hms_fast_biquadmd) ([FAST\_BiquadmD](fast-kit-fast.md#fast_biquadmd) \*filter, const double \*\*input, const size\_t strideInput, double \*\*output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfig](fast-kit-fast.md#hms_fast_fft_createconfig) (FAST\_FFTConfig\*\* config, const uint32\_t log2n) | 创建单精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfigD](fast-kit-fast.md#hms_fast_fft_createconfigd) (FAST\_FFTConfig\*\* config, const uint32\_t log2n) | 创建双精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| void [HMS\_FAST\_FFT\_DestroyConfig](fast-kit-fast.md#hms_fast_fft_destroyconfig) (FAST\_FFTConfig\* config) | 销毁FFT配置对象并释放资源。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransform](fast-kit-fast.md#hms_fast_fft_forwardtransform) (FAST\_FFTConfig\* config, const uint32\_t length, const float input[], float outputRe[], float outputIm[]) | 计算单精度实数时域信号的DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransformD](fast-kit-fast.md#hms_fast_fft_forwardtransformd) (FAST\_FFTConfig\* config, const uint32\_t length, const double input[], double outputRe[], double outputIm[]) | 计算双精度实数时域信号的DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransform](fast-kit-fast.md#hms_fast_fft_inversetransform) (FAST\_FFTConfig\* config, const uint32\_t length, const float inputRe[], const float inputIm[], float output[]) | 计算单精度复数频域序列的逆DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransformD](fast-kit-fast.md#hms_fast_fft_inversetransformd) (FAST\_FFTConfig\* config, const uint32\_t length, const double inputRe[], const double inputIm[], double output[]) | 计算双精度复数频域序列的逆DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Create](fast-kit-fast.md#hms_fast_concurrenthashmap_create) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HashFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc) hasher, [HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc) equaler, float maxLoadFac, size\_t numShards) | 使用给定配置创建并发哈希表。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Destroy](fast-kit-fast.md#hms_fast_concurrenthashmap_destroy) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 销毁指定并发哈希表。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Insert](fast-kit-fast.md#hms_fast_concurrenthashmap_insert) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr) value, [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Find](fast-kit-fast.md#hms_fast_concurrenthashmap_find) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Erase](fast-kit-fast.md#hms_fast_concurrenthashmap_erase) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr)\* originKey, [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键和值分别保存在originKey和originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_TryInsert](fast-kit-fast.md#hms_fast_concurrenthashmap_tryinsert) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](fast-kit-fast.md#fast_concurrenthashmapvalueptr) value) | 将给定的键值对插入并发哈希表中，如果键已经存在，则不执行任何操作。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_Size](fast-kit-fast.md#hms_fast_concurrenthashmap_size) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 返回给定哈希表当前的元素个数。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Clear](fast-kit-fast.md#hms_fast_concurrenthashmap_clear) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 清空给定哈希表中维护的所有元素。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_EraseIf](fast-kit-fast.md#hms_fast_concurrenthashmap_eraseif) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Traverse](fast-kit-fast.md#hms_fast_concurrenthashmap_traverse) ([FAST\_ConcurrentHashmapHandle](fast-kit-fast.md#fast_concurrenthashmaphandle) handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Create](fast-kit-fast.md#hms_fast_hashmap_create) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle)\* handle, [HMS\_FAST\_Hashmap\_HashFunc](fast-kit-fast.md#hms_fast_hashmap_hashfunc) hasher, [HMS\_FAST\_Hashmap\_KeyEqualFunc](fast-kit-fast.md#hms_fast_hashmap_keyequalfunc) equaler) | 创建哈希表实例。 |
| void [HMS\_FAST\_Hashmap\_Destroy](fast-kit-fast.md#hms_fast_hashmap_destroy) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 销毁哈希表实例。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Insert](fast-kit-fast.md#hms_fast_hashmap_insert) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 将给定的键值对插入哈希表中，如果键已经存在，则使用value覆写原有的值，并将原有值的地址保存在originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Find](fast-kit-fast.md#hms_fast_hashmap_find) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* value) | 检索与给定键关联的值，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_Erase](fast-kit-fast.md#hms_fast_hashmap_erase) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr)\* originKey, [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Hashmap\_TryInsert](fast-kit-fast.md#hms_fast_hashmap_tryinsert) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, const [FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr) key, const [FAST\_HashmapValuePtr](fast-kit-fast.md#fast_hashmapvalueptr) value) | 将给定的键值对插入哈希表中，如果键已经存在、则不做操作。 |
| size\_t [HMS\_FAST\_Hashmap\_Size](fast-kit-fast.md#hms_fast_hashmap_size) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 返回哈希表中的元素个数。 |
| void [HMS\_FAST\_Hashmap\_Clear](fast-kit-fast.md#hms_fast_hashmap_clear) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle) | 从哈希表中删除所有元素。 |
| size\_t [HMS\_FAST\_Hashmap\_EraseIf](fast-kit-fast.md#hms_fast_hashmap_eraseif) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合输入条件的所有元素，并使用自定义的方式释放其内存。 |
| void [HMS\_FAST\_Hashmap\_Traverse](fast-kit-fast.md#hms_fast_hashmap_traverse) ([FAST\_HashmapHandle](fast-kit-fast.md#fast_hashmaphandle) handle, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_Hashmap\_HookFunc](fast-kit-fast.md#hms_fast_hashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合输入条件的键值对按自定义的方式修改。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_Sort](fast-kit-fast.md#hms_fast_algo_sort) ([HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) \*data, [HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 使用用户提供的比较函数对任意类型数组进行完整排序。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_PartialSortAt](fast-kit-fast.md#hms_fast_algo_partialsortat) ([HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) \*data, size\_t offset, size\_t count, [HMS\_FAST\_Sort\_CompFunc](fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 对数组进行原地部分排序，使指定区间对应排序后的相应段。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalSort](fast-kit-fast.md#hms_fast_algo_naturalsort) ([HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) \*data, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行排序。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalPartialSortAt](fast-kit-fast.md#hms_fast_algo_naturalpartialsortat) ([HMS\_FAST\_SortData](fast-kit-fast.md#hms_fast_sortdata) \*data, size\_t offset, size\_t count, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行部分排序，使指定区间对应排序后的相应段。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_Create](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_create) (HMS\_FAST\_PerfHintConfigBuilder\*\* builder) | 创建构建器实例。 |
| void [HMS\_FAST\_PerfHintConfigBuilder\_Destroy](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_destroy) (HMS\_FAST\_PerfHintConfigBuilder\* builder) | 销毁构建器。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneType](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenetype) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_SceneType sceneType) | 设置需要系统性能优化的场景类型。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneState](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenestate) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_SceneState sceneState) | 设置需要系统性能优化的场景状态。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetDurationType](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setdurationtype) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_DurationType durationType) | 设置需要系统性能优化的持续时间选项。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetTids](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_settids) (HMS\_FAST\_PerfHintConfigBuilder\* builder, int\* tids, uint32\_t tidsSize) | 设置需要优化的线程ID。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_Build](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_build) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_PerfHintConfig\*\* config) | 创建系统性能优化配置参数。 |
| void [HMS\_FAST\_PerfHintConfig\_Destroy](fast-kit-fast.md#hms_fast_perfhintconfig_destroy) (HMS\_FAST\_PerfHintConfig\* config) | 销毁系统性能优化配置参数。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_SchedulingOptimization\_PerfHint](fast-kit-fast.md#hms_fast_schedulingoptimization_perfhint) (const HMS\_FAST\_PerfHintConfig\* config) | 系统性能优化接口。 |

## 类型定义说明

### FAST\_ErrorCode

```c
typedef enum FAST_ErrorCode FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

### FAST\_Rect

```c
typedef struct FAST_Rect FAST_Rect
```

**描述**

定义矩形的数据结构。

**起始版本：** 6.0.2(22)

### FAST\_RectPartitionConfig

```c
typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig
```

**描述**

矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。

**起始版本：** 6.0.2(22)

### FAST\_Poly

```c
typedef struct FAST_Poly FAST_Poly
```

**描述**

定义稀疏格式多项式的数据结构。多项式![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nqgSZXSjSJ-NfciIs8o08w/zh-cn_image_0000002706836738.png)由系数数组coeff和指数数组pow共同描述，且需按指数升序排列。

**起始版本：** 26.0.0

### FAST\_SegmentMapConfig

```c
typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig
```

**描述**

线段表的不透明配置（Opaque Configuration）。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapHandle

```c
typedef void* FAST_SegmentMapHandle
```

**描述**

线段表的句柄。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapQueryType

```c
typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType
```

**描述**

线段表数据结构支持的区间查询操作类型。

**起始版本：** 6.0.2(22)

### FAST\_SegmentMapUpdateType

```c
typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType
```

**描述**

线段表数据结构支持的区间更新操作类型。

**起始版本：** 6.0.2(22)

### FAST\_ConcurrentHashmapHandle

```c
typedef void* FAST_ConcurrentHashmapHandle
```

**描述**

并发哈希表的句柄。

**起始版本：** 6.1.1(24)

### FAST\_ConcurrentHashmapKeyPtr

```c
typedef void* FAST_ConcurrentHashmapKeyPtr
```

**描述**

并发哈希表的键指针。

**起始版本：** 6.1.1(24)

### FAST\_ConcurrentHashmapValuePtr

```c
typedef void* FAST_ConcurrentHashmapValuePtr
```

**描述**

并发哈希表的值指针。

**起始版本：** 6.1.1(24)

### HMS\_FAST\_ConcurrentHashmap\_HashFunc

```c
typedef uint64_t (*HMS_FAST_ConcurrentHashmap_HashFunc)(const FAST_ConcurrentHashmapKeyPtr key)
```

**描述**

并发哈希表的哈希值计算回调函数类型。

**起始版本：** 6.1.1(24)

### HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc

```c
typedef int32_t (*HMS_FAST_ConcurrentHashmap_KeyEqualFunc)(
    const FAST_ConcurrentHashmapKeyPtr leftKey,
    const FAST_ConcurrentHashmapKeyPtr rightKey
)
```

**描述**

并发哈希表的键比较回调函数类型。

**起始版本：** 6.1.1(24)

### HMS\_FAST\_ConcurrentHashmap\_HookFunc

```c
typedef int32_t (*HMS_FAST_ConcurrentHashmap_HookFunc)(
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapValuePtr value,
    void* context
)
```

**描述**

并发哈希表的通用回调函数形式。

**起始版本：** 6.1.1(24)

### FAST\_SplitComplex

```c
typedef struct FAST_SplitComplex FAST_SplitComplex
```

**描述**

定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

**起始版本：** 6.1.1(24)

### FAST\_SplitComplexD

```c
typedef struct FAST_SplitComplexD FAST_SplitComplexD
```

**描述**

定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。

**起始版本：** 6.1.1(24)

### FAST\_BiquadCoefficients

```c
typedef struct FAST_BiquadCoefficients FAST_BiquadCoefficients
```

**描述**

定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。

**起始版本：** 6.1.1(24)

### FAST\_BiquadCoefficientsD

```c
typedef struct FAST_BiquadCoefficientsD FAST_BiquadCoefficientsD
```

**描述**

定义双精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)。分母中的1实际上为系数a0归一化后的结果。

**起始版本：** 6.1.1(24)

### FAST\_BiquadState

```c
typedef struct FAST_BiquadState FAST_BiquadState
```

**描述**

定义单精度二阶IIR滤波器节的状态变量。

**起始版本：** 6.1.1(24)

### FAST\_BiquadStateD

```c
typedef struct FAST_BiquadStateD FAST_BiquadStateD
```

**描述**

定义双精度二阶IIR滤波器节的状态变量。

**起始版本：** 6.1.1(24)

### FAST\_Biquadm

```c
typedef struct FAST_Biquadm FAST_Biquadm
```

**描述**

定义单精度多通道、多节二阶IIR滤波器组的数据结构。

**起始版本：** 6.1.1(24)

### FAST\_BiquadmD

```c
typedef struct FAST_BiquadmD FAST_BiquadmD
```

**描述**

定义双精度多通道、多节二阶IIR滤波器组的数据结构。

**起始版本：** 6.1.1(24)

### FAST\_FFTConfig

```c
typedef struct FAST_FFTConfig FAST_FFTConfig
```

**描述**

快速傅里叶变换的不透明配置（Opaque Configuration）。该对象是非线程安全的，在多线程环境中，严禁多个线程同时操作同一个FAST\_FFTConfig配置对象。

**起始版本：** 26.0.0

### FAST\_HashmapHandle

```c
typedef void* FAST_HashmapHandle
```

哈希表的句柄。

**起始版本：** 26.0.0

### FAST\_HashmapKeyPtr

```c
typedef void* FAST_HashmapKeyPtr
```

**描述**

哈希表的键指针。

**起始版本：** 26.0.0

### FAST\_HashmapValuePtr

```c
typedef void* FAST_HashmapValuePtr
```

**描述**

哈希表的值指针。

**起始版本：** 26.0.0

### HMS\_FAST\_Hashmap\_HashFunc

```c
typedef uint64_t(* HMS_FAST_Hashmap_HashFunc) (const FAST_HashmapKeyPtr key)
```

**描述**

哈希表的哈希计算回调函数类型。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 要计算哈希的[FAST\_HashmapKeyPtr](fast-kit-fast.md#fast_hashmapkeyptr)。 |

**返回：**

从键派生的64位哈希值。

### HMS\_FAST\_Hashmap\_HookFunc

```c
typedef int32_t(* HMS_FAST_Hashmap_HookFunc) (const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr value, void* context)
```

**描述**

哈希表的通用回调函数形式。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 正在访问的当前元素的键。 |
| value | 与键关联的值。 |
| context | 通过遍历API传递的用户定义上下文。 |

**返回：**

非零表示条件满足（例如，用于过滤）；否则为零。

**注解：**

此函数通常用于支持条件处理的API，如选择性删除或转换。返回值的精确解释取决于调用函数：

* 在谓词上下文中（例如erase-if），非零返回值通常表示“匹配”。
* 在操作上下文中，返回值可能被忽略。

### HMS\_FAST\_Hashmap\_KeyEqualFunc

```c
typedef int32_t(* HMS_FAST_Hashmap_KeyEqualFunc) (const FAST_HashmapKeyPtr leftKey, const FAST_HashmapKeyPtr rightKey)
```

**描述**

自定义键相等比较函数回调。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| leftKey | 指向哈希表中键的指针，作为相等比较的左操作数传递。 |
| rightKey | 指向哈希表中另一个键的指针，作为相等比较的右操作数传递。 |

**返回：**

如果键被视为相等则非零；否则为零。

### HMS\_FAST\_SortElementPtr

```c
typedef void* HMS_FAST_SortElementPtr
```

**描述**

表示通用容器中单个元素的opaque pointer类型。

**起始版本：** 26.0.0

### HMS\_FAST\_SortElementConstPtr

```c
typedef const void* HMS_FAST_SortElementConstPtr
```

**描述**

表示通用容器中单个元素的const opaque pointer类型。

**起始版本：** 26.0.0

### HMS\_FAST\_Sort\_CompFunc

```c
typedef int32_t(* HMS_FAST_Sort_CompFunc) (HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second)
```

**描述**

用户自定义比较函数的回调函数类型。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| first | 指向第一个元素的指针。 |
| second | 指向第二个元素的指针。 |

**返回值：**

比较结果。必须返回：

* 负数表示first小于second
* 零表示first等于second
* 正数表示first大于second

### HMS\_FAST\_SortData

```c
typedef struct HMS_FAST_SortData HMS_FAST_SortData
```

**描述**

描述待排序的连续内存数据块。

**起始版本：** 26.0.0

### HMS\_FAST\_HannWindowType

```c
typedef enum HMS_FAST_HannWindowType HMS_FAST_HannWindowType
```

**描述**

汉宁窗类型枚举。

**起始版本：** 26.0.0

### HMS\_FAST\_PerfHintConfigBuilder

```c
typedef struct HMS_FAST_PerfHintConfigBuilder HMS_FAST_PerfHintConfigBuilder
```

**描述**

系统性能优化配置参数构建器。

**起始版本：** 26.0.0

### HMS\_FAST\_PerfHintConfig

```c
typedef struct HMS_FAST_PerfHintConfig HMS_FAST_PerfHintConfig
```

**描述**

系统性能优化配置参数。

**起始版本：** 26.0.0

## 常量说明

### FAST\_MAX\_FFT\_LOG2N

```c
const uint32_t FAST_MAX_FFT_LOG2N = 16;
```

**描述**

FFT支持的最大点数N对应的以2为底的对数值。即FAST\_MAX\_FFT\_LOG2N=![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/0Gco03znQgWg81IKkMkmnA/zh-cn_image_0000002736315847.png)，其中N为FFT支持的最大点数，例如该值为16时，最大点数为65536。

**起始版本**：26.0.0

## 枚举类型说明

### FAST\_ErrorCode

```c
enum FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| FAST\_ERROR\_CODE\_SUCCESS = 1023100000 | 成功。 |
| FAST\_ERROR\_CODE\_FAIL = 1023100001 | 失败。 |
| FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002 | 非法输入。 |
| FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003 | 无效指针（例如 NULL）。 |
| FAST\_ERROR\_CODE\_KEY\_EXISTS = 1023110000 | 键已存在。  **起始版本**：6.1.1(24) |
| FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS = 1023110001 | 键不存在。  **起始版本**：6.1.1(24) |
| FAST\_ERROR\_CODE\_OOM = 1023199001 | 内存溢出。 |

### FAST\_SegmentMapQueryType

```c
enum FAST_SegmentMapQueryType
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

```c
enum FAST_SegmentMapUpdateType
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

### HMS\_FAST\_HannWindowType

```c
enum HMS_FAST_HannWindowType
```

**描述**

汉宁窗类型枚举。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| HMS\_FAST\_HANN\_DENORMALIZE\_FULL = 0x00 | 非归一化全窗。 |
| HMS\_FAST\_HANN\_NORMALIZE\_FULL = 0x01 | 归一化全窗。 |
| HMS\_FAST\_HANN\_DENORMALIZE\_HALF = 0x10 | 非归一化半窗，给定长度为N时，仅包含前(N+1)/2个点。 |
| HMS\_FAST\_HANN\_NORMALIZE\_HALF = 0x11 | 归一化半窗，给定长度为N时，仅包含前(N+1)/2个点。 |

### HMS\_FAST\_SchedulingOptimization\_SceneType

```c
enum HMS_FAST_SchedulingOptimization_SceneType
```

**描述**

需要系统性能优化的场景类型。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| HMS\_FAST\_APP\_LAUNCH = 1 | 应用启动场景。 |
| HMS\_FAST\_PAGE\_TRANSITION = 2 | 页面切换场景。 |
| HMS\_FAST\_PAGE\_LOAD = 3 | 页面加载场景。 |
| HMS\_FAST\_NETWORK\_FILE\_PROCESSING = 4 | 网络文件处理场景。 |
| HMS\_FAST\_LOCAL\_FILE\_PROCESSING = 5 | 本地文件处理场景。 |
| HMS\_FAST\_PAGE\_DRAWING = 6 | 页面绘制场景。 |
| HMS\_FAST\_ANIMATION = 7 | 动效场景。 |
| HMS\_FAST\_MEDIA\_PLAYBACK = 8 | 媒体播放场景。 |
| HMS\_FAST\_MEDIA\_ENCODING\_AND\_DECODING = 9 | 媒体编解码场景。 |

### HMS\_FAST\_SchedulingOptimization\_SceneState

```c
enum HMS_FAST_SchedulingOptimization_SceneState
```

**描述**

需要系统性能优化的场景状态。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| HMS\_FAST\_END | 结束系统性能优化。 |
| HMS\_FAST\_BEGIN | 开始系统性能优化。 |

### HMS\_FAST\_SchedulingOptimization\_DurationType

```c
enum HMS_FAST_SchedulingOptimization_DurationType
```

**描述**

需要系统性能优化的持续时间选项。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| HMS\_FAST\_SHORT | 短持续时间。单次最大持续时间：1，间隔大于3。单位：秒。 |
| HMS\_FAST\_MEDIUM | 中等持续时间。单次最大持续时间：10，间隔大于30。单位：秒。 |
| HMS\_FAST\_LONG | 长持续时间。单次最大持续时间：60，间隔大于180。单位：秒。 |

### HMS\_FAST\_SchedulingOptimization\_ErrorCode

```c
enum HMS_FAST_SchedulingOptimization_ErrorCode
```

**描述**

系统性能优化的错误码。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS | 成功。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_HIGH\_SYSTEM\_LOAD | 系统高负载。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_POWER\_SAVING\_MODE | 省电模式。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_LOW\_POWER\_MODE | 低电量模式。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NON\_FRONTEND | 非前台调用场景。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INTERVAL | 间隔不满足要求。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_EXECUTE\_ERROR | 执行系统性能优化失败。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM | 参数无效。 |
| HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NO\_MEMORY | 内存不足。 |

## 函数说明

### HMS\_FAST\_RectPartition\_CreateConfig()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig ** config)
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

```c
FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig * config)
```

**描述**

销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁的矩形划分求解器的不透明配置[FAST\_RectPartitionConfig](fast-kit-fast.md#fast_rectpartitionconfig)。 |

### HMS\_FAST\_RectPartition\_SetAlgo()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig * config, const char * name )
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

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig * config, size_t size, const FAST_Rect * origin, FAST_Rect * result, size_t * resultSize )
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

当config选择"SweepLineAlgo"算法时，结果不会返回[FAST\_ERROR\_CODE\_FAIL](fast-kit-fast.md#fast_errorcode-1)，此处仅作为预防性设置。

### HMS\_FAST\_PolyRoot\_ComputeRoots()

```c
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRoots (const FAST_Poly * poly, const size_t maxRootCount, double * root, size_t * rootCount )
```

**描述**

计算多项式的给定数量的实数根。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| poly | 待求根的多项式[FAST\_Poly](fast-kit-fast.md#fast_poly)。 |
| maxRootCount | 需要返回的实根数量。 |
| root | 输出实根数组。 |
| rootCount | 实际返回的实根数量。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当poly或root或rootCount为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时（如指数未按升序排列），返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_PolyRoot\_ComputeSingle()

```c
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeSingle (const FAST_Poly * poly, double * root )
```

**描述**

计算多项式的绝对值最大的实根。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| poly | 待求根的多项式[FAST\_Poly](fast-kit-fast.md#fast_poly)。 |
| root | 计算出的实根。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当poly或root为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时（如指数未按升序排列），返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_PolyRoot\_ComputeRootIntervals()

```c
FAST_ErrorCode HMS_FAST_PolyRoot_ComputeRootIntervals (const FAST_Poly * poly, const size_t maxRootCount, double * leftBoundary, double * rightBoundary, size_t * rootCount )
```

**描述**

计算多项式给定数量的实根的隔离区间，输出每个实根的左右边界。每个区间包含且仅包含一个实根。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| poly | 待求根区间的多项式[FAST\_Poly](fast-kit-fast.md#fast_poly)。 |
| maxRootCount | 需要输出的实根的区间数量 |
| leftBoundary | 各个实根区间左边界的数组。 |
| rightBoundary | 各个实根区间右边界的数组。 |
| rootCount | 实际找到并返回的实根数量。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当poly或leftBoundary或rightBoundary或rootCount为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当输入非法时（如指数未按升序排列），返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_SegmentMap\_Create()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle * handle, size_t size, const int32_t * array, FAST_SegmentMapConfig * config )
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

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig ** config)
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

```c
FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle)
```

**描述**

销毁线段表实例。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 待销毁线段表句柄[FAST\_SegmentMapHandle](fast-kit-fast.md#fast_segmentmaphandle)。 |

### HMS\_FAST\_SegmentMap\_DestroyConfig()

```c
FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig * config)
```

**描述**

销毁线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁线段表不透明配置[FAST\_SegmentMapConfig](fast-kit-fast.md#fast_segmentmapconfig)。 |

### HMS\_FAST\_SegmentMap\_Query()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t * result )
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

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig * config, FAST_SegmentMapQueryType type )
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

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig * config, FAST_SegmentMapUpdateType type )
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

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value )
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

### HMS\_FAST\_Biquadm\_Create()

```c
FAST_ErrorCode HMS_FAST_Biquadm_Create (size_t numChannels, size_t numSections, size_t maxFrames, FAST_Biquadm ** filter)
```

**描述**

创建并初始化多通道多节二阶IIR滤波器组（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| numChannels | 信号通道数，必须大于0。 |
| numSections | 每通道级联的 biquad 节数，必须大于0。 |
| maxFrames | 单次处理的最大采样数（每通道），必须大于0。 |
| filter | 指向将接收新创建滤波器地址的变量指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当numChannels、numSections或maxFrames为0时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽分配失败时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_CreateD()

```c
FAST_ErrorCode HMS_FAST_Biquadm_CreateD (size_t numChannels, size_t numSections, size_t maxFrames, FAST_BiquadmD ** filter)
```

**描述**

创建并初始化多通道多节二阶IIR滤波器组（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| numChannels | 信号通道数，必须大于0。 |
| numSections | 每通道级联的 biquad 节数，必须大于0。 |
| maxFrames | 单次处理的最大采样数（每通道），必须大于0。 |
| filter | 指向将接收新创建滤波器地址的变量指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当numChannels、numSections或maxFrames为0时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽分配失败时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_Destroy()

```c
void HMS_FAST_Biquadm_Destroy (FAST_Biquadm * filter)
```

**描述**

销毁二阶滤波器实例（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 待销毁的二阶滤波器实例。 |

### HMS\_FAST\_Biquadm\_DestroyD()

```c
void HMS_FAST_Biquadm_DestroyD (FAST_BiquadmD * filter)
```

**描述**

销毁二阶滤波器实例（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 待销毁的二阶滤波器实例。 |

### HMS\_FAST\_Biquadm\_SetCoeffSingle()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingle (FAST_Biquadm * filter, const float * coeff, size_t stride)
```

**描述**

从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或coeff为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_SetCoeffDouble()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDouble (FAST_Biquadm * filter, const double * coeff, size_t stride)
```

**描述**

从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或coeff为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_SetCoeffSingleD()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffSingleD (FAST_BiquadmD * filter, const float * coeff, size_t stride)
```

**描述**

从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或coeff为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_SetCoeffDoubleD()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetCoeffDoubleD (FAST_BiquadmD * filter, const double * coeff, size_t stride)
```

**描述**

从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。系数按每节[b0, b1, b2, a1, a2]的顺序排列。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| coeff | 源系数数组。 |
| stride | 源数组中节与节之间的步长（以节为单位）。值为1表示连续存储。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或coeff为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_SetActiveFilters()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFilters (FAST_Biquadm * filter, const uint8_t * activeMask)
```

**描述**

设置二阶滤波器节的激活掩码（单精度）。掩码顺序为：[ch0\_sec0, ch0\_sec1, ch0\_sec2, ..., ch1\_sec0, ch1\_sec1, ch1\_sec2, ...]。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| activeMask | 布尔数组（大小为 filter->numSections）；非零表示激活。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm\_SetActiveFiltersD()

```c
FAST_ErrorCode HMS_FAST_Biquadm_SetActiveFiltersD (FAST_BiquadmD * filter, const uint8_t * activeMask)
```

**描述**

设置二阶滤波器节的激活掩码（双精度）。掩码顺序为：[ch0\_sec0, ch0\_sec1, ch0\_sec2, ..., ch1\_sec0, ch1\_sec1, ch1\_sec2, ...]。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 指向已初始化的二阶滤波器组的指针。 |
| activeMask | 布尔数组（大小为 filter->numSections）；非零表示激活。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter或activeMask为NULL，或filter的activeFilters为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Biquadm()

```c
FAST_ErrorCode HMS_FAST_Biquadm (FAST_Biquadm * filter, const float ** input, const size_t strideInput, float ** output, const size_t strideOutput, size_t length)
```

**描述**

通过二阶滤波器组处理多通道音频（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 已初始化的滤波器组。 |
| input | 输入通道指针数组（大小为 filter->numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter->numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter->maxFrames）。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter、coeff或output为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化或length超出范围时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_BiquadmD()

```c
FAST_ErrorCode HMS_FAST_BiquadmD (FAST_BiquadmD * filter, const double ** input, const size_t strideInput, double ** output, const size_t strideOutput, size_t length)
```

**描述**

通过二阶滤波器组处理多通道音频（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| filter | 已初始化的滤波器组。 |
| input | 输入通道指针数组（大小为 filter->numChannels）。 |
| strideInput | 每个输入通道内的步长。值为1表示连续存储。 |
| output | 输出通道指针数组（大小为 filter->numChannels）。 |
| strideOutput | 每个输出通道内的步长。值为1表示连续存储。 |
| length | 要处理的帧数（必须 ≤ filter->maxFrames）。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当filter、coeff或output为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当filter未初始化或length超出范围时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_DSP\_Maxmgv()

```c
float HMS_FAST_DSP_Maxmgv (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量中的最大幅值（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |

**返回：**

向量中的最大绝对值。如果length为0，则返回0.0f。

### HMS\_FAST\_DSP\_MaxmgvD()

```c
double HMS_FAST_DSP_MaxmgvD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量中的最大幅值（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 要处理的样本数。 |

**返回：**

向量中的最大绝对值。如果length为0，则返回0.0。

### HMS\_FAST\_DSP\_Maxvi()

```c
void HMS_FAST_DSP_Maxvi (const float * input, size_t stride, size_t length, float * value, size_t * index)
```

**描述**

查找步长实数向量中的最大值及其索引（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
| value | 用于存储最大值的指针。如果length为0，则返回-FLT\_MAX。 |
| index | 具有最大值的样本的索引（从0开始）。如果length为0，则返回0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_MaxviD()

```c
void HMS_FAST_DSP_MaxviD (const double * input, size_t stride, size_t length, double * value, size_t * index)
```

**描述**

查找步长实数向量中的最大值及其索引（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |
| value | 用于存储最大值的指针。如果length为0，则返回-DBL\_MAX。 |
| index | 具有最大值的样本的索引（从0开始）。如果length为0，则返回0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Sve()

```c
float HMS_FAST_DSP_Sve (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量的和（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

input[i]的和。如果length为0，则返回0.0f。

### HMS\_FAST\_DSP\_SveD()

```c
double HMS_FAST_DSP_SveD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量的和（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

input[i]的和。如果length为0，则返回0.0。

### HMS\_FAST\_DSP\_Svemg()

```c
float HMS_FAST_DSP_Svemg (const float * input, size_t stride, size_t length)
```

**描述**

计算步长向量的绝对值之和（L1范数）（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

输入向量内所有元素的绝对值的和。如果length为0，则返回0.0f。

### HMS\_FAST\_DSP\_SvemgD()

```c
double HMS_FAST_DSP_SvemgD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长向量的绝对值之和（L1范数）（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

输入向量内所有元素的绝对值的和。如果length为0，则返回0.0。

### HMS\_FAST\_DSP\_Meamgv()

```c
float HMS_FAST_DSP_Meamgv (const float * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量绝对值的均值（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

|input[i]|的均值。如果length为0，则返回0.0f。

### HMS\_FAST\_DSP\_MeamgvD()

```c
double HMS_FAST_DSP_MeamgvD (const double * input, size_t stride, size_t length)
```

**描述**

计算步长实数向量绝对值的均值（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

|input[i]|的均值。如果length为0，则返回0.0。

### HMS\_FAST\_DSP\_Dotpr()

```c
float HMS_FAST_DSP_Dotpr (const float * inputA, size_t strideA, const float * inputB, size_t strideB, size_t length)
```

**描述**

计算两个步长实数向量的点积（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

点积：sum(inputA[i] \* inputB[i])。如果length为0，则返回0.0f。

### HMS\_FAST\_DSP\_DotprD()

```c
double HMS_FAST_DSP_DotprD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, size_t length)
```

**描述**

计算两个步长实数向量的点积（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| length | 样本数。 |

**返回：**

点积：sum(inputA[i] \* inputB[i])。如果length为0，则返回0.0。

### HMS\_FAST\_DSP\_Vsbsm()

```c
void HMS_FAST_DSP_Vsbsm (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float scalar, float * outputC, size_t strideC, size_t length)
```

**描述**

执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| scalar | 用于计算的标量。 |
| outputC | 输出向量（调用者分配）。 |
| strideC | 输出向量的步长。值为1表示连续存储。 |
| length | 样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsbsmD()

```c
void HMS_FAST_DSP_VsbsmD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double scalar, double * outputC, size_t strideC, size_t length)
```

**描述**

执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 第一个输入向量。 |
| strideA | 第一个向量的步长。值为1表示连续存储。 |
| inputB | 第二个输入向量。 |
| strideB | 第二个向量的步长。值为1表示连续存储。 |
| scalar | 用于计算的标量。 |
| outputC | 输出向量（调用者分配）。 |
| strideC | 输出向量的步长。值为1表示连续存储。 |
| length | 样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Ctoz()

```c
void HMS_FAST_DSP_Ctoz (const float * input, size_t strideInput, FAST_SplitComplex * output, size_t strideOutput, size_t length)
```

**描述**

将交错复数数组（real, imag, real, imag, ...）转换为分离格式（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 交错复数输入（长度为复数数量的2倍）。 |
| strideInput | 复数样本之间的步长。值为1表示连续存储。 |
| output | 分离复数输出结构体。 |
| strideOutput | 输出数组中实部/虚部样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_CtozD()

```c
void HMS_FAST_DSP_CtozD (const double * input, size_t strideInput, FAST_SplitComplexD * output, size_t strideOutput, size_t length)
```

**描述**

将交错复数数组（real, imag, real, imag, ...）转换为分离格式（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 交错复数输入（长度为复数数量的2倍）。 |
| strideInput | 复数样本之间的步长。值为1表示连续存储。 |
| output | 分离复数输出结构体。 |
| strideOutput | 输出数组中实部/虚部样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Ztoc()

```c
void HMS_FAST_DSP_Ztoc (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

将分离复数数组转换为交错格式（单精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离复数输入结构体。 |
| strideInput | 实部/虚部数组中样本之间的步长。值为1表示连续存储。 |
| output | 交错输出数组（长度为复数数量的2倍）。 |
| strideOutput | 输出中复数样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_ZtocD()

```c
void HMS_FAST_DSP_ZtocD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

将分离复数数组转换为交错格式（双精度）。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离复数输入结构体。 |
| strideInput | 实部/虚部数组中样本之间的步长。值为1表示连续存储。 |
| output | 交错输出数组（长度为复数数量的2倍）。 |
| strideOutput | 输出中复数样本之间的步长。值为1表示连续存储。 |
| length | 要转换的复数样本数。必须大于0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Zvabs()

```c
void HMS_FAST_DSP_Zvabs (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的幅值（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_ZvabsD()

```c
void HMS_FAST_DSP_ZvabsD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的幅值（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Zvmags()

```c
void HMS_FAST_DSP_Zvmags (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的幅值平方（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值平方）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_ZvmagsD()

```c
void HMS_FAST_DSP_ZvmagsD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的幅值平方（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（幅值平方）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Zvphas()

```c
void HMS_FAST_DSP_Zvphas (const FAST_SplitComplex * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的相位角（弧度制）（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（相位角）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_ZvphasD()

```c
void HMS_FAST_DSP_ZvphasD (const FAST_SplitComplexD * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

计算复数向量的相位角（弧度制）（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 分离格式复数输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针（相位角）。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的复数元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsmul()

```c
void HMS_FAST_DSP_Vsmul (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```

**描述**

将向量的每个元素乘以标量，output[i] = input[i] \* scalar（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 乘法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsmulD()

```c
void HMS_FAST_DSP_VsmulD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```

**描述**

将向量的每个元素乘以标量，output[i] = input[i] \* scalar（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 乘法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsdiv()

```c
void HMS_FAST_DSP_Vsdiv (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```

**描述**

将向量的每个元素除以标量，output[i] = input[i] / scalar（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 除数标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsdivD()

```c
void HMS_FAST_DSP_VsdivD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```

**描述**

将向量的每个元素除以标量，output[i] = input[i] / scalar（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 除数标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Svdiv()

```c
void HMS_FAST_DSP_Svdiv (const float scalar, const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

将标量除以向量的每个元素，output[i] = scalar / input[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| scalar | 被除数标量。 |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_SvdivD()

```c
void HMS_FAST_DSP_SvdivD (const double scalar, const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

将标量除以向量的每个元素，output[i] = scalar / input[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| scalar | 被除数标量。 |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsadd()

```c
void HMS_FAST_DSP_Vsadd (const float * input, size_t strideInput, const float scalar, float * output, size_t strideOutput, size_t length)
```

**描述**

将标量加到向量的每个元素，output[i] = input[i] + scalar（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 加法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsaddD()

```c
void HMS_FAST_DSP_VsaddD (const double * input, size_t strideInput, const double scalar, double * output, size_t strideOutput, size_t length)
```

**描述**

将标量加到向量的每个元素，output[i] = input[i] + scalar（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| scalar | 加法标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vadd()

```c
void HMS_FAST_DSP_Vadd (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素加法，C[i] = A[i] + B[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VaddD()

```c
void HMS_FAST_DSP_VaddD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素加法，C[i] = A[i] + B[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsub()

```c
void HMS_FAST_DSP_Vsub (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素减法，C[i] = A[i] - B[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsubD()

```c
void HMS_FAST_DSP_VsubD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素减法，C[i] = A[i] - B[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vmul()

```c
void HMS_FAST_DSP_Vmul (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素乘法，C[i] = A[i] \* B[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VmulD()

```c
void HMS_FAST_DSP_VmulD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素乘法，C[i] = A[i] \* B[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vdiv()

```c
void HMS_FAST_DSP_Vdiv (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素除法，C[i] = A[i] / B[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针（被除数）。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针（除数）。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VdivD()

```c
void HMS_FAST_DSP_VdivD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```

**描述**

执行向量逐元素除法，C[i] = A[i] / B[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针（被除数）。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针（除数）。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vdist()

```c
void HMS_FAST_DSP_Vdist (const float * inputA, size_t strideA, const float * inputB, size_t strideB, float * outputC, size_t strideC, size_t length)
```

**描述**

计算两个向量对应元素的欧几里得范数（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VdistD()

```c
void HMS_FAST_DSP_VdistD (const double * inputA, size_t strideA, const double * inputB, size_t strideB, double * outputC, size_t strideC, size_t length)
```

**描述**

计算两个向量对应元素的欧几里得范数（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 输入向量A指针。 |
| strideA | 向量A的步长。值为1表示连续存储。 |
| inputB | 输入向量B指针。 |
| strideB | 向量B的步长。值为1表示连续存储。 |
| outputC | 输出向量C指针。 |
| strideC | 向量C的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Svesq()

```c
float HMS_FAST_DSP_Svesq (const float * input, size_t stride, size_t length)
```

**描述**

计算向量元素的平方和（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 输入向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

向量元素的平方和。

### HMS\_FAST\_DSP\_SvesqD()

```c
double HMS_FAST_DSP_SvesqD (const double * input, size_t stride, size_t length)
```

**描述**

计算向量元素的平方和（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 输入向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

向量元素的平方和。

### HMS\_FAST\_DSP\_Minvi()

```c
void HMS_FAST_DSP_Minvi (const float * input, size_t stride, size_t length, float * value, size_t * index)
```

**描述**

查找步长实数向量中的最小值及其索引（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 待处理的样本数。 |
| value | 输出参数，存储找到的最小值。如果length为0，设置为FLT\_MAX。 |
| index | 输出参数，存储最小值的索引（0基）。如果length为0，设置为0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_MinviD()

```c
void HMS_FAST_DSP_MinviD (const double * input, size_t stride, size_t length, double * value, size_t * index)
```

**描述**

查找步长实数向量中的最小值及其索引（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| stride | 连续样本之间的距离。值为1表示连续存储。 |
| length | 待处理的样本数。 |
| value | 输出参数，存储找到的最小值。如果length为0，设置为DBL\_MAX。 |
| index | 输出参数，存储最小值的索引（0基）。如果length为0，设置为0。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsq()

```c
void HMS_FAST_DSP_Vsq (const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

计算向量每个元素的平方（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsqD()

```c
void HMS_FAST_DSP_VsqD (const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

计算向量每个元素的平方（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vabs()

```c
void HMS_FAST_DSP_Vabs (const float * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

计算向量每个元素的绝对值（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VabsD()

```c
void HMS_FAST_DSP_VabsD (const double * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

计算向量每个元素的绝对值（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vthr()

```c
void HMS_FAST_DSP_Vthr (const float * input, size_t strideInput, const float threshold, float * output, size_t strideOutput, size_t length)
```

**描述**

对向量应用阈值，若input[i] < threshold则output[i] = threshold，否则output[i] = input[i]（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| threshold | 阈值标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VthrD()

```c
void HMS_FAST_DSP_VthrD (const double * input, size_t strideInput, const double threshold, double * output, size_t strideOutput, size_t length)
```

**描述**

对向量应用阈值，若input[i] < threshold则output[i] = threshold，否则output[i] = input[i]（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| threshold | 阈值标量。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vrvrs()

```c
void HMS_FAST_DSP_Vrvrs (float * vector, size_t stride, size_t length)
```

**描述**

原地反转向量中元素的顺序（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待反转的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VrvrsD()

```c
void HMS_FAST_DSP_VrvrsD (double * vector, size_t stride, size_t length)
```

**描述**

原地反转向量中元素的顺序（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待反转的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vspdp()

```c
void HMS_FAST_DSP_Vspdp (const float * input, size_t strideInput, double * output, size_t strideOutput, size_t length)
```

**描述**

将单精度向量转换为双精度向量。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 单精度输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 双精度输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vdpsp()

```c
void HMS_FAST_DSP_Vdpsp (const double * input, size_t strideInput, float * output, size_t strideOutput, size_t length)
```

**描述**

将双精度向量转换为单精度向量。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 双精度输入向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| output | 单精度输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vfill()

```c
void HMS_FAST_DSP_Vfill (float * vector, size_t stride, size_t length, const float scalar)
```

**描述**

使用指定标量值填充向量（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待填充的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待填充的元素数量。 |
| scalar | 标量值。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VfillD()

```c
void HMS_FAST_DSP_VfillD (double * vector, size_t stride, size_t length, const double scalar)
```

**描述**

使用指定标量值填充向量（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待填充的向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待填充的元素数量。 |
| scalar | 标量值。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vclr()

```c
void HMS_FAST_DSP_Vclr (float * vector, size_t stride, size_t length)
```

**描述**

将向量所有元素清零（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 输出向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待清零的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VclrD()

```c
void HMS_FAST_DSP_VclrD (double * vector, size_t stride, size_t length)
```

**描述**

将向量所有元素清零（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 输出向量指针。 |
| stride | 向量的步长。值为1表示连续存储。 |
| length | 待清零的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Conv()

```c
void HMS_FAST_DSP_Conv (const float * input, size_t strideInput, const float * filter, size_t strideFilter, float * output, size_t strideOutput, size_t outputLength, size_t filterLength)
```

**描述**

执行两个向量的卷积运算（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入信号向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| filter | 滤波器系数向量指针。 |
| strideFilter | 滤波器向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| outputLength | 输出向量中的元素数量。 |
| filterLength | 滤波器向量中的元素数量。 |

**返回：**

无。

**注解：**

input缓冲区长度必须大于outputLength + filterLength - 1，否则将产生未定义行为。

### HMS\_FAST\_DSP\_ConvD()

```c
void HMS_FAST_DSP_ConvD (const double * input, size_t strideInput, const double * filter, size_t strideFilter, double * output, size_t strideOutput, size_t outputLength, size_t filterLength)
```

**描述**

执行两个向量的卷积运算（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| input | 输入信号向量指针。 |
| strideInput | 输入向量的步长。值为1表示连续存储。 |
| filter | 滤波器系数向量指针。 |
| strideFilter | 滤波器向量的步长。值为1表示连续存储。 |
| output | 输出向量指针。 |
| strideOutput | 输出向量的步长。值为1表示连续存储。 |
| outputLength | 输出向量中的元素数量。 |
| filterLength | 滤波器向量中的元素数量。 |

**返回：**

无。

**注解：**

input缓冲区长度必须大于outputLength + filterLength - 1，否则将产生未定义行为。

### HMS\_FAST\_DSP\_HannWindow()

```c
void HMS_FAST_DSP_HannWindow (float * output, size_t length, HMS_FAST_HannWindowType type)
```

**描述**

生成汉宁窗序列（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| output | 输出向量指针，用于存放窗系数。 |
| length | 生成的窗点数。 |
| type | 窗类型，参见[HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1)。 |

**返回：**

无。

### HMS\_FAST\_DSP\_HannWindowD()

```c
void HMS_FAST_DSP_HannWindowD (double * output, size_t length, HMS_FAST_HannWindowType type)
```

**描述**

生成汉宁窗序列（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| output | 输出向量指针，用于存放窗系数。 |
| length | 生成的窗点数。 |
| type | 窗类型，参见[HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1)。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Mmul()

```c
void HMS_FAST_DSP_Mmul (const float * matrixA, size_t strideA, const float * matrixB, size_t strideB, float * matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)
```

**描述**

执行矩阵乘法，C = A \* B，其中A为MxP矩阵、B为PxN矩阵、C为MxN矩阵（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| matrixA | 矩阵A指针。 |
| strideA | 矩阵A的元素步长。 |
| matrixB | 矩阵B指针。 |
| strideB | 矩阵B的元素步长。 |
| matrixC | 矩阵C指针（结果）。 |
| strideC | 矩阵C的元素步长。 |
| rowsM | 矩阵A和C的行数。 |
| colsN | 矩阵B和C的列数。 |
| colsP | 矩阵A的列数和矩阵B的行数。 |

**返回：**

无。

### HMS\_FAST\_DSP\_MmulD()

```c
void HMS_FAST_DSP_MmulD (const double * matrixA, size_t strideA, const double * matrixB, size_t strideB, double * matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)
```

**描述**

执行矩阵乘法，C = A \* B，其中A为MxP矩阵、B为PxN矩阵、C为MxN矩阵（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| matrixA | 矩阵A指针。 |
| strideA | 矩阵A的元素步长。 |
| matrixB | 矩阵B指针。 |
| strideB | 矩阵B的元素步长。 |
| matrixC | 矩阵C指针（结果）。 |
| strideC | 矩阵C的元素步长。 |
| rowsM | 矩阵A和C的行数。 |
| colsN | 矩阵B和C的列数。 |
| colsP | 矩阵A的列数和矩阵B的行数。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vvpow()

```c
void HMS_FAST_DSP_Vvpow (const float * inputA, const float * inputB, float * outputC, size_t length)
```

**描述**

执行向量逐元素幂运算，C[i]等于A[i]的B[i]次方（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 底数向量A指针。 |
| inputB | 指数向量B指针。 |
| outputC | 输出向量C指针。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VvpowD()

```c
void HMS_FAST_DSP_VvpowD (const double * inputA, const double * inputB, double * outputC, size_t length)
```

**描述**

执行向量逐元素幂运算，C[i]等于A[i]的B[i]次方（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| inputA | 底数向量A指针。 |
| inputB | 指数向量B指针。 |
| outputC | 输出向量C指针。 |
| length | 待处理的元素数量。 |

**返回：**

无。

### HMS\_FAST\_DSP\_Vsort()

```c
void HMS_FAST_DSP_Vsort (float * vector, size_t length, int order)
```

**描述**

对向量进行原地排序（单精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待排序的向量指针（输入/输出）。 |
| length | 待排序的元素数量。 |
| order | 排序顺序（1表示升序，-1表示降序，其他值不执行操作）。 |

**返回：**

无。

### HMS\_FAST\_DSP\_VsortD()

```c
void HMS_FAST_DSP_VsortD (double * vector, size_t length, int order)
```

**描述**

对向量进行原地排序（双精度）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| vector | 待排序的向量指针（输入/输出）。 |
| length | 待排序的元素数量。 |
| order | 排序顺序（1表示升序，-1表示降序，其他值不执行操作）。 |

**返回：**

无。

### HMS\_FAST\_FFT\_CreateConfig()

```c
FAST_ErrorCode HMS_FAST_FFT_CreateConfig (FAST_FFTConfig** config, const uint32_t log2n)
```

**描述**

创建单精度FFT的不透明配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)（即1到16）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向快速傅里叶变换的不透明配置[FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig)的指针。 |
| log2n | FFT点数对应的以2为底的对数值（即变换长度N=1<<log2n）。必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)（即1到16）。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当log2n超出范围时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_FFT\_CreateConfigD()

```c
FAST_ErrorCode HMS_FAST_FFT_CreateConfigD (FAST_FFTConfig** config, const uint32_t log2n)
```

**描述**

创建双精度FFT的不透明配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。与[HMS\_FAST\_FFT\_CreateConfig](fast-kit-fast.md#hms_fast_fft_createconfig)功能相同，但用于双精度（double）计算，提供更高的数值精度。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向快速傅里叶变换的不透明配置[FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig)的指针。 |
| log2n | FFT点数对应的以2为底的对数值（即变换长度N=1<<log2n）。必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)（即1到16）。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当log2n超出范围时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_FFT\_DestroyConfig()

```c
void HMS_FAST_FFT_DestroyConfig (FAST_FFTConfig* config)
```

**描述**

销毁FFT的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 待销毁的FFT的不透明配置[FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig)。 |

**返回：**

无。

### HMS\_FAST\_FFT\_ForwardTransform()

```c
FAST_ErrorCode HMS_FAST_FFT_ForwardTransform (FAST_FFTConfig* config, const uint32_t length, const float input[], float outputRe[], float outputIm[])
```

**描述**

计算单精度实数时域信号的离散傅里叶变换（DFT）。该变换将实数时域信号转换为复数频域信号，最终输出复数频谱。

对于长度为N的实数输入，输出包含N/2+1个复数频率分量（由于实信号的频谱共轭对称性，只需存储前半部分）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由[HMS\_FAST\_FFT\_CreateConfig](fast-kit-fast.md#hms_fast_fft_createconfig)创建。 |
| length | 输入信号长度。必须等于创建配置时指定的2^log2n。 |
| input | 实数时域输入数组，大小为length。 |
| outputRe | 复数频域输出的实部数组，大小为length/2+1。 |
| outputIm | 复数频域输出的虚部数组，大小为length/2+1。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当input、outputRe或outputIm为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当length不等于2^log2n时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_FFT\_ForwardTransformD()

```c
FAST_ErrorCode HMS_FAST_FFT_ForwardTransformD (FAST_FFTConfig* config, const uint32_t length, const double input[], double outputRe[], double outputIm[])
```

**描述**

计算双精度实数时域信号的离散傅里叶变换（DFT）。与[HMS\_FAST\_FFT\_ForwardTransform](fast-kit-fast.md#hms_fast_fft_forwardtransform) 功能相同，但使用双精度（double）计算。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由[HMS\_FAST\_FFT\_CreateConfigD](fast-kit-fast.md#hms_fast_fft_createconfigd)创建。 |
| length | 输入信号长度。必须等于2^log2n。 |
| input | 实数时域输入数组，大小为length。 |
| outputRe | 复数频域输出的实部数组，大小为length/2+1。 |
| outputIm | 复数频域输出的虚部数组，大小为length/2+1。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当input、outputRe或outputIm为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当length不等于2^log2n时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_FFT\_InverseTransform()

```c
FAST_ErrorCode HMS_FAST_FFT_InverseTransform (FAST_FFTConfig* config, const uint32_t length, const float inputRe[], const float inputIm[], float output[])
```

**描述**

计算单精度复数频域序列的逆离散傅里叶变换（IDFT）。将频域信号转换回时域表示。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由[HMS\_FAST\_FFT\_CreateConfig](fast-kit-fast.md#hms_fast_fft_createconfig) 创建。 |
| length | 输出信号长度。必须等于2^log2n。 |
| inputRe | 复数频域输入的实部数组，大小为length/2+1。 |
| inputIm | 复数频域输入的虚部数组，大小为length/2+1。 |
| output | 实数时域输出数组，大小为length。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当inputRe、inputIm或output为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当length不等于2^log2n时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_FFT\_InverseTransformD()

```c
FAST_ErrorCode HMS_FAST_FFT_InverseTransformD (FAST_FFTConfig* config, const uint32_t length, const double inputRe[], const double inputIm[], double output[])
```

**描述**

计算双精度复数频域序列的逆离散傅里叶变换（IDFT）。与[HMS\_FAST\_FFT\_InverseTransform](fast-kit-fast.md#hms_fast_fft_inversetransform)功能相同，但使用双精度（double）计算。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 有效的FFT配置，由[HMS\_FAST\_FFT\_CreateConfigD](fast-kit-fast.md#hms_fast_fft_createconfigd)创建。 |
| length | 输出信号长度。必须等于2^log2n。 |
| inputRe | 复数频域输入的实部数组，大小为length/2+1。 |
| inputIm | 复数频域输入的虚部数组，大小为length/2+1。 |
| output | 实数时域输出数组，大小为length。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当inputRe、inputIm或output为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

length不等于2^log2n时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_Create()

```c
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create(
    FAST_ConcurrentHashmapHandle* handle,
    HMS_FAST_ConcurrentHashmap_HashFunc hasher,
    HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler,
    float maxLoadFac,
    size_t numShards
)
```

**描述**

根据输入配置创建并发哈希表。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| hasher | 开发者定义的哈希值计算回调函数。 |
| equaler | 开发者定义的键比较回调函数。 |
| maxLoadFac | 初始设定的最大负载因子。 |
| numShards | 初始设定的分段数。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle或相关回调函数为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽构造失败时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_Destroy()

```c
void HMS_FAST_ConcurrentHashmap_Destroy(FAST_ConcurrentHashmapHandle handle)
```

**描述**

销毁给定并发哈希表。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 待销毁的并发哈希表句柄。 |

### HMS\_FAST\_ConcurrentHashmap\_Insert()

```c
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Insert(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    const FAST_ConcurrentHashmapValuePtr value,
    FAST_ConcurrentHashmapValuePtr* originValue
)
```

**描述**

将给定键值对插入并发哈希表，如果给定的键在哈希表中已经存在，则覆写原有的值。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待插入的键指针。 |
| value | 待插入的值指针。 |
| originValue | 将被覆盖的值的指针，仅在返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)时有效，如果不需要请传入NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中存在相同的键时，使用value覆盖已有的值并返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_Find()

```c
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Find(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapValuePtr* value
)
```

**描述**

查找并发哈希表中给定键对应的值，将结果保存在value指针中。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待查找的键指针。 |
| value | 用于保存查询结果的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle、key或value为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中不存在匹配的键时，返回[FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_Erase()

```c
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    FAST_ConcurrentHashmapKeyPtr* originKey,
    FAST_ConcurrentHashmapValuePtr* originValue
)
```

**描述**

在并发哈希表中删除给定的键及其对应的值，并将其值保存在originalKey和originalValue中以便于开发者进行内存管理；实际使用时也可根据需求将originalKey或originalValue设为NULL，此时则不会将键或值的地址返回。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待删除的键指针。 |
| originKey | 用于返回哈希表中保存的键的指针，可为NULL。 |
| originValue | 用于返回哈希表中保存的值得指针，可为NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle或key为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中不存在匹配的键时，返回[FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_TryInsert()

```c
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_TryInsert(
    FAST_ConcurrentHashmapHandle handle,
    const FAST_ConcurrentHashmapKeyPtr key,
    const FAST_ConcurrentHashmapValuePtr value
)
```

**描述**

将给定键值对插入并发哈希表，如果给定的键在哈希表中已经存在，则放弃插入保持原状。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| key | 待插入的键指针。 |
| value | 待插入的值指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle、key或value为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中存在相同的键时，不执行任何操作并返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_ConcurrentHashmap\_Size()

```c
size_t HMS_FAST_ConcurrentHashmap_Size(FAST_ConcurrentHashmapHandle handle)
```

**描述**

返回给定并发哈希表中的元素个数。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |

**返回：**

给定并发哈希表的元素个数，需注意在重度并发操作下该返回值可能与实际值存在细微偏差。

### HMS\_FAST\_ConcurrentHashmap\_Clear()

```c
void HMS_FAST_ConcurrentHashmap_Clear(FAST_ConcurrentHashmapHandle handle)
```

**描述**

清空给定并发哈希表中的所有元素。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |

### HMS\_FAST\_ConcurrentHashmap\_EraseIf()

```c
size_t HMS_FAST_ConcurrentHashmap_EraseIf(
    FAST_ConcurrentHashmapHandle handle,
    HMS_FAST_ConcurrentHashmap_HookFunc condFunc,
    void* condCtx,
    HMS_FAST_ConcurrentHashmap_HookFunc freeFunc,
    void* freeCtx
)
```

**描述**

遍历哈希表并删除所有符合给定条件的键值对，同时使用开发者定义的freeFunc释放键值对的内存；实际使用时freeFunc可为NULL，此时要求开发者另行完成内存管理动作。注意：请避免在condFunc和freeFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的删除条件回调函数。 |
| condCtx | 条件回调函数的上下文。 |
| freeFunc | 开发者定义的内存释放回调函数，可为NULL。 |
| freeCtx | 内存释放回调函数的上下文。 |

**返回：**

完成删除操作的元素个数。

### HMS\_FAST\_ConcurrentHashmap\_Traverse()

```c
void HMS_FAST_ConcurrentHashmap_Traverse(
    FAST_ConcurrentHashmapHandle handle,
    HMS_FAST_ConcurrentHashmap_HookFunc condFunc,
    void* condCtx,
    HMS_FAST_ConcurrentHashmap_HookFunc workFunc,
    void* workCtx
)
```

**描述**

遍历哈希表并对所有符合开发者condFunc的键值对执行workFunc中的修改；如果condFunc为NULL，则对于表中存在的所有键值对都将执行开发者定义的workFunc。注意：请避免在condFunc和workFunc中定义复杂的逻辑（如加锁等）以避免死锁等不可控现象。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| handle | 并发哈希表句柄。 |
| condFunc | 开发者定义的条件回调函数，可为NULL。 |
| condCtx | 回调函数的上下文。 |
| workFunc | 开发者定义的修改回调函数。 |
| workCtx | 修改函数的上下文。 |

### HMS\_FAST\_Hashmap\_Clear()

```c
void HMS_FAST_Hashmap_Clear (FAST_HashmapHandle handle)
```

**描述**

从哈希表中删除所有元素。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |

**返回：**

无

### HMS\_FAST\_Hashmap\_Create()

```c
FAST_ErrorCode HMS_FAST_Hashmap_Create (FAST_HashmapHandle* handle, HMS_FAST_Hashmap_HashFunc hasher, HMS_FAST_Hashmap_KeyEqualFunc equaler)
```

**描述**

根据输入配置创建哈希表。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 存储创建的哈希表句柄指针。 |
| hasher | 自定义哈希计算回调函数。 |
| equaler | 自定义的键比较回调函数。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle或相关回调函数为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽构造失败时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Hashmap\_Destroy()

```c
void HMS_FAST_Hashmap_Destroy (FAST_HashmapHandle handle)
```

**描述**

销毁给定哈希表。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 要销毁的哈希表句柄。 |

**返回：**

无

**注解：**

此函数不释放与键或值相关的内存。调用者保留所有键和值资源的所有权，必须显式释放它们以避免内存泄漏。

### HMS\_FAST\_Hashmap\_Erase()

```c
FAST_ErrorCode HMS_FAST_Hashmap_Erase (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapKeyPtr* originKey, FAST_HashmapValuePtr* originValue)
```

**描述**

从哈希表中按键删除条目。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要删除的条目的键。 |
| originKey | 将被删除的键的指针，仅在成功时有效，如果不需要请传入NULL。 |
| originValue | 将被删除的值的指针，仅在成功时有效，如果不需要请传入NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle或key为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中不存在匹配的键时，返回[FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

**注解：**

内存不会自动释放，用户必须使用**originKey**和**originValue**手动释放。

### HMS\_FAST\_Hashmap\_EraseIf()

```c
size_t HMS_FAST_Hashmap_EraseIf (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc freeFunc, void* freeCtx)
```

**描述**

删除满足给定条件的所有元素。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| condFunc | 自定义的删除条件回调函数。 |
| condCtx | 条件回调函数的上下文。 |
| freeFunc | 开发者定义的内存释放回调函数，可为NULL。 |
| freeCtx | 内存释放回调函数的上下文。 |

**返回：**

成功删除的元素数量。

### HMS\_FAST\_Hashmap\_Find()

```c
FAST_ErrorCode HMS_FAST_Hashmap_Find (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, FAST_HashmapValuePtr* value)
```

**描述**

检索与给定键关联的值。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要查找的键。 |
| value | 存储检索值的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle、key或value为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中不存在匹配的键时，返回[FAST\_ERROR\_CODE\_KEY\_NOT\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Hashmap\_Insert()

```c
FAST_ErrorCode HMS_FAST_Hashmap_Insert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value, FAST_HashmapValuePtr* originValue)
```

**描述**

在哈希表中插入或更新键值对。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要插入或更新的键。 |
| value | 与键关联的值。 |
| originValue | 将被覆盖的值的指针，仅在返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)时有效，如果不需要请传入NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中存在相同的键时，使用value覆盖已有的值并返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

**注解：**

* 如果键已存在，返回值将为[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)，其值将被覆盖。
* 调用者保留键和值内存的所有权。哈希表仅存储指针；不复制或管理内存。

### HMS\_FAST\_Hashmap\_Size()

```c
size_t HMS_FAST_Hashmap_Size (FAST_HashmapHandle handle)
```

**描述**

返回哈希表中当前存储的键值对数量。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |

**返回：**

哈希表中的元素数量。

### HMS\_FAST\_Hashmap\_Traverse()

```c
void HMS_FAST_Hashmap_Traverse (FAST_HashmapHandle handle, HMS_FAST_Hashmap_HookFunc condFunc, void* condCtx, HMS_FAST_Hashmap_HookFunc workFunc, void* workCtx)
```

**描述**

遍历哈希表，可选择过滤元素并应用工作函数。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| condFunc | 可选的条件函数；如果提供，仅当 condFunc 返回非零时才对条目调用 workFunc。传入 NULL 以对所有条目应用 workFunc。 |
| condCtx | 用户定义的上下文，允许用户供应 condFunc 在执行期间可能需要的自定义数据。 |
| workFunc | 对选定条目应用的函数。 |
| workCtx | 用户定义的上下文，允许用户供应 workFunc 在执行期间可能需要的自定义数据。 |

**返回：**

无

**注解：**

condFunc和workFunc都在内部锁下调用；避免在这些回调中阻塞或重新进入哈希表API。

### HMS\_FAST\_Hashmap\_TryInsert()

```c
FAST_ErrorCode HMS_FAST_Hashmap_TryInsert (FAST_HashmapHandle handle, const FAST_HashmapKeyPtr key, const FAST_HashmapValuePtr value)
```

**描述**

仅当键不存在时插入键值对。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| handle | 哈希表句柄。 |
| key | 要插入的键。 |
| value | 与键关联的值。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当handle、key或value为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当哈希表中存在相同的键时，不执行任何操作并返回[FAST\_ERROR\_CODE\_KEY\_EXISTS](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

**注解：**

调用者管理键和值内存的生命周期。

### HMS\_FAST\_Algo\_Sort()

```c
FAST_ErrorCode HMS_FAST_Algo_Sort (HMS_FAST_SortData * data, HMS_FAST_Sort_CompFunc comp)
```

**描述**

使用用户提供的比较函数对任意类型数组进行完整排序。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。data->data不能为NULL，data->sizeOf必须大于0，data->length必须大于0。 |
| comp | 用户自定义的比较函数。不能为NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当data->sizeOf或data->length为0时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当data、data->data或comp为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Algo\_PartialSortAt()

```c
FAST_ErrorCode HMS_FAST_Algo_PartialSortAt (HMS_FAST_SortData * data, size_t offset, size_t count, HMS_FAST_Sort_CompFunc comp)
```

**描述**

对数组进行原地部分排序，使指定区间[offset, offset + count)包含排序后对应位置的元素。

**功能说明：**

* 子数组[offset, offset+count)包含排序后的第offset个到第(offset+count-1)个元素，按升序排列。
* offset之前的所有元素小于子数组中的最小元素。
* offset+count之后的所有元素大于子数组中的最大元素。
* 子数组之外的元素不保证排序。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。与[HMS\_FAST\_Algo\_Sort](fast-kit-fast.md#hms_fast_algo_sort)要求相同。 |
| offset | 子数组的起始索引。 |
| count | 子数组的元素数量。 |
| comp | 用户自定义的比较函数。不能为NULL。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当data->sizeOf或data->length为0，或(offset+count)越界时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当data、data->data或comp为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_Algo\_NaturalSort()

```c
FAST_ErrorCode HMS_FAST_Algo_NaturalSort (HMS_FAST_SortData * data, int32_t ascend)
```

**描述**

使用自然语言规则对UTF-8编码的C字符串数组进行排序。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。data->data不能为NULL，data->sizeOf必须大于0，data->length必须大于0。注意：data->sizeOf必须等于sizeof(char\*)。 |
| ascend | 排序方向，非零为升序，零为降序。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当data->length为0，或data->sizeOf不等于sizeof(char\*)时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当data或data->data为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当引用的三方库报错导致执行失败时，返回[FAST\_ERROR\_CODE\_FAIL](fast-kit-fast.md#fast_errorcode-1)。

**注解：**

* 此函数专门用于排序人类可读文本，要求data->data指向char\*数组。
* 如果data->data不包含有效的null终止C字符串（如整数、结构体指针等），行为未定义，可能导致崩溃或内存损坏。
* 自然语言排序会将字符串中的数字序列视为数值进行比较，例如：file1, file2, file10, file20。

### HMS\_FAST\_Algo\_NaturalPartialSortAt()

```c
FAST_ErrorCode HMS_FAST_Algo_NaturalPartialSortAt (HMS_FAST_SortData * data, size_t offset, size_t count, int32_t ascend)
```

**描述**

使用自然语言规则对UTF-8编码的C字符串数组进行部分排序，使指定区间[offset, offset + count)包含排序后对应位置的元素。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| data | 待排序数据的描述符。与[HMS\_FAST\_Algo\_NaturalSort](fast-kit-fast.md#hms_fast_algo_naturalsort)要求相同。 |
| offset | 子数组的起始索引。 |
| count | 子数组的元素数量。 |
| ascend | 排序方向，非零为升序，零为降序。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](fast-kit-fast.md#fast_errorcode-1)。

当data->length为0，或(offset+count)越界，或data->sizeOf不等于sizeof(char\*)时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](fast-kit-fast.md#fast_errorcode-1)。

当data或data->data为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](fast-kit-fast.md#fast_errorcode-1)。

当引用的三方库报错导致执行失败时，返回[FAST\_ERROR\_CODE\_FAIL](fast-kit-fast.md#fast_errorcode-1)。

### HMS\_FAST\_PerfHintConfigBuilder\_Create()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Create (HMS_FAST_PerfHintConfigBuilder** builder)
```

**描述**

创建构建器实例。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 指向创建的构建器实例的引用。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当内存不足，无法分配新实例时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NO\_MEMORY](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfigBuilder\_Destroy()

```c
void HMS_FAST_PerfHintConfigBuilder_Destroy (HMS_FAST_PerfHintConfigBuilder* builder)
```

**描述**

销毁构建器。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |

### HMS\_FAST\_PerfHintConfigBuilder\_SetSceneType()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneType sceneType)
```

**描述**

设置需要系统性能优化的场景类型。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| sceneType | 需要系统性能优化的场景类型。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfigBuilder\_SetSceneState()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetSceneState (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_SceneState sceneState)
```

**描述**

设置需要系统性能优化的场景状态。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| sceneState | 需要系统性能优化的场景状态。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfigBuilder\_SetDurationType()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetDurationType (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_SchedulingOptimization_DurationType durationType)
```

**描述**

设置需要系统性能优化的持续时间选项。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| durationType | 需要系统性能优化的持续时间选项。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfigBuilder\_SetTids()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_SetTids (HMS_FAST_PerfHintConfigBuilder* builder, int* tids, uint32_t tidsSize)
```

**描述**

设置需要优化的线程ID。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| tids | 需要优化的线程ID数组。 |
| tidsSize | 线程ID数组大小，最大长度为16。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfigBuilder\_Build()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_PerfHintConfigBuilder_Build (HMS_FAST_PerfHintConfigBuilder* builder, HMS_FAST_PerfHintConfig** config)
```

**描述**

创建系统性能优化配置参数。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| builder | 构建器实例指针。 |
| config | 指向接收系统性能优化配置参数对象的指针。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当内存不足，无法分配新实例时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NO\_MEMORY](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

### HMS\_FAST\_PerfHintConfig\_Destroy()

```c
void HMS_FAST_PerfHintConfig_Destroy (HMS_FAST_PerfHintConfig* config)
```

**描述**

销毁系统性能优化配置参数。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 配置参数实例指针。 |

### HMS\_FAST\_SchedulingOptimization\_PerfHint()

```c
HMS_FAST_SchedulingOptimization_ErrorCode HMS_FAST_SchedulingOptimization_PerfHint (const HMS_FAST_PerfHintConfig* config)
```

**描述**

系统性能优化接口。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| config | 指向系统性能优化配置参数的指针。 |

**返回：**

当成功时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当系统高负载时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_HIGH\_SYSTEM\_LOAD](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当省电模式时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_POWER\_SAVING\_MODE](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当低电量模式时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_LOW\_POWER\_MODE](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当非前台调用场景时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NON\_FRONTEND](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当间隔不满足要求时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INTERVAL](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当执行系统性能优化失败时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_EXECUTE\_ERROR](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。

当参数无效时，返回[HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode)。
