---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-initbufpool
title: InitBufPool
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPipe > InitBufPool
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:f4a01249934c1f807fb9af50c9a7e4810c854b356162c6c86d001cefc188c671
---

## 功能说明

初始化TBufPool内存资源池。本接口适用于内存资源有限时，希望手动指定UB/L1内存资源复用的场景。本接口初始化后在整体内存资源中划分出一块子资源池。划分出的子资源池TBufPool，提供了如下方式进行资源管理：

* TPipe::InitBufPool的重载接口指定与其他TBufPool子资源池复用。
* TBufPool::InitBufPool接口对子资源池继续划分。
* TBufPool::InitBuffer接口分配Buffer。

关于TBufPool的具体介绍及资源划分图示请参考[TBufPool](cannkit-tbufpool-overview.md)。

## 函数原型

```cpp
template <class T> 
__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len)
template <class T, class U> 
__aicore__ inline bool InitBufPool(T& bufPool, uint32_t len, U& shareBuf)
```

## 参数说明

表1 InitBufPool(T& bufPool, uint32\_t len) 原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| bufPool | 输入 | 新划分的资源池，类型为TBufPool。 |
| len | 输入 | 新划分资源池长度，单位为Byte，非32Bytes对齐会自动补齐至32Bytes对齐。 |

表2 InitBufPool(T& bufPool, uint32\_t len, U& shareBuf)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| bufPool | 输入 | 新划分的资源池，类型为TBufPool。 |
| len | 输入 | 新划分资源池长度，单位为Byte，非32Bytes对齐会自动补齐至32Bytes对齐。 |
| shareBuf | 输入 | 被复用资源池，类型为TBufPool，新划分资源池与被复用资源池共享起始地址及长度。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 新划分的资源池与被复用资源池的硬件属性需要一致，两者共享起始地址及长度。
* 输入长度需要小于等于被复用资源池长度。
* 其他泛用约束参考[TBufPool](cannkit-tbufpool-overview.md)。

## 返回值

无

## 调用示例

由于物理内存的大小有限，在计算过程没有数据依赖的场景或数据依赖串行、没有内存踩踏的场景下，可以通过指定内存复用解决资源不足的问题。本示例中Tpipe::InitBufPool初始化子资源池tbufPool1，并且指定tbufPool2复用tbufPool1的起始地址及长度。tbufPool1及tbufPool2的后续计算串行，不存在数据踩踏，实现了内存复用及自动同步的能力。

```cpp
#include "kernel_operator.h"
class ResetApi {
public:
    __aicore__ inline ResetApi() {}
    __aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        src0Global.SetGlobalBuffer((__gm__ half*)src0Gm);
        src1Global.SetGlobalBuffer((__gm__ half*)src1Gm);
        dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
        pipe.InitBufPool(tbufPool1, 196608);
        pipe.InitBufPool(tbufPool2, 196608, tbufPool1);
    }
    __aicore__ inline void Process()
    {
        tbufPool1.InitBuffer(queSrc0, 1, 65536);
        tbufPool1.InitBuffer(queSrc1, 1, 65536);
        tbufPool1.InitBuffer(queDst0, 1, 65536);
        CopyIn();
        Compute();
        CopyOut();
        tbufPool1.Reset();
        tbufPool2.InitBuffer(queSrc2, 1, 65536);
        tbufPool2.InitBuffer(queSrc3, 1, 65536);
        tbufPool2.InitBuffer(queDst1, 1, 65536);
        CopyIn1();
        Compute1();
        CopyOut1();
        tbufPool2.Reset();
    }
private:
    __aicore__ inline void CopyIn()
    {
        AscendC::LocalTensor<half> src0Local = queSrc0.AllocTensor<half>();
        AscendC::LocalTensor<half> src1Local = queSrc1.AllocTensor<half>();
        AscendC::DataCopy(src0Local, src0Global, 512);
        AscendC::DataCopy(src1Local, src1Global, 512);
        queSrc0.EnQue(src0Local);
        queSrc1.EnQue(src1Local);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> src0Local = queSrc0.DeQue<half>();
        AscendC::LocalTensor<half> src1Local = queSrc1.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = queDst0.AllocTensor<half>();
        AscendC::Add(dstLocal, src0Local, src1Local, 512);
        queDst0.EnQue<half>(dstLocal);
        queSrc0.FreeTensor(src0Local);
        queSrc1.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<half> dstLocal = queDst0.DeQue<half>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        queDst0.FreeTensor(dstLocal);
    }
    __aicore__ inline void CopyIn1()
    {
        AscendC::LocalTensor<half> src0Local = queSrc2.AllocTensor<half>();
        AscendC::LocalTensor<half> src1Local = queSrc3.AllocTensor<half>();
        AscendC::DataCopy(src0Local, src0Global, 512);
        AscendC::DataCopy(src1Local, src1Global, 512);
        queSrc2.EnQue(src0Local);
        queSrc3.EnQue(src1Local);
    }
    __aicore__ inline void Compute1()
    {
        AscendC::LocalTensor<half> src0Local = queSrc2.DeQue<half>();
        AscendC::LocalTensor<half> src1Local = queSrc3.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = queDst1.AllocTensor<half>();
        AscendC::Add(dstLocal, src0Local, src1Local, 512);
        queDst1.EnQue<half>(dstLocal);
        queSrc2.FreeTensor(src0Local);
        queSrc3.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut1()
    {
        AscendC::LocalTensor<half> dstLocal = queDst1.DeQue<half>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        queDst1.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TBufPool<AscendC::TPosition::VECCALC> tbufPool1, tbufPool2;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> queSrc0, queSrc1, queSrc2, queSrc3;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> queDst0, queDst1;
    AscendC::GlobalTensor<half> src0Global, src1Global, dstGlobal;
};
extern "C" __global__ __aicore__ void tbufpool_kernel(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
{
    ResetApi op;
    op.Init(src0Gm, src1Gm, dstGm);
    op.Process();
}
```
