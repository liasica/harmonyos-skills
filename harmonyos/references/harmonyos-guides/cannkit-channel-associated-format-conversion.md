---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-channel-associated-format-conversion
title: 随路格式转换
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 数据搬运 > DataCopy > 随路格式转换
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:437ef658008146157f2981ecd0cbbdc3ede07d020452861435c58466c8779b9e
---

## 功能说明

随路格式转换数据搬运，适用于在搬运时进行格式转换。

## 函数原型

* 源操作数为GlobalTensor，目的操作数为LocalTensor（只支持ND2NZ格式转换）

  ```
  1. template <typename T>
  2. __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const GlobalTensor<T>& srcGlobal, const Nd2NzParams& intriParams);
  ```

  该原型接口支持的数据通路和数据类型如下所示：

  **表1** 数据通路和数据类型（源操作数为GlobalTensor，目的操作数为LocalTensor）

  | 支持型号 | 数据通路 | 源操作数和目的操作数的数据类型 (两者保持一致) |
  | --- | --- | --- |
  | Kirin9020系列处理器 | GM->A1/B1 | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | KirinX90系列处理器 | GM->A1/B1 | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |

  说明

  使用该接口时需要预留8K的Unified Buffer空间，作为接口的临时数据存放区。
* 源操作数为LocalTensor，目的操作数为LocalTensor

  支持ND2NZ格式转换：

  ```
  1. // 支持ND2NZ格式转换
  2. template <typename T>
  3. __aicore__ inline void DataCopy(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcGlobal, const Nd2NzParams& intriParams);
  ```

  该原型接口支持的数据通路和数据类型如下所示：

  **表2** 数据通路和数据类型（源操作数为LocalTensor，目的操作数为LocalTensor）

  | 支持型号 | 数据通路 | 源操作数和目的操作数的数据类型 (两者保持一致) |
  | --- | --- | --- |
  | Kirin9020系列处理器 | VECIN / VECCALC / VECOUT -> TSCM | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |
  | KirinX90系列处理器 | VECIN / VECCALC / VECOUT -> TSCM | int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |

  说明

  当前Kirin9020通用核只考虑32Byte对齐的情形，后续根据需要增强接口。

## 参数说明

**表3** 接口参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal, dstGlobal | 输出 | 目的操作数，类型为LocalTensor或GlobalTensor。支持的数据类型为：half/int16\_t/uint16\_t/float/int32\_t/uint32\_t/int8\_t/uint8\_t。 |
| srcLocal, srcGlobal | 输入 | 源操作数，类型为LocalTensor或GlobalTensor。支持的数据类型为：half/int16\_t/uint16\_t/float/int32\_t/uint32\_t/int8\_t/uint8\_t。 |
| intriParams | 输入 | 搬运参数，类型为Nd2NzParams/Nz2NdParamsFull/DataCopyCO12DstParams。 |

**表4** Nd2NzParams结构体参数定义

| 参数名称 | 含义 |
| --- | --- |
| ndNum | 传输nd矩阵的数目，取值范围：ndNum∈[0, 4095]。 |
| nValue | nd矩阵的行数，取值范围：nValue∈[0, 16384]。 |
| dValue | nd矩阵的列数，取值范围：dValue∈[0, 65535]。 |
| srcNdMatrixStride | 源操作数相邻nd矩阵起始地址间的偏移，取值范围：srcNdMatrixStride∈[0, 65535]，单位：element。 |
| srcDValue | 源操作数同一nd矩阵的相邻行起始地址间的偏移，取值范围：srcDValue∈[1, 65535]，单位：element。 |
| dstNzC0Stride | ND转换到NZ格式后，源操作数中的一行会转换为目的操作数的多行。dstNzC0Stride表示，目的nz矩阵中，来自源操作数同一行的多行数据相邻行起始地址间的偏移，取值范围：dstNzC0Stride∈[1, 16384]，单位：C0\_SIZE（32B）。 |
| dstNzNStride | 目的nz矩阵中，Z型矩阵相邻行起始地址之间的偏移。取值范围：dstNzNStride∈[1, 16384]，单位：C0\_SIZE（32B）。 |
| dstNzMatrixStride | 目的nz矩阵中，相邻nz矩阵起始地址间的偏移，取值范围：dstNzMatrixStride∈[1, 65535]，单位：element。 |

ND2NZ转换示意图如下，样例中参数设置值和解释说明如下。

* ndNum = 2，表示传输nd矩阵的数目为2 (nd矩阵1为A1~A2 + B1~B2, nd矩阵2为C1~C2 + D1~D2)。
* nValue = 2，nd矩阵的行数，也就是矩阵的高度为2。
* dValue = 24，nd矩阵的列数，也就是矩阵的宽度为24个元素。
* srcNdMatrixStride = 144，表达相邻nd矩阵起始地址间的偏移，即为A1~C1的距离，即为9个datablock，9 \* 16 = 144个元素。
* srcDValue = 48，表示一行的所含元素个数，即为A1到B1的距离，即为3个datablock，3 \* 16 = 48个元素
* dstNzC0Stride = 11。ND转换到NZ格式后，源操作数中的一行会转换为目的操作数的多行，例如src中A1和A2为1行，dst中A1和A2被分为2行。多行数据起始地址之间的偏移就是A1和A2在dst中的偏移，偏移为11个datablock。
* dstNzNStride = 2，表达dst中一个ndMatrix, src的第x行和第x+1行之间的偏移，即A1和B1之间的距离，即为2个datablock。
* dstNzMatrixStride = 96，表达dst中第x个ndMatrix的起点和第x+1个ndMatrix的起点的偏移，即A1和C1之间的距离，即为6个datablock，6 \* 16 = 96个元素。

**图1** Nd2Nz转换示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/AhnVvZ7CQcWYhVrBGLE0Mw/zh-cn_image_0000002589245589.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=A05681CF375ABAB9EF643B875B93973060A5AEBD6406542F91E401A4EC6BCBA0)

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器
