---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-createvecindex
title: CreateVecIndex
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 数据填充 > CreateVecIndex
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:70b83ca08ac3c9287d7d91de32467eeab982e6351e0cf4bfc55330fba94aef15
---

## 功能说明

以firstValue为起始值创建向量索引。

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T> 
__aicore__ inline void CreateVecIndex(LocalTensor<T> dstLocal, const T &firstValue, uint32_t calCount)
```

## 参数说明

**表1** 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：int8、int16、int32、float16、float。 |
| firstValue | 输入 | 索引的第一个数值，数据类型需与dstLocal中元素的数据类型保持一致。 |
| calCount | 输入 | 输入数据元素个数。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* firstValue需保证不超出dstLocal中元素数据类型对应的大小范围。

## 返回值

无

## 调用示例

本样例中只展示Compute流程中的部分代码。如果开发者需要运行样例代码，请将该代码段拷贝并替换[样例模板](cannkit-data-createvecindex.md#样例模板)中Compute函数相关代码片段即可。

tensor前n个数据计算样例：

```cpp
AscendC::CreateVecIndex(dstLocal, (T)0, 128);
```

结果示例如下。

```text
输入数据（firstValue）：0
输出数据（dstLocal）：[0 1 2 ... 127]
```

## 样例模板

```cpp
#include "kernel_operator.h"
template <typename T> 
class CreateVecIndexTest {
public:
    __aicore__ inline CreateVecIndexTest() {}
    __aicore__ inline void Init(GM_ADDR dstGm, uint64_t mask, uint8_t repeatTimes,
        uint16_t dstBlkStride, uint8_t dstRepStride)
    {
        m_mask = mask;
        m_repeatTimes = repeatTimes;
        m_dstBlkStride = dstBlkStride;
        m_dstRepStride = dstRepStride;
        m_elementCount = m_dstBlkStride * m_dstRepStride * 32 * m_repeatTimes / sizeof(T);
        m_dstGlobal.SetGlobalBuffer((__gm__ T*)dstGm);
        m_pipe.InitBuffer(m_queOut, 1, m_dstBlkStride * m_dstRepStride * 32 * m_repeatTimes);
        m_pipe.InitBuffer(m_queTmp, 1, 1024);
    }
    __aicore__ inline void Process()
    {
        // 无需CopyIn
        Compute();
        CopyOut();
    }
private:

    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<T> dstLocal = m_queOut.AllocTensor<T>();
        AscendC::LocalTensor<uint8_t> tmpLocal = m_queTmp.AllocTensor<uint8_t>();
        AscendC::Duplicate(dstLocal, (T)0, m_elementCount);
        AscendC::PipeBarrier<PIPE_ALL>();
        AscendC::CreateVecIndex(dstLocal, (T)0, m_repeatTimes * 256 / sizeof(T));
        m_queOut.EnQue(dstLocal);
        m_queTmp.FreeTensor(tmpLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<T> dstLocal = m_queOut.DeQue<T>();
 
        AscendC::DataCopy(m_dstGlobal, dstLocal, m_elementCount);
        m_queOut.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe m_pipe;
    uint32_t m_elementCount;
    uint32_t m_mask;
    uint32_t m_repeatTimes;
    uint32_t m_dstBlkStride;
    uint32_t m_dstRepStride;
    AscendC::GlobalTensor<T> m_dstGlobal;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> m_queOut;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> m_queTmp;
}; // class CreateVecIndexTest
template <typename T> 
__global__ __aicore__ void testCreateVecIndex(GM_ADDR dstGm, uint64_t mask, uint8_t repeatTimes,
        uint16_t dstBlkStride, uint8_t dstRepStride)
{
    CreateVecIndexTest<T> op;
    op.Init(dstGm, mask, repeatTimes, dstBlkStride, dstRepStride);
    op.Process();
}
```
