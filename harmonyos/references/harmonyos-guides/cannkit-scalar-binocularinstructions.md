---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalar-binocularinstructions
title: 更多样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 标量双目指令 > 更多样例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:df4dac4adcb7ee80172f1ef04da75eacc9c291fee8b0ac44b1c26e69c54e75ac
---

## 样例模板

为了方便开发者快速运行具体指令中的参考样例，本章节提供标量双目指令的样例模板。

开发者可以将以下样例模板作为代码框架，只需将具体指令中的样例片段拷贝替换下文代码段中的加粗内容即可。

```cpp
#include "kernel_operator.h"
class KernelBinaryScalar {
public:
    __aicore__ inline KernelBinaryScalar() {}
    __aicore__ inline void Init(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
    {
        srcGlobal.SetGlobalBuffer((__gm__ int16_t*)src);
        dstGlobal.SetGlobalBuffer((__gm__ int16_t*)dstGm);
        pipe.InitBuffer(inQueueSrc, 1, 512 * sizeof(int16_t));
        pipe.InitBuffer(outQueueDst, 1, 512 * sizeof(int16_t));
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
        AscendC::LocalTensor<int16_t> srcLocal = inQueueSrc.AllocTensor<int16_t>();
        AscendC::DataCopy(srcLocal, srcGlobal, 512);
        inQueueSrc.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<int16_t> srcLocal = inQueueSrc.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.AllocTensor<int16_t>();
        **int16_t scalar = 2;**
        **AscendC::Adds(dstLocal, srcLocal, scalar, 512);**
         
        outQueueDst.EnQue<int16_t>(dstLocal);
        inQueueSrc.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.DeQue<int16_t>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<int16_t> srcGlobal, dstGlobal;
};
extern "C" __global__ __aicore__ void binary_scalar_simple_kernel(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
{
    KernelBinaryScalar op;
    op.Init(src, dstGm);
    op.Process();
}
```
