---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkitvectorcalculation-binocularinstructions
title: 更多样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 双目指令 > 更多样例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:099dc7a8653bc48fafba56aeca4b5fa8960ed7b097782ca15beba62d523c1f94
---

## 样例模板

为了方便开发者快速运行具体指令中的参考样例，本章节提供双目指令的样例模板。

开发者可以将以下样例模板作为代码框架，只需将具体指令中的样例片段拷贝替换下文代码段中的加粗内容即可。

```cpp
#include "kernel_operator.h"
  
class KernelAdd {
public:
    __aicore__ inline KernelAdd() {}
    __aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        src0Global.SetGlobalBuffer((__gm__ int16_t*)src0Gm);
        src1Global.SetGlobalBuffer((__gm__ int16_t*)src1Gm);
        dstGlobal.SetGlobalBuffer((__gm__ int16_t*)dstGm);
        pipe.InitBuffer(inQueueSrc0, 1, 512 * sizeof(int16_t));
        pipe.InitBuffer(inQueueSrc1, 1, 512 * sizeof(int16_t));
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
        AscendC::LocalTensor<int16_t> src0Local = inQueueSrc0.AllocTensor<int16_t>();
        AscendC::LocalTensor<int16_t> src1Local = inQueueSrc1.AllocTensor<int16_t>();
        AscendC::DataCopy(src0Local, src0Global, 512);
        AscendC::DataCopy(src1Local, src1Global, 512);
        inQueueSrc0.EnQue(src0Local);
        inQueueSrc1.EnQue(src1Local);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<int16_t> src0Local = inQueueSrc0.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> src1Local = inQueueSrc1.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.AllocTensor<int16_t>();
  
        **AscendC::Add(dstLocal, src0Local, src1Local, 512);**
 
        outQueueDst.EnQue<int16_t>(dstLocal);
        inQueueSrc0.FreeTensor(src0Local);
        inQueueSrc1.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.DeQue<int16_t>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc0, inQueueSrc1;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<int16_t> src0Global, src1Global, dstGlobal;
};
  
extern "C" __global__ __aicore__ void add_simple_kernel(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
{
    KernelAdd op;
    op.Init(src0Gm, src1Gm, dstGm);
    op.Process();
}
```
