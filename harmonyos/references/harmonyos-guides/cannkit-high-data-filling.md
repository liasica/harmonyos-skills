---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-high-data-filling
title: 数据填充
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 数据填充
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fab7a4b24e869ba6834a675f6823f67a18b7fa7352a9a5868d5de4c9a7cfa964
---

## Broadcast

### 功能说明

将输入按照输出shape进行广播。

比如A的shape为(2,1)，广播的目标shape为(2,16)，则会将原来的一列扩展为相同的16列。

```
1. 输入数据：  [[ 1] [ 2]]
2. 输出数据：  [[ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1] [ 2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2]]
```

### 实现原理

以float类型，ND格式，[m, 1]广播到[m, k]为例，描述Broadcast高阶API内部算法框图，如下图所示。

**图1** Broadcast算法框图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/QicCiqfiTXCEgUW0UMZPqQ/zh-cn_image_0000002552799642.png?HW-CC-KV=V1&HW-CC-Date=20260427T235144Z&HW-CC-Expire=86400&HW-CC-Sign=CA698B847C79F5BA77571A0059010E2A2D2380EB9CB94BFE8C6089D5E622620A)

计算过程分为如下几步，均在Vector上进行：

1. Brcb步骤：将每个元素广播为一个datablock；
2. Copy步骤：将每个datablock均复制为多个datablock，k对齐场景下即为结果y；
3. 对于k非对齐的场景，再使用GatherMask截取[m, k]个元素， 其中k'表示k向上对齐32B的大小。

### 函数原型

* 通过sharedTmpBuffer入参传入临时空间

  ```
  1. template <typename T, int32_t dim, int32_t axis, bool isReuseSource = false>
  2. __aicore__ inline void Broadcast(const LocalTensor<T> &dstLocal, const LocalTensor<T> &srcLocal, const uint32_t dstShape[dim], const uint32_t srcShape[dim], LocalTensor<uint8_t> &sharedTmpBuffer)
  ```
* 接口框架申请临时空间

  ```
  1. template <typename T, int32_t dim, int32_t axis, bool isReuseSource = false>
  2. __aicore__ inline void Broadcast(const LocalTensor<T> &dstLocal, const LocalTensor<T> &srcLocal, const uint32_t dstShape[dim], const uint32_t srcShape[dim])
  ```

该接口需要额外的临时空间来存储计算过程中的中间变量。临时空间支持开发者通过sharedTmpBuffer入参传入和接口框架申请两种方式。

* 通过sharedTmpBuffer入参传入，使用该tensor作为临时空间进行处理，接口框架不再申请。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。
* 接口框架申请临时空间，开发者无需申请，但是需要预留临时空间的大小。

通过sharedTmpBuffer传入的情况，开发者需要为tensor申请空间；接口框架申请的方式，开发者需要预留临时空间。

### 参数说明

**表1** 模板参数说明

| 参数名称 | 功能 |
| --- | --- |
| T | 操作数的数据类型。支持的数据类型为：uint8\_t/int8\_t/half/float。 |
| dim | 输入/输出tensor的维度，目前仅支持1维和2维。 |
| axis | 要广播的维度，目前仅支持0和1。 |
| isReuseSource | 是否允许修改源操作数。该参数预留，传入默认值false即可。 |

**表2** 接口参数说明

| 参数名称 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。 |
| srcLocal | 输入 | 源操作数。  源操作数的数据类型需要与目的操作数保持一致。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。 |
| dstShape | 输入 | 输出tensor的shape：uint32\_t类型的数组，长度为1或者2， 输入/输出的shape维度数目必须一致。 |
| srcShape | 输入 | 输入tensor的shape：uint32\_t类型的数组，长度为1或者2， 输入/输出的shape维度数目必须一致。 |
| sharedTmpBuffer | 输入 | 临时缓存。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。  用于Broadcast内部复杂计算时存储中间变量，由开发者提供。 |

### 返回值

无

### 支持的型号

KirinX90系列处理器

### 约束说明

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 不支持源操作数与目的操作数地址重叠。
* 当前仅支持ND格式的输入，不支持其他格式。
* dim目前仅支持1或者2， axis目前仅支持0或者1。
* 对于Atlas推理系列产品AI Core，在dim=2，axis=1时，srcShape[0]必须为32B对齐。
* 在dim=2，axis=0时，要求srcShape[1]必须32B对齐。

### 调用示例

```
1. #include "kernel_operator.h"

3. template <typename T, int32_t dim, int32_t axis>
4. class KernelBroadcast {
5. public:
6. __aicore__ inline KernelBroadcast()
7. {}
8. __aicore__ inline void Init(
9. GM_ADDR srcGm, GM_ADDR dstGm, const uint32_t dstShape[dim], const uint32_t srcShape[dim])
10. {
11. for (uint32_t i = 0; i < dim; i++) {
12. srcSize *= srcShape[i];
13. dstSize *= dstShape[i];
14. }
15. srcGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ T *>(srcGm), srcSize);
16. dstGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ T *>(dstGm), dstSize);

18. pipe.InitBuffer(inQueueX, 1, srcSize * sizeof(T));
19. pipe.InitBuffer(outQueue, 1, dstSize * sizeof(T));
20. dstShape_ = dstShape;
21. srcShape_ = srcShape;
22. }
23. __aicore__ inline void Process()
24. {
25. CopyIn();
26. Compute();
27. CopyOut();
28. }

30. private:
31. __aicore__ inline void CopyIn()
32. {
33. AscendC::LocalTensor<T> srcLocal = inQueueX.AllocTensor<T>();
34. AscendC::DataCopy(srcLocal, srcGlobal, srcSize);
35. inQueueX.EnQue(srcLocal);
36. }
37. __aicore__ inline void Compute()
38. {
39. AscendC::LocalTensor<T> dstLocal = outQueue.AllocTensor<T>();
40. AscendC::LocalTensor<T> srcLocal = inQueueX.DeQue<T>();
41. AscendC::Broadcast<T, dim, axis>(dstLocal, srcLocal, dstShape_, srcShape_);

43. outQueue.EnQue<T>(dstLocal);
44. inQueueX.FreeTensor(srcLocal);
45. }
46. __aicore__ inline void CopyOut()
47. {
48. AscendC::LocalTensor<T> dstLocal = outQueue.DeQue<T>();
49. AscendC::DataCopy(dstGlobal, dstLocal, dstSize);
50. outQueue.FreeTensor(dstLocal);
51. }

53. private:
54. AscendC::GlobalTensor<T> srcGlobal;
55. AscendC::GlobalTensor<T> dstGlobal;

57. AscendC::TPipe pipe;
58. AscendC::TQue<AscendC::TPosition::VECIN, 1> inQueueX;
59. AscendC::TQue<AscendC::TPosition::VECOUT, 1> outQueue;
60. const uint32_t *dstShape_{nullptr};
61. const uint32_t *srcShape_{nullptr};
62. int32_t srcSize{1};
63. int32_t dstSize{1};
64. };

66. template <typename T, int32_t dim, int32_t axis>
67. __aicore__ void kernel_broadcast_operator(
68. GM_ADDR srcGm, GM_ADDR dstGm, const uint32_t dstShape[dim], const uint32_t srcShape[dim])
69. {
70. KernelBroadcast<T, dim, axis> op;
71. op.Init(srcGm, dstGm, dstShape, srcShape);
72. op.Process();
73. }
```

结果示例如下：

```
1. 输入数据（srcLocal）:
2. [[ 1] [ 2] [ 3] [ 4] [ 5] [ 6] [ 7] [ 8] [ 9] [10] [11] [12] [13] [14] [15] [16]]
3. dim：2
4. axis：1
5. 输出数据（dstLocal）:
6. [[ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1]
7. [ 2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2]
8. [ 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3]
9. [ 4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4]
10. [ 5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5]
11. [ 6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6]
12. [ 7  7  7  7  7  7  7  7  7  7  7  7  7  7  7  7]
13. [ 8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8]
14. [ 9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9]
15. [10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10]
16. [11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11]
17. [12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12]
18. [13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13]
19. [14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14]
20. [15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15]
21. [16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16]]
```
