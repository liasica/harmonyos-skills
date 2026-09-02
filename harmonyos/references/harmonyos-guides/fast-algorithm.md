---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-algorithm
title: 使用Sort进行通用和自然语言排序
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用Sort进行通用和自然语言排序
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0787a2ef3e61f674d7497b9234a3b274dd1e0ca9457133cb746e2034152e67f3
---

从API版本26.0.0开始，FAST Kit提供Algorithm算法库用于通用数据类型的排序操作，支持任意类型的完整排序、部分排序以及自然语言字符串排序。

Algorithm算法库提供以下能力：

* **通用排序（HMS\_FAST\_Algo\_Sort）**：对任意数据类型的数组进行完整排序，通过用户提供的比较函数实现灵活的排序逻辑。
* **部分排序（HMS\_FAST\_Algo\_PartialSortAt）**：对数组进行原地部分排序，使指定区间[offset, offset + count)包含排序后对应位置的元素，适用于Top-K选择等场景。
* **自然语言排序（HMS\_FAST\_Algo\_NaturalSort）**：对UTF-8编码的C字符串数组进行自然语言排序，正确处理数字序列（如file1, file2, file10而非file1, file10, file2）。
* **自然语言部分排序（HMS\_FAST\_Algo\_NaturalPartialSortAt）**：结合自然语言排序与部分排序能力，高效获取排序后字符串数组的指定区间。

## 场景介绍

Algorithm算法库适用于以下场景：

* **通用排序**：

  + 数据预处理：对数值、浮点数等基础类型数据进行排序，为后续二分查找等操作做准备。
  + 自定义类型排序：通过自定义比较函数，对结构体、对象指针等复杂类型按特定字段排序。
  + 大规模数据排序：处理万级以上数据量的排序需求，提供稳定的排序性能。
* **部分排序**：

  + Top-K 问题：快速获取数组中最大或最小的K个元素，无需完全排序。
  + 中位数查找：通过部分排序定位中间位置元素。
  + 分位数计算：获取特定分位点的数据值。
* **自然语言排序**：

  + 文件列表排序：按自然顺序排序文件名（如file1.txt, file2.txt, file10.txt）。
  + 版本管理：对版本号字符串进行正确排序（如v1.0, v1.10, v2.0）。
  + 带编号资源排序：对img1, img2, img10等资源名称进行用户友好的排序。
  + 多语言文本排序：支持UTF-8编码的多语言文本自然排序。

## 基本概念

**SortData（排序数据描述符）**：描述待排序数据的结构，包含元素大小（sizeOf）、数组长度（length）和数据指针（data）三个字段，用于支持任意数据类型的排序。

**比较函数（Comparator）**：需要开发者自行提供的比较回调函数，接收两个元素指针，返回负数表示第一个元素小于第二个，零表示相等，正数表示第一个元素大于第二个。

**自然语言排序（Natural Sort）**：一种智能的字符串排序方式，将字符串中的数字序列视为数值进行比较，而非简单的字符逐个比较，使排序结果更符合人类直觉。

**部分排序（Partial Sort）**：仅保证指定区间内的元素处于完全排序后应有的位置，区间外的元素仅满足与区间内元素的大小关系，不进行完全排序。

## 约束与限制

### 支持的数据类型

* **通用排序**：支持任意数据类型，包括基础类型（int、double等）、结构体、指针等。
* **自然语言排序**：仅支持char\*类型的字符串数组，元素大小必须等于sizeof(char\*)。

### 内存要求

* 排序操作会在内部进行元素交换，需要可写的内存区域。
* 部分排序会修改原数组，传入的数组指针必须有效且可写。

### 比较函数要求

* 比较函数必须实现严格弱序（Strict Weak Ordering）。
* 比较函数不应修改传入的元素数据。
* 比较函数应保持确定性，相同输入始终返回相同结果。

## 接口说明

具体API使用说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_Sort](../harmonyos-references/fast-kit-fast.md#hms_fast_algo_sort) ([HMS\_FAST\_SortData](../harmonyos-references/fast-kit-fast.md#hms_fast_sortdata) \*data, [HMS\_FAST\_Sort\_CompFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 使用用户提供的比较函数对任意类型数组进行完整排序。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_PartialSortAt](../harmonyos-references/fast-kit-fast.md#hms_fast_algo_partialsortat) ([HMS\_FAST\_SortData](../harmonyos-references/fast-kit-fast.md#hms_fast_sortdata) \*data, size\_t offset, size\_t count, [HMS\_FAST\_Sort\_CompFunc](../harmonyos-references/fast-kit-fast.md#hms_fast_sort_compfunc) comp) | 对数组进行原地部分排序，使指定区间对应排序后的相应段。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalSort](../harmonyos-references/fast-kit-fast.md#hms_fast_algo_naturalsort) ([HMS\_FAST\_SortData](../harmonyos-references/fast-kit-fast.md#hms_fast_sortdata) \*data, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行排序。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Algo\_NaturalPartialSortAt](../harmonyos-references/fast-kit-fast.md#hms_fast_algo_naturalpartialsortat) ([HMS\_FAST\_SortData](../harmonyos-references/fast-kit-fast.md#hms_fast_sortdata) \*data, size\_t offset, size\_t count, int32\_t ascend) | 使用自然语言规则对UTF-8字符串数组进行部分排序，使指定区间对应排序后的相应段。 |

## 开发步骤

### 通用排序使用步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
   find_library(
       lib_fast_utils
       NAMES fast_utils
   )
   target_link_libraries(entry PRIVATE ${lib_fast_utils})
   ```
2. 定义比较函数。
3. 构造HMS\_FAST\_SortData结构体。
4. 调用HMS\_FAST\_Algo\_Sort进行排序。
5. 检查返回值确认排序是否成功。

```cpp
#include "FASTKit/fast_utils_algorithm.h"
#include <cstdio>
#include <cstdlib>

// 定义整数比较函数
static int compareInt(HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second) {
    int a = *static_cast<const int*>(first);
    int b = *static_cast<const int*>(second);
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 3, 7, 4, 6, 0};
    size_t length = sizeof(arr) / sizeof(arr[0]);
    
    HMS_FAST_SortData data = {sizeof(int), length, arr};
    
    FAST_ErrorCode ret = HMS_FAST_Algo_Sort(&data, compareInt);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Sorting failed with error code: %d\n", ret);
        return -1;
    }
    
    // 排序后：0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for (size_t i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
```

### 部分排序使用步骤

1. 定义比较函数（同通用排序）。
2. 构造HMS\_FAST\_SortData结构体。
3. 指定排序区间参数（offset和count）。
4. 调用HMS\_FAST\_Algo\_PartialSortAt进行部分排序。
5. 检查返回值确认操作是否成功。

```cpp
#include "FASTKit/fast_utils_algorithm.h"
#include <cstdio>

static int compareInt(HMS_FAST_SortElementConstPtr first, HMS_FAST_SortElementConstPtr second) {
    int a = *static_cast<const int*>(first);
    int b = *static_cast<const int*>(second);
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
}

int main() {
    int arr[] = {9, 4, 7, 1, 3, 8, 5, 6, 2, 0};
    size_t length = sizeof(arr) / sizeof(arr[0]);
    
    HMS_FAST_SortData data = {sizeof(int), length, arr};
    
    // 获取 arr[2] 开始的 3 个元素
    FAST_ErrorCode ret = HMS_FAST_Algo_PartialSortAt(&data, 2, 3, compareInt);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Partial sort failed with error code: %d\n", ret);
        return -1;
    }
    
    // 窗口内 3 个元素为：2, 3, 4（已排序）
    printf("Element 2~4: %d, %d, %d\n", arr[2], arr[3], arr[4]);
    
    return 0;
}
```

### 自然语言排序使用步骤

1. 构造HMS\_FAST\_SortData结构体（注意sizeOf必须为sizeof(char\*)）。
2. 指定排序方向（ascend：非零为升序，零为降序）。
3. 调用HMS\_FAST\_Algo\_NaturalSort进行自然语言排序。
4. 检查返回值确认排序是否成功。

```cpp
#include "FASTKit/fast_utils_algorithm.h"
#include <cstdio>

int main() {
    const char* arr[] = {"file10.txt", "file2.txt", "file1.txt", "file20.txt", "file3.txt"};
    size_t length = sizeof(arr) / sizeof(arr[0]);
    
    HMS_FAST_SortData data = {sizeof(char*), length, const_cast<char**>(arr)};
    
    // 升序排序
    FAST_ErrorCode ret = HMS_FAST_Algo_NaturalSort(&data, 1);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Natural sort failed with error code: %d\n", ret);
        return -1;
    }
    
    // 排序后：file1.txt, file2.txt, file3.txt, file10.txt, file20.txt
    for (size_t i = 0; i < length; i++) {
        printf("%s\n", arr[i]);
    }
    
    return 0;
}
```
