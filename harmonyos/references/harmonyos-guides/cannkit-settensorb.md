---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settensorb
title: SetTensorB
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > SetTensorB
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:a1dcd850e4896ddbb297326b177a7d8b8678e0704504e7b88d2eb43af75218a6
---

## 功能说明

设置矩阵乘的右矩阵B。

## 函数原型

```cpp
__aicore__ inline void SetTensorB(const GlobalTensor<SrcBT>& gm, bool isTransposeB = false)
__aicore__ inline void SetTensorB(const LocalTensor<SrcBT>& rightMatrix, bool isTransposeB = false)
__aicore__ inline void SetTensorB(SrcBT bScalar)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| gm | 输入 | B矩阵在Global Memory上的首地址。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。 |
| rightMatrix | 输入 | B矩阵在TSCM上的首地址或者在VECOUT上的首地址。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。  若设置TSCM首地址，默认矩阵可全载，已经位于TSCM，Iterate接口无需再进行GM->A1/B1搬运。 |
| bScalar | 输入 | B矩阵中设置的值。支持传入标量数据，标量数据会被扩展为一个形状为[1, K]的tensor参与矩阵乘计算，tensor的数值均为该标量值。例如，开发者可以通过将bScalar设置为1来实现矩阵A在K方向的reduce sum操作。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。 |
| isTransposeB | 输入 | B矩阵是否需要转置。  **说明：**  - 若B矩阵MatmulType ISTRANS参数设置为true，此参数可以为true也可以为false，即运行时可以转置和非转置交替使用。  - 若B矩阵MatmulType ISTRANS参数设置为false，此参数只能设置为false，若强行设置为true，精度会有异常。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

传入的TensorB地址空间大小需要保证不小于singleK \* singleN。

## 调用示例

```cpp
REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);
mm.SetTensorA(gm_a);
mm.SetTensorB(gm_b); // 设置右矩阵B
mm.SetBias(gm_bias);
mm.IterateAll(gm_c);
```
