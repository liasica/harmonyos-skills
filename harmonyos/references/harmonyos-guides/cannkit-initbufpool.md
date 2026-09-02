---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-initbufpool
title: InitBufPool
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBufPool > InitBufPool
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:fc70720a2ee9a52ae905eda6d1f88b482a3ff04b2ef4866e9de1738225e39ea3
---

## 功能说明

通过Tpipe::InitBufPool接口可划分出整块资源，整块TBufPool资源可以继续通过TBufPool::InitBufPool接口划分成小块资源。

## 函数原型

```cpp
template <class T> 
__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len)
template <class T, class U> 
__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len, U& shareBuf)
```

## 参数说明

**表1** InitBufPool(T& bufPool, uint32\_t len) 原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| bufPool | 输入 | 新划分的资源池，类型为TBufPool。 |
| len | 输入 | 新划分资源池长度，单位为Byte，非32Bytes对齐会自动向上补齐至32Bytes对齐。 |

**表2** InitBufPool(T& bufPool, uint32\_t len, U& shareBuf) 原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| bufPool | 输入 | 新划分的资源池，类型为TBufPool。 |
| len | 输入 | 新划分资源池长度，单位为Byte，非32Bytes对齐会自动向上补齐至32Bytes对齐。 |
| shareBuf | 输入 | 被复用资源池，类型为TBufPool，新划分资源池与被复用资源池共享起始地址及长度。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 新划分的资源池与被复用资源池的物理内存需要一致，两者共享起始地址及长度。
* 输入长度需要小于等于被复用资源池长度。
* 其他泛用约束参考[InitBufPool](cannkit-initbufpool.md)。

## 返回值

无

## 调用示例

数据量较大且内存有限时，无法一次完成所有数据搬运，需要拆分成多个阶段计算，每次计算使用其中的一部分数据，可以通过TBufPool资源池进行内存地址复用。本例中，从Tpipe划分出资源池tbufPool0，tbufPool0为src0Gm分配空间后，继续分配了资源池tbufPool1，指定tbufPool1与tbufPool2复用并分别运用于第一、二轮计算，此时tbufPool1及tbufPool2共享起始地址及长度。

```cpp
class ResetApi {
public:
    __aicore__ inline ResetApi() {}
    __aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        src0Global.SetGlobalBuffer((__gm__ half*)src0Gm);
        src1Global.SetGlobalBuffer((__gm__ half*)src1Gm);
        dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
        pipe.InitBufPool(tbufPool0, 131072);
        tbufPool0.InitBuffer(srcQue0, 1, 65536); // Total src0
        tbufPool0.InitBufPool(tbufPool1, 65536);
        tbufPool0.InitBufPool(tbufPool2, 65536, tbufPool1);
    }
    __aicore__ inline void Process()
    {
        tbufPool1.InitBuffer(srcQue1, 1, 32768);
        tbufPool1.InitBuffer(dstQue0, 1, 32768);
        CopyIn();
        Compute();
        CopyOut();
        tbufPool1.Reset();
        tbufPool2.InitBuffer(srcQue2, 1, 32768);
        tbufPool2.InitBuffer(dstQue1, 1, 32768);
        CopyIn1();
        Compute1();
        CopyOut1();
        tbufPool2.Reset();
        tbufPool0.Reset();
        pipe.Reset();
    }
private:
    __aicore__ inline void CopyIn()
    {
        AscendC::LocalTensor<half> src0Local = srcQue0.AllocTensor<half>();
        AscendC::LocalTensor<half> src1Local = srcQue1.AllocTensor<half>();
        AscendC::DataCopy(src0Local, src0Global, 16384);
        AscendC::DataCopy(src1Local, src1Global, 16384);
        srcQue0.EnQue(src0Local);
        srcQue1.EnQue(src1Local);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> src0Local = srcQue0.DeQue<half>();
        AscendC::LocalTensor<half> src1Local = srcQue1.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = dstQue0.AllocTensor<half>();
        AscendC::Add(dstLocal, src0Local, src1Local, 16384);
        dstQue0.EnQue<half>(dstLocal);
        srcQue0.FreeTensor(src0Local);
        srcQue1.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<half> dstLocal = dstQue0.DeQue<half>();
        AscendC::DataCopy(dstGlobal, dstLocal, 16384);
        dstQue0.FreeTensor(dstLocal);
    }
    __aicore__ inline void CopyIn1()
    {
        AscendC::LocalTensor<half> src0Local = srcQue0.AllocTensor<half>();
        AscendC::LocalTensor<half> src1Local = srcQue2.AllocTensor<half>();
        AscendC::DataCopy(src0Local, src0Global[16384], 16384);
        AscendC::DataCopy(src1Local, src1Global[16384], 16384);
        srcQue0.EnQue(src0Local);
        srcQue2.EnQue(src1Local);
    }
    __aicore__ inline void Compute1()
    {
        AscendC::LocalTensor<half> src0Local = srcQue0.DeQue<half>();
        AscendC::LocalTensor<half> src1Local = srcQue2.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = dstQue1.AllocTensor<half>();
        AscendC::Add(dstLocal, src0Local, src1Local, 16384);
        dstQue1.EnQue<half>(dstLocal);
        srcQue0.FreeTensor(src0Local);
        srcQue2.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut1()
    {
        AscendC::LocalTensor<half> dstLocal = dstQue1.DeQue<half>();
        AscendC::DataCopy(dstGlobal[16384], dstLocal, 16384);
        dstQue1.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TBufPool<AscendC::TPosition::VECCALC> tbufPool0, tbufPool1, tbufPool2;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> srcQue0, srcQue1, srcQue2;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> dstQue0, dstQue1;
    AscendC::GlobalTensor<half> src0Global, src1Global, dstGlobal;
};
extern "C" __global__ __aicore__ void tbufpool_kernel(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
{
    ResetApi op;
    op.Init(src0Gm, src1Gm, dstGm);
    op.Process();
}
```
