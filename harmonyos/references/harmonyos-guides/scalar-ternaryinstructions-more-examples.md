---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scalar-ternaryinstructions-more-examples
title: 更多样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 标量三目指令 > 更多样例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:cfd63c9e0101216bcf19ba80c689d1dbf0ee4e005e12bbfd83dfa938fa71bdb5
---

## 样例模板

为了方便开发者快速运行具体指令中的参考样例，本章节提供标量三目指令的样例模板。

开发者可以将以下样例模板作为代码框架，只需将具体指令中的样例片段拷贝替换下文代码段中的加粗内容即可。

```cpp
// 完整样例一、half精度组合
#include "kernel_operator.h"
class KernelAxpy {
public:
    __aicore__ inline KernelAxpy() {}
    __aicore__ inline void Init(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
    {
        srcGlobal.SetGlobalBuffer((__gm__ half*)srcGm);
        dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
        pipe.InitBuffer(inQueueSrc, 1, 512 * sizeof(half));
        pipe.InitBuffer(outQueueDst, 1, 512 * sizeof(half));
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
        AscendC::DataCopy(srcLocal, srcGlobal, 512);
        inQueueSrc.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = outQueueDst.AllocTensor<half>();
  
        **AscendC::Axpy(dstLocal, srcLocal, (half)2.0, 512);**
  
        outQueueDst.EnQue<half>(dstLocal);
        inQueueSrc.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<half> dstLocal = outQueueDst.DeQue<half>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<half> srcGlobal, dstGlobal;
};
extern "C" __global__ __aicore__ void kernel_vec_ternary_scalar_Axpy_half_2_half(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
{
    KernelAxpy op;
    op.Init(srcGm, dstGm);
    op.Process();
}
// 输入数据(src1Gm):
// [1. 1. 1. 1. 1. 1. ... 1.]
// 输出数据(dstGm):
// [2. 2. 2. 2. 2. 2. ... 2.]
```

```cpp
// 完整样例二、mixed精度组合
#include "kernel_operator.h"
class KernelAxpy {
public:
    __aicore__ inline KernelAxpy() {}
    __aicore__ inline void Init(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
    {
        srcGlobal.SetGlobalBuffer((__gm__ half*)srcGm);
        dstGlobal.SetGlobalBuffer((__gm__ float*)dstGm);
        pipe.InitBuffer(outQueueDst, 1, 512 * sizeof(float));
        pipe.InitBuffer(inQueueSrc, 1, 512 * sizeof(half));
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
        AscendC::DataCopy(srcLocal, srcGlobal, 512);
        inQueueSrc.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
        AscendC::LocalTensor<float> dstLocal = outQueueDst.AllocTensor<float>();
  
        AscendC::Axpy(dstLocal, srcLocal, (half)2.0, 512);
  
        outQueueDst.EnQue<float>(dstLocal);
        inQueueSrc.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<float> dstLocal = outQueueDst.DeQue<float>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<half> srcGlobal;
    AscendC::GlobalTensor<float> dstGlobal;
};
extern "C" __global__ __aicore__ void kernel_vec_ternary_scalar_Axpy_half_2_float(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
{
    KernelAxpy op;
    op.Init(srcGm, dstGm);
    op.Process();
}
// 输入数据(src1Gm):
// [1. 1. 1. 1. 1. 1. ... 1.]
// 输出数据(dstGm):
// [2. 2. 2. 2. 2. 2. ... 2.]
```
