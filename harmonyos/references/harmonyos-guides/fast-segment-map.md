---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-segment-map
title: 使用SegmentMap查询维护区间信息
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用SegmentMap查询维护区间信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:878b703a3c6437800ad20210371b3fcc739524e36e730f704910a83fa5596c0a
---

FAST Kit提供Segment Map用于查询维护区间信息，实现数据序列区间段的快速更新和快速查询。线段表（Segment Map）是一种用于高效处理区间段信息的数据结构，适用于需要频繁对数据序列的某个区间段进行统计或修改的场景。其典型操作包括单点修改、区间修改、区间查询等。

线段表有多种实现方式，其中最常见的是使用二分树的方案，也被称为线段树（Segment Tree）。与直接遍历区间相比，线段表能将许多区间操作的时间复杂度从 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/NJDIWshZRCuKPnY0oWGogA/zh-cn_image_0000002583438495.png?HW-CC-KV=V1&HW-CC-Date=20260427T234426Z&HW-CC-Expire=86400&HW-CC-Sign=470DFBAB7D8F7CBE7CCE2D25F288844982EAC4255598992C48404C0097ABB22F) 优化至![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/GyyKlwFrTJOnovIYsZURTQ/zh-cn_image_0000002552958450.png?HW-CC-KV=V1&HW-CC-Date=20260427T234426Z&HW-CC-Expire=86400&HW-CC-Sign=210F14CDD6AE5130C78EEEC5187BB76684CBE24DB9FE032E3D682128DE1A3E4A)，在处理大规模数据时优势显著，为构建高性能、响应迅速的应用程序提供数据结构基础。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_CreateConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_createconfig) ([FAST\_SegmentMapConfig](../harmonyos-references/fast-kit-fast.md#fast_segmentmapconfig) \*\*config) | 创建线段表的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_destroyconfig) ([FAST\_SegmentMapConfig](../harmonyos-references/fast-kit-fast.md#fast_segmentmapconfig) \*config) | 销毁线段表的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetQueryType](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_setquerytype) ([FAST\_SegmentMapConfig](../harmonyos-references/fast-kit-fast.md#fast_segmentmapconfig) \*config, [FAST\_SegmentMapQueryType](../harmonyos-references/fast-kit-fast.md#fast_segmentmapquerytype-1) type) | 设置线段表不透明配置中的查询类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetUpdateType](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_setupdatetype) ([FAST\_SegmentMapConfig](../harmonyos-references/fast-kit-fast.md#fast_segmentmapconfig) \*config, [FAST\_SegmentMapUpdateType](../harmonyos-references/fast-kit-fast.md#fast_segmentmapupdatetype-1) type) | 设置线段表不透明配置中的更新类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Create](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_create) ([FAST\_SegmentMapHandle](../harmonyos-references/fast-kit-fast.md#fast_segmentmaphandle) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](../harmonyos-references/fast-kit-fast.md#fast_segmentmapconfig) \*config) | 创建线段表。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_destroy) ([FAST\_SegmentMapHandle](../harmonyos-references/fast-kit-fast.md#fast_segmentmaphandle) handle) | 销毁线段表实例，释放内存，再次调用为未定义行为。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Update](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_update) ([FAST\_SegmentMapHandle](../harmonyos-references/fast-kit-fast.md#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t value) | 更新线段表的区间，根据配置按照赋值、加法、减法等操作更新。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Query](../harmonyos-references/fast-kit-fast.md#hms_fast_segmentmap_query) ([FAST\_SegmentMapHandle](../harmonyos-references/fast-kit-fast.md#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t \*result) | 查询线段表的区间，根据配置返回最大值、最小值、求和等数据。 |

## 开发步骤

1. 首先在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC libfast_ads.so)
   ```
2. 调用HMS\_FAST\_SegmentMap\_CreateConfig生成线段表配置实例（FAST\_SegmentMapConfig）。
3. 调用HMS\_FAST\_SegmentMap\_SetQueryType设置查询类型。
4. 调用HMS\_FAST\_SegmentMap\_SetUpdateType设置更新类型。
5. 调用HMS\_FAST\_SegmentMap\_Create生成线段表实例 （FAST\_SegmentMapHandle）。生成实例之后，无法再修改查询和更新类型。
6. 调用HMS\_FAST\_SegmentMap\_Query进行高效区间查询操作。
7. 调用HMS\_FAST\_SegmentMap\_Update进行高效区间更新操作。
8. 调用HMS\_FAST\_SegmentMap\_Destroy销毁线段表实例。
9. 调用HMS\_FAST\_SegmentMap\_DestroyConfig销毁线段表配置实例。

```
1. #include <cassert>
2. #include <iostream>
3. #include "FASTKit/fast_ads_segment_map.h"

5. FAST_ErrorCode demoSegmentMapSumSet()
6. {
7. FAST_SegmentMapConfig *config = nullptr;
8. FAST_SegmentMapHandle handle = nullptr;
9. int32_t *array = nullptr;
10. FAST_ErrorCode ret;

12. ret = HMS_FAST_SegmentMap_CreateConfig(&config);
13. if (ret != FAST_ERROR_CODE_SUCCESS) {
14. return ret;
15. }

17. do {
18. // 初始化配置
19. ret = HMS_FAST_SegmentMap_SetQueryType(config, FAST_SEGMENTMAP_QUERY_TYPE_SUM);
20. if (ret != FAST_ERROR_CODE_SUCCESS) {
21. break;
22. }

24. ret = HMS_FAST_SegmentMap_SetUpdateType(config, FAST_SEGMENTMAP_UPDATE_TYPE_SET);
25. if (ret != FAST_ERROR_CODE_SUCCESS) {
26. break;
27. }

29. // 初始化数组
30. size_t size = 10;
31. array = new int32_t[size];
32. for (size_t i = 0; i < size; ++i) {
33. array[i] = i + 1;
34. }
35. // array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

37. // 创建线段表实例
38. ret = HMS_FAST_SegmentMap_Create(&handle, size, array, config);
39. // 线段表初始化为 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
40. if (ret != FAST_ERROR_CODE_SUCCESS) {
41. break;
42. }

44. int32_t result;

46. // 第一次查询：查询区间[0, 5)的求和值
47. ret = HMS_FAST_SegmentMap_Query(handle, 0, 5, &result);
48. if (ret != FAST_ERROR_CODE_SUCCESS) {
49. break;
50. }
51. assert(result == 15);  // 1 + 2 + 3 + 4 + 5 = 15

53. // 第一次更新：将区间[3, 7)的值设置为-1
54. ret = HMS_FAST_SegmentMap_Update(handle, 3, 7, -1);
55. if (ret != FAST_ERROR_CODE_SUCCESS) {
56. break;
57. }
58. // 线段表更新为 {1, 2, 3, -1, -1, -1, -1, 8, 9, 10}

60. // 第二次查询：查询区间[0, 5)的求和值
61. ret = HMS_FAST_SegmentMap_Query(handle, 0, 5, &result);
62. if (ret != FAST_ERROR_CODE_SUCCESS) {
63. break;
64. }
65. assert(result == 4);  // 1 + 2 + 3 - 1 - 1 = 4

67. // 第二次更新：将区间[5, 9)的值设置为2
68. ret = HMS_FAST_SegmentMap_Update(handle, 5, 9, 2);
69. if (ret != FAST_ERROR_CODE_SUCCESS) {
70. break;
71. }
72. // 线段表更新为 {1, 2, 3, -1, -1, 2, 2, 2, 2, 10}

74. // 第三次查询：查询区间[0, 10)的求和值
75. ret = HMS_FAST_SegmentMap_Query(handle, 0, 10, &result);
76. if (ret != FAST_ERROR_CODE_SUCCESS) {
77. break;
78. }
79. assert(result == 22);  // 1 + 2 + 3 -1 -1 + 2 + 2 + 2 + 2 + 10 = 22

81. // 第三次更新：将区间[0, 3)的值设置为0
82. ret = HMS_FAST_SegmentMap_Update(handle, 0, 3, 0);
83. if (ret != FAST_ERROR_CODE_SUCCESS) {
84. break;
85. }
86. // 线段表更新为 {0, 0, 0, -1, -1, 2, 2, 2, 2, 10}

88. // 第四次查询：查询区间[3, 7)的求和值
89. ret = HMS_FAST_SegmentMap_Query(handle, 3, 7, &result);
90. if (ret != FAST_ERROR_CODE_SUCCESS) {
91. break;
92. }
93. assert(result == 2);  // -1 -1 + 2 + 2 = 2

95. // 第四次更新：将区间[7, 10)的值设置为5
96. ret = HMS_FAST_SegmentMap_Update(handle, 7, 10, 5);
97. if (ret != FAST_ERROR_CODE_SUCCESS) {
98. break;
99. }
100. // 线段表更新为 {0, 0, 0, -1, -1, 2, 2, 5, 5, 5}

102. // 第五次查询：查询区间[0, 10)的求和值
103. ret = HMS_FAST_SegmentMap_Query(handle, 0, 10, &result);
104. if (ret != FAST_ERROR_CODE_SUCCESS) {
105. break;
106. }
107. assert(result == 17);  // 0 + 0 + 0 -1 -1 + 2 + 2 + 5 + 5 + 5 = 17
108. } while (0);

110. // 销毁线段表实例
111. HMS_FAST_SegmentMap_Destroy(handle);

113. // 销毁配置
114. HMS_FAST_SegmentMap_DestroyConfig(config);

116. // 释放数组
117. if (array) {
118. delete[] array;
119. }

121. return ret;
122. }
```
