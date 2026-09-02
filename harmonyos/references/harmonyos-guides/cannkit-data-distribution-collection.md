---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-distribution-collection
title: 数据分散/数据收集
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 数据分散/数据收集
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:06+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:7150f2e01f27381cd3ed33c96978f590464b3c7b95cc390a2bc4c6b33973e476
---

## Gather

### 功能说明

给定输入的张量和一个地址偏移张量，Gather指令根据偏移地址将输入张量按元素收集到结果张量中。

### 函数原型

tensor前n个数据计算：

```cpp
template <typename T> 
__aicore__ inline void Gather(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const LocalTensor<uint32_t>& srcOffsetLocal, const uint32_t srcBaseAddr, const uint32_t count)
```

### 参数说明

**表1** 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：  uint16\_t、int16\_t、uint32\_t、int32\_t、half、float32\_t。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  数据类型和dstLocal保持一致。 |
| srcOffsetLocal | 输入 | 每个元素在src中对应的地址偏移。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  该偏移量相对于src的起始基地址而言。单位为Bytes。地址偏移要大于等于0，取值应保证src元素类型位宽对齐，否则会导致非预期行为，同时需要保证偏移地址后不能超出UB大小数据的范围。  每个元素在src中对应的地址偏移，地址偏移要大于等于0。该偏移量是相对于src的基地址而言，每个数值的单位为Bytes，数据类型根据srcLocal数据类型决定，支持情况如下。  srcOffsetLocal支持数据类型：u32。 |
| srcBaseAddr | 输入 | srcLocal的起始基地址，单位为Bytes。取值应保证src元素类型位宽对齐，否则会导致非预期行为。 |
| count | 输入 | 执行处理的数据个数，不得超过srcLocal和srcOffsetLocal的元素个数。 |

### 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

### 约束说明

操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。

### 调用示例

```cpp
#include "kernel_operator.h"
template <typename T>
class GatherTest {
public:
    __aicore__ inline GatherTest() {}
    __aicore__ inline void Init(__gm__ uint8_t* dstGm, __gm__ uint8_t* srcGm,
        __gm__ uint8_t* srcOffsetGm, const uint32_t count)
    {
        m_elementCount = count;
        m_dstGlobal.SetGlobalBuffer((__gm__ T*)dstGm);
        m_srcGlobal.SetGlobalBuffer((__gm__ T*)srcGm);
        m_srcOffsetGlobal.SetGlobalBuffer((__gm__ uint32_t*)srcOffsetGm);
        m_pipe.InitBuffer(m_queIn, 2, m_elementCount * sizeof(uint32_t));
        m_pipe.InitBuffer(m_queOut, 2, m_elementCount * sizeof(uint32_t));
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
        AscendC::LocalTensor<T> srcLocal = m_queIn.AllocTensor<T>();
        AscendC::DataCopy(srcLocal, m_srcGlobal, m_elementCount);
        m_queIn.EnQue(srcLocal);
        AscendC::LocalTensor<uint32_t> srcOffsetLocal = m_queIn.AllocTensor<uint32_t>();
        AscendC::DataCopy(srcOffsetLocal, m_srcOffsetGlobal, m_elementCount);
        m_queIn.EnQue(srcOffsetLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<T> srcLocal = m_queIn.DeQue<T>();
        AscendC::LocalTensor<uint32_t> srcOffsetLocal = m_queIn.DeQue<uint32_t>();
        AscendC::LocalTensor<T> dstLocal = m_queOut.AllocTensor<T>();
        srcLocal.SetSize(m_elementCount);
        AscendC::Gather(dstLocal, srcLocal, srcOffsetLocal, (uint32_t)0, m_elementCount);
        m_queIn.FreeTensor(srcLocal);
        m_queIn.FreeTensor(srcOffsetLocal);
        m_queOut.EnQue(dstLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<T> dstLocal = m_queOut.DeQue<T>();
        AscendC::DataCopy(m_dstGlobal, dstLocal, m_elementCount);
        m_queOut.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe m_pipe;
    AscendC::TQue<AscendC::TPosition::VECIN, 1> m_queCalc;
    AscendC::GlobalTensor<T> m_valueGlobal;
    uint32_t m_concatRepeatTimes;
    uint32_t m_sortRepeatTimes;
    uint32_t m_extractRepeatTimes;
    uint32_t m_elementCount;
    AscendC::GlobalTensor<uint32_t> m_srcOffsetGlobal;
    AscendC::GlobalTensor<T> m_srcGlobal;
    AscendC::GlobalTensor<T> m_dstGlobal;
    AscendC::TQue<AscendC::TPosition::VECIN, 2> m_queIn;
    AscendC::TQue<AscendC::TPosition::VECOUT, 2> m_queOut;
}; // class GatherTest

extern "C" __global__ __aicore__ void kernel_gather(GM_ADDR dstGm, GM_ADDR srcGm, GM_ADDR srcOffsetGm)
{
    GatherTest<half> op;
    op.Init(dstGm, srcGm, srcOffsetGm, 128);
    op.Process();
}
```

结果示例：

```text
输入数据srcOffsetLocal:
[254 252 250 ... 4 2 0]
输入数据srcLocal（128个half类型数据）:
[0 1 2 ... 125 126 127]
输出数据dstGlobal:
[127 126 125 ... 2 1 0]
```
