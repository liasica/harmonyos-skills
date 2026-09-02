---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPipe > Init
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:6cff0fde5596d27b944db1058dbd95e8abf9d9c9d3a0f8d67d2dbc3bb155ad7e
---

## 功能说明

初始化内存和用于同步流水事件的EventID的初始化。

## 函数原型

```cpp
__aicore__ inline void TPipe::Init()
```

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

重复申请释放TPipe，要与[Destroy](cannkit-destroy.md)接口成对使用，TPipe如果要重复申请需要先Destroy释放后再Init。

## 返回值

无

## 调用示例

```cpp
template <typename srcType> 
class KernelAsin {
public:
    __aicore__ inline KernelAsin()
    {}
    __aicore__ inline void Init(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize, TPipe *pipe)
    {
        src_global.SetGlobalBuffer(reinterpret_cast<__gm__ srcType *>(src_gm), srcSize);
        dst_global.SetGlobalBuffer(reinterpret_cast<__gm__ srcType *>(dst_gm), srcSize);
        pipe->InitBuffer(inQueueX, 1, srcSize * sizeof(srcType));
        pipe->InitBuffer(outQueue, 1, srcSize * sizeof(srcType));
        bufferSize = srcSize;
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
        AscendC::LocalTensor<srcType> srcLocal = inQueueX.AllocTensor<srcType>();
        AscendC::DataCopy(srcLocal, src_global, bufferSize);
        inQueueX.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<srcType> dstLocal = outQueue.AllocTensor<srcType>();
        AscendC::LocalTensor<srcType> srcLocal = inQueueX.DeQue<srcType>();
        int16_t scalar_value = 3;
        AscendC::Muls(dstLocal, srcLocal, (srcType)scalar_value, bufferSize);
        outQueue.EnQue<srcType>(dstLocal);
        inQueueX.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut(uint32_t offset)
    {
        AscendC::LocalTensor<srcType> dstLocal = outQueue.DeQue<srcType>();
        AscendC::DataCopy(dst_global, dstLocal, bufferSize);
        outQueue.FreeTensor(dstLocal);
    }
private:
    AscendC::GlobalTensor<srcType> src_global;
    AscendC::GlobalTensor<srcType> dst_global;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueX;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueue;
    uint32_t bufferSize = 0;
};
template <typename dataType> 
__aicore__ void kernel_Test_operator(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize)
{
    KernelAsin<dataType> op;
    AscendC::TPipe pipeIn;
    for (uint32_t index =0; index < 1; index++) {
        if (index != 0) {
            pipeIn.Init();
        }
        op.Process();
        pipeIn.Destroy();
        AscendC::TPipe pipeCast;
        op.Init(src_gm, dst_gm, srcSize, &pipeCast);
        op.Process();
        pipeCast.Destroy();
    }
}
```
