---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-rect-partition
title: 使用RectPartition求解矩形划分
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用RectPartition求解矩形划分
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:46+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f7f648aee3ea6a6593cc920ac854ccdda65f810d4ae9701a3008cc8d2f4acd3a
---

矩形划分求解器（Rectangular Partition Solver）用于解决矩形划分问题。其接收若干个彼此不相交的矩形作为输入（主要关注这些矩形共同定义的区域的并集），计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少（但不保证最优）。形如下方示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ZL2ShhHCTeaS5Rhq5HuFpQ/zh-cn_image_0000002792877470.png?HW-CC-KV=V1&HW-CC-Date=20261121T011019Z&HW-CC-Expire=31536000000&HW-CC-Sign=F561C9401702FFB6FD1377002B355730110BD2A55479BC6E0FF57EA806F6B077)

其相关定义如下：一个矩形![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/YTHAsfLZQ72As65z1Y0qew/zh-cn_image_0000002821837377.png?HW-CC-KV=V1&HW-CC-Date=20261121T011019Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B3366EAAB33DEF9539B7EDD66B7FAAB2F7BE1547ABC6E2BB51F73B42C8A7F2C)为二维网格内横纵坐标满足![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/wJdefbgcQU-sLqXfKIHcow/zh-cn_image_0000002821757379.png?HW-CC-KV=V1&HW-CC-Date=20261121T011019Z&HW-CC-Expire=31536000000&HW-CC-Sign=22DACE4A08C3392DBCADD365C25E4FCECDE2CCB0035B519B4850E48AEF485A45)的所有单元矩形构成的集合（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。两个矩形相交，当且仅当它们共享至少一个公共的单元矩形。

在矩形划分问题（Rectangular Partition Problem）中，给定N个彼此不相交的矩形，要求输出M个矩形，使其满足如下几点：

* 输出的M个矩形彼此不相交。
* 输出的M个矩形的并集与输入的N个矩形的并集完全相同。
* 输出的矩形数量M尽可能少。

矩形划分求解器运行的时间复杂度为 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/SEzEjn4mRNmbevcz2XL7vQ/zh-cn_image_0000002793037442.png?HW-CC-KV=V1&HW-CC-Date=20261121T011019Z&HW-CC-Expire=31536000000&HW-CC-Sign=5416C6F3496D922EF0E38C427B92BB1CBFAC3DE5D7178DF84863BEF21D19C5F4)，可以高效处理大规模输入数据。在网格数据处理和空间几何计算等优化场景中，可以使用矩形划分求解器提升区域处理效率，减少冗余空间。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为。 |
| FAST\_EXPORT [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](../harmonyos-references/fast-kit-fast.md#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](../harmonyos-references/fast-kit-fast.md#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](../harmonyos-references/fast-kit--fast-rect.md) \*origin, [FAST\_Rect](../harmonyos-references/fast-kit--fast-rect.md) \*result, size\_t \*resultSize) | 在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。  **说明**：  1. 输入须保证矩形两两不相交（即任意两个矩形满足： 或 或或 ）。若输入的矩形不满足上述条件时，函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT错误码，表示输入参数非法。  2. 函数能保证输出矩形的数量小于等于输入矩形的数量。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
   find_library(
       lib_fast_solver
       NAMES fast_solver
   )
   target_link_libraries(entry PRIVATE ${lib_fast_solver})
   ```
2. 调用HMS\_FAST\_RectPartition\_CreateConfig生成矩形划分求解器配置实例（FAST\_RectPartitionConfig）。
3. 调用HMS\_FAST\_RectPartition\_SetAlgo设置求解算法为“SweepLineAlgo”（扫描线算法）。
4. 调用HMS\_FAST\_RectPartition\_Solve计算矩形划分方案。
5. 调用HMS\_FAST\_RectPartition\_DestroyConfig销毁矩形划分求解器配置实例。

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_solver_rect_partition.h"

// 定义一个函数来打印矩形
void print_rect(const FAST_Rect* rect) {
    printf("Rect: left=%d, top=%d, right=%d, bottom=%d\n",
           rect->left, rect->top, rect->right, rect->bottom);
}

FAST_ErrorCode rect_partition_demo() {
    // 定义输入矩形
    FAST_Rect origin[] = {
        {1, 4, 1, 6},
        {2, 1, 2, 6},
        {3, 1, 3, 3}
    };
    size_t size = sizeof(origin) / sizeof(FAST_Rect);

    // 定义输出矩形
    FAST_Rect* result = (FAST_Rect*)malloc(size * sizeof(FAST_Rect));
    size_t result_size = 0;

    FAST_RectPartitionConfig* config = nullptr;
    FAST_ErrorCode ret;

    do {
        // 创建配置
        ret = HMS_FAST_RectPartition_CreateConfig(&config);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to create config: %d\n", ret);
            break;
        }

        // 设置算法
        ret = HMS_FAST_RectPartition_SetAlgo(config, "SweepLineAlgo");
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to set algorithm: %d\n", ret);
            break;
        }

        // 计算矩形划分方案
        ret = HMS_FAST_RectPartition_Solve(config, size, origin, result, &result_size);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("Failed to solve: %d\n", ret);
            break;
        }

        // 打印结果
        printf("Resulting rectangles(result_size=%ld):\n", result_size);
        for (size_t i = 0; i < result_size; ++i) {
            print_rect(&result[i]);
        }
        /*
            Resulting rectangles(result_size=2):
            Rect: left=1, top=4, right=2, bottom=6
            Rect: left=2, top=1, right=3, bottom=3
         */

    } while (0);

    // 销毁配置
    HMS_FAST_RectPartition_DestroyConfig(config);

    // 释放数组
    free(result);

    return ret;
}
```
