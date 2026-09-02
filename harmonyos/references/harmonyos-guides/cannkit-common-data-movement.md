---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-common-data-movement
title: 普通数据搬运
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 数据搬运 > DataCopy > 普通数据搬运
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:8dfa4ae9fee5d0c506837801a8d6f820c7bd60506a6a3cbbb65b98f69e3648a4
---

## 函数功能

普通数据搬运接口，适用于连续和不连续数据搬运。

## 函数原型

* 源操作数为GlobalTensor，目的操作数为LocalTensor

  ```cpp
  // 支持连续和不连续
  template <typename T> 
  __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const GlobalTensor<T>& srcGlobal, const DataCopyParams& repeatParams);
   
  // 支持连续
  template <typename T> 
  __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const GlobalTensor<T>& srcGlobal, const uint32_t calCount);
  ```

  该原型接口支持的数据通路和数据类型如下所示：

  **表1** 数据通路和数据类型（源操作数为GlobalTensor，目的操作数为LocalTensor）

  | 支持型号 | 数据通路（通过[TPosition](cannkit-tposition.md)章节中表1表达） | 源操作数和目的操作数的数据类型 (两者保持一致) |
  | --- | --- | --- |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | GM->L1 | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | GM->UB | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
* 源操作数和目的操作数都为LocalTensor

  ```cpp
  // 支持连续和不连续
   template <typename T> 
   __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcGlobal, const DataCopyParams& repeatParams);
    
   // 支持连续
   template <typename T> 
   __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcGlobal, const uint32_t calCount);
  ```

  该原型接口支持的数据通路和数据类型如下所示：

  **表2** 数据通路和数据类型（源操作数和目的操作数都为LocalTensor）

  | 支持型号 | 数据通路（通过[TPosition](cannkit-tposition.md)章节中表1表达） | 源操作数和目的操作数的数据类型 (两者保持一致) |
  | --- | --- | --- |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | L1->UB | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | L1->BT | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | L1->PT | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | L1->FB | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | UB->L1 | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
* 源操作数为LocalTensor，目的操作数为GlobalTensor

  ```cpp
  // 支持连续和不连续
  template <typename T> 
  __aicore__ inline void DataCopy(const GlobalTensor <T>& dstGlobal, const LocalTensor <T>& srcLocal, const DataCopyParams& repeatParams);
  // 支持连续
  template <typename T> 
  __aicore__ inline void DataCopy(const GlobalTensor <T>& dstGlobal, const LocalTensor <T>& srcLocal, const uint32_t calCount);
  ```

  该原型接口支持的数据通路和数据类型如下所示：

  **表3** 数据通路和数据类型（源操作数为LocalTensor，目的操作数为GlobalTensor）

  | 支持型号 | 数据通路（通过[TPosition](cannkit-tposition.md)章节中表1表达） | 源操作数和目的操作数的数据类型 (两者保持一致) |
  | --- | --- | --- |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | L1->GM | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器 | UB->GM | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
* 源操作数和目的操作数都为LocalTensor，支持源操作数和目的操作数类型不一致

  ```cpp
  template <typename dst_T, typename src_T> 
  __aicore__ inline void DataCopy(const LocalTensor<dst_T>& dstLocal, const LocalTensor<src_T>& srcLocal, const DataCopyParams& repeatParams);
  ```

## 参数说明

**表4** 普通数据搬运接口参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal，dstGlobal | 输出 | 目的操作数，类型为LocalTensor或GlobalTensor。**当dstLocal位于C2时，起始地址要求64B对齐；dstLocal位于C2PIPE2GM时，起始地址要求128B对齐；其他情况均为32字节对齐。** |
| srcLocal，srcGlobal | 输入 | 源操作数，类型为LocalTensor或GlobalTensor。 |
| repeatParams | 输入 | 搬运参数，DataCopyParams类型，定义如下，具体参数说明请参考表5。 |
| calCount | 输入 | 参与搬运的元素个数。  **说明：** DataCopy的搬运量要求为32byte的倍数，因此使用普通数据搬运接口（连续数据搬运，包含calCount参数）时，calCount \* sizeof(T)需要32byte对齐，若不对齐，搬运量将对32byte做向下取整。 |

**表5** DataCopyParams结构体参数定义

| 参数名称 | 含义 |
| --- | --- |
| blockCount | 指定该指令包含的连续传输数据块个数，取值范围：blockCount∈[1, 4095]。 |
| blockLen | 指定该指令每个连续传输数据块长度，单位为datablock(32Bytes)。取值范围：blockLen∈[1, 65535]。  特别的，当dstLocal位于C2PIPE2GM时，单位为128B；当dstLocal位于C2时，单位为64B。 |
| srcStride | 源操作数，相邻连续数据块的间隔（前面一个数据块的尾与后面数据块的头的间隔），单位为datablock(32Bytes)。数据类型为uint16\_t，srcStride不要超出该数据类型的取值范围。 |
| dstStride | 目的操作数，相邻连续数据块间的间隔（前面一个数据块的尾与后面数据块的头的间隔），单位为datablock(32Bytes)。数据类型为uint16\_t，dstStride不要超出该数据类型的取值范围。  特别的，当dstLocal位于C2PIPE2GM时，单位为128B；当dstLocal位于C2时，单位为64B。 |

下面的样例呈现了DataCopyParams结构体参数的使用方法，样例中完成了2个连续传输数据块的搬运，每个数据块含有8个datablock，源操作数相邻数据块之间无间隔，目的操作数相邻数据块尾与头之间间隔1个datablock。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/uErzIV1ySa-jcwgLsLXAEw/zh-cn_image_0000002706675404.png)

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* 硬件在执行数据搬运时会以datablock作为基本单位，而1 datablock = 32 Byte，故使用者可以尝试通过每次指令处理32Byte整数倍大小的数据来提高指令的执行效率。
* 如果执行多个DataCopy指令时，需确保DataCopy的目的地址不存在重叠。

## 调用示例

```cpp
#include "kernel_operator.h"
class KernelDataCopy {
public:
    __aicore__ inline KernelDataCopy() {}
    __aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        src0Global.SetGlobalBuffer((__gm__ half*)src0Gm);
        src1Global.SetGlobalBuffer((__gm__ half*)src1Gm);
        dstGlobal.SetGlobalBuffer((__gm__ half*)dstGm);
        pipe.InitBuffer(inQueueSrc0, 1, 512 * sizeof(half));
        pipe.InitBuffer(inQueueSrc1, 1, 512 * sizeof(half));
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
        AscendC::LocalTensor<half> src0Local = inQueueSrc0.AllocTensor<half>();
        AscendC::LocalTensor<half> src1Local = inQueueSrc1.AllocTensor<half>();
        AscendC::DataCopy(src0Local, src0Global, 512);
        AscendC::DataCopy(src1Local, src1Global, 512);
        inQueueSrc0.EnQue(src0Local);
        inQueueSrc1.EnQue(src1Local);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> src0Local = inQueueSrc0.DeQue<half>();
        AscendC::LocalTensor<half> src1Local = inQueueSrc1.DeQue<half>();
        AscendC::LocalTensor<half> dstLocal = outQueueDst.AllocTensor<half>();
        AscendC::Add(dstLocal, src0Local, src1Local, 512);
        outQueueDst.EnQue<half>(dstLocal);
        inQueueSrc0.FreeTensor(src0Local);
        inQueueSrc1.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<half> dstLocal = outQueueDst.DeQue<half>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc0, inQueueSrc1;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<half> src0Global, src1Global, dstGlobal;
};
extern "C" __global__ __aicore__ void data_copy_kernel(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
{
    KernelDataCopy op;
    op.Init(src0Gm, src1Gm, dstGm);
    op.Process();
}
```

结果示例：

```text
输入数据(src0Global): [1 2 3 ... 512]
输入数据(src1Global): [1 2 3 ... 512]
输出数据(dstGlobal):[2 4 6 ... 1024]
```
