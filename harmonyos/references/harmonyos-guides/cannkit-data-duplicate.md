---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-duplicate
title: Duplicate
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 数据填充 > Duplicate
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:b8bd936f71d74b499141f72ef839d420e1bc23d399991cf6ca88938e7b9bea84
---

## 功能说明

将一个变量或一个立即数，复制多次并填充到向量，其中PAR表示矢量计算单元一个迭代能够处理的元素个数：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/MeXH-rDcTOawSws9GGRLFg/zh-cn_image_0000002736314447.png)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T> 
void Duplicate(const LocalTensor<T>& dstLocal, const T& scalarValue, const int32_t& calCount)
```

## 参数说明

**表1** 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：uint8、int8、uint16\_t、int16\_t、half、uint32\_t、int32\_t、float16、float。 |
| scalarValue | 输入 | 被复制的源操作数，支持输入变量和立即数，数据类型需与dstLocal中元素的数据类型保持一致。 |
| calCount | 输入 | 输入数据元素个数。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 开发者输入立即数需自行保证不超出dstLocal中元素数据类型对应的大小范围。

## 返回值

无

## 调用示例

本样例中只展示Compute流程中的部分代码。如果开发者需要运行样例代码，请将该代码段拷贝并替换[样例模板](cannkit-data-duplicate.md#样例模板)中的Compute函数粗体部分即可。

tensor前n个数据计算样例：

```cpp
half inputVal(18.0);
AscendC::Duplicate<half>(dstLocal, inputVal, srcDataSize);
```

结果示例如下。

```text
输入数据：[0 1.0 2.0 ... 254.0 255.0]    // 不关心输入数据，会被Duplicate盖掉
输出数据：[18.0 18.0 18.0 ... 18.0 18.0]
```

## 样例模板

```cpp
#include "kernel_operator.h"
 class KernelDuplicate {
 public:
     __aicore__ inline KernelDuplicate() {}
     __aicore__ inline void Init(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
     {
         srcGlobal.SetGlobalBuffer((__gm__ half*)src);
         dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
         pipe.InitBuffer(inQueueSrc, 1, srcDataSize * sizeof(half));
         pipe.InitBuffer(outQueueDst, 1, dstDataSize * sizeof(half));
     }
     __aicore__ inline void Process()
     {
         CopyIn();
         Compute();
         CopyOut();
     }
 private:
     __aicore__ inline void CopyIn()
     {
         AscendC::LocalTensor<half> srcLocal = inQueueSrc.AllocTensor<half>();
         AscendC::DataCopy(srcLocal, srcGlobal, srcDataSize);
         inQueueSrc.EnQue(srcLocal);
     }
     __aicore__ inline void Compute()
     {
         AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
         AscendC::LocalTensor<half> dstLocal = outQueueDst.AllocTensor<half>();
         **half inputVal(18.0);**
         **AscendC::Duplicate<half>(dstLocal, inputVal, srcDataSize);**
         outQueueDst.EnQue<half>(dstLocal);
         inQueueSrc.FreeTensor(srcLocal);
     }
     __aicore__ inline void CopyOut()
     {
         AscendC::LocalTensor<half> dstLocal = outQueueDst.DeQue<half>();
         AscendC::DataCopy(dstGlobal, dstLocal, dstDataSize);
         outQueueDst.FreeTensor(dstLocal);
     }
 private:
     AscendC::TPipe pipe;
     AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
     AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
     AscendC::GlobalTensor<half> srcGlobal, dstGlobal;
     int srcDataSize = 256;
     int dstDataSize = 256;
 };
 extern "C" __global__ __aicore__ void duplicate_kernel(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
 {
     KernelDuplicate op;
     op.Init(src, dstGm);
     op.Process();
 }
```
