---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-rect-partition
title: 使用RectPartition求解矩形划分
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用RectPartition求解矩形划分
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05629a9fd6ba46a89aa0fd3eb53c98d22076cdd83a21d857888408d24c5a459e
---

矩形划分求解器（Rectangular Partition Solver）用于解决矩形划分问题。其接收若干个彼此不相交的矩形作为输入（主要关注这些矩形共同定义的区域的并集），计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少（但不保证最优）。形如下方示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/lr3O3oTvSey2i-JeRjRMeg/zh-cn_image_0000002558605294.png?HW-CC-KV=V1&HW-CC-Date=20260429T053319Z&HW-CC-Expire=86400&HW-CC-Sign=B9348E7F1756CD2E725DCAE9D453D1CF7B10D450C62353BAA769EEE06AA2908A)

其相关定义如下：一个矩形![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/rvPQh1vVTMqiAHtxu2MMQQ/zh-cn_image_0000002589324819.png?HW-CC-KV=V1&HW-CC-Date=20260429T053319Z&HW-CC-Expire=86400&HW-CC-Sign=30CE53C1889A4EAA5C1ACF1C37E10CF4E94A238918E8998464F6017CA7AD5A86)为二维网格内横纵坐标满足![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/jv4G9FF0R0KZ02kmXqL9aw/zh-cn_image_0000002589244757.png?HW-CC-KV=V1&HW-CC-Date=20260429T053319Z&HW-CC-Expire=86400&HW-CC-Sign=C7D873C0CB449550EDF2082E939CBC85AC460A276CCBC3CB5A0EEEEAE9B5780D)的所有单元矩形构成的集合（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。两个矩形相交，当且仅当它们共享至少一个公共的单元矩形。

在矩形划分问题（Rectangular Partition Problem）中，给定N个彼此不相交的矩形，要求输出M个矩形，使其满足如下几点：

* 输出的M个矩形彼此不相交。
* 输出的M个矩形的并集与输入的N个矩形的并集完全相同。
* 输出的矩形数量M尽可能少。

矩形划分求解器运行的时间复杂度为 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/QWeEaBJXSlytdALTBWbiqQ/zh-cn_image_0000002558764952.png?HW-CC-KV=V1&HW-CC-Date=20260429T053319Z&HW-CC-Expire=86400&HW-CC-Sign=285687EEA43D0485AC30330F0AB00FBB061F090CAEDD03862865204AB22F5E01)，可以高效处理大规模输入数据。在网格数据处理和空间几何计算等优化场景中，可以使用矩形划分求解器提升区域处理效率，减少冗余空间。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](../harmonyos-references/fast-kit--fast-rect.md) \*origin, [FAST\_Rect](../harmonyos-references/fast-kit--fast-rect.md) \*result, size\_t \*resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。  **说明**：  1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。  2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |

## 开发步骤

1. 首先在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC libfast_ads.so)
   ```
2. 调用HMS\_FAST\_RectPartition\_CreateConfig生成矩形划分求解器配置实例（FAST\_RectPartitionConfig）。
3. 调用HMS\_FAST\_RectPartition\_SetAlgo设置求解算法为“SweepLineAlgo”（扫描线算法）。
4. 调用HMS\_FAST\_RectPartition\_Solve计算矩形划分方案。
5. 调用HMS\_FAST\_RectPartition\_DestroyConfig销毁矩形划分求解器配置实例。

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_solver_rect_partition.h"

5. // 定义一个函数来打印矩形
6. void print_rect(const FAST_Rect* rect) {
7. printf("Rect: left=%d, top=%d, right=%d, bottom=%d\n",
8. rect->left, rect->top, rect->right, rect->bottom);
9. }

11. FAST_ErrorCode rect_partition_demo() {
12. // 定义输入矩形
13. FAST_Rect origin[] = {
14. {1, 4, 1, 6},
15. {2, 1, 2, 6},
16. {3, 1, 3, 3}
17. };
18. size_t size = sizeof(origin) / sizeof(FAST_Rect);

20. // 定义输出矩形
21. FAST_Rect* result = (FAST_Rect*)malloc(size * sizeof(FAST_Rect));
22. size_t result_size = 0;

24. FAST_RectPartitionConfig* config = nullptr;
25. FAST_ErrorCode ret;

27. do {
28. // 创建配置
29. ret = HMS_FAST_RectPartition_CreateConfig(&config);
30. if (ret != FAST_ERROR_CODE_SUCCESS) {
31. printf("Failed to create config: %d\n", ret);
32. break;
33. }

35. // 设置算法
36. ret = HMS_FAST_RectPartition_SetAlgo(config, "SweepLineAlgo");
37. if (ret != FAST_ERROR_CODE_SUCCESS) {
38. printf("Failed to set algorithm: %d\n", ret);
39. break;
40. }

42. // 计算矩形划分方案
43. ret = HMS_FAST_RectPartition_Solve(config, size, origin, result, &result_size);
44. if (ret != FAST_ERROR_CODE_SUCCESS) {
45. printf("Failed to solve: %d\n", ret);
46. break;
47. }

49. // 打印结果
50. printf("Resulting rectangles(result_size=%ld):\n", result_size);
51. for (size_t i = 0; i < result_size; ++i) {
52. print_rect(&result[i]);
53. }
54. /*
55. Resulting rectangles(result_size=2):
56. Rect: left=1, top=4, right=2, bottom=6
57. Rect: left=2, top=1, right=3, bottom=3
58. */

60. } while (0);

63. // 销毁配置
64. HMS_FAST_RectPartition_DestroyConfig(config);

66. // 释放数组
67. free(result);

69. return ret;
70. }
```
